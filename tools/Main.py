#!/bin/env python3
import argparse as ap
from urllib.parse import urlparse, parse_qs
from tools.Config import ScriptConfiguration
from tools.WMSLayerImporter import WMSLayerImporter
from tools.WFSLayerImporter import WFSLayerImporter
from tools.api.GeoserverApi import GeoserverAPI
from tools.api.models.Layer import Layer
from tools.PGMetadata import PGMetadata
from tools.domain.GdiDeServiceWMS import GdiDeServiceWMS
from configparser import ConfigParser
import json
import xmltodict
from tools.api.models.Common import KeyDollarListDict

import logging

# use INFO for production
# use DEBUG for development
logging.basicConfig(level=logging.DEBUG)
log = logging.Logger(__name__)

handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
log.addHandler(handler)




def parse_args()->ap.Namespace:
    """Parse the command line arguments"""
    # add an argument parser
    parser = ap.ArgumentParser(description='Tools for managing geoserver')
    # add config file argument
    parser.add_argument('--config', '-c', default = 'config.ini', help='Configuration file to use')
    # parse the arguments
    args = parser.parse_args()
    # create the config object
    return args

def load_config(args: ap.Namespace)->ScriptConfiguration:
    """"Load the configuration file"""
    config = ScriptConfiguration(args.config)
    return config



# todo
# - attributes
# - crs
# - bounding box
# - metadata url
# - abstract
# - inspire extended capabilities
# - LayerGroup

def convert_keys_to_lowercase(input_dict):
    return {key.lower(): value for key, value in input_dict.items()}

def rewrite_csw_id_url(url: str, config: ConfigParser, add_output_schema=True):
    parsed_url = urlparse(url)
    query_params = convert_keys_to_lowercase(parse_qs(parsed_url.query, keep_blank_values=True))

    new_query_params = {}
    for param, value in config['inspire'].items():
        if param != "host":
            new_query_params[param] = value
    new_query_params['id'] = query_params['id'][0]
    if not add_output_schema:
        del new_query_params['outputschema']
    params_string = "&".join([f"{key}={value}" for key, value in new_query_params.items()])        
    rewrited_url = f"{config['inspire']['host']}?{params_string}"
    # for the moment, just return the url
    return rewrited_url

def createWorkspace(geoserver: GeoserverAPI, workspace: str):
    geoserver.create_workspace(workspace)
    geoserver.update_namespace(workspace, workspace)
    
def activateWmsServices(geoserver: GeoserverAPI, workspace: str, config: ConfigParser,wms_importer: WMSLayerImporter):
    overrideMetadataEntries = {}
    try:
        # The identifier is not always available
        identifier = xmltodict.parse(wms_importer.wms.getServiceXML())['WMS_Capabilities']['Capability']['Layer']['Identifier']['#text']
    except:
        identifier = ""
        log.warning(f"Root layer identifier not found in {wms_importer.wms.getServiceXML()}")
    wmsService = GdiDeServiceWMS(
            workspace=workspace,
            config=config["wmsservice"],
            keywords=wms_importer.wms.identification.keywords,
            fees = wms_importer.wms.identification.fees,
            accessConstraints = wms_importer.wms.identification.accessconstraints,
            internationalAbstract = wms_importer.wms.identification.abstract,
            internationalTitle = wms_importer.wms.identification.title,
            overrideMetadataEntries = {
                "inspire.metadataURL": rewrite_csw_id_url(
                        wms_importer.inspireCapabilities["inspire_vs:ExtendedCapabilities"]["inspire_common:MetadataUrl"]["inspire_common:URL"],
                        config
                    )
                },
            identifier = identifier
        )
    
    
    geoserver.activate_wms_service(workspace, wmsService)
    
def activateWfsServices(geoserver: GeoserverAPI, workspace: str, config: ConfigParser, wfs_importer: WFSLayerImporter):
    # geoserver.activate_wfs_service(workspace)
    raise NotImplementedError
    
def createDatastore(geoserver: GeoserverAPI, workspace: str, datastore_name: str, config: ScriptConfiguration):
    postgisStoreDefaults = KeyDollarListDict(json.loads(config.defaults['wmsservice']['postgisDataStoreDefaults']))
    geoserver.create_datastore(
        workspace,
        datastore_name,
        postgisStoreDefaults,
        config.configParser['database']['host'],
        config.configParser['database']['port'],
        config.configParser['database']['database'],
        config.configParser['database']['username'],
        config.configParser['database']['password'],
        config.configParser['database']['schema']
        )
    #log.debug(geoserver.get_datastore(workspace, store_name=datastore_name))

def getLayerPostGisMetadata(config: ScriptConfiguration, schema_name: str, table_name: str):
    metadata = PGMetadata(
        schema_name,
        table_name,
        config.configParser['database']['host'],
        config.configParser['database']['port'],
        config.configParser['database']['database'],
        config.configParser['database']['username'],
        config.configParser['database']['password']
    )
    return metadata.getMetadata()

def createWmsLayer(
        geoserver: GeoserverAPI,
        workspace: str,
        datastore_name: str,
        layerName: str
        ):
    pass
    

def createLayers(
        geoserver: GeoserverAPI,
        workspace: str,
        datastore_name: str,
        config: ScriptConfiguration,
        inputWmsServer: WMSLayerImporter
    ):
    #log.debug(geoserver.list_layers(workspace))
    sublayers = json.loads(config.configParser['layer']['sublayers'])
    sublayers_list = []
    layergroup_name = config.configParser['layer']['layername']
    for sublayer, content in sublayers.items():
        layerName = f"{config.configParser['layer']['layername']}_{sublayer}"
        sublayers_list.append(layerName)
        tableName = content["table_name"]
        srs = content["srs"]
        style_name = f"{workspace}_{content['style_name']}"
        disabled_services = config.configParser['layer']['disabled_services'].split(",") if config.configParser['layer']['disabled_services'] else []
        log.debug(f"disabled_services={disabled_services}")
        geoserver.create_featuretype(
            workspace,
            datastore_name,
            layerName,
            tableName,
            srs,
            title = inputWmsServer.sublayers[sublayer].title,
            abstract = inputWmsServer.sublayers[sublayer].abstract,
            keywords = {"string": inputWmsServer.sublayers[sublayer].keywords},
            disabled_services = disabled_services,
            metadata_url = rewrite_csw_id_url(inputWmsServer.sublayers[sublayer].metadataUrls[0]['url'], config.defaults, add_output_schema=False),
            metadata_type = inputWmsServer.sublayers[sublayer].metadataUrls[0]['type'],
            metadata_format = inputWmsServer.sublayers[sublayer].metadataUrls[0]['format']
        )
        geoserver.create_style(
            workspace,
            style_name,
            content["style_file"]
        )
        log.debug(f"legend_url={inputWmsServer.sublayers[sublayer].styles['inspire_common:DEFAULT']['legend']}")
        log.debug(f"legend_format={inputWmsServer.sublayers[sublayer].styles['inspire_common:DEFAULT']['legend_format']}")
        geoserver.update_style_legend(
            workspace,
            style_name,
            content["style_file"],
            legend_url=inputWmsServer.sublayers[sublayer].styles['inspire_common:DEFAULT']['legend'],
            legend_format=inputWmsServer.sublayers[sublayer].styles['inspire_common:DEFAULT']['legend_format'],
            legend_width=inputWmsServer.sublayers[sublayer].styles['inspire_common:DEFAULT']['legend_width'],
            legend_height=inputWmsServer.sublayers[sublayer].styles['inspire_common:DEFAULT']['legend_height']
        )
        geoserver.update_style(
            workspace,
            style_name,
            content["style_file"]
        )
        geoserver.update_default_style(
            workspace,
            layerName,
            style_name
        )



    # geoserver.create_layergroup(
    #     workspace_name=workspace,
    #     layergroup_name=layergroup_name,
    #     layer_names=sublayers_list,
    #     internationalTitle={config.defaults['inspire']['default_language']: inputWmsServer.wms.contents[layergroup_name].title},
    #     internationalAbstract={config.defaults['inspire']['default_language']: inputWmsServer.wms.contents[layergroup_name].abstract},
    #     metadataLinksIdentifier=rewrite_csw_id_url(inputWmsServer.wms.contents[layergroup_name].metadataUrls[0]['url'], config.defaults),
    # )

def main():

    args = parse_args()
    config = load_config(args)
    
    inputWmsServer = WMSLayerImporter(
        config.configParser['fis_broker']['url'], 
        config.configParser['layer']['layername'],
        config.configParser['fis_broker']['wms_version']
        )
    log.debug(inputWmsServer)
    log.debug(inputWmsServer.getInspireExtendedCapabilitiesAsXml())
    geoserver = GeoserverAPI(
        config.configParser['geoserver']['geoserver_url'],
        config.configParser['geoserver']['geoserver_username'],
        config.configParser['geoserver']['geoserver_password']
        )

    workspace = config.configParser['layer']['workspace']
    createWorkspace(geoserver, workspace)
    activateWmsServices(geoserver, workspace, config.defaults, inputWmsServer)
    schema = config.configParser['database']['schema']
    datastore_name = f"pg_{schema}"
    createDatastore(geoserver, workspace, datastore_name, config)
    # 
    createLayers(geoserver, workspace, datastore_name, config, inputWmsServer)
    
    
    
# if main script
if __name__ == '__main__':
    main()

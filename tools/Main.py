#!/bin/env python3
import argparse as ap
from tools.Config import ScriptConfiguration
from tools.WMSLayerImporter import WMSLayerImporter
from tools.api.GeoserverApi import GeoserverAPI
from tools.PGMetadata import PGMetadata
import json

import logging

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
# - style
# - keywords
# - title
# - layer name
# - attributes
# - crs
# - bounding box
# - metadata url
# - abstract
# - inspire extended capabilities
# - table name
# - data store name

def createWorkspace(geoserver: GeoserverAPI, workspace: str):
    geoserver.create_workspace(workspace)
    
def createDatastore(geoserver: GeoserverAPI, workspace: str, datastore_name: str, config: ScriptConfiguration):

    geoserver.create_datastore(
        workspace,
        datastore_name,
        config.configParser['database']['host'],
        config.configParser['database']['port'],
        config.configParser['database']['database'],
        config.configParser['database']['username'],
        config.configParser['database']['password'],
        config.configParser['database']['schema']
        )
    #log.info(geoserver.get_datastore(workspace, store_name=datastore_name))

def getLayerMetadata(config: ScriptConfiguration, schema_name: str, table_name: str):
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
    try:
        existing_layers = geoserver.get_featuretypes(workspace)
    except AttributeError:
        existing_layers = []
    sublayers = json.loads(config.configParser['layer']['sublayers'])
    for sublayer, content in sublayers.items():
        layerName = f"{config.configParser['layer']['layername']}_{sublayer}"
        tableName = content["table_name"]
        srs = content["srs"]
        geoserver.create_featuretype(
            workspace,
            datastore_name,
            layerName,
            tableName,
            srs
        )
        geoserver.create_style(
            workspace,
            layerName,
            content["style_file"]
        )
        createWmsLayer(
            geoserver,
            workspace,
            datastore_name,
            layerName,
            tableName,
            srs,
            config,
            inputWmsServer
        )

       

def main():

    args = parse_args()
    config = load_config(args)
    # print(config.configParser.sections())
    
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
    schema = config.configParser['database']['schema']
    
    datastore_name = f"pg_{workspace}_{schema}"
    createDatastore(geoserver, workspace, datastore_name, config)
    # 
    createLayers(geoserver, workspace, datastore_name, config, inputWmsServer)
    
    
    
# if main script
if __name__ == '__main__':
    main()

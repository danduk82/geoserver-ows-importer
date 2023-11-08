#!/bin/env python3
import argparse as ap
from tools.Config import ScriptConfiguration
from tools.WMSLayerImporter import WMSLayerImporter
from tools.api.GeoserverApi import GeoserverAPI

import logging

logging.basicConfig(level=logging.INFO)
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

def main():

    args = parse_args()
    config = load_config(args)
    # print(config.configParser.sections())
    
    inputWmsServer = WMSLayerImporter(
        config.configParser['input_server']['url'], 
        config.configParser['layer']['layername'],
        config.configParser['input_server']['wms_version']
        )
    log.debug(inputWmsServer)
    log.debug(inputWmsServer.getInspireExtendedCapabilitiesAsXml())
    
    output_server = GeoserverAPI(
        config.configParser['output_server']['geoserver_url'],
        config.configParser['output_server']['geoserver_username'],
        config.configParser['output_server']['geoserver_password']
        )

    workspaces = output_server.list_workspaces()
    log.debug(workspaces)
    if config.configParser['output_server']['workspace'] not in workspaces:
        output_server.create_workspace(config.configParser['output_server']['workspace'])
    log.debug(output_server.list_workspaces())
    
    datastore_name = "something"
    # try:
    #     stores = output_server.list_datastores(config.configParser['output_server']['workspace'])
    # except ValueError:
    #     stores = []
    # if datastore_name not in stores:
    output_server.create_datastore(
        config.configParser['output_server']['workspace'],
        datastore_name,
        config.configParser['database']['host'],
        config.configParser['database']['port'],
        config.configParser['database']['database'],
        config.configParser['database']['username'],
        config.configParser['database']['password']
        )
    
    log.info(output_server.get_datastore(config.configParser['output_server']['workspace'], store_name=datastore_name))
    
    
    
# if main script
if __name__ == '__main__':
    main()

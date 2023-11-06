#!/bin/env python3
import argparse as ap
from Config import ScriptConfiguration
from WMSLayerImporter import WMSLayerImporter

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



def main():
    args = parse_args()
    config = load_config(args)
    print(config.configParser.sections())
    
    inputWmsServer = WMSLayerImporter(
        config.configParser['input_server']['url'], 
        config.configParser['layer']['layername'],
        config.configParser['input_server']['wms_version']
        )
    print(inputWmsServer)
    print(inputWmsServer.getInspireExtendedCapabilitiesAsXml())

# if main script
if __name__ == '__main__':
    main()

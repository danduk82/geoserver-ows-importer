from owslib.wfs import WebFeatureService
from lxml import etree
from .api.GeoserverApi import GeoserverAPI
import xmltodict
import json

import logging

import logging

log = logging.getLogger()

class WFSLayerImporter:
    def __init__(self, wfs_server_url: str, layerName: str, wfs_version='1.1.1') -> None:
        """[summary]
        Initialize the WMSLayerImporter class
        Input:
        - wfs_server_url: The URL of the WMS server
        - layerName: The name of the layer to import
        - wfs_version: The WMS version to use
        
        """
        wfs = WebFeatureService(wfs_server_url, version=wfs_version, timeout=60)
        self.crsOptions = wfs.contents[layerName].crsOptions
        self.boundingBox = wfs.contents[layerName].boundingBox
        self.boundingBoxWGS84 = wfs.contents[layerName].boundingBoxWGS84
        self.metadataUrls = wfs.contents[layerName].metadataUrls
        self.styles = wfs.contents[layerName].styles
        self.keywords = wfs.contents[layerName].keywords
        self.abstract = wfs.contents[layerName].abstract
        self.title = wfs.contents[layerName].title
        self.capabilities_xml = wfs.getServiceXML()
        self.inspireCapabilities = self.parseInspireExtendedCapabilities()

    def printKeysOfDict(myDict):
        for key in myDict.keys():
            print(key)
            
    def __repr__(self):
        # return all the attributes of the class as json
        output = {}
        output['crsOptions'] = self.crsOptions
        output['boundingBox'] = self.boundingBox
        output['boundingBoxWGS84'] = self.boundingBoxWGS84
        output['metadataUrls'] = self.metadataUrls
        output['styles'] = self.styles
        output['keywords'] = self.keywords
        output['abstract'] = self.abstract
        output['title'] = self.title
        output['inspireCapabilities'] = self.inspireCapabilities
        return json.dumps(output)
    
    def __str__(self):
        return self.__repr__()
    
    def parseInspireExtendedCapabilities(self):
        capabilities_tree = etree.fromstring(self.capabilities_xml)
        log.debug(etree.tostring(capabilities_tree).decode())
        
        # Define the namespace for INSPIRE elements
        namespaces={
            'inspire_vs': 'http://inspire.ec.europa.eu/schemas/inspire_vs/1.0',
            'inspire_common': 'http://inspire.ec.europa.eu/schemas/common/1.0'
        }
        # Find the inspire_vs:ExtendedCapabilities section
        extended_capabilities = capabilities_tree.find('.//inspire_vs:ExtendedCapabilities', namespaces=namespaces)
        # Find the inspire_common:MetadataUrl section (not needed for now)
        # metadata_url_elements = capabilities_tree.xpath('.//inspire_common:MetadataUrl', namespaces=namespaces['inspire_common'])
        try:
            return xmltodict.parse(etree.tostring(extended_capabilities))
        except:
            return None
        
    def getInspireExtendedCapabilities(self):
        return self.inspireCapabilities
    
    def getInspireExtendedCapabilitiesAsXml(self):
        return xmltodict.unparse(self.inspireCapabilities) #.split('\n', 1)[1]

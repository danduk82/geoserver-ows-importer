from owslib.wms import WebMapService
from owslib.wfs import WebFeatureService
from lxml import etree
from .api.GeoserverApi import GeoserverAPI
import xmltodict
import json

import logging

log = logging.getLogger()


class WMSLayerImporter:
    def __init__(self, wms_server_url: str, layerName: str, wms_version='1.3.0') -> None:
        """[summary]
        Initialize the WMSLayerImporter class
        Input:
        - wms_server_url: The URL of the WMS server
        - layerName: The name of the layer to import
        - wms_version: The WMS version to use
        
        """
        self.wms = WebMapService(wms_server_url, version=wms_version, timeout=60)
        self.layername = layerName
        self.crsOptions = self.wms.contents[layerName].crsOptions
        self.boundingBox = self.wms.contents[layerName].boundingBox
        self.boundingBoxWGS84 = self.wms.contents[layerName].boundingBoxWGS84
        self.metadataUrls = self.wms.contents[layerName].metadataUrls
        self.styles = self.wms.contents[layerName].styles
        self.keywords = self.wms.contents[layerName].keywords
        self.abstract = self.wms.contents[layerName].abstract
        self.title = self.wms.contents[layerName].title
        self.extractSublayers()
        self.capabilities_xml = self.wms.getServiceXML()
        self.inspireCapabilities = self.parseInspireExtendedCapabilities()

    def printKeysOfDict(myDict):
        for key in myDict.keys():
            print(key)
            
    def extractSublayers(self):
        """[summary]
        Extract the sublayers of the WMS layer
        """
        self.sublayers = {}
        for l in self.wms.contents[self.layername].layers:
            self.sublayers[l.name] = l
            
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


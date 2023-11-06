from owslib import WebMapService, WebFeatureService
from lxml import etree
from api.GeoserverApi import GeoserverAPI
import xmltodict


class WMSLayerImporter:
    def __init__(self, wms: WebMapService, layerName: str):
        self.crsOptions = wms.contents[layerName].crsOptions
        self.boundingBox = wms.contents[layerName].boundingBox
        self.boundingBoxWGS84 = wms.contents[layerName].boundingBoxWGS84
        self.metadataUrls = wms.contents[layerName].metadataUrls
        self.styles = wms.contents[layerName].styles
        self.keywords = wms.contents[layerName].keywords
        self.abstract = wms.contents[layerName].abstract
        self.title = wms.contents[layerName].title
        self.capabilities_xml = wms.getServiceXML()
        self.inspireCapabilities = self.parseInspireExtendedCapabilities()

    def printKeysOfDict(myDict):
        for key in myDict.keys():
            print(key)

    def parseInspireExtendedCapabilities(self):
        capabilities_tree = etree.fromstring(self.capabilities_xml)
        print(etree.tostring(extended_capabilities).decode())
        
        # Define the namespace for INSPIRE elements
        namespaces={
            'inspire_vs': 'http://inspire.ec.europa.eu/schemas/inspire_vs/1.0',
            'inspire_common': 'http://inspire.ec.europa.eu/schemas/common/1.0'
        }
        # Find the inspire_vs:ExtendedCapabilities section
        extended_capabilities = capabilities_tree.find('.//inspire_vs:ExtendedCapabilities', namespaces=namespaces['inspire_vs'])
        return xmltodict.parse(etree.tostring(extended_capabilities))
    

        # Find the inspire_common:MetadataUrl section
        # metadata_url_elements = capabilities_tree.xpath('.//inspire_common:MetadataUrl', namespaces=namespaces['inspire_common'])


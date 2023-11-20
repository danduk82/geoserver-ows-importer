import jsonschema
import requests

import logging
log = logging.getLogger()


class FeatureType:
    _responseSchema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "featureType": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "nativeName": {"type": "string"},
                "namespace": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "href": {"type": "string", "format": "uri"}
                },
                "required": ["name", "href"]
                },
                "title": {"type": "string"},
                "keywords": {
                "type": "object",
                "properties": {
                    "string": {
                    "type": "array",
                    "items": {"type": "string"}
                    }
                },
                "required": ["string"]
                },
                "srs": {"type": "string"},
                "nativeBoundingBox": {
                "type": "object",
                "properties": {
                    "minx": {"type": "number"},
                    "maxx": {"type": "number"},
                    "miny": {"type": "number"},
                    "maxy": {"type": "number"},
                    "crs": {"type": "object", "properties": {"@class": {"type": "string"}, "$": {"type": "string"}}}
                },
                "required": ["minx", "maxx", "miny", "maxy", "crs"]
                },
                "latLonBoundingBox": {
                "type": "object",
                "properties": {
                    "minx": {"type": "number"},
                    "maxx": {"type": "number"},
                    "miny": {"type": "number"},
                    "maxy": {"type": "number"},
                    "crs": {"type": "string"}
                },
                "required": ["minx", "maxx", "miny", "maxy", "crs"]
                },
                "projectionPolicy": {"type": "string"},
                "enabled": {"type": "boolean"},
                "store": {
                "type": "object",
                "properties": {
                    "@class": {"type": "string"},
                    "name": {"type": "string"},
                    "href": {"type": "string", "format": "uri"}
                },
                "required": ["@class", "name", "href"]
                },
                "serviceConfiguration": {"type": "boolean"},
                "maxFeatures": {"type": "integer"},
                "numDecimals": {"type": "integer"},
                "padWithZeros": {"type": "boolean"},
                "forcedDecimal": {"type": "boolean"},
                "overridingServiceSRS": {"type": "boolean"},
                "skipNumberMatched": {"type": "boolean"},
                "circularArcPresent": {"type": "boolean"},
                "attributes": {
                "type": "object",
                "properties": {
                    "attribute": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                        "name": {"type": "string"},
                        "minOccurs": {"type": "integer"},
                        "maxOccurs": {"type": "integer"},
                        "nillable": {"type": "boolean"},
                        "binding": {"type": "string"}
                        },
                        "required": ["name", "minOccurs", "maxOccurs", "nillable", "binding"]
                    }
                    }
                },
                "required": ["attribute"]
                }
            },
            "required": [
                "name", "nativeName", "namespace", 
                "nativeBoundingBox", "latLonBoundingBox", 
                "enabled", "store", "attributes"
            ]
            }
        },
        "required": ["featureType"]
        }
    
    def __init__(self,
                workspace_name,
                store_name,
                layer_name,
                table_name,
                srs = "EPSG:4326",
                internationalTitle = {"de-DE": "change-me - title"},
                internationalAbstract = {"de-DE": "change-me - abstract"},
                keywords = {},
                disabled_services=[]
                ) -> None:
        self.workspace_name = workspace_name
        self.store_name = store_name
        self.layer_name = layer_name
        self.internationalTitle = internationalTitle
        self.internationalAbstract = internationalAbstract
        self.table_name = table_name
        self.srs = srs
        self.keywords = keywords
        self.disabled_services = disabled_services
        
    @property
    def responseSchema(self):
        return self._responseSchema
    
    def endpoint_url(self):
        return f"/workspaces/{self.workspace}/featuretypes/{self.featureTypeName}.json"
    
    def post_payload(self):
        log.debug(f"post_payload: keywords = {self.keywords}")
        payload = {
            "featureType": {
                "name": self.layer_name,
                "nativeName": self.table_name,
                "internationalTitle": self.internationalTitle,
                "internationalAbstract": self.internationalAbstract,
                "srs": self.srs,
                "keywords": self.keywords                
            }
        }
        if self.disabled_services != []:
            payload["featureType"]["serviceConfiguration"] = True
            payload["featureType"]["disabledServices"] = { "string" : self.disabled_services}
        return payload
   
    def validate(self, response):
        try:
            jsonschema.validate(response, self.responseSchema)
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            return False
        return True
            
    def parseResponse(self, response):
        if response.status_code == 200:
            # Parse the JSON response
            self.featureType = response.json()
            self.validate(self.featureType)
        else:
            log.error(f"Error: {response.status_code}")

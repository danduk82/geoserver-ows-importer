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
    
    def __init__(self) -> None:
        pass
    
    @property
    def responseSchema(self):
        return self._responseSchema
    
    def __init__(self):
        pass
    
    def validate(self, response):
        try:
            jsonschema.validate(response, self.responseSchema)
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            return False
        return True
            
    def fetchFeatureType(self, workspace):
        response = requests.get(self.listUrl(self.geoserverInstance.restUrl, workspace), auth=(self.geoserverInstance.username, self.geoserverInstance.password)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            self.featureType = response.json()
            self.validate(self.featureType)
        else:
            log.error(f"Error: {response.status_code}")

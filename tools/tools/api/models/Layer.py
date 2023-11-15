import jsonschema
import requests

import logging
log = logging.getLogger()


class Layer:
    _responseSchema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "layer": {
            "type": "object",
            "properties": {
                "name": {
                "type": "string"
                },
                "type": {
                "type": "string"
                },
                "defaultStyle": {
                "type": "object",
                "properties": {
                    "name": {
                    "type": "string"
                    },
                    "href": {
                    "type": "string",
                    "format": "uri"
                    }
                },
                "required": ["name", "href"]
                },
                "resource": {
                "type": "object",
                "properties": {
                    "@class": {
                    "type": "string",
                    "const": "featureType"
                    },
                    "name": {
                    "type": "string"
                    },
                    "href": {
                    "type": "string",
                    "format": "uri"
                    }
                },
                "required": ["@class", "name", "href"]
                },
                "attribution": {
                "type": "object",
                "properties": {
                    "logoWidth": {
                    "type": "integer"
                    },
                    "logoHeight": {
                    "type": "integer"
                    }
                },
                "required": ["logoWidth", "logoHeight"]
                },
                "dateCreated": {
                "type": "string",
                "format": "date-time"
                }
            },
            "required": ["name", "type", "defaultStyle", "resource", "attribution", "dateCreated"]
            }
        },
        "required": ["layer"]
        }

    
    def __init__(self,
                workspace_name,
                layer_name,
                srs = "EPSG:4326",
                title = "",
                abstract = "",
                keywords = {}) -> None:
        self.workspace = workspace_name
        self.layer_name = layer_name
        self.title = title
        self.srs = srs
        self.abstract = abstract
        self.keywords = keywords
        
    @property
    def responseSchema(self):
        return self._responseSchema
    
    def endpoint_url(self):
        return f"/workspaces/{self.workspace}/layers/{self.layer_name}.json"
    
    def put_payload_style(self, style_name):
        return {
            "layer": {
                "name": self.layer_name,
                "defaultStyle": {
                    "name": style_name
                }
            }
        }
   
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
            self.layer = response.json()
            self.validate(self.layer)
        else:
            log.error(f"Error: {response.status_code}")
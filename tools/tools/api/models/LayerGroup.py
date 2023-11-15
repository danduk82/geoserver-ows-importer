import jsonschema
import requests

import logging
log = logging.getLogger()


class LayerGroup:
    _responseSchema = {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "type": "object",
            "properties": {
                "layerGroup": {
                "type": "object",
                "properties": {
                    "name": {
                    "type": "string"
                    },
                    "mode": {
                    "type": "string"
                    },
                    "title": {
                    "type": "string"
                    },
                    "abstractTxt": {
                    "type": "string"
                    },
                    "workspace": {
                    "type": "object",
                    "properties": {
                        "name": {
                        "type": "string"
                        }
                    },
                    "required": ["name"]
                    },
                    "internationalTitle": {
                    "type": "string"
                    },
                    "internationalAbstract": {
                    "type": "string"
                    },
                    "publishables": {
                    "type": "object",
                    "properties": {
                        "published": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                            "@type": {
                                "type": "string",
                                "const": "layer"
                            },
                            "name": {
                                "type": "string"
                            },
                            "href": {
                                "type": "string",
                                "format": "uri"
                            }
                            },
                            "required": ["@type", "name", "href"]
                        }
                        }
                    },
                    "required": ["published"]
                    },
                    "styles": {
                    "type": "object",
                    "properties": {
                        "style": {
                        "type": "array",
                        "items": {
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
                        }
                        }
                    },
                    "required": ["style"]
                    },
                    "bounds": {
                    "type": "object",
                    "properties": {
                        "minx": {
                        "type": "number"
                        },
                        "maxx": {
                        "type": "number"
                        },
                        "miny": {
                        "type": "number"
                        },
                        "maxy": {
                        "type": "number"
                        },
                        "crs": {
                        "type": "object",
                        "properties": {
                            "@class": {
                            "type": "string",
                            "const": "projected"
                            },
                            "$": {
                            "type": "string",
                            "const": "EPSG:25833"
                            }
                        },
                        "required": ["@class", "$"]
                        }
                    },
                    "required": ["minx", "maxx", "miny", "maxy", "crs"]
                    },
                    "dateCreated": {
                    "type": "string",
                    "format": "date-time"
                    }
                },
                "required": [
                    "name",
                    "mode",
                    "title",
                    "abstractTxt",
                    "workspace",
                    "publishables",
                    "styles",
                    "bounds",
                    "dateCreated"
                ]
                }
            },
            "required": ["layerGroup"]
            }

    
    def __init__(self,
                workspace_name,
                layer_group_name,
                layers_list,
                srs = "EPSG:4326",
                title = "",
                abstract = "",
                keywords = {}) -> None:
        self.workspace_name = workspace_name
        self.layer_group_name = layer_group_name
        self.layers_list = layers_list
        self.title = title
        self.srs = srs
        self.abstract = abstract
        self.keywords = keywords
        
    @property
    def responseSchema(self):
        return self._responseSchema
    
    def endpoint_url(self):
        return f"/workspaces/{self.workspace}/layergroups/{self.layerGroupName}.json"
    
    def post_payload(self):
        return {
            "layerGroup": {
                "name": self.layer_group_name,
                "title": self.title,
                "abstract": self.abstract,
                "srs": self.srs,
                "keywords": self.keywords                
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
            self.layerGroup = response.json()
            self.validate(self.layerGroup)
        else:
            log.error(f"Error: {response.status_code}")

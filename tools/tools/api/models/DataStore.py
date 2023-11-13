
import jsonschema
import requests

import logging
log = logging.getLogger()

class DataStore:
    _responseSchema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "dataStore": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "type": {"type": "string"},
                "enabled": {"type": "boolean"},
                "workspace": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "href": {"type": "string", "format": "uri"}
                },
                "required": ["name", "href"]
                },
                "connectionParameters": {
                "type": "object",
                "properties": {
                    "entry": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                        "@key": {"type": "string"},
                        "$": {"type": "string"}
                        },
                        "required": ["@key", "$"]
                    }
                    }
                },
                "required": ["entry"]
                },
                "_default": {"type": "boolean"},
                "dateCreated": {"type": "string", "format": "date-time"},
                "dateModified": {"type": "string", "format": "date-time"},
                "featureTypes": {"type": "string", "format": "uri"}
            },
            "required": [
                "name",
                "type",
                "enabled",
                "workspace",
                "connectionParameters",
                "_default",
                "dateCreated",
                "dateModified",
                "featureTypes"
            ]
            }
        },
        "required": ["dataStore"]
        }


    def __init__(self, workspace_name, data_store_name, connection_parameters, data_store_type="PostGIS") -> None:
        self.workspace_name = workspace_name
        self.data_store_name = data_store_name
        self.connection_parameters = connection_parameters
        self.data_store_type = data_store_type
        
    def endpoint_url(self):
        return f"/workspaces/{self.workspace_name}/datastores/{self.data_store_name}.json"
    
    @property
    def name(self):
        return self.data_store_name
    
    def post_payload(self):
        return {
            "dataStore": {
                "name": self.data_store_name,
                "type": self.data_store_type,
                "enabled": True,
                "workspace": {
                    "name": self.workspace_name
                },
                "connectionParameters": {
                    "entry": [
                        {"@key": key, "$": value} for key, value in self.connection_parameters.items()
                    ]
                }
            }
        }

    def fetch_data_store_response(self):
        url = f"{self.geoserver_instance.rest_url}/workspaces/{self.workspace_name}/datastores/{self.data_store_name}.json"
        response = requests.get(url, auth=(self.geoserver_instance.username, self.geoserver_instance.password))

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            json_data = response.json()
            self.validate(json_data)

            # Extract connection parameters
            self.connection_parameters = self.parse_connection_parameters(json_data)
        else:
            log.error(f"Error: {response.status_code}")

    def validate(self, response):
        try:
            jsonschema.validate(response, self.responseSchema())
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            raise Exception("Invalid from data store response")

    def parse_connection_parameters(self, json_data):
        return {entry["@key"]: entry["$"] for entry in json_data.get("dataStore", {}).get("connectionParameters", {}).get("entry", [])}

    @property
    def responseSchema(self):
        # Define the JSON schema here
        return self._responseSchema



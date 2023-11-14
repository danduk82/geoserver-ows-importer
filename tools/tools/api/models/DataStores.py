import jsonschema
import requests

import logging
log = logging.getLogger()


class DataStores:
    
    def __init__(self, workspace) -> None:
        self.workspace = workspace
        self.dataStores = {}
        
    
    def endpoint_url(self):
        return f"/workspaces/{self.workspace}/datastores.json"
    
    _responseSchema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "dataStores": {
            "type": "object",
            "properties": {
                "dataStore": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                    "name": {"type": "string"},
                    "href": {"type": "string", "format": "uri"}
                    },
                    "required": ["name", "href"]
                }
                }
            },
            "required": ["dataStore"]
            }
        },
        "required": ["dataStores"]
        }
    
    @property
    def responseSchema(self):
        return self._responseSchema
    
    def validate(self, response):
        try:
            log.debug("validate: response = " + str(response))
            if not response["dataStores"] == '':
                jsonschema.validate(response, self.responseSchema)
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            return False
        return True
    
    def parseResponse(self, response):
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            json_data = response.json()
            if not (self.validate(json_data)):
                raise Exception("Invalid from datastores")
            # Map the response to a list of DataStore instances
            try:
                for store in json_data.get('dataStores', {}).get('dataStore', []):
                    self.dataStores[store['name']] = store['href']  
            except AttributeError:
                self.dataStores = {}

            # Now 'dataStores' is a list of DataStore instances
            for data_store_name, data_store_href in self.dataStores.items():
                log.debug(f"Name: {data_store_name}, Href: {data_store_href}")
        else:
            log.error(f"Error: {response.status_code}")

    
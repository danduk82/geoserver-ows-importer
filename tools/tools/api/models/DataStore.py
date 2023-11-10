import jsonschema
import requests

import logging
log = logging.getLogger()

class DataStore:
    def __init__(self, name, href):
        self.name = name
        self.href = href


class DataStores:
    
    def __init__(self, geoserverInstance) -> None:
        self.geoserverInstance = geoserverInstance
        
    def listUrl(geoserverRestUrl, workspace):
        return f"{geoserverRestUrl}/workspaces/{workspace}/datastores.json"
    
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
            jsonschema.validate(response, self.responseSchema)
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            return False
        return True
    
    def fetchDataStores(self, workspace):
        response = requests.get(self.listUrl(self.geoserverInstance.restUrl, workspace), auth=(self.geoserverInstance.username, self.geoserverInstance.password)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            json_data = response.json()
            if not (self.validate(json_data)):
                raise Exception("Invalid from datastores")
    

            # Map the response to a list of DataStore instances
            self.data_stores = [DataStore(store['name'], store['href']) for store in json_data.get('dataStores', {}).get('dataStore', [])]

            # Now 'data_stores' is a list of DataStore instances
            for data_store in self.data_stores:
                log.debug(f"Name: {data_store.name}, Href: {data_store.href}")
        else:
            log.error(f"Error: {response.status_code}")

    
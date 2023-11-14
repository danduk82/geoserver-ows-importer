import jsonschema
import requests

import logging
log = logging.getLogger()

class Workspace:   

    def __init__(self, workspace_name) -> None:
        self.workspace_name = workspace_name
        self.workspace_info = None
        
    def endpoint_url(self):
        return f"/workspaces/{self.workspace_name}.json"
    

    _responseSchema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "workspace": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "isolated": {"type": "boolean"},
                "dateCreated": {"type": "string", "format": "date-time"},
                "dataStores": {"type": "string", "format": "uri"},
                "coverageStores": {"type": "string", "format": "uri"},
                "wmsStores": {"type": "string", "format": "uri"},
                "wmtsStores": {"type": "string", "format": "uri"}
            },
            "required": ["name", "isolated", "dataStores", "coverageStores", "wmsStores", "wmtsStores"]
            }
        },
        "required": ["workspace"]
        }

    def post_payload(self, is_isolated=False):
        return {
            "workspace": {
                "name": self.workspace_name
            }
        }
        
    def fetch_workspace_response(self):
        url = f"{self.geoserver_instance.rest_url}/workspaces/{self.workspace_name}.json"
        response = requests.get(url, auth=(self.geoserver_instance.username, self.geoserver_instance.password))

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            json_data = response.json()
            self.validate(json_data)

            # Set the workspace info
            self.workspace_info = json_data.get("workspace", {})
        else:
            log.error(f"Error: {response.status_code}")

    def validate(self, response):
        try:
            jsonschema.validate(response, self.responseSchema())
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            raise Exception("Invalid from workspace response")

    @property
    def responseSchema(self):
        # Define the JSON schema here
        return self._responseSchema


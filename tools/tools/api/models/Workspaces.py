import jsonschema
import requests

import logging
log = logging.getLogger()

class Workspaces:

    def __init__(self, geoserver_instance) -> None:
        self.geoserver_instance = geoserver_instance
        self._workspaces = {}

    def endpoint_url(self):
        return f"/workspaces.json"

    _response_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "workspaces": {
                "type": "object",
                "properties": {
                    "workspace": {
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
                "required": ["workspace"]
            }
        },
        "required": ["workspaces"]
    }

    @property
    def response_schema(self):
        return self._response_schema

    def validate(self, response):
        try:
            jsonschema.validate(response, self.response_schema)
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            return False
        return True

    def find(self, workspace_name):
        return self.workspaces.get(workspace_name, None)
    
    @property
    def workspaces(self):
        return self._workspaces
        
    def parseResponse(self, response):

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            json_data = response.json()
            if not self.validate(json_data):
                raise Exception("Invalid response from workspaces")

            # Map the response to a list of Workspace instances
            for ws in json_data.get('workspaces', {}).get('workspace', []):
                self._workspaces[ws['name']] = ws['href']

            # Now 'workspaces' is a list of Workspace instances
            log.debug("Parsed Workspaces:")
            for workspace,href in self._workspaces.items():
                log.debug(f"Name: {workspace}, Href: {href}")
        else:
            log.error(f"Error: {response.status_code}")

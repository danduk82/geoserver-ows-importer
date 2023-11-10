import jsonschema
import requests

import logging
log = logging.getLogger()

class WorkspaceItem:
    def __init__(self, name, href):
        self.name = name
        self.href = href

class Workspaces:

    def __init__(self, geoserver_instance) -> None:
        self.geoserver_instance = geoserver_instance
        self.workspaces = []  # To store Workspace instances

    def list_url(self):
        return f"{self.geoserver_instance.rest_url}/workspaces.json"

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

    def fetchWorkspaces(self):
        response = requests.get(self.list_url(), auth=(self.geoserver_instance.username, self.geoserver_instance.password))

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            json_data = response.json()
            if not self.validate(json_data):
                raise Exception("Invalid response from workspaces")

            # Map the response to a list of Workspace instances
            self.workspaces = [WorkspaceItem(ws['name'], ws['href']) for ws in json_data.get('workspaces', {}).get('workspace', [])]

            # Now 'workspaces' is a list of Workspace instances
            for workspace in self.workspaces:
                log.debug(f"Name: {workspace.name}, Href: {workspace.href}")
        else:
            log.error(f"Error: {response.status_code}")

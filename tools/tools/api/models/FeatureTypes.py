import jsonschema
import requests

import logging
log = logging.getLogger()

class FeatureTypeItem:
    def __init__(self, name, href):
        self.name = name
        self.href = href

class FeatureTypes:

    def __init__(self, geoserver_instance, workspace_name) -> None:
        self.geoserver_instance = geoserver_instance
        self.workspace_name = workspace_name
        self.feature_types = None

    def url(self):
        return f"{self.geoserver_instance.rest_url}/workspaces/{self.workspace_name}/featuretypes.json"

    _response_schema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "featureTypes": {
                "type": "object",
                "properties": {
                    "featureType": {
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
                "required": ["featureType"]
            }
        },
        "required": ["featureTypes"]
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

    def fetch_feature_types(self):
        response = requests.get(self.url(), auth=(self.geoserver_instance.username, self.geoserver_instance.password))

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            json_data = response.json()
            if not self.validate(json_data):
                raise Exception("Invalid from featureTypes")

            # Map the response to a list of FeatureType instances
            self.feature_types = [FeatureTypeItem(feature['name'], feature['href']) for feature in json_data.get('featureTypes', {}).get('featureType', [])]

            # Now 'feature_types' is a list of FeatureType instances
            for feature_type in self.feature_types:
                log.debug(f"Name: {feature_type.name}, Href: {feature_type.href}")
        else:
            log.error(f"Error: {response.status_code}")

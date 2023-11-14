import jsonschema
import requests

import logging
log = logging.getLogger()


class FeatureTypes:

    def __init__(self, workspace_name, data_store_name, featureTypes={}) -> None:
        self.workspace_name = workspace_name
        self.data_store_name = data_store_name
        self.featureTypes = featureTypes

    def endpoint_url(self):
        return f"/workspaces/{self.workspace_name}/datastores/{self.data_store_name}/featuretypes.json"

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
            if not response["featureTypes"] == '':
                jsonschema.validate(response, self.response_schema)
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            return False
        return True

    def parseResponse(self, response):
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            json_data = response.json()
            if not self.validate(json_data):
                raise Exception("Invalid from featureTypes")

            # Map the response to a list of FeatureType instances
            try:
                for feature in json_data.get('featureTypes', {}).get('featureType', []):
                    self.featureTypes[feature['name']] = feature['href']
            except AttributeError:
                self.featureTypes = {}

            # Now 'featureTypes' is a list of FeatureType instances
            for feature_type_name, feature_type_href in self.featureTypes.items():
                log.debug(f"Name: {feature_type_name}, Href: {feature_type_href}")
        else:
            log.error(f"Error: {response.status_code}")

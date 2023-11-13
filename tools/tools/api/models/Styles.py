import jsonschema
import requests
import logging

log = logging.getLogger()

class StyleItem:
    def __init__(self, name, href):
        self.name = name
        self.href = href


class Styles:
    
    def __init__(self, workspace) -> None:
        self.workspace = workspace
        self.styles = {}
        
    
    def endpoint_url(self):
        return f"/workspaces/{self.workspace}/styles.json"
    
    _responseSchema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "styles": {
                "type": "object",
                "properties": {
                    "style": {
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
                "required": ["style"]
            }
        },
        "required": ["styles"]
    }
    
    @property
    def responseSchema(self):
        return self._responseSchema
    
    def validate(self, response):
        try:
            log.debug("validate: response = " + str(response))
            if not response["styles"] == '':
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
                raise Exception("Invalid from styles")
            # Map the response to a list of Style instances
            try:
                self.styles = [StyleItem(style['name'], style['href']) for style in json_data.get('styles', {}).get('style', [])]
            except AttributeError:
                self.styles = []

            # Now 'styles' is a list of Style instances
            for style in self.styles:
                log.debug(f"Name: {style.name}, Href: {style.href}")
        else:
            log.error(f"Error: {response.status_code}")
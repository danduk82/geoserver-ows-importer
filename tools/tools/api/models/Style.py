import jsonschema
import requests
import logging
import xmltodict

log = logging.getLogger()

class Style:
    
    def __init__(self, workspace, name=None, format=None, language_version=None, filename=None, date_created=None, date_modified=None) -> None:
        self.workspace = workspace
        self.name = name
        self.format = format
        self.language_version = language_version
        self.filename = filename
        self.date_created = date_created
        self.date_modified = date_modified
    
    def endpoint_url(self):
        return f"/workspaces/{self.workspace}/styles/{self.name}"
    
    def post_payload(self):
        return {
            "style": {
                "name": self.name,
                "filename": self.filename
            }
        }

    def put_payload(self):
        return {
            "style": {
                "name": self.name,
                "filename": self.filename
            }
        }
    
    def xml_post_payload(self):
        return xmltodict.unparse(self.post_payload()).split('\n', 1)[1]
    
    def xml_put_payload(self):
        return xmltodict.unparse(self.put_payload()).split('\n', 1)[1]
    
    _responseSchema = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "properties": {
            "style": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "workspace": {
                        "type": "object",
                        "properties": {"name": {"type": "string"}},
                        "required": ["name"]
                    },
                    "format": {"type": "string"},
                    "languageVersion": {
                        "type": "object",
                        "properties": {"version": {"type": "string"}},
                        "required": ["version"]
                    },
                    "filename": {"type": "string"},
                    "dateCreated": {"type": "string", "format": "date-time"},
                    "dateModified": {"type": "string", "format": "date-time"}
                },
                "required": ["name", "workspace", "format", "languageVersion", "filename", "dateCreated", "dateModified"]
            }
        },
        "required": ["style"]
    }
    
    @property
    def responseSchema(self):
        return self._responseSchema
    
    def validate(self, response):
        try:
            log.debug("validate: response = " + str(response))
            if not response["style"] == '':
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
            # Map the response to attributes of the Style instance
            try:
                style_data = json_data.get('style', {})
                self.name = style_data.get('name')
                self.format = style_data.get('format')
                self.language_version = style_data.get('languageVersion', {}).get('version')
                self.filename = style_data.get('filename')
                self.date_created = style_data.get('dateCreated')
                self.date_modified = style_data.get('dateModified')
            except AttributeError:
                # Handle the case where the attributes are not present in the response
                self.name = None

            # Now 'style' is a Style instance
            if self.name:
                log.debug(f"Name: {self.name}, Workspace: {self.workspace}, Format: {self.format}")
        else:
            log.error(f"Error: {response.status_code}")

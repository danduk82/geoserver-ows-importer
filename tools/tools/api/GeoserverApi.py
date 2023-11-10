import sys
import os.path

import requests
import json

from models import FeatureTypes, DataStores, FeatureType, DataStore

class GeoserverRestAPI:
    def __init__(self, geoserver_base_url, username, password) -> None:
        self.geoserver_base_url = geoserver_base_url
        self.username = username
        self.password = password
        self.geoserver_rest_url = self.sanitize_rest_url(geoserver_base_url)
        self.headers = {"Content-Type": "application/json"}

    @staticmethod
    def sanitize_rest_url(url):
        if url.endswith('/'):
            url = url[:-1]
        if not url.endswith('/rest'):
            url = url + '/rest'
        return url
    
    def GET(self, endpoint_url):
        url = self.geoserver_rest_url + endpoint_url
        response = requests.get(url, auth=(self.username, self.password), headers=self.headers)
        return response
    
    def POST(self, endpoint_url, data):
        url = self.geoserver_rest_url + endpoint_url
        response = requests.post(url, auth=(self.username, self.password), headers=self.headers, data=data)
        return response
    
    def PUT(self, endpoint_url, data):
        url = self.geoserver_rest_url + endpoint_url
        response = requests.put(url, auth=(self.username, self.password), headers=self.headers, data=data)
        return response
    
    def DELETE(self, endpoint_url):
        url = self.geoserver_rest_url + endpoint_url
        response = requests.delete(url, auth=(self.username, self.password), headers=self.headers)
        return response
    
    
class GeoserverAPI:
    def __init__(
        self, geoserver_rest_url, geoserver_username, geoserver_password
    ) -> None:
        self.geoserverRestApi = GeoserverRestAPI(geoserver_rest_url, geoserver_username, geoserver_password)

    
    def create_workspace(self, workspace_name, default=False):
        pass

    def get_workspace(self, workspace_name):
        pass

    def update_workspace(self, workspace_name):
        pass

    def delete_workspace(self, workspace_name):
        pass

    def list_workspaces(self):
        
        pass

    def create_datastore(
        self,
        workspace_name,
        store_name,
        host="172.17.0.1",
        port="5432",
        database="test",
        username="username",
        password="password",
    ):

        pass

    def delete_datastore(self, workspace_name, store_name):
        pass

    def get_datastore(self, workspace_name, store_name):
        pass
    
    def get_datastores(self, workspace_name):
        dataStore = DataStores.DataStores(workspace_name)
        response = self.geoserverRestApi.GET(dataStore.endpoint_url())
        dataStore.parseResponse(response)
        return dataStore.data_stores
    
    def create_featuretype(
        self,
        workspace_name,
        store_name,
        layer_name,
        title,
        table_name,
        feature_type="Point",
        srs="EPSG:3857",
        abstract=""
    ):
        pass

    def delete_featuretype(self, workspace_name, store_name, layer_name):
        pass

    def get_featuretype(self, workspace_name, store_name, layer_name):
        pass
    
    def list_featuretypes(self, workspace_name):
        pass


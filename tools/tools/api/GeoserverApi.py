import sys
import os.path

import requests
import json

from .models import (
    FeatureTypes,
    DataStores,
    FeatureType,
    DataStore,
    Workspaces,
    Workspace,
    Styles,
    Style
)

import logging
log = logging.getLogger()


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
    
    _methods_mapping = {
        "GET": requests.get,
        "POST": requests.post,
        "PUT": requests.put,
        "DELETE": requests.delete
    }
    
    def _render_request_parameters(self, parameters):
        return "&".join([f"{key}={value}" for key, value in parameters.items()])
    
    def _do_request(self, method, endpoint_url, data=None, files=None, headers=None, parameters=None):
        url = self.geoserver_rest_url + endpoint_url + ("?{}".format(self._render_request_parameters(parameters)) if parameters else "")
        log.debug(f"url = {url}")
        log.debug(f"data = {data}")
        log.debug(f"headers = {headers}")
        log.debug(f"files = {files}")
        log.debug(f"parameters = {parameters}")
        request_headers = self.headers.copy()
        request_headers.update(headers or {})
        if request_headers['Content-Type'] != "application/json":
            if data is not None:
                data = data.encode('utf-8')
            response = self._methods_mapping[method](url, auth=(self.username, self.password), headers=request_headers, data=data, files=files)
        else:
            response = self._methods_mapping[method](url, auth=(self.username, self.password), headers=request_headers, json=data, files=files)
        return response
    
    def GET(self, endpoint_url, headers=None, parameters=None):
        return self._do_request("GET", endpoint_url, headers=headers, parameters=parameters)
    
    def POST(self, endpoint_url, data, files=None, headers=None, parameters=None):
        return self._do_request("POST", endpoint_url, data, files=files, headers=headers, parameters=parameters)

    def PUT(self, endpoint_url, data, files=None, headers=None, parameters=None):
        return self._do_request("PUT", endpoint_url, data, files=files, headers=headers, parameters=parameters)
        
    def DELETE(self, endpoint_url, data=None, headers=None, parameters=None):
        return self._do_request("DELETE", endpoint_url, data, headers=headers, parameters=parameters)
    
    
class GeoserverAPI:
    def __init__(
        self, geoserver_rest_url, geoserver_username, geoserver_password
    ) -> None:
        self.geoserverRestApi = GeoserverRestAPI(geoserver_rest_url, geoserver_username, geoserver_password)

    def create_workspace(self, workspace_name):
        log.debug(f"inside method : create_workspace")
        self._populate_workspaces()
        newWorkspace = Workspace.Workspace(workspace_name)
        
        if not self.workspaces.find(workspace_name):
            self.geoserverRestApi.POST(self.workspaces.endpoint_url(), newWorkspace.post_payload())
        
    def get_workspace(self, workspace_name):
        raise NotImplementedError

    def update_workspace(self, workspace_name):
        raise NotImplementedError

    def delete_workspace(self, workspace_name):
        log.debug(f"inside method : delete_workspace")
        self._populate_workspaces()
        delWorkspace = Workspace.Workspace(workspace_name)
        if self.workspaces.find(workspace_name):
            self.geoserverRestApi.DELETE(delWorkspace.endpoint_url(), parameters={"recurse": "true"})
        
    def _populate_workspaces(self):
        log.debug(f"inside method : _populate_workspaces")
        self.workspaces = Workspaces.Workspaces()
        response = self.geoserverRestApi.GET(self.workspaces.endpoint_url())
        self.workspaces.parseResponse(response)
        
    def get_workspaces(self):
        log.debug(f"inside method : get_workspaces")
        self._populate_workspaces()
        return self.workspaces.workspaces

    def create_datastore(
        self,
        workspace_name,
        store_name,
        host="172.17.0.1",
        port="5432",
        database="test",
        username="username",
        password="password",
        schema="public"
    ):
        log.debug(f"inside method : create_datastore")
        if not store_name in self.get_datastores_per_workspace(workspace_name):
            connectionParameters = {"host": host, "port": port, "database": database, "user": username, "passwd": password, "schema": schema, "dbtype": "postgis"}
            newDataStore = DataStore.DataStore(
                workspace_name,
                store_name,
                connectionParameters
            )
            self.geoserverRestApi.POST(self.datastores[workspace_name].endpoint_url(), newDataStore.post_payload())

    def delete_datastore(self, workspace_name, store_name):
        raise NotImplementedError

    def get_datastore(self, workspace_name, store_name):
        raise NotImplementedError
    
    def _populate_datastores(self):
        log.debug(f"inside method : _populate_datastores")
        self.datastores = {}
        for workspace_name in self.get_workspaces():
            self.datastores[workspace_name] = DataStores.DataStores(workspace_name)
            response = self.geoserverRestApi.GET(self.datastores[workspace_name].endpoint_url())
            self.datastores[workspace_name].parseResponse(response)
    
    def _refresh_datastores_per_workspace(self, workspace_name):
        log.debug(f"inside method : _refresh_datastores_per_workspace")
        if not hasattr(self, "datastores"):
            self._populate_datastores()
        self.datastores[workspace_name] = DataStores.DataStores(workspace_name)
        response = self.geoserverRestApi.GET(self.datastores[workspace_name].endpoint_url())
        self.datastores[workspace_name].parseResponse(response)
        
    def get_datastores_per_workspace(self, workspace_name):
        log.debug(f"inside method : get_datastores_per_workspace")
        self._refresh_datastores_per_workspace(workspace_name)
        return self.datastores[workspace_name].dataStores.keys()
    
    def create_featuretype(
        self,
        workspace_name,
        store_name,
        layer_name,
        table_name,
        feature_type="Point",
        srs="EPSG:3857",
        title = "",
        abstract=""
    ):
        log.debug(f"inside method : create_featuretype")
        if not layer_name in self.get_featuretype_per_datastore(workspace_name, store_name):
            newFeatureType = FeatureType.FeatureType(
                workspace_name,
                store_name,
                layer_name,
                table_name,
                feature_type,
                srs,
                title,
                abstract
            )
            self.geoserverRestApi.POST(self.featuretypes[workspace_name][store_name].endpoint_url(), newFeatureType.post_payload())

    def delete_featuretype(self, workspace_name, store_name, layer_name):
        raise NotImplementedError

    def get_featuretype(self, workspace_name, store_name, layer_name):
        raise NotImplementedError
    
    def _populate_featuretypes(self):
        log.debug(f"inside method : _populate_featuretypes")
        self.featuretypes = {}
        for workspace_name in self.get_workspaces():
            log.debug(f"workspace_name = {workspace_name}")
            self.featuretypes[workspace_name] = {}
            log.debug(f"self.featuretypes = {self.featuretypes}")
            for store_name in self.get_datastores_per_workspace(workspace_name):
                log.debug(f"store_name = {store_name}")
                self.featuretypes[workspace_name][store_name] = FeatureTypes.FeatureTypes(workspace_name, store_name)
                response = self.geoserverRestApi.GET(self.featuretypes[workspace_name][store_name].endpoint_url())
                self.featuretypes[workspace_name][store_name].parseResponse(response)
                
    def _refresh_featuretypes_per_workspace_datastore(self, workspace_name, store_name):
        log.debug(f"inside method : _refresh_featuretypes_per_workspace_datastore")
        if not hasattr(self, "featuretypes"):
            self._populate_featuretypes()
        log.debug(f"self.featuretypes = {self.featuretypes}")
        self.featuretypes[workspace_name][store_name] = FeatureTypes.FeatureTypes(workspace_name, store_name)
        response = self.geoserverRestApi.GET(self.featuretypes[workspace_name][store_name].endpoint_url())
        self.featuretypes[workspace_name][store_name].parseResponse(response)
    
    def get_featuretypes(self, workspace_name, store_name):
        log.debug(f"inside method : get_featuretypes")
        self._populate_featuretypes()
        log.debug(f"featureTypes in workspace {workspace_name} = {self.featuretypes}")
        return self.featuretypes[workspace_name]
    
    def get_featuretype_per_datastore(self, workspace_name, store_name):
        log.debug(f"inside method : get_featuretype_per_datastore")
        self._refresh_featuretypes_per_workspace_datastore(workspace_name, store_name)
        return self.featuretypes[workspace_name][store_name].featureTypes

    def _populate_styles(self):
        log.debug(f"inside method : _populate_styles")
        self.styles = {}
        for workspace_name in self.get_workspaces():
            self.styles[workspace_name] = Styles.Styles(workspace_name)
            response = self.geoserverRestApi.GET(self.styles[workspace_name].endpoint_url())
            self.styles[workspace_name].parseResponse(response)
    
    def _refresh_sytles_per_workspace(self, workspace_name):
        log.debug(f"inside method : _refresh_sytles_per_workspace")
        if not hasattr(self, "styles"):
            self._populate_styles()
        self.styles[workspace_name] = Styles.Styles(workspace_name)
        response = self.geoserverRestApi.GET(self.styles[workspace_name].endpoint_url())
        self.styles[workspace_name].parseResponse(response)

    def get_styles(self, workspace_name):
        log.debug(f"inside method : get_styles")
        self._refresh_sytles_per_workspace(workspace_name)
        return self.styles[workspace_name].styles
        
    def get_style(self, workspace_name, style_name):
        log.debug(f"inside method : get_style")
        raise NotImplementedError
    
    def create_style(self, workspace_name, style_name, style_file):
        log.debug(f"inside method : create_style")
        fileName = os.path.basename(style_file) if style_file else None
        newStyle = Style.Style(workspace=workspace_name, name=style_name, filename=fileName)
        if not style_name in self.get_styles(workspace_name):
            self.geoserverRestApi.POST(self.styles[workspace_name].endpoint_url(), newStyle.xml_post_payload(), headers = {"Content-Type": "text/xml"})
        
    
    def delete_style(self, workspace_name, style_name):
        raise NotImplementedError
    
    def update_style(self, workspace_name, style_name, style_file):
        log.debug(f"inside method : update_style")
        fileName = os.path.basename(style_file) if style_file else None
        newStyle = Style.Style(workspace=workspace_name, name=style_name, format="sld", filename=fileName, language_version="1.0.0")
        request_files = {'files': (os.path.basename(style_file), open(style_file, 'rb'))}
        log.debug(f"request_files = {request_files}")
        if not style_name in self.get_styles(workspace_name):
            self.geoserverRestApi.PUT(newStyle.endpoint_url(), data=None, files = request_files, headers = {"Content-Type": "application/vnd.ogc.sld+xml"}, parameters={"raw": "true"})
        
import sys
import os.path

import requests
import json

from .models import (
    FeatureTypes,
    DataStores,
    FeatureType,
    DataStore,
    LayerGroups,
    LayerGroup,
    Layers,
    Layer,
    Namespace,
    Workspaces,
    Workspace,
    SettingsWMS,
    SettingsWFS,
    Styles,
    Style
)

from .models.Common import KeyDollarListDict

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
            if (data is not None) and (type(data) != bytes):
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
        connectionParameters: KeyDollarListDict,
        host="172.17.0.1",
        port="5432",
        database="test",
        username="username",
        password="password",
        schema="public"
    ):
        log.debug(f"inside method : create_datastore")
        if not store_name in self.get_datastores_per_workspace(workspace_name):
            connectionParameters.update({"host": host, "port": port, "database": database, "user": username, "passwd": password, "schema": schema, "dbtype": "postgis"})
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
    
    def get_layers_per_workspace(self, workspace_name):
        log.debug(f"inside method : get_layers_per_datastore")
        self._refresh_layers_per_workspace(workspace_name)
        log.debug("self.layers[workspace_name].layers.keys() = {}".format(self.layers[workspace_name].layers))
        return self.layers[workspace_name].layers.keys()
    
    def _refresh_layers_per_workspace(self, workspace_name):
        log.debug(f"inside method : _refresh_layers_per_workspace")
        if not hasattr(self, "layers"):
            self._populate_layers()
        self.layers[workspace_name] = Layers.Layers(workspace_name)
        log.info(f"self.layers = {self.layers}")
        response = self.geoserverRestApi.GET(self.layers[workspace_name].endpoint_url())
        self.layers[workspace_name].parseResponse(response)
        
    def _populate_layers(self):
        log.debug(f"inside method : _populate_layers")
        self.layers = {}
        for workspace_name in self.get_workspaces():
            self.layers[workspace_name] = Layers.Layers(workspace_name)
            response = self.geoserverRestApi.GET(self.layers[workspace_name].endpoint_url())
            self.layers[workspace_name].parseResponse(response)
    
    def _populate_layergroups(self):
        log.debug(f"inside method : _populate_layergroups")
        self.layergroups = {}
        for workspace_name in self.get_workspaces():
            self.layergroups[workspace_name] = LayerGroups.LayerGroups(workspace_name)
            response = self.geoserverRestApi.GET(self.layergroups[workspace_name].endpoint_url())
            self.layergroups[workspace_name].parseResponse(response)
    
    def _refresh_layergroups_per_workspace(self, workspace_name):
        log.debug(f"inside method : _refresh_layergroups_per_workspace")
        if not hasattr(self, "layergroups"):
            self._populate_layergroups()
        self.layergroups[workspace_name] = LayerGroups.LayerGroups(workspace_name)
        response = self.geoserverRestApi.GET(self.layergroups[workspace_name].endpoint_url())
        self.layergroups[workspace_name].parseResponse(response)
    
    def get_layergroups_per_workspace(self, workspace_name):
        log.debug(f"inside method : get_layergroups_per_workspace")
        self._refresh_layergroups_per_workspace(workspace_name)
        return self.layergroups[workspace_name].layerGroups.keys()
    
    def create_layergroup(self, workspace_name, layergroup_name, layer_names, internationalTitle, internationalAbstract, metadataLinksIdentifier):
        log.debug(f"inside method : create_layergroup")
        if not layergroup_name in self.get_layergroups_per_workspace(workspace_name):
            layers_list = [ Layer.Layer(workspace_name, layer_name) for layer_name in layer_names ]
            log.debug(f"layers_list = {layers_list}")
            styles_list = [ Style.Style(workspace_name, layer_name) for layer_name in layer_names ]
            newLayerGroup = LayerGroup.LayerGroup(
                    workspace_name,
                    layergroup_name,
                    layers_list,
                    styles_list,
                    internationalAbstract=internationalAbstract,
                    internationalTitle=internationalTitle,
                    metadataLinksIdentifier=metadataLinksIdentifier
                )
            self.geoserverRestApi.POST(self.layergroups[workspace_name].endpoint_url(), newLayerGroup.post_payload())

    def _set_default_wms_service(self):
        log.debug(f"inside method : get_default_wms_service")
        self.defaultWmsSettings = SettingsWMS.SettingsWMS()
        response = self.geoserverRestApi.GET(self.defaultWmsSettings.endpoint_url_default_service())
        self.defaultWmsSettings.parseResponse(response)
        
    def get_default_wms_service(self):
        log.debug(f"inside method : get_default_wms_service")
        if not hasattr(self, "defaultWmsSettings"):
            self._set_default_wms_service()
        return self.defaultWmsSettings.wms
                
    def create_featuretype(
        self,
        workspace_name,
        store_name,
        layer_name,
        table_name,
        srs="EPSG:3857",
        title = "",
        abstract="",
        keywords = {"string": []},
        disabled_services = [],
        metadata_url=None,
        metadata_type="TC211",
        metadata_format="text/xml"
    ):
        log.debug(f"inside method : create_featuretype")
        if not layer_name in self.get_featuretype_per_datastore(workspace_name, store_name):
            newFeatureType = FeatureType.FeatureType(
                workspace_name=workspace_name,
                store_name=store_name,
                layer_name=layer_name,
                table_name=table_name,
                srs=srs,
                internationalTitle= {"de-DE": title},
                internationalAbstract={"de-DE": abstract} if abstract else None,
                keywords=keywords,
                disabled_services=disabled_services,
                metadata_url=metadata_url,
                metadata_type=metadata_type,
                metadata_format=metadata_format
            )
            self.geoserverRestApi.POST(self.featuretypes[workspace_name][store_name].endpoint_url(), newFeatureType.post_payload())

    
    def update_default_style(
                                self,
                                workspace_name,
                                layer_name,
                                style_name,
                                autorityUrl = {"name": "GDI-DE","href": "https://www.gdi-de.org"},
                                identifier = {"authority": "GDI-DE","identifier": "https://gdi.de/identifier"}
                            ):
        updateLayer = Layer.Layer(workspace_name, layer_name)
        self.geoserverRestApi.PUT(updateLayer.endpoint_url(), updateLayer.put_payload_style(style_name, autorityUrl, identifier))
        

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
    
    def update_style_legend(self, workspace_name, style_name, style_file, legend_url=None, legend_format=None, legend_width=None, legend_height=None):
        log.debug(f"inside method : update_style_legend")
        fileName = os.path.basename(style_file) if style_file else None
        updateStyle = Style.Style(workspace_name, style_name, filename=fileName, legend_url=legend_url, legend_format=legend_format, legend_width=legend_width, legend_height=legend_height)
        self.geoserverRestApi.PUT(updateStyle.endpoint_url(), updateStyle.xml_put_payload(), headers = {"Content-Type": "text/xml"})
    
    def update_style(self, workspace_name, style_name, style_file):
        log.debug(f"inside method : update_style")
        fileName = os.path.basename(style_file) if style_file else None
        newStyle = Style.Style(workspace=workspace_name, name=style_name, format="sld", filename=fileName, language_version="1.0.0")
        with open(style_file, 'rb') as file_content:
            data = file_content.read()
        self.geoserverRestApi.PUT(newStyle.endpoint_url(), data=data,  headers = {"Content-Type": "application/vnd.ogc.sld+xml"}, parameters={"raw": "true"})
        
    def update_namespace(self, workspace_name, uri, isolated="true"):
        log.debug(f"inside method : update_namespace")
        updateNamespace = Namespace.Namespace(workspace_name)
        self.geoserverRestApi.PUT(updateNamespace.endpoint_url(), updateNamespace.put_payload(uri=uri, isolated=isolated))    
    
    def activate_wms_service(self, workspace_name, wmsService):
        log.debug(f"inside method : activate_wms_service")
        self.geoserverRestApi.PUT(wmsService.endpoint_url(), wmsService.put_payload())
        
    def activate_wfs_service(self, workspace_name):
        log.debug(f"inside method : activate_wfs_service")
        updateSettingsWFS = SettingsWFS.SettingsWFS(workspace_name)
        self.geoserverRestApi.PUT(updateSettingsWFS.endpoint_url(), updateSettingsWFS.put_payload(enabled="true"))
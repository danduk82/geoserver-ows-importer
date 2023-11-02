# coding: utf-8

"""
    GeoServer Workspace

    A workspace is a grouping of data stores. Similar to a namespace, it is used to group data that is related in some way.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from geoserver.api_client import ApiClient


class SettingsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_local_settings(self, body, workspace, **kwargs):  # noqa: E501
        """Create workspace-specific settings  # noqa: E501

        Create new workspace-specific settings on the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_local_settings(body, workspace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsInfoWrapper body: The workspace-specific settings information to upload. (required)
        :param str workspace: The workspace name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_local_settings_with_http_info(body, workspace, **kwargs)  # noqa: E501
        else:
            (data) = self.create_local_settings_with_http_info(body, workspace, **kwargs)  # noqa: E501
            return data

    def create_local_settings_with_http_info(self, body, workspace, **kwargs):  # noqa: E501
        """Create workspace-specific settings  # noqa: E501

        Create new workspace-specific settings on the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_local_settings_with_http_info(body, workspace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsInfoWrapper body: The workspace-specific settings information to upload. (required)
        :param str workspace: The workspace name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'workspace']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_local_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_local_settings`")  # noqa: E501
        # verify the required parameter 'workspace' is set
        if ('workspace' not in params or
                params['workspace'] is None):
            raise ValueError("Missing the required parameter `workspace` when calling `create_local_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workspace' in params:
            path_params['workspace'] = params['workspace']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/workspaces/{workspace}/settings', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_global_contact_info(self, **kwargs):  # noqa: E501
        """Get the global contact information  # noqa: E501

        Displays a list of all global contact settings on the server. This is a subset of what is available at the /settings endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_global_contact_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ContactInfoWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_global_contact_info_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_global_contact_info_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_global_contact_info_with_http_info(self, **kwargs):  # noqa: E501
        """Get the global contact information  # noqa: E501

        Displays a list of all global contact settings on the server. This is a subset of what is available at the /settings endpoint.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_global_contact_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ContactInfoWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_global_contact_info" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/settings/contact', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContactInfoWrapper',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_local_settings(self, workspace, **kwargs):  # noqa: E501
        """Get workspace-specific settings  # noqa: E501

        Displays all workspace-specific settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_local_settings(workspace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace: The workspace name (required)
        :return: SettingsInfoWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_local_settings_with_http_info(workspace, **kwargs)  # noqa: E501
        else:
            (data) = self.get_local_settings_with_http_info(workspace, **kwargs)  # noqa: E501
            return data

    def get_local_settings_with_http_info(self, workspace, **kwargs):  # noqa: E501
        """Get workspace-specific settings  # noqa: E501

        Displays all workspace-specific settings.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_local_settings_with_http_info(workspace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace: The workspace name (required)
        :return: SettingsInfoWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['workspace']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_local_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace' is set
        if ('workspace' not in params or
                params['workspace'] is None):
            raise ValueError("Missing the required parameter `workspace` when calling `get_local_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workspace' in params:
            path_params['workspace'] = params['workspace']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/workspaces/{workspace}/settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SettingsInfoWrapper',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_settings(self, **kwargs):  # noqa: E501
        """Get geoserver global settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_settings(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GeoServerInfoWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_settings_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_settings_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_settings_with_http_info(self, **kwargs):  # noqa: E501
        """Get geoserver global settings  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_settings_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: GeoServerInfoWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_settings" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/settings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GeoServerInfoWrapper',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_global_contact_info(self, body, **kwargs):  # noqa: E501
        """Update contact settings  # noqa: E501

        Updates global contact settings on the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_global_contact_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ContactInfoWrapper body: The contact settings information to upload. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_global_contact_info_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_global_contact_info_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_global_contact_info_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update contact settings  # noqa: E501

        Updates global contact settings on the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_global_contact_info_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ContactInfoWrapper body: The contact settings information to upload. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_global_contact_info" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_global_contact_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/settings/contact', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_local_settings(self, body, workspace, **kwargs):  # noqa: E501
        """Update workspace-specific settings  # noqa: E501

        Updates workspace-specific settings on the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_local_settings(body, workspace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsInfoWrapper body: The workspace-specific settings information to upload. (required)
        :param str workspace: The workspace name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_local_settings_with_http_info(body, workspace, **kwargs)  # noqa: E501
        else:
            (data) = self.update_local_settings_with_http_info(body, workspace, **kwargs)  # noqa: E501
            return data

    def update_local_settings_with_http_info(self, body, workspace, **kwargs):  # noqa: E501
        """Update workspace-specific settings  # noqa: E501

        Updates workspace-specific settings on the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_local_settings_with_http_info(body, workspace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SettingsInfoWrapper body: The workspace-specific settings information to upload. (required)
        :param str workspace: The workspace name (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'workspace']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_local_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_local_settings`")  # noqa: E501
        # verify the required parameter 'workspace' is set
        if ('workspace' not in params or
                params['workspace'] is None):
            raise ValueError("Missing the required parameter `workspace` when calling `update_local_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'workspace' in params:
            path_params['workspace'] = params['workspace']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/workspaces/{workspace}/settings', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_settings(self, body, **kwargs):  # noqa: E501
        """Update the global configuration  # noqa: E501

        Adds a new data store to the workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_settings(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GeoServerInfoWrapper body: global settings upload request body (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_settings_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_settings_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def update_settings_with_http_info(self, body, **kwargs):  # noqa: E501
        """Update the global configuration  # noqa: E501

        Adds a new data store to the workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_settings_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GeoServerInfoWrapper body: global settings upload request body (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_settings" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_settings`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/settings', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

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


class NamespacesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_namespace(self, body, **kwargs):  # noqa: E501
        """Add a new namespace to GeoServer  # noqa: E501

        Adds a new namespace to the server  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_namespace(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NamespaceWrapper body: The Namespace body information to upload. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.add_namespace_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.add_namespace_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def add_namespace_with_http_info(self, body, **kwargs):  # noqa: E501
        """Add a new namespace to GeoServer  # noqa: E501

        Adds a new namespace to the server  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_namespace_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NamespaceWrapper body: The Namespace body information to upload. (required)
        :return: str
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
                    " to method add_namespace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `add_namespace`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/namespaces', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_namespace(self, namespace_prefix, **kwargs):  # noqa: E501
        """Delete a namespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_namespace(namespace_prefix, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace_prefix: The name of the namespace to fetch, or \"default\" to get the default namespace. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_namespace_with_http_info(namespace_prefix, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_namespace_with_http_info(namespace_prefix, **kwargs)  # noqa: E501
            return data

    def delete_namespace_with_http_info(self, namespace_prefix, **kwargs):  # noqa: E501
        """Delete a namespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_namespace_with_http_info(namespace_prefix, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace_prefix: The name of the namespace to fetch, or \"default\" to get the default namespace. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace_prefix']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_namespace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace_prefix' is set
        if ('namespace_prefix' not in params or
                params['namespace_prefix'] is None):
            raise ValueError("Missing the required parameter `namespace_prefix` when calling `delete_namespace`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace_prefix' in params:
            path_params['namespacePrefix'] = params['namespace_prefix']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/namespaces/{namespacePrefix}', 'DELETE',
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

    def get_namespace(self, namespace_prefix, **kwargs):  # noqa: E501
        """Retrieve a namespace  # noqa: E501

        Retrieves a single namespace definition.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_namespace(namespace_prefix, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace_prefix: The name of the namespace to fetch, or \"default\" to get the default namespace. (required)
        :param bool quiet_on_not_found:
        :return: NamespaceWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_namespace_with_http_info(namespace_prefix, **kwargs)  # noqa: E501
        else:
            (data) = self.get_namespace_with_http_info(namespace_prefix, **kwargs)  # noqa: E501
            return data

    def get_namespace_with_http_info(self, namespace_prefix, **kwargs):  # noqa: E501
        """Retrieve a namespace  # noqa: E501

        Retrieves a single namespace definition.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_namespace_with_http_info(namespace_prefix, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str namespace_prefix: The name of the namespace to fetch, or \"default\" to get the default namespace. (required)
        :param bool quiet_on_not_found:
        :return: NamespaceWrapper
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['namespace_prefix', 'quiet_on_not_found']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_namespace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'namespace_prefix' is set
        if ('namespace_prefix' not in params or
                params['namespace_prefix'] is None):
            raise ValueError("Missing the required parameter `namespace_prefix` when calling `get_namespace`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace_prefix' in params:
            path_params['namespacePrefix'] = params['namespace_prefix']  # noqa: E501

        query_params = []
        if 'quiet_on_not_found' in params:
            query_params.append(('quietOnNotFound', params['quiet_on_not_found']))  # noqa: E501

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
            '/namespaces/{namespacePrefix}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NamespaceWrapper',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_namespaces(self, **kwargs):  # noqa: E501
        """Get a list of namespaces  # noqa: E501

        Displays a list of all namespaces on the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_namespaces(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NamespacesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_namespaces_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_namespaces_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_namespaces_with_http_info(self, **kwargs):  # noqa: E501
        """Get a list of namespaces  # noqa: E501

        Displays a list of all namespaces on the server.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_namespaces_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: NamespacesResponse
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
                    " to method get_namespaces" % key
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
            '/namespaces', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NamespacesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_namespace(self, body, namespace_prefix, **kwargs):  # noqa: E501
        """Update a namespace  # noqa: E501

        Takes the body of the put and modifies the namespace from it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_namespace(body, namespace_prefix, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NamespaceWrapper body: The Namespace body information to upload. (required)
        :param str namespace_prefix: The name of the namespace to fetch, or \"default\" to get the default namespace. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_namespace_with_http_info(body, namespace_prefix, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_namespace_with_http_info(body, namespace_prefix, **kwargs)  # noqa: E501
            return data

    def modify_namespace_with_http_info(self, body, namespace_prefix, **kwargs):  # noqa: E501
        """Update a namespace  # noqa: E501

        Takes the body of the put and modifies the namespace from it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_namespace_with_http_info(body, namespace_prefix, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param NamespaceWrapper body: The Namespace body information to upload. (required)
        :param str namespace_prefix: The name of the namespace to fetch, or \"default\" to get the default namespace. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'namespace_prefix']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_namespace" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `modify_namespace`")  # noqa: E501
        # verify the required parameter 'namespace_prefix' is set
        if ('namespace_prefix' not in params or
                params['namespace_prefix'] is None):
            raise ValueError("Missing the required parameter `namespace_prefix` when calling `modify_namespace`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'namespace_prefix' in params:
            path_params['namespacePrefix'] = params['namespace_prefix']  # noqa: E501

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
            '/namespaces/{namespacePrefix}', 'PUT',
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
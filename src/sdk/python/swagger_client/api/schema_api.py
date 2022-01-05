# coding: utf-8

"""
    self-managed-osdu

    Rest API Documentation for Self Managed OSDU  # noqa: E501

    OpenAPI spec version: 0.11.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SchemaApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_schema(self, data_partition_id, body, **kwargs):  # noqa: E501
        """Adds a schema to the schema repository.  # noqa: E501

        Adds a schema to the schema repository. The schemaIdentity must be unique. The `authority`, `source` and `entityType` will be registered if not present. If lower minor versions are registered the service validates the new schema against breaking changes; if breaking changes are discovered the request fails. **Note:** The schema must not reference other schemas with status `DEVELOPMENT`. Scope to a schema will be set by system based on partition id (`SHARED` for common tenant and `INTERNAL` for private tenant). Required roles 'users.datalake.editors' or 'users.datalake.admins' groups to create schema.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_schema(data_partition_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_partition_id: Specifies the data partition to use. This should be either the partition name or crm account ID associated with the partition. (required)
        :param SchemaRequest body: (required)
        :return: SchemaInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_schema_with_http_info(data_partition_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_schema_with_http_info(data_partition_id, body, **kwargs)  # noqa: E501
            return data

    def create_schema_with_http_info(self, data_partition_id, body, **kwargs):  # noqa: E501
        """Adds a schema to the schema repository.  # noqa: E501

        Adds a schema to the schema repository. The schemaIdentity must be unique. The `authority`, `source` and `entityType` will be registered if not present. If lower minor versions are registered the service validates the new schema against breaking changes; if breaking changes are discovered the request fails. **Note:** The schema must not reference other schemas with status `DEVELOPMENT`. Scope to a schema will be set by system based on partition id (`SHARED` for common tenant and `INTERNAL` for private tenant). Required roles 'users.datalake.editors' or 'users.datalake.admins' groups to create schema.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_schema_with_http_info(data_partition_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_partition_id: Specifies the data partition to use. This should be either the partition name or crm account ID associated with the partition. (required)
        :param SchemaRequest body: (required)
        :return: SchemaInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_partition_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_schema" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_partition_id' is set
        if self.api_client.client_side_validation and ('data_partition_id' not in params or
                                                       params['data_partition_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `data_partition_id` when calling `create_schema`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `create_schema`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'data_partition_id' in params:
            header_params['data-partition-id'] = params['data_partition_id']  # noqa: E501

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
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/schema-service/v1/schema', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SchemaInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_schema(self, data_partition_id, id, **kwargs):  # noqa: E501
        """Gets schema from the schema repository.  # noqa: E501

        Retrieve a schema using its system defined id. Required roles 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins' groups to get the schema.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_schema(data_partition_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_partition_id: Specifies the data partition to use. This should be either the partition name or crm account ID associated with the partition. (required)
        :param str id: the system id of the schema (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_schema_with_http_info(data_partition_id, id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_schema_with_http_info(data_partition_id, id, **kwargs)  # noqa: E501
            return data

    def get_schema_with_http_info(self, data_partition_id, id, **kwargs):  # noqa: E501
        """Gets schema from the schema repository.  # noqa: E501

        Retrieve a schema using its system defined id. Required roles 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins' groups to get the schema.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_schema_with_http_info(data_partition_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_partition_id: Specifies the data partition to use. This should be either the partition name or crm account ID associated with the partition. (required)
        :param str id: the system id of the schema (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_partition_id', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_schema" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_partition_id' is set
        if self.api_client.client_side_validation and ('data_partition_id' not in params or
                                                       params['data_partition_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `data_partition_id` when calling `get_schema`")  # noqa: E501
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_schema`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'data_partition_id' in params:
            header_params['data-partition-id'] = params['data_partition_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/schema-service/v1/schema/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_schema_info_repository(self, data_partition_id, **kwargs):  # noqa: E501
        """Searches schemaInfo repository  # noqa: E501

        Searches for information of available schema (SchemInfo) in schema repository. Supports options to filter out the search contents. Required roles 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins' groups to get the schema.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_schema_info_repository(data_partition_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_partition_id: Specifies the data partition to use. This should be either the partition name or crm account ID associated with the partition. (required)
        :param str authority: pass an optional string to search for a specific authority
        :param str source: pass an optional string to search for a specific source
        :param str entity_type: pass an optional string to search for a specific entityType
        :param str schema_version_major: pass an optional string to search for a specific schemaVersionMajor
        :param str schema_version_minor: pass an optional string to search for a specific schemaVersionMinor
        :param str status: The schema status specification
        :param str scope: The scope or schema visibility specification
        :param bool latest_version: if True, only return the latest version
        :param int limit: maximum number of schema records to return
        :param int offset: number of records to skip for pagination
        :return: SchemaInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_schema_info_repository_with_http_info(data_partition_id, **kwargs)  # noqa: E501
        else:
            (data) = self.search_schema_info_repository_with_http_info(data_partition_id, **kwargs)  # noqa: E501
            return data

    def search_schema_info_repository_with_http_info(self, data_partition_id, **kwargs):  # noqa: E501
        """Searches schemaInfo repository  # noqa: E501

        Searches for information of available schema (SchemInfo) in schema repository. Supports options to filter out the search contents. Required roles 'users.datalake.viewers' or 'users.datalake.editors' or 'users.datalake.admins' groups to get the schema.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_schema_info_repository_with_http_info(data_partition_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_partition_id: Specifies the data partition to use. This should be either the partition name or crm account ID associated with the partition. (required)
        :param str authority: pass an optional string to search for a specific authority
        :param str source: pass an optional string to search for a specific source
        :param str entity_type: pass an optional string to search for a specific entityType
        :param str schema_version_major: pass an optional string to search for a specific schemaVersionMajor
        :param str schema_version_minor: pass an optional string to search for a specific schemaVersionMinor
        :param str status: The schema status specification
        :param str scope: The scope or schema visibility specification
        :param bool latest_version: if True, only return the latest version
        :param int limit: maximum number of schema records to return
        :param int offset: number of records to skip for pagination
        :return: SchemaInfoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_partition_id', 'authority', 'source', 'entity_type', 'schema_version_major', 'schema_version_minor', 'status', 'scope', 'latest_version', 'limit', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_schema_info_repository" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_partition_id' is set
        if self.api_client.client_side_validation and ('data_partition_id' not in params or
                                                       params['data_partition_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `data_partition_id` when calling `search_schema_info_repository`")  # noqa: E501

        if self.api_client.client_side_validation and ('limit' in params and params['limit'] > 100):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `search_schema_info_repository`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('limit' in params and params['limit'] < 0):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `search_schema_info_repository`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and ('offset' in params and params['offset'] < 0):  # noqa: E501
            raise ValueError("Invalid value for parameter `offset` when calling `search_schema_info_repository`, must be a value greater than or equal to `0`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'authority' in params:
            query_params.append(('authority', params['authority']))  # noqa: E501
        if 'source' in params:
            query_params.append(('source', params['source']))  # noqa: E501
        if 'entity_type' in params:
            query_params.append(('entityType', params['entity_type']))  # noqa: E501
        if 'schema_version_major' in params:
            query_params.append(('schemaVersionMajor', params['schema_version_major']))  # noqa: E501
        if 'schema_version_minor' in params:
            query_params.append(('schemaVersionMinor', params['schema_version_minor']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'scope' in params:
            query_params.append(('scope', params['scope']))  # noqa: E501
        if 'latest_version' in params:
            query_params.append(('latestVersion', params['latest_version']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}
        if 'data_partition_id' in params:
            header_params['data-partition-id'] = params['data_partition_id']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/schema-service/v1/schema', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SchemaInfoResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_schema(self, data_partition_id, body, **kwargs):  # noqa: E501
        """Creates/Updates a schema in development status  # noqa: E501

        Creates a new schema or updates an already existing schema with status `DEVELOPMENT` in the schema repository. If a user tries to create/update a schema with status other then `DEVELOPMENT`, API will throw an exception. Any schema instance with the same schemaIdentity is replaced (in contrast to the immutability of `PUBLISHED` or `OBSOLETE` schemas). A schema state can also be changed from `DEVELOPMENT` to `PUBLISHED` or `OBSOLETE` while updating schema content or by providing the same schema content. **Note:** The schema may refer to other schema definitions in `DEVELOPMENT` state. If those schemas are updated themselves, it is the developer's responsibility to PUT the dependent schemas again to update the schemas. Scope for a schema can't be updated, its a system defined value. Required roles  'users.datalake.editors' or 'users.datalake.admins' groups to update schema.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_schema(data_partition_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_partition_id: Specifies the data partition to use. This should be either the partition name or crm account ID associated with the partition. (required)
        :param SchemaRequest body: SchemaRequest (required)
        :return: SchemaInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_schema_with_http_info(data_partition_id, body, **kwargs)  # noqa: E501
        else:
            (data) = self.update_schema_with_http_info(data_partition_id, body, **kwargs)  # noqa: E501
            return data

    def update_schema_with_http_info(self, data_partition_id, body, **kwargs):  # noqa: E501
        """Creates/Updates a schema in development status  # noqa: E501

        Creates a new schema or updates an already existing schema with status `DEVELOPMENT` in the schema repository. If a user tries to create/update a schema with status other then `DEVELOPMENT`, API will throw an exception. Any schema instance with the same schemaIdentity is replaced (in contrast to the immutability of `PUBLISHED` or `OBSOLETE` schemas). A schema state can also be changed from `DEVELOPMENT` to `PUBLISHED` or `OBSOLETE` while updating schema content or by providing the same schema content. **Note:** The schema may refer to other schema definitions in `DEVELOPMENT` state. If those schemas are updated themselves, it is the developer's responsibility to PUT the dependent schemas again to update the schemas. Scope for a schema can't be updated, its a system defined value. Required roles  'users.datalake.editors' or 'users.datalake.admins' groups to update schema.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_schema_with_http_info(data_partition_id, body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str data_partition_id: Specifies the data partition to use. This should be either the partition name or crm account ID associated with the partition. (required)
        :param SchemaRequest body: SchemaRequest (required)
        :return: SchemaInfo
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_partition_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_schema" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'data_partition_id' is set
        if self.api_client.client_side_validation and ('data_partition_id' not in params or
                                                       params['data_partition_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `data_partition_id` when calling `update_schema`")  # noqa: E501
        # verify the required parameter 'body' is set
        if self.api_client.client_side_validation and ('body' not in params or
                                                       params['body'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `body` when calling `update_schema`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'data_partition_id' in params:
            header_params['data-partition-id'] = params['data_partition_id']  # noqa: E501

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
        auth_settings = ['Bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/schema-service/v1/schema', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SchemaInfo',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

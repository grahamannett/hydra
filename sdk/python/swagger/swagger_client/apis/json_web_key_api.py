# coding: utf-8

"""
    Hydra OAuth2 & OpenID Connect Server

    Please refer to the user guide for in-depth documentation: https://ory.gitbooks.io/hydra/content/   Hydra offers OAuth 2.0 and OpenID Connect Core 1.0 capabilities as a service. Hydra is different, because it works with any existing authentication infrastructure, not just LDAP or SAML. By implementing a consent app (works with any programming language) you build a bridge between Hydra and your authentication infrastructure. Hydra is able to securely manage JSON Web Keys, and has a sophisticated policy-based access control you can use if you want to. Hydra is suitable for green- (new) and brownfield (existing) projects. If you are not familiar with OAuth 2.0 and are working on a greenfield project, we recommend evaluating if OAuth 2.0 really serves your purpose. Knowledge of OAuth 2.0 is imperative in understanding what Hydra does and how it works.   The official repository is located at https://github.com/ory/hydra   ### Important REST API Documentation Notes  The swagger generator used to create this documentation does currently not support example responses. To see request and response payloads click on **\"Show JSON schema\"**: ![Enable JSON Schema on Apiary](https://storage.googleapis.com/ory.am/hydra/json-schema.png)   The API documentation always refers to the latest tagged version of ORY Hydra. For previous API documentations, please refer to https://github.com/ory/hydra/blob/<tag-id>/docs/api.swagger.yaml - for example:  0.9.13: https://github.com/ory/hydra/blob/v0.9.13/docs/api.swagger.yaml 0.8.1: https://github.com/ory/hydra/blob/v0.8.1/docs/api.swagger.yaml

    OpenAPI spec version: Latest
    Contact: hi@ory.am
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class JsonWebKeyApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_json_web_key_set(self, set, **kwargs):
        """
        Generate a new JSON Web Key
        This endpoint is capable of generating JSON Web Key Sets for you. There a different strategies available, such as symmetric cryptographic keys (HS256, HS512) and asymetric cryptographic keys (RS256, ECDSA).   If the specified JSON Web Key Set does not exist, it will be created.   The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:keys:<set>:<kid>\"], \"actions\": [\"create\"], \"effect\": \"allow\" } ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_json_web_key_set(set, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str set: The set (required)
        :param JsonWebKeySetGeneratorRequest body:
        :return: JsonWebKeySet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_json_web_key_set_with_http_info(set, **kwargs)
        else:
            (data) = self.create_json_web_key_set_with_http_info(set, **kwargs)
            return data

    def create_json_web_key_set_with_http_info(self, set, **kwargs):
        """
        Generate a new JSON Web Key
        This endpoint is capable of generating JSON Web Key Sets for you. There a different strategies available, such as symmetric cryptographic keys (HS256, HS512) and asymetric cryptographic keys (RS256, ECDSA).   If the specified JSON Web Key Set does not exist, it will be created.   The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:keys:<set>:<kid>\"], \"actions\": [\"create\"], \"effect\": \"allow\" } ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_json_web_key_set_with_http_info(set, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str set: The set (required)
        :param JsonWebKeySetGeneratorRequest body:
        :return: JsonWebKeySet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['set', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_json_web_key_set" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'set' is set
        if ('set' not in params) or (params['set'] is None):
            raise ValueError("Missing the required parameter `set` when calling `create_json_web_key_set`")


        collection_formats = {}

        path_params = {}
        if 'set' in params:
            path_params['set'] = params['set']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api('/keys/{set}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='JsonWebKeySet',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_json_web_key(self, kid, set, **kwargs):
        """
        Delete a JSON Web Key
        The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:keys:<set>:<kid>\"], \"actions\": [\"delete\"], \"effect\": \"allow\" } ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_json_web_key(kid, set, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str kid: The kid of the desired key (required)
        :param str set: The set (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_json_web_key_with_http_info(kid, set, **kwargs)
        else:
            (data) = self.delete_json_web_key_with_http_info(kid, set, **kwargs)
            return data

    def delete_json_web_key_with_http_info(self, kid, set, **kwargs):
        """
        Delete a JSON Web Key
        The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:keys:<set>:<kid>\"], \"actions\": [\"delete\"], \"effect\": \"allow\" } ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_json_web_key_with_http_info(kid, set, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str kid: The kid of the desired key (required)
        :param str set: The set (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kid', 'set']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_json_web_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kid' is set
        if ('kid' not in params) or (params['kid'] is None):
            raise ValueError("Missing the required parameter `kid` when calling `delete_json_web_key`")
        # verify the required parameter 'set' is set
        if ('set' not in params) or (params['set'] is None):
            raise ValueError("Missing the required parameter `set` when calling `delete_json_web_key`")


        collection_formats = {}

        path_params = {}
        if 'kid' in params:
            path_params['kid'] = params['kid']
        if 'set' in params:
            path_params['set'] = params['set']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api('/keys/{set}/{kid}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_json_web_key_set(self, set, **kwargs):
        """
        Delete a JSON Web Key
        The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:keys:<set>\"], \"actions\": [\"delete\"], \"effect\": \"allow\" } ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_json_web_key_set(set, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str set: The set (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_json_web_key_set_with_http_info(set, **kwargs)
        else:
            (data) = self.delete_json_web_key_set_with_http_info(set, **kwargs)
            return data

    def delete_json_web_key_set_with_http_info(self, set, **kwargs):
        """
        Delete a JSON Web Key
        The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:keys:<set>\"], \"actions\": [\"delete\"], \"effect\": \"allow\" } ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_json_web_key_set_with_http_info(set, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str set: The set (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['set']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_json_web_key_set" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'set' is set
        if ('set' not in params) or (params['set'] is None):
            raise ValueError("Missing the required parameter `set` when calling `delete_json_web_key_set`")


        collection_formats = {}

        path_params = {}
        if 'set' in params:
            path_params['set'] = params['set']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api('/keys/{set}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_json_web_key(self, kid, set, **kwargs):
        """
        Retrieve a JSON Web Key
        This endpoint can be used to retrieve JWKs stored in ORY Hydra.   The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:keys:<set>:<kid>\"], \"actions\": [\"get\"], \"effect\": \"allow\" } ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_json_web_key(kid, set, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str kid: The kid of the desired key (required)
        :param str set: The set (required)
        :return: JsonWebKeySet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_json_web_key_with_http_info(kid, set, **kwargs)
        else:
            (data) = self.get_json_web_key_with_http_info(kid, set, **kwargs)
            return data

    def get_json_web_key_with_http_info(self, kid, set, **kwargs):
        """
        Retrieve a JSON Web Key
        This endpoint can be used to retrieve JWKs stored in ORY Hydra.   The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:keys:<set>:<kid>\"], \"actions\": [\"get\"], \"effect\": \"allow\" } ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_json_web_key_with_http_info(kid, set, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str kid: The kid of the desired key (required)
        :param str set: The set (required)
        :return: JsonWebKeySet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kid', 'set']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_json_web_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kid' is set
        if ('kid' not in params) or (params['kid'] is None):
            raise ValueError("Missing the required parameter `kid` when calling `get_json_web_key`")
        # verify the required parameter 'set' is set
        if ('set' not in params) or (params['set'] is None):
            raise ValueError("Missing the required parameter `set` when calling `get_json_web_key`")


        collection_formats = {}

        path_params = {}
        if 'kid' in params:
            path_params['kid'] = params['kid']
        if 'set' in params:
            path_params['set'] = params['set']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api('/keys/{set}/{kid}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='JsonWebKeySet',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_json_web_key_set(self, set, **kwargs):
        """
        Retrieve a JSON Web Key Set
        This endpoint can be used to retrieve JWK Sets stored in ORY Hydra.   The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:keys:<set>:<kid>\"], \"actions\": [\"get\"], \"effect\": \"allow\" } ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_json_web_key_set(set, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str set: The set (required)
        :return: JsonWebKeySet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_json_web_key_set_with_http_info(set, **kwargs)
        else:
            (data) = self.get_json_web_key_set_with_http_info(set, **kwargs)
            return data

    def get_json_web_key_set_with_http_info(self, set, **kwargs):
        """
        Retrieve a JSON Web Key Set
        This endpoint can be used to retrieve JWK Sets stored in ORY Hydra.   The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:keys:<set>:<kid>\"], \"actions\": [\"get\"], \"effect\": \"allow\" } ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_json_web_key_set_with_http_info(set, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str set: The set (required)
        :return: JsonWebKeySet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['set']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_json_web_key_set" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'set' is set
        if ('set' not in params) or (params['set'] is None):
            raise ValueError("Missing the required parameter `set` when calling `get_json_web_key_set`")


        collection_formats = {}

        path_params = {}
        if 'set' in params:
            path_params['set'] = params['set']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api('/keys/{set}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='JsonWebKeySet',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_json_web_key(self, kid, set, **kwargs):
        """
        Update a JSON Web Key
        Use this method if you do not want to let Hydra generate the JWKs for you, but instead save your own.   The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:keys:<set>:<kid>\"], \"actions\": [\"update\"], \"effect\": \"allow\" } ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_json_web_key(kid, set, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str kid: The kid of the desired key (required)
        :param str set: The set (required)
        :param JsonWebKey body:
        :return: JsonWebKey
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_json_web_key_with_http_info(kid, set, **kwargs)
        else:
            (data) = self.update_json_web_key_with_http_info(kid, set, **kwargs)
            return data

    def update_json_web_key_with_http_info(self, kid, set, **kwargs):
        """
        Update a JSON Web Key
        Use this method if you do not want to let Hydra generate the JWKs for you, but instead save your own.   The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:keys:<set>:<kid>\"], \"actions\": [\"update\"], \"effect\": \"allow\" } ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_json_web_key_with_http_info(kid, set, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str kid: The kid of the desired key (required)
        :param str set: The set (required)
        :param JsonWebKey body:
        :return: JsonWebKey
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['kid', 'set', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_json_web_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'kid' is set
        if ('kid' not in params) or (params['kid'] is None):
            raise ValueError("Missing the required parameter `kid` when calling `update_json_web_key`")
        # verify the required parameter 'set' is set
        if ('set' not in params) or (params['set'] is None):
            raise ValueError("Missing the required parameter `set` when calling `update_json_web_key`")


        collection_formats = {}

        path_params = {}
        if 'kid' in params:
            path_params['kid'] = params['kid']
        if 'set' in params:
            path_params['set'] = params['set']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api('/keys/{set}/{kid}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='JsonWebKey',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_json_web_key_set(self, set, **kwargs):
        """
        Update a JSON Web Key Set
        Use this method if you do not want to let Hydra generate the JWKs for you, but instead save your own.   The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:keys:<set>\"], \"actions\": [\"update\"], \"effect\": \"allow\" } ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_json_web_key_set(set, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str set: The set (required)
        :param JsonWebKeySet body:
        :return: JsonWebKeySet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_json_web_key_set_with_http_info(set, **kwargs)
        else:
            (data) = self.update_json_web_key_set_with_http_info(set, **kwargs)
            return data

    def update_json_web_key_set_with_http_info(self, set, **kwargs):
        """
        Update a JSON Web Key Set
        Use this method if you do not want to let Hydra generate the JWKs for you, but instead save your own.   The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:keys:<set>\"], \"actions\": [\"update\"], \"effect\": \"allow\" } ```
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_json_web_key_set_with_http_info(set, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str set: The set (required)
        :param JsonWebKeySet body:
        :return: JsonWebKeySet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['set', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_json_web_key_set" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'set' is set
        if ('set' not in params) or (params['set'] is None):
            raise ValueError("Missing the required parameter `set` when calling `update_json_web_key_set`")


        collection_formats = {}

        path_params = {}
        if 'set' in params:
            path_params['set'] = params['set']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['oauth2']

        return self.api_client.call_api('/keys/{set}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='JsonWebKeySet',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

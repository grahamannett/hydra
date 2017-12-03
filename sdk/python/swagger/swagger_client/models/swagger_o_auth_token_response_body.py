# coding: utf-8

"""
    Hydra OAuth2 & OpenID Connect Server

    Please refer to the user guide for in-depth documentation: https://ory.gitbooks.io/hydra/content/   Hydra offers OAuth 2.0 and OpenID Connect Core 1.0 capabilities as a service. Hydra is different, because it works with any existing authentication infrastructure, not just LDAP or SAML. By implementing a consent app (works with any programming language) you build a bridge between Hydra and your authentication infrastructure. Hydra is able to securely manage JSON Web Keys, and has a sophisticated policy-based access control you can use if you want to. Hydra is suitable for green- (new) and brownfield (existing) projects. If you are not familiar with OAuth 2.0 and are working on a greenfield project, we recommend evaluating if OAuth 2.0 really serves your purpose. Knowledge of OAuth 2.0 is imperative in understanding what Hydra does and how it works.   The official repository is located at https://github.com/ory/hydra   ### Important REST API Documentation Notes  The swagger generator used to create this documentation does currently not support example responses. To see request and response payloads click on **\"Show JSON schema\"**: ![Enable JSON Schema on Apiary](https://storage.googleapis.com/ory.am/hydra/json-schema.png)   The API documentation always refers to the latest tagged version of ORY Hydra. For previous API documentations, please refer to https://github.com/ory/hydra/blob/<tag-id>/docs/api.swagger.yaml - for example:  0.9.13: https://github.com/ory/hydra/blob/v0.9.13/docs/api.swagger.yaml 0.8.1: https://github.com/ory/hydra/blob/v0.8.1/docs/api.swagger.yaml

    OpenAPI spec version: Latest
    Contact: hi@ory.am
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SwaggerOAuthTokenResponseBody(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'access_token': 'str',
        'expires_in': 'int',
        'id_token': 'int',
        'refresh_token': 'str',
        'scope': 'int',
        'token_type': 'str'
    }

    attribute_map = {
        'access_token': 'access_token',
        'expires_in': 'expires_in',
        'id_token': 'id_token',
        'refresh_token': 'refresh_token',
        'scope': 'scope',
        'token_type': 'token_type'
    }

    def __init__(self, access_token=None, expires_in=None, id_token=None, refresh_token=None, scope=None, token_type=None):
        """
        SwaggerOAuthTokenResponseBody - a model defined in Swagger
        """

        self._access_token = None
        self._expires_in = None
        self._id_token = None
        self._refresh_token = None
        self._scope = None
        self._token_type = None

        if access_token is not None:
          self.access_token = access_token
        if expires_in is not None:
          self.expires_in = expires_in
        if id_token is not None:
          self.id_token = id_token
        if refresh_token is not None:
          self.refresh_token = refresh_token
        if scope is not None:
          self.scope = scope
        if token_type is not None:
          self.token_type = token_type

    @property
    def access_token(self):
        """
        Gets the access_token of this SwaggerOAuthTokenResponseBody.
        The access token issued by the authorization server.

        :return: The access_token of this SwaggerOAuthTokenResponseBody.
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """
        Sets the access_token of this SwaggerOAuthTokenResponseBody.
        The access token issued by the authorization server.

        :param access_token: The access_token of this SwaggerOAuthTokenResponseBody.
        :type: str
        """

        self._access_token = access_token

    @property
    def expires_in(self):
        """
        Gets the expires_in of this SwaggerOAuthTokenResponseBody.
        The lifetime in seconds of the access token.  For example, the value \"3600\" denotes that the access token will expire in one hour from the time the response was generated.

        :return: The expires_in of this SwaggerOAuthTokenResponseBody.
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """
        Sets the expires_in of this SwaggerOAuthTokenResponseBody.
        The lifetime in seconds of the access token.  For example, the value \"3600\" denotes that the access token will expire in one hour from the time the response was generated.

        :param expires_in: The expires_in of this SwaggerOAuthTokenResponseBody.
        :type: int
        """

        self._expires_in = expires_in

    @property
    def id_token(self):
        """
        Gets the id_token of this SwaggerOAuthTokenResponseBody.
        To retrieve a refresh token request the id_token scope.

        :return: The id_token of this SwaggerOAuthTokenResponseBody.
        :rtype: int
        """
        return self._id_token

    @id_token.setter
    def id_token(self, id_token):
        """
        Sets the id_token of this SwaggerOAuthTokenResponseBody.
        To retrieve a refresh token request the id_token scope.

        :param id_token: The id_token of this SwaggerOAuthTokenResponseBody.
        :type: int
        """

        self._id_token = id_token

    @property
    def refresh_token(self):
        """
        Gets the refresh_token of this SwaggerOAuthTokenResponseBody.
        The refresh token, which can be used to obtain new access tokens. To retrieve it add the scope \"offline\" to your access token request.

        :return: The refresh_token of this SwaggerOAuthTokenResponseBody.
        :rtype: str
        """
        return self._refresh_token

    @refresh_token.setter
    def refresh_token(self, refresh_token):
        """
        Sets the refresh_token of this SwaggerOAuthTokenResponseBody.
        The refresh token, which can be used to obtain new access tokens. To retrieve it add the scope \"offline\" to your access token request.

        :param refresh_token: The refresh_token of this SwaggerOAuthTokenResponseBody.
        :type: str
        """

        self._refresh_token = refresh_token

    @property
    def scope(self):
        """
        Gets the scope of this SwaggerOAuthTokenResponseBody.
        The scope of the access token

        :return: The scope of this SwaggerOAuthTokenResponseBody.
        :rtype: int
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this SwaggerOAuthTokenResponseBody.
        The scope of the access token

        :param scope: The scope of this SwaggerOAuthTokenResponseBody.
        :type: int
        """

        self._scope = scope

    @property
    def token_type(self):
        """
        Gets the token_type of this SwaggerOAuthTokenResponseBody.
        The type of the token issued

        :return: The token_type of this SwaggerOAuthTokenResponseBody.
        :rtype: str
        """
        return self._token_type

    @token_type.setter
    def token_type(self, token_type):
        """
        Sets the token_type of this SwaggerOAuthTokenResponseBody.
        The type of the token issued

        :param token_type: The token_type of this SwaggerOAuthTokenResponseBody.
        :type: str
        """

        self._token_type = token_type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, SwaggerOAuthTokenResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
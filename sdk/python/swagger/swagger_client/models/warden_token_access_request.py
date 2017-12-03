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


class WardenTokenAccessRequest(object):
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
        'action': 'str',
        'context': 'dict(str, object)',
        'resource': 'str',
        'scopes': 'list[str]',
        'token': 'str'
    }

    attribute_map = {
        'action': 'action',
        'context': 'context',
        'resource': 'resource',
        'scopes': 'scopes',
        'token': 'token'
    }

    def __init__(self, action=None, context=None, resource=None, scopes=None, token=None):
        """
        WardenTokenAccessRequest - a model defined in Swagger
        """

        self._action = None
        self._context = None
        self._resource = None
        self._scopes = None
        self._token = None

        if action is not None:
          self.action = action
        if context is not None:
          self.context = context
        if resource is not None:
          self.resource = resource
        if scopes is not None:
          self.scopes = scopes
        if token is not None:
          self.token = token

    @property
    def action(self):
        """
        Gets the action of this WardenTokenAccessRequest.
        Action is the action that is requested on the resource.

        :return: The action of this WardenTokenAccessRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this WardenTokenAccessRequest.
        Action is the action that is requested on the resource.

        :param action: The action of this WardenTokenAccessRequest.
        :type: str
        """

        self._action = action

    @property
    def context(self):
        """
        Gets the context of this WardenTokenAccessRequest.
        Context is the request's environmental context.

        :return: The context of this WardenTokenAccessRequest.
        :rtype: dict(str, object)
        """
        return self._context

    @context.setter
    def context(self, context):
        """
        Sets the context of this WardenTokenAccessRequest.
        Context is the request's environmental context.

        :param context: The context of this WardenTokenAccessRequest.
        :type: dict(str, object)
        """

        self._context = context

    @property
    def resource(self):
        """
        Gets the resource of this WardenTokenAccessRequest.
        Resource is the resource that access is requested to.

        :return: The resource of this WardenTokenAccessRequest.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """
        Sets the resource of this WardenTokenAccessRequest.
        Resource is the resource that access is requested to.

        :param resource: The resource of this WardenTokenAccessRequest.
        :type: str
        """

        self._resource = resource

    @property
    def scopes(self):
        """
        Gets the scopes of this WardenTokenAccessRequest.
        Scopes is an array of scopes that are requried.

        :return: The scopes of this WardenTokenAccessRequest.
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """
        Sets the scopes of this WardenTokenAccessRequest.
        Scopes is an array of scopes that are requried.

        :param scopes: The scopes of this WardenTokenAccessRequest.
        :type: list[str]
        """

        self._scopes = scopes

    @property
    def token(self):
        """
        Gets the token of this WardenTokenAccessRequest.
        Token is the token to introspect.

        :return: The token of this WardenTokenAccessRequest.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """
        Sets the token of this WardenTokenAccessRequest.
        Token is the token to introspect.

        :param token: The token of this WardenTokenAccessRequest.
        :type: str
        """

        self._token = token

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
        if not isinstance(other, WardenTokenAccessRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

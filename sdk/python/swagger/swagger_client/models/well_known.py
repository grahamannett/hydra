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


class WellKnown(object):
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
        'authorization_endpoint': 'str',
        'id_token_signing_alg_values_supported': 'list[str]',
        'issuer': 'str',
        'jwks_uri': 'str',
        'response_types_supported': 'list[str]',
        'subject_types_supported': 'list[str]',
        'token_endpoint': 'str'
    }

    attribute_map = {
        'authorization_endpoint': 'authorization_endpoint',
        'id_token_signing_alg_values_supported': 'id_token_signing_alg_values_supported',
        'issuer': 'issuer',
        'jwks_uri': 'jwks_uri',
        'response_types_supported': 'response_types_supported',
        'subject_types_supported': 'subject_types_supported',
        'token_endpoint': 'token_endpoint'
    }

    def __init__(self, authorization_endpoint=None, id_token_signing_alg_values_supported=None, issuer=None, jwks_uri=None, response_types_supported=None, subject_types_supported=None, token_endpoint=None):
        """
        WellKnown - a model defined in Swagger
        """

        self._authorization_endpoint = None
        self._id_token_signing_alg_values_supported = None
        self._issuer = None
        self._jwks_uri = None
        self._response_types_supported = None
        self._subject_types_supported = None
        self._token_endpoint = None

        self.authorization_endpoint = authorization_endpoint
        self.id_token_signing_alg_values_supported = id_token_signing_alg_values_supported
        self.issuer = issuer
        self.jwks_uri = jwks_uri
        self.response_types_supported = response_types_supported
        self.subject_types_supported = subject_types_supported
        self.token_endpoint = token_endpoint

    @property
    def authorization_endpoint(self):
        """
        Gets the authorization_endpoint of this WellKnown.
        URL of the OP's OAuth 2.0 Authorization Endpoint

        :return: The authorization_endpoint of this WellKnown.
        :rtype: str
        """
        return self._authorization_endpoint

    @authorization_endpoint.setter
    def authorization_endpoint(self, authorization_endpoint):
        """
        Sets the authorization_endpoint of this WellKnown.
        URL of the OP's OAuth 2.0 Authorization Endpoint

        :param authorization_endpoint: The authorization_endpoint of this WellKnown.
        :type: str
        """
        if authorization_endpoint is None:
            raise ValueError("Invalid value for `authorization_endpoint`, must not be `None`")

        self._authorization_endpoint = authorization_endpoint

    @property
    def id_token_signing_alg_values_supported(self):
        """
        Gets the id_token_signing_alg_values_supported of this WellKnown.
        JSON array containing a list of the JWS signing algorithms (alg values) supported by the OP for the ID Token to encode the Claims in a JWT [JWT]. The algorithm RS256 MUST be included. The value none MAY be supported, but MUST NOT be used unless the Response Type used returns no ID Token from the Authorization Endpoint (such as when using the Authorization Code Flow).

        :return: The id_token_signing_alg_values_supported of this WellKnown.
        :rtype: list[str]
        """
        return self._id_token_signing_alg_values_supported

    @id_token_signing_alg_values_supported.setter
    def id_token_signing_alg_values_supported(self, id_token_signing_alg_values_supported):
        """
        Sets the id_token_signing_alg_values_supported of this WellKnown.
        JSON array containing a list of the JWS signing algorithms (alg values) supported by the OP for the ID Token to encode the Claims in a JWT [JWT]. The algorithm RS256 MUST be included. The value none MAY be supported, but MUST NOT be used unless the Response Type used returns no ID Token from the Authorization Endpoint (such as when using the Authorization Code Flow).

        :param id_token_signing_alg_values_supported: The id_token_signing_alg_values_supported of this WellKnown.
        :type: list[str]
        """
        if id_token_signing_alg_values_supported is None:
            raise ValueError("Invalid value for `id_token_signing_alg_values_supported`, must not be `None`")

        self._id_token_signing_alg_values_supported = id_token_signing_alg_values_supported

    @property
    def issuer(self):
        """
        Gets the issuer of this WellKnown.
        URL using the https scheme with no query or fragment component that the OP asserts as its Issuer Identifier. If Issuer discovery is supported , this value MUST be identical to the issuer value returned by WebFinger. This also MUST be identical to the iss Claim value in ID Tokens issued from this Issuer.

        :return: The issuer of this WellKnown.
        :rtype: str
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """
        Sets the issuer of this WellKnown.
        URL using the https scheme with no query or fragment component that the OP asserts as its Issuer Identifier. If Issuer discovery is supported , this value MUST be identical to the issuer value returned by WebFinger. This also MUST be identical to the iss Claim value in ID Tokens issued from this Issuer.

        :param issuer: The issuer of this WellKnown.
        :type: str
        """
        if issuer is None:
            raise ValueError("Invalid value for `issuer`, must not be `None`")

        self._issuer = issuer

    @property
    def jwks_uri(self):
        """
        Gets the jwks_uri of this WellKnown.
        URL of the OP's JSON Web Key Set [JWK] document. This contains the signing key(s) the RP uses to validate signatures from the OP. The JWK Set MAY also contain the Server's encryption key(s), which are used by RPs to encrypt requests to the Server. When both signing and encryption keys are made available, a use (Key Use) parameter value is REQUIRED for all keys in the referenced JWK Set to indicate each key's intended usage. Although some algorithms allow the same key to be used for both signatures and encryption, doing so is NOT RECOMMENDED, as it is less secure. The JWK x5c parameter MAY be used to provide X.509 representations of keys provided. When used, the bare key values MUST still be present and MUST match those in the certificate.

        :return: The jwks_uri of this WellKnown.
        :rtype: str
        """
        return self._jwks_uri

    @jwks_uri.setter
    def jwks_uri(self, jwks_uri):
        """
        Sets the jwks_uri of this WellKnown.
        URL of the OP's JSON Web Key Set [JWK] document. This contains the signing key(s) the RP uses to validate signatures from the OP. The JWK Set MAY also contain the Server's encryption key(s), which are used by RPs to encrypt requests to the Server. When both signing and encryption keys are made available, a use (Key Use) parameter value is REQUIRED for all keys in the referenced JWK Set to indicate each key's intended usage. Although some algorithms allow the same key to be used for both signatures and encryption, doing so is NOT RECOMMENDED, as it is less secure. The JWK x5c parameter MAY be used to provide X.509 representations of keys provided. When used, the bare key values MUST still be present and MUST match those in the certificate.

        :param jwks_uri: The jwks_uri of this WellKnown.
        :type: str
        """
        if jwks_uri is None:
            raise ValueError("Invalid value for `jwks_uri`, must not be `None`")

        self._jwks_uri = jwks_uri

    @property
    def response_types_supported(self):
        """
        Gets the response_types_supported of this WellKnown.
        JSON array containing a list of the OAuth 2.0 response_type values that this OP supports. Dynamic OpenID Providers MUST support the code, id_token, and the token id_token Response Type values.

        :return: The response_types_supported of this WellKnown.
        :rtype: list[str]
        """
        return self._response_types_supported

    @response_types_supported.setter
    def response_types_supported(self, response_types_supported):
        """
        Sets the response_types_supported of this WellKnown.
        JSON array containing a list of the OAuth 2.0 response_type values that this OP supports. Dynamic OpenID Providers MUST support the code, id_token, and the token id_token Response Type values.

        :param response_types_supported: The response_types_supported of this WellKnown.
        :type: list[str]
        """
        if response_types_supported is None:
            raise ValueError("Invalid value for `response_types_supported`, must not be `None`")

        self._response_types_supported = response_types_supported

    @property
    def subject_types_supported(self):
        """
        Gets the subject_types_supported of this WellKnown.
        JSON array containing a list of the Subject Identifier types that this OP supports. Valid types include pairwise and public.

        :return: The subject_types_supported of this WellKnown.
        :rtype: list[str]
        """
        return self._subject_types_supported

    @subject_types_supported.setter
    def subject_types_supported(self, subject_types_supported):
        """
        Sets the subject_types_supported of this WellKnown.
        JSON array containing a list of the Subject Identifier types that this OP supports. Valid types include pairwise and public.

        :param subject_types_supported: The subject_types_supported of this WellKnown.
        :type: list[str]
        """
        if subject_types_supported is None:
            raise ValueError("Invalid value for `subject_types_supported`, must not be `None`")

        self._subject_types_supported = subject_types_supported

    @property
    def token_endpoint(self):
        """
        Gets the token_endpoint of this WellKnown.
        URL of the OP's OAuth 2.0 Token Endpoint

        :return: The token_endpoint of this WellKnown.
        :rtype: str
        """
        return self._token_endpoint

    @token_endpoint.setter
    def token_endpoint(self, token_endpoint):
        """
        Sets the token_endpoint of this WellKnown.
        URL of the OP's OAuth 2.0 Token Endpoint

        :param token_endpoint: The token_endpoint of this WellKnown.
        :type: str
        """
        if token_endpoint is None:
            raise ValueError("Invalid value for `token_endpoint`, must not be `None`")

        self._token_endpoint = token_endpoint

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
        if not isinstance(other, WellKnown):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

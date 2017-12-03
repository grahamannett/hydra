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


class JsonWebKey(object):
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
        'alg': 'str',
        'crv': 'str',
        'd': 'str',
        'dp': 'str',
        'dq': 'str',
        'e': 'str',
        'k': 'str',
        'kid': 'str',
        'kty': 'str',
        'n': 'str',
        'p': 'str',
        'q': 'str',
        'qi': 'str',
        'use': 'str',
        'x': 'str',
        'x5c': 'list[str]',
        'y': 'str'
    }

    attribute_map = {
        'alg': 'alg',
        'crv': 'crv',
        'd': 'd',
        'dp': 'dp',
        'dq': 'dq',
        'e': 'e',
        'k': 'k',
        'kid': 'kid',
        'kty': 'kty',
        'n': 'n',
        'p': 'p',
        'q': 'q',
        'qi': 'qi',
        'use': 'use',
        'x': 'x',
        'x5c': 'x5c',
        'y': 'y'
    }

    def __init__(self, alg=None, crv=None, d=None, dp=None, dq=None, e=None, k=None, kid=None, kty=None, n=None, p=None, q=None, qi=None, use=None, x=None, x5c=None, y=None):
        """
        JsonWebKey - a model defined in Swagger
        """

        self._alg = None
        self._crv = None
        self._d = None
        self._dp = None
        self._dq = None
        self._e = None
        self._k = None
        self._kid = None
        self._kty = None
        self._n = None
        self._p = None
        self._q = None
        self._qi = None
        self._use = None
        self._x = None
        self._x5c = None
        self._y = None

        if alg is not None:
          self.alg = alg
        if crv is not None:
          self.crv = crv
        if d is not None:
          self.d = d
        if dp is not None:
          self.dp = dp
        if dq is not None:
          self.dq = dq
        if e is not None:
          self.e = e
        if k is not None:
          self.k = k
        if kid is not None:
          self.kid = kid
        if kty is not None:
          self.kty = kty
        if n is not None:
          self.n = n
        if p is not None:
          self.p = p
        if q is not None:
          self.q = q
        if qi is not None:
          self.qi = qi
        if use is not None:
          self.use = use
        if x is not None:
          self.x = x
        if x5c is not None:
          self.x5c = x5c
        if y is not None:
          self.y = y

    @property
    def alg(self):
        """
        Gets the alg of this JsonWebKey.
        The \"alg\" (algorithm) parameter identifies the algorithm intended for use with the key.  The values used should either be registered in the IANA \"JSON Web Signature and Encryption Algorithms\" registry established by [JWA] or be a value that contains a Collision- Resistant Name.

        :return: The alg of this JsonWebKey.
        :rtype: str
        """
        return self._alg

    @alg.setter
    def alg(self, alg):
        """
        Sets the alg of this JsonWebKey.
        The \"alg\" (algorithm) parameter identifies the algorithm intended for use with the key.  The values used should either be registered in the IANA \"JSON Web Signature and Encryption Algorithms\" registry established by [JWA] or be a value that contains a Collision- Resistant Name.

        :param alg: The alg of this JsonWebKey.
        :type: str
        """

        self._alg = alg

    @property
    def crv(self):
        """
        Gets the crv of this JsonWebKey.

        :return: The crv of this JsonWebKey.
        :rtype: str
        """
        return self._crv

    @crv.setter
    def crv(self, crv):
        """
        Sets the crv of this JsonWebKey.

        :param crv: The crv of this JsonWebKey.
        :type: str
        """

        self._crv = crv

    @property
    def d(self):
        """
        Gets the d of this JsonWebKey.

        :return: The d of this JsonWebKey.
        :rtype: str
        """
        return self._d

    @d.setter
    def d(self, d):
        """
        Sets the d of this JsonWebKey.

        :param d: The d of this JsonWebKey.
        :type: str
        """

        self._d = d

    @property
    def dp(self):
        """
        Gets the dp of this JsonWebKey.

        :return: The dp of this JsonWebKey.
        :rtype: str
        """
        return self._dp

    @dp.setter
    def dp(self, dp):
        """
        Sets the dp of this JsonWebKey.

        :param dp: The dp of this JsonWebKey.
        :type: str
        """

        self._dp = dp

    @property
    def dq(self):
        """
        Gets the dq of this JsonWebKey.

        :return: The dq of this JsonWebKey.
        :rtype: str
        """
        return self._dq

    @dq.setter
    def dq(self, dq):
        """
        Sets the dq of this JsonWebKey.

        :param dq: The dq of this JsonWebKey.
        :type: str
        """

        self._dq = dq

    @property
    def e(self):
        """
        Gets the e of this JsonWebKey.

        :return: The e of this JsonWebKey.
        :rtype: str
        """
        return self._e

    @e.setter
    def e(self, e):
        """
        Sets the e of this JsonWebKey.

        :param e: The e of this JsonWebKey.
        :type: str
        """

        self._e = e

    @property
    def k(self):
        """
        Gets the k of this JsonWebKey.

        :return: The k of this JsonWebKey.
        :rtype: str
        """
        return self._k

    @k.setter
    def k(self, k):
        """
        Sets the k of this JsonWebKey.

        :param k: The k of this JsonWebKey.
        :type: str
        """

        self._k = k

    @property
    def kid(self):
        """
        Gets the kid of this JsonWebKey.
        The \"kid\" (key ID) parameter is used to match a specific key.  This is used, for instance, to choose among a set of keys within a JWK Set during key rollover.  The structure of the \"kid\" value is unspecified.  When \"kid\" values are used within a JWK Set, different keys within the JWK Set SHOULD use distinct \"kid\" values.  (One example in which different keys might use the same \"kid\" value is if they have different \"kty\" (key type) values but are considered to be equivalent alternatives by the application using them.)  The \"kid\" value is a case-sensitive string.

        :return: The kid of this JsonWebKey.
        :rtype: str
        """
        return self._kid

    @kid.setter
    def kid(self, kid):
        """
        Sets the kid of this JsonWebKey.
        The \"kid\" (key ID) parameter is used to match a specific key.  This is used, for instance, to choose among a set of keys within a JWK Set during key rollover.  The structure of the \"kid\" value is unspecified.  When \"kid\" values are used within a JWK Set, different keys within the JWK Set SHOULD use distinct \"kid\" values.  (One example in which different keys might use the same \"kid\" value is if they have different \"kty\" (key type) values but are considered to be equivalent alternatives by the application using them.)  The \"kid\" value is a case-sensitive string.

        :param kid: The kid of this JsonWebKey.
        :type: str
        """

        self._kid = kid

    @property
    def kty(self):
        """
        Gets the kty of this JsonWebKey.
        The \"kty\" (key type) parameter identifies the cryptographic algorithm family used with the key, such as \"RSA\" or \"EC\". \"kty\" values should either be registered in the IANA \"JSON Web Key Types\" registry established by [JWA] or be a value that contains a Collision- Resistant Name.  The \"kty\" value is a case-sensitive string.

        :return: The kty of this JsonWebKey.
        :rtype: str
        """
        return self._kty

    @kty.setter
    def kty(self, kty):
        """
        Sets the kty of this JsonWebKey.
        The \"kty\" (key type) parameter identifies the cryptographic algorithm family used with the key, such as \"RSA\" or \"EC\". \"kty\" values should either be registered in the IANA \"JSON Web Key Types\" registry established by [JWA] or be a value that contains a Collision- Resistant Name.  The \"kty\" value is a case-sensitive string.

        :param kty: The kty of this JsonWebKey.
        :type: str
        """

        self._kty = kty

    @property
    def n(self):
        """
        Gets the n of this JsonWebKey.

        :return: The n of this JsonWebKey.
        :rtype: str
        """
        return self._n

    @n.setter
    def n(self, n):
        """
        Sets the n of this JsonWebKey.

        :param n: The n of this JsonWebKey.
        :type: str
        """

        self._n = n

    @property
    def p(self):
        """
        Gets the p of this JsonWebKey.

        :return: The p of this JsonWebKey.
        :rtype: str
        """
        return self._p

    @p.setter
    def p(self, p):
        """
        Sets the p of this JsonWebKey.

        :param p: The p of this JsonWebKey.
        :type: str
        """

        self._p = p

    @property
    def q(self):
        """
        Gets the q of this JsonWebKey.

        :return: The q of this JsonWebKey.
        :rtype: str
        """
        return self._q

    @q.setter
    def q(self, q):
        """
        Sets the q of this JsonWebKey.

        :param q: The q of this JsonWebKey.
        :type: str
        """

        self._q = q

    @property
    def qi(self):
        """
        Gets the qi of this JsonWebKey.

        :return: The qi of this JsonWebKey.
        :rtype: str
        """
        return self._qi

    @qi.setter
    def qi(self, qi):
        """
        Sets the qi of this JsonWebKey.

        :param qi: The qi of this JsonWebKey.
        :type: str
        """

        self._qi = qi

    @property
    def use(self):
        """
        Gets the use of this JsonWebKey.
        The \"use\" (public key use) parameter identifies the intended use of the public key. The \"use\" parameter is employed to indicate whether a public key is used for encrypting data or verifying the signature on data. Values are commonly \"sig\" (signature) or \"enc\" (encryption).

        :return: The use of this JsonWebKey.
        :rtype: str
        """
        return self._use

    @use.setter
    def use(self, use):
        """
        Sets the use of this JsonWebKey.
        The \"use\" (public key use) parameter identifies the intended use of the public key. The \"use\" parameter is employed to indicate whether a public key is used for encrypting data or verifying the signature on data. Values are commonly \"sig\" (signature) or \"enc\" (encryption).

        :param use: The use of this JsonWebKey.
        :type: str
        """

        self._use = use

    @property
    def x(self):
        """
        Gets the x of this JsonWebKey.

        :return: The x of this JsonWebKey.
        :rtype: str
        """
        return self._x

    @x.setter
    def x(self, x):
        """
        Sets the x of this JsonWebKey.

        :param x: The x of this JsonWebKey.
        :type: str
        """

        self._x = x

    @property
    def x5c(self):
        """
        Gets the x5c of this JsonWebKey.
        The \"x5c\" (X.509 certificate chain) parameter contains a chain of one or more PKIX certificates [RFC5280].  The certificate chain is represented as a JSON array of certificate value strings.  Each string in the array is a base64-encoded (Section 4 of [RFC4648] -- not base64url-encoded) DER [ITU.X690.1994] PKIX certificate value. The PKIX certificate containing the key value MUST be the first certificate.

        :return: The x5c of this JsonWebKey.
        :rtype: list[str]
        """
        return self._x5c

    @x5c.setter
    def x5c(self, x5c):
        """
        Sets the x5c of this JsonWebKey.
        The \"x5c\" (X.509 certificate chain) parameter contains a chain of one or more PKIX certificates [RFC5280].  The certificate chain is represented as a JSON array of certificate value strings.  Each string in the array is a base64-encoded (Section 4 of [RFC4648] -- not base64url-encoded) DER [ITU.X690.1994] PKIX certificate value. The PKIX certificate containing the key value MUST be the first certificate.

        :param x5c: The x5c of this JsonWebKey.
        :type: list[str]
        """

        self._x5c = x5c

    @property
    def y(self):
        """
        Gets the y of this JsonWebKey.

        :return: The y of this JsonWebKey.
        :rtype: str
        """
        return self._y

    @y.setter
    def y(self, y):
        """
        Sets the y of this JsonWebKey.

        :param y: The y of this JsonWebKey.
        :type: str
        """

        self._y = y

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
        if not isinstance(other, JsonWebKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

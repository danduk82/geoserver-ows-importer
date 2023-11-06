# coding: utf-8

"""
    GeoServer Workspace

    A workspace is a grouping of data stores. Similar to a namespace, it is used to group data that is related in some way.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NamespaceInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'prefix': 'str',
        'uri': 'str',
        'isolated': 'bool'
    }

    attribute_map = {
        'prefix': 'prefix',
        'uri': 'uri',
        'isolated': 'isolated'
    }

    def __init__(self, prefix=None, uri=None, isolated=None):  # noqa: E501
        """NamespaceInfo - a model defined in Swagger"""  # noqa: E501
        self._prefix = None
        self._uri = None
        self._isolated = None
        self.discriminator = None
        if prefix is not None:
            self.prefix = prefix
        if uri is not None:
            self.uri = uri
        if isolated is not None:
            self.isolated = isolated

    @property
    def prefix(self):
        """Gets the prefix of this NamespaceInfo.  # noqa: E501

        The name of the namespace.  # noqa: E501

        :return: The prefix of this NamespaceInfo.  # noqa: E501
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """Sets the prefix of this NamespaceInfo.

        The name of the namespace.  # noqa: E501

        :param prefix: The prefix of this NamespaceInfo.  # noqa: E501
        :type: str
        """

        self._prefix = prefix

    @property
    def uri(self):
        """Gets the uri of this NamespaceInfo.  # noqa: E501

        URL to the namespace.  # noqa: E501

        :return: The uri of this NamespaceInfo.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this NamespaceInfo.

        URL to the namespace.  # noqa: E501

        :param uri: The uri of this NamespaceInfo.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def isolated(self):
        """Gets the isolated of this NamespaceInfo.  # noqa: E501

        Isolated workspaces content is only visible and queryable in the context of a virtual service bound to the isolated workspace.  # noqa: E501

        :return: The isolated of this NamespaceInfo.  # noqa: E501
        :rtype: bool
        """
        return self._isolated

    @isolated.setter
    def isolated(self, isolated):
        """Sets the isolated of this NamespaceInfo.

        Isolated workspaces content is only visible and queryable in the context of a virtual service bound to the isolated workspace.  # noqa: E501

        :param isolated: The isolated of this NamespaceInfo.  # noqa: E501
        :type: bool
        """

        self._isolated = isolated

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(NamespaceInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NamespaceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
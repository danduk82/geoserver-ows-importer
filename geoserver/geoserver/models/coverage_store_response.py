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

class CoverageStoreResponse(object):
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
        'name': 'str',
        'description': 'str',
        'type': 'str',
        'enabled': 'bool',
        'workspace': 'CatalogresponsesYamlcomponentsschemasNamedLink',
        'url': 'str',
        'coverages': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'type': 'type',
        'enabled': 'enabled',
        'workspace': 'workspace',
        'url': 'url',
        'coverages': 'coverages'
    }

    def __init__(self, name=None, description=None, type=None, enabled=None, workspace=None, url=None, coverages=None):  # noqa: E501
        """CoverageStoreResponse - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._type = None
        self._enabled = None
        self._workspace = None
        self._url = None
        self._coverages = None
        self.discriminator = None
        self.name = name
        if description is not None:
            self.description = description
        self.type = type
        if enabled is not None:
            self.enabled = enabled
        if workspace is not None:
            self.workspace = workspace
        if url is not None:
            self.url = url
        if coverages is not None:
            self.coverages = coverages

    @property
    def name(self):
        """Gets the name of this CoverageStoreResponse.  # noqa: E501

        Name of the coverage store  # noqa: E501

        :return: The name of this CoverageStoreResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CoverageStoreResponse.

        Name of the coverage store  # noqa: E501

        :param name: The name of this CoverageStoreResponse.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CoverageStoreResponse.  # noqa: E501

        Description of the coverage store  # noqa: E501

        :return: The description of this CoverageStoreResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CoverageStoreResponse.

        Description of the coverage store  # noqa: E501

        :param description: The description of this CoverageStoreResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this CoverageStoreResponse.  # noqa: E501

        Type of coverage store  # noqa: E501

        :return: The type of this CoverageStoreResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CoverageStoreResponse.

        Type of coverage store  # noqa: E501

        :param type: The type of this CoverageStoreResponse.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def enabled(self):
        """Gets the enabled of this CoverageStoreResponse.  # noqa: E501

        Whether the store is enabled, or not  # noqa: E501

        :return: The enabled of this CoverageStoreResponse.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CoverageStoreResponse.

        Whether the store is enabled, or not  # noqa: E501

        :param enabled: The enabled of this CoverageStoreResponse.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def workspace(self):
        """Gets the workspace of this CoverageStoreResponse.  # noqa: E501


        :return: The workspace of this CoverageStoreResponse.  # noqa: E501
        :rtype: CatalogresponsesYamlcomponentsschemasNamedLink
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this CoverageStoreResponse.


        :param workspace: The workspace of this CoverageStoreResponse.  # noqa: E501
        :type: CatalogresponsesYamlcomponentsschemasNamedLink
        """

        self._workspace = workspace

    @property
    def url(self):
        """Gets the url of this CoverageStoreResponse.  # noqa: E501

        Location of the raster data source (often, but not necessarily, a file). Can be relative to the data directory.  # noqa: E501

        :return: The url of this CoverageStoreResponse.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this CoverageStoreResponse.

        Location of the raster data source (often, but not necessarily, a file). Can be relative to the data directory.  # noqa: E501

        :param url: The url of this CoverageStoreResponse.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def coverages(self):
        """Gets the coverages of this CoverageStoreResponse.  # noqa: E501

        URL to the list of coverages contained in this store  # noqa: E501

        :return: The coverages of this CoverageStoreResponse.  # noqa: E501
        :rtype: str
        """
        return self._coverages

    @coverages.setter
    def coverages(self, coverages):
        """Sets the coverages of this CoverageStoreResponse.

        URL to the list of coverages contained in this store  # noqa: E501

        :param coverages: The coverages of this CoverageStoreResponse.  # noqa: E501
        :type: str
        """

        self._coverages = coverages

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
        if issubclass(CoverageStoreResponse, dict):
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
        if not isinstance(other, CoverageStoreResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

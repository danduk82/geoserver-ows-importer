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

class StyleInfo(object):
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
        'workspace': 'WorkspaceInfo',
        'format': 'str',
        'format_version': 'Version',
        'language_version': 'Version',
        'filename': 'str',
        'legend': 'LegendInfo'
    }

    attribute_map = {
        'name': 'name',
        'workspace': 'workspace',
        'format': 'format',
        'format_version': 'formatVersion',
        'language_version': 'languageVersion',
        'filename': 'filename',
        'legend': 'legend'
    }

    def __init__(self, name=None, workspace=None, format=None, format_version=None, language_version=None, filename=None, legend=None):  # noqa: E501
        """StyleInfo - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._workspace = None
        self._format = None
        self._format_version = None
        self._language_version = None
        self._filename = None
        self._legend = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if workspace is not None:
            self.workspace = workspace
        if format is not None:
            self.format = format
        if format_version is not None:
            self.format_version = format_version
        if language_version is not None:
            self.language_version = language_version
        if filename is not None:
            self.filename = filename
        if legend is not None:
            self.legend = legend

    @property
    def name(self):
        """Gets the name of this StyleInfo.  # noqa: E501

        Name of the style. This value is unique among all styles and can be used to identify the style.  # noqa: E501

        :return: The name of this StyleInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StyleInfo.

        Name of the style. This value is unique among all styles and can be used to identify the style.  # noqa: E501

        :param name: The name of this StyleInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def workspace(self):
        """Gets the workspace of this StyleInfo.  # noqa: E501


        :return: The workspace of this StyleInfo.  # noqa: E501
        :rtype: WorkspaceInfo
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this StyleInfo.


        :param workspace: The workspace of this StyleInfo.  # noqa: E501
        :type: WorkspaceInfo
        """

        self._workspace = workspace

    @property
    def format(self):
        """Gets the format of this StyleInfo.  # noqa: E501

        The styling language/format for the style, for example: \"sld\"  # noqa: E501

        :return: The format of this StyleInfo.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this StyleInfo.

        The styling language/format for the style, for example: \"sld\"  # noqa: E501

        :param format: The format of this StyleInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["sld", "mbstyle"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"  # noqa: E501
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def format_version(self):
        """Gets the format_version of this StyleInfo.  # noqa: E501


        :return: The format_version of this StyleInfo.  # noqa: E501
        :rtype: Version
        """
        return self._format_version

    @format_version.setter
    def format_version(self, format_version):
        """Sets the format_version of this StyleInfo.


        :param format_version: The format_version of this StyleInfo.  # noqa: E501
        :type: Version
        """

        self._format_version = format_version

    @property
    def language_version(self):
        """Gets the language_version of this StyleInfo.  # noqa: E501


        :return: The language_version of this StyleInfo.  # noqa: E501
        :rtype: Version
        """
        return self._language_version

    @language_version.setter
    def language_version(self, language_version):
        """Sets the language_version of this StyleInfo.


        :param language_version: The language_version of this StyleInfo.  # noqa: E501
        :type: Version
        """

        self._language_version = language_version

    @property
    def filename(self):
        """Gets the filename of this StyleInfo.  # noqa: E501

        name of the file the style originates from.  # noqa: E501

        :return: The filename of this StyleInfo.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this StyleInfo.

        name of the file the style originates from.  # noqa: E501

        :param filename: The filename of this StyleInfo.  # noqa: E501
        :type: str
        """

        self._filename = filename

    @property
    def legend(self):
        """Gets the legend of this StyleInfo.  # noqa: E501


        :return: The legend of this StyleInfo.  # noqa: E501
        :rtype: LegendInfo
        """
        return self._legend

    @legend.setter
    def legend(self, legend):
        """Sets the legend of this StyleInfo.


        :param legend: The legend of this StyleInfo.  # noqa: E501
        :type: LegendInfo
        """

        self._legend = legend

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
        if issubclass(StyleInfo, dict):
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
        if not isinstance(other, StyleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

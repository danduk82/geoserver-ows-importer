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
from geoserver.models.service_info import ServiceInfo  # noqa: F401,E501

class WFSInfo(ServiceInfo):
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
        'gml': 'WFSInfoGmlSettings',
        'service_level': 'WFSServiceLevel',
        'max_features': 'int',
        'feature_bounding': 'bool',
        'canonical_schema_location': 'bool',
        'encode_feature_member': 'bool',
        'hits_ignore_max_features': 'bool'
    }
    if hasattr(ServiceInfo, "swagger_types"):
        swagger_types.update(ServiceInfo.swagger_types)

    attribute_map = {
        'gml': 'gml',
        'service_level': 'serviceLevel',
        'max_features': 'maxFeatures',
        'feature_bounding': 'featureBounding',
        'canonical_schema_location': 'canonicalSchemaLocation',
        'encode_feature_member': 'encodeFeatureMember',
        'hits_ignore_max_features': 'hitsIgnoreMaxFeatures'
    }
    if hasattr(ServiceInfo, "attribute_map"):
        attribute_map.update(ServiceInfo.attribute_map)

    def __init__(self, gml=None, service_level=None, max_features=None, feature_bounding=None, canonical_schema_location=None, encode_feature_member=None, hits_ignore_max_features=None, *args, **kwargs):  # noqa: E501
        """WFSInfo - a model defined in Swagger"""  # noqa: E501
        self._gml = None
        self._service_level = None
        self._max_features = None
        self._feature_bounding = None
        self._canonical_schema_location = None
        self._encode_feature_member = None
        self._hits_ignore_max_features = None
        self.discriminator = None
        if gml is not None:
            self.gml = gml
        if service_level is not None:
            self.service_level = service_level
        if max_features is not None:
            self.max_features = max_features
        if feature_bounding is not None:
            self.feature_bounding = feature_bounding
        if canonical_schema_location is not None:
            self.canonical_schema_location = canonical_schema_location
        if encode_feature_member is not None:
            self.encode_feature_member = encode_feature_member
        if hits_ignore_max_features is not None:
            self.hits_ignore_max_features = hits_ignore_max_features
        ServiceInfo.__init__(self, *args, **kwargs)

    @property
    def gml(self):
        """Gets the gml of this WFSInfo.  # noqa: E501


        :return: The gml of this WFSInfo.  # noqa: E501
        :rtype: WFSInfoGmlSettings
        """
        return self._gml

    @gml.setter
    def gml(self, gml):
        """Sets the gml of this WFSInfo.


        :param gml: The gml of this WFSInfo.  # noqa: E501
        :type: WFSInfoGmlSettings
        """

        self._gml = gml

    @property
    def service_level(self):
        """Gets the service_level of this WFSInfo.  # noqa: E501


        :return: The service_level of this WFSInfo.  # noqa: E501
        :rtype: WFSServiceLevel
        """
        return self._service_level

    @service_level.setter
    def service_level(self, service_level):
        """Sets the service_level of this WFSInfo.


        :param service_level: The service_level of this WFSInfo.  # noqa: E501
        :type: WFSServiceLevel
        """

        self._service_level = service_level

    @property
    def max_features(self):
        """Gets the max_features of this WFSInfo.  # noqa: E501

        Global cap on the number of features to allow when processing a request  # noqa: E501

        :return: The max_features of this WFSInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_features

    @max_features.setter
    def max_features(self, max_features):
        """Sets the max_features of this WFSInfo.

        Global cap on the number of features to allow when processing a request  # noqa: E501

        :param max_features: The max_features of this WFSInfo.  # noqa: E501
        :type: int
        """

        self._max_features = max_features

    @property
    def feature_bounding(self):
        """Gets the feature_bounding of this WFSInfo.  # noqa: E501

        Flag which determines if gml:bounds elements should be encoded at the feature level in GML output  # noqa: E501

        :return: The feature_bounding of this WFSInfo.  # noqa: E501
        :rtype: bool
        """
        return self._feature_bounding

    @feature_bounding.setter
    def feature_bounding(self, feature_bounding):
        """Sets the feature_bounding of this WFSInfo.

        Flag which determines if gml:bounds elements should be encoded at the feature level in GML output  # noqa: E501

        :param feature_bounding: The feature_bounding of this WFSInfo.  # noqa: E501
        :type: bool
        """

        self._feature_bounding = feature_bounding

    @property
    def canonical_schema_location(self):
        """Gets the canonical_schema_location of this WFSInfo.  # noqa: E501

        Flag that determines the encoding of the WFS schemaLocation. True if the WFS schemaLocation should refer to the canonical location, false if the WFS schemaLocation should refer to a copy served by GeoServer.  # noqa: E501

        :return: The canonical_schema_location of this WFSInfo.  # noqa: E501
        :rtype: bool
        """
        return self._canonical_schema_location

    @canonical_schema_location.setter
    def canonical_schema_location(self, canonical_schema_location):
        """Sets the canonical_schema_location of this WFSInfo.

        Flag that determines the encoding of the WFS schemaLocation. True if the WFS schemaLocation should refer to the canonical location, false if the WFS schemaLocation should refer to a copy served by GeoServer.  # noqa: E501

        :param canonical_schema_location: The canonical_schema_location of this WFSInfo.  # noqa: E501
        :type: bool
        """

        self._canonical_schema_location = canonical_schema_location

    @property
    def encode_feature_member(self):
        """Gets the encode_feature_member of this WFSInfo.  # noqa: E501

        Flag that determines encoding of featureMember or featureMembers. True if the featureMember should be encoded False if the featureMembers should be encoded.  # noqa: E501

        :return: The encode_feature_member of this WFSInfo.  # noqa: E501
        :rtype: bool
        """
        return self._encode_feature_member

    @encode_feature_member.setter
    def encode_feature_member(self, encode_feature_member):
        """Sets the encode_feature_member of this WFSInfo.

        Flag that determines encoding of featureMember or featureMembers. True if the featureMember should be encoded False if the featureMembers should be encoded.  # noqa: E501

        :param encode_feature_member: The encode_feature_member of this WFSInfo.  # noqa: E501
        :type: bool
        """

        self._encode_feature_member = encode_feature_member

    @property
    def hits_ignore_max_features(self):
        """Gets the hits_ignore_max_features of this WFSInfo.  # noqa: E501

        Flag that determines if WFS hit requests (counts) will ignore the maximum features limit for this server  # noqa: E501

        :return: The hits_ignore_max_features of this WFSInfo.  # noqa: E501
        :rtype: bool
        """
        return self._hits_ignore_max_features

    @hits_ignore_max_features.setter
    def hits_ignore_max_features(self, hits_ignore_max_features):
        """Sets the hits_ignore_max_features of this WFSInfo.

        Flag that determines if WFS hit requests (counts) will ignore the maximum features limit for this server  # noqa: E501

        :param hits_ignore_max_features: The hits_ignore_max_features of this WFSInfo.  # noqa: E501
        :type: bool
        """

        self._hits_ignore_max_features = hits_ignore_max_features

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
        if issubclass(WFSInfo, dict):
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
        if not isinstance(other, WFSInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

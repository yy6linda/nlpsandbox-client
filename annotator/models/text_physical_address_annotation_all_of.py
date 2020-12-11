# coding: utf-8

"""
    NLP Sandbox Date Annotator API

    The OpenAPI specification implemented by NLP Sandbox Date Annotators. # Overview This NLP tool detects date references in the clinical note specified and returns a list of date annotations.   # noqa: E501

    The version of the OpenAPI document: 0.2.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from annotator.configuration import Configuration


class TextPhysicalAddressAnnotationAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'address_type': 'str'
    }

    attribute_map = {
        'address_type': 'addressType'
    }

    def __init__(self, address_type=None, local_vars_configuration=None):  # noqa: E501
        """TextPhysicalAddressAnnotationAllOf - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._address_type = None
        self.discriminator = None

        if address_type is not None:
            self.address_type = address_type

    @property
    def address_type(self):
        """Gets the address_type of this TextPhysicalAddressAnnotationAllOf.  # noqa: E501

        Type of address information  # noqa: E501

        :return: The address_type of this TextPhysicalAddressAnnotationAllOf.  # noqa: E501
        :rtype: str
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this TextPhysicalAddressAnnotationAllOf.

        Type of address information  # noqa: E501

        :param address_type: The address_type of this TextPhysicalAddressAnnotationAllOf.  # noqa: E501
        :type: str
        """
        allowed_values = ["city", "country", "department", "hospital", "organization", "other", "room", "state", "street", "zip"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and address_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `address_type` ({0}), must be one of {1}"  # noqa: E501
                .format(address_type, allowed_values)
            )

        self._address_type = address_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TextPhysicalAddressAnnotationAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TextPhysicalAddressAnnotationAllOf):
            return True

        return self.to_dict() != other.to_dict()

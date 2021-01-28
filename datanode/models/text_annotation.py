# coding: utf-8

"""
    NLP Sandbox Data Node API

    The OpenAPI specification implemented by NLP Sandbox Data Nodes. # Overview A NLP Sandbox Data Node is a repository of clinical notes that implements this OpenAPI specification so that other services in the NLP Sandbox ecosystem can access them. For example, a client requests data from a Data Node before passing them as input to an NLP Tool like a Date Annotator, Person Name Annotator, etc. For the sake of benchmarking NLP Tool, a Data Node can also give access to the gold standard that the NLP Tool is expected to infer (e.g. annotations).   # noqa: E501

    The version of the OpenAPI document: 0.3.1
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from datanode.configuration import Configuration


class TextAnnotation(object):
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
        'start': 'int',
        'length': 'int',
        'text': 'str',
        'confidence': 'float'
    }

    attribute_map = {
        'start': 'start',
        'length': 'length',
        'text': 'text',
        'confidence': 'confidence'
    }

    def __init__(self, start=None, length=None, text=None, confidence=None, local_vars_configuration=None):  # noqa: E501
        """TextAnnotation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._start = None
        self._length = None
        self._text = None
        self._confidence = None
        self.discriminator = None

        self.start = start
        self.length = length
        self.text = text
        if confidence is not None:
            self.confidence = confidence

    @property
    def start(self):
        """Gets the start of this TextAnnotation.  # noqa: E501

        The position of the first character  # noqa: E501

        :return: The start of this TextAnnotation.  # noqa: E501
        :rtype: int
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this TextAnnotation.

        The position of the first character  # noqa: E501

        :param start: The start of this TextAnnotation.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and start is None:  # noqa: E501
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def length(self):
        """Gets the length of this TextAnnotation.  # noqa: E501

        The length of the annotation  # noqa: E501

        :return: The length of this TextAnnotation.  # noqa: E501
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this TextAnnotation.

        The length of the annotation  # noqa: E501

        :param length: The length of this TextAnnotation.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and length is None:  # noqa: E501
            raise ValueError("Invalid value for `length`, must not be `None`")  # noqa: E501

        self._length = length

    @property
    def text(self):
        """Gets the text of this TextAnnotation.  # noqa: E501

        The string annotated  # noqa: E501

        :return: The text of this TextAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this TextAnnotation.

        The string annotated  # noqa: E501

        :param text: The text of this TextAnnotation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and text is None:  # noqa: E501
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def confidence(self):
        """Gets the confidence of this TextAnnotation.  # noqa: E501

        The confidence in the accuracy of the annotation  # noqa: E501

        :return: The confidence of this TextAnnotation.  # noqa: E501
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """Sets the confidence of this TextAnnotation.

        The confidence in the accuracy of the annotation  # noqa: E501

        :param confidence: The confidence of this TextAnnotation.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                confidence is not None and confidence > 100):  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value less than or equal to `100`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                confidence is not None and confidence < 0):  # noqa: E501
            raise ValueError("Invalid value for `confidence`, must be a value greater than or equal to `0`")  # noqa: E501

        self._confidence = confidence

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
        if not isinstance(other, TextAnnotation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TextAnnotation):
            return True

        return self.to_dict() != other.to_dict()

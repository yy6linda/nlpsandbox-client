# coding: utf-8

"""
    NLP Sandbox Data Node API

    The OpenAPI specification implemented by NLP Sandbox Data Nodes. # Overview A NLP Sandbox Data Node is a repository of clinical notes that implements this OpenAPI specification so that other services in the NLP Sandbox ecosystem can access them. For example, a client requests data from a Data Node before passing them as input to an NLP Tool like a Date Annotator, Person Name Annotator, etc. For the sake of benchmarking NLP Tool, a Data Node can also give access to the gold standard that the NLP Tool is expected to infer (e.g. annotations).   # noqa: E501

    The version of the OpenAPI document: 0.2.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from datanode.configuration import Configuration


class Note(object):
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
        'id': 'str',
        'text': 'str',
        'note_type': 'str',
        'patient_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'text': 'text',
        'note_type': 'noteType',
        'patient_id': 'patientId'
    }

    def __init__(self, id=None, text=None, note_type=None, patient_id=None, local_vars_configuration=None):  # noqa: E501
        """Note - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._text = None
        self._note_type = None
        self._patient_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.text = text
        self.note_type = note_type
        if patient_id is not None:
            self.patient_id = patient_id

    @property
    def id(self):
        """Gets the id of this Note.  # noqa: E501

        The ID of the note  # noqa: E501

        :return: The id of this Note.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Note.

        The ID of the note  # noqa: E501

        :param id: The id of this Note.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def text(self):
        """Gets the text of this Note.  # noqa: E501

        The content of the clinical note  # noqa: E501

        :return: The text of this Note.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Note.

        The content of the clinical note  # noqa: E501

        :param text: The text of this Note.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and text is None:  # noqa: E501
            raise ValueError("Invalid value for `text`, must not be `None`")  # noqa: E501

        self._text = text

    @property
    def note_type(self):
        """Gets the note_type of this Note.  # noqa: E501

        The note type (LOINC concept)  # noqa: E501

        :return: The note_type of this Note.  # noqa: E501
        :rtype: str
        """
        return self._note_type

    @note_type.setter
    def note_type(self, note_type):
        """Sets the note_type of this Note.

        The note type (LOINC concept)  # noqa: E501

        :param note_type: The note_type of this Note.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and note_type is None:  # noqa: E501
            raise ValueError("Invalid value for `note_type`, must not be `None`")  # noqa: E501

        self._note_type = note_type

    @property
    def patient_id(self):
        """Gets the patient_id of this Note.  # noqa: E501

        The patient ID  # noqa: E501

        :return: The patient_id of this Note.  # noqa: E501
        :rtype: str
        """
        return self._patient_id

    @patient_id.setter
    def patient_id(self, patient_id):
        """Sets the patient_id of this Note.

        The patient ID  # noqa: E501

        :param patient_id: The patient_id of this Note.  # noqa: E501
        :type: str
        """

        self._patient_id = patient_id

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
        if not isinstance(other, Note):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Note):
            return True

        return self.to_dict() != other.to_dict()

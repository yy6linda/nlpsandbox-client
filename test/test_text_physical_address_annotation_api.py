# coding: utf-8

"""
    NLP Sandbox Date Annotator API

    The OpenAPI specification implemented by NLP Sandbox Date Annotators. # Overview This NLP tool detects date references in the clinical note specified and returns a list of date annotations.   # noqa: E501

    The version of the OpenAPI document: 0.2.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import annotator
from annotator.api.text_physical_address_annotation_api import TextPhysicalAddressAnnotationApi  # noqa: E501
from annotator.rest import ApiException


class TestTextPhysicalAddressAnnotationApi(unittest.TestCase):
    """TextPhysicalAddressAnnotationApi unit test stubs"""

    def setUp(self):
        self.api = annotator.api.text_physical_address_annotation_api.TextPhysicalAddressAnnotationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_text_physical_address_annotations(self):
        """Test case for create_text_physical_address_annotations

        Annotate physical addresses in a clinical note  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

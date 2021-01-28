# coding: utf-8

"""
    NLP Sandbox Data Node API

    The OpenAPI specification implemented by NLP Sandbox Data Nodes. # Overview A NLP Sandbox Data Node is a repository of clinical notes that implements this OpenAPI specification so that other services in the NLP Sandbox ecosystem can access them. For example, a client requests data from a Data Node before passing them as input to an NLP Tool like a Date Annotator, Person Name Annotator, etc. For the sake of benchmarking NLP Tool, a Data Node can also give access to the gold standard that the NLP Tool is expected to infer (e.g. annotations).   # noqa: E501

    The version of the OpenAPI document: 0.2.2
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import datanode
from datanode.models.dataset_create_response import DatasetCreateResponse  # noqa: E501
from datanode.rest import ApiException

class TestDatasetCreateResponse(unittest.TestCase):
    """DatasetCreateResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DatasetCreateResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = datanode.models.dataset_create_response.DatasetCreateResponse()  # noqa: E501
        if include_optional :
            return DatasetCreateResponse(
                name = 'datasets/awesome-dataset'
            )
        else :
            return DatasetCreateResponse(
        )

    def testDatasetCreateResponse(self):
        """Test DatasetCreateResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()

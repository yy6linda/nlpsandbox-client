"""
    NLP Sandbox Data Node API

    The OpenAPI specification implemented by NLP Sandbox Data Nodes. # Overview A NLP Sandbox Data Node is a repository of clinical notes that implements this OpenAPI specification so that other services in the NLP Sandbox ecosystem can access them. For example, a client requests data from a Data Node before passing them as input to an NLP Tool like a Date Annotator, Person Name Annotator, etc. For the sake of benchmarking NLP Tool, a Data Node can also give access to the gold standard that the NLP Tool is expected to infer (e.g. annotations).   # noqa: E501

    The version of the OpenAPI document: 0.3.1
    Contact: thomas.schaffter@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import unittest

import datanode
from datanode.api.patient_api import PatientApi  # noqa: E501


class TestPatientApi(unittest.TestCase):
    """PatientApi unit test stubs"""

    def setUp(self):
        self.api = PatientApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_patient(self):
        """Test case for create_patient

        Create a FHIR patient  # noqa: E501
        """
        pass

    def test_delete_patient(self):
        """Test case for delete_patient

        Delete a FHIR patient  # noqa: E501
        """
        pass

    def test_get_patient(self):
        """Test case for get_patient

        Get a FHIR patient  # noqa: E501
        """
        pass

    def test_list_patients(self):
        """Test case for list_patients

        List the Patients in a FHIR store  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

"""
SFDCFW.Test.TestMetadata
~~~~~~~~~~~~~~~~~~~~~~~~
"""

import json
import os
import unittest

from SFDCFW.Rest import Rest
from SFDCFW.Metadata import Metadata
from SFDCFW.SFDCFW import SFDCFW
from SFDCFW.Constant import TEST_DATA


def setUpModule():
    """Set Up Module"""
    pass


def tearDownModule():
    """Tear Down Module"""
    pass


class TestMetadata(unittest.TestCase):
    """Test Metadata."""

    @classmethod
    def setUpClass(cls):
        """Prepare test set up class.

        Get the Test Data from JSON (JavaScript Object Notation) file.
        """

        # Get the current directory of the file
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # Get the path of the Test Data file
        test_data_file = os.path.join(current_directory, TEST_DATA)

        # Open the file for reading
        with open(test_data_file, 'r') as f:
            data = json.load(f)

        # Get the domain
        domain = data['domain']

        # Get the WSDL (Web Service Definition Language) file path
        enterprise_wsdl = os.path.join(current_directory, data['enterprise_wsdl'])
        metadata_wsdl = os.path.join(current_directory, data["metadata_wsdl"])

        # Create the WSDL information
        # {
        #     'enterprise': None,
        #     'partner': None,
        #     'apex': None,
        #     'metadata': None,
        #     'tooling': None,
        #     'tooling_typed': None,
        #     'delegated_authentication': None
        # }
        wsdl = {
            'enterprise': enterprise_wsdl,
            'metadata': metadata_wsdl
        }

        # Get the REST Access user data for success login
        rest_access_user_success = data['user']['access_user_success']

        # Create an instance of SFDCFW
        sfdcfw = SFDCFW(username=rest_access_user_success['username'],
                        password=rest_access_user_success['password'],
                        security_token=rest_access_user_success['security_token'],
                        domain=domain,
                        wsdl=wsdl)

        # Get the `metadata` property
        cls.sfdcfw_metadata = sfdcfw.metadata


    def test_list_metadata_success(self):
        """Test a success of list metadata.

        Create a `query` and execute it with `listMetadata`. Should
        result in response with a `list`.
        """

        # Create a `query` with `WorkflowRule` type
        query = [
            { "type": "WorkflowRule" }
        ]

        # Execute `listMetadata` with the `query`
        result = self.sfdcfw_metadata.list_metadata(query=query)

        # Test to ensure `result` is of type `list`
        self.assertIsInstance(result, list)


    @classmethod
    def tearDownClass(cls):
        """Prepare test teardown class.
        """
        pass


def suite():
    """Test Suite."""

    # Create the Unit Test Suite
    suite = unittest.TestSuite()

    # Load a suite of all test cases contained in `testCaseClass`
    test_metadata = unittest.defaultTestLoader.loadTestsFromTestCase(TestMetadata)

    # Add the test suite
    suite.addTest(test_metadata)

    # Return the Test Suite
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
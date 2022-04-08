"""
SFDCFW.Test.TestSFDCFW
~~~~~~~~~~~~~~~~~~~~~~
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


class TestSFDCFW(unittest.TestCase):
    """Test the SFDCFW module."""

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
                        client_id=rest_access_user_success['consumer_key'],
                        client_secret=rest_access_user_success['consumer_secret'],
                        domain=domain,
                        wsdl=wsdl)

        # Get the `rest` property
        cls.sfdcfw_rest = sfdcfw.rest

        # Get the `metadata` property
        cls.sfdcfw_metadata = sfdcfw.metadata


    def test_sfdcfw_rest_create_success(self):
        """Test a success of REST (REpresentational State Transfer) create.

        Get the `rest` property `sfdcfw`. Should result in an object of
        type `Rest`.
        """

        # Test to ensure object returned is type `Rest`
        self.assertIsInstance(self.sfdcfw_rest, Rest)


    def test_sfdcfw_metadata_create_success(self):
        """Test a success of Metadata create.

        Test the type of the `metadata` property for `sfdcfw`. Should
        result in an object of type `Metadata`.
        """

        # Test to ensure object returned is type `Metadata`
        self.assertIsInstance(self.sfdcfw_metadata, Metadata)


    def test_sfdcfw_metadata_get_wsdl_success(self):
        """Test a success of the WSDL (Web Service Definition Language)

        Test the type of the `wsdl` property for `sfdcfw
        """

        # Test to ensure `wsdl` property is type `str`
        self.assertIsInstance(self.sfdcfw_metadata.wsdl, str)


def suite():
    """Test Suite."""

    # Create the Unit Test Suite
    suite = unittest.TestSuite()

    # Load a suite of all test cases contained in `testCaseClass`
    test_sfdcfw = unittest.defaultTestLoader.loadTestsFromTestCase(TestSFDCFW)

    # Add the test suite
    suite.addTest(test_sfdcfw)

    # Return the Test Suite
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
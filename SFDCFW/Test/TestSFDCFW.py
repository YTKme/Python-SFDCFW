"""
SFDCFW.Test.TestSFDCFW
~~~~~~~~~~~~~~~~~~~~~~
"""

import json
import os
import unittest
from SFDCFW.Rest import Rest

from SFDCFW.SFDCFW import SFDCFW
from SFDCFW.Constant import TEST_DATA


def setUpModule():
    """Set Up Module"""
    pass


def tearDownModule():
    """Tear Down Module"""
    pass


class TestSFDCFW(unittest.TestCase):
    """Test the SFDCFW module.
    """

    @classmethod
    def setUpClass(cls):
        """Prepare test setup class.
        """

        # Get the current directory of the file
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # Get the path of the Test Data file
        cls.test_data_file = os.path.join(current_directory, TEST_DATA)

        # Open the file for reading
        with open(cls.test_data_file, 'r') as f:
            cls.data = json.load(f)

        # Get the domain
        domain = cls.data['domain']

        # Get the REST Access user data for success login
        rest_access_user_success = cls.data['user']['access_user_success']

        # Create an instance of SFDCFW
        cls.sfdcfw = SFDCFW(username=rest_access_user_success['username'],
                            password=rest_access_user_success['password'],
                            security_token=rest_access_user_success['security_token'],
                            client_id=rest_access_user_success['consumer_key'],
                            client_secret=rest_access_user_success['consumer_secret'],
                            domain=domain)


    def test_sfdcfw_rest_create_success(self):
        """Test a success of REST (REpresentational State Transfer) create.

        Get the `rest` property `sfdcfw`. Should result in an object of
        type `Rest`.
        """

        # Get the property
        sfdcfw_rest = self.sfdcfw.rest

        # Test to ensure object returned is type `Rest`
        self.assertIsInstance(sfdcfw_rest, Rest)


    @classmethod
    def tearDownClass(cls):
        """Prepare test teardown class.
        """
        pass


def suite():
    """Test Suite"""

    # Create the Unit Test Suite
    suite = unittest.TestSuite()

    # Load a suite of all test cases contained in `testCaseClass`
    test_sfdcfw = unittest.defaultTestLoader.loadTestsFromTestCase(TestSFDCFW)

    # Add the test suite
    suite.addTest(test_sfdcfw)

    # Return the Test Suite
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
"""
SFDCAPI.Test.TestRest
~~~~~~~~~~~~~~~~~~~~~
"""

import json
import os
import unittest
from SFDCAPI.Authentication.Access import Access
from SFDCAPI.Rest.Rest import Rest
from SFDCAPI.Constant.Constant import HTTP_GET
from SFDCAPI.Constant.Constant import TEST_DATA


class TestRest(unittest.TestCase):
    """Test the REST (REpresentational State Transfer) module."""

    @classmethod
    def setUpClass(cls):
        """Prepare test set up class.

        Get the Test Data from JSON (JavaScript Object Notation) file.
        """

        # Get the current directory of the file
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # Get the path of the Test Data file
        cls.test_data_file = os.path.join(current_directory, TEST_DATA)

        # Open the file for reading
        with open(cls.test_data_file, 'r') as f:
            cls.data = json.load(f)

        # Get the URL (Uniform Resource Locator) from the Test Data
        cls.url = cls.data['url']


    def test_send_get_success(self):
        """Test a success of the send method.
        """

        # Create instance of Rest object
        rest = Rest()
        # Send a GET request to a valid URL
        response = rest.send(HTTP_GET, self.url)

        # Test to ensure getting HTTP (HyperText Transfer Protocol) status code 200
        self.assertEqual(response.status_code, 200)


def suite():
    """Test Suite"""

    # Create the Unit Test Suite
    suite = unittest.TestSuite()

    # Add the Unit Test
    suite.addTest(TestRest)

    # Return the Test Suite
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
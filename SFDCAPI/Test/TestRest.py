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


class TestRestGet(unittest.TestCase):
    """Test Rest Get
    
    Test the REST (REpresentational State Transfer) module with the HTTP
    (HyperText Transfer Protocol) GET method.
    """

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


    def test_send_success(self):
        """Test a success of the send method.

        Send a HTTP GET request to a valid URL and test to ensure the
        response status code is 200 OK.
        """

        # Create instance of Rest object
        rest = Rest()
        # Send a HTTP GET request to a valid URL
        response = rest.send(HTTP_GET, self.url)

        # Test to ensure getting HTTP status code 200
        self.assertEqual(response.status_code, 200)


def suite():
    """Test Suite"""

    # Create the Unit Test Suite
    suite = unittest.TestSuite()

    # Add the Unit Test
    suite.addTest(TestRestGet)

    # Return the Test Suite
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
"""
SFDCAPI.Test.Test
~~~~~~~~~~~~~~~~~
"""

import json
import os
import unittest
from SFDCAPI.Authentication.Access import Access
from SFDCAPI.Rest.Rest import Rest
from SFDCAPI.Constant.Constant import HTTP_GET


class TestRest(unittest.TestCase):
    """Test the Rest module."""

    def test_send(self):
        """Test a failure of the send method.
        """

        # Get the current directory of the file
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # Get the path of the test data file
        test_access_file = os.path.join(current_directory, "Test_Access.json")

        # Open the file for reading
        with open(test_access_file, "r") as f:
            data = json.load(f)

        # Get the user data for success login
        user_success = data["user_success"]

        # Create an instance of Access object and login
        access = Access(username=user_success["username"], password=user_success["password"], domain="test", metadata=True).login()

        # Create instance of Rest object
        rest = Rest(access)
        # Send a failure (invalid) GET request
        response = rest.send(HTTP_GET, "/invalid", None)

        # Test to ensure getting HTTP status code 200
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
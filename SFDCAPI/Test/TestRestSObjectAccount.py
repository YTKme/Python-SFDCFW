"""
SFDCAPI.Test.Test
~~~~~~~~~~~~~~~~~
"""

import json
import os
import random
import string
import unittest

from SFDCAPI.Authentication.Access import Access
from SFDCAPI.Rest.SObject import SObject

class TestRestSObjectAccount(unittest.TestCase):
    """
    Test the SObject module using REST (REpresentational State Transfer)
    with Account.
    """

    @classmethod
    def setUpClass(cls):
        """Prepare test setup class.

        Get the data from JSON (JavaScript Object Notation) file and
        login.
        """

        # Get the current directory of the file
        current_directory = os.path.dirname(os.path.abspath(__file__))
        # Get the path of the Test Data file
        cls._test_data_file = os.path.join(current_directory, "TestData.json")

        # Open the file for reading
        with open(cls._test_data_file, "r") as f:
            cls._data = json.load(f)

        # Get the domain
        domain = cls._data["domain"]

        # Get the user data for success login
        user_rest_success = cls._data["user"]["user_rest_success"]

        # Create an instance of Access object and login
        cls._access = Access(username=user_rest_success["username"],
                             password=user_rest_success["password"],
                             security_token=user_rest_success["security_token"],
                             client_id=user_rest_success["consumer_key"],
                             client_secret=user_rest_success["consumer_secret"],
                             domain=domain).login()

        # Create an instance of SObject
        cls._sobject = SObject(cls._access)

        # Set up Account for Delete
        account_id = cls._create_account()

        # Create the dictionary
        cls._data["account"]["delete_account_success"] = {}
        # Create or update the Account ID in the Test Data
        cls._data["account"]["delete_account_success"]["id"] = account_id

        # Write the new Test Data to file
        with open(cls._test_data_file, "w") as f:
            json.dump(cls._data, f)


    @classmethod
    def _create_account(cls):
        """Create Account.

        Generated Account Name to make a request for create Account.

        Returns:
            A string of the Account ID (unique identifier)
        """

        # Create the payload
        payload = {
            # Generate a random Account Name
            "name": "Account-{}".format(random.randrange(10000, 99999))
        }

        # Make a request to create the Account
        # Get the return unique identifier (ID)
        # The payload need to be serialized to JSON formatted str (json.dumps)
        account_id = cls._sobject.Account.create(json.dumps(payload))

        # Return the Account ID
        return account_id


    def test_create_account_failure(self):
        """Test a failure for create Account.

        Generated a random Account Description to make a request for
        create. Should result in response with status code 400 Bad
        Request.
        """

        # Create the payload
        payload = {
            # Generate a random Account Description
            "Description": "Description-{}".format(random.randrange(10000, 99999))
        }

        # Make a request to create the Account
        # Get the return unique identifier (ID)
        # The payload need to be serialized to JSON formatted str (json.dumps)
        account_id = self._sobject.Account.create(json.dumps(payload))

        # Test to ensure Account ID is None
        self.assertEqual(account_id, None)


    def test_create_account_success(self):
        """Test a success for create Account.

        Generated Account Name to make a request for create. Should
        result in response with status code 204 No Content.
        """

        # Create the payload
        payload = {
            # Generate a random Account Name
            "Name": "Account-{}".format(random.randrange(10000, 99999))
        }

        # Make a request to create the Account
        # Get the return unique identifier (ID)
        # The payload need to be serialized to JSON formatted str (json.dumps)
        account_id = self._sobject.Account.create(json.dumps(payload))

        # Create the dictionary
        self._data["account"]["read_account_success"] = {}
        # Create or update the Account ID in the Test Data
        self._data["account"]["read_account_success"]["id"] = account_id

        # Write the new Test Data to file
        with open(self._test_data_file, "w") as f:
            json.dump(self._data, f)

        # Test to ensure Account ID is a string
        self.assertEqual(type(account_id), str)


    def test_read_account_success(self):
        """Test a success for read Account.

        Make a request for read Account. Should result in response with
        a string and status code 200 OK.
        """

        # Make a request to read the Account
        # Get the return Account data
        account_data = self._sobject.Account.read()

        # Test to ensure Account data is a string
        self.assertEqual(type(account_data), str)


    def test_read_account_failure(self):
        """Test a failure for read Account.

        Generate a fake random Account unique identifier (ID) and make
        a request for read Account. Should result in response with
        None (status code 404 Not Found).
        """

        # Generate a random Account unique identifier (ID)
        # The Account unique identifier (ID) will have invalid length
        account_id = "".join(random.choice(string.ascii_letters + string.digits) for i in range(8))

        # Make a request to read the Account
        # Get the return Account data
        account_data = self._sobject.Account.read(account_id)

        # Test to ensure Account data is None
        self.assertIsNone(account_data)


    def test_update_account_success(self):
        """Test a success for update Account.

        Generated Account Name to make a request for update. Should
        result in response with status code 204 No Content.
        """

        # Get the read Account success data
        read_account_success = self._data["account"]["read_account_success"]

        # Create the payload
        payload = {
            # Generate a random Account Name
            "Name": "Account-{}".format(random.randrange(10000, 99999))
        }

        # Make a request to update the Account
        account = self._sobject.Account.update(read_account_success["id"], payload)

        # Test to ensure HTTP status code is 204 No Content
        self.assertEqual(account, 204)


    def test_update_account_failure(self):
        """Test a failure for update Account.

        Generate Account Name to make a request for update. Should
        result in response with status code 204 No Content.
        """

        # Generate a random Account unique identifier (ID)
        # The Account unique identifier (ID) will have invalid length
        account_id = "".join(random.choice(string.ascii_letters + string.digits) for i in range(8))

        # Create the payload
        payload = {
            # Generate a random Account Name
            "Name": "Account-{}".format(random.randrange(10000, 99999))
        }

        # Make a request to update the Account
        account = self._sobject.Account.update(account_id, payload)

        # Test to ensure HTTP status code is not 204 No Content
        self.assertNotEqual(account, 204)


    def test_delete_account_success(self):
        """Test a success for delete Account.

        Get the unique identifier (ID) of the Account from the Test Data
        to make a request for delete. Should result in response with
        status code 204 No Content.
        """

        # Get the delete Account success data
        delete_account_success = self._data["account"]["delete_account_success"]

        # Make a request to delete the Account
        account = self._sobject.Account.delete(delete_account_success["id"])

        # Delete the Account entry from the Test Data
        if "delete_account_success" in self._data["account"]:
            del self._data["account"]["delete_account_success"]

        # Write the new Test Data to file
        with open(self._test_data_file, "w") as f:
            json.dump(self._data, f)

        # Test to ensure HTTP status code is 204 No Content
        self.assertEqual(account, 204)


    def test_delete_account_failure(self):
        """Test a failure for delete Account.

        Generate a random unique identifier (ID) of the Account to make
        a request for update. Should result in response with status
        code 204 No Content.
        """

        # Generate a random Account unique identifier (ID)
        # The Account unique identifier (ID) will have invalid length
        account_id = "".join(random.choice(string.ascii_letters + string.digits) for i in range(8))

        # Make a request to delete the Account
        account = self._sobject.Account.delete(account_id)

        # Test to ensure HTTP status code is not 204 No Content
        self.assertNotEqual(account, 204)


    @classmethod
    def _delete_account(cls):
        """Delete Account.

        Get the Account unique identifier (ID) from the Test Data to
        make a request for delete Account.

        Returns:
            A HTTP Status Code (or None) of the response.
        """
        
        # Get the read Account success data
        read_account_success = cls._data["account"]["read_account_success"]

        # Make a request to delete the Account
        account = cls._sobject.Account.delete(read_account_success["id"])

        # Delete the Account entry from the Test Data
        if "read_account_success" in cls._data["account"]:
            del cls._data["account"]["read_account_success"]

        # Write the new Test Data to file
        with open(cls._test_data_file, "w") as f:
            json.dump(cls._data, f)

        # Return the response
        return account


    @classmethod
    def tearDownClass(cls):
        """Prepare test teardown class.

        Clean up Test Data
        """

        # Delete the Account and delete information from Test Data
        cls._delete_account()


if __name__ == "__main__":
    unittest.main()
"""
SFDCAPI.Rest.SObject
~~~~~~~~~~~~~~~~~~~~
"""

import json

from SFDCAPI.Rest.Rest import Rest

from SFDCAPI.Constant.Constant import SFDC_API_V
from SFDCAPI.Constant.Constant import HTTP_GET
from SFDCAPI.Constant.Constant import HTTP_POST
from SFDCAPI.Constant.Constant import HTTP_PATCH
from SFDCAPI.Constant.Constant import HTTP_DELETE

class SObject(Rest):
    """SObject class.
    """

    def __getattr__(self, label):
        """Get Attribute Passed In.

        Args:
            label (str): The attribute passed in.

        Returns:
            A instance of the SObject class.
        """
        # Set the name / label
        self.label = label

        # Return the self instance
        return self


    def create(self, data):
        """Create SObject.

        Args:
            data (dict): The required data for the SObject.

        Returns:
            A string for the unique identifier (ID) of the SObject.
        """
        
        # Create the request URL
        request_url = "/services/data/v" + SFDC_API_V + "/sobjects/" + self.label

        # Send the request
        r = self.send(HTTP_POST, request_url, data)

        # Check the status code
        if r.status_code == 201:
            # Parse the unique identifier (ID) of the SObject
            sobject_id = json.loads(r.text)["id"]
            # Return the unique identifier (ID) of the SObject
            return sobject_id

        # There was an error
        return None


    def read(self, id=None):
        """Read SObject.

        Args:
            id (str): The unique identifier (ID) of the SObject.

        Returns:
            A string formatted JSON for the request.
        """

        if id is not None:
            # Create the request URL with unique identifier (ID) of the SObject
            request_url = "/services/data/v" + SFDC_API_V + "/sobjects/" + self.label + "/" + id
        else:
            # Create the base request URL
            request_url = "/services/data/v" + SFDC_API_V + "/sobjects/" + self.label

        # Send the request
        r = self.send(HTTP_GET, request_url, None)

        # Check the status code
        if r.status_code == 200:
            # Return the response text (message body)
            return r.text

        # There was an error
        return None


    def find_by_id(self, id):
        """Find By ID.

        Args:
            id (str): The ID of the SObject.

        Returns:
            A string formatted JSON for the HTTP response object.
        """
        
        # Create the request URL
        request_url = "/services/data/v" + SFDC_API_V + "/sobjects/" + self.label + "/" + id

        # Send the request
        r = self.send(HTTP_GET, request_url, None)

        return r.text


    def update(self, id, data):
        """Update SObject.

        Args:
            id (str): The ID of the SObject.
            data (dict): The updated data for the SObject.

        Returns:
            A HTTP Status Code (or None) of the response.
        """

        # Create the request URL
        request_url = "/sobjects/" + self.label + "/" + id

        # Send the request
        r = self.send(HTTP_PATCH, request_url, json.dumps(data))

        # Check the status code
        if r.status_code == 204:
            # Return the status code
            return r.status_code

        # There was an error
        return None


    def delete(self, id):
        """Delete SObject.

        Args:
            id (str): The ID of the SObject.

        Returns:
            A HTTP Status Code (or None) of the response.
        """

        # Create the request URL
        request_url = "/sobjects/" + self.label + "/" + id

        # Send the request
        r = self.send(HTTP_DELETE, request_url, None)

        # Check the status code
        if r.status_code == 204:
            # Return the status code
            return r.status_code

        # There was an error
        return None
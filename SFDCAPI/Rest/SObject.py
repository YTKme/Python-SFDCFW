"""
SFDCAPI.Rest.SObject
~~~~~~~~~~~~~~~~~~~~
"""

import json
from urllib.parse import urlparse

from SFDCAPI.Rest.Rest import Rest

from SFDCAPI.Constant.Constant import SFDC_API_V
from SFDCAPI.Constant.Constant import HTTP_GET
from SFDCAPI.Constant.Constant import HTTP_POST
from SFDCAPI.Constant.Constant import HTTP_PATCH
from SFDCAPI.Constant.Constant import HTTP_DELETE

class SObject(Rest):
    """SObject class.
    """

    def __init__(self, access):
        """Constructor

        Args:
            access (tuple): The Salesforce session ID / access token and
                server URL / instance URL tuple
        """

        # Unpack the tuple for session ID / access token and server URL / instance URL
        self.id_token, self.url = access
        
        # Parse the URL
        u = urlparse(self.url)
        self.url = "{scheme}://{netloc}".format(scheme=u.scheme, netloc=u.netloc)

        # Create REST header
        self._header = {
            "Authorization": "Bearer " + self.id_token,
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json"
        }

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
        request_url = '/services/data/v' + SFDC_API_V + '/sobjects/' + self.label

        # Send the request
        r = self.send(HTTP_POST,
                      request_url,
                      header=self.header,
                      payload=data)

        # Check the status code
        if r.status_code == 201:
            # Parse the unique identifier (ID) of the SObject
            sobject_id = json.loads(r.text)['id']
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
            request_url = '/services/data/v' + SFDC_API_V + '/sobjects/' + self.label + '/' + id
        else:
            # Create the base request URL
            request_url = '/services/data/v' + SFDC_API_V + '/sobjects/' + self.label

        # Send the request
        r = self.send(HTTP_GET, request_url)

        # Check the status code
        if r.status_code == 200:
            # Return the response text (message body)
            return r.text

        # There was an error
        return None


    def update(self, id, data):
        """Update SObject.

        Args:
            id (str): The ID of the SObject.
            data (dict): The updated data for the SObject.

        Returns:
            A HTTP Status Code (or None) of the response.
        """

        # Create the request URL
        request_url = '/sobjects/' + self.label + '/' + id

        # Send the request
        r = self.send(HTTP_PATCH,
                      request_url,
                      header=self.header,
                      payload=json.dumps(data))

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
        request_url = '/sobjects/' + self.label + '/' + id

        # Send the request
        r = self.send(HTTP_DELETE, request_url)

        # Check the status code
        if r.status_code == 204:
            # Return the status code
            return r.status_code

        # There was an error
        return None
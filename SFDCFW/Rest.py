"""
SFDCFW.Rest
~~~~~~~~~~~
"""

from __future__ import annotations

import json
from typing import Optional
from urllib.parse import urlparse

import requests

from SFDCFW.Constant import SFDC_API_V


class Rest:
    """REST (REpresentational State Transfer) class."""

    def __init__(self, access: tuple) -> None:
        """Instantiator.

        Args:
            access (tuple): The Salesforce session ID / access token and
                server URL / instance URL tuple
        """

        # Initialize the name / label
        self.label = None

        # Unpack the tuple for session ID / access token and server URL / instance URL
        self.id_token, self.base_url = access
        
        # Parse the URL
        u = urlparse(self.base_url)
        self.base_url = f'{u.scheme}://{u.netloc}'

        # Create REST header
        self.header = {
            'Authorization': f'Bearer {self.id_token}',
            'Content-Type': 'application/json; charset=UTF-8',
            'Accept': 'application/json'
        }


    def __getattr__(self, label: str) -> Rest:
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


    def create(self, payload) -> Optional[str]:
        """Create.

        Args:
            payload (dict): The required data for the SObject.

        Returns:
            A string for the unique identifier (ID) of the SObject.
        """
        
        # Create the request URL
        request_url = f'{self.base_url}/services/data/v{SFDC_API_V}/sobjects/{self.label}'

        # Send the request
        r = requests.post(url=request_url,
                          headers=self.header,
                          data=payload)

        # Check the status code
        if r.status_code == 201:
            # Parse the unique identifier (ID) of the SObject
            sobject_id = json.loads(r.text)['id']
            # Return the unique identifier (ID) of the SObject
            return sobject_id

        # There was an error
        return None


    def read(self, id=None):
        """Read.

        Args:
            id (str): The unique identifier (ID) of the SObject.

        Returns:
            A string formatted JSON for the request.
        """

        if id is not None:
            # Create the request URL with ID
            request_url = f'{self.base_url}/services/data/v{SFDC_API_V}/sobjects/{self.label}/{id}'
        else:
            # Create the request URL without ID
            request_url = f'{self.base_url}/services/data/v{SFDC_API_V}/sobjects/{self.label}'

        # Send the request
        r = requests.get(url=request_url,
                         headers=self.header)

        # Check the status code
        if r.status_code == 200:
            # Return the response text (message body)
            return r.text

        # There was an error
        return None


    def update(self, id, payload):
        """Update.

        Args:
            id (str): The ID of the SObject.
            payload (dict): The updated data for the SObject.

        Returns:
            A HTTP Status Code (or None) of the response.
        """

        # Create the request URL
        request_url = f'{self.base_url}/services/data/v{SFDC_API_V}/sobjects/{self.label}/{id}'

        # Send the request
        r = requests.patch(url=request_url,
                           headers=self.header,
                           data=payload)

        # Check the status code
        if r.status_code == 204:
            # Return the status code
            return r.status_code

        # There was an error
        return None


    def delete(self, id):
        """Delete.

        Args:
            id (str): The ID of the SObject.

        Returns:
            A HTTP Status Code (or None) of the response.
        """

        # Create the request URL
        request_url = f'{self.base_url}/services/data/v{SFDC_API_V}/sobjects/{self.label}/{id}'

        # Send the request
        r = requests.delete(url=request_url,
                            headers=self.header)

        # Check the status code
        if r.status_code == 204:
            # Return the status code
            return r.status_code

        # There was an error
        return None
"""
SFDCAPI.Rest.Rest
~~~~~~~~~~~~~~~~~
"""

import re
from urllib.parse import urlparse
from requests import Request, Session

from SFDCAPI.Constant.Constant import SFDC_API_V
from SFDCAPI.Constant.Constant import HTTP_GET


class Rest(object):
    """A REST (REpresentational State Transfer) object.

    General API (Application Programming Interface) for request and response.

    Basic Usage:

        >>> from SFDCAPI.Rest.Rest import Rest
        >>> rest = Rest(access)
        >>> rest.send("GET", "/sobjects/Account/describe", None)
    """

    def __init__(self, access):
        """Constructor

        Args:
            access (tuple): The Salesforce session ID / access token and server
                URL / instance URL tuple
        """

        # Unpack the tuple for session ID / access token and server URL / instance URL
        self._id_token, self._url = access
        
        # Parse the URL
        u = urlparse(self._url)
        self._url = "{scheme}://{netloc}".format(scheme=u.scheme, netloc=u.netloc)

        # Create REST header
        self._header = {
            "Authorization": "Bearer " + self._id_token,
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json"
        }


    def query(self, query):
        """Execute SOQL (Salesforce Object Query Language) Query

        Args:
            query (str): The SOQL (Salesforce Object Query Language) query

        Returns:
            A string formatted JSON for the query response
        """

        # Create the request URL
        request_url = "/query/?q=" + query

        # Send the request
        r = self.send(HTTP_GET, request_url, None)

        return r.text


    def query_more(self, next_record_url):
        """Query Next Record Batch

        Args:
            next_record_url (str): The URL for the next batch of records

        Returns:
            A string formatted JSON for the query response
        """

        # Send the request
        r = self.send(HTTP_GET, next_record_url, None)

        return r.text


    def send(self, method, relative_url, payload):
        """Send REST Request

        Args:
            method (str): The HTTP method for the request
            relative_url (str): The relative URL for the HTTP request, with or
                without the beginning slash ( / )
                Example: /services/data/v46.0 or /sobjects
            payload (dict): The body of the HTTP request

        Returns:
            A string formatted JSON for the HTTP response object
        """

        # TODO: Expand method to take certificate and extra parameters.

        # Create the request URL
        request_url = self._url

        if "services/data" in relative_url:
            # If the complete relative URL is provided
            request_url += "/" + relative_url
        else:
            # Assume only a partial relative URL is provided
            request_url += "/services/data/v" + SFDC_API_V + "/" + relative_url

        # Clean up any extra slash ( / )
        request_url = re.sub(r"(?<=[^:\s])(\/+\/)", r"/", request_url)

        # Create a session
        session = Session()

        # Create the request
        request = Request(method=method,
                          url=request_url,
                          headers=self._header,
                          data=payload)
        # Prepare the request
        preparation = request.prepare()

        # Send the prepared request for response
        response = session.send(preparation)

        return response
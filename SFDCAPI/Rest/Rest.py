"""
SFDCAPI.Rest.Rest
~~~~~~~~~~~~~~~~~
"""

from requests import Request, Session


class Rest(object):
    """A REST (REpresentational State Transfer) object.

    General API (Application Programming Interface) for request and
    response.

    Basic Usage:

        >>> from SFDCAPI.Rest.Rest import Rest
        >>> rest = Rest()
        >>> rest.send("GET", "https://yourInstance.my.salesforce.com/services/data/")

        or

        >>> from SFDCAPI.Rest.Rest import Rest
        >>> rest = Rest("GET", "https://yourInstance.my.salesforce.com/services/data/")
        >>> rest.send()
    """

    def __init__(self, method, url, header=None, payload=None):
        """Constructor.

        Args:
            method (str): The HTTP method for the request
            relative_url (str): The relative URL for the HTTP request
            header (dict): The header of the HTTP request
            payload (dict): The body of the HTTP request
        """

        self.method = method
        self.url = url
        self.header = header
        self.payload = payload


    def send(self, method, url, header=None, payload=None):
        """Send REST Request.

        Args:
            method (str): The HTTP method for the request
            relative_url (str): The relative URL for the HTTP request
            header (dict): The header of the HTTP request
            payload (dict): The body of the HTTP request

        Returns:
            A string formatted JSON for the HTTP response object
        """

        # Create a session
        session = Session()

        # Create the request
        request = Request(method=self.method if self.method else method,
                          url=self.url if self.url else url,
                          headers=self.header if self.header else header,
                          data=self.payload if self.payload else payload)
        # Prepare the request
        preparation = request.prepare()

        # Send the prepared request for response
        response = session.send(preparation)

        # Return the response
        return response
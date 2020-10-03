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
        >>> rest.send('GET', 'https://yourInstance.my.salesforce.com/services/data/')
    """

    def __init__(self):
        """Constructor."""
        pass


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
        request = Request(method=method,
                          url=url,
                          headers=header,
                          data=payload)
        # Prepare the request
        preparation = request.prepare()

        # Send the prepared request for response
        response = session.send(preparation)

        # Return the response
        return response
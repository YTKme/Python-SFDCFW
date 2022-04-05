"""
Metadata API

Metadata Coverage

.. _Metadata Coverage:
   https://developer.salesforce.com/docs/metadata-coverage/
"""

from __future__ import annotations

import threading

from zeep import Client, Settings

from SFDCFW.Constant import SFDC_API_V

class Metadata:
    """Metadata class."""

    def __init__(self, access: tuple) -> None:
        """Instantiator.

        Args:
            access (tuple): The Salesforce session ID / access token,
                server URL / instance URL tuple, and WSDL (Web Services
                Description Language) file
        """

        # Unpack the tuple
        # Get session ID / access token
        # Get server URL / instance URL
        # Get WSDL (Web Services Description Language) file
        self.id_token, self.url, self.wsdl = access

        # Create client with setting of disable strict mode, use recovery mode
        setting = Settings(strict=False)
        client = Client(wsdl=self.wsdl, settings=setting)
        # Create the service with custom binding and URL
        binding = '{urn:enterprise.soap.sforce.com}SoapBinding'
        self.service = client.create_service(binding, self.url)

        # Create the SOAP header (this is different than the HTTP header)
        self.soap_header = {
            "SessionHeader": {
                "sessionId": self.id_token
            }
        }


    def __getattr__(self, label: str) -> Metadata:
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
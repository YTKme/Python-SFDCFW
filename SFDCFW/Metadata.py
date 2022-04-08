"""
SFDCFW.Metadata
~~~~~~~~~~~~~~~

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
    """Metadata."""

    def __init__(self, access: tuple, metadata_wsdl: str) -> None:
        """Instantiator.

        Args:
            access (tuple): The Salesforce session ID / access token and
                metadata server URL / instance URL.
            wsdl (str): The path to the Metadata WSDL (Web Services
                Description Language) file.
        """

        # Set the name / label
        self.label = None

        # Unpack the tuple
        # Get the session ID / access token and metadata server URL / instance URL
        session_id, metadata_server_url = access

        # Get the Metadata WSDL
        self.metadata_wsdl = metadata_wsdl

        # Create client with setting of disable strict mode, use recovery mode
        setting = Settings(strict=False)
        client = Client(wsdl=metadata_wsdl, settings=setting)
        # Create the service with custom binding and URL
        # This binding is used with Metadata specifically
        binding = '{http://soap.sforce.com/2006/04/metadata}MetadataBinding'
        self.service = client.create_service(binding, metadata_server_url)

        # Create the SOAP header (this is different than the HTTP header)
        self.soap_header = {
            "SessionHeader": {
                "sessionId": session_id
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


    @property
    def wsdl(self) -> str:
        """The WSDL (Web Services Description Language) property.

        Returns:
            A string for the location and name of the WSDL file.
        """

        return self.metadata_wsdl


    def list_metadata(self, query):
        """List Metadata.

        Args:
            query (list): A complex list of dictionary specify components.
                [
                    { "folder": "Report", "type": "ReportName" },
                    { "type": "WorkflowRule" }
                ]

        Returns:
            A complex list of dictionary for the requested metadata
            component(s).
        """

        return self.service.listMetadata(queries=query,
                                         asOfVersion=SFDC_API_V,
                                         _soapheaders=self.soap_header)


    def create(self):
        pass


    def read(self):
        pass


    def update(self):
        pass


    def delete(self):
        pass
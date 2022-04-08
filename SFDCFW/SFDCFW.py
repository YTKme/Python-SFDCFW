"""
SFDCFW.SFDCFW
~~~~~~~~~~~~~
"""

from __future__ import annotations

from SFDCFW.Access import Access
from SFDCFW.Rest import Rest
from SFDCFW.Metadata import Metadata

from SFDCFW.Constant import SFDC_API_V


class SFDCFW:
    """Salesforce.com FrameWork"""

    def __init__(
        self,
        username: str = None,
        password: str = None,
        security_token: str = None,
        client_id: str = None,
        client_secret: str = None,
        version: str = SFDC_API_V,
        domain: str = 'login',
        wsdl: dict = None
    ) -> None:
        """Instantiator.

        Args:
            username (str): The Salesforce user Username.
            password (str): The Salesforce user Password.
            security_token (str): The Salesforce user Security Token.
            client_id (str): The Salesforce Connected App Consumer Key.
            client_secret (str): The Salesforce Connected App Consumer Secret.
            version (str): The Salesforce version of the Application Programming Interface.
            domain (str): The common Salesforce domain for connection (login or test).
            wsdl (dict): The path(s) to the WSDL (Web Services Description Language) file(s).
        """

        # Set the name / label
        self.label = None

        # Get the WSDL
        self.wsdl = wsdl

        # Parse the enterprise WSDL
        enterprise_wsdl = self.wsdl['enterprise']

        # Create an instance of Access object and login
        self.access = Access(username=username,
                             password=password,
                             security_token=security_token,
                             client_id=client_id,
                             client_secret=client_secret,
                             version=version,
                             domain=domain,
                             wsdl=enterprise_wsdl).login()


    def __getattr__(self, label: str) -> SFDCFW:
        """Get Attribute Passed In.

        Args:
            label (str): The attribute passed in.

        Returns:
            A instance of the SFDCFW class.
        """

        # Set the name / label
        self.label = label

        # Return the self instance
        return self


    @property
    def rest(self) -> Rest:
        """Rest

        A Rest property for the REST (REpresentational State Transfer)
        API (Application Programming Interface).

        Returns:
            A instance of the Rest class.
        """

        # Create and instantiate a Rest object
        rest = Rest(self.access)

        # Return the Rest object
        return rest

    
    @property
    def metadata(self):
        """Metadata.

        A Metadata property for the Metadata API (Application
        Programming Interface).
        """

        # Parse the metadata WSDL
        metadata_wsdl = self.wsdl['metadata']

        # Create and instantiate a Metadata object
        metadata = Metadata(self.access, metadata_wsdl)

        # Return the Metadata object
        return metadata
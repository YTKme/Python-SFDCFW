"""
SFDCFW.SFDCFW
~~~~~~~~~~~~~
"""

from __future__ import annotations

from SFDCFW.Access import Access
from SFDCFW.Rest import Rest

from SFDCFW.Constant import SFDC_API_V


class SFDCFW:
    """Salesforce.com FrameWork."""

    def __init__(
        self,
        username: str = None,
        password: str = None,
        security_token: str = None,
        client_id: str = None,
        client_secret: str = None,
        version: str = SFDC_API_V,
        domain: str = 'login',
        wsdl: str = None,
        metadata: str = False
    ) -> None:
        """Instantiator.

        Args:
            username (str): The Salesforce user Username
            password (str): The Salesforce user Password
            security_token (str): The Salesforce user Security Token
            client_id (str): The Salesforce Connected App Consumer Key
            client_secret (str): The Salesforce Connected App Consumer Secret
            version (str): The Salesforce version of the Application Programming Interface
            domain (str): The common Salesforce domain for connection (login or test)
            wsdl (str): The path to the WSDL (Web Services Description Language) file
            metadata (bool): Whether or not this is for metadata
        """

        # Set the name / label
        self.label = None

        # Create an instance of Access object and login
        self.access = Access(username=username,
                             password=password,
                             security_token=security_token,
                             client_id=client_id,
                             client_secret=client_secret,
                             version=version,
                             domain=domain,
                             wsdl=wsdl,
                             metadata=metadata).login()


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
        """Rest.

        A Rest property for the REST (REpresentational State Transfer)
        API (Application Programming Interface)

        Returns:
            A instance of the Rest class.
        """

        # Create and instantiate a Rest object
        rest = Rest(self.access)
        # Return the Rest object
        return rest

    
    def metadata(self):
        """Metadata

        A Metadata property for the Metadata API (Application
        Programming Interface)
        """

        pass
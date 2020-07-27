from setuptools import setup, find_packages

setup(
    name = "SFDCAPI",
    version = "0.1.0",
    packages = find_packages(),

    # Dependency
    install_requires = [
        "pandas",
        "requests",
        "zeep",
    ],

    # Metadata
    author = "Yan Kuang",
    author_email = "YTKme@Outlook.com",
    description = "Saleforce Application Programming Interface.",
    license = "GNU GENERAL PUBLIC LICENSE",
    keywords = "Salesforce"
)
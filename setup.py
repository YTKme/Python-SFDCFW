from setuptools import setup, find_packages

setup(
    name = 'SFDCAPI',
    version = '0.1.0',
    packages = find_packages(),

    # Dependency
    install_requires = [
        'pandas',
        'requests',
        'zeep',
    ],

    # Metadata
    author = 'Yan Kuang',
    author_email = 'YTKme@Outlook.com',
    description = 'Saleforce Application Programming Interface.',
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
    keywords = 'Salesforce',
)
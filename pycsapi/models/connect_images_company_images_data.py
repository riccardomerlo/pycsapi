# coding: utf-8

"""
    Creditsafe Connect

     Last Updated: 09th July 2024<br>  # Introduction   Creditsafe Connect is a REST API that provides access to the <a href=\"https://www.creditsafe.com/gb/en/more/about/our-data.html\" target=\"_blank\">Creditsafe Global Company Database.</a> This allows you to: <ul><li>Control your master data</li><li>Utilize up-to-date Business and Director information, enhancing your onboarding and qualification processes</li><li>Receive alerts when your customer's and supplier's Credit Report changes</li></ul><br>Check the status of Creditsafe Services <a href=\"https://status.creditsafe.com/\" target=\"_blank\">HERE</a>     ## Customer Feedback  Use the buttons below to let us know what you think of this documentation. Please leave comments in your feedback for the author to consider for future versions.<br><br><a href=\"https://app.customerthermometer.com/?template=log_feedback&hash=f49570f5&embed_data=dGVtcGVyYXR1cmVfaWQ9MSZ0aGVybW9tZXRlcl9pZD0xNjM2NTImbnBzX3JhdGluZz0=&e=&f=&l=&c=&c1=&c2=&c3=&c4=&c5=&c6=&c7=&c8=&c9=&c10=\" target=\"_blank\"> <img src=\"https://app.customerthermometer.com/sites/app/images/icon_sets/icon_set_3s/gold.png\" /></a><a href=\"https://app.customerthermometer.com/?template=log_feedback&hash=601a6fd1&embed_data=dGVtcGVyYXR1cmVfaWQ9MiZ0aGVybW9tZXRlcl9pZD0xNjM2NTImbnBzX3JhdGluZz0=&e=&f=&l=&c=&c1=&c2=&c3=&c4=&c5=&c6=&c7=&c8=&c9=&c10=\" target=\"_blank\"><img src=\"https://app.customerthermometer.com/sites/app/images/icon_sets/icon_set_3s/green.png\" /></a><a href=\"https://app.customerthermometer.com/?template=log_feedback&hash=f1f7701c&embed_data=dGVtcGVyYXR1cmVfaWQ9MyZ0aGVybW9tZXRlcl9pZD0xNjM2NTImbnBzX3JhdGluZz0=&e=&f=&l=&c=&c1=&c2=&c3=&c4=&c5=&c6=&c7=&c8=&c9=&c10=\" target=\"_blank\"><img src=\"https://app.customerthermometer.com/sites/app/images/icon_sets/icon_set_3s/amber.png\" /></a><a href=\"https://app.customerthermometer.com/?template=log_feedback&hash=73951e8b&embed_data=dGVtcGVyYXR1cmVfaWQ9NCZ0aGVybW9tZXRlcl9pZD0xNjM2NTImbnBzX3JhdGluZz0=&e=&f=&l=&c=&c1=&c2=&c3=&c4=&c5=&c6=&c7=&c8=&c9=&c10=\" target=\"_blank\"><img src=\"https://app.customerthermometer.com/sites/app/images/icon_sets/icon_set_3s/red.png\" /></a> <br><br> Selecting one of the buttons above will open a new tab to the feedback portal.   ## Quick Start  To start your Creditsafe Connect API integration you will need to have activated your account and set a password by following the instructions in your Welcome Email. If you have not received a Welcome Email please contact your Creditsafe Account Manager.</br></br>By default, you will have been setup on our Sandbox environment.</br></br>  Using a REST API client construct an `/authenticate` POST request and enter your username & password (case-sensitive) into the POST body. A successful response will return an  `authentication token`.</br></br>  Use the `authentication token` in an `Authorization` header on all other Creditsafe Connect calls as proof of your authenticity.   ## Environments  Production Environment baseurl: <code> https://connect.creditsafe.com/v1 </code> </br> Sandbox Test Environment baseurl:  <code>https://connect.sandbox.creditsafe.com/v1</code>    ## Resources   | Item | Description | |----------------|----------------| | <a href=\"https://connect-portal.creditsafe.com\" target=\"_blank\"> A Front End Demo Site</a> | Opens a friendly UI to test the Connect API | | <a href=\"https://creditsafe.github.io/connect-docs/cs_connectv1-15.html\" target=\"_blank\"> Open API Spec </a>  | This will allow you to view the documentation in the swagger portal - this will be discontinued | <a href=\"https://help.creditsafeuk.com/en/support/solutions\" target=\"_blank\"> Help Articles</a> | Opens the Help Hub with a list of common questions and answers | | <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000053487-connect-api-data-dictionaries\" target=\"_blank\"> Data Dictionaries </a> | The connect documentation shows the general use case, the data dictionaries include the additional specific data that is returned by individual countries | | <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000054765-connect-api-data-availability-per-country\" target=\"_blank\"> Data Availability per Country </a> | The Data Matrix is a document that outlines all the fields that are available in the company report for an online territory | | <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000054656-connect-api-feature-availability-per-country\" target=\"_blank\"> Creditsafe Online Country Feature Availability</a> | This matrix displays what features are available with the online Creditsafe Countries and the partner network | | <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000063360-connect-report-templates-glossary-availability\" target=\"_blank\"> Connect Report Templates </a> | The document identifies the templates available for specific parts of the Company Credit Report, avoiding the need to order the full report object in one API call. | | <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000081984-connect-api-server-response-codes\" target=\"_blank\"> Connect API Response Codes </a> | Opens up a basic table of response codes, provides a link to a more detailed response code list |   <br>    ## Versioning and Changes    ### Non-Breaking Changes   Non-breaking changes will generally include additive functions or bug fixes. It is crucial for the integration of the code to be done in such a way that it does not depend on the sequence in which items are returned. This ensures that updates can be applied seamlessly without affecting the existing functionality.    ### Breaking Changes   Breaking changes refer to any modifications to the API's functionality that could disrupt the current contract of the API. Such changes necessitate communication with stakeholders and will lead to a major version number update, indicating the significant nature of these changes.   # noqa: E501

    OpenAPI spec version: 1.10.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ConnectImagesCompanyImagesData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'image_id': 'str',
        'company': 'ConnectImagesCompanyImagesCompany',
        'document': 'ConnectImagesCompanyImagesDocument',
        'format': 'str',
        'source': 'str',
        'filing_date': 'str',
        'upload_date': 'str',
        'accounting_date': 'str',
        'language': 'str',
        'comments': 'str',
        'status': 'str',
        'available_formats': 'list[str]',
        'local_properties': 'ConnectImagesCompanyImagesLocalProperties'
    }

    attribute_map = {
        'image_id': 'imageId',
        'company': 'company',
        'document': 'document',
        'format': 'format',
        'source': 'source',
        'filing_date': 'filingDate',
        'upload_date': 'uploadDate',
        'accounting_date': 'accountingDate',
        'language': 'language',
        'comments': 'comments',
        'status': 'status',
        'available_formats': 'availableFormats',
        'local_properties': 'localProperties'
    }

    def __init__(self, image_id=None, company=None, document=None, format=None, source=None, filing_date=None, upload_date=None, accounting_date=None, language=None, comments=None, status=None, available_formats=None, local_properties=None):  # noqa: E501
        """ConnectImagesCompanyImagesData - a model defined in Swagger"""  # noqa: E501
        self._image_id = None
        self._company = None
        self._document = None
        self._format = None
        self._source = None
        self._filing_date = None
        self._upload_date = None
        self._accounting_date = None
        self._language = None
        self._comments = None
        self._status = None
        self._available_formats = None
        self._local_properties = None
        self.discriminator = None
        if image_id is not None:
            self.image_id = image_id
        if company is not None:
            self.company = company
        if document is not None:
            self.document = document
        if format is not None:
            self.format = format
        if source is not None:
            self.source = source
        if filing_date is not None:
            self.filing_date = filing_date
        if upload_date is not None:
            self.upload_date = upload_date
        if accounting_date is not None:
            self.accounting_date = accounting_date
        if language is not None:
            self.language = language
        if comments is not None:
            self.comments = comments
        if status is not None:
            self.status = status
        if available_formats is not None:
            self.available_formats = available_formats
        if local_properties is not None:
            self.local_properties = local_properties

    @property
    def image_id(self):
        """Gets the image_id of this ConnectImagesCompanyImagesData.  # noqa: E501


        :return: The image_id of this ConnectImagesCompanyImagesData.  # noqa: E501
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """Sets the image_id of this ConnectImagesCompanyImagesData.


        :param image_id: The image_id of this ConnectImagesCompanyImagesData.  # noqa: E501
        :type: str
        """

        self._image_id = image_id

    @property
    def company(self):
        """Gets the company of this ConnectImagesCompanyImagesData.  # noqa: E501


        :return: The company of this ConnectImagesCompanyImagesData.  # noqa: E501
        :rtype: ConnectImagesCompanyImagesCompany
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this ConnectImagesCompanyImagesData.


        :param company: The company of this ConnectImagesCompanyImagesData.  # noqa: E501
        :type: ConnectImagesCompanyImagesCompany
        """

        self._company = company

    @property
    def document(self):
        """Gets the document of this ConnectImagesCompanyImagesData.  # noqa: E501


        :return: The document of this ConnectImagesCompanyImagesData.  # noqa: E501
        :rtype: ConnectImagesCompanyImagesDocument
        """
        return self._document

    @document.setter
    def document(self, document):
        """Sets the document of this ConnectImagesCompanyImagesData.


        :param document: The document of this ConnectImagesCompanyImagesData.  # noqa: E501
        :type: ConnectImagesCompanyImagesDocument
        """

        self._document = document

    @property
    def format(self):
        """Gets the format of this ConnectImagesCompanyImagesData.  # noqa: E501


        :return: The format of this ConnectImagesCompanyImagesData.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this ConnectImagesCompanyImagesData.


        :param format: The format of this ConnectImagesCompanyImagesData.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def source(self):
        """Gets the source of this ConnectImagesCompanyImagesData.  # noqa: E501


        :return: The source of this ConnectImagesCompanyImagesData.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ConnectImagesCompanyImagesData.


        :param source: The source of this ConnectImagesCompanyImagesData.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def filing_date(self):
        """Gets the filing_date of this ConnectImagesCompanyImagesData.  # noqa: E501


        :return: The filing_date of this ConnectImagesCompanyImagesData.  # noqa: E501
        :rtype: str
        """
        return self._filing_date

    @filing_date.setter
    def filing_date(self, filing_date):
        """Sets the filing_date of this ConnectImagesCompanyImagesData.


        :param filing_date: The filing_date of this ConnectImagesCompanyImagesData.  # noqa: E501
        :type: str
        """

        self._filing_date = filing_date

    @property
    def upload_date(self):
        """Gets the upload_date of this ConnectImagesCompanyImagesData.  # noqa: E501


        :return: The upload_date of this ConnectImagesCompanyImagesData.  # noqa: E501
        :rtype: str
        """
        return self._upload_date

    @upload_date.setter
    def upload_date(self, upload_date):
        """Sets the upload_date of this ConnectImagesCompanyImagesData.


        :param upload_date: The upload_date of this ConnectImagesCompanyImagesData.  # noqa: E501
        :type: str
        """

        self._upload_date = upload_date

    @property
    def accounting_date(self):
        """Gets the accounting_date of this ConnectImagesCompanyImagesData.  # noqa: E501


        :return: The accounting_date of this ConnectImagesCompanyImagesData.  # noqa: E501
        :rtype: str
        """
        return self._accounting_date

    @accounting_date.setter
    def accounting_date(self, accounting_date):
        """Sets the accounting_date of this ConnectImagesCompanyImagesData.


        :param accounting_date: The accounting_date of this ConnectImagesCompanyImagesData.  # noqa: E501
        :type: str
        """

        self._accounting_date = accounting_date

    @property
    def language(self):
        """Gets the language of this ConnectImagesCompanyImagesData.  # noqa: E501


        :return: The language of this ConnectImagesCompanyImagesData.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ConnectImagesCompanyImagesData.


        :param language: The language of this ConnectImagesCompanyImagesData.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def comments(self):
        """Gets the comments of this ConnectImagesCompanyImagesData.  # noqa: E501


        :return: The comments of this ConnectImagesCompanyImagesData.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this ConnectImagesCompanyImagesData.


        :param comments: The comments of this ConnectImagesCompanyImagesData.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def status(self):
        """Gets the status of this ConnectImagesCompanyImagesData.  # noqa: E501


        :return: The status of this ConnectImagesCompanyImagesData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConnectImagesCompanyImagesData.


        :param status: The status of this ConnectImagesCompanyImagesData.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def available_formats(self):
        """Gets the available_formats of this ConnectImagesCompanyImagesData.  # noqa: E501


        :return: The available_formats of this ConnectImagesCompanyImagesData.  # noqa: E501
        :rtype: list[str]
        """
        return self._available_formats

    @available_formats.setter
    def available_formats(self, available_formats):
        """Sets the available_formats of this ConnectImagesCompanyImagesData.


        :param available_formats: The available_formats of this ConnectImagesCompanyImagesData.  # noqa: E501
        :type: list[str]
        """

        self._available_formats = available_formats

    @property
    def local_properties(self):
        """Gets the local_properties of this ConnectImagesCompanyImagesData.  # noqa: E501


        :return: The local_properties of this ConnectImagesCompanyImagesData.  # noqa: E501
        :rtype: ConnectImagesCompanyImagesLocalProperties
        """
        return self._local_properties

    @local_properties.setter
    def local_properties(self, local_properties):
        """Sets the local_properties of this ConnectImagesCompanyImagesData.


        :param local_properties: The local_properties of this ConnectImagesCompanyImagesData.  # noqa: E501
        :type: ConnectImagesCompanyImagesLocalProperties
        """

        self._local_properties = local_properties

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ConnectImagesCompanyImagesData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConnectImagesCompanyImagesData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

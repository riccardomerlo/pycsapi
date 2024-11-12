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

class ConnectBankMatchResultBankMatchResults(object):
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
        'company_number': 'str',
        'account_number': 'str',
        'iban': 'str',
        'iban_result': 'str',
        'iban_text': 'str',
        'log_date': 'str',
        'safe_number': 'str',
        'scan_result': 'str',
        'scan_text': 'str',
        'sort_code': 'str',
        'status_result': 'str',
        'status_text': 'str',
        'vat_result': 'str',
        'vat_text': 'str'
    }

    attribute_map = {
        'company_number': 'companyNumber',
        'account_number': 'accountNumber',
        'iban': 'iban',
        'iban_result': 'ibanResult',
        'iban_text': 'ibanText',
        'log_date': 'logDate',
        'safe_number': 'safeNumber',
        'scan_result': 'scanResult',
        'scan_text': 'scanText',
        'sort_code': 'sortCode',
        'status_result': 'statusResult',
        'status_text': 'statusText',
        'vat_result': 'vatResult',
        'vat_text': 'vatText'
    }

    def __init__(self, company_number=None, account_number=None, iban=None, iban_result=None, iban_text=None, log_date=None, safe_number=None, scan_result=None, scan_text=None, sort_code=None, status_result=None, status_text=None, vat_result=None, vat_text=None):  # noqa: E501
        """ConnectBankMatchResultBankMatchResults - a model defined in Swagger"""  # noqa: E501
        self._company_number = None
        self._account_number = None
        self._iban = None
        self._iban_result = None
        self._iban_text = None
        self._log_date = None
        self._safe_number = None
        self._scan_result = None
        self._scan_text = None
        self._sort_code = None
        self._status_result = None
        self._status_text = None
        self._vat_result = None
        self._vat_text = None
        self.discriminator = None
        if company_number is not None:
            self.company_number = company_number
        if account_number is not None:
            self.account_number = account_number
        if iban is not None:
            self.iban = iban
        if iban_result is not None:
            self.iban_result = iban_result
        if iban_text is not None:
            self.iban_text = iban_text
        if log_date is not None:
            self.log_date = log_date
        if safe_number is not None:
            self.safe_number = safe_number
        if scan_result is not None:
            self.scan_result = scan_result
        if scan_text is not None:
            self.scan_text = scan_text
        if sort_code is not None:
            self.sort_code = sort_code
        if status_result is not None:
            self.status_result = status_result
        if status_text is not None:
            self.status_text = status_text
        if vat_result is not None:
            self.vat_result = vat_result
        if vat_text is not None:
            self.vat_text = vat_text

    @property
    def company_number(self):
        """Gets the company_number of this ConnectBankMatchResultBankMatchResults.  # noqa: E501


        :return: The company_number of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :rtype: str
        """
        return self._company_number

    @company_number.setter
    def company_number(self, company_number):
        """Sets the company_number of this ConnectBankMatchResultBankMatchResults.


        :param company_number: The company_number of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :type: str
        """

        self._company_number = company_number

    @property
    def account_number(self):
        """Gets the account_number of this ConnectBankMatchResultBankMatchResults.  # noqa: E501


        :return: The account_number of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this ConnectBankMatchResultBankMatchResults.


        :param account_number: The account_number of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def iban(self):
        """Gets the iban of this ConnectBankMatchResultBankMatchResults.  # noqa: E501


        :return: The iban of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this ConnectBankMatchResultBankMatchResults.


        :param iban: The iban of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :type: str
        """

        self._iban = iban

    @property
    def iban_result(self):
        """Gets the iban_result of this ConnectBankMatchResultBankMatchResults.  # noqa: E501

        Match or No Match  # noqa: E501

        :return: The iban_result of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :rtype: str
        """
        return self._iban_result

    @iban_result.setter
    def iban_result(self, iban_result):
        """Sets the iban_result of this ConnectBankMatchResultBankMatchResults.

        Match or No Match  # noqa: E501

        :param iban_result: The iban_result of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :type: str
        """

        self._iban_result = iban_result

    @property
    def iban_text(self):
        """Gets the iban_text of this ConnectBankMatchResultBankMatchResults.  # noqa: E501


        :return: The iban_text of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :rtype: str
        """
        return self._iban_text

    @iban_text.setter
    def iban_text(self, iban_text):
        """Sets the iban_text of this ConnectBankMatchResultBankMatchResults.


        :param iban_text: The iban_text of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :type: str
        """

        self._iban_text = iban_text

    @property
    def log_date(self):
        """Gets the log_date of this ConnectBankMatchResultBankMatchResults.  # noqa: E501


        :return: The log_date of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :rtype: str
        """
        return self._log_date

    @log_date.setter
    def log_date(self, log_date):
        """Sets the log_date of this ConnectBankMatchResultBankMatchResults.


        :param log_date: The log_date of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :type: str
        """

        self._log_date = log_date

    @property
    def safe_number(self):
        """Gets the safe_number of this ConnectBankMatchResultBankMatchResults.  # noqa: E501


        :return: The safe_number of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :rtype: str
        """
        return self._safe_number

    @safe_number.setter
    def safe_number(self, safe_number):
        """Sets the safe_number of this ConnectBankMatchResultBankMatchResults.


        :param safe_number: The safe_number of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :type: str
        """

        self._safe_number = safe_number

    @property
    def scan_result(self):
        """Gets the scan_result of this ConnectBankMatchResultBankMatchResults.  # noqa: E501

        Match or No Match  # noqa: E501

        :return: The scan_result of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :rtype: str
        """
        return self._scan_result

    @scan_result.setter
    def scan_result(self, scan_result):
        """Sets the scan_result of this ConnectBankMatchResultBankMatchResults.

        Match or No Match  # noqa: E501

        :param scan_result: The scan_result of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :type: str
        """

        self._scan_result = scan_result

    @property
    def scan_text(self):
        """Gets the scan_text of this ConnectBankMatchResultBankMatchResults.  # noqa: E501


        :return: The scan_text of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :rtype: str
        """
        return self._scan_text

    @scan_text.setter
    def scan_text(self, scan_text):
        """Sets the scan_text of this ConnectBankMatchResultBankMatchResults.


        :param scan_text: The scan_text of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :type: str
        """

        self._scan_text = scan_text

    @property
    def sort_code(self):
        """Gets the sort_code of this ConnectBankMatchResultBankMatchResults.  # noqa: E501


        :return: The sort_code of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :rtype: str
        """
        return self._sort_code

    @sort_code.setter
    def sort_code(self, sort_code):
        """Sets the sort_code of this ConnectBankMatchResultBankMatchResults.


        :param sort_code: The sort_code of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :type: str
        """

        self._sort_code = sort_code

    @property
    def status_result(self):
        """Gets the status_result of this ConnectBankMatchResultBankMatchResults.  # noqa: E501

        Request status, e.g. Success, Error, Warning  # noqa: E501

        :return: The status_result of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :rtype: str
        """
        return self._status_result

    @status_result.setter
    def status_result(self, status_result):
        """Sets the status_result of this ConnectBankMatchResultBankMatchResults.

        Request status, e.g. Success, Error, Warning  # noqa: E501

        :param status_result: The status_result of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :type: str
        """

        self._status_result = status_result

    @property
    def status_text(self):
        """Gets the status_text of this ConnectBankMatchResultBankMatchResults.  # noqa: E501

        Explanation for error or warning, if applicable, otherwise empty quotation marks  # noqa: E501

        :return: The status_text of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :rtype: str
        """
        return self._status_text

    @status_text.setter
    def status_text(self, status_text):
        """Sets the status_text of this ConnectBankMatchResultBankMatchResults.

        Explanation for error or warning, if applicable, otherwise empty quotation marks  # noqa: E501

        :param status_text: The status_text of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :type: str
        """

        self._status_text = status_text

    @property
    def vat_result(self):
        """Gets the vat_result of this ConnectBankMatchResultBankMatchResults.  # noqa: E501

        Match or No Match  # noqa: E501

        :return: The vat_result of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :rtype: str
        """
        return self._vat_result

    @vat_result.setter
    def vat_result(self, vat_result):
        """Sets the vat_result of this ConnectBankMatchResultBankMatchResults.

        Match or No Match  # noqa: E501

        :param vat_result: The vat_result of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :type: str
        """

        self._vat_result = vat_result

    @property
    def vat_text(self):
        """Gets the vat_text of this ConnectBankMatchResultBankMatchResults.  # noqa: E501


        :return: The vat_text of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :rtype: str
        """
        return self._vat_text

    @vat_text.setter
    def vat_text(self, vat_text):
        """Sets the vat_text of this ConnectBankMatchResultBankMatchResults.


        :param vat_text: The vat_text of this ConnectBankMatchResultBankMatchResults.  # noqa: E501
        :type: str
        """

        self._vat_text = vat_text

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
        if issubclass(ConnectBankMatchResultBankMatchResults, dict):
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
        if not isinstance(other, ConnectBankMatchResultBankMatchResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

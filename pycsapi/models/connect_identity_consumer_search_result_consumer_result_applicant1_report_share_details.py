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

class ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails(object):
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
        'account_number': 'str',
        'account_suffix': 'str',
        'joint': 'bool',
        'status': 'str',
        'date_updated': 'datetime',
        'currency_code': 'str',
        'balance': 'int',
        'limit': 'int',
        'opening_balance': 'int',
        'payment_start_date': 'datetime',
        'account_start_date': 'datetime',
        'regular_payment': 'int',
        'repayment_period': 'int',
        'lump_payment': 'int',
        'repayment_frequency_code': 'str',
        'repayment_frequency': 'str'
    }

    attribute_map = {
        'account_number': 'accountNumber',
        'account_suffix': 'accountSuffix',
        'joint': 'joint',
        'status': 'status',
        'date_updated': 'dateUpdated',
        'currency_code': 'currencyCode',
        'balance': 'balance',
        'limit': 'limit',
        'opening_balance': 'openingBalance',
        'payment_start_date': 'paymentStartDate',
        'account_start_date': 'accountStartDate',
        'regular_payment': 'regularPayment',
        'repayment_period': 'repaymentPeriod',
        'lump_payment': 'lumpPayment',
        'repayment_frequency_code': 'repaymentFrequencyCode',
        'repayment_frequency': 'repaymentFrequency'
    }

    def __init__(self, account_number=None, account_suffix=None, joint=None, status=None, date_updated=None, currency_code=None, balance=None, limit=None, opening_balance=None, payment_start_date=None, account_start_date=None, regular_payment=None, repayment_period=None, lump_payment=None, repayment_frequency_code=None, repayment_frequency=None):  # noqa: E501
        """ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails - a model defined in Swagger"""  # noqa: E501
        self._account_number = None
        self._account_suffix = None
        self._joint = None
        self._status = None
        self._date_updated = None
        self._currency_code = None
        self._balance = None
        self._limit = None
        self._opening_balance = None
        self._payment_start_date = None
        self._account_start_date = None
        self._regular_payment = None
        self._repayment_period = None
        self._lump_payment = None
        self._repayment_frequency_code = None
        self._repayment_frequency = None
        self.discriminator = None
        if account_number is not None:
            self.account_number = account_number
        if account_suffix is not None:
            self.account_suffix = account_suffix
        if joint is not None:
            self.joint = joint
        if status is not None:
            self.status = status
        if date_updated is not None:
            self.date_updated = date_updated
        if currency_code is not None:
            self.currency_code = currency_code
        if balance is not None:
            self.balance = balance
        if limit is not None:
            self.limit = limit
        if opening_balance is not None:
            self.opening_balance = opening_balance
        if payment_start_date is not None:
            self.payment_start_date = payment_start_date
        if account_start_date is not None:
            self.account_start_date = account_start_date
        if regular_payment is not None:
            self.regular_payment = regular_payment
        if repayment_period is not None:
            self.repayment_period = repayment_period
        if lump_payment is not None:
            self.lump_payment = lump_payment
        if repayment_frequency_code is not None:
            self.repayment_frequency_code = repayment_frequency_code
        if repayment_frequency is not None:
            self.repayment_frequency = repayment_frequency

    @property
    def account_number(self):
        """Gets the account_number of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501


        :return: The account_number of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.


        :param account_number: The account_number of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def account_suffix(self):
        """Gets the account_suffix of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501


        :return: The account_suffix of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :rtype: str
        """
        return self._account_suffix

    @account_suffix.setter
    def account_suffix(self, account_suffix):
        """Sets the account_suffix of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.


        :param account_suffix: The account_suffix of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :type: str
        """

        self._account_suffix = account_suffix

    @property
    def joint(self):
        """Gets the joint of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501


        :return: The joint of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :rtype: bool
        """
        return self._joint

    @joint.setter
    def joint(self, joint):
        """Sets the joint of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.


        :param joint: The joint of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :type: bool
        """

        self._joint = joint

    @property
    def status(self):
        """Gets the status of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501


        :return: The status of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.


        :param status: The status of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def date_updated(self):
        """Gets the date_updated of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501


        :return: The date_updated of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """Sets the date_updated of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.


        :param date_updated: The date_updated of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :type: datetime
        """

        self._date_updated = date_updated

    @property
    def currency_code(self):
        """Gets the currency_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501


        :return: The currency_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.


        :param currency_code: The currency_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def balance(self):
        """Gets the balance of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501


        :return: The balance of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :rtype: int
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.


        :param balance: The balance of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :type: int
        """

        self._balance = balance

    @property
    def limit(self):
        """Gets the limit of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501


        :return: The limit of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.


        :param limit: The limit of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def opening_balance(self):
        """Gets the opening_balance of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501


        :return: The opening_balance of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :rtype: int
        """
        return self._opening_balance

    @opening_balance.setter
    def opening_balance(self, opening_balance):
        """Sets the opening_balance of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.


        :param opening_balance: The opening_balance of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :type: int
        """

        self._opening_balance = opening_balance

    @property
    def payment_start_date(self):
        """Gets the payment_start_date of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501


        :return: The payment_start_date of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._payment_start_date

    @payment_start_date.setter
    def payment_start_date(self, payment_start_date):
        """Sets the payment_start_date of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.


        :param payment_start_date: The payment_start_date of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :type: datetime
        """

        self._payment_start_date = payment_start_date

    @property
    def account_start_date(self):
        """Gets the account_start_date of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501


        :return: The account_start_date of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._account_start_date

    @account_start_date.setter
    def account_start_date(self, account_start_date):
        """Sets the account_start_date of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.


        :param account_start_date: The account_start_date of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :type: datetime
        """

        self._account_start_date = account_start_date

    @property
    def regular_payment(self):
        """Gets the regular_payment of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501


        :return: The regular_payment of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :rtype: int
        """
        return self._regular_payment

    @regular_payment.setter
    def regular_payment(self, regular_payment):
        """Sets the regular_payment of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.


        :param regular_payment: The regular_payment of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :type: int
        """

        self._regular_payment = regular_payment

    @property
    def repayment_period(self):
        """Gets the repayment_period of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501


        :return: The repayment_period of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :rtype: int
        """
        return self._repayment_period

    @repayment_period.setter
    def repayment_period(self, repayment_period):
        """Sets the repayment_period of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.


        :param repayment_period: The repayment_period of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :type: int
        """

        self._repayment_period = repayment_period

    @property
    def lump_payment(self):
        """Gets the lump_payment of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501


        :return: The lump_payment of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :rtype: int
        """
        return self._lump_payment

    @lump_payment.setter
    def lump_payment(self, lump_payment):
        """Sets the lump_payment of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.


        :param lump_payment: The lump_payment of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :type: int
        """

        self._lump_payment = lump_payment

    @property
    def repayment_frequency_code(self):
        """Gets the repayment_frequency_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501


        :return: The repayment_frequency_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :rtype: str
        """
        return self._repayment_frequency_code

    @repayment_frequency_code.setter
    def repayment_frequency_code(self, repayment_frequency_code):
        """Sets the repayment_frequency_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.


        :param repayment_frequency_code: The repayment_frequency_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :type: str
        """

        self._repayment_frequency_code = repayment_frequency_code

    @property
    def repayment_frequency(self):
        """Gets the repayment_frequency of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501


        :return: The repayment_frequency of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :rtype: str
        """
        return self._repayment_frequency

    @repayment_frequency.setter
    def repayment_frequency(self, repayment_frequency):
        """Sets the repayment_frequency of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.


        :param repayment_frequency: The repayment_frequency of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails.  # noqa: E501
        :type: str
        """

        self._repayment_frequency = repayment_frequency

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
        if issubclass(ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails, dict):
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
        if not isinstance(other, ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShareDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

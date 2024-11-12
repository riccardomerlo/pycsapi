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

class ConnectIdentityShareAccountDetails(object):
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
        'account_suffix': 'int',
        'joint': 'bool',
        'status': 'str',
        'date_updated': 'datetime',
        'currency_code': 'str',
        'balance': 'int',
        'limit': 'int',
        'opening_balance': 'int',
        'arrangement_start_date': 'datetime',
        'arrangement_end_date': 'datetime',
        'payment_start_date': 'datetime',
        'account_start_date': 'datetime',
        'account_end_date': 'datetime',
        'regular_payment': 'int',
        'expected_payment': 'int',
        'actual_payment': 'int',
        'repayment_period': 'int',
        'lump_payment': 'int',
        'penalty_interest_amount': 'int',
        'promotional_rate': 'bool',
        'minimum_payment': 'bool',
        'statement_balance': 'int',
        'type_code': 'str',
        'type': 'str',
        'group_id': 'int',
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
        'arrangement_start_date': 'arrangementStartDate',
        'arrangement_end_date': 'arrangementEndDate',
        'payment_start_date': 'paymentStartDate',
        'account_start_date': 'accountStartDate',
        'account_end_date': 'accountEndDate',
        'regular_payment': 'regularPayment',
        'expected_payment': 'expectedPayment',
        'actual_payment': 'actualPayment',
        'repayment_period': 'repaymentPeriod',
        'lump_payment': 'lumpPayment',
        'penalty_interest_amount': 'penaltyInterestAmount',
        'promotional_rate': 'promotionalRate',
        'minimum_payment': 'minimumPayment',
        'statement_balance': 'statementBalance',
        'type_code': 'typeCode',
        'type': 'type',
        'group_id': 'groupId',
        'repayment_frequency_code': 'repaymentFrequencyCode',
        'repayment_frequency': 'repaymentFrequency'
    }

    def __init__(self, account_number=None, account_suffix=None, joint=None, status=None, date_updated=None, currency_code=None, balance=None, limit=None, opening_balance=None, arrangement_start_date=None, arrangement_end_date=None, payment_start_date=None, account_start_date=None, account_end_date=None, regular_payment=None, expected_payment=None, actual_payment=None, repayment_period=None, lump_payment=None, penalty_interest_amount=None, promotional_rate=None, minimum_payment=None, statement_balance=None, type_code=None, type=None, group_id=None, repayment_frequency_code=None, repayment_frequency=None):  # noqa: E501
        """ConnectIdentityShareAccountDetails - a model defined in Swagger"""  # noqa: E501
        self._account_number = None
        self._account_suffix = None
        self._joint = None
        self._status = None
        self._date_updated = None
        self._currency_code = None
        self._balance = None
        self._limit = None
        self._opening_balance = None
        self._arrangement_start_date = None
        self._arrangement_end_date = None
        self._payment_start_date = None
        self._account_start_date = None
        self._account_end_date = None
        self._regular_payment = None
        self._expected_payment = None
        self._actual_payment = None
        self._repayment_period = None
        self._lump_payment = None
        self._penalty_interest_amount = None
        self._promotional_rate = None
        self._minimum_payment = None
        self._statement_balance = None
        self._type_code = None
        self._type = None
        self._group_id = None
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
        if arrangement_start_date is not None:
            self.arrangement_start_date = arrangement_start_date
        if arrangement_end_date is not None:
            self.arrangement_end_date = arrangement_end_date
        if payment_start_date is not None:
            self.payment_start_date = payment_start_date
        if account_start_date is not None:
            self.account_start_date = account_start_date
        if account_end_date is not None:
            self.account_end_date = account_end_date
        if regular_payment is not None:
            self.regular_payment = regular_payment
        if expected_payment is not None:
            self.expected_payment = expected_payment
        if actual_payment is not None:
            self.actual_payment = actual_payment
        if repayment_period is not None:
            self.repayment_period = repayment_period
        if lump_payment is not None:
            self.lump_payment = lump_payment
        if penalty_interest_amount is not None:
            self.penalty_interest_amount = penalty_interest_amount
        if promotional_rate is not None:
            self.promotional_rate = promotional_rate
        if minimum_payment is not None:
            self.minimum_payment = minimum_payment
        if statement_balance is not None:
            self.statement_balance = statement_balance
        if type_code is not None:
            self.type_code = type_code
        if type is not None:
            self.type = type
        if group_id is not None:
            self.group_id = group_id
        if repayment_frequency_code is not None:
            self.repayment_frequency_code = repayment_frequency_code
        if repayment_frequency is not None:
            self.repayment_frequency = repayment_frequency

    @property
    def account_number(self):
        """Gets the account_number of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The account_number of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this ConnectIdentityShareAccountDetails.


        :param account_number: The account_number of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def account_suffix(self):
        """Gets the account_suffix of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The account_suffix of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: int
        """
        return self._account_suffix

    @account_suffix.setter
    def account_suffix(self, account_suffix):
        """Sets the account_suffix of this ConnectIdentityShareAccountDetails.


        :param account_suffix: The account_suffix of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: int
        """

        self._account_suffix = account_suffix

    @property
    def joint(self):
        """Gets the joint of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The joint of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: bool
        """
        return self._joint

    @joint.setter
    def joint(self, joint):
        """Sets the joint of this ConnectIdentityShareAccountDetails.


        :param joint: The joint of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: bool
        """

        self._joint = joint

    @property
    def status(self):
        """Gets the status of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The status of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConnectIdentityShareAccountDetails.


        :param status: The status of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def date_updated(self):
        """Gets the date_updated of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The date_updated of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """Sets the date_updated of this ConnectIdentityShareAccountDetails.


        :param date_updated: The date_updated of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: datetime
        """

        self._date_updated = date_updated

    @property
    def currency_code(self):
        """Gets the currency_code of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The currency_code of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this ConnectIdentityShareAccountDetails.


        :param currency_code: The currency_code of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def balance(self):
        """Gets the balance of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The balance of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: int
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this ConnectIdentityShareAccountDetails.


        :param balance: The balance of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: int
        """

        self._balance = balance

    @property
    def limit(self):
        """Gets the limit of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The limit of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ConnectIdentityShareAccountDetails.


        :param limit: The limit of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def opening_balance(self):
        """Gets the opening_balance of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The opening_balance of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: int
        """
        return self._opening_balance

    @opening_balance.setter
    def opening_balance(self, opening_balance):
        """Sets the opening_balance of this ConnectIdentityShareAccountDetails.


        :param opening_balance: The opening_balance of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: int
        """

        self._opening_balance = opening_balance

    @property
    def arrangement_start_date(self):
        """Gets the arrangement_start_date of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The arrangement_start_date of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._arrangement_start_date

    @arrangement_start_date.setter
    def arrangement_start_date(self, arrangement_start_date):
        """Sets the arrangement_start_date of this ConnectIdentityShareAccountDetails.


        :param arrangement_start_date: The arrangement_start_date of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: datetime
        """

        self._arrangement_start_date = arrangement_start_date

    @property
    def arrangement_end_date(self):
        """Gets the arrangement_end_date of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The arrangement_end_date of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._arrangement_end_date

    @arrangement_end_date.setter
    def arrangement_end_date(self, arrangement_end_date):
        """Sets the arrangement_end_date of this ConnectIdentityShareAccountDetails.


        :param arrangement_end_date: The arrangement_end_date of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: datetime
        """

        self._arrangement_end_date = arrangement_end_date

    @property
    def payment_start_date(self):
        """Gets the payment_start_date of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The payment_start_date of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._payment_start_date

    @payment_start_date.setter
    def payment_start_date(self, payment_start_date):
        """Sets the payment_start_date of this ConnectIdentityShareAccountDetails.


        :param payment_start_date: The payment_start_date of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: datetime
        """

        self._payment_start_date = payment_start_date

    @property
    def account_start_date(self):
        """Gets the account_start_date of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The account_start_date of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._account_start_date

    @account_start_date.setter
    def account_start_date(self, account_start_date):
        """Sets the account_start_date of this ConnectIdentityShareAccountDetails.


        :param account_start_date: The account_start_date of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: datetime
        """

        self._account_start_date = account_start_date

    @property
    def account_end_date(self):
        """Gets the account_end_date of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The account_end_date of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: datetime
        """
        return self._account_end_date

    @account_end_date.setter
    def account_end_date(self, account_end_date):
        """Sets the account_end_date of this ConnectIdentityShareAccountDetails.


        :param account_end_date: The account_end_date of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: datetime
        """

        self._account_end_date = account_end_date

    @property
    def regular_payment(self):
        """Gets the regular_payment of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The regular_payment of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: int
        """
        return self._regular_payment

    @regular_payment.setter
    def regular_payment(self, regular_payment):
        """Sets the regular_payment of this ConnectIdentityShareAccountDetails.


        :param regular_payment: The regular_payment of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: int
        """

        self._regular_payment = regular_payment

    @property
    def expected_payment(self):
        """Gets the expected_payment of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The expected_payment of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: int
        """
        return self._expected_payment

    @expected_payment.setter
    def expected_payment(self, expected_payment):
        """Sets the expected_payment of this ConnectIdentityShareAccountDetails.


        :param expected_payment: The expected_payment of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: int
        """

        self._expected_payment = expected_payment

    @property
    def actual_payment(self):
        """Gets the actual_payment of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The actual_payment of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: int
        """
        return self._actual_payment

    @actual_payment.setter
    def actual_payment(self, actual_payment):
        """Sets the actual_payment of this ConnectIdentityShareAccountDetails.


        :param actual_payment: The actual_payment of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: int
        """

        self._actual_payment = actual_payment

    @property
    def repayment_period(self):
        """Gets the repayment_period of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The repayment_period of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: int
        """
        return self._repayment_period

    @repayment_period.setter
    def repayment_period(self, repayment_period):
        """Sets the repayment_period of this ConnectIdentityShareAccountDetails.


        :param repayment_period: The repayment_period of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: int
        """

        self._repayment_period = repayment_period

    @property
    def lump_payment(self):
        """Gets the lump_payment of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The lump_payment of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: int
        """
        return self._lump_payment

    @lump_payment.setter
    def lump_payment(self, lump_payment):
        """Sets the lump_payment of this ConnectIdentityShareAccountDetails.


        :param lump_payment: The lump_payment of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: int
        """

        self._lump_payment = lump_payment

    @property
    def penalty_interest_amount(self):
        """Gets the penalty_interest_amount of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The penalty_interest_amount of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: int
        """
        return self._penalty_interest_amount

    @penalty_interest_amount.setter
    def penalty_interest_amount(self, penalty_interest_amount):
        """Sets the penalty_interest_amount of this ConnectIdentityShareAccountDetails.


        :param penalty_interest_amount: The penalty_interest_amount of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: int
        """

        self._penalty_interest_amount = penalty_interest_amount

    @property
    def promotional_rate(self):
        """Gets the promotional_rate of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The promotional_rate of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: bool
        """
        return self._promotional_rate

    @promotional_rate.setter
    def promotional_rate(self, promotional_rate):
        """Sets the promotional_rate of this ConnectIdentityShareAccountDetails.


        :param promotional_rate: The promotional_rate of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: bool
        """

        self._promotional_rate = promotional_rate

    @property
    def minimum_payment(self):
        """Gets the minimum_payment of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The minimum_payment of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: bool
        """
        return self._minimum_payment

    @minimum_payment.setter
    def minimum_payment(self, minimum_payment):
        """Sets the minimum_payment of this ConnectIdentityShareAccountDetails.


        :param minimum_payment: The minimum_payment of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: bool
        """

        self._minimum_payment = minimum_payment

    @property
    def statement_balance(self):
        """Gets the statement_balance of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The statement_balance of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: int
        """
        return self._statement_balance

    @statement_balance.setter
    def statement_balance(self, statement_balance):
        """Sets the statement_balance of this ConnectIdentityShareAccountDetails.


        :param statement_balance: The statement_balance of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: int
        """

        self._statement_balance = statement_balance

    @property
    def type_code(self):
        """Gets the type_code of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The type_code of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._type_code

    @type_code.setter
    def type_code(self, type_code):
        """Sets the type_code of this ConnectIdentityShareAccountDetails.


        :param type_code: The type_code of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: str
        """

        self._type_code = type_code

    @property
    def type(self):
        """Gets the type of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The type of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConnectIdentityShareAccountDetails.


        :param type: The type of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def group_id(self):
        """Gets the group_id of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The group_id of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ConnectIdentityShareAccountDetails.


        :param group_id: The group_id of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: int
        """

        self._group_id = group_id

    @property
    def repayment_frequency_code(self):
        """Gets the repayment_frequency_code of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The repayment_frequency_code of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._repayment_frequency_code

    @repayment_frequency_code.setter
    def repayment_frequency_code(self, repayment_frequency_code):
        """Sets the repayment_frequency_code of this ConnectIdentityShareAccountDetails.


        :param repayment_frequency_code: The repayment_frequency_code of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :type: str
        """

        self._repayment_frequency_code = repayment_frequency_code

    @property
    def repayment_frequency(self):
        """Gets the repayment_frequency of this ConnectIdentityShareAccountDetails.  # noqa: E501


        :return: The repayment_frequency of this ConnectIdentityShareAccountDetails.  # noqa: E501
        :rtype: str
        """
        return self._repayment_frequency

    @repayment_frequency.setter
    def repayment_frequency(self, repayment_frequency):
        """Sets the repayment_frequency of this ConnectIdentityShareAccountDetails.


        :param repayment_frequency: The repayment_frequency of this ConnectIdentityShareAccountDetails.  # noqa: E501
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
        if issubclass(ConnectIdentityShareAccountDetails, dict):
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
        if not isinstance(other, ConnectIdentityShareAccountDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

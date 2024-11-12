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

class ConnectCcdsFullHistory(object):
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
        'business_type_indicator': 'str',
        'business_name': 'str',
        'business_address': 'ConnectBankMatchBusinessAddress',
        'additional_trading_style': 'str',
        'business_telephone_number': 'str',
        'company_registration_number': 'str',
        'vat_number': 'str',
        'special_instruction_indicator': 'str',
        'start_date_of_agreement': 'datetime',
        'current_balance': 'int',
        'current_balance_credit_indicator': 'str',
        'actual_current_balance': 'int',
        'facility_status': 'str',
        'original_default_balance': 'int',
        'credit_or_overdraft_limit': 'int',
        'flag_settings': 'str',
        'transferred_to_consolidated_debt_account': 'str',
        'repayment_period': 'int',
        'payment_amount': 'int',
        'payment_frequency_indicator': 'str',
        'number_of_cash_advances': 'int',
        'value_of_cash_advances': 'int',
        'minimum_balance': 'int',
        'minimum_balance_credit_indicator': 'str',
        'actual_minimum_balance': 'int',
        'maximum_balance': 'int',
        'maximum_balance_credit_indicator': 'str',
        'actual_maximum_balance': 'int',
        'average_balance': 'int',
        'average_balance_credit_indicator': 'str',
        'actual_average_balance': 'int',
        'credit_turnover': 'int',
        'credit_turnover_net_or_gross_indicator': 'str',
        'debit_turnover': 'int',
        'debit_turnover_net_or_gross_indicator': 'str',
        'rejected_payments': 'int',
        'maximum_duration_of_excess': 'int',
        'changedfacilitynumber': 'str',
        'bankaccountiban': 'str',
        'current_account_reporting_level_indicator': 'str',
        'source_code': 'int',
        'facilitynumber': 'str',
        'facilityid': 'str',
        'identifier': 'str',
        'providertype': 'str',
        'bankcode': 'str',
        'facility_type': 'str',
        'facility_type_category': 'str',
        'isvalid': 'bool',
        'bank': 'str',
        'portfolio': 'str',
        '_date': 'str'
    }

    attribute_map = {
        'business_type_indicator': 'businessTypeIndicator',
        'business_name': 'businessName',
        'business_address': 'businessAddress',
        'additional_trading_style': 'additionalTradingStyle',
        'business_telephone_number': 'businessTelephoneNumber',
        'company_registration_number': 'companyRegistrationNumber',
        'vat_number': 'vatNumber',
        'special_instruction_indicator': 'specialInstructionIndicator',
        'start_date_of_agreement': 'startDateOfAgreement',
        'current_balance': 'currentBalance',
        'current_balance_credit_indicator': 'currentBalanceCreditIndicator',
        'actual_current_balance': 'actualCurrentBalance',
        'facility_status': 'facilityStatus',
        'original_default_balance': 'originalDefaultBalance',
        'credit_or_overdraft_limit': 'creditOrOverdraftLimit',
        'flag_settings': 'flagSettings',
        'transferred_to_consolidated_debt_account': 'transferredToConsolidatedDebtAccount',
        'repayment_period': 'repaymentPeriod',
        'payment_amount': 'paymentAmount',
        'payment_frequency_indicator': 'paymentFrequencyIndicator',
        'number_of_cash_advances': 'numberOfCashAdvances',
        'value_of_cash_advances': 'valueOfCashAdvances',
        'minimum_balance': 'minimumBalance',
        'minimum_balance_credit_indicator': 'minimumBalanceCreditIndicator',
        'actual_minimum_balance': 'actualMinimumBalance',
        'maximum_balance': 'maximumBalance',
        'maximum_balance_credit_indicator': 'maximumBalanceCreditIndicator',
        'actual_maximum_balance': 'actualMaximumBalance',
        'average_balance': 'averageBalance',
        'average_balance_credit_indicator': 'averageBalanceCreditIndicator',
        'actual_average_balance': 'actualAverageBalance',
        'credit_turnover': 'creditTurnover',
        'credit_turnover_net_or_gross_indicator': 'creditTurnoverNetOrGrossIndicator',
        'debit_turnover': 'debitTurnover',
        'debit_turnover_net_or_gross_indicator': 'debitTurnoverNetOrGrossIndicator',
        'rejected_payments': 'rejectedPayments',
        'maximum_duration_of_excess': 'maximumDurationOfExcess',
        'changedfacilitynumber': 'changedfacilitynumber',
        'bankaccountiban': 'bankaccountiban',
        'current_account_reporting_level_indicator': 'currentAccountReportingLevelIndicator',
        'source_code': 'sourceCode',
        'facilitynumber': 'facilitynumber',
        'facilityid': 'facilityid',
        'identifier': 'identifier',
        'providertype': 'providertype',
        'bankcode': 'bankcode',
        'facility_type': 'facilityType',
        'facility_type_category': 'facilityTypeCategory',
        'isvalid': 'isvalid',
        'bank': 'bank',
        'portfolio': 'portfolio',
        '_date': 'date'
    }

    def __init__(self, business_type_indicator=None, business_name=None, business_address=None, additional_trading_style=None, business_telephone_number=None, company_registration_number=None, vat_number=None, special_instruction_indicator=None, start_date_of_agreement=None, current_balance=None, current_balance_credit_indicator=None, actual_current_balance=None, facility_status=None, original_default_balance=None, credit_or_overdraft_limit=None, flag_settings=None, transferred_to_consolidated_debt_account=None, repayment_period=None, payment_amount=None, payment_frequency_indicator=None, number_of_cash_advances=None, value_of_cash_advances=None, minimum_balance=None, minimum_balance_credit_indicator=None, actual_minimum_balance=None, maximum_balance=None, maximum_balance_credit_indicator=None, actual_maximum_balance=None, average_balance=None, average_balance_credit_indicator=None, actual_average_balance=None, credit_turnover=None, credit_turnover_net_or_gross_indicator=None, debit_turnover=None, debit_turnover_net_or_gross_indicator=None, rejected_payments=None, maximum_duration_of_excess=None, changedfacilitynumber=None, bankaccountiban=None, current_account_reporting_level_indicator=None, source_code=None, facilitynumber=None, facilityid=None, identifier=None, providertype=None, bankcode=None, facility_type=None, facility_type_category=None, isvalid=None, bank=None, portfolio=None, _date=None):  # noqa: E501
        """ConnectCcdsFullHistory - a model defined in Swagger"""  # noqa: E501
        self._business_type_indicator = None
        self._business_name = None
        self._business_address = None
        self._additional_trading_style = None
        self._business_telephone_number = None
        self._company_registration_number = None
        self._vat_number = None
        self._special_instruction_indicator = None
        self._start_date_of_agreement = None
        self._current_balance = None
        self._current_balance_credit_indicator = None
        self._actual_current_balance = None
        self._facility_status = None
        self._original_default_balance = None
        self._credit_or_overdraft_limit = None
        self._flag_settings = None
        self._transferred_to_consolidated_debt_account = None
        self._repayment_period = None
        self._payment_amount = None
        self._payment_frequency_indicator = None
        self._number_of_cash_advances = None
        self._value_of_cash_advances = None
        self._minimum_balance = None
        self._minimum_balance_credit_indicator = None
        self._actual_minimum_balance = None
        self._maximum_balance = None
        self._maximum_balance_credit_indicator = None
        self._actual_maximum_balance = None
        self._average_balance = None
        self._average_balance_credit_indicator = None
        self._actual_average_balance = None
        self._credit_turnover = None
        self._credit_turnover_net_or_gross_indicator = None
        self._debit_turnover = None
        self._debit_turnover_net_or_gross_indicator = None
        self._rejected_payments = None
        self._maximum_duration_of_excess = None
        self._changedfacilitynumber = None
        self._bankaccountiban = None
        self._current_account_reporting_level_indicator = None
        self._source_code = None
        self._facilitynumber = None
        self._facilityid = None
        self._identifier = None
        self._providertype = None
        self._bankcode = None
        self._facility_type = None
        self._facility_type_category = None
        self._isvalid = None
        self._bank = None
        self._portfolio = None
        self.__date = None
        self.discriminator = None
        if business_type_indicator is not None:
            self.business_type_indicator = business_type_indicator
        if business_name is not None:
            self.business_name = business_name
        if business_address is not None:
            self.business_address = business_address
        if additional_trading_style is not None:
            self.additional_trading_style = additional_trading_style
        if business_telephone_number is not None:
            self.business_telephone_number = business_telephone_number
        if company_registration_number is not None:
            self.company_registration_number = company_registration_number
        if vat_number is not None:
            self.vat_number = vat_number
        if special_instruction_indicator is not None:
            self.special_instruction_indicator = special_instruction_indicator
        if start_date_of_agreement is not None:
            self.start_date_of_agreement = start_date_of_agreement
        if current_balance is not None:
            self.current_balance = current_balance
        if current_balance_credit_indicator is not None:
            self.current_balance_credit_indicator = current_balance_credit_indicator
        if actual_current_balance is not None:
            self.actual_current_balance = actual_current_balance
        if facility_status is not None:
            self.facility_status = facility_status
        if original_default_balance is not None:
            self.original_default_balance = original_default_balance
        if credit_or_overdraft_limit is not None:
            self.credit_or_overdraft_limit = credit_or_overdraft_limit
        if flag_settings is not None:
            self.flag_settings = flag_settings
        if transferred_to_consolidated_debt_account is not None:
            self.transferred_to_consolidated_debt_account = transferred_to_consolidated_debt_account
        if repayment_period is not None:
            self.repayment_period = repayment_period
        if payment_amount is not None:
            self.payment_amount = payment_amount
        if payment_frequency_indicator is not None:
            self.payment_frequency_indicator = payment_frequency_indicator
        if number_of_cash_advances is not None:
            self.number_of_cash_advances = number_of_cash_advances
        if value_of_cash_advances is not None:
            self.value_of_cash_advances = value_of_cash_advances
        if minimum_balance is not None:
            self.minimum_balance = minimum_balance
        if minimum_balance_credit_indicator is not None:
            self.minimum_balance_credit_indicator = minimum_balance_credit_indicator
        if actual_minimum_balance is not None:
            self.actual_minimum_balance = actual_minimum_balance
        if maximum_balance is not None:
            self.maximum_balance = maximum_balance
        if maximum_balance_credit_indicator is not None:
            self.maximum_balance_credit_indicator = maximum_balance_credit_indicator
        if actual_maximum_balance is not None:
            self.actual_maximum_balance = actual_maximum_balance
        if average_balance is not None:
            self.average_balance = average_balance
        if average_balance_credit_indicator is not None:
            self.average_balance_credit_indicator = average_balance_credit_indicator
        if actual_average_balance is not None:
            self.actual_average_balance = actual_average_balance
        if credit_turnover is not None:
            self.credit_turnover = credit_turnover
        if credit_turnover_net_or_gross_indicator is not None:
            self.credit_turnover_net_or_gross_indicator = credit_turnover_net_or_gross_indicator
        if debit_turnover is not None:
            self.debit_turnover = debit_turnover
        if debit_turnover_net_or_gross_indicator is not None:
            self.debit_turnover_net_or_gross_indicator = debit_turnover_net_or_gross_indicator
        if rejected_payments is not None:
            self.rejected_payments = rejected_payments
        if maximum_duration_of_excess is not None:
            self.maximum_duration_of_excess = maximum_duration_of_excess
        if changedfacilitynumber is not None:
            self.changedfacilitynumber = changedfacilitynumber
        if bankaccountiban is not None:
            self.bankaccountiban = bankaccountiban
        if current_account_reporting_level_indicator is not None:
            self.current_account_reporting_level_indicator = current_account_reporting_level_indicator
        if source_code is not None:
            self.source_code = source_code
        if facilitynumber is not None:
            self.facilitynumber = facilitynumber
        if facilityid is not None:
            self.facilityid = facilityid
        if identifier is not None:
            self.identifier = identifier
        if providertype is not None:
            self.providertype = providertype
        if bankcode is not None:
            self.bankcode = bankcode
        if facility_type is not None:
            self.facility_type = facility_type
        if facility_type_category is not None:
            self.facility_type_category = facility_type_category
        if isvalid is not None:
            self.isvalid = isvalid
        if bank is not None:
            self.bank = bank
        if portfolio is not None:
            self.portfolio = portfolio
        if _date is not None:
            self._date = _date

    @property
    def business_type_indicator(self):
        """Gets the business_type_indicator of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The business_type_indicator of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._business_type_indicator

    @business_type_indicator.setter
    def business_type_indicator(self, business_type_indicator):
        """Sets the business_type_indicator of this ConnectCcdsFullHistory.


        :param business_type_indicator: The business_type_indicator of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._business_type_indicator = business_type_indicator

    @property
    def business_name(self):
        """Gets the business_name of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The business_name of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        """Sets the business_name of this ConnectCcdsFullHistory.


        :param business_name: The business_name of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._business_name = business_name

    @property
    def business_address(self):
        """Gets the business_address of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The business_address of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: ConnectBankMatchBusinessAddress
        """
        return self._business_address

    @business_address.setter
    def business_address(self, business_address):
        """Sets the business_address of this ConnectCcdsFullHistory.


        :param business_address: The business_address of this ConnectCcdsFullHistory.  # noqa: E501
        :type: ConnectBankMatchBusinessAddress
        """

        self._business_address = business_address

    @property
    def additional_trading_style(self):
        """Gets the additional_trading_style of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The additional_trading_style of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._additional_trading_style

    @additional_trading_style.setter
    def additional_trading_style(self, additional_trading_style):
        """Sets the additional_trading_style of this ConnectCcdsFullHistory.


        :param additional_trading_style: The additional_trading_style of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._additional_trading_style = additional_trading_style

    @property
    def business_telephone_number(self):
        """Gets the business_telephone_number of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The business_telephone_number of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._business_telephone_number

    @business_telephone_number.setter
    def business_telephone_number(self, business_telephone_number):
        """Sets the business_telephone_number of this ConnectCcdsFullHistory.


        :param business_telephone_number: The business_telephone_number of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._business_telephone_number = business_telephone_number

    @property
    def company_registration_number(self):
        """Gets the company_registration_number of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The company_registration_number of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._company_registration_number

    @company_registration_number.setter
    def company_registration_number(self, company_registration_number):
        """Sets the company_registration_number of this ConnectCcdsFullHistory.


        :param company_registration_number: The company_registration_number of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._company_registration_number = company_registration_number

    @property
    def vat_number(self):
        """Gets the vat_number of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The vat_number of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._vat_number

    @vat_number.setter
    def vat_number(self, vat_number):
        """Sets the vat_number of this ConnectCcdsFullHistory.


        :param vat_number: The vat_number of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._vat_number = vat_number

    @property
    def special_instruction_indicator(self):
        """Gets the special_instruction_indicator of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The special_instruction_indicator of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._special_instruction_indicator

    @special_instruction_indicator.setter
    def special_instruction_indicator(self, special_instruction_indicator):
        """Sets the special_instruction_indicator of this ConnectCcdsFullHistory.


        :param special_instruction_indicator: The special_instruction_indicator of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._special_instruction_indicator = special_instruction_indicator

    @property
    def start_date_of_agreement(self):
        """Gets the start_date_of_agreement of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The start_date_of_agreement of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date_of_agreement

    @start_date_of_agreement.setter
    def start_date_of_agreement(self, start_date_of_agreement):
        """Sets the start_date_of_agreement of this ConnectCcdsFullHistory.


        :param start_date_of_agreement: The start_date_of_agreement of this ConnectCcdsFullHistory.  # noqa: E501
        :type: datetime
        """

        self._start_date_of_agreement = start_date_of_agreement

    @property
    def current_balance(self):
        """Gets the current_balance of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The current_balance of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: int
        """
        return self._current_balance

    @current_balance.setter
    def current_balance(self, current_balance):
        """Sets the current_balance of this ConnectCcdsFullHistory.


        :param current_balance: The current_balance of this ConnectCcdsFullHistory.  # noqa: E501
        :type: int
        """

        self._current_balance = current_balance

    @property
    def current_balance_credit_indicator(self):
        """Gets the current_balance_credit_indicator of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The current_balance_credit_indicator of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._current_balance_credit_indicator

    @current_balance_credit_indicator.setter
    def current_balance_credit_indicator(self, current_balance_credit_indicator):
        """Sets the current_balance_credit_indicator of this ConnectCcdsFullHistory.


        :param current_balance_credit_indicator: The current_balance_credit_indicator of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._current_balance_credit_indicator = current_balance_credit_indicator

    @property
    def actual_current_balance(self):
        """Gets the actual_current_balance of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The actual_current_balance of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: int
        """
        return self._actual_current_balance

    @actual_current_balance.setter
    def actual_current_balance(self, actual_current_balance):
        """Sets the actual_current_balance of this ConnectCcdsFullHistory.


        :param actual_current_balance: The actual_current_balance of this ConnectCcdsFullHistory.  # noqa: E501
        :type: int
        """

        self._actual_current_balance = actual_current_balance

    @property
    def facility_status(self):
        """Gets the facility_status of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The facility_status of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._facility_status

    @facility_status.setter
    def facility_status(self, facility_status):
        """Sets the facility_status of this ConnectCcdsFullHistory.


        :param facility_status: The facility_status of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._facility_status = facility_status

    @property
    def original_default_balance(self):
        """Gets the original_default_balance of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The original_default_balance of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: int
        """
        return self._original_default_balance

    @original_default_balance.setter
    def original_default_balance(self, original_default_balance):
        """Sets the original_default_balance of this ConnectCcdsFullHistory.


        :param original_default_balance: The original_default_balance of this ConnectCcdsFullHistory.  # noqa: E501
        :type: int
        """

        self._original_default_balance = original_default_balance

    @property
    def credit_or_overdraft_limit(self):
        """Gets the credit_or_overdraft_limit of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The credit_or_overdraft_limit of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: int
        """
        return self._credit_or_overdraft_limit

    @credit_or_overdraft_limit.setter
    def credit_or_overdraft_limit(self, credit_or_overdraft_limit):
        """Sets the credit_or_overdraft_limit of this ConnectCcdsFullHistory.


        :param credit_or_overdraft_limit: The credit_or_overdraft_limit of this ConnectCcdsFullHistory.  # noqa: E501
        :type: int
        """

        self._credit_or_overdraft_limit = credit_or_overdraft_limit

    @property
    def flag_settings(self):
        """Gets the flag_settings of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The flag_settings of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._flag_settings

    @flag_settings.setter
    def flag_settings(self, flag_settings):
        """Sets the flag_settings of this ConnectCcdsFullHistory.


        :param flag_settings: The flag_settings of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._flag_settings = flag_settings

    @property
    def transferred_to_consolidated_debt_account(self):
        """Gets the transferred_to_consolidated_debt_account of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The transferred_to_consolidated_debt_account of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._transferred_to_consolidated_debt_account

    @transferred_to_consolidated_debt_account.setter
    def transferred_to_consolidated_debt_account(self, transferred_to_consolidated_debt_account):
        """Sets the transferred_to_consolidated_debt_account of this ConnectCcdsFullHistory.


        :param transferred_to_consolidated_debt_account: The transferred_to_consolidated_debt_account of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._transferred_to_consolidated_debt_account = transferred_to_consolidated_debt_account

    @property
    def repayment_period(self):
        """Gets the repayment_period of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The repayment_period of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: int
        """
        return self._repayment_period

    @repayment_period.setter
    def repayment_period(self, repayment_period):
        """Sets the repayment_period of this ConnectCcdsFullHistory.


        :param repayment_period: The repayment_period of this ConnectCcdsFullHistory.  # noqa: E501
        :type: int
        """

        self._repayment_period = repayment_period

    @property
    def payment_amount(self):
        """Gets the payment_amount of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The payment_amount of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: int
        """
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, payment_amount):
        """Sets the payment_amount of this ConnectCcdsFullHistory.


        :param payment_amount: The payment_amount of this ConnectCcdsFullHistory.  # noqa: E501
        :type: int
        """

        self._payment_amount = payment_amount

    @property
    def payment_frequency_indicator(self):
        """Gets the payment_frequency_indicator of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The payment_frequency_indicator of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._payment_frequency_indicator

    @payment_frequency_indicator.setter
    def payment_frequency_indicator(self, payment_frequency_indicator):
        """Sets the payment_frequency_indicator of this ConnectCcdsFullHistory.


        :param payment_frequency_indicator: The payment_frequency_indicator of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._payment_frequency_indicator = payment_frequency_indicator

    @property
    def number_of_cash_advances(self):
        """Gets the number_of_cash_advances of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The number_of_cash_advances of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: int
        """
        return self._number_of_cash_advances

    @number_of_cash_advances.setter
    def number_of_cash_advances(self, number_of_cash_advances):
        """Sets the number_of_cash_advances of this ConnectCcdsFullHistory.


        :param number_of_cash_advances: The number_of_cash_advances of this ConnectCcdsFullHistory.  # noqa: E501
        :type: int
        """

        self._number_of_cash_advances = number_of_cash_advances

    @property
    def value_of_cash_advances(self):
        """Gets the value_of_cash_advances of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The value_of_cash_advances of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: int
        """
        return self._value_of_cash_advances

    @value_of_cash_advances.setter
    def value_of_cash_advances(self, value_of_cash_advances):
        """Sets the value_of_cash_advances of this ConnectCcdsFullHistory.


        :param value_of_cash_advances: The value_of_cash_advances of this ConnectCcdsFullHistory.  # noqa: E501
        :type: int
        """

        self._value_of_cash_advances = value_of_cash_advances

    @property
    def minimum_balance(self):
        """Gets the minimum_balance of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The minimum_balance of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: int
        """
        return self._minimum_balance

    @minimum_balance.setter
    def minimum_balance(self, minimum_balance):
        """Sets the minimum_balance of this ConnectCcdsFullHistory.


        :param minimum_balance: The minimum_balance of this ConnectCcdsFullHistory.  # noqa: E501
        :type: int
        """

        self._minimum_balance = minimum_balance

    @property
    def minimum_balance_credit_indicator(self):
        """Gets the minimum_balance_credit_indicator of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The minimum_balance_credit_indicator of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._minimum_balance_credit_indicator

    @minimum_balance_credit_indicator.setter
    def minimum_balance_credit_indicator(self, minimum_balance_credit_indicator):
        """Sets the minimum_balance_credit_indicator of this ConnectCcdsFullHistory.


        :param minimum_balance_credit_indicator: The minimum_balance_credit_indicator of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._minimum_balance_credit_indicator = minimum_balance_credit_indicator

    @property
    def actual_minimum_balance(self):
        """Gets the actual_minimum_balance of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The actual_minimum_balance of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: int
        """
        return self._actual_minimum_balance

    @actual_minimum_balance.setter
    def actual_minimum_balance(self, actual_minimum_balance):
        """Sets the actual_minimum_balance of this ConnectCcdsFullHistory.


        :param actual_minimum_balance: The actual_minimum_balance of this ConnectCcdsFullHistory.  # noqa: E501
        :type: int
        """

        self._actual_minimum_balance = actual_minimum_balance

    @property
    def maximum_balance(self):
        """Gets the maximum_balance of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The maximum_balance of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: int
        """
        return self._maximum_balance

    @maximum_balance.setter
    def maximum_balance(self, maximum_balance):
        """Sets the maximum_balance of this ConnectCcdsFullHistory.


        :param maximum_balance: The maximum_balance of this ConnectCcdsFullHistory.  # noqa: E501
        :type: int
        """

        self._maximum_balance = maximum_balance

    @property
    def maximum_balance_credit_indicator(self):
        """Gets the maximum_balance_credit_indicator of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The maximum_balance_credit_indicator of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._maximum_balance_credit_indicator

    @maximum_balance_credit_indicator.setter
    def maximum_balance_credit_indicator(self, maximum_balance_credit_indicator):
        """Sets the maximum_balance_credit_indicator of this ConnectCcdsFullHistory.


        :param maximum_balance_credit_indicator: The maximum_balance_credit_indicator of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._maximum_balance_credit_indicator = maximum_balance_credit_indicator

    @property
    def actual_maximum_balance(self):
        """Gets the actual_maximum_balance of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The actual_maximum_balance of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: int
        """
        return self._actual_maximum_balance

    @actual_maximum_balance.setter
    def actual_maximum_balance(self, actual_maximum_balance):
        """Sets the actual_maximum_balance of this ConnectCcdsFullHistory.


        :param actual_maximum_balance: The actual_maximum_balance of this ConnectCcdsFullHistory.  # noqa: E501
        :type: int
        """

        self._actual_maximum_balance = actual_maximum_balance

    @property
    def average_balance(self):
        """Gets the average_balance of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The average_balance of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: int
        """
        return self._average_balance

    @average_balance.setter
    def average_balance(self, average_balance):
        """Sets the average_balance of this ConnectCcdsFullHistory.


        :param average_balance: The average_balance of this ConnectCcdsFullHistory.  # noqa: E501
        :type: int
        """

        self._average_balance = average_balance

    @property
    def average_balance_credit_indicator(self):
        """Gets the average_balance_credit_indicator of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The average_balance_credit_indicator of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._average_balance_credit_indicator

    @average_balance_credit_indicator.setter
    def average_balance_credit_indicator(self, average_balance_credit_indicator):
        """Sets the average_balance_credit_indicator of this ConnectCcdsFullHistory.


        :param average_balance_credit_indicator: The average_balance_credit_indicator of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._average_balance_credit_indicator = average_balance_credit_indicator

    @property
    def actual_average_balance(self):
        """Gets the actual_average_balance of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The actual_average_balance of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: int
        """
        return self._actual_average_balance

    @actual_average_balance.setter
    def actual_average_balance(self, actual_average_balance):
        """Sets the actual_average_balance of this ConnectCcdsFullHistory.


        :param actual_average_balance: The actual_average_balance of this ConnectCcdsFullHistory.  # noqa: E501
        :type: int
        """

        self._actual_average_balance = actual_average_balance

    @property
    def credit_turnover(self):
        """Gets the credit_turnover of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The credit_turnover of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: int
        """
        return self._credit_turnover

    @credit_turnover.setter
    def credit_turnover(self, credit_turnover):
        """Sets the credit_turnover of this ConnectCcdsFullHistory.


        :param credit_turnover: The credit_turnover of this ConnectCcdsFullHistory.  # noqa: E501
        :type: int
        """

        self._credit_turnover = credit_turnover

    @property
    def credit_turnover_net_or_gross_indicator(self):
        """Gets the credit_turnover_net_or_gross_indicator of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The credit_turnover_net_or_gross_indicator of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._credit_turnover_net_or_gross_indicator

    @credit_turnover_net_or_gross_indicator.setter
    def credit_turnover_net_or_gross_indicator(self, credit_turnover_net_or_gross_indicator):
        """Sets the credit_turnover_net_or_gross_indicator of this ConnectCcdsFullHistory.


        :param credit_turnover_net_or_gross_indicator: The credit_turnover_net_or_gross_indicator of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._credit_turnover_net_or_gross_indicator = credit_turnover_net_or_gross_indicator

    @property
    def debit_turnover(self):
        """Gets the debit_turnover of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The debit_turnover of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: int
        """
        return self._debit_turnover

    @debit_turnover.setter
    def debit_turnover(self, debit_turnover):
        """Sets the debit_turnover of this ConnectCcdsFullHistory.


        :param debit_turnover: The debit_turnover of this ConnectCcdsFullHistory.  # noqa: E501
        :type: int
        """

        self._debit_turnover = debit_turnover

    @property
    def debit_turnover_net_or_gross_indicator(self):
        """Gets the debit_turnover_net_or_gross_indicator of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The debit_turnover_net_or_gross_indicator of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._debit_turnover_net_or_gross_indicator

    @debit_turnover_net_or_gross_indicator.setter
    def debit_turnover_net_or_gross_indicator(self, debit_turnover_net_or_gross_indicator):
        """Sets the debit_turnover_net_or_gross_indicator of this ConnectCcdsFullHistory.


        :param debit_turnover_net_or_gross_indicator: The debit_turnover_net_or_gross_indicator of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._debit_turnover_net_or_gross_indicator = debit_turnover_net_or_gross_indicator

    @property
    def rejected_payments(self):
        """Gets the rejected_payments of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The rejected_payments of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: int
        """
        return self._rejected_payments

    @rejected_payments.setter
    def rejected_payments(self, rejected_payments):
        """Sets the rejected_payments of this ConnectCcdsFullHistory.


        :param rejected_payments: The rejected_payments of this ConnectCcdsFullHistory.  # noqa: E501
        :type: int
        """

        self._rejected_payments = rejected_payments

    @property
    def maximum_duration_of_excess(self):
        """Gets the maximum_duration_of_excess of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The maximum_duration_of_excess of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: int
        """
        return self._maximum_duration_of_excess

    @maximum_duration_of_excess.setter
    def maximum_duration_of_excess(self, maximum_duration_of_excess):
        """Sets the maximum_duration_of_excess of this ConnectCcdsFullHistory.


        :param maximum_duration_of_excess: The maximum_duration_of_excess of this ConnectCcdsFullHistory.  # noqa: E501
        :type: int
        """

        self._maximum_duration_of_excess = maximum_duration_of_excess

    @property
    def changedfacilitynumber(self):
        """Gets the changedfacilitynumber of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The changedfacilitynumber of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._changedfacilitynumber

    @changedfacilitynumber.setter
    def changedfacilitynumber(self, changedfacilitynumber):
        """Sets the changedfacilitynumber of this ConnectCcdsFullHistory.


        :param changedfacilitynumber: The changedfacilitynumber of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._changedfacilitynumber = changedfacilitynumber

    @property
    def bankaccountiban(self):
        """Gets the bankaccountiban of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The bankaccountiban of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._bankaccountiban

    @bankaccountiban.setter
    def bankaccountiban(self, bankaccountiban):
        """Sets the bankaccountiban of this ConnectCcdsFullHistory.


        :param bankaccountiban: The bankaccountiban of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._bankaccountiban = bankaccountiban

    @property
    def current_account_reporting_level_indicator(self):
        """Gets the current_account_reporting_level_indicator of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The current_account_reporting_level_indicator of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._current_account_reporting_level_indicator

    @current_account_reporting_level_indicator.setter
    def current_account_reporting_level_indicator(self, current_account_reporting_level_indicator):
        """Sets the current_account_reporting_level_indicator of this ConnectCcdsFullHistory.


        :param current_account_reporting_level_indicator: The current_account_reporting_level_indicator of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._current_account_reporting_level_indicator = current_account_reporting_level_indicator

    @property
    def source_code(self):
        """Gets the source_code of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The source_code of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: int
        """
        return self._source_code

    @source_code.setter
    def source_code(self, source_code):
        """Sets the source_code of this ConnectCcdsFullHistory.


        :param source_code: The source_code of this ConnectCcdsFullHistory.  # noqa: E501
        :type: int
        """

        self._source_code = source_code

    @property
    def facilitynumber(self):
        """Gets the facilitynumber of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The facilitynumber of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._facilitynumber

    @facilitynumber.setter
    def facilitynumber(self, facilitynumber):
        """Sets the facilitynumber of this ConnectCcdsFullHistory.


        :param facilitynumber: The facilitynumber of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._facilitynumber = facilitynumber

    @property
    def facilityid(self):
        """Gets the facilityid of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The facilityid of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._facilityid

    @facilityid.setter
    def facilityid(self, facilityid):
        """Sets the facilityid of this ConnectCcdsFullHistory.


        :param facilityid: The facilityid of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._facilityid = facilityid

    @property
    def identifier(self):
        """Gets the identifier of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The identifier of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ConnectCcdsFullHistory.


        :param identifier: The identifier of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def providertype(self):
        """Gets the providertype of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The providertype of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._providertype

    @providertype.setter
    def providertype(self, providertype):
        """Sets the providertype of this ConnectCcdsFullHistory.


        :param providertype: The providertype of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._providertype = providertype

    @property
    def bankcode(self):
        """Gets the bankcode of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The bankcode of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._bankcode

    @bankcode.setter
    def bankcode(self, bankcode):
        """Sets the bankcode of this ConnectCcdsFullHistory.


        :param bankcode: The bankcode of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._bankcode = bankcode

    @property
    def facility_type(self):
        """Gets the facility_type of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The facility_type of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._facility_type

    @facility_type.setter
    def facility_type(self, facility_type):
        """Sets the facility_type of this ConnectCcdsFullHistory.


        :param facility_type: The facility_type of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._facility_type = facility_type

    @property
    def facility_type_category(self):
        """Gets the facility_type_category of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The facility_type_category of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._facility_type_category

    @facility_type_category.setter
    def facility_type_category(self, facility_type_category):
        """Sets the facility_type_category of this ConnectCcdsFullHistory.


        :param facility_type_category: The facility_type_category of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._facility_type_category = facility_type_category

    @property
    def isvalid(self):
        """Gets the isvalid of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The isvalid of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: bool
        """
        return self._isvalid

    @isvalid.setter
    def isvalid(self, isvalid):
        """Sets the isvalid of this ConnectCcdsFullHistory.


        :param isvalid: The isvalid of this ConnectCcdsFullHistory.  # noqa: E501
        :type: bool
        """

        self._isvalid = isvalid

    @property
    def bank(self):
        """Gets the bank of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The bank of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._bank

    @bank.setter
    def bank(self, bank):
        """Sets the bank of this ConnectCcdsFullHistory.


        :param bank: The bank of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._bank = bank

    @property
    def portfolio(self):
        """Gets the portfolio of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The portfolio of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self._portfolio

    @portfolio.setter
    def portfolio(self, portfolio):
        """Sets the portfolio of this ConnectCcdsFullHistory.


        :param portfolio: The portfolio of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self._portfolio = portfolio

    @property
    def _date(self):
        """Gets the _date of this ConnectCcdsFullHistory.  # noqa: E501


        :return: The _date of this ConnectCcdsFullHistory.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ConnectCcdsFullHistory.


        :param _date: The _date of this ConnectCcdsFullHistory.  # noqa: E501
        :type: str
        """

        self.__date = _date

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
        if issubclass(ConnectCcdsFullHistory, dict):
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
        if not isinstance(other, ConnectCcdsFullHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

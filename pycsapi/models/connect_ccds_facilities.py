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

class ConnectCcdsFacilities(object):
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
        'start_date_of_agreement': 'datetime',
        'current_balance': 'int',
        'actual_current_balance': 'int',
        'original_default_balance': 'int',
        'credit_or_overdraft_limit': 'int',
        'repayment_period': 'int',
        'payment_amount': 'int',
        'number_of_cash_advances': 'int',
        'value_of_cash_advances': 'int',
        'minimum_balance': 'int',
        'actual_minimum_balance': 'int',
        'maximum_balance': 'int',
        'actual_maximum_balance': 'int',
        'average_balance': 'int',
        'actual_average_balance': 'int',
        'credit_turnover': 'int',
        'debit_turnover': 'int',
        'rejected_payments': 'int',
        'maximum_duration_of_excess': 'int'
    }

    attribute_map = {
        'start_date_of_agreement': 'startDateOfAgreement',
        'current_balance': 'currentBalance',
        'actual_current_balance': 'actualCurrentBalance',
        'original_default_balance': 'originalDefaultBalance',
        'credit_or_overdraft_limit': 'creditOrOverdraftLimit',
        'repayment_period': 'repaymentPeriod',
        'payment_amount': 'paymentAmount',
        'number_of_cash_advances': 'numberOfCashAdvances',
        'value_of_cash_advances': 'valueOfCashAdvances',
        'minimum_balance': 'minimumBalance',
        'actual_minimum_balance': 'actualMinimumBalance',
        'maximum_balance': 'maximumBalance',
        'actual_maximum_balance': 'actualMaximumBalance',
        'average_balance': 'averageBalance',
        'actual_average_balance': 'actualAverageBalance',
        'credit_turnover': 'creditTurnover',
        'debit_turnover': 'debitTurnover',
        'rejected_payments': 'rejectedPayments',
        'maximum_duration_of_excess': 'maximumDurationOfExcess'
    }

    def __init__(self, start_date_of_agreement=None, current_balance=None, actual_current_balance=None, original_default_balance=None, credit_or_overdraft_limit=None, repayment_period=None, payment_amount=None, number_of_cash_advances=None, value_of_cash_advances=None, minimum_balance=None, actual_minimum_balance=None, maximum_balance=None, actual_maximum_balance=None, average_balance=None, actual_average_balance=None, credit_turnover=None, debit_turnover=None, rejected_payments=None, maximum_duration_of_excess=None):  # noqa: E501
        """ConnectCcdsFacilities - a model defined in Swagger"""  # noqa: E501
        self._start_date_of_agreement = None
        self._current_balance = None
        self._actual_current_balance = None
        self._original_default_balance = None
        self._credit_or_overdraft_limit = None
        self._repayment_period = None
        self._payment_amount = None
        self._number_of_cash_advances = None
        self._value_of_cash_advances = None
        self._minimum_balance = None
        self._actual_minimum_balance = None
        self._maximum_balance = None
        self._actual_maximum_balance = None
        self._average_balance = None
        self._actual_average_balance = None
        self._credit_turnover = None
        self._debit_turnover = None
        self._rejected_payments = None
        self._maximum_duration_of_excess = None
        self.discriminator = None
        if start_date_of_agreement is not None:
            self.start_date_of_agreement = start_date_of_agreement
        if current_balance is not None:
            self.current_balance = current_balance
        if actual_current_balance is not None:
            self.actual_current_balance = actual_current_balance
        if original_default_balance is not None:
            self.original_default_balance = original_default_balance
        if credit_or_overdraft_limit is not None:
            self.credit_or_overdraft_limit = credit_or_overdraft_limit
        if repayment_period is not None:
            self.repayment_period = repayment_period
        if payment_amount is not None:
            self.payment_amount = payment_amount
        if number_of_cash_advances is not None:
            self.number_of_cash_advances = number_of_cash_advances
        if value_of_cash_advances is not None:
            self.value_of_cash_advances = value_of_cash_advances
        if minimum_balance is not None:
            self.minimum_balance = minimum_balance
        if actual_minimum_balance is not None:
            self.actual_minimum_balance = actual_minimum_balance
        if maximum_balance is not None:
            self.maximum_balance = maximum_balance
        if actual_maximum_balance is not None:
            self.actual_maximum_balance = actual_maximum_balance
        if average_balance is not None:
            self.average_balance = average_balance
        if actual_average_balance is not None:
            self.actual_average_balance = actual_average_balance
        if credit_turnover is not None:
            self.credit_turnover = credit_turnover
        if debit_turnover is not None:
            self.debit_turnover = debit_turnover
        if rejected_payments is not None:
            self.rejected_payments = rejected_payments
        if maximum_duration_of_excess is not None:
            self.maximum_duration_of_excess = maximum_duration_of_excess

    @property
    def start_date_of_agreement(self):
        """Gets the start_date_of_agreement of this ConnectCcdsFacilities.  # noqa: E501


        :return: The start_date_of_agreement of this ConnectCcdsFacilities.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date_of_agreement

    @start_date_of_agreement.setter
    def start_date_of_agreement(self, start_date_of_agreement):
        """Sets the start_date_of_agreement of this ConnectCcdsFacilities.


        :param start_date_of_agreement: The start_date_of_agreement of this ConnectCcdsFacilities.  # noqa: E501
        :type: datetime
        """

        self._start_date_of_agreement = start_date_of_agreement

    @property
    def current_balance(self):
        """Gets the current_balance of this ConnectCcdsFacilities.  # noqa: E501


        :return: The current_balance of this ConnectCcdsFacilities.  # noqa: E501
        :rtype: int
        """
        return self._current_balance

    @current_balance.setter
    def current_balance(self, current_balance):
        """Sets the current_balance of this ConnectCcdsFacilities.


        :param current_balance: The current_balance of this ConnectCcdsFacilities.  # noqa: E501
        :type: int
        """

        self._current_balance = current_balance

    @property
    def actual_current_balance(self):
        """Gets the actual_current_balance of this ConnectCcdsFacilities.  # noqa: E501


        :return: The actual_current_balance of this ConnectCcdsFacilities.  # noqa: E501
        :rtype: int
        """
        return self._actual_current_balance

    @actual_current_balance.setter
    def actual_current_balance(self, actual_current_balance):
        """Sets the actual_current_balance of this ConnectCcdsFacilities.


        :param actual_current_balance: The actual_current_balance of this ConnectCcdsFacilities.  # noqa: E501
        :type: int
        """

        self._actual_current_balance = actual_current_balance

    @property
    def original_default_balance(self):
        """Gets the original_default_balance of this ConnectCcdsFacilities.  # noqa: E501


        :return: The original_default_balance of this ConnectCcdsFacilities.  # noqa: E501
        :rtype: int
        """
        return self._original_default_balance

    @original_default_balance.setter
    def original_default_balance(self, original_default_balance):
        """Sets the original_default_balance of this ConnectCcdsFacilities.


        :param original_default_balance: The original_default_balance of this ConnectCcdsFacilities.  # noqa: E501
        :type: int
        """

        self._original_default_balance = original_default_balance

    @property
    def credit_or_overdraft_limit(self):
        """Gets the credit_or_overdraft_limit of this ConnectCcdsFacilities.  # noqa: E501


        :return: The credit_or_overdraft_limit of this ConnectCcdsFacilities.  # noqa: E501
        :rtype: int
        """
        return self._credit_or_overdraft_limit

    @credit_or_overdraft_limit.setter
    def credit_or_overdraft_limit(self, credit_or_overdraft_limit):
        """Sets the credit_or_overdraft_limit of this ConnectCcdsFacilities.


        :param credit_or_overdraft_limit: The credit_or_overdraft_limit of this ConnectCcdsFacilities.  # noqa: E501
        :type: int
        """

        self._credit_or_overdraft_limit = credit_or_overdraft_limit

    @property
    def repayment_period(self):
        """Gets the repayment_period of this ConnectCcdsFacilities.  # noqa: E501


        :return: The repayment_period of this ConnectCcdsFacilities.  # noqa: E501
        :rtype: int
        """
        return self._repayment_period

    @repayment_period.setter
    def repayment_period(self, repayment_period):
        """Sets the repayment_period of this ConnectCcdsFacilities.


        :param repayment_period: The repayment_period of this ConnectCcdsFacilities.  # noqa: E501
        :type: int
        """

        self._repayment_period = repayment_period

    @property
    def payment_amount(self):
        """Gets the payment_amount of this ConnectCcdsFacilities.  # noqa: E501


        :return: The payment_amount of this ConnectCcdsFacilities.  # noqa: E501
        :rtype: int
        """
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, payment_amount):
        """Sets the payment_amount of this ConnectCcdsFacilities.


        :param payment_amount: The payment_amount of this ConnectCcdsFacilities.  # noqa: E501
        :type: int
        """

        self._payment_amount = payment_amount

    @property
    def number_of_cash_advances(self):
        """Gets the number_of_cash_advances of this ConnectCcdsFacilities.  # noqa: E501


        :return: The number_of_cash_advances of this ConnectCcdsFacilities.  # noqa: E501
        :rtype: int
        """
        return self._number_of_cash_advances

    @number_of_cash_advances.setter
    def number_of_cash_advances(self, number_of_cash_advances):
        """Sets the number_of_cash_advances of this ConnectCcdsFacilities.


        :param number_of_cash_advances: The number_of_cash_advances of this ConnectCcdsFacilities.  # noqa: E501
        :type: int
        """

        self._number_of_cash_advances = number_of_cash_advances

    @property
    def value_of_cash_advances(self):
        """Gets the value_of_cash_advances of this ConnectCcdsFacilities.  # noqa: E501


        :return: The value_of_cash_advances of this ConnectCcdsFacilities.  # noqa: E501
        :rtype: int
        """
        return self._value_of_cash_advances

    @value_of_cash_advances.setter
    def value_of_cash_advances(self, value_of_cash_advances):
        """Sets the value_of_cash_advances of this ConnectCcdsFacilities.


        :param value_of_cash_advances: The value_of_cash_advances of this ConnectCcdsFacilities.  # noqa: E501
        :type: int
        """

        self._value_of_cash_advances = value_of_cash_advances

    @property
    def minimum_balance(self):
        """Gets the minimum_balance of this ConnectCcdsFacilities.  # noqa: E501


        :return: The minimum_balance of this ConnectCcdsFacilities.  # noqa: E501
        :rtype: int
        """
        return self._minimum_balance

    @minimum_balance.setter
    def minimum_balance(self, minimum_balance):
        """Sets the minimum_balance of this ConnectCcdsFacilities.


        :param minimum_balance: The minimum_balance of this ConnectCcdsFacilities.  # noqa: E501
        :type: int
        """

        self._minimum_balance = minimum_balance

    @property
    def actual_minimum_balance(self):
        """Gets the actual_minimum_balance of this ConnectCcdsFacilities.  # noqa: E501


        :return: The actual_minimum_balance of this ConnectCcdsFacilities.  # noqa: E501
        :rtype: int
        """
        return self._actual_minimum_balance

    @actual_minimum_balance.setter
    def actual_minimum_balance(self, actual_minimum_balance):
        """Sets the actual_minimum_balance of this ConnectCcdsFacilities.


        :param actual_minimum_balance: The actual_minimum_balance of this ConnectCcdsFacilities.  # noqa: E501
        :type: int
        """

        self._actual_minimum_balance = actual_minimum_balance

    @property
    def maximum_balance(self):
        """Gets the maximum_balance of this ConnectCcdsFacilities.  # noqa: E501


        :return: The maximum_balance of this ConnectCcdsFacilities.  # noqa: E501
        :rtype: int
        """
        return self._maximum_balance

    @maximum_balance.setter
    def maximum_balance(self, maximum_balance):
        """Sets the maximum_balance of this ConnectCcdsFacilities.


        :param maximum_balance: The maximum_balance of this ConnectCcdsFacilities.  # noqa: E501
        :type: int
        """

        self._maximum_balance = maximum_balance

    @property
    def actual_maximum_balance(self):
        """Gets the actual_maximum_balance of this ConnectCcdsFacilities.  # noqa: E501


        :return: The actual_maximum_balance of this ConnectCcdsFacilities.  # noqa: E501
        :rtype: int
        """
        return self._actual_maximum_balance

    @actual_maximum_balance.setter
    def actual_maximum_balance(self, actual_maximum_balance):
        """Sets the actual_maximum_balance of this ConnectCcdsFacilities.


        :param actual_maximum_balance: The actual_maximum_balance of this ConnectCcdsFacilities.  # noqa: E501
        :type: int
        """

        self._actual_maximum_balance = actual_maximum_balance

    @property
    def average_balance(self):
        """Gets the average_balance of this ConnectCcdsFacilities.  # noqa: E501


        :return: The average_balance of this ConnectCcdsFacilities.  # noqa: E501
        :rtype: int
        """
        return self._average_balance

    @average_balance.setter
    def average_balance(self, average_balance):
        """Sets the average_balance of this ConnectCcdsFacilities.


        :param average_balance: The average_balance of this ConnectCcdsFacilities.  # noqa: E501
        :type: int
        """

        self._average_balance = average_balance

    @property
    def actual_average_balance(self):
        """Gets the actual_average_balance of this ConnectCcdsFacilities.  # noqa: E501


        :return: The actual_average_balance of this ConnectCcdsFacilities.  # noqa: E501
        :rtype: int
        """
        return self._actual_average_balance

    @actual_average_balance.setter
    def actual_average_balance(self, actual_average_balance):
        """Sets the actual_average_balance of this ConnectCcdsFacilities.


        :param actual_average_balance: The actual_average_balance of this ConnectCcdsFacilities.  # noqa: E501
        :type: int
        """

        self._actual_average_balance = actual_average_balance

    @property
    def credit_turnover(self):
        """Gets the credit_turnover of this ConnectCcdsFacilities.  # noqa: E501


        :return: The credit_turnover of this ConnectCcdsFacilities.  # noqa: E501
        :rtype: int
        """
        return self._credit_turnover

    @credit_turnover.setter
    def credit_turnover(self, credit_turnover):
        """Sets the credit_turnover of this ConnectCcdsFacilities.


        :param credit_turnover: The credit_turnover of this ConnectCcdsFacilities.  # noqa: E501
        :type: int
        """

        self._credit_turnover = credit_turnover

    @property
    def debit_turnover(self):
        """Gets the debit_turnover of this ConnectCcdsFacilities.  # noqa: E501


        :return: The debit_turnover of this ConnectCcdsFacilities.  # noqa: E501
        :rtype: int
        """
        return self._debit_turnover

    @debit_turnover.setter
    def debit_turnover(self, debit_turnover):
        """Sets the debit_turnover of this ConnectCcdsFacilities.


        :param debit_turnover: The debit_turnover of this ConnectCcdsFacilities.  # noqa: E501
        :type: int
        """

        self._debit_turnover = debit_turnover

    @property
    def rejected_payments(self):
        """Gets the rejected_payments of this ConnectCcdsFacilities.  # noqa: E501


        :return: The rejected_payments of this ConnectCcdsFacilities.  # noqa: E501
        :rtype: int
        """
        return self._rejected_payments

    @rejected_payments.setter
    def rejected_payments(self, rejected_payments):
        """Sets the rejected_payments of this ConnectCcdsFacilities.


        :param rejected_payments: The rejected_payments of this ConnectCcdsFacilities.  # noqa: E501
        :type: int
        """

        self._rejected_payments = rejected_payments

    @property
    def maximum_duration_of_excess(self):
        """Gets the maximum_duration_of_excess of this ConnectCcdsFacilities.  # noqa: E501


        :return: The maximum_duration_of_excess of this ConnectCcdsFacilities.  # noqa: E501
        :rtype: int
        """
        return self._maximum_duration_of_excess

    @maximum_duration_of_excess.setter
    def maximum_duration_of_excess(self, maximum_duration_of_excess):
        """Sets the maximum_duration_of_excess of this ConnectCcdsFacilities.


        :param maximum_duration_of_excess: The maximum_duration_of_excess of this ConnectCcdsFacilities.  # noqa: E501
        :type: int
        """

        self._maximum_duration_of_excess = maximum_duration_of_excess

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
        if issubclass(ConnectCcdsFacilities, dict):
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
        if not isinstance(other, ConnectCcdsFacilities):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

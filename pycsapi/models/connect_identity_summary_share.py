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

class ConnectIdentitySummaryShare(object):
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
        'account_count': 'int',
        'active_account_count': 'int',
        'settled_account_count': 'int',
        'accounts_opened_in_last6_months_count': 'int',
        'delinquent_accounts_in_last12_months_count': 'int',
        'worst_payment_status_in_last12_months_count': 'str',
        'worst_payment_status_in_last36_months_count': 'str',
        'defaults_in_last12_months_count': 'int',
        'defaults_in_last36_months_count': 'int'
    }

    attribute_map = {
        'account_count': 'accountCount',
        'active_account_count': 'activeAccountCount',
        'settled_account_count': 'settledAccountCount',
        'accounts_opened_in_last6_months_count': 'accountsOpenedInLast6MonthsCount',
        'delinquent_accounts_in_last12_months_count': 'delinquentAccountsInLast12MonthsCount',
        'worst_payment_status_in_last12_months_count': 'worstPaymentStatusInLast12MonthsCount',
        'worst_payment_status_in_last36_months_count': 'worstPaymentStatusInLast36MonthsCount',
        'defaults_in_last12_months_count': 'defaultsInLast12MonthsCount',
        'defaults_in_last36_months_count': 'defaultsInLast36MonthsCount'
    }

    def __init__(self, account_count=None, active_account_count=None, settled_account_count=None, accounts_opened_in_last6_months_count=None, delinquent_accounts_in_last12_months_count=None, worst_payment_status_in_last12_months_count=None, worst_payment_status_in_last36_months_count=None, defaults_in_last12_months_count=None, defaults_in_last36_months_count=None):  # noqa: E501
        """ConnectIdentitySummaryShare - a model defined in Swagger"""  # noqa: E501
        self._account_count = None
        self._active_account_count = None
        self._settled_account_count = None
        self._accounts_opened_in_last6_months_count = None
        self._delinquent_accounts_in_last12_months_count = None
        self._worst_payment_status_in_last12_months_count = None
        self._worst_payment_status_in_last36_months_count = None
        self._defaults_in_last12_months_count = None
        self._defaults_in_last36_months_count = None
        self.discriminator = None
        if account_count is not None:
            self.account_count = account_count
        if active_account_count is not None:
            self.active_account_count = active_account_count
        if settled_account_count is not None:
            self.settled_account_count = settled_account_count
        if accounts_opened_in_last6_months_count is not None:
            self.accounts_opened_in_last6_months_count = accounts_opened_in_last6_months_count
        if delinquent_accounts_in_last12_months_count is not None:
            self.delinquent_accounts_in_last12_months_count = delinquent_accounts_in_last12_months_count
        if worst_payment_status_in_last12_months_count is not None:
            self.worst_payment_status_in_last12_months_count = worst_payment_status_in_last12_months_count
        if worst_payment_status_in_last36_months_count is not None:
            self.worst_payment_status_in_last36_months_count = worst_payment_status_in_last36_months_count
        if defaults_in_last12_months_count is not None:
            self.defaults_in_last12_months_count = defaults_in_last12_months_count
        if defaults_in_last36_months_count is not None:
            self.defaults_in_last36_months_count = defaults_in_last36_months_count

    @property
    def account_count(self):
        """Gets the account_count of this ConnectIdentitySummaryShare.  # noqa: E501


        :return: The account_count of this ConnectIdentitySummaryShare.  # noqa: E501
        :rtype: int
        """
        return self._account_count

    @account_count.setter
    def account_count(self, account_count):
        """Sets the account_count of this ConnectIdentitySummaryShare.


        :param account_count: The account_count of this ConnectIdentitySummaryShare.  # noqa: E501
        :type: int
        """

        self._account_count = account_count

    @property
    def active_account_count(self):
        """Gets the active_account_count of this ConnectIdentitySummaryShare.  # noqa: E501


        :return: The active_account_count of this ConnectIdentitySummaryShare.  # noqa: E501
        :rtype: int
        """
        return self._active_account_count

    @active_account_count.setter
    def active_account_count(self, active_account_count):
        """Sets the active_account_count of this ConnectIdentitySummaryShare.


        :param active_account_count: The active_account_count of this ConnectIdentitySummaryShare.  # noqa: E501
        :type: int
        """

        self._active_account_count = active_account_count

    @property
    def settled_account_count(self):
        """Gets the settled_account_count of this ConnectIdentitySummaryShare.  # noqa: E501


        :return: The settled_account_count of this ConnectIdentitySummaryShare.  # noqa: E501
        :rtype: int
        """
        return self._settled_account_count

    @settled_account_count.setter
    def settled_account_count(self, settled_account_count):
        """Sets the settled_account_count of this ConnectIdentitySummaryShare.


        :param settled_account_count: The settled_account_count of this ConnectIdentitySummaryShare.  # noqa: E501
        :type: int
        """

        self._settled_account_count = settled_account_count

    @property
    def accounts_opened_in_last6_months_count(self):
        """Gets the accounts_opened_in_last6_months_count of this ConnectIdentitySummaryShare.  # noqa: E501


        :return: The accounts_opened_in_last6_months_count of this ConnectIdentitySummaryShare.  # noqa: E501
        :rtype: int
        """
        return self._accounts_opened_in_last6_months_count

    @accounts_opened_in_last6_months_count.setter
    def accounts_opened_in_last6_months_count(self, accounts_opened_in_last6_months_count):
        """Sets the accounts_opened_in_last6_months_count of this ConnectIdentitySummaryShare.


        :param accounts_opened_in_last6_months_count: The accounts_opened_in_last6_months_count of this ConnectIdentitySummaryShare.  # noqa: E501
        :type: int
        """

        self._accounts_opened_in_last6_months_count = accounts_opened_in_last6_months_count

    @property
    def delinquent_accounts_in_last12_months_count(self):
        """Gets the delinquent_accounts_in_last12_months_count of this ConnectIdentitySummaryShare.  # noqa: E501


        :return: The delinquent_accounts_in_last12_months_count of this ConnectIdentitySummaryShare.  # noqa: E501
        :rtype: int
        """
        return self._delinquent_accounts_in_last12_months_count

    @delinquent_accounts_in_last12_months_count.setter
    def delinquent_accounts_in_last12_months_count(self, delinquent_accounts_in_last12_months_count):
        """Sets the delinquent_accounts_in_last12_months_count of this ConnectIdentitySummaryShare.


        :param delinquent_accounts_in_last12_months_count: The delinquent_accounts_in_last12_months_count of this ConnectIdentitySummaryShare.  # noqa: E501
        :type: int
        """

        self._delinquent_accounts_in_last12_months_count = delinquent_accounts_in_last12_months_count

    @property
    def worst_payment_status_in_last12_months_count(self):
        """Gets the worst_payment_status_in_last12_months_count of this ConnectIdentitySummaryShare.  # noqa: E501


        :return: The worst_payment_status_in_last12_months_count of this ConnectIdentitySummaryShare.  # noqa: E501
        :rtype: str
        """
        return self._worst_payment_status_in_last12_months_count

    @worst_payment_status_in_last12_months_count.setter
    def worst_payment_status_in_last12_months_count(self, worst_payment_status_in_last12_months_count):
        """Sets the worst_payment_status_in_last12_months_count of this ConnectIdentitySummaryShare.


        :param worst_payment_status_in_last12_months_count: The worst_payment_status_in_last12_months_count of this ConnectIdentitySummaryShare.  # noqa: E501
        :type: str
        """

        self._worst_payment_status_in_last12_months_count = worst_payment_status_in_last12_months_count

    @property
    def worst_payment_status_in_last36_months_count(self):
        """Gets the worst_payment_status_in_last36_months_count of this ConnectIdentitySummaryShare.  # noqa: E501


        :return: The worst_payment_status_in_last36_months_count of this ConnectIdentitySummaryShare.  # noqa: E501
        :rtype: str
        """
        return self._worst_payment_status_in_last36_months_count

    @worst_payment_status_in_last36_months_count.setter
    def worst_payment_status_in_last36_months_count(self, worst_payment_status_in_last36_months_count):
        """Sets the worst_payment_status_in_last36_months_count of this ConnectIdentitySummaryShare.


        :param worst_payment_status_in_last36_months_count: The worst_payment_status_in_last36_months_count of this ConnectIdentitySummaryShare.  # noqa: E501
        :type: str
        """

        self._worst_payment_status_in_last36_months_count = worst_payment_status_in_last36_months_count

    @property
    def defaults_in_last12_months_count(self):
        """Gets the defaults_in_last12_months_count of this ConnectIdentitySummaryShare.  # noqa: E501


        :return: The defaults_in_last12_months_count of this ConnectIdentitySummaryShare.  # noqa: E501
        :rtype: int
        """
        return self._defaults_in_last12_months_count

    @defaults_in_last12_months_count.setter
    def defaults_in_last12_months_count(self, defaults_in_last12_months_count):
        """Sets the defaults_in_last12_months_count of this ConnectIdentitySummaryShare.


        :param defaults_in_last12_months_count: The defaults_in_last12_months_count of this ConnectIdentitySummaryShare.  # noqa: E501
        :type: int
        """

        self._defaults_in_last12_months_count = defaults_in_last12_months_count

    @property
    def defaults_in_last36_months_count(self):
        """Gets the defaults_in_last36_months_count of this ConnectIdentitySummaryShare.  # noqa: E501


        :return: The defaults_in_last36_months_count of this ConnectIdentitySummaryShare.  # noqa: E501
        :rtype: int
        """
        return self._defaults_in_last36_months_count

    @defaults_in_last36_months_count.setter
    def defaults_in_last36_months_count(self, defaults_in_last36_months_count):
        """Sets the defaults_in_last36_months_count of this ConnectIdentitySummaryShare.


        :param defaults_in_last36_months_count: The defaults_in_last36_months_count of this ConnectIdentitySummaryShare.  # noqa: E501
        :type: int
        """

        self._defaults_in_last36_months_count = defaults_in_last36_months_count

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
        if issubclass(ConnectIdentitySummaryShare, dict):
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
        if not isinstance(other, ConnectIdentitySummaryShare):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

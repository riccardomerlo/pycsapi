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

class CreditsafeGlobalDataReportsFinancialRatios(object):
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
        'pre_tax_profit_margin': 'float',
        'return_on_capital_employed': 'float',
        'return_on_total_assets_employed': 'float',
        'return_on_net_assets_employed': 'float',
        'sales_or_net_working_capital': 'float',
        'stock_turnover_ratio': 'float',
        'debtor_days': 'float',
        'creditor_days': 'float',
        'current_ratio': 'float',
        'liquidity_ratio_or_acid_test': 'float',
        'current_debt_ratio': 'float',
        'gearing': 'float',
        'equity_in_percentage': 'float',
        'total_debt_ratio': 'float'
    }

    attribute_map = {
        'pre_tax_profit_margin': 'preTaxProfitMargin',
        'return_on_capital_employed': 'returnOnCapitalEmployed',
        'return_on_total_assets_employed': 'returnOnTotalAssetsEmployed',
        'return_on_net_assets_employed': 'returnOnNetAssetsEmployed',
        'sales_or_net_working_capital': 'salesOrNetWorkingCapital',
        'stock_turnover_ratio': 'stockTurnoverRatio',
        'debtor_days': 'debtorDays',
        'creditor_days': 'creditorDays',
        'current_ratio': 'currentRatio',
        'liquidity_ratio_or_acid_test': 'liquidityRatioOrAcidTest',
        'current_debt_ratio': 'currentDebtRatio',
        'gearing': 'gearing',
        'equity_in_percentage': 'equityInPercentage',
        'total_debt_ratio': 'totalDebtRatio'
    }

    def __init__(self, pre_tax_profit_margin=None, return_on_capital_employed=None, return_on_total_assets_employed=None, return_on_net_assets_employed=None, sales_or_net_working_capital=None, stock_turnover_ratio=None, debtor_days=None, creditor_days=None, current_ratio=None, liquidity_ratio_or_acid_test=None, current_debt_ratio=None, gearing=None, equity_in_percentage=None, total_debt_ratio=None):  # noqa: E501
        """CreditsafeGlobalDataReportsFinancialRatios - a model defined in Swagger"""  # noqa: E501
        self._pre_tax_profit_margin = None
        self._return_on_capital_employed = None
        self._return_on_total_assets_employed = None
        self._return_on_net_assets_employed = None
        self._sales_or_net_working_capital = None
        self._stock_turnover_ratio = None
        self._debtor_days = None
        self._creditor_days = None
        self._current_ratio = None
        self._liquidity_ratio_or_acid_test = None
        self._current_debt_ratio = None
        self._gearing = None
        self._equity_in_percentage = None
        self._total_debt_ratio = None
        self.discriminator = None
        if pre_tax_profit_margin is not None:
            self.pre_tax_profit_margin = pre_tax_profit_margin
        if return_on_capital_employed is not None:
            self.return_on_capital_employed = return_on_capital_employed
        if return_on_total_assets_employed is not None:
            self.return_on_total_assets_employed = return_on_total_assets_employed
        if return_on_net_assets_employed is not None:
            self.return_on_net_assets_employed = return_on_net_assets_employed
        if sales_or_net_working_capital is not None:
            self.sales_or_net_working_capital = sales_or_net_working_capital
        if stock_turnover_ratio is not None:
            self.stock_turnover_ratio = stock_turnover_ratio
        if debtor_days is not None:
            self.debtor_days = debtor_days
        if creditor_days is not None:
            self.creditor_days = creditor_days
        if current_ratio is not None:
            self.current_ratio = current_ratio
        if liquidity_ratio_or_acid_test is not None:
            self.liquidity_ratio_or_acid_test = liquidity_ratio_or_acid_test
        if current_debt_ratio is not None:
            self.current_debt_ratio = current_debt_ratio
        if gearing is not None:
            self.gearing = gearing
        if equity_in_percentage is not None:
            self.equity_in_percentage = equity_in_percentage
        if total_debt_ratio is not None:
            self.total_debt_ratio = total_debt_ratio

    @property
    def pre_tax_profit_margin(self):
        """Gets the pre_tax_profit_margin of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501


        :return: The pre_tax_profit_margin of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :rtype: float
        """
        return self._pre_tax_profit_margin

    @pre_tax_profit_margin.setter
    def pre_tax_profit_margin(self, pre_tax_profit_margin):
        """Sets the pre_tax_profit_margin of this CreditsafeGlobalDataReportsFinancialRatios.


        :param pre_tax_profit_margin: The pre_tax_profit_margin of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :type: float
        """

        self._pre_tax_profit_margin = pre_tax_profit_margin

    @property
    def return_on_capital_employed(self):
        """Gets the return_on_capital_employed of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501


        :return: The return_on_capital_employed of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :rtype: float
        """
        return self._return_on_capital_employed

    @return_on_capital_employed.setter
    def return_on_capital_employed(self, return_on_capital_employed):
        """Sets the return_on_capital_employed of this CreditsafeGlobalDataReportsFinancialRatios.


        :param return_on_capital_employed: The return_on_capital_employed of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :type: float
        """

        self._return_on_capital_employed = return_on_capital_employed

    @property
    def return_on_total_assets_employed(self):
        """Gets the return_on_total_assets_employed of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501


        :return: The return_on_total_assets_employed of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :rtype: float
        """
        return self._return_on_total_assets_employed

    @return_on_total_assets_employed.setter
    def return_on_total_assets_employed(self, return_on_total_assets_employed):
        """Sets the return_on_total_assets_employed of this CreditsafeGlobalDataReportsFinancialRatios.


        :param return_on_total_assets_employed: The return_on_total_assets_employed of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :type: float
        """

        self._return_on_total_assets_employed = return_on_total_assets_employed

    @property
    def return_on_net_assets_employed(self):
        """Gets the return_on_net_assets_employed of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501


        :return: The return_on_net_assets_employed of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :rtype: float
        """
        return self._return_on_net_assets_employed

    @return_on_net_assets_employed.setter
    def return_on_net_assets_employed(self, return_on_net_assets_employed):
        """Sets the return_on_net_assets_employed of this CreditsafeGlobalDataReportsFinancialRatios.


        :param return_on_net_assets_employed: The return_on_net_assets_employed of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :type: float
        """

        self._return_on_net_assets_employed = return_on_net_assets_employed

    @property
    def sales_or_net_working_capital(self):
        """Gets the sales_or_net_working_capital of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501


        :return: The sales_or_net_working_capital of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :rtype: float
        """
        return self._sales_or_net_working_capital

    @sales_or_net_working_capital.setter
    def sales_or_net_working_capital(self, sales_or_net_working_capital):
        """Sets the sales_or_net_working_capital of this CreditsafeGlobalDataReportsFinancialRatios.


        :param sales_or_net_working_capital: The sales_or_net_working_capital of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :type: float
        """

        self._sales_or_net_working_capital = sales_or_net_working_capital

    @property
    def stock_turnover_ratio(self):
        """Gets the stock_turnover_ratio of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501


        :return: The stock_turnover_ratio of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :rtype: float
        """
        return self._stock_turnover_ratio

    @stock_turnover_ratio.setter
    def stock_turnover_ratio(self, stock_turnover_ratio):
        """Sets the stock_turnover_ratio of this CreditsafeGlobalDataReportsFinancialRatios.


        :param stock_turnover_ratio: The stock_turnover_ratio of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :type: float
        """

        self._stock_turnover_ratio = stock_turnover_ratio

    @property
    def debtor_days(self):
        """Gets the debtor_days of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501


        :return: The debtor_days of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :rtype: float
        """
        return self._debtor_days

    @debtor_days.setter
    def debtor_days(self, debtor_days):
        """Sets the debtor_days of this CreditsafeGlobalDataReportsFinancialRatios.


        :param debtor_days: The debtor_days of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :type: float
        """

        self._debtor_days = debtor_days

    @property
    def creditor_days(self):
        """Gets the creditor_days of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501


        :return: The creditor_days of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :rtype: float
        """
        return self._creditor_days

    @creditor_days.setter
    def creditor_days(self, creditor_days):
        """Sets the creditor_days of this CreditsafeGlobalDataReportsFinancialRatios.


        :param creditor_days: The creditor_days of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :type: float
        """

        self._creditor_days = creditor_days

    @property
    def current_ratio(self):
        """Gets the current_ratio of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501


        :return: The current_ratio of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :rtype: float
        """
        return self._current_ratio

    @current_ratio.setter
    def current_ratio(self, current_ratio):
        """Sets the current_ratio of this CreditsafeGlobalDataReportsFinancialRatios.


        :param current_ratio: The current_ratio of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :type: float
        """

        self._current_ratio = current_ratio

    @property
    def liquidity_ratio_or_acid_test(self):
        """Gets the liquidity_ratio_or_acid_test of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501


        :return: The liquidity_ratio_or_acid_test of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :rtype: float
        """
        return self._liquidity_ratio_or_acid_test

    @liquidity_ratio_or_acid_test.setter
    def liquidity_ratio_or_acid_test(self, liquidity_ratio_or_acid_test):
        """Sets the liquidity_ratio_or_acid_test of this CreditsafeGlobalDataReportsFinancialRatios.


        :param liquidity_ratio_or_acid_test: The liquidity_ratio_or_acid_test of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :type: float
        """

        self._liquidity_ratio_or_acid_test = liquidity_ratio_or_acid_test

    @property
    def current_debt_ratio(self):
        """Gets the current_debt_ratio of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501


        :return: The current_debt_ratio of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :rtype: float
        """
        return self._current_debt_ratio

    @current_debt_ratio.setter
    def current_debt_ratio(self, current_debt_ratio):
        """Sets the current_debt_ratio of this CreditsafeGlobalDataReportsFinancialRatios.


        :param current_debt_ratio: The current_debt_ratio of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :type: float
        """

        self._current_debt_ratio = current_debt_ratio

    @property
    def gearing(self):
        """Gets the gearing of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501


        :return: The gearing of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :rtype: float
        """
        return self._gearing

    @gearing.setter
    def gearing(self, gearing):
        """Sets the gearing of this CreditsafeGlobalDataReportsFinancialRatios.


        :param gearing: The gearing of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :type: float
        """

        self._gearing = gearing

    @property
    def equity_in_percentage(self):
        """Gets the equity_in_percentage of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501


        :return: The equity_in_percentage of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :rtype: float
        """
        return self._equity_in_percentage

    @equity_in_percentage.setter
    def equity_in_percentage(self, equity_in_percentage):
        """Sets the equity_in_percentage of this CreditsafeGlobalDataReportsFinancialRatios.


        :param equity_in_percentage: The equity_in_percentage of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :type: float
        """

        self._equity_in_percentage = equity_in_percentage

    @property
    def total_debt_ratio(self):
        """Gets the total_debt_ratio of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501


        :return: The total_debt_ratio of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :rtype: float
        """
        return self._total_debt_ratio

    @total_debt_ratio.setter
    def total_debt_ratio(self, total_debt_ratio):
        """Sets the total_debt_ratio of this CreditsafeGlobalDataReportsFinancialRatios.


        :param total_debt_ratio: The total_debt_ratio of this CreditsafeGlobalDataReportsFinancialRatios.  # noqa: E501
        :type: float
        """

        self._total_debt_ratio = total_debt_ratio

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
        if issubclass(CreditsafeGlobalDataReportsFinancialRatios, dict):
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
        if not isinstance(other, CreditsafeGlobalDataReportsFinancialRatios):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

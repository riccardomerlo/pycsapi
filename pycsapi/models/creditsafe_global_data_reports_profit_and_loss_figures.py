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

class CreditsafeGlobalDataReportsProfitAndLossFigures(object):
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
        'revenue': 'float',
        'operating_costs': 'float',
        'operating_profit': 'float',
        'wages_and_salaries': 'float',
        'pension_costs': 'float',
        'depreciation': 'float',
        'amortisation': 'float',
        'financial_income': 'float',
        'financial_expenses': 'float',
        'extraordinary_income': 'float',
        'extraordinary_costs': 'float',
        'profit_before_tax': 'float',
        'tax': 'float',
        'profit_after_tax': 'float',
        'dividends': 'float',
        'minority_interests': 'float',
        'other_appropriations': 'float',
        'retained_profit': 'float'
    }

    attribute_map = {
        'revenue': 'revenue',
        'operating_costs': 'operatingCosts',
        'operating_profit': 'operatingProfit',
        'wages_and_salaries': 'wagesAndSalaries',
        'pension_costs': 'pensionCosts',
        'depreciation': 'depreciation',
        'amortisation': 'amortisation',
        'financial_income': 'financialIncome',
        'financial_expenses': 'financialExpenses',
        'extraordinary_income': 'extraordinaryIncome',
        'extraordinary_costs': 'extraordinaryCosts',
        'profit_before_tax': 'profitBeforeTax',
        'tax': 'tax',
        'profit_after_tax': 'profitAfterTax',
        'dividends': 'dividends',
        'minority_interests': 'minorityInterests',
        'other_appropriations': 'otherAppropriations',
        'retained_profit': 'retainedProfit'
    }

    def __init__(self, revenue=None, operating_costs=None, operating_profit=None, wages_and_salaries=None, pension_costs=None, depreciation=None, amortisation=None, financial_income=None, financial_expenses=None, extraordinary_income=None, extraordinary_costs=None, profit_before_tax=None, tax=None, profit_after_tax=None, dividends=None, minority_interests=None, other_appropriations=None, retained_profit=None):  # noqa: E501
        """CreditsafeGlobalDataReportsProfitAndLossFigures - a model defined in Swagger"""  # noqa: E501
        self._revenue = None
        self._operating_costs = None
        self._operating_profit = None
        self._wages_and_salaries = None
        self._pension_costs = None
        self._depreciation = None
        self._amortisation = None
        self._financial_income = None
        self._financial_expenses = None
        self._extraordinary_income = None
        self._extraordinary_costs = None
        self._profit_before_tax = None
        self._tax = None
        self._profit_after_tax = None
        self._dividends = None
        self._minority_interests = None
        self._other_appropriations = None
        self._retained_profit = None
        self.discriminator = None
        if revenue is not None:
            self.revenue = revenue
        if operating_costs is not None:
            self.operating_costs = operating_costs
        if operating_profit is not None:
            self.operating_profit = operating_profit
        if wages_and_salaries is not None:
            self.wages_and_salaries = wages_and_salaries
        if pension_costs is not None:
            self.pension_costs = pension_costs
        if depreciation is not None:
            self.depreciation = depreciation
        if amortisation is not None:
            self.amortisation = amortisation
        if financial_income is not None:
            self.financial_income = financial_income
        if financial_expenses is not None:
            self.financial_expenses = financial_expenses
        if extraordinary_income is not None:
            self.extraordinary_income = extraordinary_income
        if extraordinary_costs is not None:
            self.extraordinary_costs = extraordinary_costs
        if profit_before_tax is not None:
            self.profit_before_tax = profit_before_tax
        if tax is not None:
            self.tax = tax
        if profit_after_tax is not None:
            self.profit_after_tax = profit_after_tax
        if dividends is not None:
            self.dividends = dividends
        if minority_interests is not None:
            self.minority_interests = minority_interests
        if other_appropriations is not None:
            self.other_appropriations = other_appropriations
        if retained_profit is not None:
            self.retained_profit = retained_profit

    @property
    def revenue(self):
        """Gets the revenue of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501


        :return: The revenue of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :rtype: float
        """
        return self._revenue

    @revenue.setter
    def revenue(self, revenue):
        """Sets the revenue of this CreditsafeGlobalDataReportsProfitAndLossFigures.


        :param revenue: The revenue of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :type: float
        """

        self._revenue = revenue

    @property
    def operating_costs(self):
        """Gets the operating_costs of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501


        :return: The operating_costs of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :rtype: float
        """
        return self._operating_costs

    @operating_costs.setter
    def operating_costs(self, operating_costs):
        """Sets the operating_costs of this CreditsafeGlobalDataReportsProfitAndLossFigures.


        :param operating_costs: The operating_costs of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :type: float
        """

        self._operating_costs = operating_costs

    @property
    def operating_profit(self):
        """Gets the operating_profit of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501


        :return: The operating_profit of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :rtype: float
        """
        return self._operating_profit

    @operating_profit.setter
    def operating_profit(self, operating_profit):
        """Sets the operating_profit of this CreditsafeGlobalDataReportsProfitAndLossFigures.


        :param operating_profit: The operating_profit of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :type: float
        """

        self._operating_profit = operating_profit

    @property
    def wages_and_salaries(self):
        """Gets the wages_and_salaries of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501


        :return: The wages_and_salaries of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :rtype: float
        """
        return self._wages_and_salaries

    @wages_and_salaries.setter
    def wages_and_salaries(self, wages_and_salaries):
        """Sets the wages_and_salaries of this CreditsafeGlobalDataReportsProfitAndLossFigures.


        :param wages_and_salaries: The wages_and_salaries of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :type: float
        """

        self._wages_and_salaries = wages_and_salaries

    @property
    def pension_costs(self):
        """Gets the pension_costs of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501


        :return: The pension_costs of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :rtype: float
        """
        return self._pension_costs

    @pension_costs.setter
    def pension_costs(self, pension_costs):
        """Sets the pension_costs of this CreditsafeGlobalDataReportsProfitAndLossFigures.


        :param pension_costs: The pension_costs of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :type: float
        """

        self._pension_costs = pension_costs

    @property
    def depreciation(self):
        """Gets the depreciation of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501


        :return: The depreciation of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :rtype: float
        """
        return self._depreciation

    @depreciation.setter
    def depreciation(self, depreciation):
        """Sets the depreciation of this CreditsafeGlobalDataReportsProfitAndLossFigures.


        :param depreciation: The depreciation of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :type: float
        """

        self._depreciation = depreciation

    @property
    def amortisation(self):
        """Gets the amortisation of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501


        :return: The amortisation of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :rtype: float
        """
        return self._amortisation

    @amortisation.setter
    def amortisation(self, amortisation):
        """Sets the amortisation of this CreditsafeGlobalDataReportsProfitAndLossFigures.


        :param amortisation: The amortisation of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :type: float
        """

        self._amortisation = amortisation

    @property
    def financial_income(self):
        """Gets the financial_income of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501


        :return: The financial_income of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :rtype: float
        """
        return self._financial_income

    @financial_income.setter
    def financial_income(self, financial_income):
        """Sets the financial_income of this CreditsafeGlobalDataReportsProfitAndLossFigures.


        :param financial_income: The financial_income of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :type: float
        """

        self._financial_income = financial_income

    @property
    def financial_expenses(self):
        """Gets the financial_expenses of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501


        :return: The financial_expenses of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :rtype: float
        """
        return self._financial_expenses

    @financial_expenses.setter
    def financial_expenses(self, financial_expenses):
        """Sets the financial_expenses of this CreditsafeGlobalDataReportsProfitAndLossFigures.


        :param financial_expenses: The financial_expenses of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :type: float
        """

        self._financial_expenses = financial_expenses

    @property
    def extraordinary_income(self):
        """Gets the extraordinary_income of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501


        :return: The extraordinary_income of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :rtype: float
        """
        return self._extraordinary_income

    @extraordinary_income.setter
    def extraordinary_income(self, extraordinary_income):
        """Sets the extraordinary_income of this CreditsafeGlobalDataReportsProfitAndLossFigures.


        :param extraordinary_income: The extraordinary_income of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :type: float
        """

        self._extraordinary_income = extraordinary_income

    @property
    def extraordinary_costs(self):
        """Gets the extraordinary_costs of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501


        :return: The extraordinary_costs of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :rtype: float
        """
        return self._extraordinary_costs

    @extraordinary_costs.setter
    def extraordinary_costs(self, extraordinary_costs):
        """Sets the extraordinary_costs of this CreditsafeGlobalDataReportsProfitAndLossFigures.


        :param extraordinary_costs: The extraordinary_costs of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :type: float
        """

        self._extraordinary_costs = extraordinary_costs

    @property
    def profit_before_tax(self):
        """Gets the profit_before_tax of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501


        :return: The profit_before_tax of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :rtype: float
        """
        return self._profit_before_tax

    @profit_before_tax.setter
    def profit_before_tax(self, profit_before_tax):
        """Sets the profit_before_tax of this CreditsafeGlobalDataReportsProfitAndLossFigures.


        :param profit_before_tax: The profit_before_tax of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :type: float
        """

        self._profit_before_tax = profit_before_tax

    @property
    def tax(self):
        """Gets the tax of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501


        :return: The tax of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :rtype: float
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this CreditsafeGlobalDataReportsProfitAndLossFigures.


        :param tax: The tax of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :type: float
        """

        self._tax = tax

    @property
    def profit_after_tax(self):
        """Gets the profit_after_tax of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501


        :return: The profit_after_tax of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :rtype: float
        """
        return self._profit_after_tax

    @profit_after_tax.setter
    def profit_after_tax(self, profit_after_tax):
        """Sets the profit_after_tax of this CreditsafeGlobalDataReportsProfitAndLossFigures.


        :param profit_after_tax: The profit_after_tax of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :type: float
        """

        self._profit_after_tax = profit_after_tax

    @property
    def dividends(self):
        """Gets the dividends of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501


        :return: The dividends of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :rtype: float
        """
        return self._dividends

    @dividends.setter
    def dividends(self, dividends):
        """Sets the dividends of this CreditsafeGlobalDataReportsProfitAndLossFigures.


        :param dividends: The dividends of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :type: float
        """

        self._dividends = dividends

    @property
    def minority_interests(self):
        """Gets the minority_interests of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501


        :return: The minority_interests of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :rtype: float
        """
        return self._minority_interests

    @minority_interests.setter
    def minority_interests(self, minority_interests):
        """Sets the minority_interests of this CreditsafeGlobalDataReportsProfitAndLossFigures.


        :param minority_interests: The minority_interests of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :type: float
        """

        self._minority_interests = minority_interests

    @property
    def other_appropriations(self):
        """Gets the other_appropriations of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501


        :return: The other_appropriations of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :rtype: float
        """
        return self._other_appropriations

    @other_appropriations.setter
    def other_appropriations(self, other_appropriations):
        """Sets the other_appropriations of this CreditsafeGlobalDataReportsProfitAndLossFigures.


        :param other_appropriations: The other_appropriations of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :type: float
        """

        self._other_appropriations = other_appropriations

    @property
    def retained_profit(self):
        """Gets the retained_profit of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501


        :return: The retained_profit of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :rtype: float
        """
        return self._retained_profit

    @retained_profit.setter
    def retained_profit(self, retained_profit):
        """Sets the retained_profit of this CreditsafeGlobalDataReportsProfitAndLossFigures.


        :param retained_profit: The retained_profit of this CreditsafeGlobalDataReportsProfitAndLossFigures.  # noqa: E501
        :type: float
        """

        self._retained_profit = retained_profit

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
        if issubclass(CreditsafeGlobalDataReportsProfitAndLossFigures, dict):
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
        if not isinstance(other, CreditsafeGlobalDataReportsProfitAndLossFigures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

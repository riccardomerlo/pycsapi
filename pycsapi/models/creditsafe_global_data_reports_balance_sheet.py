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

class CreditsafeGlobalDataReportsBalanceSheet(object):
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
        'land_and_buildings': 'float',
        'plant_and_machinery': 'float',
        'other_tangible_assets': 'float',
        'total_tangible_assets': 'float',
        'goodwill': 'float',
        'other_intangible_assets': 'float',
        'total_intangible_assets': 'float',
        'investments': 'float',
        'loans_to_group': 'float',
        'other_loans': 'float',
        'miscellaneous_fixed_assets': 'float',
        'total_other_fixed_assets': 'float',
        'total_fixed_assets': 'float',
        'raw_materials': 'float',
        'work_in_progress': 'float',
        'finished_goods': 'float',
        'other_inventories': 'float',
        'total_inventories': 'float',
        'trade_receivables': 'float',
        'group_receivables': 'float',
        'receivables_due_after1_year': 'float',
        'miscellaneous_receivables': 'float',
        'total_receivables': 'float',
        'cash': 'float',
        'other_current_assets': 'float',
        'total_current_assets': 'float',
        'total_assets': 'float',
        'trade_payables': 'float',
        'bank_liabilities': 'float',
        'other_loans_or_finance': 'float',
        'group_payables': 'float',
        'miscellaneous_liabilities': 'float',
        'total_current_liabilities': 'float',
        'trade_payables_due_after1_year': 'float',
        'bank_liabilities_due_after1_year': 'float',
        'other_loans_or_finance_due_after1_year': 'float',
        'group_payables_due_after1_year': 'float',
        'miscellaneous_liabilities_due_after1_year': 'float',
        'total_long_term_liabilities': 'float',
        'total_liabilities': 'float',
        'called_up_share_capital': 'float',
        'share_premium': 'float',
        'revenue_reserves': 'float',
        'other_reserves': 'float',
        'total_shareholders_equity': 'float'
    }

    attribute_map = {
        'land_and_buildings': 'landAndBuildings',
        'plant_and_machinery': 'plantAndMachinery',
        'other_tangible_assets': 'otherTangibleAssets',
        'total_tangible_assets': 'totalTangibleAssets',
        'goodwill': 'goodwill',
        'other_intangible_assets': 'otherIntangibleAssets',
        'total_intangible_assets': 'totalIntangibleAssets',
        'investments': 'investments',
        'loans_to_group': 'loansToGroup',
        'other_loans': 'otherLoans',
        'miscellaneous_fixed_assets': 'miscellaneousFixedAssets',
        'total_other_fixed_assets': 'totalOtherFixedAssets',
        'total_fixed_assets': 'totalFixedAssets',
        'raw_materials': 'rawMaterials',
        'work_in_progress': 'workInProgress',
        'finished_goods': 'finishedGoods',
        'other_inventories': 'otherInventories',
        'total_inventories': 'totalInventories',
        'trade_receivables': 'tradeReceivables',
        'group_receivables': 'groupReceivables',
        'receivables_due_after1_year': 'receivablesDueAfter1Year',
        'miscellaneous_receivables': 'miscellaneousReceivables',
        'total_receivables': 'totalReceivables',
        'cash': 'cash',
        'other_current_assets': 'otherCurrentAssets',
        'total_current_assets': 'totalCurrentAssets',
        'total_assets': 'totalAssets',
        'trade_payables': 'tradePayables',
        'bank_liabilities': 'bankLiabilities',
        'other_loans_or_finance': 'otherLoansOrFinance',
        'group_payables': 'groupPayables',
        'miscellaneous_liabilities': 'miscellaneousLiabilities',
        'total_current_liabilities': 'totalCurrentLiabilities',
        'trade_payables_due_after1_year': 'tradePayablesDueAfter1Year',
        'bank_liabilities_due_after1_year': 'bankLiabilitiesDueAfter1Year',
        'other_loans_or_finance_due_after1_year': 'otherLoansOrFinanceDueAfter1Year',
        'group_payables_due_after1_year': 'groupPayablesDueAfter1Year',
        'miscellaneous_liabilities_due_after1_year': 'miscellaneousLiabilitiesDueAfter1Year',
        'total_long_term_liabilities': 'totalLongTermLiabilities',
        'total_liabilities': 'totalLiabilities',
        'called_up_share_capital': 'calledUpShareCapital',
        'share_premium': 'sharePremium',
        'revenue_reserves': 'revenueReserves',
        'other_reserves': 'otherReserves',
        'total_shareholders_equity': 'totalShareholdersEquity'
    }

    def __init__(self, land_and_buildings=None, plant_and_machinery=None, other_tangible_assets=None, total_tangible_assets=None, goodwill=None, other_intangible_assets=None, total_intangible_assets=None, investments=None, loans_to_group=None, other_loans=None, miscellaneous_fixed_assets=None, total_other_fixed_assets=None, total_fixed_assets=None, raw_materials=None, work_in_progress=None, finished_goods=None, other_inventories=None, total_inventories=None, trade_receivables=None, group_receivables=None, receivables_due_after1_year=None, miscellaneous_receivables=None, total_receivables=None, cash=None, other_current_assets=None, total_current_assets=None, total_assets=None, trade_payables=None, bank_liabilities=None, other_loans_or_finance=None, group_payables=None, miscellaneous_liabilities=None, total_current_liabilities=None, trade_payables_due_after1_year=None, bank_liabilities_due_after1_year=None, other_loans_or_finance_due_after1_year=None, group_payables_due_after1_year=None, miscellaneous_liabilities_due_after1_year=None, total_long_term_liabilities=None, total_liabilities=None, called_up_share_capital=None, share_premium=None, revenue_reserves=None, other_reserves=None, total_shareholders_equity=None):  # noqa: E501
        """CreditsafeGlobalDataReportsBalanceSheet - a model defined in Swagger"""  # noqa: E501
        self._land_and_buildings = None
        self._plant_and_machinery = None
        self._other_tangible_assets = None
        self._total_tangible_assets = None
        self._goodwill = None
        self._other_intangible_assets = None
        self._total_intangible_assets = None
        self._investments = None
        self._loans_to_group = None
        self._other_loans = None
        self._miscellaneous_fixed_assets = None
        self._total_other_fixed_assets = None
        self._total_fixed_assets = None
        self._raw_materials = None
        self._work_in_progress = None
        self._finished_goods = None
        self._other_inventories = None
        self._total_inventories = None
        self._trade_receivables = None
        self._group_receivables = None
        self._receivables_due_after1_year = None
        self._miscellaneous_receivables = None
        self._total_receivables = None
        self._cash = None
        self._other_current_assets = None
        self._total_current_assets = None
        self._total_assets = None
        self._trade_payables = None
        self._bank_liabilities = None
        self._other_loans_or_finance = None
        self._group_payables = None
        self._miscellaneous_liabilities = None
        self._total_current_liabilities = None
        self._trade_payables_due_after1_year = None
        self._bank_liabilities_due_after1_year = None
        self._other_loans_or_finance_due_after1_year = None
        self._group_payables_due_after1_year = None
        self._miscellaneous_liabilities_due_after1_year = None
        self._total_long_term_liabilities = None
        self._total_liabilities = None
        self._called_up_share_capital = None
        self._share_premium = None
        self._revenue_reserves = None
        self._other_reserves = None
        self._total_shareholders_equity = None
        self.discriminator = None
        if land_and_buildings is not None:
            self.land_and_buildings = land_and_buildings
        if plant_and_machinery is not None:
            self.plant_and_machinery = plant_and_machinery
        if other_tangible_assets is not None:
            self.other_tangible_assets = other_tangible_assets
        if total_tangible_assets is not None:
            self.total_tangible_assets = total_tangible_assets
        if goodwill is not None:
            self.goodwill = goodwill
        if other_intangible_assets is not None:
            self.other_intangible_assets = other_intangible_assets
        if total_intangible_assets is not None:
            self.total_intangible_assets = total_intangible_assets
        if investments is not None:
            self.investments = investments
        if loans_to_group is not None:
            self.loans_to_group = loans_to_group
        if other_loans is not None:
            self.other_loans = other_loans
        if miscellaneous_fixed_assets is not None:
            self.miscellaneous_fixed_assets = miscellaneous_fixed_assets
        if total_other_fixed_assets is not None:
            self.total_other_fixed_assets = total_other_fixed_assets
        if total_fixed_assets is not None:
            self.total_fixed_assets = total_fixed_assets
        if raw_materials is not None:
            self.raw_materials = raw_materials
        if work_in_progress is not None:
            self.work_in_progress = work_in_progress
        if finished_goods is not None:
            self.finished_goods = finished_goods
        if other_inventories is not None:
            self.other_inventories = other_inventories
        if total_inventories is not None:
            self.total_inventories = total_inventories
        if trade_receivables is not None:
            self.trade_receivables = trade_receivables
        if group_receivables is not None:
            self.group_receivables = group_receivables
        if receivables_due_after1_year is not None:
            self.receivables_due_after1_year = receivables_due_after1_year
        if miscellaneous_receivables is not None:
            self.miscellaneous_receivables = miscellaneous_receivables
        if total_receivables is not None:
            self.total_receivables = total_receivables
        if cash is not None:
            self.cash = cash
        if other_current_assets is not None:
            self.other_current_assets = other_current_assets
        if total_current_assets is not None:
            self.total_current_assets = total_current_assets
        if total_assets is not None:
            self.total_assets = total_assets
        if trade_payables is not None:
            self.trade_payables = trade_payables
        if bank_liabilities is not None:
            self.bank_liabilities = bank_liabilities
        if other_loans_or_finance is not None:
            self.other_loans_or_finance = other_loans_or_finance
        if group_payables is not None:
            self.group_payables = group_payables
        if miscellaneous_liabilities is not None:
            self.miscellaneous_liabilities = miscellaneous_liabilities
        if total_current_liabilities is not None:
            self.total_current_liabilities = total_current_liabilities
        if trade_payables_due_after1_year is not None:
            self.trade_payables_due_after1_year = trade_payables_due_after1_year
        if bank_liabilities_due_after1_year is not None:
            self.bank_liabilities_due_after1_year = bank_liabilities_due_after1_year
        if other_loans_or_finance_due_after1_year is not None:
            self.other_loans_or_finance_due_after1_year = other_loans_or_finance_due_after1_year
        if group_payables_due_after1_year is not None:
            self.group_payables_due_after1_year = group_payables_due_after1_year
        if miscellaneous_liabilities_due_after1_year is not None:
            self.miscellaneous_liabilities_due_after1_year = miscellaneous_liabilities_due_after1_year
        if total_long_term_liabilities is not None:
            self.total_long_term_liabilities = total_long_term_liabilities
        if total_liabilities is not None:
            self.total_liabilities = total_liabilities
        if called_up_share_capital is not None:
            self.called_up_share_capital = called_up_share_capital
        if share_premium is not None:
            self.share_premium = share_premium
        if revenue_reserves is not None:
            self.revenue_reserves = revenue_reserves
        if other_reserves is not None:
            self.other_reserves = other_reserves
        if total_shareholders_equity is not None:
            self.total_shareholders_equity = total_shareholders_equity

    @property
    def land_and_buildings(self):
        """Gets the land_and_buildings of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The land_and_buildings of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._land_and_buildings

    @land_and_buildings.setter
    def land_and_buildings(self, land_and_buildings):
        """Sets the land_and_buildings of this CreditsafeGlobalDataReportsBalanceSheet.


        :param land_and_buildings: The land_and_buildings of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._land_and_buildings = land_and_buildings

    @property
    def plant_and_machinery(self):
        """Gets the plant_and_machinery of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The plant_and_machinery of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._plant_and_machinery

    @plant_and_machinery.setter
    def plant_and_machinery(self, plant_and_machinery):
        """Sets the plant_and_machinery of this CreditsafeGlobalDataReportsBalanceSheet.


        :param plant_and_machinery: The plant_and_machinery of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._plant_and_machinery = plant_and_machinery

    @property
    def other_tangible_assets(self):
        """Gets the other_tangible_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The other_tangible_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._other_tangible_assets

    @other_tangible_assets.setter
    def other_tangible_assets(self, other_tangible_assets):
        """Sets the other_tangible_assets of this CreditsafeGlobalDataReportsBalanceSheet.


        :param other_tangible_assets: The other_tangible_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._other_tangible_assets = other_tangible_assets

    @property
    def total_tangible_assets(self):
        """Gets the total_tangible_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The total_tangible_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._total_tangible_assets

    @total_tangible_assets.setter
    def total_tangible_assets(self, total_tangible_assets):
        """Sets the total_tangible_assets of this CreditsafeGlobalDataReportsBalanceSheet.


        :param total_tangible_assets: The total_tangible_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._total_tangible_assets = total_tangible_assets

    @property
    def goodwill(self):
        """Gets the goodwill of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The goodwill of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._goodwill

    @goodwill.setter
    def goodwill(self, goodwill):
        """Sets the goodwill of this CreditsafeGlobalDataReportsBalanceSheet.


        :param goodwill: The goodwill of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._goodwill = goodwill

    @property
    def other_intangible_assets(self):
        """Gets the other_intangible_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The other_intangible_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._other_intangible_assets

    @other_intangible_assets.setter
    def other_intangible_assets(self, other_intangible_assets):
        """Sets the other_intangible_assets of this CreditsafeGlobalDataReportsBalanceSheet.


        :param other_intangible_assets: The other_intangible_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._other_intangible_assets = other_intangible_assets

    @property
    def total_intangible_assets(self):
        """Gets the total_intangible_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The total_intangible_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._total_intangible_assets

    @total_intangible_assets.setter
    def total_intangible_assets(self, total_intangible_assets):
        """Sets the total_intangible_assets of this CreditsafeGlobalDataReportsBalanceSheet.


        :param total_intangible_assets: The total_intangible_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._total_intangible_assets = total_intangible_assets

    @property
    def investments(self):
        """Gets the investments of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The investments of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._investments

    @investments.setter
    def investments(self, investments):
        """Sets the investments of this CreditsafeGlobalDataReportsBalanceSheet.


        :param investments: The investments of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._investments = investments

    @property
    def loans_to_group(self):
        """Gets the loans_to_group of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The loans_to_group of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._loans_to_group

    @loans_to_group.setter
    def loans_to_group(self, loans_to_group):
        """Sets the loans_to_group of this CreditsafeGlobalDataReportsBalanceSheet.


        :param loans_to_group: The loans_to_group of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._loans_to_group = loans_to_group

    @property
    def other_loans(self):
        """Gets the other_loans of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The other_loans of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._other_loans

    @other_loans.setter
    def other_loans(self, other_loans):
        """Sets the other_loans of this CreditsafeGlobalDataReportsBalanceSheet.


        :param other_loans: The other_loans of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._other_loans = other_loans

    @property
    def miscellaneous_fixed_assets(self):
        """Gets the miscellaneous_fixed_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The miscellaneous_fixed_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._miscellaneous_fixed_assets

    @miscellaneous_fixed_assets.setter
    def miscellaneous_fixed_assets(self, miscellaneous_fixed_assets):
        """Sets the miscellaneous_fixed_assets of this CreditsafeGlobalDataReportsBalanceSheet.


        :param miscellaneous_fixed_assets: The miscellaneous_fixed_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._miscellaneous_fixed_assets = miscellaneous_fixed_assets

    @property
    def total_other_fixed_assets(self):
        """Gets the total_other_fixed_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The total_other_fixed_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._total_other_fixed_assets

    @total_other_fixed_assets.setter
    def total_other_fixed_assets(self, total_other_fixed_assets):
        """Sets the total_other_fixed_assets of this CreditsafeGlobalDataReportsBalanceSheet.


        :param total_other_fixed_assets: The total_other_fixed_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._total_other_fixed_assets = total_other_fixed_assets

    @property
    def total_fixed_assets(self):
        """Gets the total_fixed_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The total_fixed_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._total_fixed_assets

    @total_fixed_assets.setter
    def total_fixed_assets(self, total_fixed_assets):
        """Sets the total_fixed_assets of this CreditsafeGlobalDataReportsBalanceSheet.


        :param total_fixed_assets: The total_fixed_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._total_fixed_assets = total_fixed_assets

    @property
    def raw_materials(self):
        """Gets the raw_materials of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The raw_materials of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._raw_materials

    @raw_materials.setter
    def raw_materials(self, raw_materials):
        """Sets the raw_materials of this CreditsafeGlobalDataReportsBalanceSheet.


        :param raw_materials: The raw_materials of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._raw_materials = raw_materials

    @property
    def work_in_progress(self):
        """Gets the work_in_progress of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The work_in_progress of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._work_in_progress

    @work_in_progress.setter
    def work_in_progress(self, work_in_progress):
        """Sets the work_in_progress of this CreditsafeGlobalDataReportsBalanceSheet.


        :param work_in_progress: The work_in_progress of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._work_in_progress = work_in_progress

    @property
    def finished_goods(self):
        """Gets the finished_goods of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The finished_goods of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._finished_goods

    @finished_goods.setter
    def finished_goods(self, finished_goods):
        """Sets the finished_goods of this CreditsafeGlobalDataReportsBalanceSheet.


        :param finished_goods: The finished_goods of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._finished_goods = finished_goods

    @property
    def other_inventories(self):
        """Gets the other_inventories of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The other_inventories of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._other_inventories

    @other_inventories.setter
    def other_inventories(self, other_inventories):
        """Sets the other_inventories of this CreditsafeGlobalDataReportsBalanceSheet.


        :param other_inventories: The other_inventories of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._other_inventories = other_inventories

    @property
    def total_inventories(self):
        """Gets the total_inventories of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The total_inventories of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._total_inventories

    @total_inventories.setter
    def total_inventories(self, total_inventories):
        """Sets the total_inventories of this CreditsafeGlobalDataReportsBalanceSheet.


        :param total_inventories: The total_inventories of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._total_inventories = total_inventories

    @property
    def trade_receivables(self):
        """Gets the trade_receivables of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The trade_receivables of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._trade_receivables

    @trade_receivables.setter
    def trade_receivables(self, trade_receivables):
        """Sets the trade_receivables of this CreditsafeGlobalDataReportsBalanceSheet.


        :param trade_receivables: The trade_receivables of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._trade_receivables = trade_receivables

    @property
    def group_receivables(self):
        """Gets the group_receivables of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The group_receivables of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._group_receivables

    @group_receivables.setter
    def group_receivables(self, group_receivables):
        """Sets the group_receivables of this CreditsafeGlobalDataReportsBalanceSheet.


        :param group_receivables: The group_receivables of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._group_receivables = group_receivables

    @property
    def receivables_due_after1_year(self):
        """Gets the receivables_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The receivables_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._receivables_due_after1_year

    @receivables_due_after1_year.setter
    def receivables_due_after1_year(self, receivables_due_after1_year):
        """Sets the receivables_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.


        :param receivables_due_after1_year: The receivables_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._receivables_due_after1_year = receivables_due_after1_year

    @property
    def miscellaneous_receivables(self):
        """Gets the miscellaneous_receivables of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The miscellaneous_receivables of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._miscellaneous_receivables

    @miscellaneous_receivables.setter
    def miscellaneous_receivables(self, miscellaneous_receivables):
        """Sets the miscellaneous_receivables of this CreditsafeGlobalDataReportsBalanceSheet.


        :param miscellaneous_receivables: The miscellaneous_receivables of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._miscellaneous_receivables = miscellaneous_receivables

    @property
    def total_receivables(self):
        """Gets the total_receivables of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The total_receivables of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._total_receivables

    @total_receivables.setter
    def total_receivables(self, total_receivables):
        """Sets the total_receivables of this CreditsafeGlobalDataReportsBalanceSheet.


        :param total_receivables: The total_receivables of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._total_receivables = total_receivables

    @property
    def cash(self):
        """Gets the cash of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The cash of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._cash

    @cash.setter
    def cash(self, cash):
        """Sets the cash of this CreditsafeGlobalDataReportsBalanceSheet.


        :param cash: The cash of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._cash = cash

    @property
    def other_current_assets(self):
        """Gets the other_current_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The other_current_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._other_current_assets

    @other_current_assets.setter
    def other_current_assets(self, other_current_assets):
        """Sets the other_current_assets of this CreditsafeGlobalDataReportsBalanceSheet.


        :param other_current_assets: The other_current_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._other_current_assets = other_current_assets

    @property
    def total_current_assets(self):
        """Gets the total_current_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The total_current_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._total_current_assets

    @total_current_assets.setter
    def total_current_assets(self, total_current_assets):
        """Sets the total_current_assets of this CreditsafeGlobalDataReportsBalanceSheet.


        :param total_current_assets: The total_current_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._total_current_assets = total_current_assets

    @property
    def total_assets(self):
        """Gets the total_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The total_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._total_assets

    @total_assets.setter
    def total_assets(self, total_assets):
        """Sets the total_assets of this CreditsafeGlobalDataReportsBalanceSheet.


        :param total_assets: The total_assets of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._total_assets = total_assets

    @property
    def trade_payables(self):
        """Gets the trade_payables of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The trade_payables of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._trade_payables

    @trade_payables.setter
    def trade_payables(self, trade_payables):
        """Sets the trade_payables of this CreditsafeGlobalDataReportsBalanceSheet.


        :param trade_payables: The trade_payables of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._trade_payables = trade_payables

    @property
    def bank_liabilities(self):
        """Gets the bank_liabilities of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The bank_liabilities of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._bank_liabilities

    @bank_liabilities.setter
    def bank_liabilities(self, bank_liabilities):
        """Sets the bank_liabilities of this CreditsafeGlobalDataReportsBalanceSheet.


        :param bank_liabilities: The bank_liabilities of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._bank_liabilities = bank_liabilities

    @property
    def other_loans_or_finance(self):
        """Gets the other_loans_or_finance of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The other_loans_or_finance of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._other_loans_or_finance

    @other_loans_or_finance.setter
    def other_loans_or_finance(self, other_loans_or_finance):
        """Sets the other_loans_or_finance of this CreditsafeGlobalDataReportsBalanceSheet.


        :param other_loans_or_finance: The other_loans_or_finance of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._other_loans_or_finance = other_loans_or_finance

    @property
    def group_payables(self):
        """Gets the group_payables of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The group_payables of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._group_payables

    @group_payables.setter
    def group_payables(self, group_payables):
        """Sets the group_payables of this CreditsafeGlobalDataReportsBalanceSheet.


        :param group_payables: The group_payables of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._group_payables = group_payables

    @property
    def miscellaneous_liabilities(self):
        """Gets the miscellaneous_liabilities of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The miscellaneous_liabilities of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._miscellaneous_liabilities

    @miscellaneous_liabilities.setter
    def miscellaneous_liabilities(self, miscellaneous_liabilities):
        """Sets the miscellaneous_liabilities of this CreditsafeGlobalDataReportsBalanceSheet.


        :param miscellaneous_liabilities: The miscellaneous_liabilities of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._miscellaneous_liabilities = miscellaneous_liabilities

    @property
    def total_current_liabilities(self):
        """Gets the total_current_liabilities of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The total_current_liabilities of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._total_current_liabilities

    @total_current_liabilities.setter
    def total_current_liabilities(self, total_current_liabilities):
        """Sets the total_current_liabilities of this CreditsafeGlobalDataReportsBalanceSheet.


        :param total_current_liabilities: The total_current_liabilities of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._total_current_liabilities = total_current_liabilities

    @property
    def trade_payables_due_after1_year(self):
        """Gets the trade_payables_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The trade_payables_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._trade_payables_due_after1_year

    @trade_payables_due_after1_year.setter
    def trade_payables_due_after1_year(self, trade_payables_due_after1_year):
        """Sets the trade_payables_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.


        :param trade_payables_due_after1_year: The trade_payables_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._trade_payables_due_after1_year = trade_payables_due_after1_year

    @property
    def bank_liabilities_due_after1_year(self):
        """Gets the bank_liabilities_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The bank_liabilities_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._bank_liabilities_due_after1_year

    @bank_liabilities_due_after1_year.setter
    def bank_liabilities_due_after1_year(self, bank_liabilities_due_after1_year):
        """Sets the bank_liabilities_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.


        :param bank_liabilities_due_after1_year: The bank_liabilities_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._bank_liabilities_due_after1_year = bank_liabilities_due_after1_year

    @property
    def other_loans_or_finance_due_after1_year(self):
        """Gets the other_loans_or_finance_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The other_loans_or_finance_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._other_loans_or_finance_due_after1_year

    @other_loans_or_finance_due_after1_year.setter
    def other_loans_or_finance_due_after1_year(self, other_loans_or_finance_due_after1_year):
        """Sets the other_loans_or_finance_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.


        :param other_loans_or_finance_due_after1_year: The other_loans_or_finance_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._other_loans_or_finance_due_after1_year = other_loans_or_finance_due_after1_year

    @property
    def group_payables_due_after1_year(self):
        """Gets the group_payables_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The group_payables_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._group_payables_due_after1_year

    @group_payables_due_after1_year.setter
    def group_payables_due_after1_year(self, group_payables_due_after1_year):
        """Sets the group_payables_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.


        :param group_payables_due_after1_year: The group_payables_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._group_payables_due_after1_year = group_payables_due_after1_year

    @property
    def miscellaneous_liabilities_due_after1_year(self):
        """Gets the miscellaneous_liabilities_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The miscellaneous_liabilities_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._miscellaneous_liabilities_due_after1_year

    @miscellaneous_liabilities_due_after1_year.setter
    def miscellaneous_liabilities_due_after1_year(self, miscellaneous_liabilities_due_after1_year):
        """Sets the miscellaneous_liabilities_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.


        :param miscellaneous_liabilities_due_after1_year: The miscellaneous_liabilities_due_after1_year of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._miscellaneous_liabilities_due_after1_year = miscellaneous_liabilities_due_after1_year

    @property
    def total_long_term_liabilities(self):
        """Gets the total_long_term_liabilities of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The total_long_term_liabilities of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._total_long_term_liabilities

    @total_long_term_liabilities.setter
    def total_long_term_liabilities(self, total_long_term_liabilities):
        """Sets the total_long_term_liabilities of this CreditsafeGlobalDataReportsBalanceSheet.


        :param total_long_term_liabilities: The total_long_term_liabilities of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._total_long_term_liabilities = total_long_term_liabilities

    @property
    def total_liabilities(self):
        """Gets the total_liabilities of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The total_liabilities of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._total_liabilities

    @total_liabilities.setter
    def total_liabilities(self, total_liabilities):
        """Sets the total_liabilities of this CreditsafeGlobalDataReportsBalanceSheet.


        :param total_liabilities: The total_liabilities of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._total_liabilities = total_liabilities

    @property
    def called_up_share_capital(self):
        """Gets the called_up_share_capital of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The called_up_share_capital of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._called_up_share_capital

    @called_up_share_capital.setter
    def called_up_share_capital(self, called_up_share_capital):
        """Sets the called_up_share_capital of this CreditsafeGlobalDataReportsBalanceSheet.


        :param called_up_share_capital: The called_up_share_capital of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._called_up_share_capital = called_up_share_capital

    @property
    def share_premium(self):
        """Gets the share_premium of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The share_premium of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._share_premium

    @share_premium.setter
    def share_premium(self, share_premium):
        """Sets the share_premium of this CreditsafeGlobalDataReportsBalanceSheet.


        :param share_premium: The share_premium of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._share_premium = share_premium

    @property
    def revenue_reserves(self):
        """Gets the revenue_reserves of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The revenue_reserves of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._revenue_reserves

    @revenue_reserves.setter
    def revenue_reserves(self, revenue_reserves):
        """Sets the revenue_reserves of this CreditsafeGlobalDataReportsBalanceSheet.


        :param revenue_reserves: The revenue_reserves of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._revenue_reserves = revenue_reserves

    @property
    def other_reserves(self):
        """Gets the other_reserves of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The other_reserves of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._other_reserves

    @other_reserves.setter
    def other_reserves(self, other_reserves):
        """Sets the other_reserves of this CreditsafeGlobalDataReportsBalanceSheet.


        :param other_reserves: The other_reserves of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._other_reserves = other_reserves

    @property
    def total_shareholders_equity(self):
        """Gets the total_shareholders_equity of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501


        :return: The total_shareholders_equity of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :rtype: float
        """
        return self._total_shareholders_equity

    @total_shareholders_equity.setter
    def total_shareholders_equity(self, total_shareholders_equity):
        """Sets the total_shareholders_equity of this CreditsafeGlobalDataReportsBalanceSheet.


        :param total_shareholders_equity: The total_shareholders_equity of this CreditsafeGlobalDataReportsBalanceSheet.  # noqa: E501
        :type: float
        """

        self._total_shareholders_equity = total_shareholders_equity

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
        if issubclass(CreditsafeGlobalDataReportsBalanceSheet, dict):
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
        if not isinstance(other, CreditsafeGlobalDataReportsBalanceSheet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

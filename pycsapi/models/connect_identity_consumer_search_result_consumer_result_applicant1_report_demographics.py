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

class ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics(object):
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
        'cameo_code': 'str',
        'cameo_investor_code': 'str',
        'cameo_income_code': 'str',
        'cameo_unemployment_code': 'str',
        'cameo_property_code': 'str',
        'cameo_finance_code': 'str',
        'cameo_finance_group': 'str',
        'cameo_income_group': 'str',
        'cameo_investment_group': 'str',
        'cameo_group': 'str',
        'age_composition': 'ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsAgeComposition',
        'economic_activity_composition': 'ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsEconomicActivityComposition',
        'has_values': 'bool',
        'household_composition': 'ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsHouseholdComposition',
        'lifestage_composition': 'ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsLifestageComposition',
        'mortgage_composition': 'ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsMortgageComposition',
        'neighbourhood_definition': 'ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsNeighbourhoodDefinition',
        'occupation_composition': 'ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsOccupationComposition',
        'property_composition': 'ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition',
        'shareholder_composition': 'ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsShareholderComposition'
    }

    attribute_map = {
        'cameo_code': 'cameoCode',
        'cameo_investor_code': 'cameoInvestorCode',
        'cameo_income_code': 'cameoIncomeCode',
        'cameo_unemployment_code': 'cameoUnemploymentCode',
        'cameo_property_code': 'cameoPropertyCode',
        'cameo_finance_code': 'cameoFinanceCode',
        'cameo_finance_group': 'cameoFinanceGroup',
        'cameo_income_group': 'cameoIncomeGroup',
        'cameo_investment_group': 'cameoInvestmentGroup',
        'cameo_group': 'cameoGroup',
        'age_composition': 'ageComposition',
        'economic_activity_composition': 'economicActivityComposition',
        'has_values': 'hasValues',
        'household_composition': 'householdComposition',
        'lifestage_composition': 'lifestageComposition',
        'mortgage_composition': 'mortgageComposition',
        'neighbourhood_definition': 'neighbourhoodDefinition',
        'occupation_composition': 'occupationComposition',
        'property_composition': 'propertyComposition',
        'shareholder_composition': 'shareholderComposition'
    }

    def __init__(self, cameo_code=None, cameo_investor_code=None, cameo_income_code=None, cameo_unemployment_code=None, cameo_property_code=None, cameo_finance_code=None, cameo_finance_group=None, cameo_income_group=None, cameo_investment_group=None, cameo_group=None, age_composition=None, economic_activity_composition=None, has_values=None, household_composition=None, lifestage_composition=None, mortgage_composition=None, neighbourhood_definition=None, occupation_composition=None, property_composition=None, shareholder_composition=None):  # noqa: E501
        """ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics - a model defined in Swagger"""  # noqa: E501
        self._cameo_code = None
        self._cameo_investor_code = None
        self._cameo_income_code = None
        self._cameo_unemployment_code = None
        self._cameo_property_code = None
        self._cameo_finance_code = None
        self._cameo_finance_group = None
        self._cameo_income_group = None
        self._cameo_investment_group = None
        self._cameo_group = None
        self._age_composition = None
        self._economic_activity_composition = None
        self._has_values = None
        self._household_composition = None
        self._lifestage_composition = None
        self._mortgage_composition = None
        self._neighbourhood_definition = None
        self._occupation_composition = None
        self._property_composition = None
        self._shareholder_composition = None
        self.discriminator = None
        if cameo_code is not None:
            self.cameo_code = cameo_code
        if cameo_investor_code is not None:
            self.cameo_investor_code = cameo_investor_code
        if cameo_income_code is not None:
            self.cameo_income_code = cameo_income_code
        if cameo_unemployment_code is not None:
            self.cameo_unemployment_code = cameo_unemployment_code
        if cameo_property_code is not None:
            self.cameo_property_code = cameo_property_code
        if cameo_finance_code is not None:
            self.cameo_finance_code = cameo_finance_code
        if cameo_finance_group is not None:
            self.cameo_finance_group = cameo_finance_group
        if cameo_income_group is not None:
            self.cameo_income_group = cameo_income_group
        if cameo_investment_group is not None:
            self.cameo_investment_group = cameo_investment_group
        if cameo_group is not None:
            self.cameo_group = cameo_group
        if age_composition is not None:
            self.age_composition = age_composition
        if economic_activity_composition is not None:
            self.economic_activity_composition = economic_activity_composition
        if has_values is not None:
            self.has_values = has_values
        if household_composition is not None:
            self.household_composition = household_composition
        if lifestage_composition is not None:
            self.lifestage_composition = lifestage_composition
        if mortgage_composition is not None:
            self.mortgage_composition = mortgage_composition
        if neighbourhood_definition is not None:
            self.neighbourhood_definition = neighbourhood_definition
        if occupation_composition is not None:
            self.occupation_composition = occupation_composition
        if property_composition is not None:
            self.property_composition = property_composition
        if shareholder_composition is not None:
            self.shareholder_composition = shareholder_composition

    @property
    def cameo_code(self):
        """Gets the cameo_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501


        :return: The cameo_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :rtype: str
        """
        return self._cameo_code

    @cameo_code.setter
    def cameo_code(self, cameo_code):
        """Sets the cameo_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.


        :param cameo_code: The cameo_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :type: str
        """

        self._cameo_code = cameo_code

    @property
    def cameo_investor_code(self):
        """Gets the cameo_investor_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501


        :return: The cameo_investor_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :rtype: str
        """
        return self._cameo_investor_code

    @cameo_investor_code.setter
    def cameo_investor_code(self, cameo_investor_code):
        """Sets the cameo_investor_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.


        :param cameo_investor_code: The cameo_investor_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :type: str
        """

        self._cameo_investor_code = cameo_investor_code

    @property
    def cameo_income_code(self):
        """Gets the cameo_income_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501


        :return: The cameo_income_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :rtype: str
        """
        return self._cameo_income_code

    @cameo_income_code.setter
    def cameo_income_code(self, cameo_income_code):
        """Sets the cameo_income_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.


        :param cameo_income_code: The cameo_income_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :type: str
        """

        self._cameo_income_code = cameo_income_code

    @property
    def cameo_unemployment_code(self):
        """Gets the cameo_unemployment_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501


        :return: The cameo_unemployment_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :rtype: str
        """
        return self._cameo_unemployment_code

    @cameo_unemployment_code.setter
    def cameo_unemployment_code(self, cameo_unemployment_code):
        """Sets the cameo_unemployment_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.


        :param cameo_unemployment_code: The cameo_unemployment_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :type: str
        """

        self._cameo_unemployment_code = cameo_unemployment_code

    @property
    def cameo_property_code(self):
        """Gets the cameo_property_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501


        :return: The cameo_property_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :rtype: str
        """
        return self._cameo_property_code

    @cameo_property_code.setter
    def cameo_property_code(self, cameo_property_code):
        """Sets the cameo_property_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.


        :param cameo_property_code: The cameo_property_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :type: str
        """

        self._cameo_property_code = cameo_property_code

    @property
    def cameo_finance_code(self):
        """Gets the cameo_finance_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501


        :return: The cameo_finance_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :rtype: str
        """
        return self._cameo_finance_code

    @cameo_finance_code.setter
    def cameo_finance_code(self, cameo_finance_code):
        """Sets the cameo_finance_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.


        :param cameo_finance_code: The cameo_finance_code of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :type: str
        """

        self._cameo_finance_code = cameo_finance_code

    @property
    def cameo_finance_group(self):
        """Gets the cameo_finance_group of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501


        :return: The cameo_finance_group of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :rtype: str
        """
        return self._cameo_finance_group

    @cameo_finance_group.setter
    def cameo_finance_group(self, cameo_finance_group):
        """Sets the cameo_finance_group of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.


        :param cameo_finance_group: The cameo_finance_group of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :type: str
        """

        self._cameo_finance_group = cameo_finance_group

    @property
    def cameo_income_group(self):
        """Gets the cameo_income_group of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501


        :return: The cameo_income_group of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :rtype: str
        """
        return self._cameo_income_group

    @cameo_income_group.setter
    def cameo_income_group(self, cameo_income_group):
        """Sets the cameo_income_group of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.


        :param cameo_income_group: The cameo_income_group of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :type: str
        """

        self._cameo_income_group = cameo_income_group

    @property
    def cameo_investment_group(self):
        """Gets the cameo_investment_group of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501


        :return: The cameo_investment_group of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :rtype: str
        """
        return self._cameo_investment_group

    @cameo_investment_group.setter
    def cameo_investment_group(self, cameo_investment_group):
        """Sets the cameo_investment_group of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.


        :param cameo_investment_group: The cameo_investment_group of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :type: str
        """

        self._cameo_investment_group = cameo_investment_group

    @property
    def cameo_group(self):
        """Gets the cameo_group of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501


        :return: The cameo_group of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :rtype: str
        """
        return self._cameo_group

    @cameo_group.setter
    def cameo_group(self, cameo_group):
        """Sets the cameo_group of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.


        :param cameo_group: The cameo_group of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :type: str
        """

        self._cameo_group = cameo_group

    @property
    def age_composition(self):
        """Gets the age_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501


        :return: The age_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :rtype: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsAgeComposition
        """
        return self._age_composition

    @age_composition.setter
    def age_composition(self, age_composition):
        """Sets the age_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.


        :param age_composition: The age_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :type: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsAgeComposition
        """

        self._age_composition = age_composition

    @property
    def economic_activity_composition(self):
        """Gets the economic_activity_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501


        :return: The economic_activity_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :rtype: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsEconomicActivityComposition
        """
        return self._economic_activity_composition

    @economic_activity_composition.setter
    def economic_activity_composition(self, economic_activity_composition):
        """Sets the economic_activity_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.


        :param economic_activity_composition: The economic_activity_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :type: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsEconomicActivityComposition
        """

        self._economic_activity_composition = economic_activity_composition

    @property
    def has_values(self):
        """Gets the has_values of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501


        :return: The has_values of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :rtype: bool
        """
        return self._has_values

    @has_values.setter
    def has_values(self, has_values):
        """Sets the has_values of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.


        :param has_values: The has_values of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :type: bool
        """

        self._has_values = has_values

    @property
    def household_composition(self):
        """Gets the household_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501


        :return: The household_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :rtype: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsHouseholdComposition
        """
        return self._household_composition

    @household_composition.setter
    def household_composition(self, household_composition):
        """Sets the household_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.


        :param household_composition: The household_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :type: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsHouseholdComposition
        """

        self._household_composition = household_composition

    @property
    def lifestage_composition(self):
        """Gets the lifestage_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501


        :return: The lifestage_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :rtype: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsLifestageComposition
        """
        return self._lifestage_composition

    @lifestage_composition.setter
    def lifestage_composition(self, lifestage_composition):
        """Sets the lifestage_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.


        :param lifestage_composition: The lifestage_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :type: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsLifestageComposition
        """

        self._lifestage_composition = lifestage_composition

    @property
    def mortgage_composition(self):
        """Gets the mortgage_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501


        :return: The mortgage_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :rtype: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsMortgageComposition
        """
        return self._mortgage_composition

    @mortgage_composition.setter
    def mortgage_composition(self, mortgage_composition):
        """Sets the mortgage_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.


        :param mortgage_composition: The mortgage_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :type: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsMortgageComposition
        """

        self._mortgage_composition = mortgage_composition

    @property
    def neighbourhood_definition(self):
        """Gets the neighbourhood_definition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501


        :return: The neighbourhood_definition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :rtype: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsNeighbourhoodDefinition
        """
        return self._neighbourhood_definition

    @neighbourhood_definition.setter
    def neighbourhood_definition(self, neighbourhood_definition):
        """Sets the neighbourhood_definition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.


        :param neighbourhood_definition: The neighbourhood_definition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :type: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsNeighbourhoodDefinition
        """

        self._neighbourhood_definition = neighbourhood_definition

    @property
    def occupation_composition(self):
        """Gets the occupation_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501


        :return: The occupation_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :rtype: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsOccupationComposition
        """
        return self._occupation_composition

    @occupation_composition.setter
    def occupation_composition(self, occupation_composition):
        """Sets the occupation_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.


        :param occupation_composition: The occupation_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :type: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsOccupationComposition
        """

        self._occupation_composition = occupation_composition

    @property
    def property_composition(self):
        """Gets the property_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501


        :return: The property_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :rtype: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition
        """
        return self._property_composition

    @property_composition.setter
    def property_composition(self, property_composition):
        """Sets the property_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.


        :param property_composition: The property_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :type: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition
        """

        self._property_composition = property_composition

    @property
    def shareholder_composition(self):
        """Gets the shareholder_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501


        :return: The shareholder_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :rtype: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsShareholderComposition
        """
        return self._shareholder_composition

    @shareholder_composition.setter
    def shareholder_composition(self, shareholder_composition):
        """Sets the shareholder_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.


        :param shareholder_composition: The shareholder_composition of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics.  # noqa: E501
        :type: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsShareholderComposition
        """

        self._shareholder_composition = shareholder_composition

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
        if issubclass(ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics, dict):
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
        if not isinstance(other, ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

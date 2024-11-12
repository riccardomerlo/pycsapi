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

class ConnectIdentityDemographicsNeighbourhoodDefinition(object):
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
        'finance_group': 'str',
        'finance_group_household_perc': 'str',
        'income': 'str',
        'income_group': 'str',
        'investor_household_perc': 'str',
        'investor_index': 'str',
        'risk_factor': 'str',
        'uk': 'str',
        'uk_group': 'str',
        'uk_household_perc': 'str',
        'description': 'str'
    }

    attribute_map = {
        'finance_group': 'financeGroup',
        'finance_group_household_perc': 'financeGroupHouseholdPerc',
        'income': 'income',
        'income_group': 'incomeGroup',
        'investor_household_perc': 'investorHouseholdPerc',
        'investor_index': 'investorIndex',
        'risk_factor': 'riskFactor',
        'uk': 'uk',
        'uk_group': 'ukGroup',
        'uk_household_perc': 'ukHouseholdPerc',
        'description': 'description'
    }

    def __init__(self, finance_group=None, finance_group_household_perc=None, income=None, income_group=None, investor_household_perc=None, investor_index=None, risk_factor=None, uk=None, uk_group=None, uk_household_perc=None, description=None):  # noqa: E501
        """ConnectIdentityDemographicsNeighbourhoodDefinition - a model defined in Swagger"""  # noqa: E501
        self._finance_group = None
        self._finance_group_household_perc = None
        self._income = None
        self._income_group = None
        self._investor_household_perc = None
        self._investor_index = None
        self._risk_factor = None
        self._uk = None
        self._uk_group = None
        self._uk_household_perc = None
        self._description = None
        self.discriminator = None
        if finance_group is not None:
            self.finance_group = finance_group
        if finance_group_household_perc is not None:
            self.finance_group_household_perc = finance_group_household_perc
        if income is not None:
            self.income = income
        if income_group is not None:
            self.income_group = income_group
        if investor_household_perc is not None:
            self.investor_household_perc = investor_household_perc
        if investor_index is not None:
            self.investor_index = investor_index
        if risk_factor is not None:
            self.risk_factor = risk_factor
        if uk is not None:
            self.uk = uk
        if uk_group is not None:
            self.uk_group = uk_group
        if uk_household_perc is not None:
            self.uk_household_perc = uk_household_perc
        if description is not None:
            self.description = description

    @property
    def finance_group(self):
        """Gets the finance_group of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501


        :return: The finance_group of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :rtype: str
        """
        return self._finance_group

    @finance_group.setter
    def finance_group(self, finance_group):
        """Sets the finance_group of this ConnectIdentityDemographicsNeighbourhoodDefinition.


        :param finance_group: The finance_group of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :type: str
        """

        self._finance_group = finance_group

    @property
    def finance_group_household_perc(self):
        """Gets the finance_group_household_perc of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501


        :return: The finance_group_household_perc of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :rtype: str
        """
        return self._finance_group_household_perc

    @finance_group_household_perc.setter
    def finance_group_household_perc(self, finance_group_household_perc):
        """Sets the finance_group_household_perc of this ConnectIdentityDemographicsNeighbourhoodDefinition.


        :param finance_group_household_perc: The finance_group_household_perc of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :type: str
        """

        self._finance_group_household_perc = finance_group_household_perc

    @property
    def income(self):
        """Gets the income of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501


        :return: The income of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :rtype: str
        """
        return self._income

    @income.setter
    def income(self, income):
        """Sets the income of this ConnectIdentityDemographicsNeighbourhoodDefinition.


        :param income: The income of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :type: str
        """

        self._income = income

    @property
    def income_group(self):
        """Gets the income_group of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501


        :return: The income_group of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :rtype: str
        """
        return self._income_group

    @income_group.setter
    def income_group(self, income_group):
        """Sets the income_group of this ConnectIdentityDemographicsNeighbourhoodDefinition.


        :param income_group: The income_group of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :type: str
        """

        self._income_group = income_group

    @property
    def investor_household_perc(self):
        """Gets the investor_household_perc of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501


        :return: The investor_household_perc of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :rtype: str
        """
        return self._investor_household_perc

    @investor_household_perc.setter
    def investor_household_perc(self, investor_household_perc):
        """Sets the investor_household_perc of this ConnectIdentityDemographicsNeighbourhoodDefinition.


        :param investor_household_perc: The investor_household_perc of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :type: str
        """

        self._investor_household_perc = investor_household_perc

    @property
    def investor_index(self):
        """Gets the investor_index of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501


        :return: The investor_index of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :rtype: str
        """
        return self._investor_index

    @investor_index.setter
    def investor_index(self, investor_index):
        """Sets the investor_index of this ConnectIdentityDemographicsNeighbourhoodDefinition.


        :param investor_index: The investor_index of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :type: str
        """

        self._investor_index = investor_index

    @property
    def risk_factor(self):
        """Gets the risk_factor of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501


        :return: The risk_factor of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :rtype: str
        """
        return self._risk_factor

    @risk_factor.setter
    def risk_factor(self, risk_factor):
        """Sets the risk_factor of this ConnectIdentityDemographicsNeighbourhoodDefinition.


        :param risk_factor: The risk_factor of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :type: str
        """

        self._risk_factor = risk_factor

    @property
    def uk(self):
        """Gets the uk of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501


        :return: The uk of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :rtype: str
        """
        return self._uk

    @uk.setter
    def uk(self, uk):
        """Sets the uk of this ConnectIdentityDemographicsNeighbourhoodDefinition.


        :param uk: The uk of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :type: str
        """

        self._uk = uk

    @property
    def uk_group(self):
        """Gets the uk_group of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501


        :return: The uk_group of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :rtype: str
        """
        return self._uk_group

    @uk_group.setter
    def uk_group(self, uk_group):
        """Sets the uk_group of this ConnectIdentityDemographicsNeighbourhoodDefinition.


        :param uk_group: The uk_group of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :type: str
        """

        self._uk_group = uk_group

    @property
    def uk_household_perc(self):
        """Gets the uk_household_perc of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501


        :return: The uk_household_perc of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :rtype: str
        """
        return self._uk_household_perc

    @uk_household_perc.setter
    def uk_household_perc(self, uk_household_perc):
        """Sets the uk_household_perc of this ConnectIdentityDemographicsNeighbourhoodDefinition.


        :param uk_household_perc: The uk_household_perc of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :type: str
        """

        self._uk_household_perc = uk_household_perc

    @property
    def description(self):
        """Gets the description of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501


        :return: The description of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConnectIdentityDemographicsNeighbourhoodDefinition.


        :param description: The description of this ConnectIdentityDemographicsNeighbourhoodDefinition.  # noqa: E501
        :type: str
        """

        self._description = description

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
        if issubclass(ConnectIdentityDemographicsNeighbourhoodDefinition, dict):
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
        if not isinstance(other, ConnectIdentityDemographicsNeighbourhoodDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

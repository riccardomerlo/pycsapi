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

class ConnectIdentityDemographicsShareholderComposition(object):
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
        'average_investments': 'str',
        'average_investments_description': 'str',
        'average_investments_label': 'str',
        'average_shareholders': 'str',
        'average_shareholders_description': 'str',
        'average_shareholders_label': 'str',
        'average_shares': 'str',
        'average_shares_description': 'str',
        'average_shares_label': 'str',
        'average_value': 'str',
        'average_value_description': 'str',
        'average_value_label': 'str',
        'proportion_of_households_with_shares': 'str',
        'proportion_of_households_with_shares_description': 'str',
        'proportion_of_households_with_shares_label': 'str'
    }

    attribute_map = {
        'average_investments': 'averageInvestments',
        'average_investments_description': 'averageInvestmentsDescription',
        'average_investments_label': 'averageInvestmentsLabel',
        'average_shareholders': 'averageShareholders',
        'average_shareholders_description': 'averageShareholdersDescription',
        'average_shareholders_label': 'averageShareholdersLabel',
        'average_shares': 'averageShares',
        'average_shares_description': 'averageSharesDescription',
        'average_shares_label': 'averageSharesLabel',
        'average_value': 'averageValue',
        'average_value_description': 'averageValueDescription',
        'average_value_label': 'averageValueLabel',
        'proportion_of_households_with_shares': 'proportionOfHouseholdsWithShares',
        'proportion_of_households_with_shares_description': 'proportionOfHouseholdsWithSharesDescription',
        'proportion_of_households_with_shares_label': 'proportionOfHouseholdsWithSharesLabel'
    }

    def __init__(self, average_investments=None, average_investments_description=None, average_investments_label=None, average_shareholders=None, average_shareholders_description=None, average_shareholders_label=None, average_shares=None, average_shares_description=None, average_shares_label=None, average_value=None, average_value_description=None, average_value_label=None, proportion_of_households_with_shares=None, proportion_of_households_with_shares_description=None, proportion_of_households_with_shares_label=None):  # noqa: E501
        """ConnectIdentityDemographicsShareholderComposition - a model defined in Swagger"""  # noqa: E501
        self._average_investments = None
        self._average_investments_description = None
        self._average_investments_label = None
        self._average_shareholders = None
        self._average_shareholders_description = None
        self._average_shareholders_label = None
        self._average_shares = None
        self._average_shares_description = None
        self._average_shares_label = None
        self._average_value = None
        self._average_value_description = None
        self._average_value_label = None
        self._proportion_of_households_with_shares = None
        self._proportion_of_households_with_shares_description = None
        self._proportion_of_households_with_shares_label = None
        self.discriminator = None
        if average_investments is not None:
            self.average_investments = average_investments
        if average_investments_description is not None:
            self.average_investments_description = average_investments_description
        if average_investments_label is not None:
            self.average_investments_label = average_investments_label
        if average_shareholders is not None:
            self.average_shareholders = average_shareholders
        if average_shareholders_description is not None:
            self.average_shareholders_description = average_shareholders_description
        if average_shareholders_label is not None:
            self.average_shareholders_label = average_shareholders_label
        if average_shares is not None:
            self.average_shares = average_shares
        if average_shares_description is not None:
            self.average_shares_description = average_shares_description
        if average_shares_label is not None:
            self.average_shares_label = average_shares_label
        if average_value is not None:
            self.average_value = average_value
        if average_value_description is not None:
            self.average_value_description = average_value_description
        if average_value_label is not None:
            self.average_value_label = average_value_label
        if proportion_of_households_with_shares is not None:
            self.proportion_of_households_with_shares = proportion_of_households_with_shares
        if proportion_of_households_with_shares_description is not None:
            self.proportion_of_households_with_shares_description = proportion_of_households_with_shares_description
        if proportion_of_households_with_shares_label is not None:
            self.proportion_of_households_with_shares_label = proportion_of_households_with_shares_label

    @property
    def average_investments(self):
        """Gets the average_investments of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501


        :return: The average_investments of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :rtype: str
        """
        return self._average_investments

    @average_investments.setter
    def average_investments(self, average_investments):
        """Sets the average_investments of this ConnectIdentityDemographicsShareholderComposition.


        :param average_investments: The average_investments of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :type: str
        """

        self._average_investments = average_investments

    @property
    def average_investments_description(self):
        """Gets the average_investments_description of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501


        :return: The average_investments_description of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :rtype: str
        """
        return self._average_investments_description

    @average_investments_description.setter
    def average_investments_description(self, average_investments_description):
        """Sets the average_investments_description of this ConnectIdentityDemographicsShareholderComposition.


        :param average_investments_description: The average_investments_description of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :type: str
        """

        self._average_investments_description = average_investments_description

    @property
    def average_investments_label(self):
        """Gets the average_investments_label of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501


        :return: The average_investments_label of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :rtype: str
        """
        return self._average_investments_label

    @average_investments_label.setter
    def average_investments_label(self, average_investments_label):
        """Sets the average_investments_label of this ConnectIdentityDemographicsShareholderComposition.


        :param average_investments_label: The average_investments_label of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :type: str
        """

        self._average_investments_label = average_investments_label

    @property
    def average_shareholders(self):
        """Gets the average_shareholders of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501


        :return: The average_shareholders of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :rtype: str
        """
        return self._average_shareholders

    @average_shareholders.setter
    def average_shareholders(self, average_shareholders):
        """Sets the average_shareholders of this ConnectIdentityDemographicsShareholderComposition.


        :param average_shareholders: The average_shareholders of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :type: str
        """

        self._average_shareholders = average_shareholders

    @property
    def average_shareholders_description(self):
        """Gets the average_shareholders_description of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501


        :return: The average_shareholders_description of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :rtype: str
        """
        return self._average_shareholders_description

    @average_shareholders_description.setter
    def average_shareholders_description(self, average_shareholders_description):
        """Sets the average_shareholders_description of this ConnectIdentityDemographicsShareholderComposition.


        :param average_shareholders_description: The average_shareholders_description of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :type: str
        """

        self._average_shareholders_description = average_shareholders_description

    @property
    def average_shareholders_label(self):
        """Gets the average_shareholders_label of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501


        :return: The average_shareholders_label of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :rtype: str
        """
        return self._average_shareholders_label

    @average_shareholders_label.setter
    def average_shareholders_label(self, average_shareholders_label):
        """Sets the average_shareholders_label of this ConnectIdentityDemographicsShareholderComposition.


        :param average_shareholders_label: The average_shareholders_label of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :type: str
        """

        self._average_shareholders_label = average_shareholders_label

    @property
    def average_shares(self):
        """Gets the average_shares of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501


        :return: The average_shares of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :rtype: str
        """
        return self._average_shares

    @average_shares.setter
    def average_shares(self, average_shares):
        """Sets the average_shares of this ConnectIdentityDemographicsShareholderComposition.


        :param average_shares: The average_shares of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :type: str
        """

        self._average_shares = average_shares

    @property
    def average_shares_description(self):
        """Gets the average_shares_description of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501


        :return: The average_shares_description of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :rtype: str
        """
        return self._average_shares_description

    @average_shares_description.setter
    def average_shares_description(self, average_shares_description):
        """Sets the average_shares_description of this ConnectIdentityDemographicsShareholderComposition.


        :param average_shares_description: The average_shares_description of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :type: str
        """

        self._average_shares_description = average_shares_description

    @property
    def average_shares_label(self):
        """Gets the average_shares_label of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501


        :return: The average_shares_label of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :rtype: str
        """
        return self._average_shares_label

    @average_shares_label.setter
    def average_shares_label(self, average_shares_label):
        """Sets the average_shares_label of this ConnectIdentityDemographicsShareholderComposition.


        :param average_shares_label: The average_shares_label of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :type: str
        """

        self._average_shares_label = average_shares_label

    @property
    def average_value(self):
        """Gets the average_value of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501


        :return: The average_value of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :rtype: str
        """
        return self._average_value

    @average_value.setter
    def average_value(self, average_value):
        """Sets the average_value of this ConnectIdentityDemographicsShareholderComposition.


        :param average_value: The average_value of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :type: str
        """

        self._average_value = average_value

    @property
    def average_value_description(self):
        """Gets the average_value_description of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501


        :return: The average_value_description of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :rtype: str
        """
        return self._average_value_description

    @average_value_description.setter
    def average_value_description(self, average_value_description):
        """Sets the average_value_description of this ConnectIdentityDemographicsShareholderComposition.


        :param average_value_description: The average_value_description of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :type: str
        """

        self._average_value_description = average_value_description

    @property
    def average_value_label(self):
        """Gets the average_value_label of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501


        :return: The average_value_label of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :rtype: str
        """
        return self._average_value_label

    @average_value_label.setter
    def average_value_label(self, average_value_label):
        """Sets the average_value_label of this ConnectIdentityDemographicsShareholderComposition.


        :param average_value_label: The average_value_label of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :type: str
        """

        self._average_value_label = average_value_label

    @property
    def proportion_of_households_with_shares(self):
        """Gets the proportion_of_households_with_shares of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501


        :return: The proportion_of_households_with_shares of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :rtype: str
        """
        return self._proportion_of_households_with_shares

    @proportion_of_households_with_shares.setter
    def proportion_of_households_with_shares(self, proportion_of_households_with_shares):
        """Sets the proportion_of_households_with_shares of this ConnectIdentityDemographicsShareholderComposition.


        :param proportion_of_households_with_shares: The proportion_of_households_with_shares of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :type: str
        """

        self._proportion_of_households_with_shares = proportion_of_households_with_shares

    @property
    def proportion_of_households_with_shares_description(self):
        """Gets the proportion_of_households_with_shares_description of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501


        :return: The proportion_of_households_with_shares_description of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :rtype: str
        """
        return self._proportion_of_households_with_shares_description

    @proportion_of_households_with_shares_description.setter
    def proportion_of_households_with_shares_description(self, proportion_of_households_with_shares_description):
        """Sets the proportion_of_households_with_shares_description of this ConnectIdentityDemographicsShareholderComposition.


        :param proportion_of_households_with_shares_description: The proportion_of_households_with_shares_description of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :type: str
        """

        self._proportion_of_households_with_shares_description = proportion_of_households_with_shares_description

    @property
    def proportion_of_households_with_shares_label(self):
        """Gets the proportion_of_households_with_shares_label of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501


        :return: The proportion_of_households_with_shares_label of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :rtype: str
        """
        return self._proportion_of_households_with_shares_label

    @proportion_of_households_with_shares_label.setter
    def proportion_of_households_with_shares_label(self, proportion_of_households_with_shares_label):
        """Sets the proportion_of_households_with_shares_label of this ConnectIdentityDemographicsShareholderComposition.


        :param proportion_of_households_with_shares_label: The proportion_of_households_with_shares_label of this ConnectIdentityDemographicsShareholderComposition.  # noqa: E501
        :type: str
        """

        self._proportion_of_households_with_shares_label = proportion_of_households_with_shares_label

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
        if issubclass(ConnectIdentityDemographicsShareholderComposition, dict):
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
        if not isinstance(other, ConnectIdentityDemographicsShareholderComposition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

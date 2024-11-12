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

class CreditsafeGlobalDataReportsShareClass(object):
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
        'share_type': 'str',
        'currency': 'CreditsafeGlobalDataCurrency',
        'value_per_share': 'float',
        'jointly_owned': 'bool',
        'number_of_shares_owned': 'int',
        'value_of_shares_owned': 'float',
        'additional_data': 'CreditsafeGlobalDataReportsShareClassAdditionalData'
    }

    attribute_map = {
        'share_type': 'shareType',
        'currency': 'currency',
        'value_per_share': 'valuePerShare',
        'jointly_owned': 'jointlyOwned',
        'number_of_shares_owned': 'numberOfSharesOwned',
        'value_of_shares_owned': 'valueOfSharesOwned',
        'additional_data': 'additionalData'
    }

    def __init__(self, share_type=None, currency=None, value_per_share=None, jointly_owned=None, number_of_shares_owned=None, value_of_shares_owned=None, additional_data=None):  # noqa: E501
        """CreditsafeGlobalDataReportsShareClass - a model defined in Swagger"""  # noqa: E501
        self._share_type = None
        self._currency = None
        self._value_per_share = None
        self._jointly_owned = None
        self._number_of_shares_owned = None
        self._value_of_shares_owned = None
        self._additional_data = None
        self.discriminator = None
        if share_type is not None:
            self.share_type = share_type
        if currency is not None:
            self.currency = currency
        if value_per_share is not None:
            self.value_per_share = value_per_share
        if jointly_owned is not None:
            self.jointly_owned = jointly_owned
        if number_of_shares_owned is not None:
            self.number_of_shares_owned = number_of_shares_owned
        if value_of_shares_owned is not None:
            self.value_of_shares_owned = value_of_shares_owned
        if additional_data is not None:
            self.additional_data = additional_data

    @property
    def share_type(self):
        """Gets the share_type of this CreditsafeGlobalDataReportsShareClass.  # noqa: E501


        :return: The share_type of this CreditsafeGlobalDataReportsShareClass.  # noqa: E501
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """Sets the share_type of this CreditsafeGlobalDataReportsShareClass.


        :param share_type: The share_type of this CreditsafeGlobalDataReportsShareClass.  # noqa: E501
        :type: str
        """

        self._share_type = share_type

    @property
    def currency(self):
        """Gets the currency of this CreditsafeGlobalDataReportsShareClass.  # noqa: E501


        :return: The currency of this CreditsafeGlobalDataReportsShareClass.  # noqa: E501
        :rtype: CreditsafeGlobalDataCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CreditsafeGlobalDataReportsShareClass.


        :param currency: The currency of this CreditsafeGlobalDataReportsShareClass.  # noqa: E501
        :type: CreditsafeGlobalDataCurrency
        """

        self._currency = currency

    @property
    def value_per_share(self):
        """Gets the value_per_share of this CreditsafeGlobalDataReportsShareClass.  # noqa: E501


        :return: The value_per_share of this CreditsafeGlobalDataReportsShareClass.  # noqa: E501
        :rtype: float
        """
        return self._value_per_share

    @value_per_share.setter
    def value_per_share(self, value_per_share):
        """Sets the value_per_share of this CreditsafeGlobalDataReportsShareClass.


        :param value_per_share: The value_per_share of this CreditsafeGlobalDataReportsShareClass.  # noqa: E501
        :type: float
        """

        self._value_per_share = value_per_share

    @property
    def jointly_owned(self):
        """Gets the jointly_owned of this CreditsafeGlobalDataReportsShareClass.  # noqa: E501


        :return: The jointly_owned of this CreditsafeGlobalDataReportsShareClass.  # noqa: E501
        :rtype: bool
        """
        return self._jointly_owned

    @jointly_owned.setter
    def jointly_owned(self, jointly_owned):
        """Sets the jointly_owned of this CreditsafeGlobalDataReportsShareClass.


        :param jointly_owned: The jointly_owned of this CreditsafeGlobalDataReportsShareClass.  # noqa: E501
        :type: bool
        """

        self._jointly_owned = jointly_owned

    @property
    def number_of_shares_owned(self):
        """Gets the number_of_shares_owned of this CreditsafeGlobalDataReportsShareClass.  # noqa: E501


        :return: The number_of_shares_owned of this CreditsafeGlobalDataReportsShareClass.  # noqa: E501
        :rtype: int
        """
        return self._number_of_shares_owned

    @number_of_shares_owned.setter
    def number_of_shares_owned(self, number_of_shares_owned):
        """Sets the number_of_shares_owned of this CreditsafeGlobalDataReportsShareClass.


        :param number_of_shares_owned: The number_of_shares_owned of this CreditsafeGlobalDataReportsShareClass.  # noqa: E501
        :type: int
        """

        self._number_of_shares_owned = number_of_shares_owned

    @property
    def value_of_shares_owned(self):
        """Gets the value_of_shares_owned of this CreditsafeGlobalDataReportsShareClass.  # noqa: E501


        :return: The value_of_shares_owned of this CreditsafeGlobalDataReportsShareClass.  # noqa: E501
        :rtype: float
        """
        return self._value_of_shares_owned

    @value_of_shares_owned.setter
    def value_of_shares_owned(self, value_of_shares_owned):
        """Sets the value_of_shares_owned of this CreditsafeGlobalDataReportsShareClass.


        :param value_of_shares_owned: The value_of_shares_owned of this CreditsafeGlobalDataReportsShareClass.  # noqa: E501
        :type: float
        """

        self._value_of_shares_owned = value_of_shares_owned

    @property
    def additional_data(self):
        """Gets the additional_data of this CreditsafeGlobalDataReportsShareClass.  # noqa: E501


        :return: The additional_data of this CreditsafeGlobalDataReportsShareClass.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsShareClassAdditionalData
        """
        return self._additional_data

    @additional_data.setter
    def additional_data(self, additional_data):
        """Sets the additional_data of this CreditsafeGlobalDataReportsShareClass.


        :param additional_data: The additional_data of this CreditsafeGlobalDataReportsShareClass.  # noqa: E501
        :type: CreditsafeGlobalDataReportsShareClassAdditionalData
        """

        self._additional_data = additional_data

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
        if issubclass(CreditsafeGlobalDataReportsShareClass, dict):
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
        if not isinstance(other, CreditsafeGlobalDataReportsShareClass):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

class CreditsafeGlobalDataReportsLtdContactInformation(object):
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
        'main_address': 'CreditsafeGlobalDataAddressDataReport',
        'other_addresses': 'list[CreditsafeGlobalDataAddressDataReport]',
        'previous_addresses': 'list[CreditsafeGlobalDataAddressDataReport]',
        'email_addresses': 'list[str]',
        'websites': 'list[str]'
    }

    attribute_map = {
        'main_address': 'mainAddress',
        'other_addresses': 'otherAddresses',
        'previous_addresses': 'previousAddresses',
        'email_addresses': 'emailAddresses',
        'websites': 'websites'
    }

    def __init__(self, main_address=None, other_addresses=None, previous_addresses=None, email_addresses=None, websites=None):  # noqa: E501
        """CreditsafeGlobalDataReportsLtdContactInformation - a model defined in Swagger"""  # noqa: E501
        self._main_address = None
        self._other_addresses = None
        self._previous_addresses = None
        self._email_addresses = None
        self._websites = None
        self.discriminator = None
        if main_address is not None:
            self.main_address = main_address
        if other_addresses is not None:
            self.other_addresses = other_addresses
        if previous_addresses is not None:
            self.previous_addresses = previous_addresses
        if email_addresses is not None:
            self.email_addresses = email_addresses
        if websites is not None:
            self.websites = websites

    @property
    def main_address(self):
        """Gets the main_address of this CreditsafeGlobalDataReportsLtdContactInformation.  # noqa: E501


        :return: The main_address of this CreditsafeGlobalDataReportsLtdContactInformation.  # noqa: E501
        :rtype: CreditsafeGlobalDataAddressDataReport
        """
        return self._main_address

    @main_address.setter
    def main_address(self, main_address):
        """Sets the main_address of this CreditsafeGlobalDataReportsLtdContactInformation.


        :param main_address: The main_address of this CreditsafeGlobalDataReportsLtdContactInformation.  # noqa: E501
        :type: CreditsafeGlobalDataAddressDataReport
        """

        self._main_address = main_address

    @property
    def other_addresses(self):
        """Gets the other_addresses of this CreditsafeGlobalDataReportsLtdContactInformation.  # noqa: E501


        :return: The other_addresses of this CreditsafeGlobalDataReportsLtdContactInformation.  # noqa: E501
        :rtype: list[CreditsafeGlobalDataAddressDataReport]
        """
        return self._other_addresses

    @other_addresses.setter
    def other_addresses(self, other_addresses):
        """Sets the other_addresses of this CreditsafeGlobalDataReportsLtdContactInformation.


        :param other_addresses: The other_addresses of this CreditsafeGlobalDataReportsLtdContactInformation.  # noqa: E501
        :type: list[CreditsafeGlobalDataAddressDataReport]
        """

        self._other_addresses = other_addresses

    @property
    def previous_addresses(self):
        """Gets the previous_addresses of this CreditsafeGlobalDataReportsLtdContactInformation.  # noqa: E501


        :return: The previous_addresses of this CreditsafeGlobalDataReportsLtdContactInformation.  # noqa: E501
        :rtype: list[CreditsafeGlobalDataAddressDataReport]
        """
        return self._previous_addresses

    @previous_addresses.setter
    def previous_addresses(self, previous_addresses):
        """Sets the previous_addresses of this CreditsafeGlobalDataReportsLtdContactInformation.


        :param previous_addresses: The previous_addresses of this CreditsafeGlobalDataReportsLtdContactInformation.  # noqa: E501
        :type: list[CreditsafeGlobalDataAddressDataReport]
        """

        self._previous_addresses = previous_addresses

    @property
    def email_addresses(self):
        """Gets the email_addresses of this CreditsafeGlobalDataReportsLtdContactInformation.  # noqa: E501


        :return: The email_addresses of this CreditsafeGlobalDataReportsLtdContactInformation.  # noqa: E501
        :rtype: list[str]
        """
        return self._email_addresses

    @email_addresses.setter
    def email_addresses(self, email_addresses):
        """Sets the email_addresses of this CreditsafeGlobalDataReportsLtdContactInformation.


        :param email_addresses: The email_addresses of this CreditsafeGlobalDataReportsLtdContactInformation.  # noqa: E501
        :type: list[str]
        """

        self._email_addresses = email_addresses

    @property
    def websites(self):
        """Gets the websites of this CreditsafeGlobalDataReportsLtdContactInformation.  # noqa: E501


        :return: The websites of this CreditsafeGlobalDataReportsLtdContactInformation.  # noqa: E501
        :rtype: list[str]
        """
        return self._websites

    @websites.setter
    def websites(self, websites):
        """Sets the websites of this CreditsafeGlobalDataReportsLtdContactInformation.


        :param websites: The websites of this CreditsafeGlobalDataReportsLtdContactInformation.  # noqa: E501
        :type: list[str]
        """

        self._websites = websites

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
        if issubclass(CreditsafeGlobalDataReportsLtdContactInformation, dict):
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
        if not isinstance(other, CreditsafeGlobalDataReportsLtdContactInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

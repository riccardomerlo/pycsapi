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

class ConnectIdentityReportAddress(object):
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
        'address': 'str',
        'is_current': 'bool',
        'is_paf': 'bool',
        'residents': 'list[ConnectIdentityReportResident]',
        'other_residents': 'bool',
        'electoral_roll_history': 'list[ConnectIdentityReportElectoralRollHistory]',
        'undeclared_address_type': 'str'
    }

    attribute_map = {
        'address': 'address',
        'is_current': 'isCurrent',
        'is_paf': 'isPaf',
        'residents': 'residents',
        'other_residents': 'otherResidents',
        'electoral_roll_history': 'electoralRollHistory',
        'undeclared_address_type': 'undeclaredAddressType'
    }

    def __init__(self, address=None, is_current=None, is_paf=None, residents=None, other_residents=None, electoral_roll_history=None, undeclared_address_type=None):  # noqa: E501
        """ConnectIdentityReportAddress - a model defined in Swagger"""  # noqa: E501
        self._address = None
        self._is_current = None
        self._is_paf = None
        self._residents = None
        self._other_residents = None
        self._electoral_roll_history = None
        self._undeclared_address_type = None
        self.discriminator = None
        if address is not None:
            self.address = address
        if is_current is not None:
            self.is_current = is_current
        if is_paf is not None:
            self.is_paf = is_paf
        if residents is not None:
            self.residents = residents
        if other_residents is not None:
            self.other_residents = other_residents
        if electoral_roll_history is not None:
            self.electoral_roll_history = electoral_roll_history
        if undeclared_address_type is not None:
            self.undeclared_address_type = undeclared_address_type

    @property
    def address(self):
        """Gets the address of this ConnectIdentityReportAddress.  # noqa: E501


        :return: The address of this ConnectIdentityReportAddress.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ConnectIdentityReportAddress.


        :param address: The address of this ConnectIdentityReportAddress.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def is_current(self):
        """Gets the is_current of this ConnectIdentityReportAddress.  # noqa: E501


        :return: The is_current of this ConnectIdentityReportAddress.  # noqa: E501
        :rtype: bool
        """
        return self._is_current

    @is_current.setter
    def is_current(self, is_current):
        """Sets the is_current of this ConnectIdentityReportAddress.


        :param is_current: The is_current of this ConnectIdentityReportAddress.  # noqa: E501
        :type: bool
        """

        self._is_current = is_current

    @property
    def is_paf(self):
        """Gets the is_paf of this ConnectIdentityReportAddress.  # noqa: E501


        :return: The is_paf of this ConnectIdentityReportAddress.  # noqa: E501
        :rtype: bool
        """
        return self._is_paf

    @is_paf.setter
    def is_paf(self, is_paf):
        """Sets the is_paf of this ConnectIdentityReportAddress.


        :param is_paf: The is_paf of this ConnectIdentityReportAddress.  # noqa: E501
        :type: bool
        """

        self._is_paf = is_paf

    @property
    def residents(self):
        """Gets the residents of this ConnectIdentityReportAddress.  # noqa: E501


        :return: The residents of this ConnectIdentityReportAddress.  # noqa: E501
        :rtype: list[ConnectIdentityReportResident]
        """
        return self._residents

    @residents.setter
    def residents(self, residents):
        """Sets the residents of this ConnectIdentityReportAddress.


        :param residents: The residents of this ConnectIdentityReportAddress.  # noqa: E501
        :type: list[ConnectIdentityReportResident]
        """

        self._residents = residents

    @property
    def other_residents(self):
        """Gets the other_residents of this ConnectIdentityReportAddress.  # noqa: E501


        :return: The other_residents of this ConnectIdentityReportAddress.  # noqa: E501
        :rtype: bool
        """
        return self._other_residents

    @other_residents.setter
    def other_residents(self, other_residents):
        """Sets the other_residents of this ConnectIdentityReportAddress.


        :param other_residents: The other_residents of this ConnectIdentityReportAddress.  # noqa: E501
        :type: bool
        """

        self._other_residents = other_residents

    @property
    def electoral_roll_history(self):
        """Gets the electoral_roll_history of this ConnectIdentityReportAddress.  # noqa: E501


        :return: The electoral_roll_history of this ConnectIdentityReportAddress.  # noqa: E501
        :rtype: list[ConnectIdentityReportElectoralRollHistory]
        """
        return self._electoral_roll_history

    @electoral_roll_history.setter
    def electoral_roll_history(self, electoral_roll_history):
        """Sets the electoral_roll_history of this ConnectIdentityReportAddress.


        :param electoral_roll_history: The electoral_roll_history of this ConnectIdentityReportAddress.  # noqa: E501
        :type: list[ConnectIdentityReportElectoralRollHistory]
        """

        self._electoral_roll_history = electoral_roll_history

    @property
    def undeclared_address_type(self):
        """Gets the undeclared_address_type of this ConnectIdentityReportAddress.  # noqa: E501


        :return: The undeclared_address_type of this ConnectIdentityReportAddress.  # noqa: E501
        :rtype: str
        """
        return self._undeclared_address_type

    @undeclared_address_type.setter
    def undeclared_address_type(self, undeclared_address_type):
        """Sets the undeclared_address_type of this ConnectIdentityReportAddress.


        :param undeclared_address_type: The undeclared_address_type of this ConnectIdentityReportAddress.  # noqa: E501
        :type: str
        """

        self._undeclared_address_type = undeclared_address_type

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
        if issubclass(ConnectIdentityReportAddress, dict):
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
        if not isinstance(other, ConnectIdentityReportAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

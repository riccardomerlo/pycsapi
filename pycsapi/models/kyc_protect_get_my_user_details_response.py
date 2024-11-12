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

class KycProtectGetMyUserDetailsResponse(object):
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
        'username': 'str',
        'email_address': 'str',
        'owning_entity': 'str',
        'default_language': 'str',
        'primary_contact': 'KycProtectGetMyUserDetailsResponsePrimaryContact',
        'ietf_language': 'str',
        'country_code': 'str',
        'is_active': 'str',
        'correlation_id': 'str'
    }

    attribute_map = {
        'username': 'username',
        'email_address': 'emailAddress',
        'owning_entity': 'owningEntity',
        'default_language': 'defaultLanguage',
        'primary_contact': 'primaryContact',
        'ietf_language': 'ietfLanguage',
        'country_code': 'countryCode',
        'is_active': 'isActive',
        'correlation_id': 'correlationId'
    }

    def __init__(self, username=None, email_address=None, owning_entity=None, default_language=None, primary_contact=None, ietf_language=None, country_code=None, is_active=None, correlation_id=None):  # noqa: E501
        """KycProtectGetMyUserDetailsResponse - a model defined in Swagger"""  # noqa: E501
        self._username = None
        self._email_address = None
        self._owning_entity = None
        self._default_language = None
        self._primary_contact = None
        self._ietf_language = None
        self._country_code = None
        self._is_active = None
        self._correlation_id = None
        self.discriminator = None
        if username is not None:
            self.username = username
        if email_address is not None:
            self.email_address = email_address
        if owning_entity is not None:
            self.owning_entity = owning_entity
        if default_language is not None:
            self.default_language = default_language
        if primary_contact is not None:
            self.primary_contact = primary_contact
        if ietf_language is not None:
            self.ietf_language = ietf_language
        if country_code is not None:
            self.country_code = country_code
        if is_active is not None:
            self.is_active = is_active
        if correlation_id is not None:
            self.correlation_id = correlation_id

    @property
    def username(self):
        """Gets the username of this KycProtectGetMyUserDetailsResponse.  # noqa: E501

        The name of the user.  # noqa: E501

        :return: The username of this KycProtectGetMyUserDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this KycProtectGetMyUserDetailsResponse.

        The name of the user.  # noqa: E501

        :param username: The username of this KycProtectGetMyUserDetailsResponse.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def email_address(self):
        """Gets the email_address of this KycProtectGetMyUserDetailsResponse.  # noqa: E501

        The email address of the user.  # noqa: E501

        :return: The email_address of this KycProtectGetMyUserDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this KycProtectGetMyUserDetailsResponse.

        The email address of the user.  # noqa: E501

        :param email_address: The email_address of this KycProtectGetMyUserDetailsResponse.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def owning_entity(self):
        """Gets the owning_entity of this KycProtectGetMyUserDetailsResponse.  # noqa: E501

        Owning entity of the user.  # noqa: E501

        :return: The owning_entity of this KycProtectGetMyUserDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._owning_entity

    @owning_entity.setter
    def owning_entity(self, owning_entity):
        """Sets the owning_entity of this KycProtectGetMyUserDetailsResponse.

        Owning entity of the user.  # noqa: E501

        :param owning_entity: The owning_entity of this KycProtectGetMyUserDetailsResponse.  # noqa: E501
        :type: str
        """

        self._owning_entity = owning_entity

    @property
    def default_language(self):
        """Gets the default_language of this KycProtectGetMyUserDetailsResponse.  # noqa: E501

        user default language.  # noqa: E501

        :return: The default_language of this KycProtectGetMyUserDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._default_language

    @default_language.setter
    def default_language(self, default_language):
        """Sets the default_language of this KycProtectGetMyUserDetailsResponse.

        user default language.  # noqa: E501

        :param default_language: The default_language of this KycProtectGetMyUserDetailsResponse.  # noqa: E501
        :type: str
        """

        self._default_language = default_language

    @property
    def primary_contact(self):
        """Gets the primary_contact of this KycProtectGetMyUserDetailsResponse.  # noqa: E501


        :return: The primary_contact of this KycProtectGetMyUserDetailsResponse.  # noqa: E501
        :rtype: KycProtectGetMyUserDetailsResponsePrimaryContact
        """
        return self._primary_contact

    @primary_contact.setter
    def primary_contact(self, primary_contact):
        """Sets the primary_contact of this KycProtectGetMyUserDetailsResponse.


        :param primary_contact: The primary_contact of this KycProtectGetMyUserDetailsResponse.  # noqa: E501
        :type: KycProtectGetMyUserDetailsResponsePrimaryContact
        """

        self._primary_contact = primary_contact

    @property
    def ietf_language(self):
        """Gets the ietf_language of this KycProtectGetMyUserDetailsResponse.  # noqa: E501

        user default language.  # noqa: E501

        :return: The ietf_language of this KycProtectGetMyUserDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._ietf_language

    @ietf_language.setter
    def ietf_language(self, ietf_language):
        """Sets the ietf_language of this KycProtectGetMyUserDetailsResponse.

        user default language.  # noqa: E501

        :param ietf_language: The ietf_language of this KycProtectGetMyUserDetailsResponse.  # noqa: E501
        :type: str
        """

        self._ietf_language = ietf_language

    @property
    def country_code(self):
        """Gets the country_code of this KycProtectGetMyUserDetailsResponse.  # noqa: E501

        country code of the user.  # noqa: E501

        :return: The country_code of this KycProtectGetMyUserDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this KycProtectGetMyUserDetailsResponse.

        country code of the user.  # noqa: E501

        :param country_code: The country_code of this KycProtectGetMyUserDetailsResponse.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def is_active(self):
        """Gets the is_active of this KycProtectGetMyUserDetailsResponse.  # noqa: E501

        status of the user.  # noqa: E501

        :return: The is_active of this KycProtectGetMyUserDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this KycProtectGetMyUserDetailsResponse.

        status of the user.  # noqa: E501

        :param is_active: The is_active of this KycProtectGetMyUserDetailsResponse.  # noqa: E501
        :type: str
        """

        self._is_active = is_active

    @property
    def correlation_id(self):
        """Gets the correlation_id of this KycProtectGetMyUserDetailsResponse.  # noqa: E501

        A unique ID assigned to this request.  # noqa: E501

        :return: The correlation_id of this KycProtectGetMyUserDetailsResponse.  # noqa: E501
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this KycProtectGetMyUserDetailsResponse.

        A unique ID assigned to this request.  # noqa: E501

        :param correlation_id: The correlation_id of this KycProtectGetMyUserDetailsResponse.  # noqa: E501
        :type: str
        """

        self._correlation_id = correlation_id

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
        if issubclass(KycProtectGetMyUserDetailsResponse, dict):
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
        if not isinstance(other, KycProtectGetMyUserDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

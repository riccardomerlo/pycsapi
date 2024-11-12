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

class PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse(object):
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
        'name': 'str',
        'first_name': 'str',
        'middle_name': 'str',
        'last_name': 'str',
        'entity_type': 'str',
        'key_party_type': 'str',
        'gender': 'str',
        'date_of_birth': 'date',
        'organisation_number': 'str',
        'activity_code': 'str',
        'percentage_of_shares': 'float',
        'role': 'str',
        'country_code': 'str',
        'address': 'PostKYCKeypartiesByProfileIdAddressRequestContractResponse'
    }

    attribute_map = {
        'name': 'name',
        'first_name': 'firstName',
        'middle_name': 'middleName',
        'last_name': 'lastName',
        'entity_type': 'entityType',
        'key_party_type': 'keyPartyType',
        'gender': 'gender',
        'date_of_birth': 'dateOfBirth',
        'organisation_number': 'organisationNumber',
        'activity_code': 'activityCode',
        'percentage_of_shares': 'percentageOfShares',
        'role': 'role',
        'country_code': 'countryCode',
        'address': 'address'
    }

    def __init__(self, name=None, first_name=None, middle_name=None, last_name=None, entity_type=None, key_party_type=None, gender=None, date_of_birth=None, organisation_number=None, activity_code=None, percentage_of_shares=None, role=None, country_code=None, address=None):  # noqa: E501
        """PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._entity_type = None
        self._key_party_type = None
        self._gender = None
        self._date_of_birth = None
        self._organisation_number = None
        self._activity_code = None
        self._percentage_of_shares = None
        self._role = None
        self._country_code = None
        self._address = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if first_name is not None:
            self.first_name = first_name
        if middle_name is not None:
            self.middle_name = middle_name
        if last_name is not None:
            self.last_name = last_name
        if entity_type is not None:
            self.entity_type = entity_type
        if key_party_type is not None:
            self.key_party_type = key_party_type
        if gender is not None:
            self.gender = gender
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if organisation_number is not None:
            self.organisation_number = organisation_number
        if activity_code is not None:
            self.activity_code = activity_code
        if percentage_of_shares is not None:
            self.percentage_of_shares = percentage_of_shares
        if role is not None:
            self.role = role
        if country_code is not None:
            self.country_code = country_code
        if address is not None:
            self.address = address

    @property
    def name(self):
        """Gets the name of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501

        Name of the key party  Maximum length is 200 characters  # noqa: E501

        :return: The name of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.

        Name of the key party  Maximum length is 200 characters  # noqa: E501

        :param name: The name of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def first_name(self):
        """Gets the first_name of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501

        First name of the key party  <br> Valid for only entity type Individual <br> Maximum length is 200 characters combining First name, Middle name and Last name  # noqa: E501

        :return: The first_name of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.

        First name of the key party  <br> Valid for only entity type Individual <br> Maximum length is 200 characters combining First name, Middle name and Last name  # noqa: E501

        :param first_name: The first_name of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def middle_name(self):
        """Gets the middle_name of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501

        Middle name of the key party  <br> Valid for only entity type Individual <br> Maximum length is 200 characters combining First name, Middle name and Last name  # noqa: E501

        :return: The middle_name of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.

        Middle name of the key party  <br> Valid for only entity type Individual <br> Maximum length is 200 characters combining First name, Middle name and Last name  # noqa: E501

        :param middle_name: The middle_name of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :type: str
        """

        self._middle_name = middle_name

    @property
    def last_name(self):
        """Gets the last_name of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501

        Last name of the key party  <br> Valid for only entity type Individual <br> Maximum length is 200 characters combining First name, Middle name and Last name  # noqa: E501

        :return: The last_name of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.

        Last name of the key party  <br> Valid for only entity type Individual <br> Maximum length is 200 characters combining First name, Middle name and Last name  # noqa: E501

        :param last_name: The last_name of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def entity_type(self):
        """Gets the entity_type of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501

        Entity type of the key party, individual, business  # noqa: E501

        :return: The entity_type of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.

        Entity type of the key party, individual, business  # noqa: E501

        :param entity_type: The entity_type of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :type: str
        """

        self._entity_type = entity_type

    @property
    def key_party_type(self):
        """Gets the key_party_type of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501

        Type of the key party  <br> Valid Key Party types for entity type Individual are Director, Ubo and ShareHolder <br> Valid Key Party types for entity type Business are Ubo and ShareHolder , director, shareHolder, ubo  # noqa: E501

        :return: The key_party_type of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :rtype: str
        """
        return self._key_party_type

    @key_party_type.setter
    def key_party_type(self, key_party_type):
        """Sets the key_party_type of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.

        Type of the key party  <br> Valid Key Party types for entity type Individual are Director, Ubo and ShareHolder <br> Valid Key Party types for entity type Business are Ubo and ShareHolder , director, shareHolder, ubo  # noqa: E501

        :param key_party_type: The key_party_type of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :type: str
        """

        self._key_party_type = key_party_type

    @property
    def gender(self):
        """Gets the gender of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501

        Gender of the key party  Valid for entity type Individual, male, female  # noqa: E501

        :return: The gender of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.

        Gender of the key party  Valid for entity type Individual, male, female  # noqa: E501

        :param gender: The gender of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501

        Date of birth of the key party  Date YYYY-MM-DD or YYYY format. Must be after 1900 and not in the future  <br> Valid for the entity type Individual   # noqa: E501

        :return: The date_of_birth of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :rtype: date
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.

        Date of birth of the key party  Date YYYY-MM-DD or YYYY format. Must be after 1900 and not in the future  <br> Valid for the entity type Individual   # noqa: E501

        :param date_of_birth: The date_of_birth of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :type: date
        """

        self._date_of_birth = date_of_birth

    @property
    def organisation_number(self):
        """Gets the organisation_number of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501

        <br> Key party organisation number   <br> Valid for entity type Business   # noqa: E501

        :return: The organisation_number of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :rtype: str
        """
        return self._organisation_number

    @organisation_number.setter
    def organisation_number(self, organisation_number):
        """Sets the organisation_number of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.

        <br> Key party organisation number   <br> Valid for entity type Business   # noqa: E501

        :param organisation_number: The organisation_number of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :type: str
        """

        self._organisation_number = organisation_number

    @property
    def activity_code(self):
        """Gets the activity_code of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501

        Activity code of the key party  <br> Valid for entity type Business   # noqa: E501

        :return: The activity_code of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :rtype: str
        """
        return self._activity_code

    @activity_code.setter
    def activity_code(self, activity_code):
        """Sets the activity_code of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.

        Activity code of the key party  <br> Valid for entity type Business   # noqa: E501

        :param activity_code: The activity_code of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :type: str
        """

        self._activity_code = activity_code

    @property
    def percentage_of_shares(self):
        """Gets the percentage_of_shares of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501

        Share percentage of the key party  <br> Valid for key party type ShareHolder   # noqa: E501

        :return: The percentage_of_shares of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :rtype: float
        """
        return self._percentage_of_shares

    @percentage_of_shares.setter
    def percentage_of_shares(self, percentage_of_shares):
        """Sets the percentage_of_shares of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.

        Share percentage of the key party  <br> Valid for key party type ShareHolder   # noqa: E501

        :param percentage_of_shares: The percentage_of_shares of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :type: float
        """

        self._percentage_of_shares = percentage_of_shares

    @property
    def role(self):
        """Gets the role of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501

        Role of the key party  <br> Valid for key party type Director   # noqa: E501

        :return: The role of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.

        Role of the key party  <br> Valid for key party type Director   # noqa: E501

        :param role: The role of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def country_code(self):
        """Gets the country_code of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501

        Country code of the key party  # noqa: E501

        :return: The country_code of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.

        Country code of the key party  # noqa: E501

        :param country_code: The country_code of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def address(self):
        """Gets the address of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501


        :return: The address of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :rtype: PostKYCKeypartiesByProfileIdAddressRequestContractResponse
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.


        :param address: The address of this PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse.  # noqa: E501
        :type: PostKYCKeypartiesByProfileIdAddressRequestContractResponse
        """

        self._address = address

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
        if issubclass(PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse, dict):
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
        if not isinstance(other, PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

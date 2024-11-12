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
from pycsapi.models.creditsafe_global_data_reports_entity_full_name import (
    CreditsafeGlobalDataReportsEntityFullName,
)  # noqa: F401,E501


class CreditsafeGlobalDataReportsDirector(CreditsafeGlobalDataReportsEntityFullName):
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
        "gender": "CreditsafeGlobalDataReportsGender",
        "birth_name": "str",
        "date_of_birth": "datetime",
        "place_of_birth": "str",
        "nationality": "str",
        "country_of_residence": "str",
        "country": "CreditsafeGlobalDataCountryCode",
        "director_type": "CreditsafeGlobalDataReportsEntityType",
        "has_negative_info": "bool",
        "signing_authority": "bool",
        "positions": "list[CreditsafeGlobalDataReportsCorporatePosition]",
        "additional_data": "CreditsafeGlobalDataReportsDirectorAdditionalData",
    }
    if hasattr(CreditsafeGlobalDataReportsEntityFullName, "swagger_types"):
        swagger_types.update(CreditsafeGlobalDataReportsEntityFullName.swagger_types)

    attribute_map = {
        "gender": "gender",
        "birth_name": "birthName",
        "date_of_birth": "dateOfBirth",
        "place_of_birth": "placeOfBirth",
        "nationality": "nationality",
        "country_of_residence": "countryOfResidence",
        "country": "country",
        "director_type": "directorType",
        "has_negative_info": "hasNegativeInfo",
        "signing_authority": "signingAuthority",
        "positions": "positions",
        "additional_data": "additionalData",
    }
    if hasattr(CreditsafeGlobalDataReportsEntityFullName, "attribute_map"):
        attribute_map.update(CreditsafeGlobalDataReportsEntityFullName.attribute_map)

    def __init__(
        self,
        gender=None,
        birth_name=None,
        date_of_birth=None,
        place_of_birth=None,
        nationality=None,
        country_of_residence=None,
        country=None,
        director_type=None,
        has_negative_info=None,
        signing_authority=None,
        positions=None,
        additional_data=None,
        *args,
        **kwargs
    ):  # noqa: E501
        """CreditsafeGlobalDataReportsDirector - a model defined in Swagger"""  # noqa: E501
        self._gender = None
        self._birth_name = None
        self._date_of_birth = None
        self._place_of_birth = None
        self._nationality = None
        self._country_of_residence = None
        self._country = None
        self._director_type = None
        self._has_negative_info = None
        self._signing_authority = None
        self._positions = None
        self._additional_data = None
        self.discriminator = None
        if gender is not None:
            self.gender = gender
        if birth_name is not None:
            self.birth_name = birth_name
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if place_of_birth is not None:
            self.place_of_birth = place_of_birth
        if nationality is not None:
            self.nationality = nationality
        if country_of_residence is not None:
            self.country_of_residence = country_of_residence
        if country is not None:
            self.country = country
        if director_type is not None:
            self.director_type = director_type
        if has_negative_info is not None:
            self.has_negative_info = has_negative_info
        if signing_authority is not None:
            self.signing_authority = signing_authority
        if positions is not None:
            self.positions = positions
        if additional_data is not None:
            self.additional_data = additional_data
        CreditsafeGlobalDataReportsEntityFullName.__init__(self, *args, **kwargs)

    @property
    def gender(self):
        """Gets the gender of this CreditsafeGlobalDataReportsDirector.  # noqa: E501


        :return: The gender of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsGender
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this CreditsafeGlobalDataReportsDirector.


        :param gender: The gender of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :type: CreditsafeGlobalDataReportsGender
        """

        self._gender = gender

    @property
    def birth_name(self):
        """Gets the birth_name of this CreditsafeGlobalDataReportsDirector.  # noqa: E501


        :return: The birth_name of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :rtype: str
        """
        return self._birth_name

    @birth_name.setter
    def birth_name(self, birth_name):
        """Sets the birth_name of this CreditsafeGlobalDataReportsDirector.


        :param birth_name: The birth_name of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :type: str
        """

        self._birth_name = birth_name

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this CreditsafeGlobalDataReportsDirector.  # noqa: E501


        :return: The date_of_birth of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :rtype: datetime
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this CreditsafeGlobalDataReportsDirector.


        :param date_of_birth: The date_of_birth of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :type: datetime
        """

        self._date_of_birth = date_of_birth

    @property
    def place_of_birth(self):
        """Gets the place_of_birth of this CreditsafeGlobalDataReportsDirector.  # noqa: E501


        :return: The place_of_birth of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :rtype: str
        """
        return self._place_of_birth

    @place_of_birth.setter
    def place_of_birth(self, place_of_birth):
        """Sets the place_of_birth of this CreditsafeGlobalDataReportsDirector.


        :param place_of_birth: The place_of_birth of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :type: str
        """

        self._place_of_birth = place_of_birth

    @property
    def nationality(self):
        """Gets the nationality of this CreditsafeGlobalDataReportsDirector.  # noqa: E501


        :return: The nationality of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this CreditsafeGlobalDataReportsDirector.


        :param nationality: The nationality of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :type: str
        """

        self._nationality = nationality

    @property
    def country_of_residence(self):
        """Gets the country_of_residence of this CreditsafeGlobalDataReportsDirector.  # noqa: E501


        :return: The country_of_residence of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :rtype: str
        """
        return self._country_of_residence

    @country_of_residence.setter
    def country_of_residence(self, country_of_residence):
        """Sets the country_of_residence of this CreditsafeGlobalDataReportsDirector.


        :param country_of_residence: The country_of_residence of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :type: str
        """

        self._country_of_residence = country_of_residence

    @property
    def country(self):
        """Gets the country of this CreditsafeGlobalDataReportsDirector.  # noqa: E501


        :return: The country of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :rtype: CreditsafeGlobalDataCountryCode
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CreditsafeGlobalDataReportsDirector.


        :param country: The country of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :type: CreditsafeGlobalDataCountryCode
        """

        self._country = country

    @property
    def director_type(self):
        """Gets the director_type of this CreditsafeGlobalDataReportsDirector.  # noqa: E501


        :return: The director_type of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsEntityType
        """
        return self._director_type

    @director_type.setter
    def director_type(self, director_type):
        """Sets the director_type of this CreditsafeGlobalDataReportsDirector.


        :param director_type: The director_type of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :type: CreditsafeGlobalDataReportsEntityType
        """

        self._director_type = director_type

    @property
    def has_negative_info(self):
        """Gets the has_negative_info of this CreditsafeGlobalDataReportsDirector.  # noqa: E501

        Linked with DE searches, may return with other countries if data is available.  # noqa: E501

        :return: The has_negative_info of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :rtype: bool
        """
        return self._has_negative_info

    @has_negative_info.setter
    def has_negative_info(self, has_negative_info):
        """Sets the has_negative_info of this CreditsafeGlobalDataReportsDirector.

        Linked with DE searches, may return with other countries if data is available.  # noqa: E501

        :param has_negative_info: The has_negative_info of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :type: bool
        """

        self._has_negative_info = has_negative_info

    @property
    def signing_authority(self):
        """Gets the signing_authority of this CreditsafeGlobalDataReportsDirector.  # noqa: E501

        Linked with DE searches, may return with other countries if data is available.  # noqa: E501

        :return: The signing_authority of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :rtype: bool
        """
        return self._signing_authority

    @signing_authority.setter
    def signing_authority(self, signing_authority):
        """Sets the signing_authority of this CreditsafeGlobalDataReportsDirector.

        Linked with DE searches, may return with other countries if data is available.  # noqa: E501

        :param signing_authority: The signing_authority of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :type: bool
        """

        self._signing_authority = signing_authority

    @property
    def positions(self):
        """Gets the positions of this CreditsafeGlobalDataReportsDirector.  # noqa: E501


        :return: The positions of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :rtype: list[CreditsafeGlobalDataReportsCorporatePosition]
        """
        return self._positions

    @positions.setter
    def positions(self, positions):
        """Sets the positions of this CreditsafeGlobalDataReportsDirector.


        :param positions: The positions of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :type: list[CreditsafeGlobalDataReportsCorporatePosition]
        """

        self._positions = positions

    @property
    def additional_data(self):
        """Gets the additional_data of this CreditsafeGlobalDataReportsDirector.  # noqa: E501


        :return: The additional_data of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsDirectorAdditionalData
        """
        return self._additional_data

    @additional_data.setter
    def additional_data(self, additional_data):
        """Sets the additional_data of this CreditsafeGlobalDataReportsDirector.


        :param additional_data: The additional_data of this CreditsafeGlobalDataReportsDirector.  # noqa: E501
        :type: CreditsafeGlobalDataReportsDirectorAdditionalData
        """

        self._additional_data = additional_data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (
                            (item[0], item[1].to_dict())
                            if hasattr(item[1], "to_dict")
                            else item
                        ),
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(CreditsafeGlobalDataReportsDirector, dict):
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
        if not isinstance(other, CreditsafeGlobalDataReportsDirector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

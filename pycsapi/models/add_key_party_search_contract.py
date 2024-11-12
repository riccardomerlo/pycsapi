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

class AddKeyPartySearchContract(object):
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
        'type': 'str',
        'name': 'str',
        'first_name': 'str',
        'middle_name': 'str',
        'last_name': 'str',
        'date_of_birth': 'date',
        'gender': 'str',
        'pep_tiers': 'list[str]',
        'datasets': 'list[str]',
        'country_codes': 'list[str]',
        'threshold': 'int',
        'key_party_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'first_name': 'firstName',
        'middle_name': 'middleName',
        'last_name': 'lastName',
        'date_of_birth': 'dateOfBirth',
        'gender': 'gender',
        'pep_tiers': 'pepTiers',
        'datasets': 'datasets',
        'country_codes': 'countryCodes',
        'threshold': 'threshold',
        'key_party_id': 'keyPartyId'
    }

    def __init__(self, type=None, name=None, first_name=None, middle_name=None, last_name=None, date_of_birth=None, gender=None, pep_tiers=None, datasets=None, country_codes=None, threshold=None, key_party_id=None):  # noqa: E501
        """AddKeyPartySearchContract - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._name = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._date_of_birth = None
        self._gender = None
        self._pep_tiers = None
        self._datasets = None
        self._country_codes = None
        self._threshold = None
        self._key_party_id = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if first_name is not None:
            self.first_name = first_name
        if middle_name is not None:
            self.middle_name = middle_name
        if last_name is not None:
            self.last_name = last_name
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if gender is not None:
            self.gender = gender
        if pep_tiers is not None:
            self.pep_tiers = pep_tiers
        if datasets is not None:
            self.datasets = datasets
        if country_codes is not None:
            self.country_codes = country_codes
        if threshold is not None:
            self.threshold = threshold
        if key_party_id is not None:
            self.key_party_id = key_party_id

    @property
    def type(self):
        """Gets the type of this AddKeyPartySearchContract.  # noqa: E501

        The entity type of the search. Available values are individual and business.  # noqa: E501

        :return: The type of this AddKeyPartySearchContract.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AddKeyPartySearchContract.

        The entity type of the search. Available values are individual and business.  # noqa: E501

        :param type: The type of this AddKeyPartySearchContract.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this AddKeyPartySearchContract.  # noqa: E501

        Required if FirstName and LastName are not provided  # noqa: E501

        :return: The name of this AddKeyPartySearchContract.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AddKeyPartySearchContract.

        Required if FirstName and LastName are not provided  # noqa: E501

        :param name: The name of this AddKeyPartySearchContract.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def first_name(self):
        """Gets the first_name of this AddKeyPartySearchContract.  # noqa: E501

        If FirstName is provided then LastName must also be provided  # noqa: E501

        :return: The first_name of this AddKeyPartySearchContract.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this AddKeyPartySearchContract.

        If FirstName is provided then LastName must also be provided  # noqa: E501

        :param first_name: The first_name of this AddKeyPartySearchContract.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def middle_name(self):
        """Gets the middle_name of this AddKeyPartySearchContract.  # noqa: E501

        Middle name is optional, valid along with Firstname and LastName only  # noqa: E501

        :return: The middle_name of this AddKeyPartySearchContract.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this AddKeyPartySearchContract.

        Middle name is optional, valid along with Firstname and LastName only  # noqa: E501

        :param middle_name: The middle_name of this AddKeyPartySearchContract.  # noqa: E501
        :type: str
        """

        self._middle_name = middle_name

    @property
    def last_name(self):
        """Gets the last_name of this AddKeyPartySearchContract.  # noqa: E501

        If LastName is provided then FirstName must also be provided  # noqa: E501

        :return: The last_name of this AddKeyPartySearchContract.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this AddKeyPartySearchContract.

        If LastName is provided then FirstName must also be provided  # noqa: E501

        :param last_name: The last_name of this AddKeyPartySearchContract.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this AddKeyPartySearchContract.  # noqa: E501

        Date YYYY-MM-DD or YYYY format. Must be after 1900 and not in the future.  # noqa: E501

        :return: The date_of_birth of this AddKeyPartySearchContract.  # noqa: E501
        :rtype: date
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this AddKeyPartySearchContract.

        Date YYYY-MM-DD or YYYY format. Must be after 1900 and not in the future.  # noqa: E501

        :param date_of_birth: The date_of_birth of this AddKeyPartySearchContract.  # noqa: E501
        :type: date
        """

        self._date_of_birth = date_of_birth

    @property
    def gender(self):
        """Gets the gender of this AddKeyPartySearchContract.  # noqa: E501

        Define the gender of the individual you are searching for.  # noqa: E501

        :return: The gender of this AddKeyPartySearchContract.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this AddKeyPartySearchContract.

        Define the gender of the individual you are searching for.  # noqa: E501

        :param gender: The gender of this AddKeyPartySearchContract.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def pep_tiers(self):
        """Gets the pep_tiers of this AddKeyPartySearchContract.  # noqa: E501

        When searching the PEP dataset, define what tiers of the PEP profiles should be included in the results. Where PEP Tier 1 indicates senior roles, PEP Tier 2 - middle-ranking, and PEP Tier 3 - junior officials. If the PEP Dataset is NOT included on the list of searched datasets, then this value is ignored. The PEP Tier filter does not apply to PEP-LINKED Profiles.  # noqa: E501

        :return: The pep_tiers of this AddKeyPartySearchContract.  # noqa: E501
        :rtype: list[str]
        """
        return self._pep_tiers

    @pep_tiers.setter
    def pep_tiers(self, pep_tiers):
        """Sets the pep_tiers of this AddKeyPartySearchContract.

        When searching the PEP dataset, define what tiers of the PEP profiles should be included in the results. Where PEP Tier 1 indicates senior roles, PEP Tier 2 - middle-ranking, and PEP Tier 3 - junior officials. If the PEP Dataset is NOT included on the list of searched datasets, then this value is ignored. The PEP Tier filter does not apply to PEP-LINKED Profiles.  # noqa: E501

        :param pep_tiers: The pep_tiers of this AddKeyPartySearchContract.  # noqa: E501
        :type: list[str]
        """

        self._pep_tiers = pep_tiers

    @property
    def datasets(self):
        """Gets the datasets of this AddKeyPartySearchContract.  # noqa: E501

        UPDATE THIS SO IT DETAILS BOT INDIVIDUALS AND BUSINESSES Specifies which datasets will be searched PEP - Politically Exposed Persons (All) PEP-CURRENT - Only current PEPs PEP-FORMER - Only former PEPs PEP-LINKED - Only linked PEPs (PEP by Association) SAN - Sanctioned (All) SAN-CURRENT - Only current Sanctions SAN-FORMER - Only former Sanctions INS - Insolvency AM - Averse Media POI - Profile of Interest ENF - Enforcement DD - Disqualified Director  # noqa: E501

        :return: The datasets of this AddKeyPartySearchContract.  # noqa: E501
        :rtype: list[str]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this AddKeyPartySearchContract.

        UPDATE THIS SO IT DETAILS BOT INDIVIDUALS AND BUSINESSES Specifies which datasets will be searched PEP - Politically Exposed Persons (All) PEP-CURRENT - Only current PEPs PEP-FORMER - Only former PEPs PEP-LINKED - Only linked PEPs (PEP by Association) SAN - Sanctioned (All) SAN-CURRENT - Only current Sanctions SAN-FORMER - Only former Sanctions INS - Insolvency AM - Averse Media POI - Profile of Interest ENF - Enforcement DD - Disqualified Director  # noqa: E501

        :param datasets: The datasets of this AddKeyPartySearchContract.  # noqa: E501
        :type: list[str]
        """

        self._datasets = datasets

    @property
    def country_codes(self):
        """Gets the country_codes of this AddKeyPartySearchContract.  # noqa: E501


        :return: The country_codes of this AddKeyPartySearchContract.  # noqa: E501
        :rtype: list[str]
        """
        return self._country_codes

    @country_codes.setter
    def country_codes(self, country_codes):
        """Sets the country_codes of this AddKeyPartySearchContract.


        :param country_codes: The country_codes of this AddKeyPartySearchContract.  # noqa: E501
        :type: list[str]
        """

        self._country_codes = country_codes

    @property
    def threshold(self):
        """Gets the threshold of this AddKeyPartySearchContract.  # noqa: E501

        Must be one of 75, 80, 85, 90, 95, or 100  # noqa: E501

        :return: The threshold of this AddKeyPartySearchContract.  # noqa: E501
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this AddKeyPartySearchContract.

        Must be one of 75, 80, 85, 90, 95, or 100  # noqa: E501

        :param threshold: The threshold of this AddKeyPartySearchContract.  # noqa: E501
        :type: int
        """

        self._threshold = threshold

    @property
    def key_party_id(self):
        """Gets the key_party_id of this AddKeyPartySearchContract.  # noqa: E501


        :return: The key_party_id of this AddKeyPartySearchContract.  # noqa: E501
        :rtype: str
        """
        return self._key_party_id

    @key_party_id.setter
    def key_party_id(self, key_party_id):
        """Sets the key_party_id of this AddKeyPartySearchContract.


        :param key_party_id: The key_party_id of this AddKeyPartySearchContract.  # noqa: E501
        :type: str
        """

        self._key_party_id = key_party_id

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
        if issubclass(AddKeyPartySearchContract, dict):
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
        if not isinstance(other, AddKeyPartySearchContract):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

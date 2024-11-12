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

class ConnectIdentityAmlSupplierResultResultCodes(object):
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
        'uk_edited_voters_database': 'UKEditedVotersDatabase',
        'uk_national_identity_register': 'UKNationalIdentityRegister',
        'uk_landline_telephone_database': 'UKLandlineTelephoneDatabase',
        'uk_credit_header_aml': 'UKCreditHeaderAml',
        'uk_deceased_person_database': 'UKDeceasedPersonDatabase',
        'international_sanctions': 'InternationalSanctions',
        'international_enhanced_pep_database': 'InternationalEnhancedPepDatabase',
        'uk_births_registry_database': 'UKBirthsRegistryDatabase',
        'international_age_algorithm': 'InternationalAgeAlgorithm'
    }

    attribute_map = {
        'uk_edited_voters_database': 'UKEditedVotersDatabase',
        'uk_national_identity_register': 'UKNationalIdentityRegister',
        'uk_landline_telephone_database': 'UKLandlineTelephoneDatabase',
        'uk_credit_header_aml': 'UKCreditHeaderAml',
        'uk_deceased_person_database': 'UKDeceasedPersonDatabase',
        'international_sanctions': 'InternationalSanctions',
        'international_enhanced_pep_database': 'InternationalEnhancedPepDatabase',
        'uk_births_registry_database': 'UKBirthsRegistryDatabase',
        'international_age_algorithm': 'InternationalAgeAlgorithm'
    }

    def __init__(self, uk_edited_voters_database=None, uk_national_identity_register=None, uk_landline_telephone_database=None, uk_credit_header_aml=None, uk_deceased_person_database=None, international_sanctions=None, international_enhanced_pep_database=None, uk_births_registry_database=None, international_age_algorithm=None):  # noqa: E501
        """ConnectIdentityAmlSupplierResultResultCodes - a model defined in Swagger"""  # noqa: E501
        self._uk_edited_voters_database = None
        self._uk_national_identity_register = None
        self._uk_landline_telephone_database = None
        self._uk_credit_header_aml = None
        self._uk_deceased_person_database = None
        self._international_sanctions = None
        self._international_enhanced_pep_database = None
        self._uk_births_registry_database = None
        self._international_age_algorithm = None
        self.discriminator = None
        if uk_edited_voters_database is not None:
            self.uk_edited_voters_database = uk_edited_voters_database
        if uk_national_identity_register is not None:
            self.uk_national_identity_register = uk_national_identity_register
        if uk_landline_telephone_database is not None:
            self.uk_landline_telephone_database = uk_landline_telephone_database
        if uk_credit_header_aml is not None:
            self.uk_credit_header_aml = uk_credit_header_aml
        if uk_deceased_person_database is not None:
            self.uk_deceased_person_database = uk_deceased_person_database
        if international_sanctions is not None:
            self.international_sanctions = international_sanctions
        if international_enhanced_pep_database is not None:
            self.international_enhanced_pep_database = international_enhanced_pep_database
        if uk_births_registry_database is not None:
            self.uk_births_registry_database = uk_births_registry_database
        if international_age_algorithm is not None:
            self.international_age_algorithm = international_age_algorithm

    @property
    def uk_edited_voters_database(self):
        """Gets the uk_edited_voters_database of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501


        :return: The uk_edited_voters_database of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501
        :rtype: UKEditedVotersDatabase
        """
        return self._uk_edited_voters_database

    @uk_edited_voters_database.setter
    def uk_edited_voters_database(self, uk_edited_voters_database):
        """Sets the uk_edited_voters_database of this ConnectIdentityAmlSupplierResultResultCodes.


        :param uk_edited_voters_database: The uk_edited_voters_database of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501
        :type: UKEditedVotersDatabase
        """

        self._uk_edited_voters_database = uk_edited_voters_database

    @property
    def uk_national_identity_register(self):
        """Gets the uk_national_identity_register of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501


        :return: The uk_national_identity_register of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501
        :rtype: UKNationalIdentityRegister
        """
        return self._uk_national_identity_register

    @uk_national_identity_register.setter
    def uk_national_identity_register(self, uk_national_identity_register):
        """Sets the uk_national_identity_register of this ConnectIdentityAmlSupplierResultResultCodes.


        :param uk_national_identity_register: The uk_national_identity_register of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501
        :type: UKNationalIdentityRegister
        """

        self._uk_national_identity_register = uk_national_identity_register

    @property
    def uk_landline_telephone_database(self):
        """Gets the uk_landline_telephone_database of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501


        :return: The uk_landline_telephone_database of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501
        :rtype: UKLandlineTelephoneDatabase
        """
        return self._uk_landline_telephone_database

    @uk_landline_telephone_database.setter
    def uk_landline_telephone_database(self, uk_landline_telephone_database):
        """Sets the uk_landline_telephone_database of this ConnectIdentityAmlSupplierResultResultCodes.


        :param uk_landline_telephone_database: The uk_landline_telephone_database of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501
        :type: UKLandlineTelephoneDatabase
        """

        self._uk_landline_telephone_database = uk_landline_telephone_database

    @property
    def uk_credit_header_aml(self):
        """Gets the uk_credit_header_aml of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501


        :return: The uk_credit_header_aml of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501
        :rtype: UKCreditHeaderAml
        """
        return self._uk_credit_header_aml

    @uk_credit_header_aml.setter
    def uk_credit_header_aml(self, uk_credit_header_aml):
        """Sets the uk_credit_header_aml of this ConnectIdentityAmlSupplierResultResultCodes.


        :param uk_credit_header_aml: The uk_credit_header_aml of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501
        :type: UKCreditHeaderAml
        """

        self._uk_credit_header_aml = uk_credit_header_aml

    @property
    def uk_deceased_person_database(self):
        """Gets the uk_deceased_person_database of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501


        :return: The uk_deceased_person_database of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501
        :rtype: UKDeceasedPersonDatabase
        """
        return self._uk_deceased_person_database

    @uk_deceased_person_database.setter
    def uk_deceased_person_database(self, uk_deceased_person_database):
        """Sets the uk_deceased_person_database of this ConnectIdentityAmlSupplierResultResultCodes.


        :param uk_deceased_person_database: The uk_deceased_person_database of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501
        :type: UKDeceasedPersonDatabase
        """

        self._uk_deceased_person_database = uk_deceased_person_database

    @property
    def international_sanctions(self):
        """Gets the international_sanctions of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501


        :return: The international_sanctions of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501
        :rtype: InternationalSanctions
        """
        return self._international_sanctions

    @international_sanctions.setter
    def international_sanctions(self, international_sanctions):
        """Sets the international_sanctions of this ConnectIdentityAmlSupplierResultResultCodes.


        :param international_sanctions: The international_sanctions of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501
        :type: InternationalSanctions
        """

        self._international_sanctions = international_sanctions

    @property
    def international_enhanced_pep_database(self):
        """Gets the international_enhanced_pep_database of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501


        :return: The international_enhanced_pep_database of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501
        :rtype: InternationalEnhancedPepDatabase
        """
        return self._international_enhanced_pep_database

    @international_enhanced_pep_database.setter
    def international_enhanced_pep_database(self, international_enhanced_pep_database):
        """Sets the international_enhanced_pep_database of this ConnectIdentityAmlSupplierResultResultCodes.


        :param international_enhanced_pep_database: The international_enhanced_pep_database of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501
        :type: InternationalEnhancedPepDatabase
        """

        self._international_enhanced_pep_database = international_enhanced_pep_database

    @property
    def uk_births_registry_database(self):
        """Gets the uk_births_registry_database of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501


        :return: The uk_births_registry_database of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501
        :rtype: UKBirthsRegistryDatabase
        """
        return self._uk_births_registry_database

    @uk_births_registry_database.setter
    def uk_births_registry_database(self, uk_births_registry_database):
        """Sets the uk_births_registry_database of this ConnectIdentityAmlSupplierResultResultCodes.


        :param uk_births_registry_database: The uk_births_registry_database of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501
        :type: UKBirthsRegistryDatabase
        """

        self._uk_births_registry_database = uk_births_registry_database

    @property
    def international_age_algorithm(self):
        """Gets the international_age_algorithm of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501


        :return: The international_age_algorithm of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501
        :rtype: InternationalAgeAlgorithm
        """
        return self._international_age_algorithm

    @international_age_algorithm.setter
    def international_age_algorithm(self, international_age_algorithm):
        """Sets the international_age_algorithm of this ConnectIdentityAmlSupplierResultResultCodes.


        :param international_age_algorithm: The international_age_algorithm of this ConnectIdentityAmlSupplierResultResultCodes.  # noqa: E501
        :type: InternationalAgeAlgorithm
        """

        self._international_age_algorithm = international_age_algorithm

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
        if issubclass(ConnectIdentityAmlSupplierResultResultCodes, dict):
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
        if not isinstance(other, ConnectIdentityAmlSupplierResultResultCodes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
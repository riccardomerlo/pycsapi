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

class CreditsafeGlobalDataReportsLtdCompanyBasicInformation(object):
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
        'business_name': 'str',
        'registered_company_name': 'str',
        'company_registration_number': 'str',
        'country': 'CreditsafeGlobalDataCountryCode',
        'vat_registration_number': 'str',
        'vat_registration_date': 'datetime',
        'company_registration_date': 'datetime',
        'operations_start_date': 'datetime',
        'commercial_court': 'str',
        'legal_form': 'CreditsafeGlobalDataReportsLegalForm',
        'ownership_type': 'str',
        'company_status': 'CreditsafeGlobalDataReportsCompanyStatusDescription',
        'principal_activity': 'CreditsafeGlobalDataCompanyActivityClassification',
        'contact_address': 'CreditsafeGlobalDataAddressData'
    }

    attribute_map = {
        'business_name': 'businessName',
        'registered_company_name': 'registeredCompanyName',
        'company_registration_number': 'companyRegistrationNumber',
        'country': 'country',
        'vat_registration_number': 'vatRegistrationNumber',
        'vat_registration_date': 'vatRegistrationDate',
        'company_registration_date': 'companyRegistrationDate',
        'operations_start_date': 'operationsStartDate',
        'commercial_court': 'commercialCourt',
        'legal_form': 'legalForm',
        'ownership_type': 'ownershipType',
        'company_status': 'companyStatus',
        'principal_activity': 'principalActivity',
        'contact_address': 'contactAddress'
    }

    def __init__(self, business_name=None, registered_company_name=None, company_registration_number=None, country=None, vat_registration_number=None, vat_registration_date=None, company_registration_date=None, operations_start_date=None, commercial_court=None, legal_form=None, ownership_type=None, company_status=None, principal_activity=None, contact_address=None):  # noqa: E501
        """CreditsafeGlobalDataReportsLtdCompanyBasicInformation - a model defined in Swagger"""  # noqa: E501
        self._business_name = None
        self._registered_company_name = None
        self._company_registration_number = None
        self._country = None
        self._vat_registration_number = None
        self._vat_registration_date = None
        self._company_registration_date = None
        self._operations_start_date = None
        self._commercial_court = None
        self._legal_form = None
        self._ownership_type = None
        self._company_status = None
        self._principal_activity = None
        self._contact_address = None
        self.discriminator = None
        if business_name is not None:
            self.business_name = business_name
        if registered_company_name is not None:
            self.registered_company_name = registered_company_name
        if company_registration_number is not None:
            self.company_registration_number = company_registration_number
        if country is not None:
            self.country = country
        if vat_registration_number is not None:
            self.vat_registration_number = vat_registration_number
        if vat_registration_date is not None:
            self.vat_registration_date = vat_registration_date
        if company_registration_date is not None:
            self.company_registration_date = company_registration_date
        if operations_start_date is not None:
            self.operations_start_date = operations_start_date
        if commercial_court is not None:
            self.commercial_court = commercial_court
        if legal_form is not None:
            self.legal_form = legal_form
        if ownership_type is not None:
            self.ownership_type = ownership_type
        if company_status is not None:
            self.company_status = company_status
        if principal_activity is not None:
            self.principal_activity = principal_activity
        if contact_address is not None:
            self.contact_address = contact_address

    @property
    def business_name(self):
        """Gets the business_name of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501


        :return: The business_name of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        """Sets the business_name of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.


        :param business_name: The business_name of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :type: str
        """

        self._business_name = business_name

    @property
    def registered_company_name(self):
        """Gets the registered_company_name of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501


        :return: The registered_company_name of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :rtype: str
        """
        return self._registered_company_name

    @registered_company_name.setter
    def registered_company_name(self, registered_company_name):
        """Sets the registered_company_name of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.


        :param registered_company_name: The registered_company_name of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :type: str
        """

        self._registered_company_name = registered_company_name

    @property
    def company_registration_number(self):
        """Gets the company_registration_number of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501


        :return: The company_registration_number of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :rtype: str
        """
        return self._company_registration_number

    @company_registration_number.setter
    def company_registration_number(self, company_registration_number):
        """Sets the company_registration_number of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.


        :param company_registration_number: The company_registration_number of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :type: str
        """

        self._company_registration_number = company_registration_number

    @property
    def country(self):
        """Gets the country of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501


        :return: The country of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :rtype: CreditsafeGlobalDataCountryCode
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.


        :param country: The country of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :type: CreditsafeGlobalDataCountryCode
        """

        self._country = country

    @property
    def vat_registration_number(self):
        """Gets the vat_registration_number of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501


        :return: The vat_registration_number of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :rtype: str
        """
        return self._vat_registration_number

    @vat_registration_number.setter
    def vat_registration_number(self, vat_registration_number):
        """Sets the vat_registration_number of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.


        :param vat_registration_number: The vat_registration_number of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :type: str
        """

        self._vat_registration_number = vat_registration_number

    @property
    def vat_registration_date(self):
        """Gets the vat_registration_date of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501


        :return: The vat_registration_date of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :rtype: datetime
        """
        return self._vat_registration_date

    @vat_registration_date.setter
    def vat_registration_date(self, vat_registration_date):
        """Sets the vat_registration_date of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.


        :param vat_registration_date: The vat_registration_date of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :type: datetime
        """

        self._vat_registration_date = vat_registration_date

    @property
    def company_registration_date(self):
        """Gets the company_registration_date of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501


        :return: The company_registration_date of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :rtype: datetime
        """
        return self._company_registration_date

    @company_registration_date.setter
    def company_registration_date(self, company_registration_date):
        """Sets the company_registration_date of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.


        :param company_registration_date: The company_registration_date of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :type: datetime
        """

        self._company_registration_date = company_registration_date

    @property
    def operations_start_date(self):
        """Gets the operations_start_date of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501


        :return: The operations_start_date of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :rtype: datetime
        """
        return self._operations_start_date

    @operations_start_date.setter
    def operations_start_date(self, operations_start_date):
        """Sets the operations_start_date of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.


        :param operations_start_date: The operations_start_date of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :type: datetime
        """

        self._operations_start_date = operations_start_date

    @property
    def commercial_court(self):
        """Gets the commercial_court of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501


        :return: The commercial_court of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :rtype: str
        """
        return self._commercial_court

    @commercial_court.setter
    def commercial_court(self, commercial_court):
        """Sets the commercial_court of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.


        :param commercial_court: The commercial_court of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :type: str
        """

        self._commercial_court = commercial_court

    @property
    def legal_form(self):
        """Gets the legal_form of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501


        :return: The legal_form of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsLegalForm
        """
        return self._legal_form

    @legal_form.setter
    def legal_form(self, legal_form):
        """Sets the legal_form of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.


        :param legal_form: The legal_form of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :type: CreditsafeGlobalDataReportsLegalForm
        """

        self._legal_form = legal_form

    @property
    def ownership_type(self):
        """Gets the ownership_type of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501


        :return: The ownership_type of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :rtype: str
        """
        return self._ownership_type

    @ownership_type.setter
    def ownership_type(self, ownership_type):
        """Sets the ownership_type of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.


        :param ownership_type: The ownership_type of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :type: str
        """

        self._ownership_type = ownership_type

    @property
    def company_status(self):
        """Gets the company_status of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501


        :return: The company_status of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsCompanyStatusDescription
        """
        return self._company_status

    @company_status.setter
    def company_status(self, company_status):
        """Sets the company_status of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.


        :param company_status: The company_status of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :type: CreditsafeGlobalDataReportsCompanyStatusDescription
        """

        self._company_status = company_status

    @property
    def principal_activity(self):
        """Gets the principal_activity of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501


        :return: The principal_activity of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :rtype: CreditsafeGlobalDataCompanyActivityClassification
        """
        return self._principal_activity

    @principal_activity.setter
    def principal_activity(self, principal_activity):
        """Sets the principal_activity of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.


        :param principal_activity: The principal_activity of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :type: CreditsafeGlobalDataCompanyActivityClassification
        """

        self._principal_activity = principal_activity

    @property
    def contact_address(self):
        """Gets the contact_address of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501


        :return: The contact_address of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :rtype: CreditsafeGlobalDataAddressData
        """
        return self._contact_address

    @contact_address.setter
    def contact_address(self, contact_address):
        """Sets the contact_address of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.


        :param contact_address: The contact_address of this CreditsafeGlobalDataReportsLtdCompanyBasicInformation.  # noqa: E501
        :type: CreditsafeGlobalDataAddressData
        """

        self._contact_address = contact_address

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
        if issubclass(CreditsafeGlobalDataReportsLtdCompanyBasicInformation, dict):
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
        if not isinstance(other, CreditsafeGlobalDataReportsLtdCompanyBasicInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

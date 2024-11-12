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

class CreditsafeGlobalDataCompanyData(object):
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
        'id': 'str',
        'country': 'CreditsafeGlobalDataCountryCode',
        'reg_no': 'str',
        'safe_no': 'str',
        'id_type': 'CreditsafeGlobalDataReportsIdType',
        'name': 'str',
        'type': 'CreditsafeGlobalDataCompanyType',
        'office_type': 'CreditsafeGlobalDataOfficeType',
        'status': 'CreditsafeGlobalDataCompanyStatus',
        'vat_no': 'OneOfCreditsafeGlobalDataCompanyDataVatNo',
        'address': 'CreditsafeGlobalDataAddressData',
        'activity': 'CreditsafeGlobalDataCompanyActivityClassification',
        'legal_form': 'str',
        'additional_data': 'CreditsafeGlobalDataCompanyDataAdditionalData'
    }

    attribute_map = {
        'id': 'id',
        'country': 'country',
        'reg_no': 'regNo',
        'safe_no': 'safeNo',
        'id_type': 'idType',
        'name': 'name',
        'type': 'type',
        'office_type': 'officeType',
        'status': 'status',
        'vat_no': 'vatNo',
        'address': 'address',
        'activity': 'activity',
        'legal_form': 'legalForm',
        'additional_data': 'additionalData'
    }

    def __init__(self, id=None, country=None, reg_no=None, safe_no=None, id_type=None, name=None, type=None, office_type=None, status=None, vat_no=None, address=None, activity=None, legal_form=None, additional_data=None):  # noqa: E501
        """CreditsafeGlobalDataCompanyData - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._country = None
        self._reg_no = None
        self._safe_no = None
        self._id_type = None
        self._name = None
        self._type = None
        self._office_type = None
        self._status = None
        self._vat_no = None
        self._address = None
        self._activity = None
        self._legal_form = None
        self._additional_data = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if country is not None:
            self.country = country
        if reg_no is not None:
            self.reg_no = reg_no
        if safe_no is not None:
            self.safe_no = safe_no
        if id_type is not None:
            self.id_type = id_type
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if office_type is not None:
            self.office_type = office_type
        if status is not None:
            self.status = status
        if vat_no is not None:
            self.vat_no = vat_no
        if address is not None:
            self.address = address
        if activity is not None:
            self.activity = activity
        if legal_form is not None:
            self.legal_form = legal_form
        if additional_data is not None:
            self.additional_data = additional_data

    @property
    def id(self):
        """Gets the id of this CreditsafeGlobalDataCompanyData.  # noqa: E501


        :return: The id of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreditsafeGlobalDataCompanyData.


        :param id: The id of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def country(self):
        """Gets the country of this CreditsafeGlobalDataCompanyData.  # noqa: E501


        :return: The country of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :rtype: CreditsafeGlobalDataCountryCode
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CreditsafeGlobalDataCompanyData.


        :param country: The country of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :type: CreditsafeGlobalDataCountryCode
        """

        self._country = country

    @property
    def reg_no(self):
        """Gets the reg_no of this CreditsafeGlobalDataCompanyData.  # noqa: E501


        :return: The reg_no of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :rtype: str
        """
        return self._reg_no

    @reg_no.setter
    def reg_no(self, reg_no):
        """Sets the reg_no of this CreditsafeGlobalDataCompanyData.


        :param reg_no: The reg_no of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :type: str
        """

        self._reg_no = reg_no

    @property
    def safe_no(self):
        """Gets the safe_no of this CreditsafeGlobalDataCompanyData.  # noqa: E501


        :return: The safe_no of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :rtype: str
        """
        return self._safe_no

    @safe_no.setter
    def safe_no(self, safe_no):
        """Sets the safe_no of this CreditsafeGlobalDataCompanyData.


        :param safe_no: The safe_no of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :type: str
        """

        self._safe_no = safe_no

    @property
    def id_type(self):
        """Gets the id_type of this CreditsafeGlobalDataCompanyData.  # noqa: E501


        :return: The id_type of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsIdType
        """
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        """Sets the id_type of this CreditsafeGlobalDataCompanyData.


        :param id_type: The id_type of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :type: CreditsafeGlobalDataReportsIdType
        """

        self._id_type = id_type

    @property
    def name(self):
        """Gets the name of this CreditsafeGlobalDataCompanyData.  # noqa: E501


        :return: The name of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreditsafeGlobalDataCompanyData.


        :param name: The name of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this CreditsafeGlobalDataCompanyData.  # noqa: E501


        :return: The type of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :rtype: CreditsafeGlobalDataCompanyType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreditsafeGlobalDataCompanyData.


        :param type: The type of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :type: CreditsafeGlobalDataCompanyType
        """

        self._type = type

    @property
    def office_type(self):
        """Gets the office_type of this CreditsafeGlobalDataCompanyData.  # noqa: E501


        :return: The office_type of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :rtype: CreditsafeGlobalDataOfficeType
        """
        return self._office_type

    @office_type.setter
    def office_type(self, office_type):
        """Sets the office_type of this CreditsafeGlobalDataCompanyData.


        :param office_type: The office_type of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :type: CreditsafeGlobalDataOfficeType
        """

        self._office_type = office_type

    @property
    def status(self):
        """Gets the status of this CreditsafeGlobalDataCompanyData.  # noqa: E501


        :return: The status of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :rtype: CreditsafeGlobalDataCompanyStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreditsafeGlobalDataCompanyData.


        :param status: The status of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :type: CreditsafeGlobalDataCompanyStatus
        """

        self._status = status

    @property
    def vat_no(self):
        """Gets the vat_no of this CreditsafeGlobalDataCompanyData.  # noqa: E501


        :return: The vat_no of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :rtype: OneOfCreditsafeGlobalDataCompanyDataVatNo
        """
        return self._vat_no

    @vat_no.setter
    def vat_no(self, vat_no):
        """Sets the vat_no of this CreditsafeGlobalDataCompanyData.


        :param vat_no: The vat_no of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :type: OneOfCreditsafeGlobalDataCompanyDataVatNo
        """

        self._vat_no = vat_no

    @property
    def address(self):
        """Gets the address of this CreditsafeGlobalDataCompanyData.  # noqa: E501


        :return: The address of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :rtype: CreditsafeGlobalDataAddressData
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CreditsafeGlobalDataCompanyData.


        :param address: The address of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :type: CreditsafeGlobalDataAddressData
        """

        self._address = address

    @property
    def activity(self):
        """Gets the activity of this CreditsafeGlobalDataCompanyData.  # noqa: E501


        :return: The activity of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :rtype: CreditsafeGlobalDataCompanyActivityClassification
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this CreditsafeGlobalDataCompanyData.


        :param activity: The activity of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :type: CreditsafeGlobalDataCompanyActivityClassification
        """

        self._activity = activity

    @property
    def legal_form(self):
        """Gets the legal_form of this CreditsafeGlobalDataCompanyData.  # noqa: E501


        :return: The legal_form of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :rtype: str
        """
        return self._legal_form

    @legal_form.setter
    def legal_form(self, legal_form):
        """Sets the legal_form of this CreditsafeGlobalDataCompanyData.


        :param legal_form: The legal_form of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :type: str
        """

        self._legal_form = legal_form

    @property
    def additional_data(self):
        """Gets the additional_data of this CreditsafeGlobalDataCompanyData.  # noqa: E501


        :return: The additional_data of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :rtype: CreditsafeGlobalDataCompanyDataAdditionalData
        """
        return self._additional_data

    @additional_data.setter
    def additional_data(self, additional_data):
        """Sets the additional_data of this CreditsafeGlobalDataCompanyData.


        :param additional_data: The additional_data of this CreditsafeGlobalDataCompanyData.  # noqa: E501
        :type: CreditsafeGlobalDataCompanyDataAdditionalData
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
        if issubclass(CreditsafeGlobalDataCompanyData, dict):
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
        if not isinstance(other, CreditsafeGlobalDataCompanyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

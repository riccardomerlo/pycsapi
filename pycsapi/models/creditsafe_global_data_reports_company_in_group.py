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

class CreditsafeGlobalDataReportsCompanyInGroup(object):
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
        'country': 'str',
        'safe_number': 'str',
        'id_type': 'CreditsafeGlobalDataReportsIdType',
        'company_name': 'str',
        'registered_number': 'str',
        'latest_annual_accounts': 'datetime',
        'level': 'int',
        'percent_of_ownership': 'float',
        'status': 'str',
        'common_rating_band': 'str',
        'additional_data': 'CreditsafeGlobalDataReportsCompanyInGroupAdditionalData'
    }

    attribute_map = {
        'id': 'id',
        'country': 'country',
        'safe_number': 'safeNumber',
        'id_type': 'idType',
        'company_name': 'companyName',
        'registered_number': 'registeredNumber',
        'latest_annual_accounts': 'latestAnnualAccounts',
        'level': 'level',
        'percent_of_ownership': 'percentOfOwnership',
        'status': 'status',
        'common_rating_band': 'commonRatingBand',
        'additional_data': 'additionalData'
    }

    def __init__(self, id=None, country=None, safe_number=None, id_type=None, company_name=None, registered_number=None, latest_annual_accounts=None, level=None, percent_of_ownership=None, status=None, common_rating_band=None, additional_data=None):  # noqa: E501
        """CreditsafeGlobalDataReportsCompanyInGroup - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._country = None
        self._safe_number = None
        self._id_type = None
        self._company_name = None
        self._registered_number = None
        self._latest_annual_accounts = None
        self._level = None
        self._percent_of_ownership = None
        self._status = None
        self._common_rating_band = None
        self._additional_data = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if country is not None:
            self.country = country
        if safe_number is not None:
            self.safe_number = safe_number
        if id_type is not None:
            self.id_type = id_type
        if company_name is not None:
            self.company_name = company_name
        if registered_number is not None:
            self.registered_number = registered_number
        if latest_annual_accounts is not None:
            self.latest_annual_accounts = latest_annual_accounts
        if level is not None:
            self.level = level
        if percent_of_ownership is not None:
            self.percent_of_ownership = percent_of_ownership
        if status is not None:
            self.status = status
        if common_rating_band is not None:
            self.common_rating_band = common_rating_band
        if additional_data is not None:
            self.additional_data = additional_data

    @property
    def id(self):
        """Gets the id of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501


        :return: The id of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreditsafeGlobalDataReportsCompanyInGroup.


        :param id: The id of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def country(self):
        """Gets the country of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501


        :return: The country of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CreditsafeGlobalDataReportsCompanyInGroup.


        :param country: The country of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def safe_number(self):
        """Gets the safe_number of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501


        :return: The safe_number of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :rtype: str
        """
        return self._safe_number

    @safe_number.setter
    def safe_number(self, safe_number):
        """Sets the safe_number of this CreditsafeGlobalDataReportsCompanyInGroup.


        :param safe_number: The safe_number of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :type: str
        """

        self._safe_number = safe_number

    @property
    def id_type(self):
        """Gets the id_type of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501


        :return: The id_type of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsIdType
        """
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        """Sets the id_type of this CreditsafeGlobalDataReportsCompanyInGroup.


        :param id_type: The id_type of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :type: CreditsafeGlobalDataReportsIdType
        """

        self._id_type = id_type

    @property
    def company_name(self):
        """Gets the company_name of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501


        :return: The company_name of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this CreditsafeGlobalDataReportsCompanyInGroup.


        :param company_name: The company_name of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def registered_number(self):
        """Gets the registered_number of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501


        :return: The registered_number of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :rtype: str
        """
        return self._registered_number

    @registered_number.setter
    def registered_number(self, registered_number):
        """Sets the registered_number of this CreditsafeGlobalDataReportsCompanyInGroup.


        :param registered_number: The registered_number of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :type: str
        """

        self._registered_number = registered_number

    @property
    def latest_annual_accounts(self):
        """Gets the latest_annual_accounts of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501


        :return: The latest_annual_accounts of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._latest_annual_accounts

    @latest_annual_accounts.setter
    def latest_annual_accounts(self, latest_annual_accounts):
        """Sets the latest_annual_accounts of this CreditsafeGlobalDataReportsCompanyInGroup.


        :param latest_annual_accounts: The latest_annual_accounts of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :type: datetime
        """

        self._latest_annual_accounts = latest_annual_accounts

    @property
    def level(self):
        """Gets the level of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501


        :return: The level of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this CreditsafeGlobalDataReportsCompanyInGroup.


        :param level: The level of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :type: int
        """

        self._level = level

    @property
    def percent_of_ownership(self):
        """Gets the percent_of_ownership of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501


        :return: The percent_of_ownership of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :rtype: float
        """
        return self._percent_of_ownership

    @percent_of_ownership.setter
    def percent_of_ownership(self, percent_of_ownership):
        """Sets the percent_of_ownership of this CreditsafeGlobalDataReportsCompanyInGroup.


        :param percent_of_ownership: The percent_of_ownership of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :type: float
        """

        self._percent_of_ownership = percent_of_ownership

    @property
    def status(self):
        """Gets the status of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501


        :return: The status of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreditsafeGlobalDataReportsCompanyInGroup.


        :param status: The status of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def common_rating_band(self):
        """Gets the common_rating_band of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501


        :return: The common_rating_band of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :rtype: str
        """
        return self._common_rating_band

    @common_rating_band.setter
    def common_rating_band(self, common_rating_band):
        """Sets the common_rating_band of this CreditsafeGlobalDataReportsCompanyInGroup.


        :param common_rating_band: The common_rating_band of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :type: str
        """

        self._common_rating_band = common_rating_band

    @property
    def additional_data(self):
        """Gets the additional_data of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501


        :return: The additional_data of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsCompanyInGroupAdditionalData
        """
        return self._additional_data

    @additional_data.setter
    def additional_data(self, additional_data):
        """Sets the additional_data of this CreditsafeGlobalDataReportsCompanyInGroup.


        :param additional_data: The additional_data of this CreditsafeGlobalDataReportsCompanyInGroup.  # noqa: E501
        :type: CreditsafeGlobalDataReportsCompanyInGroupAdditionalData
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
        if issubclass(CreditsafeGlobalDataReportsCompanyInGroup, dict):
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
        if not isinstance(other, CreditsafeGlobalDataReportsCompanyInGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

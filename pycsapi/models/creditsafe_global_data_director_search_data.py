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

class CreditsafeGlobalDataDirectorSearchData(object):
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
        'people_id': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'country': 'CreditsafeGlobalDataCountryCode',
        'company': 'CreditsafeGlobalDataDirectorSearchDataCompany',
        'company_name': 'str',
        'company_type': 'CreditsafeGlobalDataCompanyType',
        'company_registration_number': 'str',
        'status': 'str',
        'address': 'CreditsafeGlobalDataAddressData',
        'date_of_latest_change': 'datetime',
        'date_of_birth': 'datetime',
        'local_director_number': 'str',
        'score': 'int',
        'tax_code': 'str',
        'search_ranking': 'str'
    }

    attribute_map = {
        'people_id': 'peopleId',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'country': 'country',
        'company': 'company',
        'company_name': 'companyName',
        'company_type': 'companyType',
        'company_registration_number': 'companyRegistrationNumber',
        'status': 'status',
        'address': 'address',
        'date_of_latest_change': 'dateOfLatestChange',
        'date_of_birth': 'dateOfBirth',
        'local_director_number': 'localDirectorNumber',
        'score': 'score',
        'tax_code': 'taxCode',
        'search_ranking': 'searchRanking'
    }

    def __init__(self, people_id=None, first_name=None, last_name=None, country=None, company=None, company_name=None, company_type=None, company_registration_number=None, status=None, address=None, date_of_latest_change=None, date_of_birth=None, local_director_number=None, score=None, tax_code=None, search_ranking=None):  # noqa: E501
        """CreditsafeGlobalDataDirectorSearchData - a model defined in Swagger"""  # noqa: E501
        self._people_id = None
        self._first_name = None
        self._last_name = None
        self._country = None
        self._company = None
        self._company_name = None
        self._company_type = None
        self._company_registration_number = None
        self._status = None
        self._address = None
        self._date_of_latest_change = None
        self._date_of_birth = None
        self._local_director_number = None
        self._score = None
        self._tax_code = None
        self._search_ranking = None
        self.discriminator = None
        if people_id is not None:
            self.people_id = people_id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if country is not None:
            self.country = country
        if company is not None:
            self.company = company
        if company_name is not None:
            self.company_name = company_name
        if company_type is not None:
            self.company_type = company_type
        if company_registration_number is not None:
            self.company_registration_number = company_registration_number
        if status is not None:
            self.status = status
        if address is not None:
            self.address = address
        if date_of_latest_change is not None:
            self.date_of_latest_change = date_of_latest_change
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if local_director_number is not None:
            self.local_director_number = local_director_number
        if score is not None:
            self.score = score
        if tax_code is not None:
            self.tax_code = tax_code
        if search_ranking is not None:
            self.search_ranking = search_ranking

    @property
    def people_id(self):
        """Gets the people_id of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501

        The unique identifier of the person.  # noqa: E501

        :return: The people_id of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :rtype: str
        """
        return self._people_id

    @people_id.setter
    def people_id(self, people_id):
        """Sets the people_id of this CreditsafeGlobalDataDirectorSearchData.

        The unique identifier of the person.  # noqa: E501

        :param people_id: The people_id of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :type: str
        """

        self._people_id = people_id

    @property
    def first_name(self):
        """Gets the first_name of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501

        The first name of the director.  # noqa: E501

        :return: The first_name of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this CreditsafeGlobalDataDirectorSearchData.

        The first name of the director.  # noqa: E501

        :param first_name: The first_name of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501

        The last name of the director.  # noqa: E501

        :return: The last_name of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this CreditsafeGlobalDataDirectorSearchData.

        The last name of the director.  # noqa: E501

        :param last_name: The last_name of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def country(self):
        """Gets the country of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501


        :return: The country of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :rtype: CreditsafeGlobalDataCountryCode
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CreditsafeGlobalDataDirectorSearchData.


        :param country: The country of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :type: CreditsafeGlobalDataCountryCode
        """

        self._country = country

    @property
    def company(self):
        """Gets the company of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501


        :return: The company of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :rtype: CreditsafeGlobalDataDirectorSearchDataCompany
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this CreditsafeGlobalDataDirectorSearchData.


        :param company: The company of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :type: CreditsafeGlobalDataDirectorSearchDataCompany
        """

        self._company = company

    @property
    def company_name(self):
        """Gets the company_name of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501

        The name of the company.  # noqa: E501

        :return: The company_name of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this CreditsafeGlobalDataDirectorSearchData.

        The name of the company.  # noqa: E501

        :param company_name: The company_name of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def company_type(self):
        """Gets the company_type of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501


        :return: The company_type of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :rtype: CreditsafeGlobalDataCompanyType
        """
        return self._company_type

    @company_type.setter
    def company_type(self, company_type):
        """Sets the company_type of this CreditsafeGlobalDataDirectorSearchData.


        :param company_type: The company_type of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :type: CreditsafeGlobalDataCompanyType
        """

        self._company_type = company_type

    @property
    def company_registration_number(self):
        """Gets the company_registration_number of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501

        The registration number of the company.  # noqa: E501

        :return: The company_registration_number of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :rtype: str
        """
        return self._company_registration_number

    @company_registration_number.setter
    def company_registration_number(self, company_registration_number):
        """Sets the company_registration_number of this CreditsafeGlobalDataDirectorSearchData.

        The registration number of the company.  # noqa: E501

        :param company_registration_number: The company_registration_number of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :type: str
        """

        self._company_registration_number = company_registration_number

    @property
    def status(self):
        """Gets the status of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501


        :return: The status of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreditsafeGlobalDataDirectorSearchData.


        :param status: The status of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def address(self):
        """Gets the address of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501


        :return: The address of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :rtype: CreditsafeGlobalDataAddressData
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CreditsafeGlobalDataDirectorSearchData.


        :param address: The address of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :type: CreditsafeGlobalDataAddressData
        """

        self._address = address

    @property
    def date_of_latest_change(self):
        """Gets the date_of_latest_change of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501

        The date of the latest change to the director information.  # noqa: E501

        :return: The date_of_latest_change of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :rtype: datetime
        """
        return self._date_of_latest_change

    @date_of_latest_change.setter
    def date_of_latest_change(self, date_of_latest_change):
        """Sets the date_of_latest_change of this CreditsafeGlobalDataDirectorSearchData.

        The date of the latest change to the director information.  # noqa: E501

        :param date_of_latest_change: The date_of_latest_change of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :type: datetime
        """

        self._date_of_latest_change = date_of_latest_change

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501

        The date of birth of the director.  # noqa: E501

        :return: The date_of_birth of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :rtype: datetime
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this CreditsafeGlobalDataDirectorSearchData.

        The date of birth of the director.  # noqa: E501

        :param date_of_birth: The date_of_birth of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :type: datetime
        """

        self._date_of_birth = date_of_birth

    @property
    def local_director_number(self):
        """Gets the local_director_number of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501

        The local director number of the director.  # noqa: E501

        :return: The local_director_number of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :rtype: str
        """
        return self._local_director_number

    @local_director_number.setter
    def local_director_number(self, local_director_number):
        """Sets the local_director_number of this CreditsafeGlobalDataDirectorSearchData.

        The local director number of the director.  # noqa: E501

        :param local_director_number: The local_director_number of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :type: str
        """

        self._local_director_number = local_director_number

    @property
    def score(self):
        """Gets the score of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501


        :return: The score of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this CreditsafeGlobalDataDirectorSearchData.


        :param score: The score of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :type: int
        """

        self._score = score

    @property
    def tax_code(self):
        """Gets the tax_code of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501


        :return: The tax_code of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :rtype: str
        """
        return self._tax_code

    @tax_code.setter
    def tax_code(self, tax_code):
        """Sets the tax_code of this CreditsafeGlobalDataDirectorSearchData.


        :param tax_code: The tax_code of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :type: str
        """

        self._tax_code = tax_code

    @property
    def search_ranking(self):
        """Gets the search_ranking of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501


        :return: The search_ranking of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :rtype: str
        """
        return self._search_ranking

    @search_ranking.setter
    def search_ranking(self, search_ranking):
        """Sets the search_ranking of this CreditsafeGlobalDataDirectorSearchData.


        :param search_ranking: The search_ranking of this CreditsafeGlobalDataDirectorSearchData.  # noqa: E501
        :type: str
        """

        self._search_ranking = search_ranking

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
        if issubclass(CreditsafeGlobalDataDirectorSearchData, dict):
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
        if not isinstance(other, CreditsafeGlobalDataDirectorSearchData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

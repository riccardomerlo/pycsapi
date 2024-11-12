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

class ConnectConfidenceMatchMatchResultsMatchedCompanies(object):
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
        'match_score_confidence': 'int',
        'id': 'str',
        'country': 'str',
        'reg_no': 'str',
        'safe_no': 'str',
        'name': 'str',
        'phone_number': 'int',
        'address': 'ConnectConfidenceMatchMatchResultsAddress',
        'status': 'str',
        'type': 'str',
        'office_type': 'str',
        'date_of_latest_accounts': 'str',
        'date_of_latest_change': 'str',
        'match_score_explain_plan': 'ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan'
    }

    attribute_map = {
        'match_score_confidence': 'matchScoreConfidence',
        'id': 'id',
        'country': 'country',
        'reg_no': 'regNo',
        'safe_no': 'safeNo',
        'name': 'name',
        'phone_number': 'phoneNumber',
        'address': 'address',
        'status': 'status',
        'type': 'type',
        'office_type': 'officeType',
        'date_of_latest_accounts': 'dateOfLatestAccounts',
        'date_of_latest_change': 'dateOfLatestChange',
        'match_score_explain_plan': 'matchScoreExplainPlan'
    }

    def __init__(self, match_score_confidence=None, id=None, country=None, reg_no=None, safe_no=None, name=None, phone_number=None, address=None, status=None, type=None, office_type=None, date_of_latest_accounts=None, date_of_latest_change=None, match_score_explain_plan=None):  # noqa: E501
        """ConnectConfidenceMatchMatchResultsMatchedCompanies - a model defined in Swagger"""  # noqa: E501
        self._match_score_confidence = None
        self._id = None
        self._country = None
        self._reg_no = None
        self._safe_no = None
        self._name = None
        self._phone_number = None
        self._address = None
        self._status = None
        self._type = None
        self._office_type = None
        self._date_of_latest_accounts = None
        self._date_of_latest_change = None
        self._match_score_explain_plan = None
        self.discriminator = None
        if match_score_confidence is not None:
            self.match_score_confidence = match_score_confidence
        if id is not None:
            self.id = id
        if country is not None:
            self.country = country
        if reg_no is not None:
            self.reg_no = reg_no
        if safe_no is not None:
            self.safe_no = safe_no
        if name is not None:
            self.name = name
        if phone_number is not None:
            self.phone_number = phone_number
        if address is not None:
            self.address = address
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if office_type is not None:
            self.office_type = office_type
        if date_of_latest_accounts is not None:
            self.date_of_latest_accounts = date_of_latest_accounts
        if date_of_latest_change is not None:
            self.date_of_latest_change = date_of_latest_change
        if match_score_explain_plan is not None:
            self.match_score_explain_plan = match_score_explain_plan

    @property
    def match_score_confidence(self):
        """Gets the match_score_confidence of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501


        :return: The match_score_confidence of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :rtype: int
        """
        return self._match_score_confidence

    @match_score_confidence.setter
    def match_score_confidence(self, match_score_confidence):
        """Sets the match_score_confidence of this ConnectConfidenceMatchMatchResultsMatchedCompanies.


        :param match_score_confidence: The match_score_confidence of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :type: int
        """

        self._match_score_confidence = match_score_confidence

    @property
    def id(self):
        """Gets the id of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501


        :return: The id of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConnectConfidenceMatchMatchResultsMatchedCompanies.


        :param id: The id of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def country(self):
        """Gets the country of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501


        :return: The country of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ConnectConfidenceMatchMatchResultsMatchedCompanies.


        :param country: The country of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def reg_no(self):
        """Gets the reg_no of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501


        :return: The reg_no of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :rtype: str
        """
        return self._reg_no

    @reg_no.setter
    def reg_no(self, reg_no):
        """Sets the reg_no of this ConnectConfidenceMatchMatchResultsMatchedCompanies.


        :param reg_no: The reg_no of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :type: str
        """

        self._reg_no = reg_no

    @property
    def safe_no(self):
        """Gets the safe_no of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501


        :return: The safe_no of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :rtype: str
        """
        return self._safe_no

    @safe_no.setter
    def safe_no(self, safe_no):
        """Sets the safe_no of this ConnectConfidenceMatchMatchResultsMatchedCompanies.


        :param safe_no: The safe_no of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :type: str
        """

        self._safe_no = safe_no

    @property
    def name(self):
        """Gets the name of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501


        :return: The name of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectConfidenceMatchMatchResultsMatchedCompanies.


        :param name: The name of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phone_number(self):
        """Gets the phone_number of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501


        :return: The phone_number of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :rtype: int
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this ConnectConfidenceMatchMatchResultsMatchedCompanies.


        :param phone_number: The phone_number of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :type: int
        """

        self._phone_number = phone_number

    @property
    def address(self):
        """Gets the address of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501


        :return: The address of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :rtype: ConnectConfidenceMatchMatchResultsAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ConnectConfidenceMatchMatchResultsMatchedCompanies.


        :param address: The address of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :type: ConnectConfidenceMatchMatchResultsAddress
        """

        self._address = address

    @property
    def status(self):
        """Gets the status of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501


        :return: The status of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConnectConfidenceMatchMatchResultsMatchedCompanies.


        :param status: The status of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501


        :return: The type of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConnectConfidenceMatchMatchResultsMatchedCompanies.


        :param type: The type of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def office_type(self):
        """Gets the office_type of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501

        Only available with US companies.  # noqa: E501

        :return: The office_type of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :rtype: str
        """
        return self._office_type

    @office_type.setter
    def office_type(self, office_type):
        """Sets the office_type of this ConnectConfidenceMatchMatchResultsMatchedCompanies.

        Only available with US companies.  # noqa: E501

        :param office_type: The office_type of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :type: str
        """

        self._office_type = office_type

    @property
    def date_of_latest_accounts(self):
        """Gets the date_of_latest_accounts of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501


        :return: The date_of_latest_accounts of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :rtype: str
        """
        return self._date_of_latest_accounts

    @date_of_latest_accounts.setter
    def date_of_latest_accounts(self, date_of_latest_accounts):
        """Sets the date_of_latest_accounts of this ConnectConfidenceMatchMatchResultsMatchedCompanies.


        :param date_of_latest_accounts: The date_of_latest_accounts of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :type: str
        """

        self._date_of_latest_accounts = date_of_latest_accounts

    @property
    def date_of_latest_change(self):
        """Gets the date_of_latest_change of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501


        :return: The date_of_latest_change of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :rtype: str
        """
        return self._date_of_latest_change

    @date_of_latest_change.setter
    def date_of_latest_change(self, date_of_latest_change):
        """Sets the date_of_latest_change of this ConnectConfidenceMatchMatchResultsMatchedCompanies.


        :param date_of_latest_change: The date_of_latest_change of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :type: str
        """

        self._date_of_latest_change = date_of_latest_change

    @property
    def match_score_explain_plan(self):
        """Gets the match_score_explain_plan of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501


        :return: The match_score_explain_plan of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :rtype: ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan
        """
        return self._match_score_explain_plan

    @match_score_explain_plan.setter
    def match_score_explain_plan(self, match_score_explain_plan):
        """Sets the match_score_explain_plan of this ConnectConfidenceMatchMatchResultsMatchedCompanies.


        :param match_score_explain_plan: The match_score_explain_plan of this ConnectConfidenceMatchMatchResultsMatchedCompanies.  # noqa: E501
        :type: ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan
        """

        self._match_score_explain_plan = match_score_explain_plan

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
        if issubclass(ConnectConfidenceMatchMatchResultsMatchedCompanies, dict):
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
        if not isinstance(other, ConnectConfidenceMatchMatchResultsMatchedCompanies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

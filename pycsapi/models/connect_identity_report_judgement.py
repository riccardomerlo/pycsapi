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

class ConnectIdentityReportJudgement(object):
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
        'address': 'ConnectIdentityReportAddress',
        'address_current': 'bool',
        'date_of_birth': 'datetime',
        'judgement_date': 'datetime',
        'amount': 'int',
        'status': 'str',
        'court': 'str',
        'court_type': 'str',
        'case_number': 'str',
        'satified_date': 'datetime',
        'notices': 'list[ConnectIdentityReportNotice]'
    }

    attribute_map = {
        'name': 'name',
        'address': 'address',
        'address_current': 'addressCurrent',
        'date_of_birth': 'dateOfBirth',
        'judgement_date': 'judgementDate',
        'amount': 'amount',
        'status': 'status',
        'court': 'court',
        'court_type': 'courtType',
        'case_number': 'caseNumber',
        'satified_date': 'satifiedDate',
        'notices': 'notices'
    }

    def __init__(self, name=None, address=None, address_current=None, date_of_birth=None, judgement_date=None, amount=None, status=None, court=None, court_type=None, case_number=None, satified_date=None, notices=None):  # noqa: E501
        """ConnectIdentityReportJudgement - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._address = None
        self._address_current = None
        self._date_of_birth = None
        self._judgement_date = None
        self._amount = None
        self._status = None
        self._court = None
        self._court_type = None
        self._case_number = None
        self._satified_date = None
        self._notices = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if address is not None:
            self.address = address
        if address_current is not None:
            self.address_current = address_current
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if judgement_date is not None:
            self.judgement_date = judgement_date
        if amount is not None:
            self.amount = amount
        if status is not None:
            self.status = status
        if court is not None:
            self.court = court
        if court_type is not None:
            self.court_type = court_type
        if case_number is not None:
            self.case_number = case_number
        if satified_date is not None:
            self.satified_date = satified_date
        if notices is not None:
            self.notices = notices

    @property
    def name(self):
        """Gets the name of this ConnectIdentityReportJudgement.  # noqa: E501


        :return: The name of this ConnectIdentityReportJudgement.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectIdentityReportJudgement.


        :param name: The name of this ConnectIdentityReportJudgement.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def address(self):
        """Gets the address of this ConnectIdentityReportJudgement.  # noqa: E501


        :return: The address of this ConnectIdentityReportJudgement.  # noqa: E501
        :rtype: ConnectIdentityReportAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ConnectIdentityReportJudgement.


        :param address: The address of this ConnectIdentityReportJudgement.  # noqa: E501
        :type: ConnectIdentityReportAddress
        """

        self._address = address

    @property
    def address_current(self):
        """Gets the address_current of this ConnectIdentityReportJudgement.  # noqa: E501


        :return: The address_current of this ConnectIdentityReportJudgement.  # noqa: E501
        :rtype: bool
        """
        return self._address_current

    @address_current.setter
    def address_current(self, address_current):
        """Sets the address_current of this ConnectIdentityReportJudgement.


        :param address_current: The address_current of this ConnectIdentityReportJudgement.  # noqa: E501
        :type: bool
        """

        self._address_current = address_current

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this ConnectIdentityReportJudgement.  # noqa: E501


        :return: The date_of_birth of this ConnectIdentityReportJudgement.  # noqa: E501
        :rtype: datetime
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this ConnectIdentityReportJudgement.


        :param date_of_birth: The date_of_birth of this ConnectIdentityReportJudgement.  # noqa: E501
        :type: datetime
        """

        self._date_of_birth = date_of_birth

    @property
    def judgement_date(self):
        """Gets the judgement_date of this ConnectIdentityReportJudgement.  # noqa: E501


        :return: The judgement_date of this ConnectIdentityReportJudgement.  # noqa: E501
        :rtype: datetime
        """
        return self._judgement_date

    @judgement_date.setter
    def judgement_date(self, judgement_date):
        """Sets the judgement_date of this ConnectIdentityReportJudgement.


        :param judgement_date: The judgement_date of this ConnectIdentityReportJudgement.  # noqa: E501
        :type: datetime
        """

        self._judgement_date = judgement_date

    @property
    def amount(self):
        """Gets the amount of this ConnectIdentityReportJudgement.  # noqa: E501


        :return: The amount of this ConnectIdentityReportJudgement.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ConnectIdentityReportJudgement.


        :param amount: The amount of this ConnectIdentityReportJudgement.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def status(self):
        """Gets the status of this ConnectIdentityReportJudgement.  # noqa: E501


        :return: The status of this ConnectIdentityReportJudgement.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConnectIdentityReportJudgement.


        :param status: The status of this ConnectIdentityReportJudgement.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def court(self):
        """Gets the court of this ConnectIdentityReportJudgement.  # noqa: E501


        :return: The court of this ConnectIdentityReportJudgement.  # noqa: E501
        :rtype: str
        """
        return self._court

    @court.setter
    def court(self, court):
        """Sets the court of this ConnectIdentityReportJudgement.


        :param court: The court of this ConnectIdentityReportJudgement.  # noqa: E501
        :type: str
        """

        self._court = court

    @property
    def court_type(self):
        """Gets the court_type of this ConnectIdentityReportJudgement.  # noqa: E501


        :return: The court_type of this ConnectIdentityReportJudgement.  # noqa: E501
        :rtype: str
        """
        return self._court_type

    @court_type.setter
    def court_type(self, court_type):
        """Sets the court_type of this ConnectIdentityReportJudgement.


        :param court_type: The court_type of this ConnectIdentityReportJudgement.  # noqa: E501
        :type: str
        """

        self._court_type = court_type

    @property
    def case_number(self):
        """Gets the case_number of this ConnectIdentityReportJudgement.  # noqa: E501


        :return: The case_number of this ConnectIdentityReportJudgement.  # noqa: E501
        :rtype: str
        """
        return self._case_number

    @case_number.setter
    def case_number(self, case_number):
        """Sets the case_number of this ConnectIdentityReportJudgement.


        :param case_number: The case_number of this ConnectIdentityReportJudgement.  # noqa: E501
        :type: str
        """

        self._case_number = case_number

    @property
    def satified_date(self):
        """Gets the satified_date of this ConnectIdentityReportJudgement.  # noqa: E501


        :return: The satified_date of this ConnectIdentityReportJudgement.  # noqa: E501
        :rtype: datetime
        """
        return self._satified_date

    @satified_date.setter
    def satified_date(self, satified_date):
        """Sets the satified_date of this ConnectIdentityReportJudgement.


        :param satified_date: The satified_date of this ConnectIdentityReportJudgement.  # noqa: E501
        :type: datetime
        """

        self._satified_date = satified_date

    @property
    def notices(self):
        """Gets the notices of this ConnectIdentityReportJudgement.  # noqa: E501


        :return: The notices of this ConnectIdentityReportJudgement.  # noqa: E501
        :rtype: list[ConnectIdentityReportNotice]
        """
        return self._notices

    @notices.setter
    def notices(self, notices):
        """Sets the notices of this ConnectIdentityReportJudgement.


        :param notices: The notices of this ConnectIdentityReportJudgement.  # noqa: E501
        :type: list[ConnectIdentityReportNotice]
        """

        self._notices = notices

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
        if issubclass(ConnectIdentityReportJudgement, dict):
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
        if not isinstance(other, ConnectIdentityReportJudgement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

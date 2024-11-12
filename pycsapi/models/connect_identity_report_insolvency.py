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

class ConnectIdentityReportInsolvency(object):
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
        'address': 'ConnectIdentityReportAddress',
        'company_name': 'str',
        'court': 'str',
        'discharge_date': 'datetime',
        'name': 'str',
        'order_date': 'datetime',
        'order_type': 'str',
        'status': 'str',
        'trading_name': 'str',
        'line_of_business': 'str',
        'amount': 'int',
        'case_year': 'int',
        'case_ref': 'str',
        'date_of_birth': 'datetime',
        'notices': 'list[ConnectIdentityReportNotice]',
        'restriction': 'ConnectIdentityInsolvencyRestriction'
    }

    attribute_map = {
        'address': 'address',
        'company_name': 'companyName',
        'court': 'court',
        'discharge_date': 'dischargeDate',
        'name': 'name',
        'order_date': 'orderDate',
        'order_type': 'orderType',
        'status': 'status',
        'trading_name': 'tradingName',
        'line_of_business': 'lineOfBusiness',
        'amount': 'amount',
        'case_year': 'caseYear',
        'case_ref': 'caseRef',
        'date_of_birth': 'dateOfBirth',
        'notices': 'notices',
        'restriction': 'restriction'
    }

    def __init__(self, address=None, company_name=None, court=None, discharge_date=None, name=None, order_date=None, order_type=None, status=None, trading_name=None, line_of_business=None, amount=None, case_year=None, case_ref=None, date_of_birth=None, notices=None, restriction=None):  # noqa: E501
        """ConnectIdentityReportInsolvency - a model defined in Swagger"""  # noqa: E501
        self._address = None
        self._company_name = None
        self._court = None
        self._discharge_date = None
        self._name = None
        self._order_date = None
        self._order_type = None
        self._status = None
        self._trading_name = None
        self._line_of_business = None
        self._amount = None
        self._case_year = None
        self._case_ref = None
        self._date_of_birth = None
        self._notices = None
        self._restriction = None
        self.discriminator = None
        if address is not None:
            self.address = address
        if company_name is not None:
            self.company_name = company_name
        if court is not None:
            self.court = court
        if discharge_date is not None:
            self.discharge_date = discharge_date
        if name is not None:
            self.name = name
        if order_date is not None:
            self.order_date = order_date
        if order_type is not None:
            self.order_type = order_type
        if status is not None:
            self.status = status
        if trading_name is not None:
            self.trading_name = trading_name
        if line_of_business is not None:
            self.line_of_business = line_of_business
        if amount is not None:
            self.amount = amount
        if case_year is not None:
            self.case_year = case_year
        if case_ref is not None:
            self.case_ref = case_ref
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if notices is not None:
            self.notices = notices
        if restriction is not None:
            self.restriction = restriction

    @property
    def address(self):
        """Gets the address of this ConnectIdentityReportInsolvency.  # noqa: E501


        :return: The address of this ConnectIdentityReportInsolvency.  # noqa: E501
        :rtype: ConnectIdentityReportAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ConnectIdentityReportInsolvency.


        :param address: The address of this ConnectIdentityReportInsolvency.  # noqa: E501
        :type: ConnectIdentityReportAddress
        """

        self._address = address

    @property
    def company_name(self):
        """Gets the company_name of this ConnectIdentityReportInsolvency.  # noqa: E501


        :return: The company_name of this ConnectIdentityReportInsolvency.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ConnectIdentityReportInsolvency.


        :param company_name: The company_name of this ConnectIdentityReportInsolvency.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def court(self):
        """Gets the court of this ConnectIdentityReportInsolvency.  # noqa: E501


        :return: The court of this ConnectIdentityReportInsolvency.  # noqa: E501
        :rtype: str
        """
        return self._court

    @court.setter
    def court(self, court):
        """Sets the court of this ConnectIdentityReportInsolvency.


        :param court: The court of this ConnectIdentityReportInsolvency.  # noqa: E501
        :type: str
        """

        self._court = court

    @property
    def discharge_date(self):
        """Gets the discharge_date of this ConnectIdentityReportInsolvency.  # noqa: E501


        :return: The discharge_date of this ConnectIdentityReportInsolvency.  # noqa: E501
        :rtype: datetime
        """
        return self._discharge_date

    @discharge_date.setter
    def discharge_date(self, discharge_date):
        """Sets the discharge_date of this ConnectIdentityReportInsolvency.


        :param discharge_date: The discharge_date of this ConnectIdentityReportInsolvency.  # noqa: E501
        :type: datetime
        """

        self._discharge_date = discharge_date

    @property
    def name(self):
        """Gets the name of this ConnectIdentityReportInsolvency.  # noqa: E501


        :return: The name of this ConnectIdentityReportInsolvency.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectIdentityReportInsolvency.


        :param name: The name of this ConnectIdentityReportInsolvency.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def order_date(self):
        """Gets the order_date of this ConnectIdentityReportInsolvency.  # noqa: E501


        :return: The order_date of this ConnectIdentityReportInsolvency.  # noqa: E501
        :rtype: datetime
        """
        return self._order_date

    @order_date.setter
    def order_date(self, order_date):
        """Sets the order_date of this ConnectIdentityReportInsolvency.


        :param order_date: The order_date of this ConnectIdentityReportInsolvency.  # noqa: E501
        :type: datetime
        """

        self._order_date = order_date

    @property
    def order_type(self):
        """Gets the order_type of this ConnectIdentityReportInsolvency.  # noqa: E501


        :return: The order_type of this ConnectIdentityReportInsolvency.  # noqa: E501
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this ConnectIdentityReportInsolvency.


        :param order_type: The order_type of this ConnectIdentityReportInsolvency.  # noqa: E501
        :type: str
        """

        self._order_type = order_type

    @property
    def status(self):
        """Gets the status of this ConnectIdentityReportInsolvency.  # noqa: E501


        :return: The status of this ConnectIdentityReportInsolvency.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConnectIdentityReportInsolvency.


        :param status: The status of this ConnectIdentityReportInsolvency.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def trading_name(self):
        """Gets the trading_name of this ConnectIdentityReportInsolvency.  # noqa: E501


        :return: The trading_name of this ConnectIdentityReportInsolvency.  # noqa: E501
        :rtype: str
        """
        return self._trading_name

    @trading_name.setter
    def trading_name(self, trading_name):
        """Sets the trading_name of this ConnectIdentityReportInsolvency.


        :param trading_name: The trading_name of this ConnectIdentityReportInsolvency.  # noqa: E501
        :type: str
        """

        self._trading_name = trading_name

    @property
    def line_of_business(self):
        """Gets the line_of_business of this ConnectIdentityReportInsolvency.  # noqa: E501


        :return: The line_of_business of this ConnectIdentityReportInsolvency.  # noqa: E501
        :rtype: str
        """
        return self._line_of_business

    @line_of_business.setter
    def line_of_business(self, line_of_business):
        """Sets the line_of_business of this ConnectIdentityReportInsolvency.


        :param line_of_business: The line_of_business of this ConnectIdentityReportInsolvency.  # noqa: E501
        :type: str
        """

        self._line_of_business = line_of_business

    @property
    def amount(self):
        """Gets the amount of this ConnectIdentityReportInsolvency.  # noqa: E501


        :return: The amount of this ConnectIdentityReportInsolvency.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ConnectIdentityReportInsolvency.


        :param amount: The amount of this ConnectIdentityReportInsolvency.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def case_year(self):
        """Gets the case_year of this ConnectIdentityReportInsolvency.  # noqa: E501


        :return: The case_year of this ConnectIdentityReportInsolvency.  # noqa: E501
        :rtype: int
        """
        return self._case_year

    @case_year.setter
    def case_year(self, case_year):
        """Sets the case_year of this ConnectIdentityReportInsolvency.


        :param case_year: The case_year of this ConnectIdentityReportInsolvency.  # noqa: E501
        :type: int
        """

        self._case_year = case_year

    @property
    def case_ref(self):
        """Gets the case_ref of this ConnectIdentityReportInsolvency.  # noqa: E501


        :return: The case_ref of this ConnectIdentityReportInsolvency.  # noqa: E501
        :rtype: str
        """
        return self._case_ref

    @case_ref.setter
    def case_ref(self, case_ref):
        """Sets the case_ref of this ConnectIdentityReportInsolvency.


        :param case_ref: The case_ref of this ConnectIdentityReportInsolvency.  # noqa: E501
        :type: str
        """

        self._case_ref = case_ref

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this ConnectIdentityReportInsolvency.  # noqa: E501


        :return: The date_of_birth of this ConnectIdentityReportInsolvency.  # noqa: E501
        :rtype: datetime
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this ConnectIdentityReportInsolvency.


        :param date_of_birth: The date_of_birth of this ConnectIdentityReportInsolvency.  # noqa: E501
        :type: datetime
        """

        self._date_of_birth = date_of_birth

    @property
    def notices(self):
        """Gets the notices of this ConnectIdentityReportInsolvency.  # noqa: E501


        :return: The notices of this ConnectIdentityReportInsolvency.  # noqa: E501
        :rtype: list[ConnectIdentityReportNotice]
        """
        return self._notices

    @notices.setter
    def notices(self, notices):
        """Sets the notices of this ConnectIdentityReportInsolvency.


        :param notices: The notices of this ConnectIdentityReportInsolvency.  # noqa: E501
        :type: list[ConnectIdentityReportNotice]
        """

        self._notices = notices

    @property
    def restriction(self):
        """Gets the restriction of this ConnectIdentityReportInsolvency.  # noqa: E501


        :return: The restriction of this ConnectIdentityReportInsolvency.  # noqa: E501
        :rtype: ConnectIdentityInsolvencyRestriction
        """
        return self._restriction

    @restriction.setter
    def restriction(self, restriction):
        """Sets the restriction of this ConnectIdentityReportInsolvency.


        :param restriction: The restriction of this ConnectIdentityReportInsolvency.  # noqa: E501
        :type: ConnectIdentityInsolvencyRestriction
        """

        self._restriction = restriction

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
        if issubclass(ConnectIdentityReportInsolvency, dict):
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
        if not isinstance(other, ConnectIdentityReportInsolvency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

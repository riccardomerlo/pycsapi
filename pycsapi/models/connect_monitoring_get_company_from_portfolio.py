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

class ConnectMonitoringGetCompanyFromPortfolio(object):
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
        'correlation_id': 'str',
        'connect_id': 'str',
        'portfolio_id': 'float',
        'personal_reference': 'str',
        'free_text': 'str',
        'personal_limit': 'str',
        'safe_number': 'str',
        'name': 'str',
        'country_code': 'str',
        'address': 'str',
        'company_status': 'str',
        'credit_limit': 'float',
        'rating_common': 'str',
        'rating_local': 'str',
        'date_last_event': 'datetime',
        'date_added': 'datetime',
        'date_modified': 'datetime'
    }

    attribute_map = {
        'correlation_id': 'correlationId',
        'connect_id': 'connectId',
        'portfolio_id': 'portfolioId',
        'personal_reference': 'personalReference',
        'free_text': 'freeText',
        'personal_limit': 'personalLimit',
        'safe_number': 'safeNumber',
        'name': 'name',
        'country_code': 'countryCode',
        'address': 'address',
        'company_status': 'companyStatus',
        'credit_limit': 'creditLimit',
        'rating_common': 'ratingCommon',
        'rating_local': 'ratingLocal',
        'date_last_event': 'dateLastEvent',
        'date_added': 'dateAdded',
        'date_modified': 'dateModified'
    }

    def __init__(self, correlation_id=None, connect_id=None, portfolio_id=None, personal_reference=None, free_text=None, personal_limit=None, safe_number=None, name=None, country_code=None, address=None, company_status=None, credit_limit=None, rating_common=None, rating_local=None, date_last_event=None, date_added=None, date_modified=None):  # noqa: E501
        """ConnectMonitoringGetCompanyFromPortfolio - a model defined in Swagger"""  # noqa: E501
        self._correlation_id = None
        self._connect_id = None
        self._portfolio_id = None
        self._personal_reference = None
        self._free_text = None
        self._personal_limit = None
        self._safe_number = None
        self._name = None
        self._country_code = None
        self._address = None
        self._company_status = None
        self._credit_limit = None
        self._rating_common = None
        self._rating_local = None
        self._date_last_event = None
        self._date_added = None
        self._date_modified = None
        self.discriminator = None
        if correlation_id is not None:
            self.correlation_id = correlation_id
        if connect_id is not None:
            self.connect_id = connect_id
        if portfolio_id is not None:
            self.portfolio_id = portfolio_id
        if personal_reference is not None:
            self.personal_reference = personal_reference
        if free_text is not None:
            self.free_text = free_text
        if personal_limit is not None:
            self.personal_limit = personal_limit
        if safe_number is not None:
            self.safe_number = safe_number
        if name is not None:
            self.name = name
        if country_code is not None:
            self.country_code = country_code
        if address is not None:
            self.address = address
        if company_status is not None:
            self.company_status = company_status
        if credit_limit is not None:
            self.credit_limit = credit_limit
        if rating_common is not None:
            self.rating_common = rating_common
        if rating_local is not None:
            self.rating_local = rating_local
        if date_last_event is not None:
            self.date_last_event = date_last_event
        if date_added is not None:
            self.date_added = date_added
        if date_modified is not None:
            self.date_modified = date_modified

    @property
    def correlation_id(self):
        """Gets the correlation_id of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501

        A unique ID assigned to this request.  # noqa: E501

        :return: The correlation_id of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this ConnectMonitoringGetCompanyFromPortfolio.

        A unique ID assigned to this request.  # noqa: E501

        :param correlation_id: The correlation_id of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :type: str
        """

        self._correlation_id = correlation_id

    @property
    def connect_id(self):
        """Gets the connect_id of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501

        The connectId of the company. A connectId is the primary Company identifier that is used to uniquely identify all companies across Creditsafe's Universe and Partner Network.  # noqa: E501

        :return: The connect_id of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._connect_id

    @connect_id.setter
    def connect_id(self, connect_id):
        """Sets the connect_id of this ConnectMonitoringGetCompanyFromPortfolio.

        The connectId of the company. A connectId is the primary Company identifier that is used to uniquely identify all companies across Creditsafe's Universe and Partner Network.  # noqa: E501

        :param connect_id: The connect_id of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :type: str
        """

        self._connect_id = connect_id

    @property
    def portfolio_id(self):
        """Gets the portfolio_id of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501

        The portfolio Id of the portfolio that contains the company.  # noqa: E501

        :return: The portfolio_id of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :rtype: float
        """
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, portfolio_id):
        """Sets the portfolio_id of this ConnectMonitoringGetCompanyFromPortfolio.

        The portfolio Id of the portfolio that contains the company.  # noqa: E501

        :param portfolio_id: The portfolio_id of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :type: float
        """

        self._portfolio_id = portfolio_id

    @property
    def personal_reference(self):
        """Gets the personal_reference of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501

        Field that can be used to add a personal reference against the company in a portfolio.  # noqa: E501

        :return: The personal_reference of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._personal_reference

    @personal_reference.setter
    def personal_reference(self, personal_reference):
        """Sets the personal_reference of this ConnectMonitoringGetCompanyFromPortfolio.

        Field that can be used to add a personal reference against the company in a portfolio.  # noqa: E501

        :param personal_reference: The personal_reference of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :type: str
        """

        self._personal_reference = personal_reference

    @property
    def free_text(self):
        """Gets the free_text of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501

        Field that can be used to add a free text note to when adding a company to a portfolio.  # noqa: E501

        :return: The free_text of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._free_text

    @free_text.setter
    def free_text(self, free_text):
        """Sets the free_text of this ConnectMonitoringGetCompanyFromPortfolio.

        Field that can be used to add a free text note to when adding a company to a portfolio.  # noqa: E501

        :param free_text: The free_text of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :type: str
        """

        self._free_text = free_text

    @property
    def personal_limit(self):
        """Gets the personal_limit of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501

        Field that can be used to add a personal limit number against the company in a portfolio.  # noqa: E501

        :return: The personal_limit of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._personal_limit

    @personal_limit.setter
    def personal_limit(self, personal_limit):
        """Sets the personal_limit of this ConnectMonitoringGetCompanyFromPortfolio.

        Field that can be used to add a personal limit number against the company in a portfolio.  # noqa: E501

        :param personal_limit: The personal_limit of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :type: str
        """

        self._personal_limit = personal_limit

    @property
    def safe_number(self):
        """Gets the safe_number of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501

        The Safe Number (Creditsafe's identifier on all Companies owned in the Creditsafe Universe) of the company.  # noqa: E501

        :return: The safe_number of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._safe_number

    @safe_number.setter
    def safe_number(self, safe_number):
        """Sets the safe_number of this ConnectMonitoringGetCompanyFromPortfolio.

        The Safe Number (Creditsafe's identifier on all Companies owned in the Creditsafe Universe) of the company.  # noqa: E501

        :param safe_number: The safe_number of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :type: str
        """

        self._safe_number = safe_number

    @property
    def name(self):
        """Gets the name of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501

        The name of the company .  # noqa: E501

        :return: The name of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectMonitoringGetCompanyFromPortfolio.

        The name of the company .  # noqa: E501

        :param name: The name of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def country_code(self):
        """Gets the country_code of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501

        ISO/Alpha 2 format country code of the company.  # noqa: E501

        :return: The country_code of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this ConnectMonitoringGetCompanyFromPortfolio.

        ISO/Alpha 2 format country code of the company.  # noqa: E501

        :param country_code: The country_code of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def address(self):
        """Gets the address of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501

        The address of the company.  # noqa: E501

        :return: The address of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ConnectMonitoringGetCompanyFromPortfolio.

        The address of the company.  # noqa: E501

        :param address: The address of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def company_status(self):
        """Gets the company_status of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501

        The current status of the company  # noqa: E501

        :return: The company_status of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._company_status

    @company_status.setter
    def company_status(self, company_status):
        """Sets the company_status of this ConnectMonitoringGetCompanyFromPortfolio.

        The current status of the company  # noqa: E501

        :param company_status: The company_status of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :type: str
        """

        self._company_status = company_status

    @property
    def credit_limit(self):
        """Gets the credit_limit of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501

        The credit limit of the company.  # noqa: E501

        :return: The credit_limit of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :rtype: float
        """
        return self._credit_limit

    @credit_limit.setter
    def credit_limit(self, credit_limit):
        """Sets the credit_limit of this ConnectMonitoringGetCompanyFromPortfolio.

        The credit limit of the company.  # noqa: E501

        :param credit_limit: The credit_limit of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :type: float
        """

        self._credit_limit = credit_limit

    @property
    def rating_common(self):
        """Gets the rating_common of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501

        The rating score band that the company is in.  # noqa: E501

        :return: The rating_common of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._rating_common

    @rating_common.setter
    def rating_common(self, rating_common):
        """Sets the rating_common of this ConnectMonitoringGetCompanyFromPortfolio.

        The rating score band that the company is in.  # noqa: E501

        :param rating_common: The rating_common of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :type: str
        """

        self._rating_common = rating_common

    @property
    def rating_local(self):
        """Gets the rating_local of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501

        Country specific rating score.  # noqa: E501

        :return: The rating_local of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :rtype: str
        """
        return self._rating_local

    @rating_local.setter
    def rating_local(self, rating_local):
        """Sets the rating_local of this ConnectMonitoringGetCompanyFromPortfolio.

        Country specific rating score.  # noqa: E501

        :param rating_local: The rating_local of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :type: str
        """

        self._rating_local = rating_local

    @property
    def date_last_event(self):
        """Gets the date_last_event of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501

        The date of the most recent event the company has had.  # noqa: E501

        :return: The date_last_event of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :rtype: datetime
        """
        return self._date_last_event

    @date_last_event.setter
    def date_last_event(self, date_last_event):
        """Sets the date_last_event of this ConnectMonitoringGetCompanyFromPortfolio.

        The date of the most recent event the company has had.  # noqa: E501

        :param date_last_event: The date_last_event of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :type: datetime
        """

        self._date_last_event = date_last_event

    @property
    def date_added(self):
        """Gets the date_added of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501

        The date the company was added to the portfolio.  # noqa: E501

        :return: The date_added of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :rtype: datetime
        """
        return self._date_added

    @date_added.setter
    def date_added(self, date_added):
        """Sets the date_added of this ConnectMonitoringGetCompanyFromPortfolio.

        The date the company was added to the portfolio.  # noqa: E501

        :param date_added: The date_added of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :type: datetime
        """

        self._date_added = date_added

    @property
    def date_modified(self):
        """Gets the date_modified of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501

        The date the company was last modified in the portfolio.  # noqa: E501

        :return: The date_modified of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :rtype: datetime
        """
        return self._date_modified

    @date_modified.setter
    def date_modified(self, date_modified):
        """Sets the date_modified of this ConnectMonitoringGetCompanyFromPortfolio.

        The date the company was last modified in the portfolio.  # noqa: E501

        :param date_modified: The date_modified of this ConnectMonitoringGetCompanyFromPortfolio.  # noqa: E501
        :type: datetime
        """

        self._date_modified = date_modified

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
        if issubclass(ConnectMonitoringGetCompanyFromPortfolio, dict):
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
        if not isinstance(other, ConnectMonitoringGetCompanyFromPortfolio):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

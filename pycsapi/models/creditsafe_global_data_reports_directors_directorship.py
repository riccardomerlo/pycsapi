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

class CreditsafeGlobalDataReportsDirectorsDirectorship(object):
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
        'id_type': 'CreditsafeGlobalDataReportsIdType',
        'company_name': 'str',
        'company_number': 'str',
        'company_registration_number': 'str',
        'address': 'CreditsafeGlobalDataAddressData',
        'status': 'CreditsafeGlobalDataCompanyStatus',
        'activity': 'CreditsafeGlobalDataReportsCompanyActivity',
        'position': 'CreditsafeGlobalDataReportsCorporatePositionResigned',
        'signing_authority': 'bool',
        'company_registration_date': 'datetime',
        'legal_form': 'CreditsafeGlobalDataReportsLegalForm',
        'state': 'str',
        'year_end_date': 'datetime',
        'currency': 'CreditsafeGlobalDataCurrency',
        'latest_turnover_figure': 'CreditsafeGlobalDataReportsFinancialValue1SystemDecimal',
        'net_worth': 'CreditsafeGlobalDataReportsFinancialValue1SystemDecimal',
        'legal_count': 'int',
        'legal_amount': 'CreditsafeGlobalDataReportsFinancialValue1SystemDecimal',
        'legal_count_in_last12_months': 'int',
        'credit_score': 'CreditsafeGlobalDataReportsLtdCreditScore',
        'dbt': 'float',
        'additional_data': 'CreditsafeGlobalDataReportsDirectorsDirectorshipAdditionalData'
    }

    attribute_map = {
        'id': 'id',
        'id_type': 'idType',
        'company_name': 'companyName',
        'company_number': 'companyNumber',
        'company_registration_number': 'companyRegistrationNumber',
        'address': 'address',
        'status': 'status',
        'activity': 'activity',
        'position': 'position',
        'signing_authority': 'signingAuthority',
        'company_registration_date': 'companyRegistrationDate',
        'legal_form': 'legalForm',
        'state': 'state',
        'year_end_date': 'yearEndDate',
        'currency': 'currency',
        'latest_turnover_figure': 'latestTurnoverFigure',
        'net_worth': 'netWorth',
        'legal_count': 'legalCount',
        'legal_amount': 'legalAmount',
        'legal_count_in_last12_months': 'legalCountInLast12Months',
        'credit_score': 'creditScore',
        'dbt': 'dbt',
        'additional_data': 'additionalData'
    }

    def __init__(self, id=None, id_type=None, company_name=None, company_number=None, company_registration_number=None, address=None, status=None, activity=None, position=None, signing_authority=None, company_registration_date=None, legal_form=None, state=None, year_end_date=None, currency=None, latest_turnover_figure=None, net_worth=None, legal_count=None, legal_amount=None, legal_count_in_last12_months=None, credit_score=None, dbt=None, additional_data=None):  # noqa: E501
        """CreditsafeGlobalDataReportsDirectorsDirectorship - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._id_type = None
        self._company_name = None
        self._company_number = None
        self._company_registration_number = None
        self._address = None
        self._status = None
        self._activity = None
        self._position = None
        self._signing_authority = None
        self._company_registration_date = None
        self._legal_form = None
        self._state = None
        self._year_end_date = None
        self._currency = None
        self._latest_turnover_figure = None
        self._net_worth = None
        self._legal_count = None
        self._legal_amount = None
        self._legal_count_in_last12_months = None
        self._credit_score = None
        self._dbt = None
        self._additional_data = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if id_type is not None:
            self.id_type = id_type
        if company_name is not None:
            self.company_name = company_name
        if company_number is not None:
            self.company_number = company_number
        if company_registration_number is not None:
            self.company_registration_number = company_registration_number
        if address is not None:
            self.address = address
        if status is not None:
            self.status = status
        if activity is not None:
            self.activity = activity
        if position is not None:
            self.position = position
        if signing_authority is not None:
            self.signing_authority = signing_authority
        if company_registration_date is not None:
            self.company_registration_date = company_registration_date
        if legal_form is not None:
            self.legal_form = legal_form
        if state is not None:
            self.state = state
        if year_end_date is not None:
            self.year_end_date = year_end_date
        if currency is not None:
            self.currency = currency
        if latest_turnover_figure is not None:
            self.latest_turnover_figure = latest_turnover_figure
        if net_worth is not None:
            self.net_worth = net_worth
        if legal_count is not None:
            self.legal_count = legal_count
        if legal_amount is not None:
            self.legal_amount = legal_amount
        if legal_count_in_last12_months is not None:
            self.legal_count_in_last12_months = legal_count_in_last12_months
        if credit_score is not None:
            self.credit_score = credit_score
        if dbt is not None:
            self.dbt = dbt
        if additional_data is not None:
            self.additional_data = additional_data

    @property
    def id(self):
        """Gets the id of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The id of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param id: The id of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def id_type(self):
        """Gets the id_type of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The id_type of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsIdType
        """
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        """Sets the id_type of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param id_type: The id_type of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: CreditsafeGlobalDataReportsIdType
        """

        self._id_type = id_type

    @property
    def company_name(self):
        """Gets the company_name of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The company_name of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param company_name: The company_name of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def company_number(self):
        """Gets the company_number of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The company_number of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: str
        """
        return self._company_number

    @company_number.setter
    def company_number(self, company_number):
        """Sets the company_number of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param company_number: The company_number of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: str
        """

        self._company_number = company_number

    @property
    def company_registration_number(self):
        """Gets the company_registration_number of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The company_registration_number of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: str
        """
        return self._company_registration_number

    @company_registration_number.setter
    def company_registration_number(self, company_registration_number):
        """Sets the company_registration_number of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param company_registration_number: The company_registration_number of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: str
        """

        self._company_registration_number = company_registration_number

    @property
    def address(self):
        """Gets the address of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The address of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: CreditsafeGlobalDataAddressData
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param address: The address of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: CreditsafeGlobalDataAddressData
        """

        self._address = address

    @property
    def status(self):
        """Gets the status of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The status of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: CreditsafeGlobalDataCompanyStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param status: The status of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: CreditsafeGlobalDataCompanyStatus
        """

        self._status = status

    @property
    def activity(self):
        """Gets the activity of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The activity of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsCompanyActivity
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param activity: The activity of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: CreditsafeGlobalDataReportsCompanyActivity
        """

        self._activity = activity

    @property
    def position(self):
        """Gets the position of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The position of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsCorporatePositionResigned
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param position: The position of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: CreditsafeGlobalDataReportsCorporatePositionResigned
        """

        self._position = position

    @property
    def signing_authority(self):
        """Gets the signing_authority of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The signing_authority of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: bool
        """
        return self._signing_authority

    @signing_authority.setter
    def signing_authority(self, signing_authority):
        """Sets the signing_authority of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param signing_authority: The signing_authority of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: bool
        """

        self._signing_authority = signing_authority

    @property
    def company_registration_date(self):
        """Gets the company_registration_date of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The company_registration_date of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: datetime
        """
        return self._company_registration_date

    @company_registration_date.setter
    def company_registration_date(self, company_registration_date):
        """Sets the company_registration_date of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param company_registration_date: The company_registration_date of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: datetime
        """

        self._company_registration_date = company_registration_date

    @property
    def legal_form(self):
        """Gets the legal_form of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The legal_form of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsLegalForm
        """
        return self._legal_form

    @legal_form.setter
    def legal_form(self, legal_form):
        """Sets the legal_form of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param legal_form: The legal_form of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: CreditsafeGlobalDataReportsLegalForm
        """

        self._legal_form = legal_form

    @property
    def state(self):
        """Gets the state of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The state of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param state: The state of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def year_end_date(self):
        """Gets the year_end_date of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The year_end_date of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: datetime
        """
        return self._year_end_date

    @year_end_date.setter
    def year_end_date(self, year_end_date):
        """Sets the year_end_date of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param year_end_date: The year_end_date of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: datetime
        """

        self._year_end_date = year_end_date

    @property
    def currency(self):
        """Gets the currency of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The currency of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: CreditsafeGlobalDataCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param currency: The currency of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: CreditsafeGlobalDataCurrency
        """

        self._currency = currency

    @property
    def latest_turnover_figure(self):
        """Gets the latest_turnover_figure of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The latest_turnover_figure of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsFinancialValue1SystemDecimal
        """
        return self._latest_turnover_figure

    @latest_turnover_figure.setter
    def latest_turnover_figure(self, latest_turnover_figure):
        """Sets the latest_turnover_figure of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param latest_turnover_figure: The latest_turnover_figure of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: CreditsafeGlobalDataReportsFinancialValue1SystemDecimal
        """

        self._latest_turnover_figure = latest_turnover_figure

    @property
    def net_worth(self):
        """Gets the net_worth of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The net_worth of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsFinancialValue1SystemDecimal
        """
        return self._net_worth

    @net_worth.setter
    def net_worth(self, net_worth):
        """Sets the net_worth of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param net_worth: The net_worth of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: CreditsafeGlobalDataReportsFinancialValue1SystemDecimal
        """

        self._net_worth = net_worth

    @property
    def legal_count(self):
        """Gets the legal_count of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The legal_count of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: int
        """
        return self._legal_count

    @legal_count.setter
    def legal_count(self, legal_count):
        """Sets the legal_count of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param legal_count: The legal_count of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: int
        """

        self._legal_count = legal_count

    @property
    def legal_amount(self):
        """Gets the legal_amount of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The legal_amount of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsFinancialValue1SystemDecimal
        """
        return self._legal_amount

    @legal_amount.setter
    def legal_amount(self, legal_amount):
        """Sets the legal_amount of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param legal_amount: The legal_amount of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: CreditsafeGlobalDataReportsFinancialValue1SystemDecimal
        """

        self._legal_amount = legal_amount

    @property
    def legal_count_in_last12_months(self):
        """Gets the legal_count_in_last12_months of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The legal_count_in_last12_months of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: int
        """
        return self._legal_count_in_last12_months

    @legal_count_in_last12_months.setter
    def legal_count_in_last12_months(self, legal_count_in_last12_months):
        """Sets the legal_count_in_last12_months of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param legal_count_in_last12_months: The legal_count_in_last12_months of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: int
        """

        self._legal_count_in_last12_months = legal_count_in_last12_months

    @property
    def credit_score(self):
        """Gets the credit_score of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The credit_score of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsLtdCreditScore
        """
        return self._credit_score

    @credit_score.setter
    def credit_score(self, credit_score):
        """Sets the credit_score of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param credit_score: The credit_score of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: CreditsafeGlobalDataReportsLtdCreditScore
        """

        self._credit_score = credit_score

    @property
    def dbt(self):
        """Gets the dbt of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The dbt of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: float
        """
        return self._dbt

    @dbt.setter
    def dbt(self, dbt):
        """Sets the dbt of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param dbt: The dbt of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: float
        """

        self._dbt = dbt

    @property
    def additional_data(self):
        """Gets the additional_data of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501


        :return: The additional_data of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsDirectorsDirectorshipAdditionalData
        """
        return self._additional_data

    @additional_data.setter
    def additional_data(self, additional_data):
        """Sets the additional_data of this CreditsafeGlobalDataReportsDirectorsDirectorship.


        :param additional_data: The additional_data of this CreditsafeGlobalDataReportsDirectorsDirectorship.  # noqa: E501
        :type: CreditsafeGlobalDataReportsDirectorsDirectorshipAdditionalData
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
        if issubclass(CreditsafeGlobalDataReportsDirectorsDirectorship, dict):
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
        if not isinstance(other, CreditsafeGlobalDataReportsDirectorsDirectorship):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

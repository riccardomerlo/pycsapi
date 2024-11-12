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

class ConnectIdentityReportHistory(object):
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
        'address_match': 'str',
        'balance': 'int',
        '_date': 'datetime',
        'date_of_birth': 'datetime',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'joint_application': 'bool',
        'link_type': 'str',
        'name': 'str',
        'tp_opt_in': 'bool',
        'organisation_name': 'str',
        'organisation_type': 'str',
        'own_search': 'bool',
        'purpose': 'str',
        'reason': 'str',
        'reference': 'str',
        'supplier_reference': 'str',
        'subsequent_enquiry': 'bool',
        'term': 'int',
        'transient': 'bool',
        'credit_type': 'str',
        'unit_name': 'str',
        'user_name': 'str',
        'search_date': 'datetime',
        'search_unit_name': 'str',
        'search_organisation_name': 'str',
        'search_organisation_type': 'str'
    }

    attribute_map = {
        'address': 'address',
        'address_match': 'addressMatch',
        'balance': 'balance',
        '_date': 'date',
        'date_of_birth': 'dateOfBirth',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'joint_application': 'jointApplication',
        'link_type': 'linkType',
        'name': 'name',
        'tp_opt_in': 'tpOptIn',
        'organisation_name': 'organisationName',
        'organisation_type': 'organisationType',
        'own_search': 'ownSearch',
        'purpose': 'purpose',
        'reason': 'reason',
        'reference': 'reference',
        'supplier_reference': 'supplierReference',
        'subsequent_enquiry': 'subsequentEnquiry',
        'term': 'term',
        'transient': 'transient',
        'credit_type': 'creditType',
        'unit_name': 'unitName',
        'user_name': 'userName',
        'search_date': 'searchDate',
        'search_unit_name': 'searchUnitName',
        'search_organisation_name': 'searchOrganisationName',
        'search_organisation_type': 'searchOrganisationType'
    }

    def __init__(self, address=None, address_match=None, balance=None, _date=None, date_of_birth=None, start_date=None, end_date=None, joint_application=None, link_type=None, name=None, tp_opt_in=None, organisation_name=None, organisation_type=None, own_search=None, purpose=None, reason=None, reference=None, supplier_reference=None, subsequent_enquiry=None, term=None, transient=None, credit_type=None, unit_name=None, user_name=None, search_date=None, search_unit_name=None, search_organisation_name=None, search_organisation_type=None):  # noqa: E501
        """ConnectIdentityReportHistory - a model defined in Swagger"""  # noqa: E501
        self._address = None
        self._address_match = None
        self._balance = None
        self.__date = None
        self._date_of_birth = None
        self._start_date = None
        self._end_date = None
        self._joint_application = None
        self._link_type = None
        self._name = None
        self._tp_opt_in = None
        self._organisation_name = None
        self._organisation_type = None
        self._own_search = None
        self._purpose = None
        self._reason = None
        self._reference = None
        self._supplier_reference = None
        self._subsequent_enquiry = None
        self._term = None
        self._transient = None
        self._credit_type = None
        self._unit_name = None
        self._user_name = None
        self._search_date = None
        self._search_unit_name = None
        self._search_organisation_name = None
        self._search_organisation_type = None
        self.discriminator = None
        if address is not None:
            self.address = address
        if address_match is not None:
            self.address_match = address_match
        if balance is not None:
            self.balance = balance
        if _date is not None:
            self._date = _date
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if joint_application is not None:
            self.joint_application = joint_application
        if link_type is not None:
            self.link_type = link_type
        if name is not None:
            self.name = name
        if tp_opt_in is not None:
            self.tp_opt_in = tp_opt_in
        if organisation_name is not None:
            self.organisation_name = organisation_name
        if organisation_type is not None:
            self.organisation_type = organisation_type
        if own_search is not None:
            self.own_search = own_search
        if purpose is not None:
            self.purpose = purpose
        if reason is not None:
            self.reason = reason
        if reference is not None:
            self.reference = reference
        if supplier_reference is not None:
            self.supplier_reference = supplier_reference
        if subsequent_enquiry is not None:
            self.subsequent_enquiry = subsequent_enquiry
        if term is not None:
            self.term = term
        if transient is not None:
            self.transient = transient
        if credit_type is not None:
            self.credit_type = credit_type
        if unit_name is not None:
            self.unit_name = unit_name
        if user_name is not None:
            self.user_name = user_name
        if search_date is not None:
            self.search_date = search_date
        if search_unit_name is not None:
            self.search_unit_name = search_unit_name
        if search_organisation_name is not None:
            self.search_organisation_name = search_organisation_name
        if search_organisation_type is not None:
            self.search_organisation_type = search_organisation_type

    @property
    def address(self):
        """Gets the address of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The address of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: ConnectIdentityReportAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ConnectIdentityReportHistory.


        :param address: The address of this ConnectIdentityReportHistory.  # noqa: E501
        :type: ConnectIdentityReportAddress
        """

        self._address = address

    @property
    def address_match(self):
        """Gets the address_match of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The address_match of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: str
        """
        return self._address_match

    @address_match.setter
    def address_match(self, address_match):
        """Sets the address_match of this ConnectIdentityReportHistory.


        :param address_match: The address_match of this ConnectIdentityReportHistory.  # noqa: E501
        :type: str
        """

        self._address_match = address_match

    @property
    def balance(self):
        """Gets the balance of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The balance of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: int
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this ConnectIdentityReportHistory.


        :param balance: The balance of this ConnectIdentityReportHistory.  # noqa: E501
        :type: int
        """

        self._balance = balance

    @property
    def _date(self):
        """Gets the _date of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The _date of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ConnectIdentityReportHistory.


        :param _date: The _date of this ConnectIdentityReportHistory.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The date_of_birth of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this ConnectIdentityReportHistory.


        :param date_of_birth: The date_of_birth of this ConnectIdentityReportHistory.  # noqa: E501
        :type: datetime
        """

        self._date_of_birth = date_of_birth

    @property
    def start_date(self):
        """Gets the start_date of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The start_date of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ConnectIdentityReportHistory.


        :param start_date: The start_date of this ConnectIdentityReportHistory.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The end_date of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ConnectIdentityReportHistory.


        :param end_date: The end_date of this ConnectIdentityReportHistory.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def joint_application(self):
        """Gets the joint_application of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The joint_application of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: bool
        """
        return self._joint_application

    @joint_application.setter
    def joint_application(self, joint_application):
        """Sets the joint_application of this ConnectIdentityReportHistory.


        :param joint_application: The joint_application of this ConnectIdentityReportHistory.  # noqa: E501
        :type: bool
        """

        self._joint_application = joint_application

    @property
    def link_type(self):
        """Gets the link_type of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The link_type of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: str
        """
        return self._link_type

    @link_type.setter
    def link_type(self, link_type):
        """Sets the link_type of this ConnectIdentityReportHistory.


        :param link_type: The link_type of this ConnectIdentityReportHistory.  # noqa: E501
        :type: str
        """

        self._link_type = link_type

    @property
    def name(self):
        """Gets the name of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The name of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectIdentityReportHistory.


        :param name: The name of this ConnectIdentityReportHistory.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tp_opt_in(self):
        """Gets the tp_opt_in of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The tp_opt_in of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: bool
        """
        return self._tp_opt_in

    @tp_opt_in.setter
    def tp_opt_in(self, tp_opt_in):
        """Sets the tp_opt_in of this ConnectIdentityReportHistory.


        :param tp_opt_in: The tp_opt_in of this ConnectIdentityReportHistory.  # noqa: E501
        :type: bool
        """

        self._tp_opt_in = tp_opt_in

    @property
    def organisation_name(self):
        """Gets the organisation_name of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The organisation_name of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: str
        """
        return self._organisation_name

    @organisation_name.setter
    def organisation_name(self, organisation_name):
        """Sets the organisation_name of this ConnectIdentityReportHistory.


        :param organisation_name: The organisation_name of this ConnectIdentityReportHistory.  # noqa: E501
        :type: str
        """

        self._organisation_name = organisation_name

    @property
    def organisation_type(self):
        """Gets the organisation_type of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The organisation_type of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: str
        """
        return self._organisation_type

    @organisation_type.setter
    def organisation_type(self, organisation_type):
        """Sets the organisation_type of this ConnectIdentityReportHistory.


        :param organisation_type: The organisation_type of this ConnectIdentityReportHistory.  # noqa: E501
        :type: str
        """

        self._organisation_type = organisation_type

    @property
    def own_search(self):
        """Gets the own_search of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The own_search of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: bool
        """
        return self._own_search

    @own_search.setter
    def own_search(self, own_search):
        """Sets the own_search of this ConnectIdentityReportHistory.


        :param own_search: The own_search of this ConnectIdentityReportHistory.  # noqa: E501
        :type: bool
        """

        self._own_search = own_search

    @property
    def purpose(self):
        """Gets the purpose of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The purpose of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this ConnectIdentityReportHistory.


        :param purpose: The purpose of this ConnectIdentityReportHistory.  # noqa: E501
        :type: str
        """

        self._purpose = purpose

    @property
    def reason(self):
        """Gets the reason of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The reason of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ConnectIdentityReportHistory.


        :param reason: The reason of this ConnectIdentityReportHistory.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def reference(self):
        """Gets the reference of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The reference of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this ConnectIdentityReportHistory.


        :param reference: The reference of this ConnectIdentityReportHistory.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def supplier_reference(self):
        """Gets the supplier_reference of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The supplier_reference of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: str
        """
        return self._supplier_reference

    @supplier_reference.setter
    def supplier_reference(self, supplier_reference):
        """Sets the supplier_reference of this ConnectIdentityReportHistory.


        :param supplier_reference: The supplier_reference of this ConnectIdentityReportHistory.  # noqa: E501
        :type: str
        """

        self._supplier_reference = supplier_reference

    @property
    def subsequent_enquiry(self):
        """Gets the subsequent_enquiry of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The subsequent_enquiry of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: bool
        """
        return self._subsequent_enquiry

    @subsequent_enquiry.setter
    def subsequent_enquiry(self, subsequent_enquiry):
        """Sets the subsequent_enquiry of this ConnectIdentityReportHistory.


        :param subsequent_enquiry: The subsequent_enquiry of this ConnectIdentityReportHistory.  # noqa: E501
        :type: bool
        """

        self._subsequent_enquiry = subsequent_enquiry

    @property
    def term(self):
        """Gets the term of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The term of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: int
        """
        return self._term

    @term.setter
    def term(self, term):
        """Sets the term of this ConnectIdentityReportHistory.


        :param term: The term of this ConnectIdentityReportHistory.  # noqa: E501
        :type: int
        """

        self._term = term

    @property
    def transient(self):
        """Gets the transient of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The transient of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: bool
        """
        return self._transient

    @transient.setter
    def transient(self, transient):
        """Sets the transient of this ConnectIdentityReportHistory.


        :param transient: The transient of this ConnectIdentityReportHistory.  # noqa: E501
        :type: bool
        """

        self._transient = transient

    @property
    def credit_type(self):
        """Gets the credit_type of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The credit_type of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: str
        """
        return self._credit_type

    @credit_type.setter
    def credit_type(self, credit_type):
        """Sets the credit_type of this ConnectIdentityReportHistory.


        :param credit_type: The credit_type of this ConnectIdentityReportHistory.  # noqa: E501
        :type: str
        """

        self._credit_type = credit_type

    @property
    def unit_name(self):
        """Gets the unit_name of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The unit_name of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: str
        """
        return self._unit_name

    @unit_name.setter
    def unit_name(self, unit_name):
        """Sets the unit_name of this ConnectIdentityReportHistory.


        :param unit_name: The unit_name of this ConnectIdentityReportHistory.  # noqa: E501
        :type: str
        """

        self._unit_name = unit_name

    @property
    def user_name(self):
        """Gets the user_name of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The user_name of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ConnectIdentityReportHistory.


        :param user_name: The user_name of this ConnectIdentityReportHistory.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def search_date(self):
        """Gets the search_date of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The search_date of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: datetime
        """
        return self._search_date

    @search_date.setter
    def search_date(self, search_date):
        """Sets the search_date of this ConnectIdentityReportHistory.


        :param search_date: The search_date of this ConnectIdentityReportHistory.  # noqa: E501
        :type: datetime
        """

        self._search_date = search_date

    @property
    def search_unit_name(self):
        """Gets the search_unit_name of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The search_unit_name of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: str
        """
        return self._search_unit_name

    @search_unit_name.setter
    def search_unit_name(self, search_unit_name):
        """Sets the search_unit_name of this ConnectIdentityReportHistory.


        :param search_unit_name: The search_unit_name of this ConnectIdentityReportHistory.  # noqa: E501
        :type: str
        """

        self._search_unit_name = search_unit_name

    @property
    def search_organisation_name(self):
        """Gets the search_organisation_name of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The search_organisation_name of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: str
        """
        return self._search_organisation_name

    @search_organisation_name.setter
    def search_organisation_name(self, search_organisation_name):
        """Sets the search_organisation_name of this ConnectIdentityReportHistory.


        :param search_organisation_name: The search_organisation_name of this ConnectIdentityReportHistory.  # noqa: E501
        :type: str
        """

        self._search_organisation_name = search_organisation_name

    @property
    def search_organisation_type(self):
        """Gets the search_organisation_type of this ConnectIdentityReportHistory.  # noqa: E501


        :return: The search_organisation_type of this ConnectIdentityReportHistory.  # noqa: E501
        :rtype: str
        """
        return self._search_organisation_type

    @search_organisation_type.setter
    def search_organisation_type(self, search_organisation_type):
        """Sets the search_organisation_type of this ConnectIdentityReportHistory.


        :param search_organisation_type: The search_organisation_type of this ConnectIdentityReportHistory.  # noqa: E501
        :type: str
        """

        self._search_organisation_type = search_organisation_type

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
        if issubclass(ConnectIdentityReportHistory, dict):
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
        if not isinstance(other, ConnectIdentityReportHistory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

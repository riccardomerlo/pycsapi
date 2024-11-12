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

class PutKYCProfileDetailsByProfileIdRequest(object):
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
        'legal_name': 'str',
        'trading_name': 'str',
        'aliases': 'list[str]',
        'activity': 'str',
        'description': 'str',
        'contact_name': 'str',
        'email': 'str',
        'website': 'str',
        'telephone': 'str',
        'turnover': 'PutKYCProfileDetailsByProfileIdRequestTurnover',
        'assets_under_management': 'PutKYCProfileDetailsByProfileIdRequestAssetsUnderManagement',
        'organization_number': 'str',
        'internal_contact': 'str',
        'internal_email': 'str',
        'date_of_birth': 'date',
        'country_code': 'str',
        'vat_no': 'str',
        'is_listed_on_exchange': 'bool',
        'exchange_name': 'str'
    }

    attribute_map = {
        'legal_name': 'legalName',
        'trading_name': 'tradingName',
        'aliases': 'aliases',
        'activity': 'activity',
        'description': 'description',
        'contact_name': 'contactName',
        'email': 'email',
        'website': 'website',
        'telephone': 'telephone',
        'turnover': 'turnover',
        'assets_under_management': 'assetsUnderManagement',
        'organization_number': 'organizationNumber',
        'internal_contact': 'internalContact',
        'internal_email': 'internalEmail',
        'date_of_birth': 'dateOfBirth',
        'country_code': 'countryCode',
        'vat_no': 'vatNo',
        'is_listed_on_exchange': 'isListedOnExchange',
        'exchange_name': 'exchangeName'
    }

    def __init__(self, legal_name=None, trading_name=None, aliases=None, activity=None, description=None, contact_name=None, email=None, website=None, telephone=None, turnover=None, assets_under_management=None, organization_number=None, internal_contact=None, internal_email=None, date_of_birth=None, country_code=None, vat_no=None, is_listed_on_exchange=None, exchange_name=None):  # noqa: E501
        """PutKYCProfileDetailsByProfileIdRequest - a model defined in Swagger"""  # noqa: E501
        self._legal_name = None
        self._trading_name = None
        self._aliases = None
        self._activity = None
        self._description = None
        self._contact_name = None
        self._email = None
        self._website = None
        self._telephone = None
        self._turnover = None
        self._assets_under_management = None
        self._organization_number = None
        self._internal_contact = None
        self._internal_email = None
        self._date_of_birth = None
        self._country_code = None
        self._vat_no = None
        self._is_listed_on_exchange = None
        self._exchange_name = None
        self.discriminator = None
        self.legal_name = legal_name
        if trading_name is not None:
            self.trading_name = trading_name
        if aliases is not None:
            self.aliases = aliases
        if activity is not None:
            self.activity = activity
        if description is not None:
            self.description = description
        if contact_name is not None:
            self.contact_name = contact_name
        if email is not None:
            self.email = email
        if website is not None:
            self.website = website
        if telephone is not None:
            self.telephone = telephone
        if turnover is not None:
            self.turnover = turnover
        if assets_under_management is not None:
            self.assets_under_management = assets_under_management
        if organization_number is not None:
            self.organization_number = organization_number
        if internal_contact is not None:
            self.internal_contact = internal_contact
        if internal_email is not None:
            self.internal_email = internal_email
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if country_code is not None:
            self.country_code = country_code
        if vat_no is not None:
            self.vat_no = vat_no
        if is_listed_on_exchange is not None:
            self.is_listed_on_exchange = is_listed_on_exchange
        if exchange_name is not None:
            self.exchange_name = exchange_name

    @property
    def legal_name(self):
        """Gets the legal_name of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501

        Name of the Business or Individual<br> Maximum length is 150 characters  # noqa: E501

        :return: The legal_name of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._legal_name

    @legal_name.setter
    def legal_name(self, legal_name):
        """Sets the legal_name of this PutKYCProfileDetailsByProfileIdRequest.

        Name of the Business or Individual<br> Maximum length is 150 characters  # noqa: E501

        :param legal_name: The legal_name of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :type: str
        """
        if legal_name is None:
            raise ValueError("Invalid value for `legal_name`, must not be `None`")  # noqa: E501

        self._legal_name = legal_name

    @property
    def trading_name(self):
        """Gets the trading_name of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501

        Valid for profile type - SoleTrader<br> Maximum length is 150 characters  # noqa: E501

        :return: The trading_name of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._trading_name

    @trading_name.setter
    def trading_name(self, trading_name):
        """Sets the trading_name of this PutKYCProfileDetailsByProfileIdRequest.

        Valid for profile type - SoleTrader<br> Maximum length is 150 characters  # noqa: E501

        :param trading_name: The trading_name of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :type: str
        """

        self._trading_name = trading_name

    @property
    def aliases(self):
        """Gets the aliases of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501

        Name of any Aliases<br> Maximum length of each alias is 150 characters  # noqa: E501

        :return: The aliases of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this PutKYCProfileDetailsByProfileIdRequest.

        Name of any Aliases<br> Maximum length of each alias is 150 characters  # noqa: E501

        :param aliases: The aliases of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :type: list[str]
        """

        self._aliases = aliases

    @property
    def activity(self):
        """Gets the activity of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501

        Activity of the Business e.g. NAIC S/SIC Codes<br> Valid for profile types - Trust, Company, Partnership, OtherEntity and PLC<br> Maximum length of activity is 150 characters  # noqa: E501

        :return: The activity of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this PutKYCProfileDetailsByProfileIdRequest.

        Activity of the Business e.g. NAIC S/SIC Codes<br> Valid for profile types - Trust, Company, Partnership, OtherEntity and PLC<br> Maximum length of activity is 150 characters  # noqa: E501

        :param activity: The activity of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :type: str
        """

        self._activity = activity

    @property
    def description(self):
        """Gets the description of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501

        Description of the business/individual entity<br> Valid for the profile types Trust, Company, Partnership, OtherEntity and PLC  # noqa: E501

        :return: The description of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PutKYCProfileDetailsByProfileIdRequest.

        Description of the business/individual entity<br> Valid for the profile types Trust, Company, Partnership, OtherEntity and PLC  # noqa: E501

        :param description: The description of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def contact_name(self):
        """Gets the contact_name of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501

        Contact person at the organisation.  # noqa: E501

        :return: The contact_name of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._contact_name

    @contact_name.setter
    def contact_name(self, contact_name):
        """Sets the contact_name of this PutKYCProfileDetailsByProfileIdRequest.

        Contact person at the organisation.  # noqa: E501

        :param contact_name: The contact_name of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :type: str
        """

        self._contact_name = contact_name

    @property
    def email(self):
        """Gets the email of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501

        Contact email address of the entity  # noqa: E501

        :return: The email of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this PutKYCProfileDetailsByProfileIdRequest.

        Contact email address of the entity  # noqa: E501

        :param email: The email of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def website(self):
        """Gets the website of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501

        Website address of the entity<br> Valid for the profile types Trust, Company, Partnership, OtherEntity and PLC  # noqa: E501

        :return: The website of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this PutKYCProfileDetailsByProfileIdRequest.

        Website address of the entity<br> Valid for the profile types Trust, Company, Partnership, OtherEntity and PLC  # noqa: E501

        :param website: The website of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def telephone(self):
        """Gets the telephone of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501

        Telephone number of the entity.<br> Valid for the profile types Trust, Company, Partnership, OtherEntity and PLC  # noqa: E501

        :return: The telephone of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone):
        """Sets the telephone of this PutKYCProfileDetailsByProfileIdRequest.

        Telephone number of the entity.<br> Valid for the profile types Trust, Company, Partnership, OtherEntity and PLC  # noqa: E501

        :param telephone: The telephone of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :type: str
        """

        self._telephone = telephone

    @property
    def turnover(self):
        """Gets the turnover of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501


        :return: The turnover of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :rtype: PutKYCProfileDetailsByProfileIdRequestTurnover
        """
        return self._turnover

    @turnover.setter
    def turnover(self, turnover):
        """Sets the turnover of this PutKYCProfileDetailsByProfileIdRequest.


        :param turnover: The turnover of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :type: PutKYCProfileDetailsByProfileIdRequestTurnover
        """

        self._turnover = turnover

    @property
    def assets_under_management(self):
        """Gets the assets_under_management of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501


        :return: The assets_under_management of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :rtype: PutKYCProfileDetailsByProfileIdRequestAssetsUnderManagement
        """
        return self._assets_under_management

    @assets_under_management.setter
    def assets_under_management(self, assets_under_management):
        """Sets the assets_under_management of this PutKYCProfileDetailsByProfileIdRequest.


        :param assets_under_management: The assets_under_management of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :type: PutKYCProfileDetailsByProfileIdRequestAssetsUnderManagement
        """

        self._assets_under_management = assets_under_management

    @property
    def organization_number(self):
        """Gets the organization_number of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501

        Property valid for profile type - Trust, Company, Partnership, OtherEntity and PLC  # noqa: E501

        :return: The organization_number of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._organization_number

    @organization_number.setter
    def organization_number(self, organization_number):
        """Sets the organization_number of this PutKYCProfileDetailsByProfileIdRequest.

        Property valid for profile type - Trust, Company, Partnership, OtherEntity and PLC  # noqa: E501

        :param organization_number: The organization_number of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :type: str
        """

        self._organization_number = organization_number

    @property
    def internal_contact(self):
        """Gets the internal_contact of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501

        Internal contact name to contact regarding this profile,<br> Property valid for profile type - Trust, Company, Partnership, OtherEntity and PLC.  # noqa: E501

        :return: The internal_contact of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._internal_contact

    @internal_contact.setter
    def internal_contact(self, internal_contact):
        """Sets the internal_contact of this PutKYCProfileDetailsByProfileIdRequest.

        Internal contact name to contact regarding this profile,<br> Property valid for profile type - Trust, Company, Partnership, OtherEntity and PLC.  # noqa: E501

        :param internal_contact: The internal_contact of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :type: str
        """

        self._internal_contact = internal_contact

    @property
    def internal_email(self):
        """Gets the internal_email of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501

        Internal email address to contact regarding this profile.<br> Property valid for profile type - Trust, Company, Partnership, OtherEntity and PLC  # noqa: E501

        :return: The internal_email of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._internal_email

    @internal_email.setter
    def internal_email(self, internal_email):
        """Sets the internal_email of this PutKYCProfileDetailsByProfileIdRequest.

        Internal email address to contact regarding this profile.<br> Property valid for profile type - Trust, Company, Partnership, OtherEntity and PLC  # noqa: E501

        :param internal_email: The internal_email of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :type: str
        """

        self._internal_email = internal_email

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501

        Date YYYY-MM-DD or YYYY format. Must be after 1900 and not in the future<br> Valid for the profile types Individual and SoleTrader  # noqa: E501

        :return: The date_of_birth of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :rtype: date
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this PutKYCProfileDetailsByProfileIdRequest.

        Date YYYY-MM-DD or YYYY format. Must be after 1900 and not in the future<br> Valid for the profile types Individual and SoleTrader  # noqa: E501

        :param date_of_birth: The date_of_birth of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :type: date
        """

        self._date_of_birth = date_of_birth

    @property
    def country_code(self):
        """Gets the country_code of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501

        Two-letter country code ISO-3166-2.<br> Valid for the profile types Individual and SoleTrader  # noqa: E501

        :return: The country_code of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this PutKYCProfileDetailsByProfileIdRequest.

        Two-letter country code ISO-3166-2.<br> Valid for the profile types Individual and SoleTrader  # noqa: E501

        :param country_code: The country_code of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def vat_no(self):
        """Gets the vat_no of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501

        Tax Identification Number of the business<br> Valid for the profile types Company, Partnership, OtherEntity and PLC  # noqa: E501

        :return: The vat_no of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._vat_no

    @vat_no.setter
    def vat_no(self, vat_no):
        """Sets the vat_no of this PutKYCProfileDetailsByProfileIdRequest.

        Tax Identification Number of the business<br> Valid for the profile types Company, Partnership, OtherEntity and PLC  # noqa: E501

        :param vat_no: The vat_no of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :type: str
        """

        self._vat_no = vat_no

    @property
    def is_listed_on_exchange(self):
        """Gets the is_listed_on_exchange of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501

        Property valid for profile type PLC  # noqa: E501

        :return: The is_listed_on_exchange of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_listed_on_exchange

    @is_listed_on_exchange.setter
    def is_listed_on_exchange(self, is_listed_on_exchange):
        """Sets the is_listed_on_exchange of this PutKYCProfileDetailsByProfileIdRequest.

        Property valid for profile type PLC  # noqa: E501

        :param is_listed_on_exchange: The is_listed_on_exchange of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :type: bool
        """

        self._is_listed_on_exchange = is_listed_on_exchange

    @property
    def exchange_name(self):
        """Gets the exchange_name of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501

        Property valid for profile type PLC  # noqa: E501

        :return: The exchange_name of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._exchange_name

    @exchange_name.setter
    def exchange_name(self, exchange_name):
        """Sets the exchange_name of this PutKYCProfileDetailsByProfileIdRequest.

        Property valid for profile type PLC  # noqa: E501

        :param exchange_name: The exchange_name of this PutKYCProfileDetailsByProfileIdRequest.  # noqa: E501
        :type: str
        """

        self._exchange_name = exchange_name

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
        if issubclass(PutKYCProfileDetailsByProfileIdRequest, dict):
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
        if not isinstance(other, PutKYCProfileDetailsByProfileIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

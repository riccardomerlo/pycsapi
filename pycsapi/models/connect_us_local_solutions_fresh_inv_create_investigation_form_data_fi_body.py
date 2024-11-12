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

class ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody(object):
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
        'company_id': 'str',
        'comments': 'str',
        'company_name': 'str',
        'consent': 'str',
        'customer_email': 'str',
        'customer_id': 'str',
        'customer_name': 'str',
        'customer_phone_no': 'str',
        'customer_user_id': 'str',
        'executive_name': 'str',
        'ip_address': 'str',
        'target_building_number': 'str',
        'target_city': 'str',
        'target_company_name': 'str',
        'target_contact': 'str',
        'target_phone_no': 'str',
        'target_sos_number': 'str',
        'target_state': 'str',
        'target_street': 'str',
        'target_tax_id': 'str',
        'target_trade_name': 'str',
        'target_website_url': 'str',
        'target_zip': 'str'
    }

    attribute_map = {
        'company_id': 'companyId',
        'comments': 'comments',
        'company_name': 'companyName',
        'consent': 'consent',
        'customer_email': 'customerEmail',
        'customer_id': 'customerId',
        'customer_name': 'customerName',
        'customer_phone_no': 'customerPhoneNo',
        'customer_user_id': 'customerUserId',
        'executive_name': 'executiveName',
        'ip_address': 'ipAddress',
        'target_building_number': 'targetBuildingNumber',
        'target_city': 'targetCity',
        'target_company_name': 'targetCompanyName',
        'target_contact': 'targetContact',
        'target_phone_no': 'targetPhoneNo',
        'target_sos_number': 'targetSosNumber',
        'target_state': 'targetState',
        'target_street': 'targetStreet',
        'target_tax_id': 'targetTaxId',
        'target_trade_name': 'targetTradeName',
        'target_website_url': 'targetWebsiteUrl',
        'target_zip': 'targetZip'
    }

    def __init__(self, company_id=None, comments=None, company_name=None, consent=None, customer_email=None, customer_id=None, customer_name=None, customer_phone_no=None, customer_user_id=None, executive_name=None, ip_address=None, target_building_number=None, target_city=None, target_company_name=None, target_contact=None, target_phone_no=None, target_sos_number=None, target_state=None, target_street=None, target_tax_id=None, target_trade_name=None, target_website_url=None, target_zip=None):  # noqa: E501
        """ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody - a model defined in Swagger"""  # noqa: E501
        self._company_id = None
        self._comments = None
        self._company_name = None
        self._consent = None
        self._customer_email = None
        self._customer_id = None
        self._customer_name = None
        self._customer_phone_no = None
        self._customer_user_id = None
        self._executive_name = None
        self._ip_address = None
        self._target_building_number = None
        self._target_city = None
        self._target_company_name = None
        self._target_contact = None
        self._target_phone_no = None
        self._target_sos_number = None
        self._target_state = None
        self._target_street = None
        self._target_tax_id = None
        self._target_trade_name = None
        self._target_website_url = None
        self._target_zip = None
        self.discriminator = None
        if company_id is not None:
            self.company_id = company_id
        if comments is not None:
            self.comments = comments
        if company_name is not None:
            self.company_name = company_name
        if consent is not None:
            self.consent = consent
        if customer_email is not None:
            self.customer_email = customer_email
        if customer_id is not None:
            self.customer_id = customer_id
        if customer_name is not None:
            self.customer_name = customer_name
        if customer_phone_no is not None:
            self.customer_phone_no = customer_phone_no
        if customer_user_id is not None:
            self.customer_user_id = customer_user_id
        if executive_name is not None:
            self.executive_name = executive_name
        if ip_address is not None:
            self.ip_address = ip_address
        if target_building_number is not None:
            self.target_building_number = target_building_number
        if target_city is not None:
            self.target_city = target_city
        if target_company_name is not None:
            self.target_company_name = target_company_name
        if target_contact is not None:
            self.target_contact = target_contact
        if target_phone_no is not None:
            self.target_phone_no = target_phone_no
        if target_sos_number is not None:
            self.target_sos_number = target_sos_number
        if target_state is not None:
            self.target_state = target_state
        if target_street is not None:
            self.target_street = target_street
        if target_tax_id is not None:
            self.target_tax_id = target_tax_id
        if target_trade_name is not None:
            self.target_trade_name = target_trade_name
        if target_website_url is not None:
            self.target_website_url = target_website_url
        if target_zip is not None:
            self.target_zip = target_zip

    @property
    def company_id(self):
        """Gets the company_id of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        Unique identifier for the company on behalf of which the investigation is being conducted.  # noqa: E501

        :return: The company_id of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        Unique identifier for the company on behalf of which the investigation is being conducted.  # noqa: E501

        :param company_id: The company_id of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def comments(self):
        """Gets the comments of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        Additional comments or instructions provided by the customer to guide the investigation process.  # noqa: E501

        :return: The comments of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        Additional comments or instructions provided by the customer to guide the investigation process.  # noqa: E501

        :param comments: The comments of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._comments = comments

    @property
    def company_name(self):
        """Gets the company_name of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        The name of the company initiating the investigation.  # noqa: E501

        :return: The company_name of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        The name of the company initiating the investigation.  # noqa: E501

        :param company_name: The company_name of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def consent(self):
        """Gets the consent of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        Explicit consent provided by the customer for conducting the investigation, usually required for legal compliance.  # noqa: E501

        :return: The consent of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._consent

    @consent.setter
    def consent(self, consent):
        """Sets the consent of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        Explicit consent provided by the customer for conducting the investigation, usually required for legal compliance.  # noqa: E501

        :param consent: The consent of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._consent = consent

    @property
    def customer_email(self):
        """Gets the customer_email of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        Email address of the customer initiating the investigation.  # noqa: E501

        :return: The customer_email of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._customer_email

    @customer_email.setter
    def customer_email(self, customer_email):
        """Sets the customer_email of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        Email address of the customer initiating the investigation.  # noqa: E501

        :param customer_email: The customer_email of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._customer_email = customer_email

    @property
    def customer_id(self):
        """Gets the customer_id of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        Unique identifier of the customer requesting the investigation.  # noqa: E501

        :return: The customer_id of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        Unique identifier of the customer requesting the investigation.  # noqa: E501

        :param customer_id: The customer_id of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def customer_name(self):
        """Gets the customer_name of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        Full name of the customer who is initiating the investigation.  # noqa: E501

        :return: The customer_name of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """Sets the customer_name of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        Full name of the customer who is initiating the investigation.  # noqa: E501

        :param customer_name: The customer_name of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._customer_name = customer_name

    @property
    def customer_phone_no(self):
        """Gets the customer_phone_no of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        Phone number of the customer, used for contact purposes related to the investigation.  # noqa: E501

        :return: The customer_phone_no of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._customer_phone_no

    @customer_phone_no.setter
    def customer_phone_no(self, customer_phone_no):
        """Sets the customer_phone_no of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        Phone number of the customer, used for contact purposes related to the investigation.  # noqa: E501

        :param customer_phone_no: The customer_phone_no of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._customer_phone_no = customer_phone_no

    @property
    def customer_user_id(self):
        """Gets the customer_user_id of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        Unique user identifier for the customer within the system.  # noqa: E501

        :return: The customer_user_id of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._customer_user_id

    @customer_user_id.setter
    def customer_user_id(self, customer_user_id):
        """Sets the customer_user_id of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        Unique user identifier for the customer within the system.  # noqa: E501

        :param customer_user_id: The customer_user_id of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._customer_user_id = customer_user_id

    @property
    def executive_name(self):
        """Gets the executive_name of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        Name of the executive or representative of the company who is directly handling the investigation.  # noqa: E501

        :return: The executive_name of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._executive_name

    @executive_name.setter
    def executive_name(self, executive_name):
        """Sets the executive_name of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        Name of the executive or representative of the company who is directly handling the investigation.  # noqa: E501

        :param executive_name: The executive_name of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._executive_name = executive_name

    @property
    def ip_address(self):
        """Gets the ip_address of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        IP address from which the investigation request was submitted, used for logging or security purposes.  # noqa: E501

        :return: The ip_address of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        IP address from which the investigation request was submitted, used for logging or security purposes.  # noqa: E501

        :param ip_address: The ip_address of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._ip_address = ip_address

    @property
    def target_building_number(self):
        """Gets the target_building_number of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        The building number of the address associated with the target of the investigation.  # noqa: E501

        :return: The target_building_number of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._target_building_number

    @target_building_number.setter
    def target_building_number(self, target_building_number):
        """Sets the target_building_number of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        The building number of the address associated with the target of the investigation.  # noqa: E501

        :param target_building_number: The target_building_number of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._target_building_number = target_building_number

    @property
    def target_city(self):
        """Gets the target_city of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        The city where the target of the investigation is located.  # noqa: E501

        :return: The target_city of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._target_city

    @target_city.setter
    def target_city(self, target_city):
        """Sets the target_city of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        The city where the target of the investigation is located.  # noqa: E501

        :param target_city: The target_city of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._target_city = target_city

    @property
    def target_company_name(self):
        """Gets the target_company_name of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        The legal name of the company being investigated.  # noqa: E501

        :return: The target_company_name of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._target_company_name

    @target_company_name.setter
    def target_company_name(self, target_company_name):
        """Sets the target_company_name of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        The legal name of the company being investigated.  # noqa: E501

        :param target_company_name: The target_company_name of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._target_company_name = target_company_name

    @property
    def target_contact(self):
        """Gets the target_contact of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        Contact information for the target of the investigation, such as a direct phone number or email.  # noqa: E501

        :return: The target_contact of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._target_contact

    @target_contact.setter
    def target_contact(self, target_contact):
        """Sets the target_contact of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        Contact information for the target of the investigation, such as a direct phone number or email.  # noqa: E501

        :param target_contact: The target_contact of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._target_contact = target_contact

    @property
    def target_phone_no(self):
        """Gets the target_phone_no of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        Phone number associated with the target of the investigation.  # noqa: E501

        :return: The target_phone_no of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._target_phone_no

    @target_phone_no.setter
    def target_phone_no(self, target_phone_no):
        """Sets the target_phone_no of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        Phone number associated with the target of the investigation.  # noqa: E501

        :param target_phone_no: The target_phone_no of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._target_phone_no = target_phone_no

    @property
    def target_sos_number(self):
        """Gets the target_sos_number of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        Secretary of State file number or other governmental identifier for the target entity.  # noqa: E501

        :return: The target_sos_number of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._target_sos_number

    @target_sos_number.setter
    def target_sos_number(self, target_sos_number):
        """Sets the target_sos_number of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        Secretary of State file number or other governmental identifier for the target entity.  # noqa: E501

        :param target_sos_number: The target_sos_number of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._target_sos_number = target_sos_number

    @property
    def target_state(self):
        """Gets the target_state of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        State in which the target of the investigation is located.  # noqa: E501

        :return: The target_state of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._target_state

    @target_state.setter
    def target_state(self, target_state):
        """Sets the target_state of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        State in which the target of the investigation is located.  # noqa: E501

        :param target_state: The target_state of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._target_state = target_state

    @property
    def target_street(self):
        """Gets the target_street of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        Street address of the target entity.  # noqa: E501

        :return: The target_street of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._target_street

    @target_street.setter
    def target_street(self, target_street):
        """Sets the target_street of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        Street address of the target entity.  # noqa: E501

        :param target_street: The target_street of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._target_street = target_street

    @property
    def target_tax_id(self):
        """Gets the target_tax_id of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        Tax identification number of the target company, used for verifying its business identity.  # noqa: E501

        :return: The target_tax_id of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._target_tax_id

    @target_tax_id.setter
    def target_tax_id(self, target_tax_id):
        """Sets the target_tax_id of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        Tax identification number of the target company, used for verifying its business identity.  # noqa: E501

        :param target_tax_id: The target_tax_id of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._target_tax_id = target_tax_id

    @property
    def target_trade_name(self):
        """Gets the target_trade_name of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        Trade name or DBA (Doing Business As) under which the target company operates, if different from the legal name.  # noqa: E501

        :return: The target_trade_name of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._target_trade_name

    @target_trade_name.setter
    def target_trade_name(self, target_trade_name):
        """Sets the target_trade_name of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        Trade name or DBA (Doing Business As) under which the target company operates, if different from the legal name.  # noqa: E501

        :param target_trade_name: The target_trade_name of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._target_trade_name = target_trade_name

    @property
    def target_website_url(self):
        """Gets the target_website_url of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        URL of the target company's website, providing a direct link to their online presence.  # noqa: E501

        :return: The target_website_url of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._target_website_url

    @target_website_url.setter
    def target_website_url(self, target_website_url):
        """Sets the target_website_url of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        URL of the target company's website, providing a direct link to their online presence.  # noqa: E501

        :param target_website_url: The target_website_url of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._target_website_url = target_website_url

    @property
    def target_zip(self):
        """Gets the target_zip of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501

        Postal code for the target company's location, used for further location-specific investigations.  # noqa: E501

        :return: The target_zip of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :rtype: str
        """
        return self._target_zip

    @target_zip.setter
    def target_zip(self, target_zip):
        """Sets the target_zip of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.

        Postal code for the target company's location, used for further location-specific investigations.  # noqa: E501

        :param target_zip: The target_zip of this ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody.  # noqa: E501
        :type: str
        """

        self._target_zip = target_zip

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
        if issubclass(ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody, dict):
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
        if not isinstance(other, ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

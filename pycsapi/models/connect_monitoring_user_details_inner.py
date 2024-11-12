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

class ConnectMonitoringUserDetailsInner(object):
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
        'country_code': 'str',
        'created_date': 'datetime',
        'cs_customer_id': 'float',
        'cs_user_id': 'float',
        'is_auto_tracker': 'bool',
        'language_code': 'str',
        'last_access_date': 'datetime',
        'modified_date': 'datetime',
        'contract_end_date': 'datetime',
        'user_id': 'float'
    }

    attribute_map = {
        'country_code': 'countryCode',
        'created_date': 'createdDate',
        'cs_customer_id': 'csCustomerId',
        'cs_user_id': 'csUserId',
        'is_auto_tracker': 'isAutoTracker',
        'language_code': 'languageCode',
        'last_access_date': 'lastAccessDate',
        'modified_date': 'modifiedDate',
        'contract_end_date': 'contractEndDate',
        'user_id': 'userId'
    }

    def __init__(self, country_code=None, created_date=None, cs_customer_id=None, cs_user_id=None, is_auto_tracker=None, language_code=None, last_access_date=None, modified_date=None, contract_end_date=None, user_id=None):  # noqa: E501
        """ConnectMonitoringUserDetailsInner - a model defined in Swagger"""  # noqa: E501
        self._country_code = None
        self._created_date = None
        self._cs_customer_id = None
        self._cs_user_id = None
        self._is_auto_tracker = None
        self._language_code = None
        self._last_access_date = None
        self._modified_date = None
        self._contract_end_date = None
        self._user_id = None
        self.discriminator = None
        if country_code is not None:
            self.country_code = country_code
        if created_date is not None:
            self.created_date = created_date
        if cs_customer_id is not None:
            self.cs_customer_id = cs_customer_id
        if cs_user_id is not None:
            self.cs_user_id = cs_user_id
        if is_auto_tracker is not None:
            self.is_auto_tracker = is_auto_tracker
        if language_code is not None:
            self.language_code = language_code
        if last_access_date is not None:
            self.last_access_date = last_access_date
        if modified_date is not None:
            self.modified_date = modified_date
        if contract_end_date is not None:
            self.contract_end_date = contract_end_date
        if user_id is not None:
            self.user_id = user_id

    @property
    def country_code(self):
        """Gets the country_code of this ConnectMonitoringUserDetailsInner.  # noqa: E501

        The ISO/Alpha 2 format country code for the user's country.  # noqa: E501

        :return: The country_code of this ConnectMonitoringUserDetailsInner.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this ConnectMonitoringUserDetailsInner.

        The ISO/Alpha 2 format country code for the user's country.  # noqa: E501

        :param country_code: The country_code of this ConnectMonitoringUserDetailsInner.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def created_date(self):
        """Gets the created_date of this ConnectMonitoringUserDetailsInner.  # noqa: E501

        The date that the Global Monitoring user account was created.  # noqa: E501

        :return: The created_date of this ConnectMonitoringUserDetailsInner.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this ConnectMonitoringUserDetailsInner.

        The date that the Global Monitoring user account was created.  # noqa: E501

        :param created_date: The created_date of this ConnectMonitoringUserDetailsInner.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def cs_customer_id(self):
        """Gets the cs_customer_id of this ConnectMonitoringUserDetailsInner.  # noqa: E501

        The unique identifier for the user's customer account, used across the Creditsafe product suite.  # noqa: E501

        :return: The cs_customer_id of this ConnectMonitoringUserDetailsInner.  # noqa: E501
        :rtype: float
        """
        return self._cs_customer_id

    @cs_customer_id.setter
    def cs_customer_id(self, cs_customer_id):
        """Sets the cs_customer_id of this ConnectMonitoringUserDetailsInner.

        The unique identifier for the user's customer account, used across the Creditsafe product suite.  # noqa: E501

        :param cs_customer_id: The cs_customer_id of this ConnectMonitoringUserDetailsInner.  # noqa: E501
        :type: float
        """

        self._cs_customer_id = cs_customer_id

    @property
    def cs_user_id(self):
        """Gets the cs_user_id of this ConnectMonitoringUserDetailsInner.  # noqa: E501

        The unique identifier for the user's account, used across the Creditsafe product suite.  # noqa: E501

        :return: The cs_user_id of this ConnectMonitoringUserDetailsInner.  # noqa: E501
        :rtype: float
        """
        return self._cs_user_id

    @cs_user_id.setter
    def cs_user_id(self, cs_user_id):
        """Sets the cs_user_id of this ConnectMonitoringUserDetailsInner.

        The unique identifier for the user's account, used across the Creditsafe product suite.  # noqa: E501

        :param cs_user_id: The cs_user_id of this ConnectMonitoringUserDetailsInner.  # noqa: E501
        :type: float
        """

        self._cs_user_id = cs_user_id

    @property
    def is_auto_tracker(self):
        """Gets the is_auto_tracker of this ConnectMonitoringUserDetailsInner.  # noqa: E501

        If auto-tracker is enabled, any companies that you pull a credit report for are automatically added to the portfolio that you have selected as default.  # noqa: E501

        :return: The is_auto_tracker of this ConnectMonitoringUserDetailsInner.  # noqa: E501
        :rtype: bool
        """
        return self._is_auto_tracker

    @is_auto_tracker.setter
    def is_auto_tracker(self, is_auto_tracker):
        """Sets the is_auto_tracker of this ConnectMonitoringUserDetailsInner.

        If auto-tracker is enabled, any companies that you pull a credit report for are automatically added to the portfolio that you have selected as default.  # noqa: E501

        :param is_auto_tracker: The is_auto_tracker of this ConnectMonitoringUserDetailsInner.  # noqa: E501
        :type: bool
        """

        self._is_auto_tracker = is_auto_tracker

    @property
    def language_code(self):
        """Gets the language_code of this ConnectMonitoringUserDetailsInner.  # noqa: E501

        The language code for the user's preferred language.  # noqa: E501

        :return: The language_code of this ConnectMonitoringUserDetailsInner.  # noqa: E501
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this ConnectMonitoringUserDetailsInner.

        The language code for the user's preferred language.  # noqa: E501

        :param language_code: The language_code of this ConnectMonitoringUserDetailsInner.  # noqa: E501
        :type: str
        """

        self._language_code = language_code

    @property
    def last_access_date(self):
        """Gets the last_access_date of this ConnectMonitoringUserDetailsInner.  # noqa: E501

        The date the the user last accessed the Global Monitoring product.  # noqa: E501

        :return: The last_access_date of this ConnectMonitoringUserDetailsInner.  # noqa: E501
        :rtype: datetime
        """
        return self._last_access_date

    @last_access_date.setter
    def last_access_date(self, last_access_date):
        """Sets the last_access_date of this ConnectMonitoringUserDetailsInner.

        The date the the user last accessed the Global Monitoring product.  # noqa: E501

        :param last_access_date: The last_access_date of this ConnectMonitoringUserDetailsInner.  # noqa: E501
        :type: datetime
        """

        self._last_access_date = last_access_date

    @property
    def modified_date(self):
        """Gets the modified_date of this ConnectMonitoringUserDetailsInner.  # noqa: E501

        The date that the user's details were last modified.  # noqa: E501

        :return: The modified_date of this ConnectMonitoringUserDetailsInner.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this ConnectMonitoringUserDetailsInner.

        The date that the user's details were last modified.  # noqa: E501

        :param modified_date: The modified_date of this ConnectMonitoringUserDetailsInner.  # noqa: E501
        :type: datetime
        """

        self._modified_date = modified_date

    @property
    def contract_end_date(self):
        """Gets the contract_end_date of this ConnectMonitoringUserDetailsInner.  # noqa: E501

        The date that the user's contract is currently set to expire. From this date onward, the user will be unable to access to Global Monitoring product.  # noqa: E501

        :return: The contract_end_date of this ConnectMonitoringUserDetailsInner.  # noqa: E501
        :rtype: datetime
        """
        return self._contract_end_date

    @contract_end_date.setter
    def contract_end_date(self, contract_end_date):
        """Sets the contract_end_date of this ConnectMonitoringUserDetailsInner.

        The date that the user's contract is currently set to expire. From this date onward, the user will be unable to access to Global Monitoring product.  # noqa: E501

        :param contract_end_date: The contract_end_date of this ConnectMonitoringUserDetailsInner.  # noqa: E501
        :type: datetime
        """

        self._contract_end_date = contract_end_date

    @property
    def user_id(self):
        """Gets the user_id of this ConnectMonitoringUserDetailsInner.  # noqa: E501

        The internal identifier used to reference the user's account through the Global Monitoring product.  # noqa: E501

        :return: The user_id of this ConnectMonitoringUserDetailsInner.  # noqa: E501
        :rtype: float
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ConnectMonitoringUserDetailsInner.

        The internal identifier used to reference the user's account through the Global Monitoring product.  # noqa: E501

        :param user_id: The user_id of this ConnectMonitoringUserDetailsInner.  # noqa: E501
        :type: float
        """

        self._user_id = user_id

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
        if issubclass(ConnectMonitoringUserDetailsInner, dict):
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
        if not isinstance(other, ConnectMonitoringUserDetailsInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

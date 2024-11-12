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

class ConnectMonitoringEventRulesResponseInner(object):
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
        'is_active': 'bool',
        'rule_code': 'float',
        'rule_country_code': 'str',
        'rule_type': 'float',
        'rule_type_name': 'str',
        'name': 'str',
        'param0': 'str',
        'param1': 'str'
    }

    attribute_map = {
        'is_active': 'isActive',
        'rule_code': 'ruleCode',
        'rule_country_code': 'ruleCountryCode',
        'rule_type': 'ruleType',
        'rule_type_name': 'ruleTypeName',
        'name': 'name',
        'param0': 'param0',
        'param1': 'param1'
    }

    def __init__(self, is_active=None, rule_code=None, rule_country_code=None, rule_type=None, rule_type_name=None, name=None, param0=None, param1=None):  # noqa: E501
        """ConnectMonitoringEventRulesResponseInner - a model defined in Swagger"""  # noqa: E501
        self._is_active = None
        self._rule_code = None
        self._rule_country_code = None
        self._rule_type = None
        self._rule_type_name = None
        self._name = None
        self._param0 = None
        self._param1 = None
        self.discriminator = None
        if is_active is not None:
            self.is_active = is_active
        if rule_code is not None:
            self.rule_code = rule_code
        if rule_country_code is not None:
            self.rule_country_code = rule_country_code
        if rule_type is not None:
            self.rule_type = rule_type
        if rule_type_name is not None:
            self.rule_type_name = rule_type_name
        if name is not None:
            self.name = name
        if param0 is not None:
            self.param0 = param0
        if param1 is not None:
            self.param1 = param1

    @property
    def is_active(self):
        """Gets the is_active of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501

        Shows whether the notification event rule has been enabled for the given portfolio.  # noqa: E501

        :return: The is_active of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this ConnectMonitoringEventRulesResponseInner.

        Shows whether the notification event rule has been enabled for the given portfolio.  # noqa: E501

        :param is_active: The is_active of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def rule_code(self):
        """Gets the rule_code of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501

        The unique identifier for the notification event rule.  # noqa: E501

        :return: The rule_code of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501
        :rtype: float
        """
        return self._rule_code

    @rule_code.setter
    def rule_code(self, rule_code):
        """Sets the rule_code of this ConnectMonitoringEventRulesResponseInner.

        The unique identifier for the notification event rule.  # noqa: E501

        :param rule_code: The rule_code of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501
        :type: float
        """

        self._rule_code = rule_code

    @property
    def rule_country_code(self):
        """Gets the rule_country_code of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501

        The ISO/Alpha 2 format country code for the notification event rule. \"XX\" is used for global rules that apply to companies from all countries.  # noqa: E501

        :return: The rule_country_code of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._rule_country_code

    @rule_country_code.setter
    def rule_country_code(self, rule_country_code):
        """Sets the rule_country_code of this ConnectMonitoringEventRulesResponseInner.

        The ISO/Alpha 2 format country code for the notification event rule. \"XX\" is used for global rules that apply to companies from all countries.  # noqa: E501

        :param rule_country_code: The rule_country_code of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501
        :type: str
        """

        self._rule_country_code = rule_country_code

    @property
    def rule_type(self):
        """Gets the rule_type of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501

        The unique identifier of the `ruleType` for the notification event rule.  # noqa: E501

        :return: The rule_type of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501
        :rtype: float
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this ConnectMonitoringEventRulesResponseInner.

        The unique identifier of the `ruleType` for the notification event rule.  # noqa: E501

        :param rule_type: The rule_type of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501
        :type: float
        """

        self._rule_type = rule_type

    @property
    def rule_type_name(self):
        """Gets the rule_type_name of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501

        A short description of the `ruleType` for the notification event rule.  # noqa: E501

        :return: The rule_type_name of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._rule_type_name

    @rule_type_name.setter
    def rule_type_name(self, rule_type_name):
        """Sets the rule_type_name of this ConnectMonitoringEventRulesResponseInner.

        A short description of the `ruleType` for the notification event rule.  # noqa: E501

        :param rule_type_name: The rule_type_name of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501
        :type: str
        """

        self._rule_type_name = rule_type_name

    @property
    def name(self):
        """Gets the name of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501

        The name for the notification event rule.  # noqa: E501

        :return: The name of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectMonitoringEventRulesResponseInner.

        The name for the notification event rule.  # noqa: E501

        :param name: The name of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def param0(self):
        """Gets the param0 of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501

        Some notification event rules may include input parameters used to tailor the notifications generated to your preference.  # noqa: E501

        :return: The param0 of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._param0

    @param0.setter
    def param0(self, param0):
        """Sets the param0 of this ConnectMonitoringEventRulesResponseInner.

        Some notification event rules may include input parameters used to tailor the notifications generated to your preference.  # noqa: E501

        :param param0: The param0 of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501
        :type: str
        """

        self._param0 = param0

    @property
    def param1(self):
        """Gets the param1 of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501

        Some notification event rules may include input parameters used to tailor the notifications generated to your preference.  # noqa: E501

        :return: The param1 of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501
        :rtype: str
        """
        return self._param1

    @param1.setter
    def param1(self, param1):
        """Sets the param1 of this ConnectMonitoringEventRulesResponseInner.

        Some notification event rules may include input parameters used to tailor the notifications generated to your preference.  # noqa: E501

        :param param1: The param1 of this ConnectMonitoringEventRulesResponseInner.  # noqa: E501
        :type: str
        """

        self._param1 = param1

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
        if issubclass(ConnectMonitoringEventRulesResponseInner, dict):
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
        if not isinstance(other, ConnectMonitoringEventRulesResponseInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

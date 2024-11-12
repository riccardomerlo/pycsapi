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

class ConnectMonitoringAllNotificationsEventsData(object):
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
        'company': 'ConnectMonitoringCompanyInfo',
        'event_id': 'float',
        'event_date': 'datetime',
        'new_value': 'str',
        'old_value': 'str',
        'notification_event_id': 'float',
        'notification_id': 'float',
        'processed_date': 'datetime',
        'rule_code': 'float',
        'rule_name': 'str',
        'summary': 'str',
        'rule_text': 'str',
        'local_event_code': 'str',
        'is_processed': 'bool'
    }

    attribute_map = {
        'company': 'company',
        'event_id': 'eventId',
        'event_date': 'eventDate',
        'new_value': 'newValue',
        'old_value': 'oldValue',
        'notification_event_id': 'notificationEventId',
        'notification_id': 'notificationId',
        'processed_date': 'processedDate',
        'rule_code': 'ruleCode',
        'rule_name': 'ruleName',
        'summary': 'summary',
        'rule_text': 'ruleText',
        'local_event_code': 'localEventCode',
        'is_processed': 'isProcessed'
    }

    def __init__(self, company=None, event_id=None, event_date=None, new_value=None, old_value=None, notification_event_id=None, notification_id=None, processed_date=None, rule_code=None, rule_name=None, summary=None, rule_text=None, local_event_code=None, is_processed=None):  # noqa: E501
        """ConnectMonitoringAllNotificationsEventsData - a model defined in Swagger"""  # noqa: E501
        self._company = None
        self._event_id = None
        self._event_date = None
        self._new_value = None
        self._old_value = None
        self._notification_event_id = None
        self._notification_id = None
        self._processed_date = None
        self._rule_code = None
        self._rule_name = None
        self._summary = None
        self._rule_text = None
        self._local_event_code = None
        self._is_processed = None
        self.discriminator = None
        if company is not None:
            self.company = company
        if event_id is not None:
            self.event_id = event_id
        if event_date is not None:
            self.event_date = event_date
        if new_value is not None:
            self.new_value = new_value
        if old_value is not None:
            self.old_value = old_value
        if notification_event_id is not None:
            self.notification_event_id = notification_event_id
        if notification_id is not None:
            self.notification_id = notification_id
        if processed_date is not None:
            self.processed_date = processed_date
        if rule_code is not None:
            self.rule_code = rule_code
        if rule_name is not None:
            self.rule_name = rule_name
        if summary is not None:
            self.summary = summary
        if rule_text is not None:
            self.rule_text = rule_text
        if local_event_code is not None:
            self.local_event_code = local_event_code
        if is_processed is not None:
            self.is_processed = is_processed

    @property
    def company(self):
        """Gets the company of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501


        :return: The company of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :rtype: ConnectMonitoringCompanyInfo
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this ConnectMonitoringAllNotificationsEventsData.


        :param company: The company of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :type: ConnectMonitoringCompanyInfo
        """

        self._company = company

    @property
    def event_id(self):
        """Gets the event_id of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501

        The unique identifier of the event that triggered the generation of the `notificationEvent`. This identifier is consistent across all portfolios in the Global Monitoring product.  # noqa: E501

        :return: The event_id of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :rtype: float
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this ConnectMonitoringAllNotificationsEventsData.

        The unique identifier of the event that triggered the generation of the `notificationEvent`. This identifier is consistent across all portfolios in the Global Monitoring product.  # noqa: E501

        :param event_id: The event_id of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :type: float
        """

        self._event_id = event_id

    @property
    def event_date(self):
        """Gets the event_date of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501

        The date that the event occurred.  # noqa: E501

        :return: The event_date of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :rtype: datetime
        """
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        """Sets the event_date of this ConnectMonitoringAllNotificationsEventsData.

        The date that the event occurred.  # noqa: E501

        :param event_date: The event_date of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :type: datetime
        """

        self._event_date = event_date

    @property
    def new_value(self):
        """Gets the new_value of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501

        Some events contain an `oldValue` and `newValue` (e.g. a change in Credit Limit).  # noqa: E501

        :return: The new_value of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """Sets the new_value of this ConnectMonitoringAllNotificationsEventsData.

        Some events contain an `oldValue` and `newValue` (e.g. a change in Credit Limit).  # noqa: E501

        :param new_value: The new_value of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :type: str
        """

        self._new_value = new_value

    @property
    def old_value(self):
        """Gets the old_value of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501

        Some events contain an `oldValue` and `newValue` (e.g. a change in Credit Limit).  # noqa: E501

        :return: The old_value of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        """Sets the old_value of this ConnectMonitoringAllNotificationsEventsData.

        Some events contain an `oldValue` and `newValue` (e.g. a change in Credit Limit).  # noqa: E501

        :param old_value: The old_value of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :type: str
        """

        self._old_value = old_value

    @property
    def notification_event_id(self):
        """Gets the notification_event_id of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501

        The unique identifier for the `notificationEvent`. This identifier is tied to a specific `eventId` and `portfolioId`.  # noqa: E501

        :return: The notification_event_id of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :rtype: float
        """
        return self._notification_event_id

    @notification_event_id.setter
    def notification_event_id(self, notification_event_id):
        """Sets the notification_event_id of this ConnectMonitoringAllNotificationsEventsData.

        The unique identifier for the `notificationEvent`. This identifier is tied to a specific `eventId` and `portfolioId`.  # noqa: E501

        :param notification_event_id: The notification_event_id of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :type: float
        """

        self._notification_event_id = notification_event_id

    @property
    def notification_id(self):
        """Gets the notification_id of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501

        The unique identifier for the `notificationEvent`. This identifier is tied to a specific `eventId` and `portfolioId`.  # noqa: E501

        :return: The notification_id of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :rtype: float
        """
        return self._notification_id

    @notification_id.setter
    def notification_id(self, notification_id):
        """Sets the notification_id of this ConnectMonitoringAllNotificationsEventsData.

        The unique identifier for the `notificationEvent`. This identifier is tied to a specific `eventId` and `portfolioId`.  # noqa: E501

        :param notification_id: The notification_id of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :type: float
        """

        self._notification_id = notification_id

    @property
    def processed_date(self):
        """Gets the processed_date of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501

        If the Notification was sent by email, the date will be populated with when the notification was sent.  # noqa: E501

        :return: The processed_date of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :rtype: datetime
        """
        return self._processed_date

    @processed_date.setter
    def processed_date(self, processed_date):
        """Sets the processed_date of this ConnectMonitoringAllNotificationsEventsData.

        If the Notification was sent by email, the date will be populated with when the notification was sent.  # noqa: E501

        :param processed_date: The processed_date of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :type: datetime
        """

        self._processed_date = processed_date

    @property
    def rule_code(self):
        """Gets the rule_code of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501

        The unique identifier for the `ruleCode` that triggered the generation of the `notificationEvent`.  # noqa: E501

        :return: The rule_code of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :rtype: float
        """
        return self._rule_code

    @rule_code.setter
    def rule_code(self, rule_code):
        """Sets the rule_code of this ConnectMonitoringAllNotificationsEventsData.

        The unique identifier for the `ruleCode` that triggered the generation of the `notificationEvent`.  # noqa: E501

        :param rule_code: The rule_code of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :type: float
        """

        self._rule_code = rule_code

    @property
    def rule_name(self):
        """Gets the rule_name of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501

        The name of the notification event rule that triggered the generation of the `notificationEvent`.  # noqa: E501

        :return: The rule_name of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this ConnectMonitoringAllNotificationsEventsData.

        The name of the notification event rule that triggered the generation of the `notificationEvent`.  # noqa: E501

        :param rule_name: The rule_name of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :type: str
        """

        self._rule_name = rule_name

    @property
    def summary(self):
        """Gets the summary of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501

        A short description of the notification event rule that triggered the `notificationEvent`.  # noqa: E501

        :return: The summary of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ConnectMonitoringAllNotificationsEventsData.

        A short description of the notification event rule that triggered the `notificationEvent`.  # noqa: E501

        :param summary: The summary of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def rule_text(self):
        """Gets the rule_text of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501

        A short description of the notification event rule that triggered the `notificationEvent`.  # noqa: E501

        :return: The rule_text of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :rtype: str
        """
        return self._rule_text

    @rule_text.setter
    def rule_text(self, rule_text):
        """Sets the rule_text of this ConnectMonitoringAllNotificationsEventsData.

        A short description of the notification event rule that triggered the `notificationEvent`.  # noqa: E501

        :param rule_text: The rule_text of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :type: str
        """

        self._rule_text = rule_text

    @property
    def local_event_code(self):
        """Gets the local_event_code of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501

        The local code of the `notificationEvent`.  # noqa: E501

        :return: The local_event_code of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :rtype: str
        """
        return self._local_event_code

    @local_event_code.setter
    def local_event_code(self, local_event_code):
        """Sets the local_event_code of this ConnectMonitoringAllNotificationsEventsData.

        The local code of the `notificationEvent`.  # noqa: E501

        :param local_event_code: The local_event_code of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :type: str
        """

        self._local_event_code = local_event_code

    @property
    def is_processed(self):
        """Gets the is_processed of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501

        a `true` or `false` flag for each event. Can be updated using the PATCH endpoint.  # noqa: E501

        :return: The is_processed of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :rtype: bool
        """
        return self._is_processed

    @is_processed.setter
    def is_processed(self, is_processed):
        """Sets the is_processed of this ConnectMonitoringAllNotificationsEventsData.

        a `true` or `false` flag for each event. Can be updated using the PATCH endpoint.  # noqa: E501

        :param is_processed: The is_processed of this ConnectMonitoringAllNotificationsEventsData.  # noqa: E501
        :type: bool
        """

        self._is_processed = is_processed

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
        if issubclass(ConnectMonitoringAllNotificationsEventsData, dict):
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
        if not isinstance(other, ConnectMonitoringAllNotificationsEventsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

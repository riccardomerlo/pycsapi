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

class ConnectMonitoringCompanyEventsData(object):
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
        'event_id': 'float',
        'company_id': 'str',
        'portfolio_id': 'float',
        'rule_name': 'str',
        'local_event_code': 'str',
        'global_event_code': 'str',
        'new_value': 'str',
        'old_value': 'str',
        'event_date': 'datetime',
        'created_date': 'datetime'
    }

    attribute_map = {
        'event_id': 'eventId',
        'company_id': 'companyId',
        'portfolio_id': 'portfolioId',
        'rule_name': 'ruleName',
        'local_event_code': 'localEventCode',
        'global_event_code': 'globalEventCode',
        'new_value': 'newValue',
        'old_value': 'oldValue',
        'event_date': 'eventDate',
        'created_date': 'createdDate'
    }

    def __init__(self, event_id=None, company_id=None, portfolio_id=None, rule_name=None, local_event_code=None, global_event_code=None, new_value=None, old_value=None, event_date=None, created_date=None):  # noqa: E501
        """ConnectMonitoringCompanyEventsData - a model defined in Swagger"""  # noqa: E501
        self._event_id = None
        self._company_id = None
        self._portfolio_id = None
        self._rule_name = None
        self._local_event_code = None
        self._global_event_code = None
        self._new_value = None
        self._old_value = None
        self._event_date = None
        self._created_date = None
        self.discriminator = None
        if event_id is not None:
            self.event_id = event_id
        if company_id is not None:
            self.company_id = company_id
        if portfolio_id is not None:
            self.portfolio_id = portfolio_id
        if rule_name is not None:
            self.rule_name = rule_name
        if local_event_code is not None:
            self.local_event_code = local_event_code
        if global_event_code is not None:
            self.global_event_code = global_event_code
        if new_value is not None:
            self.new_value = new_value
        if old_value is not None:
            self.old_value = old_value
        if event_date is not None:
            self.event_date = event_date
        if created_date is not None:
            self.created_date = created_date

    @property
    def event_id(self):
        """Gets the event_id of this ConnectMonitoringCompanyEventsData.  # noqa: E501

        The unique identifier for the event.  # noqa: E501

        :return: The event_id of this ConnectMonitoringCompanyEventsData.  # noqa: E501
        :rtype: float
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this ConnectMonitoringCompanyEventsData.

        The unique identifier for the event.  # noqa: E501

        :param event_id: The event_id of this ConnectMonitoringCompanyEventsData.  # noqa: E501
        :type: float
        """

        self._event_id = event_id

    @property
    def company_id(self):
        """Gets the company_id of this ConnectMonitoringCompanyEventsData.  # noqa: E501

        The Safe Number (Creditsafe's identifier on all Companies owned in the Creditsafe Universe) of the company that triggered the event.  # noqa: E501

        :return: The company_id of this ConnectMonitoringCompanyEventsData.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this ConnectMonitoringCompanyEventsData.

        The Safe Number (Creditsafe's identifier on all Companies owned in the Creditsafe Universe) of the company that triggered the event.  # noqa: E501

        :param company_id: The company_id of this ConnectMonitoringCompanyEventsData.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def portfolio_id(self):
        """Gets the portfolio_id of this ConnectMonitoringCompanyEventsData.  # noqa: E501

        The portfolio Id of the portfolio that contains the company that you requested event information for.  # noqa: E501

        :return: The portfolio_id of this ConnectMonitoringCompanyEventsData.  # noqa: E501
        :rtype: float
        """
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, portfolio_id):
        """Sets the portfolio_id of this ConnectMonitoringCompanyEventsData.

        The portfolio Id of the portfolio that contains the company that you requested event information for.  # noqa: E501

        :param portfolio_id: The portfolio_id of this ConnectMonitoringCompanyEventsData.  # noqa: E501
        :type: float
        """

        self._portfolio_id = portfolio_id

    @property
    def rule_name(self):
        """Gets the rule_name of this ConnectMonitoringCompanyEventsData.  # noqa: E501

        A short description of the company event.  # noqa: E501

        :return: The rule_name of this ConnectMonitoringCompanyEventsData.  # noqa: E501
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this ConnectMonitoringCompanyEventsData.

        A short description of the company event.  # noqa: E501

        :param rule_name: The rule_name of this ConnectMonitoringCompanyEventsData.  # noqa: E501
        :type: str
        """

        self._rule_name = rule_name

    @property
    def local_event_code(self):
        """Gets the local_event_code of this ConnectMonitoringCompanyEventsData.  # noqa: E501

        The local event code for the event.  # noqa: E501

        :return: The local_event_code of this ConnectMonitoringCompanyEventsData.  # noqa: E501
        :rtype: str
        """
        return self._local_event_code

    @local_event_code.setter
    def local_event_code(self, local_event_code):
        """Sets the local_event_code of this ConnectMonitoringCompanyEventsData.

        The local event code for the event.  # noqa: E501

        :param local_event_code: The local_event_code of this ConnectMonitoringCompanyEventsData.  # noqa: E501
        :type: str
        """

        self._local_event_code = local_event_code

    @property
    def global_event_code(self):
        """Gets the global_event_code of this ConnectMonitoringCompanyEventsData.  # noqa: E501

        The global event code that has been mapped to the local event.  # noqa: E501

        :return: The global_event_code of this ConnectMonitoringCompanyEventsData.  # noqa: E501
        :rtype: str
        """
        return self._global_event_code

    @global_event_code.setter
    def global_event_code(self, global_event_code):
        """Sets the global_event_code of this ConnectMonitoringCompanyEventsData.

        The global event code that has been mapped to the local event.  # noqa: E501

        :param global_event_code: The global_event_code of this ConnectMonitoringCompanyEventsData.  # noqa: E501
        :type: str
        """

        self._global_event_code = global_event_code

    @property
    def new_value(self):
        """Gets the new_value of this ConnectMonitoringCompanyEventsData.  # noqa: E501

        Some events contain an `oldValue` and `newValue` (e.g. a change in Credit Limit).  # noqa: E501

        :return: The new_value of this ConnectMonitoringCompanyEventsData.  # noqa: E501
        :rtype: str
        """
        return self._new_value

    @new_value.setter
    def new_value(self, new_value):
        """Sets the new_value of this ConnectMonitoringCompanyEventsData.

        Some events contain an `oldValue` and `newValue` (e.g. a change in Credit Limit).  # noqa: E501

        :param new_value: The new_value of this ConnectMonitoringCompanyEventsData.  # noqa: E501
        :type: str
        """

        self._new_value = new_value

    @property
    def old_value(self):
        """Gets the old_value of this ConnectMonitoringCompanyEventsData.  # noqa: E501

        Some events contain an `oldValue` and `newValue` (e.g. a change in Credit Limit).  # noqa: E501

        :return: The old_value of this ConnectMonitoringCompanyEventsData.  # noqa: E501
        :rtype: str
        """
        return self._old_value

    @old_value.setter
    def old_value(self, old_value):
        """Sets the old_value of this ConnectMonitoringCompanyEventsData.

        Some events contain an `oldValue` and `newValue` (e.g. a change in Credit Limit).  # noqa: E501

        :param old_value: The old_value of this ConnectMonitoringCompanyEventsData.  # noqa: E501
        :type: str
        """

        self._old_value = old_value

    @property
    def event_date(self):
        """Gets the event_date of this ConnectMonitoringCompanyEventsData.  # noqa: E501

        The date that the event occurred.  # noqa: E501

        :return: The event_date of this ConnectMonitoringCompanyEventsData.  # noqa: E501
        :rtype: datetime
        """
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        """Sets the event_date of this ConnectMonitoringCompanyEventsData.

        The date that the event occurred.  # noqa: E501

        :param event_date: The event_date of this ConnectMonitoringCompanyEventsData.  # noqa: E501
        :type: datetime
        """

        self._event_date = event_date

    @property
    def created_date(self):
        """Gets the created_date of this ConnectMonitoringCompanyEventsData.  # noqa: E501

        The date that the event was created in the Creditsafe database.  # noqa: E501

        :return: The created_date of this ConnectMonitoringCompanyEventsData.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this ConnectMonitoringCompanyEventsData.

        The date that the event was created in the Creditsafe database.  # noqa: E501

        :param created_date: The created_date of this ConnectMonitoringCompanyEventsData.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

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
        if issubclass(ConnectMonitoringCompanyEventsData, dict):
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
        if not isinstance(other, ConnectMonitoringCompanyEventsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

class InvestigationResponse(object):
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
        'created_at': 'datetime',
        'created_by': 'int',
        'search_criteria': 'InvestigationQuery',
        'schedule_id': 'str',
        'profile_id': 'str',
        'profile_name': 'str',
        'alerts_count': 'int',
        'current_alert': 'InvestigationAlert',
        'results': 'list[Record]',
        'not_found_record_ids': 'list[int]',
        'investigation_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'createdAt',
        'created_by': 'createdBy',
        'search_criteria': 'searchCriteria',
        'schedule_id': 'scheduleId',
        'profile_id': 'profileId',
        'profile_name': 'profileName',
        'alerts_count': 'alertsCount',
        'current_alert': 'currentAlert',
        'results': 'results',
        'not_found_record_ids': 'notFoundRecordIds',
        'investigation_name': 'investigationName'
    }

    def __init__(self, id=None, created_at=None, created_by=None, search_criteria=None, schedule_id=None, profile_id=None, profile_name=None, alerts_count=None, current_alert=None, results=None, not_found_record_ids=None, investigation_name=None):  # noqa: E501
        """InvestigationResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._created_at = None
        self._created_by = None
        self._search_criteria = None
        self._schedule_id = None
        self._profile_id = None
        self._profile_name = None
        self._alerts_count = None
        self._current_alert = None
        self._results = None
        self._not_found_record_ids = None
        self._investigation_name = None
        self.discriminator = None
        self.id = id
        self.created_at = created_at
        self.created_by = created_by
        self.search_criteria = search_criteria
        if schedule_id is not None:
            self.schedule_id = schedule_id
        if profile_id is not None:
            self.profile_id = profile_id
        if profile_name is not None:
            self.profile_name = profile_name
        if alerts_count is not None:
            self.alerts_count = alerts_count
        if current_alert is not None:
            self.current_alert = current_alert
        self.results = results
        self.not_found_record_ids = not_found_record_ids
        self.investigation_name = investigation_name

    @property
    def id(self):
        """Gets the id of this InvestigationResponse.  # noqa: E501


        :return: The id of this InvestigationResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InvestigationResponse.


        :param id: The id of this InvestigationResponse.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this InvestigationResponse.  # noqa: E501


        :return: The created_at of this InvestigationResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InvestigationResponse.


        :param created_at: The created_at of this InvestigationResponse.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this InvestigationResponse.  # noqa: E501


        :return: The created_by of this InvestigationResponse.  # noqa: E501
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this InvestigationResponse.


        :param created_by: The created_by of this InvestigationResponse.  # noqa: E501
        :type: int
        """
        if created_by is None:
            raise ValueError("Invalid value for `created_by`, must not be `None`")  # noqa: E501

        self._created_by = created_by

    @property
    def search_criteria(self):
        """Gets the search_criteria of this InvestigationResponse.  # noqa: E501


        :return: The search_criteria of this InvestigationResponse.  # noqa: E501
        :rtype: InvestigationQuery
        """
        return self._search_criteria

    @search_criteria.setter
    def search_criteria(self, search_criteria):
        """Sets the search_criteria of this InvestigationResponse.


        :param search_criteria: The search_criteria of this InvestigationResponse.  # noqa: E501
        :type: InvestigationQuery
        """
        if search_criteria is None:
            raise ValueError("Invalid value for `search_criteria`, must not be `None`")  # noqa: E501

        self._search_criteria = search_criteria

    @property
    def schedule_id(self):
        """Gets the schedule_id of this InvestigationResponse.  # noqa: E501


        :return: The schedule_id of this InvestigationResponse.  # noqa: E501
        :rtype: str
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id):
        """Sets the schedule_id of this InvestigationResponse.


        :param schedule_id: The schedule_id of this InvestigationResponse.  # noqa: E501
        :type: str
        """

        self._schedule_id = schedule_id

    @property
    def profile_id(self):
        """Gets the profile_id of this InvestigationResponse.  # noqa: E501


        :return: The profile_id of this InvestigationResponse.  # noqa: E501
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this InvestigationResponse.


        :param profile_id: The profile_id of this InvestigationResponse.  # noqa: E501
        :type: str
        """

        self._profile_id = profile_id

    @property
    def profile_name(self):
        """Gets the profile_name of this InvestigationResponse.  # noqa: E501


        :return: The profile_name of this InvestigationResponse.  # noqa: E501
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """Sets the profile_name of this InvestigationResponse.


        :param profile_name: The profile_name of this InvestigationResponse.  # noqa: E501
        :type: str
        """

        self._profile_name = profile_name

    @property
    def alerts_count(self):
        """Gets the alerts_count of this InvestigationResponse.  # noqa: E501


        :return: The alerts_count of this InvestigationResponse.  # noqa: E501
        :rtype: int
        """
        return self._alerts_count

    @alerts_count.setter
    def alerts_count(self, alerts_count):
        """Sets the alerts_count of this InvestigationResponse.


        :param alerts_count: The alerts_count of this InvestigationResponse.  # noqa: E501
        :type: int
        """

        self._alerts_count = alerts_count

    @property
    def current_alert(self):
        """Gets the current_alert of this InvestigationResponse.  # noqa: E501


        :return: The current_alert of this InvestigationResponse.  # noqa: E501
        :rtype: InvestigationAlert
        """
        return self._current_alert

    @current_alert.setter
    def current_alert(self, current_alert):
        """Sets the current_alert of this InvestigationResponse.


        :param current_alert: The current_alert of this InvestigationResponse.  # noqa: E501
        :type: InvestigationAlert
        """

        self._current_alert = current_alert

    @property
    def results(self):
        """Gets the results of this InvestigationResponse.  # noqa: E501


        :return: The results of this InvestigationResponse.  # noqa: E501
        :rtype: list[Record]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this InvestigationResponse.


        :param results: The results of this InvestigationResponse.  # noqa: E501
        :type: list[Record]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

    @property
    def not_found_record_ids(self):
        """Gets the not_found_record_ids of this InvestigationResponse.  # noqa: E501


        :return: The not_found_record_ids of this InvestigationResponse.  # noqa: E501
        :rtype: list[int]
        """
        return self._not_found_record_ids

    @not_found_record_ids.setter
    def not_found_record_ids(self, not_found_record_ids):
        """Sets the not_found_record_ids of this InvestigationResponse.


        :param not_found_record_ids: The not_found_record_ids of this InvestigationResponse.  # noqa: E501
        :type: list[int]
        """
        if not_found_record_ids is None:
            raise ValueError("Invalid value for `not_found_record_ids`, must not be `None`")  # noqa: E501

        self._not_found_record_ids = not_found_record_ids

    @property
    def investigation_name(self):
        """Gets the investigation_name of this InvestigationResponse.  # noqa: E501


        :return: The investigation_name of this InvestigationResponse.  # noqa: E501
        :rtype: str
        """
        return self._investigation_name

    @investigation_name.setter
    def investigation_name(self, investigation_name):
        """Sets the investigation_name of this InvestigationResponse.


        :param investigation_name: The investigation_name of this InvestigationResponse.  # noqa: E501
        :type: str
        """
        if investigation_name is None:
            raise ValueError("Invalid value for `investigation_name`, must not be `None`")  # noqa: E501

        self._investigation_name = investigation_name

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
        if issubclass(InvestigationResponse, dict):
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
        if not isinstance(other, InvestigationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

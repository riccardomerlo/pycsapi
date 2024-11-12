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

class InvestigationAlert(object):
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
        'status': 'InvestigationAlertStatus',
        'alert_count': 'int',
        'total_record_count': 'int',
        'unprocessed_record_count': 'int',
        'result_id': 'int',
        'screening_threshold': 'int',
        'created_at': 'datetime',
        'alert_type': 'AlertType'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'alert_count': 'alertCount',
        'total_record_count': 'totalRecordCount',
        'unprocessed_record_count': 'unprocessedRecordCount',
        'result_id': 'resultId',
        'screening_threshold': 'screeningThreshold',
        'created_at': 'createdAt',
        'alert_type': 'alertType'
    }

    def __init__(self, id=None, status=None, alert_count=None, total_record_count=None, unprocessed_record_count=None, result_id=None, screening_threshold=None, created_at=None, alert_type=None):  # noqa: E501
        """InvestigationAlert - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._status = None
        self._alert_count = None
        self._total_record_count = None
        self._unprocessed_record_count = None
        self._result_id = None
        self._screening_threshold = None
        self._created_at = None
        self._alert_type = None
        self.discriminator = None
        self.id = id
        self.status = status
        self.alert_count = alert_count
        self.total_record_count = total_record_count
        self.unprocessed_record_count = unprocessed_record_count
        if result_id is not None:
            self.result_id = result_id
        self.screening_threshold = screening_threshold
        self.created_at = created_at
        self.alert_type = alert_type

    @property
    def id(self):
        """Gets the id of this InvestigationAlert.  # noqa: E501


        :return: The id of this InvestigationAlert.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InvestigationAlert.


        :param id: The id of this InvestigationAlert.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def status(self):
        """Gets the status of this InvestigationAlert.  # noqa: E501


        :return: The status of this InvestigationAlert.  # noqa: E501
        :rtype: InvestigationAlertStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InvestigationAlert.


        :param status: The status of this InvestigationAlert.  # noqa: E501
        :type: InvestigationAlertStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def alert_count(self):
        """Gets the alert_count of this InvestigationAlert.  # noqa: E501


        :return: The alert_count of this InvestigationAlert.  # noqa: E501
        :rtype: int
        """
        return self._alert_count

    @alert_count.setter
    def alert_count(self, alert_count):
        """Sets the alert_count of this InvestigationAlert.


        :param alert_count: The alert_count of this InvestigationAlert.  # noqa: E501
        :type: int
        """
        if alert_count is None:
            raise ValueError("Invalid value for `alert_count`, must not be `None`")  # noqa: E501

        self._alert_count = alert_count

    @property
    def total_record_count(self):
        """Gets the total_record_count of this InvestigationAlert.  # noqa: E501


        :return: The total_record_count of this InvestigationAlert.  # noqa: E501
        :rtype: int
        """
        return self._total_record_count

    @total_record_count.setter
    def total_record_count(self, total_record_count):
        """Sets the total_record_count of this InvestigationAlert.


        :param total_record_count: The total_record_count of this InvestigationAlert.  # noqa: E501
        :type: int
        """
        if total_record_count is None:
            raise ValueError("Invalid value for `total_record_count`, must not be `None`")  # noqa: E501

        self._total_record_count = total_record_count

    @property
    def unprocessed_record_count(self):
        """Gets the unprocessed_record_count of this InvestigationAlert.  # noqa: E501


        :return: The unprocessed_record_count of this InvestigationAlert.  # noqa: E501
        :rtype: int
        """
        return self._unprocessed_record_count

    @unprocessed_record_count.setter
    def unprocessed_record_count(self, unprocessed_record_count):
        """Sets the unprocessed_record_count of this InvestigationAlert.


        :param unprocessed_record_count: The unprocessed_record_count of this InvestigationAlert.  # noqa: E501
        :type: int
        """
        if unprocessed_record_count is None:
            raise ValueError("Invalid value for `unprocessed_record_count`, must not be `None`")  # noqa: E501

        self._unprocessed_record_count = unprocessed_record_count

    @property
    def result_id(self):
        """Gets the result_id of this InvestigationAlert.  # noqa: E501


        :return: The result_id of this InvestigationAlert.  # noqa: E501
        :rtype: int
        """
        return self._result_id

    @result_id.setter
    def result_id(self, result_id):
        """Sets the result_id of this InvestigationAlert.


        :param result_id: The result_id of this InvestigationAlert.  # noqa: E501
        :type: int
        """

        self._result_id = result_id

    @property
    def screening_threshold(self):
        """Gets the screening_threshold of this InvestigationAlert.  # noqa: E501


        :return: The screening_threshold of this InvestigationAlert.  # noqa: E501
        :rtype: int
        """
        return self._screening_threshold

    @screening_threshold.setter
    def screening_threshold(self, screening_threshold):
        """Sets the screening_threshold of this InvestigationAlert.


        :param screening_threshold: The screening_threshold of this InvestigationAlert.  # noqa: E501
        :type: int
        """
        if screening_threshold is None:
            raise ValueError("Invalid value for `screening_threshold`, must not be `None`")  # noqa: E501

        self._screening_threshold = screening_threshold

    @property
    def created_at(self):
        """Gets the created_at of this InvestigationAlert.  # noqa: E501


        :return: The created_at of this InvestigationAlert.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InvestigationAlert.


        :param created_at: The created_at of this InvestigationAlert.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def alert_type(self):
        """Gets the alert_type of this InvestigationAlert.  # noqa: E501


        :return: The alert_type of this InvestigationAlert.  # noqa: E501
        :rtype: AlertType
        """
        return self._alert_type

    @alert_type.setter
    def alert_type(self, alert_type):
        """Sets the alert_type of this InvestigationAlert.


        :param alert_type: The alert_type of this InvestigationAlert.  # noqa: E501
        :type: AlertType
        """
        if alert_type is None:
            raise ValueError("Invalid value for `alert_type`, must not be `None`")  # noqa: E501

        self._alert_type = alert_type

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
        if issubclass(InvestigationAlert, dict):
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
        if not isinstance(other, InvestigationAlert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

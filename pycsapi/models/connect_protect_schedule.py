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

class ConnectProtectSchedule(object):
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
        'correlation_id': 'str',
        'id': 'str',
        'customer_id': 'int',
        'user_id': 'int',
        'investigation_id': 'str',
        'investigation': 'ConnectProtectInvestigation',
        'frequency': 'ConnectProtectAlertsFrequency',
        'screening_threshold': 'int',
        'created_at': 'datetime',
        'is_email_required': 'bool',
        'is_disabled': 'bool'
    }

    attribute_map = {
        'correlation_id': 'correlationId',
        'id': 'id',
        'customer_id': 'customerId',
        'user_id': 'userId',
        'investigation_id': 'investigationId',
        'investigation': 'investigation',
        'frequency': 'frequency',
        'screening_threshold': 'screeningThreshold',
        'created_at': 'createdAt',
        'is_email_required': 'isEmailRequired',
        'is_disabled': 'isDisabled'
    }

    def __init__(self, correlation_id=None, id=None, customer_id=None, user_id=None, investigation_id=None, investigation=None, frequency=None, screening_threshold=None, created_at=None, is_email_required=None, is_disabled=None):  # noqa: E501
        """ConnectProtectSchedule - a model defined in Swagger"""  # noqa: E501
        self._correlation_id = None
        self._id = None
        self._customer_id = None
        self._user_id = None
        self._investigation_id = None
        self._investigation = None
        self._frequency = None
        self._screening_threshold = None
        self._created_at = None
        self._is_email_required = None
        self._is_disabled = None
        self.discriminator = None
        if correlation_id is not None:
            self.correlation_id = correlation_id
        self.id = id
        self.customer_id = customer_id
        self.user_id = user_id
        self.investigation_id = investigation_id
        self.investigation = investigation
        self.frequency = frequency
        self.screening_threshold = screening_threshold
        self.created_at = created_at
        if is_email_required is not None:
            self.is_email_required = is_email_required
        if is_disabled is not None:
            self.is_disabled = is_disabled

    @property
    def correlation_id(self):
        """Gets the correlation_id of this ConnectProtectSchedule.  # noqa: E501

        A unique ID assigned to this request.  # noqa: E501

        :return: The correlation_id of this ConnectProtectSchedule.  # noqa: E501
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this ConnectProtectSchedule.

        A unique ID assigned to this request.  # noqa: E501

        :param correlation_id: The correlation_id of this ConnectProtectSchedule.  # noqa: E501
        :type: str
        """

        self._correlation_id = correlation_id

    @property
    def id(self):
        """Gets the id of this ConnectProtectSchedule.  # noqa: E501


        :return: The id of this ConnectProtectSchedule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConnectProtectSchedule.


        :param id: The id of this ConnectProtectSchedule.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def customer_id(self):
        """Gets the customer_id of this ConnectProtectSchedule.  # noqa: E501


        :return: The customer_id of this ConnectProtectSchedule.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ConnectProtectSchedule.


        :param customer_id: The customer_id of this ConnectProtectSchedule.  # noqa: E501
        :type: int
        """
        if customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def user_id(self):
        """Gets the user_id of this ConnectProtectSchedule.  # noqa: E501


        :return: The user_id of this ConnectProtectSchedule.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ConnectProtectSchedule.


        :param user_id: The user_id of this ConnectProtectSchedule.  # noqa: E501
        :type: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def investigation_id(self):
        """Gets the investigation_id of this ConnectProtectSchedule.  # noqa: E501


        :return: The investigation_id of this ConnectProtectSchedule.  # noqa: E501
        :rtype: str
        """
        return self._investigation_id

    @investigation_id.setter
    def investigation_id(self, investigation_id):
        """Sets the investigation_id of this ConnectProtectSchedule.


        :param investigation_id: The investigation_id of this ConnectProtectSchedule.  # noqa: E501
        :type: str
        """
        if investigation_id is None:
            raise ValueError("Invalid value for `investigation_id`, must not be `None`")  # noqa: E501

        self._investigation_id = investigation_id

    @property
    def investigation(self):
        """Gets the investigation of this ConnectProtectSchedule.  # noqa: E501


        :return: The investigation of this ConnectProtectSchedule.  # noqa: E501
        :rtype: ConnectProtectInvestigation
        """
        return self._investigation

    @investigation.setter
    def investigation(self, investigation):
        """Sets the investigation of this ConnectProtectSchedule.


        :param investigation: The investigation of this ConnectProtectSchedule.  # noqa: E501
        :type: ConnectProtectInvestigation
        """
        if investigation is None:
            raise ValueError("Invalid value for `investigation`, must not be `None`")  # noqa: E501

        self._investigation = investigation

    @property
    def frequency(self):
        """Gets the frequency of this ConnectProtectSchedule.  # noqa: E501


        :return: The frequency of this ConnectProtectSchedule.  # noqa: E501
        :rtype: ConnectProtectAlertsFrequency
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this ConnectProtectSchedule.


        :param frequency: The frequency of this ConnectProtectSchedule.  # noqa: E501
        :type: ConnectProtectAlertsFrequency
        """
        if frequency is None:
            raise ValueError("Invalid value for `frequency`, must not be `None`")  # noqa: E501

        self._frequency = frequency

    @property
    def screening_threshold(self):
        """Gets the screening_threshold of this ConnectProtectSchedule.  # noqa: E501

        Can only enter the following options: 85, 90, 95, 100  # noqa: E501

        :return: The screening_threshold of this ConnectProtectSchedule.  # noqa: E501
        :rtype: int
        """
        return self._screening_threshold

    @screening_threshold.setter
    def screening_threshold(self, screening_threshold):
        """Sets the screening_threshold of this ConnectProtectSchedule.

        Can only enter the following options: 85, 90, 95, 100  # noqa: E501

        :param screening_threshold: The screening_threshold of this ConnectProtectSchedule.  # noqa: E501
        :type: int
        """
        if screening_threshold is None:
            raise ValueError("Invalid value for `screening_threshold`, must not be `None`")  # noqa: E501

        self._screening_threshold = screening_threshold

    @property
    def created_at(self):
        """Gets the created_at of this ConnectProtectSchedule.  # noqa: E501


        :return: The created_at of this ConnectProtectSchedule.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ConnectProtectSchedule.


        :param created_at: The created_at of this ConnectProtectSchedule.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def is_email_required(self):
        """Gets the is_email_required of this ConnectProtectSchedule.  # noqa: E501


        :return: The is_email_required of this ConnectProtectSchedule.  # noqa: E501
        :rtype: bool
        """
        return self._is_email_required

    @is_email_required.setter
    def is_email_required(self, is_email_required):
        """Sets the is_email_required of this ConnectProtectSchedule.


        :param is_email_required: The is_email_required of this ConnectProtectSchedule.  # noqa: E501
        :type: bool
        """

        self._is_email_required = is_email_required

    @property
    def is_disabled(self):
        """Gets the is_disabled of this ConnectProtectSchedule.  # noqa: E501


        :return: The is_disabled of this ConnectProtectSchedule.  # noqa: E501
        :rtype: bool
        """
        return self._is_disabled

    @is_disabled.setter
    def is_disabled(self, is_disabled):
        """Sets the is_disabled of this ConnectProtectSchedule.


        :param is_disabled: The is_disabled of this ConnectProtectSchedule.  # noqa: E501
        :type: bool
        """

        self._is_disabled = is_disabled

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
        if issubclass(ConnectProtectSchedule, dict):
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
        if not isinstance(other, ConnectProtectSchedule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

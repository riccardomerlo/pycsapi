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

class ConnectProtectAuditExportRequestDto(object):
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
        'file_type': 'str',
        'audit_type': 'str',
        'user_id': 'int',
        'keyword_search': 'str',
        'created_at_or_after': 'datetime',
        'created_at_or_before': 'datetime',
        'payload': 'ConnectProtectAuditExportPayloadDto'
    }

    attribute_map = {
        'file_type': 'fileType',
        'audit_type': 'auditType',
        'user_id': 'userId',
        'keyword_search': 'keywordSearch',
        'created_at_or_after': 'createdAtOrAfter',
        'created_at_or_before': 'createdAtOrBefore',
        'payload': 'payload'
    }

    def __init__(self, file_type=None, audit_type=None, user_id=None, keyword_search=None, created_at_or_after=None, created_at_or_before=None, payload=None):  # noqa: E501
        """ConnectProtectAuditExportRequestDto - a model defined in Swagger"""  # noqa: E501
        self._file_type = None
        self._audit_type = None
        self._user_id = None
        self._keyword_search = None
        self._created_at_or_after = None
        self._created_at_or_before = None
        self._payload = None
        self.discriminator = None
        self.file_type = file_type
        if audit_type is not None:
            self.audit_type = audit_type
        if user_id is not None:
            self.user_id = user_id
        if keyword_search is not None:
            self.keyword_search = keyword_search
        if created_at_or_after is not None:
            self.created_at_or_after = created_at_or_after
        if created_at_or_before is not None:
            self.created_at_or_before = created_at_or_before
        if payload is not None:
            self.payload = payload

    @property
    def file_type(self):
        """Gets the file_type of this ConnectProtectAuditExportRequestDto.  # noqa: E501


        :return: The file_type of this ConnectProtectAuditExportRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._file_type

    @file_type.setter
    def file_type(self, file_type):
        """Sets the file_type of this ConnectProtectAuditExportRequestDto.


        :param file_type: The file_type of this ConnectProtectAuditExportRequestDto.  # noqa: E501
        :type: str
        """
        if file_type is None:
            raise ValueError("Invalid value for `file_type`, must not be `None`")  # noqa: E501
        allowed_values = ["csv"]  # noqa: E501
        if file_type not in allowed_values:
            raise ValueError(
                "Invalid value for `file_type` ({0}), must be one of {1}"  # noqa: E501
                .format(file_type, allowed_values)
            )

        self._file_type = file_type

    @property
    def audit_type(self):
        """Gets the audit_type of this ConnectProtectAuditExportRequestDto.  # noqa: E501


        :return: The audit_type of this ConnectProtectAuditExportRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._audit_type

    @audit_type.setter
    def audit_type(self, audit_type):
        """Sets the audit_type of this ConnectProtectAuditExportRequestDto.


        :param audit_type: The audit_type of this ConnectProtectAuditExportRequestDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["alert.accepted", "alert.rejected", "alert.received", "profile.added", "profile.created", "investigation.accepted", "investigation.created", "investigation.file_downloaded", "schedule.created", "schedule.removed"]  # noqa: E501
        if audit_type not in allowed_values:
            raise ValueError(
                "Invalid value for `audit_type` ({0}), must be one of {1}"  # noqa: E501
                .format(audit_type, allowed_values)
            )

        self._audit_type = audit_type

    @property
    def user_id(self):
        """Gets the user_id of this ConnectProtectAuditExportRequestDto.  # noqa: E501


        :return: The user_id of this ConnectProtectAuditExportRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ConnectProtectAuditExportRequestDto.


        :param user_id: The user_id of this ConnectProtectAuditExportRequestDto.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def keyword_search(self):
        """Gets the keyword_search of this ConnectProtectAuditExportRequestDto.  # noqa: E501


        :return: The keyword_search of this ConnectProtectAuditExportRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._keyword_search

    @keyword_search.setter
    def keyword_search(self, keyword_search):
        """Sets the keyword_search of this ConnectProtectAuditExportRequestDto.


        :param keyword_search: The keyword_search of this ConnectProtectAuditExportRequestDto.  # noqa: E501
        :type: str
        """

        self._keyword_search = keyword_search

    @property
    def created_at_or_after(self):
        """Gets the created_at_or_after of this ConnectProtectAuditExportRequestDto.  # noqa: E501


        :return: The created_at_or_after of this ConnectProtectAuditExportRequestDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at_or_after

    @created_at_or_after.setter
    def created_at_or_after(self, created_at_or_after):
        """Sets the created_at_or_after of this ConnectProtectAuditExportRequestDto.


        :param created_at_or_after: The created_at_or_after of this ConnectProtectAuditExportRequestDto.  # noqa: E501
        :type: datetime
        """

        self._created_at_or_after = created_at_or_after

    @property
    def created_at_or_before(self):
        """Gets the created_at_or_before of this ConnectProtectAuditExportRequestDto.  # noqa: E501


        :return: The created_at_or_before of this ConnectProtectAuditExportRequestDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at_or_before

    @created_at_or_before.setter
    def created_at_or_before(self, created_at_or_before):
        """Sets the created_at_or_before of this ConnectProtectAuditExportRequestDto.


        :param created_at_or_before: The created_at_or_before of this ConnectProtectAuditExportRequestDto.  # noqa: E501
        :type: datetime
        """

        self._created_at_or_before = created_at_or_before

    @property
    def payload(self):
        """Gets the payload of this ConnectProtectAuditExportRequestDto.  # noqa: E501


        :return: The payload of this ConnectProtectAuditExportRequestDto.  # noqa: E501
        :rtype: ConnectProtectAuditExportPayloadDto
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this ConnectProtectAuditExportRequestDto.


        :param payload: The payload of this ConnectProtectAuditExportRequestDto.  # noqa: E501
        :type: ConnectProtectAuditExportPayloadDto
        """

        self._payload = payload

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
        if issubclass(ConnectProtectAuditExportRequestDto, dict):
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
        if not isinstance(other, ConnectProtectAuditExportRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

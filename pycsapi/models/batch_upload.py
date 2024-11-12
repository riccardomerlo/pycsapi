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

class BatchUpload(object):
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
        'user_id': 'int',
        'customer_id': 'int',
        'type': 'InvestigationType',
        'file_name': 'str',
        'storage_file_name': 'str',
        'error_filename': 'str',
        'row_count': 'int',
        'status': 'BatchUploadStatus',
        'created_at': 'datetime',
        'modified_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'userId',
        'customer_id': 'customerId',
        'type': 'type',
        'file_name': 'fileName',
        'storage_file_name': 'storageFileName',
        'error_filename': 'errorFilename',
        'row_count': 'rowCount',
        'status': 'status',
        'created_at': 'createdAt',
        'modified_at': 'modifiedAt'
    }

    def __init__(self, id=None, user_id=None, customer_id=None, type=None, file_name=None, storage_file_name=None, error_filename=None, row_count=None, status=None, created_at=None, modified_at=None):  # noqa: E501
        """BatchUpload - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._user_id = None
        self._customer_id = None
        self._type = None
        self._file_name = None
        self._storage_file_name = None
        self._error_filename = None
        self._row_count = None
        self._status = None
        self._created_at = None
        self._modified_at = None
        self.discriminator = None
        self.id = id
        self.user_id = user_id
        self.customer_id = customer_id
        if type is not None:
            self.type = type
        self.file_name = file_name
        self.storage_file_name = storage_file_name
        self.error_filename = error_filename
        self.row_count = row_count
        self.status = status
        self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at

    @property
    def id(self):
        """Gets the id of this BatchUpload.  # noqa: E501


        :return: The id of this BatchUpload.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BatchUpload.


        :param id: The id of this BatchUpload.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this BatchUpload.  # noqa: E501


        :return: The user_id of this BatchUpload.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this BatchUpload.


        :param user_id: The user_id of this BatchUpload.  # noqa: E501
        :type: int
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def customer_id(self):
        """Gets the customer_id of this BatchUpload.  # noqa: E501


        :return: The customer_id of this BatchUpload.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this BatchUpload.


        :param customer_id: The customer_id of this BatchUpload.  # noqa: E501
        :type: int
        """
        if customer_id is None:
            raise ValueError("Invalid value for `customer_id`, must not be `None`")  # noqa: E501

        self._customer_id = customer_id

    @property
    def type(self):
        """Gets the type of this BatchUpload.  # noqa: E501


        :return: The type of this BatchUpload.  # noqa: E501
        :rtype: InvestigationType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BatchUpload.


        :param type: The type of this BatchUpload.  # noqa: E501
        :type: InvestigationType
        """

        self._type = type

    @property
    def file_name(self):
        """Gets the file_name of this BatchUpload.  # noqa: E501


        :return: The file_name of this BatchUpload.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this BatchUpload.


        :param file_name: The file_name of this BatchUpload.  # noqa: E501
        :type: str
        """
        if file_name is None:
            raise ValueError("Invalid value for `file_name`, must not be `None`")  # noqa: E501

        self._file_name = file_name

    @property
    def storage_file_name(self):
        """Gets the storage_file_name of this BatchUpload.  # noqa: E501


        :return: The storage_file_name of this BatchUpload.  # noqa: E501
        :rtype: str
        """
        return self._storage_file_name

    @storage_file_name.setter
    def storage_file_name(self, storage_file_name):
        """Sets the storage_file_name of this BatchUpload.


        :param storage_file_name: The storage_file_name of this BatchUpload.  # noqa: E501
        :type: str
        """
        if storage_file_name is None:
            raise ValueError("Invalid value for `storage_file_name`, must not be `None`")  # noqa: E501

        self._storage_file_name = storage_file_name

    @property
    def error_filename(self):
        """Gets the error_filename of this BatchUpload.  # noqa: E501


        :return: The error_filename of this BatchUpload.  # noqa: E501
        :rtype: str
        """
        return self._error_filename

    @error_filename.setter
    def error_filename(self, error_filename):
        """Sets the error_filename of this BatchUpload.


        :param error_filename: The error_filename of this BatchUpload.  # noqa: E501
        :type: str
        """
        if error_filename is None:
            raise ValueError("Invalid value for `error_filename`, must not be `None`")  # noqa: E501

        self._error_filename = error_filename

    @property
    def row_count(self):
        """Gets the row_count of this BatchUpload.  # noqa: E501


        :return: The row_count of this BatchUpload.  # noqa: E501
        :rtype: int
        """
        return self._row_count

    @row_count.setter
    def row_count(self, row_count):
        """Sets the row_count of this BatchUpload.


        :param row_count: The row_count of this BatchUpload.  # noqa: E501
        :type: int
        """
        if row_count is None:
            raise ValueError("Invalid value for `row_count`, must not be `None`")  # noqa: E501

        self._row_count = row_count

    @property
    def status(self):
        """Gets the status of this BatchUpload.  # noqa: E501


        :return: The status of this BatchUpload.  # noqa: E501
        :rtype: BatchUploadStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BatchUpload.


        :param status: The status of this BatchUpload.  # noqa: E501
        :type: BatchUploadStatus
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this BatchUpload.  # noqa: E501


        :return: The created_at of this BatchUpload.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BatchUpload.


        :param created_at: The created_at of this BatchUpload.  # noqa: E501
        :type: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this BatchUpload.  # noqa: E501


        :return: The modified_at of this BatchUpload.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this BatchUpload.


        :param modified_at: The modified_at of this BatchUpload.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

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
        if issubclass(BatchUpload, dict):
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
        if not isinstance(other, BatchUpload):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

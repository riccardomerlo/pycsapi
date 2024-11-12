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

class GetKYCProfileAttachmentDetailsByAttachmentId(object):
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
        'file_name': 'str',
        'file_size_in_bytes': 'int',
        'document_type': 'str',
        'description': 'str',
        'created_at': 'datetime',
        'created_by_id': 'int',
        'created_by': 'str',
        'modified_at': 'datetime',
        'modified_by_id': 'int',
        'modified_by': 'str',
        'linked_to': 'str'
    }

    attribute_map = {
        'id': 'id',
        'file_name': 'fileName',
        'file_size_in_bytes': 'fileSizeInBytes',
        'document_type': 'documentType',
        'description': 'description',
        'created_at': 'createdAt',
        'created_by_id': 'createdById',
        'created_by': 'createdBy',
        'modified_at': 'modifiedAt',
        'modified_by_id': 'modifiedById',
        'modified_by': 'modifiedBy',
        'linked_to': 'linkedTo'
    }

    def __init__(self, id=None, file_name=None, file_size_in_bytes=None, document_type=None, description=None, created_at=None, created_by_id=None, created_by=None, modified_at=None, modified_by_id=None, modified_by=None, linked_to=None):  # noqa: E501
        """GetKYCProfileAttachmentDetailsByAttachmentId - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._file_name = None
        self._file_size_in_bytes = None
        self._document_type = None
        self._description = None
        self._created_at = None
        self._created_by_id = None
        self._created_by = None
        self._modified_at = None
        self._modified_by_id = None
        self._modified_by = None
        self._linked_to = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if file_name is not None:
            self.file_name = file_name
        if file_size_in_bytes is not None:
            self.file_size_in_bytes = file_size_in_bytes
        if document_type is not None:
            self.document_type = document_type
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_by is not None:
            self.created_by = created_by
        if modified_at is not None:
            self.modified_at = modified_at
        if modified_by_id is not None:
            self.modified_by_id = modified_by_id
        if modified_by is not None:
            self.modified_by = modified_by
        if linked_to is not None:
            self.linked_to = linked_to

    @property
    def id(self):
        """Gets the id of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501

        Attachment Id.  # noqa: E501

        :return: The id of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetKYCProfileAttachmentDetailsByAttachmentId.

        Attachment Id.  # noqa: E501

        :param id: The id of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def file_name(self):
        """Gets the file_name of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501

        Example : passport.pdf  Attachment Name.  # noqa: E501

        :return: The file_name of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this GetKYCProfileAttachmentDetailsByAttachmentId.

        Example : passport.pdf  Attachment Name.  # noqa: E501

        :param file_name: The file_name of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :type: str
        """

        self._file_name = file_name

    @property
    def file_size_in_bytes(self):
        """Gets the file_size_in_bytes of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501

        Size of the attachment in bytes.  # noqa: E501

        :return: The file_size_in_bytes of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :rtype: int
        """
        return self._file_size_in_bytes

    @file_size_in_bytes.setter
    def file_size_in_bytes(self, file_size_in_bytes):
        """Sets the file_size_in_bytes of this GetKYCProfileAttachmentDetailsByAttachmentId.

        Size of the attachment in bytes.  # noqa: E501

        :param file_size_in_bytes: The file_size_in_bytes of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :type: int
        """

        self._file_size_in_bytes = file_size_in_bytes

    @property
    def document_type(self):
        """Gets the document_type of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501

        Document type of the attachment.  # noqa: E501

        :return: The document_type of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this GetKYCProfileAttachmentDetailsByAttachmentId.

        Document type of the attachment.  # noqa: E501

        :param document_type: The document_type of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :type: str
        """

        self._document_type = document_type

    @property
    def description(self):
        """Gets the description of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501

        Description of the attachment.  # noqa: E501

        :return: The description of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetKYCProfileAttachmentDetailsByAttachmentId.

        Description of the attachment.  # noqa: E501

        :param description: The description of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501

        Attachment uploaded time.  # noqa: E501

        :return: The created_at of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GetKYCProfileAttachmentDetailsByAttachmentId.

        Attachment uploaded time.  # noqa: E501

        :param created_at: The created_at of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def created_by_id(self):
        """Gets the created_by_id of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501

        Attachment uploaded by user id  # noqa: E501

        :return: The created_by_id of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :rtype: int
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this GetKYCProfileAttachmentDetailsByAttachmentId.

        Attachment uploaded by user id  # noqa: E501

        :param created_by_id: The created_by_id of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :type: int
        """

        self._created_by_id = created_by_id

    @property
    def created_by(self):
        """Gets the created_by of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501

        Attachment uploaded by user  # noqa: E501

        :return: The created_by of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this GetKYCProfileAttachmentDetailsByAttachmentId.

        Attachment uploaded by user  # noqa: E501

        :param created_by: The created_by of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def modified_at(self):
        """Gets the modified_at of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501

        Attachment modified time  # noqa: E501

        :return: The modified_at of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this GetKYCProfileAttachmentDetailsByAttachmentId.

        Attachment modified time  # noqa: E501

        :param modified_at: The modified_at of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def modified_by_id(self):
        """Gets the modified_by_id of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501

        Attachment modified by user id  # noqa: E501

        :return: The modified_by_id of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :rtype: int
        """
        return self._modified_by_id

    @modified_by_id.setter
    def modified_by_id(self, modified_by_id):
        """Sets the modified_by_id of this GetKYCProfileAttachmentDetailsByAttachmentId.

        Attachment modified by user id  # noqa: E501

        :param modified_by_id: The modified_by_id of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :type: int
        """

        self._modified_by_id = modified_by_id

    @property
    def modified_by(self):
        """Gets the modified_by of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501

        Attachment modified by user  # noqa: E501

        :return: The modified_by of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this GetKYCProfileAttachmentDetailsByAttachmentId.

        Attachment modified by user  # noqa: E501

        :param modified_by: The modified_by of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def linked_to(self):
        """Gets the linked_to of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501

        The profile component to which current attachment is linked to.  # noqa: E501

        :return: The linked_to of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :rtype: str
        """
        return self._linked_to

    @linked_to.setter
    def linked_to(self, linked_to):
        """Sets the linked_to of this GetKYCProfileAttachmentDetailsByAttachmentId.

        The profile component to which current attachment is linked to.  # noqa: E501

        :param linked_to: The linked_to of this GetKYCProfileAttachmentDetailsByAttachmentId.  # noqa: E501
        :type: str
        """

        self._linked_to = linked_to

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
        if issubclass(GetKYCProfileAttachmentDetailsByAttachmentId, dict):
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
        if not isinstance(other, GetKYCProfileAttachmentDetailsByAttachmentId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

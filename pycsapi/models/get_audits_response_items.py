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

class GetAuditsResponseItems(object):
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
        'description': 'str',
        'category': 'str',
        'subcategory': 'str',
        'action': 'str',
        'created_at': 'datetime',
        'created_by_id': 'int',
        'created_by': 'str',
        'payload': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'category': 'category',
        'subcategory': 'subcategory',
        'action': 'action',
        'created_at': 'createdAt',
        'created_by_id': 'createdById',
        'created_by': 'createdBy',
        'payload': 'payload'
    }

    def __init__(self, id=None, description=None, category=None, subcategory=None, action=None, created_at=None, created_by_id=None, created_by=None, payload=None):  # noqa: E501
        """GetAuditsResponseItems - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._description = None
        self._category = None
        self._subcategory = None
        self._action = None
        self._created_at = None
        self._created_by_id = None
        self._created_by = None
        self._payload = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if category is not None:
            self.category = category
        if subcategory is not None:
            self.subcategory = subcategory
        if action is not None:
            self.action = action
        if created_at is not None:
            self.created_at = created_at
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_by is not None:
            self.created_by = created_by
        if payload is not None:
            self.payload = payload

    @property
    def id(self):
        """Gets the id of this GetAuditsResponseItems.  # noqa: E501

        Id of the Audit  # noqa: E501

        :return: The id of this GetAuditsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetAuditsResponseItems.

        Id of the Audit  # noqa: E501

        :param id: The id of this GetAuditsResponseItems.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def description(self):
        """Gets the description of this GetAuditsResponseItems.  # noqa: E501

        Description of the Audit  # noqa: E501

        :return: The description of this GetAuditsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetAuditsResponseItems.

        Description of the Audit  # noqa: E501

        :param description: The description of this GetAuditsResponseItems.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def category(self):
        """Gets the category of this GetAuditsResponseItems.  # noqa: E501

        Category of the audit  # noqa: E501

        :return: The category of this GetAuditsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this GetAuditsResponseItems.

        Category of the audit  # noqa: E501

        :param category: The category of this GetAuditsResponseItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["profile", "amlSearch"]  # noqa: E501
        if category not in allowed_values:
            raise ValueError(
                "Invalid value for `category` ({0}), must be one of {1}"  # noqa: E501
                .format(category, allowed_values)
            )

        self._category = category

    @property
    def subcategory(self):
        """Gets the subcategory of this GetAuditsResponseItems.  # noqa: E501

        Subcategory of the audit  # noqa: E501

        :return: The subcategory of this GetAuditsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._subcategory

    @subcategory.setter
    def subcategory(self, subcategory):
        """Sets the subcategory of this GetAuditsResponseItems.

        Subcategory of the audit  # noqa: E501

        :param subcategory: The subcategory of this GetAuditsResponseItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["profileDetails", "keyParty", "amlMonitoring"]  # noqa: E501
        if subcategory not in allowed_values:
            raise ValueError(
                "Invalid value for `subcategory` ({0}), must be one of {1}"  # noqa: E501
                .format(subcategory, allowed_values)
            )

        self._subcategory = subcategory

    @property
    def action(self):
        """Gets the action of this GetAuditsResponseItems.  # noqa: E501

        Action of the audit  # noqa: E501

        :return: The action of this GetAuditsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this GetAuditsResponseItems.

        Action of the audit  # noqa: E501

        :param action: The action of this GetAuditsResponseItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["created", "updated", "deleted", "searchRemoved", "searchLinked", "attachmentCreated", "attachmentUpdated", "attachmentDeleted", "noteCreated", "noteUpdated", "noteDeleted", "noteArchived", "noteUnarchived", "addressCreated", "addressUpdated", "addressDeleted", "kycStatusUpdated", "addedToAmlMonitoring", "updatedInAmlMonitoring", "removedFromAmlMonitoring"]  # noqa: E501
        if action not in allowed_values:
            raise ValueError(
                "Invalid value for `action` ({0}), must be one of {1}"  # noqa: E501
                .format(action, allowed_values)
            )

        self._action = action

    @property
    def created_at(self):
        """Gets the created_at of this GetAuditsResponseItems.  # noqa: E501

        Audit created date and time  # noqa: E501

        :return: The created_at of this GetAuditsResponseItems.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GetAuditsResponseItems.

        Audit created date and time  # noqa: E501

        :param created_at: The created_at of this GetAuditsResponseItems.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def created_by_id(self):
        """Gets the created_by_id of this GetAuditsResponseItems.  # noqa: E501

        Id of the user who created the audit  # noqa: E501

        :return: The created_by_id of this GetAuditsResponseItems.  # noqa: E501
        :rtype: int
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this GetAuditsResponseItems.

        Id of the user who created the audit  # noqa: E501

        :param created_by_id: The created_by_id of this GetAuditsResponseItems.  # noqa: E501
        :type: int
        """

        self._created_by_id = created_by_id

    @property
    def created_by(self):
        """Gets the created_by of this GetAuditsResponseItems.  # noqa: E501

        Name of the user who created the audit  # noqa: E501

        :return: The created_by of this GetAuditsResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this GetAuditsResponseItems.

        Name of the user who created the audit  # noqa: E501

        :param created_by: The created_by of this GetAuditsResponseItems.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def payload(self):
        """Gets the payload of this GetAuditsResponseItems.  # noqa: E501

        The `payload` property represents the state of involved entities at the time of action taking place.<br><br> This property contains dynamic data that varies depending on the request parameters and the context of the request. The response and can differ even with the same parameters under different conditions or contexts.<br><br> This means the content of this property is not fixed and can include various data types such as GUIDs, strings, integers, and complex objects.<br><br> Due to its dynamic nature, the `payload` can include any of the following potential structures, but is not limited to these examples <li> A single key-value pair where the value is a string or number. <li> A nested object containing detailed data structures. <li> An array of objects each with different attributes.<br><br> Consumers of this API should handle the `payload` dynamically and be prepared to encounter different data types and structures.<br> Detailed processing logic based on the specific application needs and context checks is recommended when utilising this field.  # noqa: E501

        :return: The payload of this GetAuditsResponseItems.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._payload

    @payload.setter
    def payload(self, payload):
        """Sets the payload of this GetAuditsResponseItems.

        The `payload` property represents the state of involved entities at the time of action taking place.<br><br> This property contains dynamic data that varies depending on the request parameters and the context of the request. The response and can differ even with the same parameters under different conditions or contexts.<br><br> This means the content of this property is not fixed and can include various data types such as GUIDs, strings, integers, and complex objects.<br><br> Due to its dynamic nature, the `payload` can include any of the following potential structures, but is not limited to these examples <li> A single key-value pair where the value is a string or number. <li> A nested object containing detailed data structures. <li> An array of objects each with different attributes.<br><br> Consumers of this API should handle the `payload` dynamically and be prepared to encounter different data types and structures.<br> Detailed processing logic based on the specific application needs and context checks is recommended when utilising this field.  # noqa: E501

        :param payload: The payload of this GetAuditsResponseItems.  # noqa: E501
        :type: dict(str, object)
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
        if issubclass(GetAuditsResponseItems, dict):
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
        if not isinstance(other, GetAuditsResponseItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

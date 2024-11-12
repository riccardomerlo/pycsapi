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

class UpdateKYCProfileByProfileIdRequest(object):
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
        'name': 'str',
        'risk_rating': 'str',
        'status': 'str',
        'internal_id': 'str',
        'assigned_to_id': 'object',
        'kyc_review_on': 'object',
        'kyc_comments': 'str'
    }

    attribute_map = {
        'name': 'name',
        'risk_rating': 'riskRating',
        'status': 'status',
        'internal_id': 'internalId',
        'assigned_to_id': 'assignedToId',
        'kyc_review_on': 'kycReviewOn',
        'kyc_comments': 'kycComments'
    }

    def __init__(self, name=None, risk_rating=None, status=None, internal_id=None, assigned_to_id=None, kyc_review_on=None, kyc_comments=None):  # noqa: E501
        """UpdateKYCProfileByProfileIdRequest - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._risk_rating = None
        self._status = None
        self._internal_id = None
        self._assigned_to_id = None
        self._kyc_review_on = None
        self._kyc_comments = None
        self.discriminator = None
        self.name = name
        self.risk_rating = risk_rating
        self.status = status
        if internal_id is not None:
            self.internal_id = internal_id
        if assigned_to_id is not None:
            self.assigned_to_id = assigned_to_id
        if kyc_review_on is not None:
            self.kyc_review_on = kyc_review_on
        if kyc_comments is not None:
            self.kyc_comments = kyc_comments

    @property
    def name(self):
        """Gets the name of this UpdateKYCProfileByProfileIdRequest.  # noqa: E501

        The name of the profile to be updated.  # noqa: E501

        :return: The name of this UpdateKYCProfileByProfileIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateKYCProfileByProfileIdRequest.

        The name of the profile to be updated.  # noqa: E501

        :param name: The name of this UpdateKYCProfileByProfileIdRequest.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def risk_rating(self):
        """Gets the risk_rating of this UpdateKYCProfileByProfileIdRequest.  # noqa: E501

        Risk rating of the profile.  # noqa: E501

        :return: The risk_rating of this UpdateKYCProfileByProfileIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._risk_rating

    @risk_rating.setter
    def risk_rating(self, risk_rating):
        """Sets the risk_rating of this UpdateKYCProfileByProfileIdRequest.

        Risk rating of the profile.  # noqa: E501

        :param risk_rating: The risk_rating of this UpdateKYCProfileByProfileIdRequest.  # noqa: E501
        :type: str
        """
        if risk_rating is None:
            raise ValueError("Invalid value for `risk_rating`, must not be `None`")  # noqa: E501
        allowed_values = ["notApplicable", "veryLow", "low", "medium", "high", "veryHigh"]  # noqa: E501
        if risk_rating not in allowed_values:
            raise ValueError(
                "Invalid value for `risk_rating` ({0}), must be one of {1}"  # noqa: E501
                .format(risk_rating, allowed_values)
            )

        self._risk_rating = risk_rating

    @property
    def status(self):
        """Gets the status of this UpdateKYCProfileByProfileIdRequest.  # noqa: E501

        Status of the profile.  # noqa: E501

        :return: The status of this UpdateKYCProfileByProfileIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateKYCProfileByProfileIdRequest.

        Status of the profile.  # noqa: E501

        :param status: The status of this UpdateKYCProfileByProfileIdRequest.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["new", "approved", "declined", "pending", "cancelled", "referred", "closed", "approvedReviewDue"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def internal_id(self):
        """Gets the internal_id of this UpdateKYCProfileByProfileIdRequest.  # noqa: E501

        Internal ID of the profile, this MUST be unique across your profiles.  # noqa: E501

        :return: The internal_id of this UpdateKYCProfileByProfileIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._internal_id

    @internal_id.setter
    def internal_id(self, internal_id):
        """Sets the internal_id of this UpdateKYCProfileByProfileIdRequest.

        Internal ID of the profile, this MUST be unique across your profiles.  # noqa: E501

        :param internal_id: The internal_id of this UpdateKYCProfileByProfileIdRequest.  # noqa: E501
        :type: str
        """

        self._internal_id = internal_id

    @property
    def assigned_to_id(self):
        """Gets the assigned_to_id of this UpdateKYCProfileByProfileIdRequest.  # noqa: E501

        Creditsafe Id of the user to assign the profile to. <br> Passing null will unassign the profile.  # noqa: E501

        :return: The assigned_to_id of this UpdateKYCProfileByProfileIdRequest.  # noqa: E501
        :rtype: object
        """
        return self._assigned_to_id

    @assigned_to_id.setter
    def assigned_to_id(self, assigned_to_id):
        """Sets the assigned_to_id of this UpdateKYCProfileByProfileIdRequest.

        Creditsafe Id of the user to assign the profile to. <br> Passing null will unassign the profile.  # noqa: E501

        :param assigned_to_id: The assigned_to_id of this UpdateKYCProfileByProfileIdRequest.  # noqa: E501
        :type: object
        """

        self._assigned_to_id = assigned_to_id

    @property
    def kyc_review_on(self):
        """Gets the kyc_review_on of this UpdateKYCProfileByProfileIdRequest.  # noqa: E501

        The date to which the profile should be reviewed. <br> Format YYYY-MM-DD <br> Validates when the date changes and is either current or in the future.  # noqa: E501

        :return: The kyc_review_on of this UpdateKYCProfileByProfileIdRequest.  # noqa: E501
        :rtype: object
        """
        return self._kyc_review_on

    @kyc_review_on.setter
    def kyc_review_on(self, kyc_review_on):
        """Sets the kyc_review_on of this UpdateKYCProfileByProfileIdRequest.

        The date to which the profile should be reviewed. <br> Format YYYY-MM-DD <br> Validates when the date changes and is either current or in the future.  # noqa: E501

        :param kyc_review_on: The kyc_review_on of this UpdateKYCProfileByProfileIdRequest.  # noqa: E501
        :type: object
        """

        self._kyc_review_on = kyc_review_on

    @property
    def kyc_comments(self):
        """Gets the kyc_comments of this UpdateKYCProfileByProfileIdRequest.  # noqa: E501

        Free text field for users to highlight key information to other users. <br> Maximum characters allowed is 250  # noqa: E501

        :return: The kyc_comments of this UpdateKYCProfileByProfileIdRequest.  # noqa: E501
        :rtype: str
        """
        return self._kyc_comments

    @kyc_comments.setter
    def kyc_comments(self, kyc_comments):
        """Sets the kyc_comments of this UpdateKYCProfileByProfileIdRequest.

        Free text field for users to highlight key information to other users. <br> Maximum characters allowed is 250  # noqa: E501

        :param kyc_comments: The kyc_comments of this UpdateKYCProfileByProfileIdRequest.  # noqa: E501
        :type: str
        """

        self._kyc_comments = kyc_comments

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
        if issubclass(UpdateKYCProfileByProfileIdRequest, dict):
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
        if not isinstance(other, UpdateKYCProfileByProfileIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

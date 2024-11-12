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

class UpdateKYCProfileByProfileId(object):
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
        'name': 'str',
        'risk_rating': 'str',
        'status': 'str',
        'type': 'str',
        'internal_id': 'str',
        'assigned_to_id': 'int',
        'assigned_to': 'str',
        'safe_number': 'str',
        'company_id': 'str',
        'formation_date': 'date',
        'created_at': 'datetime',
        'created_by_id': 'int',
        'created_by': 'str',
        'modified_at': 'datetime',
        'modified_by_id': 'int',
        'modified_by': 'str',
        'kyc_approved_at': 'datetime',
        'kyc_review_on': 'date',
        'kyc_status_updated_on': 'datetime',
        'kyc_comments': 'str',
        'note_count': 'int',
        'attachment_count': 'int',
        'key_party_count': 'int',
        'ubo_count': 'int',
        'open_alert_count': 'int',
        'mode_of_creation': 'str',
        'import_status': 'str',
        'is_locked': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'risk_rating': 'riskRating',
        'status': 'status',
        'type': 'type',
        'internal_id': 'internalId',
        'assigned_to_id': 'assignedToId',
        'assigned_to': 'assignedTo',
        'safe_number': 'safeNumber',
        'company_id': 'companyId',
        'formation_date': 'formationDate',
        'created_at': 'createdAt',
        'created_by_id': 'createdById',
        'created_by': 'createdBy',
        'modified_at': 'modifiedAt',
        'modified_by_id': 'modifiedById',
        'modified_by': 'modifiedBy',
        'kyc_approved_at': 'kycApprovedAt',
        'kyc_review_on': 'kycReviewOn',
        'kyc_status_updated_on': 'kycStatusUpdatedOn',
        'kyc_comments': 'kycComments',
        'note_count': 'noteCount',
        'attachment_count': 'attachmentCount',
        'key_party_count': 'keyPartyCount',
        'ubo_count': 'uboCount',
        'open_alert_count': 'openAlertCount',
        'mode_of_creation': 'modeOfCreation',
        'import_status': 'importStatus',
        'is_locked': 'isLocked'
    }

    def __init__(self, id=None, name=None, risk_rating=None, status=None, type=None, internal_id=None, assigned_to_id=None, assigned_to=None, safe_number=None, company_id=None, formation_date=None, created_at=None, created_by_id=None, created_by=None, modified_at=None, modified_by_id=None, modified_by=None, kyc_approved_at=None, kyc_review_on=None, kyc_status_updated_on=None, kyc_comments=None, note_count=None, attachment_count=None, key_party_count=None, ubo_count=None, open_alert_count=None, mode_of_creation=None, import_status=None, is_locked=None):  # noqa: E501
        """UpdateKYCProfileByProfileId - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._risk_rating = None
        self._status = None
        self._type = None
        self._internal_id = None
        self._assigned_to_id = None
        self._assigned_to = None
        self._safe_number = None
        self._company_id = None
        self._formation_date = None
        self._created_at = None
        self._created_by_id = None
        self._created_by = None
        self._modified_at = None
        self._modified_by_id = None
        self._modified_by = None
        self._kyc_approved_at = None
        self._kyc_review_on = None
        self._kyc_status_updated_on = None
        self._kyc_comments = None
        self._note_count = None
        self._attachment_count = None
        self._key_party_count = None
        self._ubo_count = None
        self._open_alert_count = None
        self._mode_of_creation = None
        self._import_status = None
        self._is_locked = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if risk_rating is not None:
            self.risk_rating = risk_rating
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if internal_id is not None:
            self.internal_id = internal_id
        if assigned_to_id is not None:
            self.assigned_to_id = assigned_to_id
        if assigned_to is not None:
            self.assigned_to = assigned_to
        if safe_number is not None:
            self.safe_number = safe_number
        if company_id is not None:
            self.company_id = company_id
        if formation_date is not None:
            self.formation_date = formation_date
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
        if kyc_approved_at is not None:
            self.kyc_approved_at = kyc_approved_at
        if kyc_review_on is not None:
            self.kyc_review_on = kyc_review_on
        if kyc_status_updated_on is not None:
            self.kyc_status_updated_on = kyc_status_updated_on
        if kyc_comments is not None:
            self.kyc_comments = kyc_comments
        if note_count is not None:
            self.note_count = note_count
        if attachment_count is not None:
            self.attachment_count = attachment_count
        if key_party_count is not None:
            self.key_party_count = key_party_count
        if ubo_count is not None:
            self.ubo_count = ubo_count
        if open_alert_count is not None:
            self.open_alert_count = open_alert_count
        if mode_of_creation is not None:
            self.mode_of_creation = mode_of_creation
        if import_status is not None:
            self.import_status = import_status
        if is_locked is not None:
            self.is_locked = is_locked

    @property
    def id(self):
        """Gets the id of this UpdateKYCProfileByProfileId.  # noqa: E501

        Id of the Profile  # noqa: E501

        :return: The id of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateKYCProfileByProfileId.

        Id of the Profile  # noqa: E501

        :param id: The id of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdateKYCProfileByProfileId.  # noqa: E501

        Name of the Profile  # noqa: E501

        :return: The name of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateKYCProfileByProfileId.

        Name of the Profile  # noqa: E501

        :param name: The name of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def risk_rating(self):
        """Gets the risk_rating of this UpdateKYCProfileByProfileId.  # noqa: E501

        The risk rating being assigned to the profile  # noqa: E501

        :return: The risk_rating of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: str
        """
        return self._risk_rating

    @risk_rating.setter
    def risk_rating(self, risk_rating):
        """Sets the risk_rating of this UpdateKYCProfileByProfileId.

        The risk rating being assigned to the profile  # noqa: E501

        :param risk_rating: The risk_rating of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: str
        """
        allowed_values = ["notApplicable", "veryLow", "low", "medium", "high", "veryHigh"]  # noqa: E501
        if risk_rating not in allowed_values:
            raise ValueError(
                "Invalid value for `risk_rating` ({0}), must be one of {1}"  # noqa: E501
                .format(risk_rating, allowed_values)
            )

        self._risk_rating = risk_rating

    @property
    def status(self):
        """Gets the status of this UpdateKYCProfileByProfileId.  # noqa: E501

        Status of the profile (new, approved, declined, pending, cancelled, referred, closed, approvedReviewDue)  # noqa: E501

        :return: The status of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateKYCProfileByProfileId.

        Status of the profile (new, approved, declined, pending, cancelled, referred, closed, approvedReviewDue)  # noqa: E501

        :param status: The status of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def type(self):
        """Gets the type of this UpdateKYCProfileByProfileId.  # noqa: E501

        Type of the profile (trust, individual, soleTrader, company, plc, partnership, otherEntity)  # noqa: E501

        :return: The type of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateKYCProfileByProfileId.

        Type of the profile (trust, individual, soleTrader, company, plc, partnership, otherEntity)  # noqa: E501

        :param type: The type of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def internal_id(self):
        """Gets the internal_id of this UpdateKYCProfileByProfileId.  # noqa: E501

        Internal Id of the profile.  # noqa: E501

        :return: The internal_id of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: str
        """
        return self._internal_id

    @internal_id.setter
    def internal_id(self, internal_id):
        """Sets the internal_id of this UpdateKYCProfileByProfileId.

        Internal Id of the profile.  # noqa: E501

        :param internal_id: The internal_id of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: str
        """

        self._internal_id = internal_id

    @property
    def assigned_to_id(self):
        """Gets the assigned_to_id of this UpdateKYCProfileByProfileId.  # noqa: E501

        Id of the user assigned to the profile  # noqa: E501

        :return: The assigned_to_id of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: int
        """
        return self._assigned_to_id

    @assigned_to_id.setter
    def assigned_to_id(self, assigned_to_id):
        """Sets the assigned_to_id of this UpdateKYCProfileByProfileId.

        Id of the user assigned to the profile  # noqa: E501

        :param assigned_to_id: The assigned_to_id of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: int
        """

        self._assigned_to_id = assigned_to_id

    @property
    def assigned_to(self):
        """Gets the assigned_to of this UpdateKYCProfileByProfileId.  # noqa: E501

        Name of the user assigned to the profile  # noqa: E501

        :return: The assigned_to of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: str
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to):
        """Sets the assigned_to of this UpdateKYCProfileByProfileId.

        Name of the user assigned to the profile  # noqa: E501

        :param assigned_to: The assigned_to of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: str
        """

        self._assigned_to = assigned_to

    @property
    def safe_number(self):
        """Gets the safe_number of this UpdateKYCProfileByProfileId.  # noqa: E501

        safe number of the business linked to the profile  # noqa: E501

        :return: The safe_number of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: str
        """
        return self._safe_number

    @safe_number.setter
    def safe_number(self, safe_number):
        """Sets the safe_number of this UpdateKYCProfileByProfileId.

        safe number of the business linked to the profile  # noqa: E501

        :param safe_number: The safe_number of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: str
        """

        self._safe_number = safe_number

    @property
    def company_id(self):
        """Gets the company_id of this UpdateKYCProfileByProfileId.  # noqa: E501

        company id of the business linked to the profile  # noqa: E501

        :return: The company_id of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this UpdateKYCProfileByProfileId.

        company id of the business linked to the profile  # noqa: E501

        :param company_id: The company_id of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def formation_date(self):
        """Gets the formation_date of this UpdateKYCProfileByProfileId.  # noqa: E501

        Formation date of the business linked to the profile  # noqa: E501

        :return: The formation_date of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: date
        """
        return self._formation_date

    @formation_date.setter
    def formation_date(self, formation_date):
        """Sets the formation_date of this UpdateKYCProfileByProfileId.

        Formation date of the business linked to the profile  # noqa: E501

        :param formation_date: The formation_date of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: date
        """

        self._formation_date = formation_date

    @property
    def created_at(self):
        """Gets the created_at of this UpdateKYCProfileByProfileId.  # noqa: E501

        Profile created time  # noqa: E501

        :return: The created_at of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UpdateKYCProfileByProfileId.

        Profile created time  # noqa: E501

        :param created_at: The created_at of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def created_by_id(self):
        """Gets the created_by_id of this UpdateKYCProfileByProfileId.  # noqa: E501

        Id of the user who created the profile  # noqa: E501

        :return: The created_by_id of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: int
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this UpdateKYCProfileByProfileId.

        Id of the user who created the profile  # noqa: E501

        :param created_by_id: The created_by_id of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: int
        """

        self._created_by_id = created_by_id

    @property
    def created_by(self):
        """Gets the created_by of this UpdateKYCProfileByProfileId.  # noqa: E501

        Name of the user who created the profile  # noqa: E501

        :return: The created_by of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this UpdateKYCProfileByProfileId.

        Name of the user who created the profile  # noqa: E501

        :param created_by: The created_by of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def modified_at(self):
        """Gets the modified_at of this UpdateKYCProfileByProfileId.  # noqa: E501

        Profile last updated time  # noqa: E501

        :return: The modified_at of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this UpdateKYCProfileByProfileId.

        Profile last updated time  # noqa: E501

        :param modified_at: The modified_at of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def modified_by_id(self):
        """Gets the modified_by_id of this UpdateKYCProfileByProfileId.  # noqa: E501

        Id of the user who last modified the profile  # noqa: E501

        :return: The modified_by_id of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: int
        """
        return self._modified_by_id

    @modified_by_id.setter
    def modified_by_id(self, modified_by_id):
        """Sets the modified_by_id of this UpdateKYCProfileByProfileId.

        Id of the user who last modified the profile  # noqa: E501

        :param modified_by_id: The modified_by_id of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: int
        """

        self._modified_by_id = modified_by_id

    @property
    def modified_by(self):
        """Gets the modified_by of this UpdateKYCProfileByProfileId.  # noqa: E501

        Name of the user who last modified the profile  # noqa: E501

        :return: The modified_by of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this UpdateKYCProfileByProfileId.

        Name of the user who last modified the profile  # noqa: E501

        :param modified_by: The modified_by of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def kyc_approved_at(self):
        """Gets the kyc_approved_at of this UpdateKYCProfileByProfileId.  # noqa: E501

        Date when the profile got approved  # noqa: E501

        :return: The kyc_approved_at of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: datetime
        """
        return self._kyc_approved_at

    @kyc_approved_at.setter
    def kyc_approved_at(self, kyc_approved_at):
        """Sets the kyc_approved_at of this UpdateKYCProfileByProfileId.

        Date when the profile got approved  # noqa: E501

        :param kyc_approved_at: The kyc_approved_at of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: datetime
        """

        self._kyc_approved_at = kyc_approved_at

    @property
    def kyc_review_on(self):
        """Gets the kyc_review_on of this UpdateKYCProfileByProfileId.  # noqa: E501

        Date when profile is to be reviewed  # noqa: E501

        :return: The kyc_review_on of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: date
        """
        return self._kyc_review_on

    @kyc_review_on.setter
    def kyc_review_on(self, kyc_review_on):
        """Sets the kyc_review_on of this UpdateKYCProfileByProfileId.

        Date when profile is to be reviewed  # noqa: E501

        :param kyc_review_on: The kyc_review_on of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: date
        """

        self._kyc_review_on = kyc_review_on

    @property
    def kyc_status_updated_on(self):
        """Gets the kyc_status_updated_on of this UpdateKYCProfileByProfileId.  # noqa: E501

        Date when the profile status was last updated  # noqa: E501

        :return: The kyc_status_updated_on of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: datetime
        """
        return self._kyc_status_updated_on

    @kyc_status_updated_on.setter
    def kyc_status_updated_on(self, kyc_status_updated_on):
        """Sets the kyc_status_updated_on of this UpdateKYCProfileByProfileId.

        Date when the profile status was last updated  # noqa: E501

        :param kyc_status_updated_on: The kyc_status_updated_on of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: datetime
        """

        self._kyc_status_updated_on = kyc_status_updated_on

    @property
    def kyc_comments(self):
        """Gets the kyc_comments of this UpdateKYCProfileByProfileId.  # noqa: E501

        Profile comments  # noqa: E501

        :return: The kyc_comments of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: str
        """
        return self._kyc_comments

    @kyc_comments.setter
    def kyc_comments(self, kyc_comments):
        """Sets the kyc_comments of this UpdateKYCProfileByProfileId.

        Profile comments  # noqa: E501

        :param kyc_comments: The kyc_comments of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: str
        """

        self._kyc_comments = kyc_comments

    @property
    def note_count(self):
        """Gets the note_count of this UpdateKYCProfileByProfileId.  # noqa: E501

        Count of notes associated with profile  # noqa: E501

        :return: The note_count of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: int
        """
        return self._note_count

    @note_count.setter
    def note_count(self, note_count):
        """Sets the note_count of this UpdateKYCProfileByProfileId.

        Count of notes associated with profile  # noqa: E501

        :param note_count: The note_count of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: int
        """

        self._note_count = note_count

    @property
    def attachment_count(self):
        """Gets the attachment_count of this UpdateKYCProfileByProfileId.  # noqa: E501

        Count of attachments associated with profile  # noqa: E501

        :return: The attachment_count of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: int
        """
        return self._attachment_count

    @attachment_count.setter
    def attachment_count(self, attachment_count):
        """Sets the attachment_count of this UpdateKYCProfileByProfileId.

        Count of attachments associated with profile  # noqa: E501

        :param attachment_count: The attachment_count of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: int
        """

        self._attachment_count = attachment_count

    @property
    def key_party_count(self):
        """Gets the key_party_count of this UpdateKYCProfileByProfileId.  # noqa: E501

        Count of key parties associated with profile  # noqa: E501

        :return: The key_party_count of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: int
        """
        return self._key_party_count

    @key_party_count.setter
    def key_party_count(self, key_party_count):
        """Sets the key_party_count of this UpdateKYCProfileByProfileId.

        Count of key parties associated with profile  # noqa: E501

        :param key_party_count: The key_party_count of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: int
        """

        self._key_party_count = key_party_count

    @property
    def ubo_count(self):
        """Gets the ubo_count of this UpdateKYCProfileByProfileId.  # noqa: E501

        Count of UBOs associated with profile  # noqa: E501

        :return: The ubo_count of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: int
        """
        return self._ubo_count

    @ubo_count.setter
    def ubo_count(self, ubo_count):
        """Sets the ubo_count of this UpdateKYCProfileByProfileId.

        Count of UBOs associated with profile  # noqa: E501

        :param ubo_count: The ubo_count of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: int
        """

        self._ubo_count = ubo_count

    @property
    def open_alert_count(self):
        """Gets the open_alert_count of this UpdateKYCProfileByProfileId.  # noqa: E501

        Count of Open Alerts  # noqa: E501

        :return: The open_alert_count of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: int
        """
        return self._open_alert_count

    @open_alert_count.setter
    def open_alert_count(self, open_alert_count):
        """Sets the open_alert_count of this UpdateKYCProfileByProfileId.

        Count of Open Alerts  # noqa: E501

        :param open_alert_count: The open_alert_count of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: int
        """

        self._open_alert_count = open_alert_count

    @property
    def mode_of_creation(self):
        """Gets the mode_of_creation of this UpdateKYCProfileByProfileId.  # noqa: E501

        Mode of profile creation (manual, import)  # noqa: E501

        :return: The mode_of_creation of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: str
        """
        return self._mode_of_creation

    @mode_of_creation.setter
    def mode_of_creation(self, mode_of_creation):
        """Sets the mode_of_creation of this UpdateKYCProfileByProfileId.

        Mode of profile creation (manual, import)  # noqa: E501

        :param mode_of_creation: The mode_of_creation of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: str
        """

        self._mode_of_creation = mode_of_creation

    @property
    def import_status(self):
        """Gets the import_status of this UpdateKYCProfileByProfileId.  # noqa: E501

        Status of profile creation (submitted, preprocessed, validated, queued, inProgress, processed, completed, partiallyCompleted, failed)  # noqa: E501

        :return: The import_status of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: str
        """
        return self._import_status

    @import_status.setter
    def import_status(self, import_status):
        """Sets the import_status of this UpdateKYCProfileByProfileId.

        Status of profile creation (submitted, preprocessed, validated, queued, inProgress, processed, completed, partiallyCompleted, failed)  # noqa: E501

        :param import_status: The import_status of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: str
        """

        self._import_status = import_status

    @property
    def is_locked(self):
        """Gets the is_locked of this UpdateKYCProfileByProfileId.  # noqa: E501

        Value indicating whether the profile is locked  # noqa: E501

        :return: The is_locked of this UpdateKYCProfileByProfileId.  # noqa: E501
        :rtype: bool
        """
        return self._is_locked

    @is_locked.setter
    def is_locked(self, is_locked):
        """Sets the is_locked of this UpdateKYCProfileByProfileId.

        Value indicating whether the profile is locked  # noqa: E501

        :param is_locked: The is_locked of this UpdateKYCProfileByProfileId.  # noqa: E501
        :type: bool
        """

        self._is_locked = is_locked

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
        if issubclass(UpdateKYCProfileByProfileId, dict):
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
        if not isinstance(other, UpdateKYCProfileByProfileId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

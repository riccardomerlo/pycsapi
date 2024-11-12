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

class GetKYCIndividualSearchResponseItems(object):
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
        'country_codes': 'list[str]',
        'threshold': 'float',
        'type': 'str',
        'datasets': 'list[str]',
        'status': 'str',
        'risk_rating': 'str',
        'assigned_to_user_id': 'float',
        'assigned_user': 'str',
        'created_by_id': 'float',
        'created_by': 'str',
        'created_at': 'str',
        'modified_by_id': 'float',
        'modified_by': 'str',
        'modified_at': 'str',
        'note': 'str',
        'schedule_id': 'str',
        'total_hit_count': 'float',
        'true_positive_hits_count': 'float',
        'false_positive_hits_count': 'float',
        'undecided_hits_count': 'float',
        'first_name': 'str',
        'middle_name': 'str',
        'last_name': 'str',
        'gender': 'str',
        'date_of_birth': 'str',
        'pep_tiers': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'country_codes': 'countryCodes',
        'threshold': 'threshold',
        'type': 'type',
        'datasets': 'datasets',
        'status': 'status',
        'risk_rating': 'riskRating',
        'assigned_to_user_id': 'assignedToUserId',
        'assigned_user': 'assignedUser',
        'created_by_id': 'createdById',
        'created_by': 'createdBy',
        'created_at': 'createdAt',
        'modified_by_id': 'modifiedById',
        'modified_by': 'modifiedBy',
        'modified_at': 'modifiedAt',
        'note': 'note',
        'schedule_id': 'scheduleId',
        'total_hit_count': 'totalHitCount',
        'true_positive_hits_count': 'truePositiveHitsCount',
        'false_positive_hits_count': 'falsePositiveHitsCount',
        'undecided_hits_count': 'undecidedHitsCount',
        'first_name': 'firstName',
        'middle_name': 'middleName',
        'last_name': 'lastName',
        'gender': 'gender',
        'date_of_birth': 'dateOfBirth',
        'pep_tiers': 'pepTiers'
    }

    def __init__(self, id=None, name=None, country_codes=None, threshold=None, type=None, datasets=None, status=None, risk_rating=None, assigned_to_user_id=None, assigned_user=None, created_by_id=None, created_by=None, created_at=None, modified_by_id=None, modified_by=None, modified_at=None, note=None, schedule_id=None, total_hit_count=None, true_positive_hits_count=None, false_positive_hits_count=None, undecided_hits_count=None, first_name=None, middle_name=None, last_name=None, gender=None, date_of_birth=None, pep_tiers=None):  # noqa: E501
        """GetKYCIndividualSearchResponseItems - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._country_codes = None
        self._threshold = None
        self._type = None
        self._datasets = None
        self._status = None
        self._risk_rating = None
        self._assigned_to_user_id = None
        self._assigned_user = None
        self._created_by_id = None
        self._created_by = None
        self._created_at = None
        self._modified_by_id = None
        self._modified_by = None
        self._modified_at = None
        self._note = None
        self._schedule_id = None
        self._total_hit_count = None
        self._true_positive_hits_count = None
        self._false_positive_hits_count = None
        self._undecided_hits_count = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._gender = None
        self._date_of_birth = None
        self._pep_tiers = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if country_codes is not None:
            self.country_codes = country_codes
        if threshold is not None:
            self.threshold = threshold
        if type is not None:
            self.type = type
        if datasets is not None:
            self.datasets = datasets
        if status is not None:
            self.status = status
        if risk_rating is not None:
            self.risk_rating = risk_rating
        if assigned_to_user_id is not None:
            self.assigned_to_user_id = assigned_to_user_id
        if assigned_user is not None:
            self.assigned_user = assigned_user
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if created_by is not None:
            self.created_by = created_by
        if created_at is not None:
            self.created_at = created_at
        if modified_by_id is not None:
            self.modified_by_id = modified_by_id
        if modified_by is not None:
            self.modified_by = modified_by
        if modified_at is not None:
            self.modified_at = modified_at
        if note is not None:
            self.note = note
        if schedule_id is not None:
            self.schedule_id = schedule_id
        if total_hit_count is not None:
            self.total_hit_count = total_hit_count
        if true_positive_hits_count is not None:
            self.true_positive_hits_count = true_positive_hits_count
        if false_positive_hits_count is not None:
            self.false_positive_hits_count = false_positive_hits_count
        if undecided_hits_count is not None:
            self.undecided_hits_count = undecided_hits_count
        if first_name is not None:
            self.first_name = first_name
        if middle_name is not None:
            self.middle_name = middle_name
        if last_name is not None:
            self.last_name = last_name
        if gender is not None:
            self.gender = gender
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if pep_tiers is not None:
            self.pep_tiers = pep_tiers

    @property
    def id(self):
        """Gets the id of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The id of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetKYCIndividualSearchResponseItems.


        :param id: The id of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The name of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetKYCIndividualSearchResponseItems.


        :param name: The name of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def country_codes(self):
        """Gets the country_codes of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The country_codes of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: list[str]
        """
        return self._country_codes

    @country_codes.setter
    def country_codes(self, country_codes):
        """Sets the country_codes of this GetKYCIndividualSearchResponseItems.


        :param country_codes: The country_codes of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: list[str]
        """

        self._country_codes = country_codes

    @property
    def threshold(self):
        """Gets the threshold of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The threshold of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: float
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        """Sets the threshold of this GetKYCIndividualSearchResponseItems.


        :param threshold: The threshold of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: float
        """

        self._threshold = threshold

    @property
    def type(self):
        """Gets the type of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The type of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GetKYCIndividualSearchResponseItems.


        :param type: The type of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["individual"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def datasets(self):
        """Gets the datasets of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The datasets of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: list[str]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this GetKYCIndividualSearchResponseItems.


        :param datasets: The datasets of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: list[str]
        """

        self._datasets = datasets

    @property
    def status(self):
        """Gets the status of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The status of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetKYCIndividualSearchResponseItems.


        :param status: The status of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["new"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def risk_rating(self):
        """Gets the risk_rating of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The risk_rating of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._risk_rating

    @risk_rating.setter
    def risk_rating(self, risk_rating):
        """Sets the risk_rating of this GetKYCIndividualSearchResponseItems.


        :param risk_rating: The risk_rating of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: str
        """
        allowed_values = ["notApplicable"]  # noqa: E501
        if risk_rating not in allowed_values:
            raise ValueError(
                "Invalid value for `risk_rating` ({0}), must be one of {1}"  # noqa: E501
                .format(risk_rating, allowed_values)
            )

        self._risk_rating = risk_rating

    @property
    def assigned_to_user_id(self):
        """Gets the assigned_to_user_id of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The assigned_to_user_id of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: float
        """
        return self._assigned_to_user_id

    @assigned_to_user_id.setter
    def assigned_to_user_id(self, assigned_to_user_id):
        """Sets the assigned_to_user_id of this GetKYCIndividualSearchResponseItems.


        :param assigned_to_user_id: The assigned_to_user_id of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: float
        """

        self._assigned_to_user_id = assigned_to_user_id

    @property
    def assigned_user(self):
        """Gets the assigned_user of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The assigned_user of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._assigned_user

    @assigned_user.setter
    def assigned_user(self, assigned_user):
        """Sets the assigned_user of this GetKYCIndividualSearchResponseItems.


        :param assigned_user: The assigned_user of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: str
        """

        self._assigned_user = assigned_user

    @property
    def created_by_id(self):
        """Gets the created_by_id of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The created_by_id of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: float
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this GetKYCIndividualSearchResponseItems.


        :param created_by_id: The created_by_id of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: float
        """

        self._created_by_id = created_by_id

    @property
    def created_by(self):
        """Gets the created_by of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The created_by of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this GetKYCIndividualSearchResponseItems.


        :param created_by: The created_by of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_at(self):
        """Gets the created_at of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The created_at of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GetKYCIndividualSearchResponseItems.


        :param created_at: The created_at of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def modified_by_id(self):
        """Gets the modified_by_id of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The modified_by_id of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: float
        """
        return self._modified_by_id

    @modified_by_id.setter
    def modified_by_id(self, modified_by_id):
        """Sets the modified_by_id of this GetKYCIndividualSearchResponseItems.


        :param modified_by_id: The modified_by_id of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: float
        """

        self._modified_by_id = modified_by_id

    @property
    def modified_by(self):
        """Gets the modified_by of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The modified_by of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this GetKYCIndividualSearchResponseItems.


        :param modified_by: The modified_by of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def modified_at(self):
        """Gets the modified_at of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The modified_at of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this GetKYCIndividualSearchResponseItems.


        :param modified_at: The modified_at of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: str
        """

        self._modified_at = modified_at

    @property
    def note(self):
        """Gets the note of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The note of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this GetKYCIndividualSearchResponseItems.


        :param note: The note of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def schedule_id(self):
        """Gets the schedule_id of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The schedule_id of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id):
        """Sets the schedule_id of this GetKYCIndividualSearchResponseItems.


        :param schedule_id: The schedule_id of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: str
        """

        self._schedule_id = schedule_id

    @property
    def total_hit_count(self):
        """Gets the total_hit_count of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The total_hit_count of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: float
        """
        return self._total_hit_count

    @total_hit_count.setter
    def total_hit_count(self, total_hit_count):
        """Sets the total_hit_count of this GetKYCIndividualSearchResponseItems.


        :param total_hit_count: The total_hit_count of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: float
        """

        self._total_hit_count = total_hit_count

    @property
    def true_positive_hits_count(self):
        """Gets the true_positive_hits_count of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The true_positive_hits_count of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: float
        """
        return self._true_positive_hits_count

    @true_positive_hits_count.setter
    def true_positive_hits_count(self, true_positive_hits_count):
        """Sets the true_positive_hits_count of this GetKYCIndividualSearchResponseItems.


        :param true_positive_hits_count: The true_positive_hits_count of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: float
        """

        self._true_positive_hits_count = true_positive_hits_count

    @property
    def false_positive_hits_count(self):
        """Gets the false_positive_hits_count of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The false_positive_hits_count of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: float
        """
        return self._false_positive_hits_count

    @false_positive_hits_count.setter
    def false_positive_hits_count(self, false_positive_hits_count):
        """Sets the false_positive_hits_count of this GetKYCIndividualSearchResponseItems.


        :param false_positive_hits_count: The false_positive_hits_count of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: float
        """

        self._false_positive_hits_count = false_positive_hits_count

    @property
    def undecided_hits_count(self):
        """Gets the undecided_hits_count of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The undecided_hits_count of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: float
        """
        return self._undecided_hits_count

    @undecided_hits_count.setter
    def undecided_hits_count(self, undecided_hits_count):
        """Sets the undecided_hits_count of this GetKYCIndividualSearchResponseItems.


        :param undecided_hits_count: The undecided_hits_count of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: float
        """

        self._undecided_hits_count = undecided_hits_count

    @property
    def first_name(self):
        """Gets the first_name of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The first_name of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this GetKYCIndividualSearchResponseItems.


        :param first_name: The first_name of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def middle_name(self):
        """Gets the middle_name of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The middle_name of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this GetKYCIndividualSearchResponseItems.


        :param middle_name: The middle_name of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: str
        """

        self._middle_name = middle_name

    @property
    def last_name(self):
        """Gets the last_name of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The last_name of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this GetKYCIndividualSearchResponseItems.


        :param last_name: The last_name of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def gender(self):
        """Gets the gender of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The gender of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this GetKYCIndividualSearchResponseItems.


        :param gender: The gender of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The date_of_birth of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this GetKYCIndividualSearchResponseItems.


        :param date_of_birth: The date_of_birth of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: str
        """

        self._date_of_birth = date_of_birth

    @property
    def pep_tiers(self):
        """Gets the pep_tiers of this GetKYCIndividualSearchResponseItems.  # noqa: E501


        :return: The pep_tiers of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :rtype: list[str]
        """
        return self._pep_tiers

    @pep_tiers.setter
    def pep_tiers(self, pep_tiers):
        """Sets the pep_tiers of this GetKYCIndividualSearchResponseItems.


        :param pep_tiers: The pep_tiers of this GetKYCIndividualSearchResponseItems.  # noqa: E501
        :type: list[str]
        """

        self._pep_tiers = pep_tiers

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
        if issubclass(GetKYCIndividualSearchResponseItems, dict):
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
        if not isinstance(other, GetKYCIndividualSearchResponseItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

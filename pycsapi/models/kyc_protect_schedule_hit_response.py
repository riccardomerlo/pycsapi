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

class KYCProtectScheduleHitResponse(object):
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
        'hit_score': 'int',
        'name': 'str',
        'match': 'str',
        'countries': 'list[str]',
        'datasets': 'list[str]',
        'decision': 'str',
        'note': 'str',
        'modified_by_id': 'int',
        'modified_by': 'str',
        'modified_at': 'datetime',
        'created_at': 'datetime',
        'first_name': 'str',
        'middle_name': 'str',
        'last_name': 'str',
        'gender': 'str',
        'dates_of_birth': 'list[date]',
        'pep_tier': 'str',
        'profile_images': 'list[str]',
        'superseded_hit': 'KYCProtectBaseIndividualSearchResultHitSummaryResponse',
        'search_id': 'str',
        'profile_id': 'str',
        'schedule_id': 'str',
        'key_party_id': 'str',
        'search_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'hit_score': 'hitScore',
        'name': 'name',
        'match': 'match',
        'countries': 'countries',
        'datasets': 'datasets',
        'decision': 'decision',
        'note': 'note',
        'modified_by_id': 'modifiedById',
        'modified_by': 'modifiedBy',
        'modified_at': 'modifiedAt',
        'created_at': 'createdAt',
        'first_name': 'firstName',
        'middle_name': 'middleName',
        'last_name': 'lastName',
        'gender': 'gender',
        'dates_of_birth': 'datesOfBirth',
        'pep_tier': 'pepTier',
        'profile_images': 'profileImages',
        'superseded_hit': 'supersededHit',
        'search_id': 'searchId',
        'profile_id': 'profileId',
        'schedule_id': 'scheduleId',
        'key_party_id': 'keyPartyId',
        'search_type': 'searchType'
    }

    def __init__(self, id=None, hit_score=None, name=None, match=None, countries=None, datasets=None, decision=None, note=None, modified_by_id=None, modified_by=None, modified_at=None, created_at=None, first_name=None, middle_name=None, last_name=None, gender=None, dates_of_birth=None, pep_tier=None, profile_images=None, superseded_hit=None, search_id=None, profile_id=None, schedule_id=None, key_party_id=None, search_type=None):  # noqa: E501
        """KYCProtectScheduleHitResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._hit_score = None
        self._name = None
        self._match = None
        self._countries = None
        self._datasets = None
        self._decision = None
        self._note = None
        self._modified_by_id = None
        self._modified_by = None
        self._modified_at = None
        self._created_at = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._gender = None
        self._dates_of_birth = None
        self._pep_tier = None
        self._profile_images = None
        self._superseded_hit = None
        self._search_id = None
        self._profile_id = None
        self._schedule_id = None
        self._key_party_id = None
        self._search_type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if hit_score is not None:
            self.hit_score = hit_score
        if name is not None:
            self.name = name
        if match is not None:
            self.match = match
        if countries is not None:
            self.countries = countries
        if datasets is not None:
            self.datasets = datasets
        if decision is not None:
            self.decision = decision
        if note is not None:
            self.note = note
        if modified_by_id is not None:
            self.modified_by_id = modified_by_id
        if modified_by is not None:
            self.modified_by = modified_by
        if modified_at is not None:
            self.modified_at = modified_at
        if created_at is not None:
            self.created_at = created_at
        if first_name is not None:
            self.first_name = first_name
        if middle_name is not None:
            self.middle_name = middle_name
        if last_name is not None:
            self.last_name = last_name
        if gender is not None:
            self.gender = gender
        if dates_of_birth is not None:
            self.dates_of_birth = dates_of_birth
        if pep_tier is not None:
            self.pep_tier = pep_tier
        if profile_images is not None:
            self.profile_images = profile_images
        if superseded_hit is not None:
            self.superseded_hit = superseded_hit
        if search_id is not None:
            self.search_id = search_id
        if profile_id is not None:
            self.profile_id = profile_id
        if schedule_id is not None:
            self.schedule_id = schedule_id
        if key_party_id is not None:
            self.key_party_id = key_party_id
        if search_type is not None:
            self.search_type = search_type

    @property
    def id(self):
        """Gets the id of this KYCProtectScheduleHitResponse.  # noqa: E501

        The Id of the search hit.  # noqa: E501

        :return: The id of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this KYCProtectScheduleHitResponse.

        The Id of the search hit.  # noqa: E501

        :param id: The id of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def hit_score(self):
        """Gets the hit_score of this KYCProtectScheduleHitResponse.  # noqa: E501

        The hit score associated to the search hit.  # noqa: E501

        :return: The hit_score of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: int
        """
        return self._hit_score

    @hit_score.setter
    def hit_score(self, hit_score):
        """Sets the hit_score of this KYCProtectScheduleHitResponse.

        The hit score associated to the search hit.  # noqa: E501

        :param hit_score: The hit_score of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: int
        """

        self._hit_score = hit_score

    @property
    def name(self):
        """Gets the name of this KYCProtectScheduleHitResponse.  # noqa: E501

        The name associated to the search hit.  # noqa: E501

        :return: The name of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KYCProtectScheduleHitResponse.

        The name associated to the search hit.  # noqa: E501

        :param name: The name of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def match(self):
        """Gets the match of this KYCProtectScheduleHitResponse.  # noqa: E501

        The match string associated to the search hit.  # noqa: E501

        :return: The match of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._match

    @match.setter
    def match(self, match):
        """Sets the match of this KYCProtectScheduleHitResponse.

        The match string associated to the search hit.  # noqa: E501

        :param match: The match of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: str
        """

        self._match = match

    @property
    def countries(self):
        """Gets the countries of this KYCProtectScheduleHitResponse.  # noqa: E501

        The countries associated to the search hit.  # noqa: E501

        :return: The countries of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """Sets the countries of this KYCProtectScheduleHitResponse.

        The countries associated to the search hit.  # noqa: E501

        :param countries: The countries of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: list[str]
        """

        self._countries = countries

    @property
    def datasets(self):
        """Gets the datasets of this KYCProtectScheduleHitResponse.  # noqa: E501

        The datasets associated to the search hit.  # noqa: E501

        :return: The datasets of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this KYCProtectScheduleHitResponse.

        The datasets associated to the search hit.  # noqa: E501

        :param datasets: The datasets of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: list[str]
        """

        self._datasets = datasets

    @property
    def decision(self):
        """Gets the decision of this KYCProtectScheduleHitResponse.  # noqa: E501

        The decision made on the search hit.  # noqa: E501

        :return: The decision of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._decision

    @decision.setter
    def decision(self, decision):
        """Sets the decision of this KYCProtectScheduleHitResponse.

        The decision made on the search hit.  # noqa: E501

        :param decision: The decision of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["undecided", "trueMatch", "falsePositive", "discarded"]  # noqa: E501
        if decision not in allowed_values:
            raise ValueError(
                "Invalid value for `decision` ({0}), must be one of {1}"  # noqa: E501
                .format(decision, allowed_values)
            )

        self._decision = decision

    @property
    def note(self):
        """Gets the note of this KYCProtectScheduleHitResponse.  # noqa: E501

        The note added to the search hit.  # noqa: E501

        :return: The note of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this KYCProtectScheduleHitResponse.

        The note added to the search hit.  # noqa: E501

        :param note: The note of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def modified_by_id(self):
        """Gets the modified_by_id of this KYCProtectScheduleHitResponse.  # noqa: E501

        The search hit last modified by user id.  # noqa: E501

        :return: The modified_by_id of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: int
        """
        return self._modified_by_id

    @modified_by_id.setter
    def modified_by_id(self, modified_by_id):
        """Sets the modified_by_id of this KYCProtectScheduleHitResponse.

        The search hit last modified by user id.  # noqa: E501

        :param modified_by_id: The modified_by_id of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: int
        """

        self._modified_by_id = modified_by_id

    @property
    def modified_by(self):
        """Gets the modified_by of this KYCProtectScheduleHitResponse.  # noqa: E501

        The search hit last modified by user name.  # noqa: E501

        :return: The modified_by of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this KYCProtectScheduleHitResponse.

        The search hit last modified by user name.  # noqa: E501

        :param modified_by: The modified_by of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def modified_at(self):
        """Gets the modified_at of this KYCProtectScheduleHitResponse.  # noqa: E501

        The search hit last modified date and time.  # noqa: E501

        :return: The modified_at of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this KYCProtectScheduleHitResponse.

        The search hit last modified date and time.  # noqa: E501

        :param modified_at: The modified_at of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def created_at(self):
        """Gets the created_at of this KYCProtectScheduleHitResponse.  # noqa: E501

        The search hit created date and time.  # noqa: E501

        :return: The created_at of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this KYCProtectScheduleHitResponse.

        The search hit created date and time.  # noqa: E501

        :param created_at: The created_at of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def first_name(self):
        """Gets the first_name of this KYCProtectScheduleHitResponse.  # noqa: E501

        The first name of the search hit.  # noqa: E501

        :return: The first_name of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this KYCProtectScheduleHitResponse.

        The first name of the search hit.  # noqa: E501

        :param first_name: The first_name of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def middle_name(self):
        """Gets the middle_name of this KYCProtectScheduleHitResponse.  # noqa: E501

        The middle name of the search hit.  # noqa: E501

        :return: The middle_name of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this KYCProtectScheduleHitResponse.

        The middle name of the search hit.  # noqa: E501

        :param middle_name: The middle_name of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: str
        """

        self._middle_name = middle_name

    @property
    def last_name(self):
        """Gets the last_name of this KYCProtectScheduleHitResponse.  # noqa: E501

        The last name of the search hit.  # noqa: E501

        :return: The last_name of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this KYCProtectScheduleHitResponse.

        The last name of the search hit.  # noqa: E501

        :param last_name: The last_name of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def gender(self):
        """Gets the gender of this KYCProtectScheduleHitResponse.  # noqa: E501

        The gender associated to the search hit.  # noqa: E501

        :return: The gender of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this KYCProtectScheduleHitResponse.

        The gender associated to the search hit.  # noqa: E501

        :param gender: The gender of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["male", "female"]  # noqa: E501
        if gender not in allowed_values:
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"  # noqa: E501
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def dates_of_birth(self):
        """Gets the dates_of_birth of this KYCProtectScheduleHitResponse.  # noqa: E501

        The dates of birth associated to the search hit.  # noqa: E501

        :return: The dates_of_birth of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: list[date]
        """
        return self._dates_of_birth

    @dates_of_birth.setter
    def dates_of_birth(self, dates_of_birth):
        """Sets the dates_of_birth of this KYCProtectScheduleHitResponse.

        The dates of birth associated to the search hit.  # noqa: E501

        :param dates_of_birth: The dates_of_birth of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: list[date]
        """

        self._dates_of_birth = dates_of_birth

    @property
    def pep_tier(self):
        """Gets the pep_tier of this KYCProtectScheduleHitResponse.  # noqa: E501

        The pep tier associated to the search hit.  # noqa: E501

        :return: The pep_tier of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._pep_tier

    @pep_tier.setter
    def pep_tier(self, pep_tier):
        """Sets the pep_tier of this KYCProtectScheduleHitResponse.

        The pep tier associated to the search hit.  # noqa: E501

        :param pep_tier: The pep_tier of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["pepTier1", "pepTier2", "pepTier3"]  # noqa: E501
        if pep_tier not in allowed_values:
            raise ValueError(
                "Invalid value for `pep_tier` ({0}), must be one of {1}"  # noqa: E501
                .format(pep_tier, allowed_values)
            )

        self._pep_tier = pep_tier

    @property
    def profile_images(self):
        """Gets the profile_images of this KYCProtectScheduleHitResponse.  # noqa: E501

        The profile images associated to the search hit.  # noqa: E501

        :return: The profile_images of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._profile_images

    @profile_images.setter
    def profile_images(self, profile_images):
        """Sets the profile_images of this KYCProtectScheduleHitResponse.

        The profile images associated to the search hit.  # noqa: E501

        :param profile_images: The profile_images of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: list[str]
        """

        self._profile_images = profile_images

    @property
    def superseded_hit(self):
        """Gets the superseded_hit of this KYCProtectScheduleHitResponse.  # noqa: E501


        :return: The superseded_hit of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: KYCProtectBaseIndividualSearchResultHitSummaryResponse
        """
        return self._superseded_hit

    @superseded_hit.setter
    def superseded_hit(self, superseded_hit):
        """Sets the superseded_hit of this KYCProtectScheduleHitResponse.


        :param superseded_hit: The superseded_hit of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: KYCProtectBaseIndividualSearchResultHitSummaryResponse
        """

        self._superseded_hit = superseded_hit

    @property
    def search_id(self):
        """Gets the search_id of this KYCProtectScheduleHitResponse.  # noqa: E501

        The id of the search that was being scheduled  # noqa: E501

        :return: The search_id of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._search_id

    @search_id.setter
    def search_id(self, search_id):
        """Sets the search_id of this KYCProtectScheduleHitResponse.

        The id of the search that was being scheduled  # noqa: E501

        :param search_id: The search_id of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: str
        """

        self._search_id = search_id

    @property
    def profile_id(self):
        """Gets the profile_id of this KYCProtectScheduleHitResponse.  # noqa: E501

        The id of the profile linked to the search that was being scheduled  # noqa: E501

        :return: The profile_id of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        """Sets the profile_id of this KYCProtectScheduleHitResponse.

        The id of the profile linked to the search that was being scheduled  # noqa: E501

        :param profile_id: The profile_id of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: str
        """

        self._profile_id = profile_id

    @property
    def schedule_id(self):
        """Gets the schedule_id of this KYCProtectScheduleHitResponse.  # noqa: E501

        The id of the schedule  # noqa: E501

        :return: The schedule_id of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._schedule_id

    @schedule_id.setter
    def schedule_id(self, schedule_id):
        """Sets the schedule_id of this KYCProtectScheduleHitResponse.

        The id of the schedule  # noqa: E501

        :param schedule_id: The schedule_id of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: str
        """

        self._schedule_id = schedule_id

    @property
    def key_party_id(self):
        """Gets the key_party_id of this KYCProtectScheduleHitResponse.  # noqa: E501

        The id of the key party linked to the search that was being scheduled  # noqa: E501

        :return: The key_party_id of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._key_party_id

    @key_party_id.setter
    def key_party_id(self, key_party_id):
        """Sets the key_party_id of this KYCProtectScheduleHitResponse.

        The id of the key party linked to the search that was being scheduled  # noqa: E501

        :param key_party_id: The key_party_id of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: str
        """

        self._key_party_id = key_party_id

    @property
    def search_type(self):
        """Gets the search_type of this KYCProtectScheduleHitResponse.  # noqa: E501

        The type of the search that was being scheduled  # noqa: E501

        :return: The search_type of this KYCProtectScheduleHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        """Sets the search_type of this KYCProtectScheduleHitResponse.

        The type of the search that was being scheduled  # noqa: E501

        :param search_type: The search_type of this KYCProtectScheduleHitResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["individual", "business"]  # noqa: E501
        if search_type not in allowed_values:
            raise ValueError(
                "Invalid value for `search_type` ({0}), must be one of {1}"  # noqa: E501
                .format(search_type, allowed_values)
            )

        self._search_type = search_type

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
        if issubclass(KYCProtectScheduleHitResponse, dict):
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
        if not isinstance(other, KYCProtectScheduleHitResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

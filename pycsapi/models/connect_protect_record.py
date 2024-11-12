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

class ConnectProtectRecord(object):
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
        'id': 'int',
        'match_type': 'str',
        'result_id': 'int',
        'entity_id': 'str',
        'match_score': 'int',
        'source_date': 'datetime',
        'date_listed': 'str',
        'name': 'str',
        'full_name': 'str',
        'first_name': 'str',
        'middle_name': 'str',
        'last_name': 'str',
        'reason_listed': 'str',
        'entity_type': 'str',
        'date_of_birth': 'str',
        'generation': 'str',
        'gender': 'str',
        'occupation': 'str',
        'place_of_birth': 'str',
        'has_adverse_media': 'bool',
        'other_names': 'list[str]',
        'addresses': 'list[ConnectProtectAddress]',
        'comments': 'list[str]',
        'sources': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'match_type': 'matchType',
        'result_id': 'resultId',
        'entity_id': 'entityId',
        'match_score': 'matchScore',
        'source_date': 'sourceDate',
        'date_listed': 'dateListed',
        'name': 'name',
        'full_name': 'fullName',
        'first_name': 'firstName',
        'middle_name': 'middleName',
        'last_name': 'lastName',
        'reason_listed': 'reasonListed',
        'entity_type': 'entityType',
        'date_of_birth': 'dateOfBirth',
        'generation': 'generation',
        'gender': 'gender',
        'occupation': 'occupation',
        'place_of_birth': 'placeOfBirth',
        'has_adverse_media': 'hasAdverseMedia',
        'other_names': 'otherNames',
        'addresses': 'addresses',
        'comments': 'comments',
        'sources': 'sources'
    }

    def __init__(self, id=None, match_type=None, result_id=None, entity_id=None, match_score=None, source_date=None, date_listed=None, name=None, full_name=None, first_name=None, middle_name=None, last_name=None, reason_listed=None, entity_type=None, date_of_birth=None, generation=None, gender=None, occupation=None, place_of_birth=None, has_adverse_media=None, other_names=None, addresses=None, comments=None, sources=None):  # noqa: E501
        """ConnectProtectRecord - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._match_type = None
        self._result_id = None
        self._entity_id = None
        self._match_score = None
        self._source_date = None
        self._date_listed = None
        self._name = None
        self._full_name = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._reason_listed = None
        self._entity_type = None
        self._date_of_birth = None
        self._generation = None
        self._gender = None
        self._occupation = None
        self._place_of_birth = None
        self._has_adverse_media = None
        self._other_names = None
        self._addresses = None
        self._comments = None
        self._sources = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if match_type is not None:
            self.match_type = match_type
        if result_id is not None:
            self.result_id = result_id
        if entity_id is not None:
            self.entity_id = entity_id
        if match_score is not None:
            self.match_score = match_score
        if source_date is not None:
            self.source_date = source_date
        if date_listed is not None:
            self.date_listed = date_listed
        if name is not None:
            self.name = name
        if full_name is not None:
            self.full_name = full_name
        if first_name is not None:
            self.first_name = first_name
        if middle_name is not None:
            self.middle_name = middle_name
        if last_name is not None:
            self.last_name = last_name
        if reason_listed is not None:
            self.reason_listed = reason_listed
        if entity_type is not None:
            self.entity_type = entity_type
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if generation is not None:
            self.generation = generation
        if gender is not None:
            self.gender = gender
        if occupation is not None:
            self.occupation = occupation
        if place_of_birth is not None:
            self.place_of_birth = place_of_birth
        if has_adverse_media is not None:
            self.has_adverse_media = has_adverse_media
        if other_names is not None:
            self.other_names = other_names
        if addresses is not None:
            self.addresses = addresses
        if comments is not None:
            self.comments = comments
        if sources is not None:
            self.sources = sources

    @property
    def id(self):
        """Gets the id of this ConnectProtectRecord.  # noqa: E501

         Unique ID number relating to the World Compliance report. It is also known as the InvestigationRecord.  # noqa: E501

        :return: The id of this ConnectProtectRecord.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConnectProtectRecord.

         Unique ID number relating to the World Compliance report. It is also known as the InvestigationRecord.  # noqa: E501

        :param id: The id of this ConnectProtectRecord.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def match_type(self):
        """Gets the match_type of this ConnectProtectRecord.  # noqa: E501


        :return: The match_type of this ConnectProtectRecord.  # noqa: E501
        :rtype: str
        """
        return self._match_type

    @match_type.setter
    def match_type(self, match_type):
        """Sets the match_type of this ConnectProtectRecord.


        :param match_type: The match_type of this ConnectProtectRecord.  # noqa: E501
        :type: str
        """

        self._match_type = match_type

    @property
    def result_id(self):
        """Gets the result_id of this ConnectProtectRecord.  # noqa: E501


        :return: The result_id of this ConnectProtectRecord.  # noqa: E501
        :rtype: int
        """
        return self._result_id

    @result_id.setter
    def result_id(self, result_id):
        """Sets the result_id of this ConnectProtectRecord.


        :param result_id: The result_id of this ConnectProtectRecord.  # noqa: E501
        :type: int
        """

        self._result_id = result_id

    @property
    def entity_id(self):
        """Gets the entity_id of this ConnectProtectRecord.  # noqa: E501


        :return: The entity_id of this ConnectProtectRecord.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this ConnectProtectRecord.


        :param entity_id: The entity_id of this ConnectProtectRecord.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def match_score(self):
        """Gets the match_score of this ConnectProtectRecord.  # noqa: E501

        A percentage based score depicting how accurate the search parameters relate to the report name.  # noqa: E501

        :return: The match_score of this ConnectProtectRecord.  # noqa: E501
        :rtype: int
        """
        return self._match_score

    @match_score.setter
    def match_score(self, match_score):
        """Sets the match_score of this ConnectProtectRecord.

        A percentage based score depicting how accurate the search parameters relate to the report name.  # noqa: E501

        :param match_score: The match_score of this ConnectProtectRecord.  # noqa: E501
        :type: int
        """

        self._match_score = match_score

    @property
    def source_date(self):
        """Gets the source_date of this ConnectProtectRecord.  # noqa: E501

        This is the date the report was last updated.  # noqa: E501

        :return: The source_date of this ConnectProtectRecord.  # noqa: E501
        :rtype: datetime
        """
        return self._source_date

    @source_date.setter
    def source_date(self, source_date):
        """Sets the source_date of this ConnectProtectRecord.

        This is the date the report was last updated.  # noqa: E501

        :param source_date: The source_date of this ConnectProtectRecord.  # noqa: E501
        :type: datetime
        """

        self._source_date = source_date

    @property
    def date_listed(self):
        """Gets the date_listed of this ConnectProtectRecord.  # noqa: E501

        T​he date the report was originally created.  # noqa: E501

        :return: The date_listed of this ConnectProtectRecord.  # noqa: E501
        :rtype: str
        """
        return self._date_listed

    @date_listed.setter
    def date_listed(self, date_listed):
        """Sets the date_listed of this ConnectProtectRecord.

        T​he date the report was originally created.  # noqa: E501

        :param date_listed: The date_listed of this ConnectProtectRecord.  # noqa: E501
        :type: str
        """

        self._date_listed = date_listed

    @property
    def name(self):
        """Gets the name of this ConnectProtectRecord.  # noqa: E501


        :return: The name of this ConnectProtectRecord.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectProtectRecord.


        :param name: The name of this ConnectProtectRecord.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def full_name(self):
        """Gets the full_name of this ConnectProtectRecord.  # noqa: E501


        :return: The full_name of this ConnectProtectRecord.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this ConnectProtectRecord.


        :param full_name: The full_name of this ConnectProtectRecord.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def first_name(self):
        """Gets the first_name of this ConnectProtectRecord.  # noqa: E501


        :return: The first_name of this ConnectProtectRecord.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this ConnectProtectRecord.


        :param first_name: The first_name of this ConnectProtectRecord.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def middle_name(self):
        """Gets the middle_name of this ConnectProtectRecord.  # noqa: E501


        :return: The middle_name of this ConnectProtectRecord.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this ConnectProtectRecord.


        :param middle_name: The middle_name of this ConnectProtectRecord.  # noqa: E501
        :type: str
        """

        self._middle_name = middle_name

    @property
    def last_name(self):
        """Gets the last_name of this ConnectProtectRecord.  # noqa: E501


        :return: The last_name of this ConnectProtectRecord.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this ConnectProtectRecord.


        :param last_name: The last_name of this ConnectProtectRecord.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def reason_listed(self):
        """Gets the reason_listed of this ConnectProtectRecord.  # noqa: E501


        :return: The reason_listed of this ConnectProtectRecord.  # noqa: E501
        :rtype: str
        """
        return self._reason_listed

    @reason_listed.setter
    def reason_listed(self, reason_listed):
        """Sets the reason_listed of this ConnectProtectRecord.


        :param reason_listed: The reason_listed of this ConnectProtectRecord.  # noqa: E501
        :type: str
        """

        self._reason_listed = reason_listed

    @property
    def entity_type(self):
        """Gets the entity_type of this ConnectProtectRecord.  # noqa: E501

        Business or Individual.  # noqa: E501

        :return: The entity_type of this ConnectProtectRecord.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this ConnectProtectRecord.

        Business or Individual.  # noqa: E501

        :param entity_type: The entity_type of this ConnectProtectRecord.  # noqa: E501
        :type: str
        """

        self._entity_type = entity_type

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this ConnectProtectRecord.  # noqa: E501


        :return: The date_of_birth of this ConnectProtectRecord.  # noqa: E501
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this ConnectProtectRecord.


        :param date_of_birth: The date_of_birth of this ConnectProtectRecord.  # noqa: E501
        :type: str
        """

        self._date_of_birth = date_of_birth

    @property
    def generation(self):
        """Gets the generation of this ConnectProtectRecord.  # noqa: E501


        :return: The generation of this ConnectProtectRecord.  # noqa: E501
        :rtype: str
        """
        return self._generation

    @generation.setter
    def generation(self, generation):
        """Sets the generation of this ConnectProtectRecord.


        :param generation: The generation of this ConnectProtectRecord.  # noqa: E501
        :type: str
        """

        self._generation = generation

    @property
    def gender(self):
        """Gets the gender of this ConnectProtectRecord.  # noqa: E501


        :return: The gender of this ConnectProtectRecord.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this ConnectProtectRecord.


        :param gender: The gender of this ConnectProtectRecord.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def occupation(self):
        """Gets the occupation of this ConnectProtectRecord.  # noqa: E501


        :return: The occupation of this ConnectProtectRecord.  # noqa: E501
        :rtype: str
        """
        return self._occupation

    @occupation.setter
    def occupation(self, occupation):
        """Sets the occupation of this ConnectProtectRecord.


        :param occupation: The occupation of this ConnectProtectRecord.  # noqa: E501
        :type: str
        """

        self._occupation = occupation

    @property
    def place_of_birth(self):
        """Gets the place_of_birth of this ConnectProtectRecord.  # noqa: E501


        :return: The place_of_birth of this ConnectProtectRecord.  # noqa: E501
        :rtype: str
        """
        return self._place_of_birth

    @place_of_birth.setter
    def place_of_birth(self, place_of_birth):
        """Sets the place_of_birth of this ConnectProtectRecord.


        :param place_of_birth: The place_of_birth of this ConnectProtectRecord.  # noqa: E501
        :type: str
        """

        self._place_of_birth = place_of_birth

    @property
    def has_adverse_media(self):
        """Gets the has_adverse_media of this ConnectProtectRecord.  # noqa: E501


        :return: The has_adverse_media of this ConnectProtectRecord.  # noqa: E501
        :rtype: bool
        """
        return self._has_adverse_media

    @has_adverse_media.setter
    def has_adverse_media(self, has_adverse_media):
        """Sets the has_adverse_media of this ConnectProtectRecord.


        :param has_adverse_media: The has_adverse_media of this ConnectProtectRecord.  # noqa: E501
        :type: bool
        """

        self._has_adverse_media = has_adverse_media

    @property
    def other_names(self):
        """Gets the other_names of this ConnectProtectRecord.  # noqa: E501


        :return: The other_names of this ConnectProtectRecord.  # noqa: E501
        :rtype: list[str]
        """
        return self._other_names

    @other_names.setter
    def other_names(self, other_names):
        """Sets the other_names of this ConnectProtectRecord.


        :param other_names: The other_names of this ConnectProtectRecord.  # noqa: E501
        :type: list[str]
        """

        self._other_names = other_names

    @property
    def addresses(self):
        """Gets the addresses of this ConnectProtectRecord.  # noqa: E501


        :return: The addresses of this ConnectProtectRecord.  # noqa: E501
        :rtype: list[ConnectProtectAddress]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this ConnectProtectRecord.


        :param addresses: The addresses of this ConnectProtectRecord.  # noqa: E501
        :type: list[ConnectProtectAddress]
        """

        self._addresses = addresses

    @property
    def comments(self):
        """Gets the comments of this ConnectProtectRecord.  # noqa: E501


        :return: The comments of this ConnectProtectRecord.  # noqa: E501
        :rtype: list[str]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this ConnectProtectRecord.


        :param comments: The comments of this ConnectProtectRecord.  # noqa: E501
        :type: list[str]
        """

        self._comments = comments

    @property
    def sources(self):
        """Gets the sources of this ConnectProtectRecord.  # noqa: E501


        :return: The sources of this ConnectProtectRecord.  # noqa: E501
        :rtype: list[str]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this ConnectProtectRecord.


        :param sources: The sources of this ConnectProtectRecord.  # noqa: E501
        :type: list[str]
        """

        self._sources = sources

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
        if issubclass(ConnectProtectRecord, dict):
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
        if not isinstance(other, ConnectProtectRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

class IndividualSearchResultHitResponse(object):
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
        'note': 'str',
        'countries': 'list[str]',
        'datasets': 'list[str]',
        'profile_images': 'list[str]',
        'screening_notes': 'list[str]',
        'modified_at': 'datetime',
        'modified_by_id': 'int',
        'modified_by': 'str',
        'created_at': 'datetime',
        'decision': 'str',
        'identifiers': 'list[SearchResultHitsIdentifierResponse]',
        'addresses': 'list[SearchResultHitsAddressResponse]',
        'contacts': 'list[SearchResultHitsContactResponse]',
        'business_links': 'list[SearchResultHitsBusinessLinkResponse]',
        'individual_links': 'list[SearchResultHitsIndividualLinkResponse]',
        'sources': 'list[SearchResultHitsSourceResponse]',
        'first_name': 'str',
        'middle_name': 'str',
        'last_name': 'str',
        'gender': 'str',
        'dates_of_birth': 'list[date]',
        'is_deceased': 'bool',
        'dates_of_death': 'list[date]',
        'pep_tier': 'str',
        'aliases': 'list[SearchResultHitsIndividualAliasResponse]',
        'aml_results': 'IndividualSearchResultHitResponseAmlResults'
    }

    attribute_map = {
        'id': 'id',
        'hit_score': 'hitScore',
        'name': 'name',
        'match': 'match',
        'note': 'note',
        'countries': 'countries',
        'datasets': 'datasets',
        'profile_images': 'profileImages',
        'screening_notes': 'screeningNotes',
        'modified_at': 'modifiedAt',
        'modified_by_id': 'modifiedById',
        'modified_by': 'modifiedBy',
        'created_at': 'createdAt',
        'decision': 'decision',
        'identifiers': 'identifiers',
        'addresses': 'addresses',
        'contacts': 'contacts',
        'business_links': 'businessLinks',
        'individual_links': 'individualLinks',
        'sources': 'sources',
        'first_name': 'firstName',
        'middle_name': 'middleName',
        'last_name': 'lastName',
        'gender': 'gender',
        'dates_of_birth': 'datesOfBirth',
        'is_deceased': 'isDeceased',
        'dates_of_death': 'datesOfDeath',
        'pep_tier': 'pepTier',
        'aliases': 'aliases',
        'aml_results': 'amlResults'
    }

    def __init__(self, id=None, hit_score=None, name=None, match=None, note=None, countries=None, datasets=None, profile_images=None, screening_notes=None, modified_at=None, modified_by_id=None, modified_by=None, created_at=None, decision=None, identifiers=None, addresses=None, contacts=None, business_links=None, individual_links=None, sources=None, first_name=None, middle_name=None, last_name=None, gender=None, dates_of_birth=None, is_deceased=None, dates_of_death=None, pep_tier=None, aliases=None, aml_results=None):  # noqa: E501
        """IndividualSearchResultHitResponse - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._hit_score = None
        self._name = None
        self._match = None
        self._note = None
        self._countries = None
        self._datasets = None
        self._profile_images = None
        self._screening_notes = None
        self._modified_at = None
        self._modified_by_id = None
        self._modified_by = None
        self._created_at = None
        self._decision = None
        self._identifiers = None
        self._addresses = None
        self._contacts = None
        self._business_links = None
        self._individual_links = None
        self._sources = None
        self._first_name = None
        self._middle_name = None
        self._last_name = None
        self._gender = None
        self._dates_of_birth = None
        self._is_deceased = None
        self._dates_of_death = None
        self._pep_tier = None
        self._aliases = None
        self._aml_results = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if hit_score is not None:
            self.hit_score = hit_score
        if name is not None:
            self.name = name
        if match is not None:
            self.match = match
        if note is not None:
            self.note = note
        if countries is not None:
            self.countries = countries
        if datasets is not None:
            self.datasets = datasets
        if profile_images is not None:
            self.profile_images = profile_images
        if screening_notes is not None:
            self.screening_notes = screening_notes
        if modified_at is not None:
            self.modified_at = modified_at
        if modified_by_id is not None:
            self.modified_by_id = modified_by_id
        if modified_by is not None:
            self.modified_by = modified_by
        if created_at is not None:
            self.created_at = created_at
        if decision is not None:
            self.decision = decision
        if identifiers is not None:
            self.identifiers = identifiers
        if addresses is not None:
            self.addresses = addresses
        if contacts is not None:
            self.contacts = contacts
        if business_links is not None:
            self.business_links = business_links
        if individual_links is not None:
            self.individual_links = individual_links
        if sources is not None:
            self.sources = sources
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
        if is_deceased is not None:
            self.is_deceased = is_deceased
        if dates_of_death is not None:
            self.dates_of_death = dates_of_death
        if pep_tier is not None:
            self.pep_tier = pep_tier
        if aliases is not None:
            self.aliases = aliases
        if aml_results is not None:
            self.aml_results = aml_results

    @property
    def id(self):
        """Gets the id of this IndividualSearchResultHitResponse.  # noqa: E501

        The Id of the search hit  # noqa: E501

        :return: The id of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IndividualSearchResultHitResponse.

        The Id of the search hit  # noqa: E501

        :param id: The id of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def hit_score(self):
        """Gets the hit_score of this IndividualSearchResultHitResponse.  # noqa: E501

        The hit score associated to the search hit.  # noqa: E501

        :return: The hit_score of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: int
        """
        return self._hit_score

    @hit_score.setter
    def hit_score(self, hit_score):
        """Sets the hit_score of this IndividualSearchResultHitResponse.

        The hit score associated to the search hit.  # noqa: E501

        :param hit_score: The hit_score of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: int
        """

        self._hit_score = hit_score

    @property
    def name(self):
        """Gets the name of this IndividualSearchResultHitResponse.  # noqa: E501

        The name associated to the search hit.  # noqa: E501

        :return: The name of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this IndividualSearchResultHitResponse.

        The name associated to the search hit.  # noqa: E501

        :param name: The name of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def match(self):
        """Gets the match of this IndividualSearchResultHitResponse.  # noqa: E501

        The match string associated to the search hit.  # noqa: E501

        :return: The match of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._match

    @match.setter
    def match(self, match):
        """Sets the match of this IndividualSearchResultHitResponse.

        The match string associated to the search hit.  # noqa: E501

        :param match: The match of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: str
        """

        self._match = match

    @property
    def note(self):
        """Gets the note of this IndividualSearchResultHitResponse.  # noqa: E501

        The note added to the search hit.  # noqa: E501

        :return: The note of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this IndividualSearchResultHitResponse.

        The note added to the search hit.  # noqa: E501

        :param note: The note of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def countries(self):
        """Gets the countries of this IndividualSearchResultHitResponse.  # noqa: E501

        The countries associated to the search hit.  # noqa: E501

        :return: The countries of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """Sets the countries of this IndividualSearchResultHitResponse.

        The countries associated to the search hit.  # noqa: E501

        :param countries: The countries of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: list[str]
        """

        self._countries = countries

    @property
    def datasets(self):
        """Gets the datasets of this IndividualSearchResultHitResponse.  # noqa: E501

        The datasets associated to the search hit.  # noqa: E501

        :return: The datasets of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this IndividualSearchResultHitResponse.

        The datasets associated to the search hit.  # noqa: E501

        :param datasets: The datasets of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: list[str]
        """

        self._datasets = datasets

    @property
    def profile_images(self):
        """Gets the profile_images of this IndividualSearchResultHitResponse.  # noqa: E501

        The profile images associated to the search hit.  # noqa: E501

        :return: The profile_images of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._profile_images

    @profile_images.setter
    def profile_images(self, profile_images):
        """Sets the profile_images of this IndividualSearchResultHitResponse.

        The profile images associated to the search hit.  # noqa: E501

        :param profile_images: The profile_images of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: list[str]
        """

        self._profile_images = profile_images

    @property
    def screening_notes(self):
        """Gets the screening_notes of this IndividualSearchResultHitResponse.  # noqa: E501

        The screening notes associated to the search hit.  # noqa: E501

        :return: The screening_notes of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._screening_notes

    @screening_notes.setter
    def screening_notes(self, screening_notes):
        """Sets the screening_notes of this IndividualSearchResultHitResponse.

        The screening notes associated to the search hit.  # noqa: E501

        :param screening_notes: The screening_notes of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: list[str]
        """

        self._screening_notes = screening_notes

    @property
    def modified_at(self):
        """Gets the modified_at of this IndividualSearchResultHitResponse.  # noqa: E501

        The search hit modified date and time.  # noqa: E501

        :return: The modified_at of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this IndividualSearchResultHitResponse.

        The search hit modified date and time.  # noqa: E501

        :param modified_at: The modified_at of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def modified_by_id(self):
        """Gets the modified_by_id of this IndividualSearchResultHitResponse.  # noqa: E501

        The search hit modified by user id.  # noqa: E501

        :return: The modified_by_id of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: int
        """
        return self._modified_by_id

    @modified_by_id.setter
    def modified_by_id(self, modified_by_id):
        """Sets the modified_by_id of this IndividualSearchResultHitResponse.

        The search hit modified by user id.  # noqa: E501

        :param modified_by_id: The modified_by_id of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: int
        """

        self._modified_by_id = modified_by_id

    @property
    def modified_by(self):
        """Gets the modified_by of this IndividualSearchResultHitResponse.  # noqa: E501

        The search hit modified by user name.  # noqa: E501

        :return: The modified_by of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this IndividualSearchResultHitResponse.

        The search hit modified by user name.  # noqa: E501

        :param modified_by: The modified_by of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def created_at(self):
        """Gets the created_at of this IndividualSearchResultHitResponse.  # noqa: E501

        The search hit created date and time.  # noqa: E501

        :return: The created_at of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this IndividualSearchResultHitResponse.

        The search hit created date and time.  # noqa: E501

        :param created_at: The created_at of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def decision(self):
        """Gets the decision of this IndividualSearchResultHitResponse.  # noqa: E501

        The decision made on the search hit.  # noqa: E501

        :return: The decision of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._decision

    @decision.setter
    def decision(self, decision):
        """Sets the decision of this IndividualSearchResultHitResponse.

        The decision made on the search hit.  # noqa: E501

        :param decision: The decision of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["undecided", "trueMatch", "falsePositive"]  # noqa: E501
        if decision not in allowed_values:
            raise ValueError(
                "Invalid value for `decision` ({0}), must be one of {1}"  # noqa: E501
                .format(decision, allowed_values)
            )

        self._decision = decision

    @property
    def identifiers(self):
        """Gets the identifiers of this IndividualSearchResultHitResponse.  # noqa: E501

        The identifiers associated to the search hit.  # noqa: E501

        :return: The identifiers of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: list[SearchResultHitsIdentifierResponse]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this IndividualSearchResultHitResponse.

        The identifiers associated to the search hit.  # noqa: E501

        :param identifiers: The identifiers of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: list[SearchResultHitsIdentifierResponse]
        """

        self._identifiers = identifiers

    @property
    def addresses(self):
        """Gets the addresses of this IndividualSearchResultHitResponse.  # noqa: E501

        The addresses associated to the search hit.  # noqa: E501

        :return: The addresses of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: list[SearchResultHitsAddressResponse]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this IndividualSearchResultHitResponse.

        The addresses associated to the search hit.  # noqa: E501

        :param addresses: The addresses of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: list[SearchResultHitsAddressResponse]
        """

        self._addresses = addresses

    @property
    def contacts(self):
        """Gets the contacts of this IndividualSearchResultHitResponse.  # noqa: E501

        The contact details associated to the search hit.  # noqa: E501

        :return: The contacts of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: list[SearchResultHitsContactResponse]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this IndividualSearchResultHitResponse.

        The contact details associated to the search hit.  # noqa: E501

        :param contacts: The contacts of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: list[SearchResultHitsContactResponse]
        """

        self._contacts = contacts

    @property
    def business_links(self):
        """Gets the business_links of this IndividualSearchResultHitResponse.  # noqa: E501

        The business links associated to the search hit.  # noqa: E501

        :return: The business_links of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: list[SearchResultHitsBusinessLinkResponse]
        """
        return self._business_links

    @business_links.setter
    def business_links(self, business_links):
        """Sets the business_links of this IndividualSearchResultHitResponse.

        The business links associated to the search hit.  # noqa: E501

        :param business_links: The business_links of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: list[SearchResultHitsBusinessLinkResponse]
        """

        self._business_links = business_links

    @property
    def individual_links(self):
        """Gets the individual_links of this IndividualSearchResultHitResponse.  # noqa: E501

        The individual links associated to the search hit.  # noqa: E501

        :return: The individual_links of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: list[SearchResultHitsIndividualLinkResponse]
        """
        return self._individual_links

    @individual_links.setter
    def individual_links(self, individual_links):
        """Sets the individual_links of this IndividualSearchResultHitResponse.

        The individual links associated to the search hit.  # noqa: E501

        :param individual_links: The individual_links of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: list[SearchResultHitsIndividualLinkResponse]
        """

        self._individual_links = individual_links

    @property
    def sources(self):
        """Gets the sources of this IndividualSearchResultHitResponse.  # noqa: E501

        The sources associated to the search hit.  # noqa: E501

        :return: The sources of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: list[SearchResultHitsSourceResponse]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this IndividualSearchResultHitResponse.

        The sources associated to the search hit.  # noqa: E501

        :param sources: The sources of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: list[SearchResultHitsSourceResponse]
        """

        self._sources = sources

    @property
    def first_name(self):
        """Gets the first_name of this IndividualSearchResultHitResponse.  # noqa: E501

        The first name of the individual search hit.  # noqa: E501

        :return: The first_name of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this IndividualSearchResultHitResponse.

        The first name of the individual search hit.  # noqa: E501

        :param first_name: The first_name of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def middle_name(self):
        """Gets the middle_name of this IndividualSearchResultHitResponse.  # noqa: E501

        The middle name of the individual search hit.  # noqa: E501

        :return: The middle_name of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._middle_name

    @middle_name.setter
    def middle_name(self, middle_name):
        """Sets the middle_name of this IndividualSearchResultHitResponse.

        The middle name of the individual search hit.  # noqa: E501

        :param middle_name: The middle_name of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: str
        """

        self._middle_name = middle_name

    @property
    def last_name(self):
        """Gets the last_name of this IndividualSearchResultHitResponse.  # noqa: E501

        The last name of the individual search hit.  # noqa: E501

        :return: The last_name of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this IndividualSearchResultHitResponse.

        The last name of the individual search hit.  # noqa: E501

        :param last_name: The last_name of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def gender(self):
        """Gets the gender of this IndividualSearchResultHitResponse.  # noqa: E501

        The gender associated with the search hit.  # noqa: E501

        :return: The gender of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this IndividualSearchResultHitResponse.

        The gender associated with the search hit.  # noqa: E501

        :param gender: The gender of this IndividualSearchResultHitResponse.  # noqa: E501
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
        """Gets the dates_of_birth of this IndividualSearchResultHitResponse.  # noqa: E501

        The dates of birth associated to the search hit.  # noqa: E501

        :return: The dates_of_birth of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: list[date]
        """
        return self._dates_of_birth

    @dates_of_birth.setter
    def dates_of_birth(self, dates_of_birth):
        """Sets the dates_of_birth of this IndividualSearchResultHitResponse.

        The dates of birth associated to the search hit.  # noqa: E501

        :param dates_of_birth: The dates_of_birth of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: list[date]
        """

        self._dates_of_birth = dates_of_birth

    @property
    def is_deceased(self):
        """Gets the is_deceased of this IndividualSearchResultHitResponse.  # noqa: E501

        The deceased status of the individual associated to the search hit  # noqa: E501

        :return: The is_deceased of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_deceased

    @is_deceased.setter
    def is_deceased(self, is_deceased):
        """Sets the is_deceased of this IndividualSearchResultHitResponse.

        The deceased status of the individual associated to the search hit  # noqa: E501

        :param is_deceased: The is_deceased of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: bool
        """

        self._is_deceased = is_deceased

    @property
    def dates_of_death(self):
        """Gets the dates_of_death of this IndividualSearchResultHitResponse.  # noqa: E501

        The dates of death associated to the search hit.  # noqa: E501

        :return: The dates_of_death of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: list[date]
        """
        return self._dates_of_death

    @dates_of_death.setter
    def dates_of_death(self, dates_of_death):
        """Sets the dates_of_death of this IndividualSearchResultHitResponse.

        The dates of death associated to the search hit.  # noqa: E501

        :param dates_of_death: The dates_of_death of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: list[date]
        """

        self._dates_of_death = dates_of_death

    @property
    def pep_tier(self):
        """Gets the pep_tier of this IndividualSearchResultHitResponse.  # noqa: E501

        The pep tier associated to the search hit.  # noqa: E501

        :return: The pep_tier of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._pep_tier

    @pep_tier.setter
    def pep_tier(self, pep_tier):
        """Sets the pep_tier of this IndividualSearchResultHitResponse.

        The pep tier associated to the search hit.  # noqa: E501

        :param pep_tier: The pep_tier of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["tier1", "tier2", "tier3"]  # noqa: E501
        if pep_tier not in allowed_values:
            raise ValueError(
                "Invalid value for `pep_tier` ({0}), must be one of {1}"  # noqa: E501
                .format(pep_tier, allowed_values)
            )

        self._pep_tier = pep_tier

    @property
    def aliases(self):
        """Gets the aliases of this IndividualSearchResultHitResponse.  # noqa: E501

        The aliases associated to the search hit.  # noqa: E501

        :return: The aliases of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: list[SearchResultHitsIndividualAliasResponse]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this IndividualSearchResultHitResponse.

        The aliases associated to the search hit.  # noqa: E501

        :param aliases: The aliases of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: list[SearchResultHitsIndividualAliasResponse]
        """

        self._aliases = aliases

    @property
    def aml_results(self):
        """Gets the aml_results of this IndividualSearchResultHitResponse.  # noqa: E501


        :return: The aml_results of this IndividualSearchResultHitResponse.  # noqa: E501
        :rtype: IndividualSearchResultHitResponseAmlResults
        """
        return self._aml_results

    @aml_results.setter
    def aml_results(self, aml_results):
        """Sets the aml_results of this IndividualSearchResultHitResponse.


        :param aml_results: The aml_results of this IndividualSearchResultHitResponse.  # noqa: E501
        :type: IndividualSearchResultHitResponseAmlResults
        """

        self._aml_results = aml_results

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
        if issubclass(IndividualSearchResultHitResponse, dict):
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
        if not isinstance(other, IndividualSearchResultHitResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

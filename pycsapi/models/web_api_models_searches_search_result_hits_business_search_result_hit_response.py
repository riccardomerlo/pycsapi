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

class WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse(object):
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
        'identifiers': 'list[WebApiModelsSearchesSearchResultHitsHitIdentifierResponse]',
        'addresses': 'list[WebApiModelsSearchesSearchResultHitsHitAddressResponse]',
        'contacts': 'list[WebApiModelsSearchesSearchResultHitsHitContactResponse]',
        'business_links': 'list[WebApiModelsSearchesSearchResultHitsHitBusinessLinkResponse]',
        'individual_links': 'list[WebApiModelsSearchesSearchResultHitsHitIndividualLinkResponse]',
        'sources': 'list[WebApiModelsSearchesSearchResultHitsHitSourceResponse]',
        'activities': 'list[str]',
        'aliases': 'list[WebApiModelsSearchesSearchResultHitsHitBusinessAliasResponse]',
        'aml_results': 'WebApiModelsSearchesSearchResultHitsBusinessHitAmlResultsResponse',
        'description': 'str',
        'business_types': 'list[str]'
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
        'activities': 'activities',
        'aliases': 'aliases',
        'aml_results': 'amlResults',
        'description': 'description',
        'business_types': 'businessTypes'
    }

    def __init__(self, id=None, hit_score=None, name=None, match=None, note=None, countries=None, datasets=None, profile_images=None, screening_notes=None, modified_at=None, modified_by_id=None, modified_by=None, created_at=None, decision=None, identifiers=None, addresses=None, contacts=None, business_links=None, individual_links=None, sources=None, activities=None, aliases=None, aml_results=None, description=None, business_types=None):  # noqa: E501
        """WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse - a model defined in Swagger"""  # noqa: E501
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
        self._activities = None
        self._aliases = None
        self._aml_results = None
        self._description = None
        self._business_types = None
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
        if activities is not None:
            self.activities = activities
        if aliases is not None:
            self.aliases = aliases
        if aml_results is not None:
            self.aml_results = aml_results
        if description is not None:
            self.description = description
        if business_types is not None:
            self.business_types = business_types

    @property
    def id(self):
        """Gets the id of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The Id of the search hit  # noqa: E501

        :return: The id of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The Id of the search hit  # noqa: E501

        :param id: The id of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def hit_score(self):
        """Gets the hit_score of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The hit score associated to the search hit  # noqa: E501

        :return: The hit_score of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: int
        """
        return self._hit_score

    @hit_score.setter
    def hit_score(self, hit_score):
        """Sets the hit_score of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The hit score associated to the search hit  # noqa: E501

        :param hit_score: The hit_score of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: int
        """

        self._hit_score = hit_score

    @property
    def name(self):
        """Gets the name of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The name associated to the search hit  # noqa: E501

        :return: The name of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The name associated to the search hit  # noqa: E501

        :param name: The name of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def match(self):
        """Gets the match of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The match string associated to the search hit  # noqa: E501

        :return: The match of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._match

    @match.setter
    def match(self, match):
        """Sets the match of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The match string associated to the search hit  # noqa: E501

        :param match: The match of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: str
        """

        self._match = match

    @property
    def note(self):
        """Gets the note of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The note added to the search hit  # noqa: E501

        :return: The note of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The note added to the search hit  # noqa: E501

        :param note: The note of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def countries(self):
        """Gets the countries of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The countries associated to the search hit  # noqa: E501

        :return: The countries of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """Sets the countries of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The countries associated to the search hit  # noqa: E501

        :param countries: The countries of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: list[str]
        """

        self._countries = countries

    @property
    def datasets(self):
        """Gets the datasets of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The datasets associated to the search hit  # noqa: E501

        :return: The datasets of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The datasets associated to the search hit  # noqa: E501

        :param datasets: The datasets of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: list[str]
        """

        self._datasets = datasets

    @property
    def profile_images(self):
        """Gets the profile_images of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The profile images associated to the search hit  # noqa: E501

        :return: The profile_images of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._profile_images

    @profile_images.setter
    def profile_images(self, profile_images):
        """Sets the profile_images of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The profile images associated to the search hit  # noqa: E501

        :param profile_images: The profile_images of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: list[str]
        """

        self._profile_images = profile_images

    @property
    def screening_notes(self):
        """Gets the screening_notes of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The screening notes associated to the search hit  # noqa: E501

        :return: The screening_notes of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._screening_notes

    @screening_notes.setter
    def screening_notes(self, screening_notes):
        """Sets the screening_notes of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The screening notes associated to the search hit  # noqa: E501

        :param screening_notes: The screening_notes of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: list[str]
        """

        self._screening_notes = screening_notes

    @property
    def modified_at(self):
        """Gets the modified_at of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The search hit modified date and time  # noqa: E501

        :return: The modified_at of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The search hit modified date and time  # noqa: E501

        :param modified_at: The modified_at of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def modified_by_id(self):
        """Gets the modified_by_id of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The search hit modified by user id  # noqa: E501

        :return: The modified_by_id of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: int
        """
        return self._modified_by_id

    @modified_by_id.setter
    def modified_by_id(self, modified_by_id):
        """Sets the modified_by_id of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The search hit modified by user id  # noqa: E501

        :param modified_by_id: The modified_by_id of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: int
        """

        self._modified_by_id = modified_by_id

    @property
    def modified_by(self):
        """Gets the modified_by of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The search hit modified by user name  # noqa: E501

        :return: The modified_by of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The search hit modified by user name  # noqa: E501

        :param modified_by: The modified_by of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def created_at(self):
        """Gets the created_at of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The search hit created date and time  # noqa: E501

        :return: The created_at of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The search hit created date and time  # noqa: E501

        :param created_at: The created_at of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def decision(self):
        """Gets the decision of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The decision made on the search hit Avaialable values are undecided, trueMatch, falsePositive, discarded  # noqa: E501

        :return: The decision of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._decision

    @decision.setter
    def decision(self, decision):
        """Sets the decision of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The decision made on the search hit Avaialable values are undecided, trueMatch, falsePositive, discarded  # noqa: E501

        :param decision: The decision of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: str
        """

        self._decision = decision

    @property
    def identifiers(self):
        """Gets the identifiers of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The identifiers associated to the search hit  # noqa: E501

        :return: The identifiers of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: list[WebApiModelsSearchesSearchResultHitsHitIdentifierResponse]
        """
        return self._identifiers

    @identifiers.setter
    def identifiers(self, identifiers):
        """Sets the identifiers of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The identifiers associated to the search hit  # noqa: E501

        :param identifiers: The identifiers of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: list[WebApiModelsSearchesSearchResultHitsHitIdentifierResponse]
        """

        self._identifiers = identifiers

    @property
    def addresses(self):
        """Gets the addresses of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The addresses associated to the search hit  # noqa: E501

        :return: The addresses of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: list[WebApiModelsSearchesSearchResultHitsHitAddressResponse]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The addresses associated to the search hit  # noqa: E501

        :param addresses: The addresses of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: list[WebApiModelsSearchesSearchResultHitsHitAddressResponse]
        """

        self._addresses = addresses

    @property
    def contacts(self):
        """Gets the contacts of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The contact details associated to the search hit  # noqa: E501

        :return: The contacts of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: list[WebApiModelsSearchesSearchResultHitsHitContactResponse]
        """
        return self._contacts

    @contacts.setter
    def contacts(self, contacts):
        """Sets the contacts of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The contact details associated to the search hit  # noqa: E501

        :param contacts: The contacts of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: list[WebApiModelsSearchesSearchResultHitsHitContactResponse]
        """

        self._contacts = contacts

    @property
    def business_links(self):
        """Gets the business_links of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The business links associated to the search hit  # noqa: E501

        :return: The business_links of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: list[WebApiModelsSearchesSearchResultHitsHitBusinessLinkResponse]
        """
        return self._business_links

    @business_links.setter
    def business_links(self, business_links):
        """Sets the business_links of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The business links associated to the search hit  # noqa: E501

        :param business_links: The business_links of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: list[WebApiModelsSearchesSearchResultHitsHitBusinessLinkResponse]
        """

        self._business_links = business_links

    @property
    def individual_links(self):
        """Gets the individual_links of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The individual links associated to the search hit  # noqa: E501

        :return: The individual_links of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: list[WebApiModelsSearchesSearchResultHitsHitIndividualLinkResponse]
        """
        return self._individual_links

    @individual_links.setter
    def individual_links(self, individual_links):
        """Sets the individual_links of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The individual links associated to the search hit  # noqa: E501

        :param individual_links: The individual_links of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: list[WebApiModelsSearchesSearchResultHitsHitIndividualLinkResponse]
        """

        self._individual_links = individual_links

    @property
    def sources(self):
        """Gets the sources of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The sources associated to the search hit  # noqa: E501

        :return: The sources of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: list[WebApiModelsSearchesSearchResultHitsHitSourceResponse]
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The sources associated to the search hit  # noqa: E501

        :param sources: The sources of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: list[WebApiModelsSearchesSearchResultHitsHitSourceResponse]
        """

        self._sources = sources

    @property
    def activities(self):
        """Gets the activities of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The activities associated to the search hit  # noqa: E501

        :return: The activities of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._activities

    @activities.setter
    def activities(self, activities):
        """Sets the activities of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The activities associated to the search hit  # noqa: E501

        :param activities: The activities of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: list[str]
        """

        self._activities = activities

    @property
    def aliases(self):
        """Gets the aliases of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The aliases associated to the search hit  # noqa: E501

        :return: The aliases of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: list[WebApiModelsSearchesSearchResultHitsHitBusinessAliasResponse]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The aliases associated to the search hit  # noqa: E501

        :param aliases: The aliases of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: list[WebApiModelsSearchesSearchResultHitsHitBusinessAliasResponse]
        """

        self._aliases = aliases

    @property
    def aml_results(self):
        """Gets the aml_results of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501


        :return: The aml_results of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: WebApiModelsSearchesSearchResultHitsBusinessHitAmlResultsResponse
        """
        return self._aml_results

    @aml_results.setter
    def aml_results(self, aml_results):
        """Sets the aml_results of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.


        :param aml_results: The aml_results of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: WebApiModelsSearchesSearchResultHitsBusinessHitAmlResultsResponse
        """

        self._aml_results = aml_results

    @property
    def description(self):
        """Gets the description of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The description associated to the search hit  # noqa: E501

        :return: The description of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The description associated to the search hit  # noqa: E501

        :param description: The description of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def business_types(self):
        """Gets the business_types of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501

        The business types associated to the search hit  # noqa: E501

        :return: The business_types of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._business_types

    @business_types.setter
    def business_types(self, business_types):
        """Sets the business_types of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.

        The business types associated to the search hit  # noqa: E501

        :param business_types: The business_types of this WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.  # noqa: E501
        :type: list[str]
        """

        self._business_types = business_types

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
        if issubclass(WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse, dict):
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
        if not isinstance(other, WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

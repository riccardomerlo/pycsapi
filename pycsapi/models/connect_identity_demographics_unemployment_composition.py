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

class ConnectIdentityDemographicsUnemploymentComposition(object):
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
        'male_long_term_unemployment': 'str',
        'male_long_term_unemployment_description': 'str',
        'male_long_term_unemployment_label': 'str',
        'unemployment_among18to24_year_olds': 'str',
        'unemployment_among18to24_year_olds_description': 'str',
        'unemployment_among18to24_year_olds_label': 'str',
        'unemployment_among25to39_year_olds': 'str',
        'unemployment_among25to39_year_olds_description': 'str',
        'unemployment_among25to39_year_olds_label': 'str',
        'unemployment_among_those_aged40and_older': 'str',
        'unemployment_among_those_aged40and_older_description': 'str',
        'unemployment_among_those_aged40and_older_label': 'str',
        'unemployment_score_label': 'str',
        'unemployment_score_description': 'str',
        'unemployment_score': 'str',
        'male_long_term_unemployment_score': 'str'
    }

    attribute_map = {
        'male_long_term_unemployment': 'maleLongTermUnemployment',
        'male_long_term_unemployment_description': 'maleLongTermUnemploymentDescription',
        'male_long_term_unemployment_label': 'maleLongTermUnemploymentLabel',
        'unemployment_among18to24_year_olds': 'unemploymentAmong18to24YearOlds',
        'unemployment_among18to24_year_olds_description': 'unemploymentAmong18to24YearOldsDescription',
        'unemployment_among18to24_year_olds_label': 'unemploymentAmong18to24YearOldsLabel',
        'unemployment_among25to39_year_olds': 'unemploymentAmong25to39YearOlds',
        'unemployment_among25to39_year_olds_description': 'unemploymentAmong25to39YearOldsDescription',
        'unemployment_among25to39_year_olds_label': 'unemploymentAmong25to39YearOldsLabel',
        'unemployment_among_those_aged40and_older': 'unemploymentAmongThoseAged40andOlder',
        'unemployment_among_those_aged40and_older_description': 'unemploymentAmongThoseAged40andOlderDescription',
        'unemployment_among_those_aged40and_older_label': 'unemploymentAmongThoseAged40andOlderLabel',
        'unemployment_score_label': 'unemploymentScoreLabel',
        'unemployment_score_description': 'unemploymentScoreDescription',
        'unemployment_score': 'unemploymentScore',
        'male_long_term_unemployment_score': 'maleLongTermUnemploymentScore'
    }

    def __init__(self, male_long_term_unemployment=None, male_long_term_unemployment_description=None, male_long_term_unemployment_label=None, unemployment_among18to24_year_olds=None, unemployment_among18to24_year_olds_description=None, unemployment_among18to24_year_olds_label=None, unemployment_among25to39_year_olds=None, unemployment_among25to39_year_olds_description=None, unemployment_among25to39_year_olds_label=None, unemployment_among_those_aged40and_older=None, unemployment_among_those_aged40and_older_description=None, unemployment_among_those_aged40and_older_label=None, unemployment_score_label=None, unemployment_score_description=None, unemployment_score=None, male_long_term_unemployment_score=None):  # noqa: E501
        """ConnectIdentityDemographicsUnemploymentComposition - a model defined in Swagger"""  # noqa: E501
        self._male_long_term_unemployment = None
        self._male_long_term_unemployment_description = None
        self._male_long_term_unemployment_label = None
        self._unemployment_among18to24_year_olds = None
        self._unemployment_among18to24_year_olds_description = None
        self._unemployment_among18to24_year_olds_label = None
        self._unemployment_among25to39_year_olds = None
        self._unemployment_among25to39_year_olds_description = None
        self._unemployment_among25to39_year_olds_label = None
        self._unemployment_among_those_aged40and_older = None
        self._unemployment_among_those_aged40and_older_description = None
        self._unemployment_among_those_aged40and_older_label = None
        self._unemployment_score_label = None
        self._unemployment_score_description = None
        self._unemployment_score = None
        self._male_long_term_unemployment_score = None
        self.discriminator = None
        if male_long_term_unemployment is not None:
            self.male_long_term_unemployment = male_long_term_unemployment
        if male_long_term_unemployment_description is not None:
            self.male_long_term_unemployment_description = male_long_term_unemployment_description
        if male_long_term_unemployment_label is not None:
            self.male_long_term_unemployment_label = male_long_term_unemployment_label
        if unemployment_among18to24_year_olds is not None:
            self.unemployment_among18to24_year_olds = unemployment_among18to24_year_olds
        if unemployment_among18to24_year_olds_description is not None:
            self.unemployment_among18to24_year_olds_description = unemployment_among18to24_year_olds_description
        if unemployment_among18to24_year_olds_label is not None:
            self.unemployment_among18to24_year_olds_label = unemployment_among18to24_year_olds_label
        if unemployment_among25to39_year_olds is not None:
            self.unemployment_among25to39_year_olds = unemployment_among25to39_year_olds
        if unemployment_among25to39_year_olds_description is not None:
            self.unemployment_among25to39_year_olds_description = unemployment_among25to39_year_olds_description
        if unemployment_among25to39_year_olds_label is not None:
            self.unemployment_among25to39_year_olds_label = unemployment_among25to39_year_olds_label
        if unemployment_among_those_aged40and_older is not None:
            self.unemployment_among_those_aged40and_older = unemployment_among_those_aged40and_older
        if unemployment_among_those_aged40and_older_description is not None:
            self.unemployment_among_those_aged40and_older_description = unemployment_among_those_aged40and_older_description
        if unemployment_among_those_aged40and_older_label is not None:
            self.unemployment_among_those_aged40and_older_label = unemployment_among_those_aged40and_older_label
        if unemployment_score_label is not None:
            self.unemployment_score_label = unemployment_score_label
        if unemployment_score_description is not None:
            self.unemployment_score_description = unemployment_score_description
        if unemployment_score is not None:
            self.unemployment_score = unemployment_score
        if male_long_term_unemployment_score is not None:
            self.male_long_term_unemployment_score = male_long_term_unemployment_score

    @property
    def male_long_term_unemployment(self):
        """Gets the male_long_term_unemployment of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501


        :return: The male_long_term_unemployment of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :rtype: str
        """
        return self._male_long_term_unemployment

    @male_long_term_unemployment.setter
    def male_long_term_unemployment(self, male_long_term_unemployment):
        """Sets the male_long_term_unemployment of this ConnectIdentityDemographicsUnemploymentComposition.


        :param male_long_term_unemployment: The male_long_term_unemployment of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :type: str
        """

        self._male_long_term_unemployment = male_long_term_unemployment

    @property
    def male_long_term_unemployment_description(self):
        """Gets the male_long_term_unemployment_description of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501


        :return: The male_long_term_unemployment_description of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :rtype: str
        """
        return self._male_long_term_unemployment_description

    @male_long_term_unemployment_description.setter
    def male_long_term_unemployment_description(self, male_long_term_unemployment_description):
        """Sets the male_long_term_unemployment_description of this ConnectIdentityDemographicsUnemploymentComposition.


        :param male_long_term_unemployment_description: The male_long_term_unemployment_description of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :type: str
        """

        self._male_long_term_unemployment_description = male_long_term_unemployment_description

    @property
    def male_long_term_unemployment_label(self):
        """Gets the male_long_term_unemployment_label of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501


        :return: The male_long_term_unemployment_label of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :rtype: str
        """
        return self._male_long_term_unemployment_label

    @male_long_term_unemployment_label.setter
    def male_long_term_unemployment_label(self, male_long_term_unemployment_label):
        """Sets the male_long_term_unemployment_label of this ConnectIdentityDemographicsUnemploymentComposition.


        :param male_long_term_unemployment_label: The male_long_term_unemployment_label of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :type: str
        """

        self._male_long_term_unemployment_label = male_long_term_unemployment_label

    @property
    def unemployment_among18to24_year_olds(self):
        """Gets the unemployment_among18to24_year_olds of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501


        :return: The unemployment_among18to24_year_olds of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :rtype: str
        """
        return self._unemployment_among18to24_year_olds

    @unemployment_among18to24_year_olds.setter
    def unemployment_among18to24_year_olds(self, unemployment_among18to24_year_olds):
        """Sets the unemployment_among18to24_year_olds of this ConnectIdentityDemographicsUnemploymentComposition.


        :param unemployment_among18to24_year_olds: The unemployment_among18to24_year_olds of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :type: str
        """

        self._unemployment_among18to24_year_olds = unemployment_among18to24_year_olds

    @property
    def unemployment_among18to24_year_olds_description(self):
        """Gets the unemployment_among18to24_year_olds_description of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501


        :return: The unemployment_among18to24_year_olds_description of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :rtype: str
        """
        return self._unemployment_among18to24_year_olds_description

    @unemployment_among18to24_year_olds_description.setter
    def unemployment_among18to24_year_olds_description(self, unemployment_among18to24_year_olds_description):
        """Sets the unemployment_among18to24_year_olds_description of this ConnectIdentityDemographicsUnemploymentComposition.


        :param unemployment_among18to24_year_olds_description: The unemployment_among18to24_year_olds_description of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :type: str
        """

        self._unemployment_among18to24_year_olds_description = unemployment_among18to24_year_olds_description

    @property
    def unemployment_among18to24_year_olds_label(self):
        """Gets the unemployment_among18to24_year_olds_label of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501


        :return: The unemployment_among18to24_year_olds_label of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :rtype: str
        """
        return self._unemployment_among18to24_year_olds_label

    @unemployment_among18to24_year_olds_label.setter
    def unemployment_among18to24_year_olds_label(self, unemployment_among18to24_year_olds_label):
        """Sets the unemployment_among18to24_year_olds_label of this ConnectIdentityDemographicsUnemploymentComposition.


        :param unemployment_among18to24_year_olds_label: The unemployment_among18to24_year_olds_label of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :type: str
        """

        self._unemployment_among18to24_year_olds_label = unemployment_among18to24_year_olds_label

    @property
    def unemployment_among25to39_year_olds(self):
        """Gets the unemployment_among25to39_year_olds of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501


        :return: The unemployment_among25to39_year_olds of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :rtype: str
        """
        return self._unemployment_among25to39_year_olds

    @unemployment_among25to39_year_olds.setter
    def unemployment_among25to39_year_olds(self, unemployment_among25to39_year_olds):
        """Sets the unemployment_among25to39_year_olds of this ConnectIdentityDemographicsUnemploymentComposition.


        :param unemployment_among25to39_year_olds: The unemployment_among25to39_year_olds of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :type: str
        """

        self._unemployment_among25to39_year_olds = unemployment_among25to39_year_olds

    @property
    def unemployment_among25to39_year_olds_description(self):
        """Gets the unemployment_among25to39_year_olds_description of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501


        :return: The unemployment_among25to39_year_olds_description of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :rtype: str
        """
        return self._unemployment_among25to39_year_olds_description

    @unemployment_among25to39_year_olds_description.setter
    def unemployment_among25to39_year_olds_description(self, unemployment_among25to39_year_olds_description):
        """Sets the unemployment_among25to39_year_olds_description of this ConnectIdentityDemographicsUnemploymentComposition.


        :param unemployment_among25to39_year_olds_description: The unemployment_among25to39_year_olds_description of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :type: str
        """

        self._unemployment_among25to39_year_olds_description = unemployment_among25to39_year_olds_description

    @property
    def unemployment_among25to39_year_olds_label(self):
        """Gets the unemployment_among25to39_year_olds_label of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501


        :return: The unemployment_among25to39_year_olds_label of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :rtype: str
        """
        return self._unemployment_among25to39_year_olds_label

    @unemployment_among25to39_year_olds_label.setter
    def unemployment_among25to39_year_olds_label(self, unemployment_among25to39_year_olds_label):
        """Sets the unemployment_among25to39_year_olds_label of this ConnectIdentityDemographicsUnemploymentComposition.


        :param unemployment_among25to39_year_olds_label: The unemployment_among25to39_year_olds_label of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :type: str
        """

        self._unemployment_among25to39_year_olds_label = unemployment_among25to39_year_olds_label

    @property
    def unemployment_among_those_aged40and_older(self):
        """Gets the unemployment_among_those_aged40and_older of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501


        :return: The unemployment_among_those_aged40and_older of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :rtype: str
        """
        return self._unemployment_among_those_aged40and_older

    @unemployment_among_those_aged40and_older.setter
    def unemployment_among_those_aged40and_older(self, unemployment_among_those_aged40and_older):
        """Sets the unemployment_among_those_aged40and_older of this ConnectIdentityDemographicsUnemploymentComposition.


        :param unemployment_among_those_aged40and_older: The unemployment_among_those_aged40and_older of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :type: str
        """

        self._unemployment_among_those_aged40and_older = unemployment_among_those_aged40and_older

    @property
    def unemployment_among_those_aged40and_older_description(self):
        """Gets the unemployment_among_those_aged40and_older_description of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501


        :return: The unemployment_among_those_aged40and_older_description of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :rtype: str
        """
        return self._unemployment_among_those_aged40and_older_description

    @unemployment_among_those_aged40and_older_description.setter
    def unemployment_among_those_aged40and_older_description(self, unemployment_among_those_aged40and_older_description):
        """Sets the unemployment_among_those_aged40and_older_description of this ConnectIdentityDemographicsUnemploymentComposition.


        :param unemployment_among_those_aged40and_older_description: The unemployment_among_those_aged40and_older_description of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :type: str
        """

        self._unemployment_among_those_aged40and_older_description = unemployment_among_those_aged40and_older_description

    @property
    def unemployment_among_those_aged40and_older_label(self):
        """Gets the unemployment_among_those_aged40and_older_label of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501


        :return: The unemployment_among_those_aged40and_older_label of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :rtype: str
        """
        return self._unemployment_among_those_aged40and_older_label

    @unemployment_among_those_aged40and_older_label.setter
    def unemployment_among_those_aged40and_older_label(self, unemployment_among_those_aged40and_older_label):
        """Sets the unemployment_among_those_aged40and_older_label of this ConnectIdentityDemographicsUnemploymentComposition.


        :param unemployment_among_those_aged40and_older_label: The unemployment_among_those_aged40and_older_label of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :type: str
        """

        self._unemployment_among_those_aged40and_older_label = unemployment_among_those_aged40and_older_label

    @property
    def unemployment_score_label(self):
        """Gets the unemployment_score_label of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501


        :return: The unemployment_score_label of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :rtype: str
        """
        return self._unemployment_score_label

    @unemployment_score_label.setter
    def unemployment_score_label(self, unemployment_score_label):
        """Sets the unemployment_score_label of this ConnectIdentityDemographicsUnemploymentComposition.


        :param unemployment_score_label: The unemployment_score_label of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :type: str
        """

        self._unemployment_score_label = unemployment_score_label

    @property
    def unemployment_score_description(self):
        """Gets the unemployment_score_description of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501


        :return: The unemployment_score_description of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :rtype: str
        """
        return self._unemployment_score_description

    @unemployment_score_description.setter
    def unemployment_score_description(self, unemployment_score_description):
        """Sets the unemployment_score_description of this ConnectIdentityDemographicsUnemploymentComposition.


        :param unemployment_score_description: The unemployment_score_description of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :type: str
        """

        self._unemployment_score_description = unemployment_score_description

    @property
    def unemployment_score(self):
        """Gets the unemployment_score of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501


        :return: The unemployment_score of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :rtype: str
        """
        return self._unemployment_score

    @unemployment_score.setter
    def unemployment_score(self, unemployment_score):
        """Sets the unemployment_score of this ConnectIdentityDemographicsUnemploymentComposition.


        :param unemployment_score: The unemployment_score of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :type: str
        """

        self._unemployment_score = unemployment_score

    @property
    def male_long_term_unemployment_score(self):
        """Gets the male_long_term_unemployment_score of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501


        :return: The male_long_term_unemployment_score of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :rtype: str
        """
        return self._male_long_term_unemployment_score

    @male_long_term_unemployment_score.setter
    def male_long_term_unemployment_score(self, male_long_term_unemployment_score):
        """Sets the male_long_term_unemployment_score of this ConnectIdentityDemographicsUnemploymentComposition.


        :param male_long_term_unemployment_score: The male_long_term_unemployment_score of this ConnectIdentityDemographicsUnemploymentComposition.  # noqa: E501
        :type: str
        """

        self._male_long_term_unemployment_score = male_long_term_unemployment_score

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
        if issubclass(ConnectIdentityDemographicsUnemploymentComposition, dict):
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
        if not isinstance(other, ConnectIdentityDemographicsUnemploymentComposition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

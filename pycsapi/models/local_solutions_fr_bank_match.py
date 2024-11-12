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

class LocalSolutionsFRBankMatch(object):
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
        'domain': 'str',
        'created_by': 'str',
        'created_date': 'datetime',
        'last_modified_by': 'str',
        'last_modified_date': 'datetime',
        'id': 'str',
        'score': 'int',
        'classification': 'str',
        'status': 'str',
        'entity': 'LocalSolutionsFRBankMatchEntity',
        'issuer_company': 'LocalSolutionsFRBankMatchIssuerCompany',
        'input': 'LocalSolutionsFRBankMatchInput',
        'with_deferred_result': 'bool',
        'by_api': 'bool',
        'by_ftp': 'bool',
        'workflow': 'str',
        'reasons': 'list[str]',
        'reason_labels': 'dict(str, str)'
    }

    attribute_map = {
        'domain': '@domain',
        'created_by': 'createdBy',
        'created_date': 'createdDate',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_date': 'lastModifiedDate',
        'id': 'id',
        'score': 'score',
        'classification': 'classification',
        'status': 'status',
        'entity': 'entity',
        'issuer_company': 'issuerCompany',
        'input': 'input',
        'with_deferred_result': 'withDeferredResult',
        'by_api': 'byAPI',
        'by_ftp': 'byFTP',
        'workflow': 'workflow',
        'reasons': 'reasons',
        'reason_labels': 'reasonLabels'
    }

    def __init__(self, domain=None, created_by=None, created_date=None, last_modified_by=None, last_modified_date=None, id=None, score=None, classification=None, status=None, entity=None, issuer_company=None, input=None, with_deferred_result=None, by_api=None, by_ftp=None, workflow=None, reasons=None, reason_labels=None):  # noqa: E501
        """LocalSolutionsFRBankMatch - a model defined in Swagger"""  # noqa: E501
        self._domain = None
        self._created_by = None
        self._created_date = None
        self._last_modified_by = None
        self._last_modified_date = None
        self._id = None
        self._score = None
        self._classification = None
        self._status = None
        self._entity = None
        self._issuer_company = None
        self._input = None
        self._with_deferred_result = None
        self._by_api = None
        self._by_ftp = None
        self._workflow = None
        self._reasons = None
        self._reason_labels = None
        self.discriminator = None
        if domain is not None:
            self.domain = domain
        if created_by is not None:
            self.created_by = created_by
        if created_date is not None:
            self.created_date = created_date
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if last_modified_date is not None:
            self.last_modified_date = last_modified_date
        if id is not None:
            self.id = id
        if score is not None:
            self.score = score
        if classification is not None:
            self.classification = classification
        if status is not None:
            self.status = status
        if entity is not None:
            self.entity = entity
        if issuer_company is not None:
            self.issuer_company = issuer_company
        if input is not None:
            self.input = input
        if with_deferred_result is not None:
            self.with_deferred_result = with_deferred_result
        if by_api is not None:
            self.by_api = by_api
        if by_ftp is not None:
            self.by_ftp = by_ftp
        if workflow is not None:
            self.workflow = workflow
        if reasons is not None:
            self.reasons = reasons
        if reason_labels is not None:
            self.reason_labels = reason_labels

    @property
    def domain(self):
        """Gets the domain of this LocalSolutionsFRBankMatch.  # noqa: E501

        The domain associated with the match.  # noqa: E501

        :return: The domain of this LocalSolutionsFRBankMatch.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this LocalSolutionsFRBankMatch.

        The domain associated with the match.  # noqa: E501

        :param domain: The domain of this LocalSolutionsFRBankMatch.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def created_by(self):
        """Gets the created_by of this LocalSolutionsFRBankMatch.  # noqa: E501

        The user or system that created the match record.  # noqa: E501

        :return: The created_by of this LocalSolutionsFRBankMatch.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this LocalSolutionsFRBankMatch.

        The user or system that created the match record.  # noqa: E501

        :param created_by: The created_by of this LocalSolutionsFRBankMatch.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_date(self):
        """Gets the created_date of this LocalSolutionsFRBankMatch.  # noqa: E501

        The date and time when the match record was created.  # noqa: E501

        :return: The created_date of this LocalSolutionsFRBankMatch.  # noqa: E501
        :rtype: datetime
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this LocalSolutionsFRBankMatch.

        The date and time when the match record was created.  # noqa: E501

        :param created_date: The created_date of this LocalSolutionsFRBankMatch.  # noqa: E501
        :type: datetime
        """

        self._created_date = created_date

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this LocalSolutionsFRBankMatch.  # noqa: E501

        The user or system that last modified the match record.  # noqa: E501

        :return: The last_modified_by of this LocalSolutionsFRBankMatch.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this LocalSolutionsFRBankMatch.

        The user or system that last modified the match record.  # noqa: E501

        :param last_modified_by: The last_modified_by of this LocalSolutionsFRBankMatch.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this LocalSolutionsFRBankMatch.  # noqa: E501

        The date and time when the match record was last modified.  # noqa: E501

        :return: The last_modified_date of this LocalSolutionsFRBankMatch.  # noqa: E501
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this LocalSolutionsFRBankMatch.

        The date and time when the match record was last modified.  # noqa: E501

        :param last_modified_date: The last_modified_date of this LocalSolutionsFRBankMatch.  # noqa: E501
        :type: datetime
        """

        self._last_modified_date = last_modified_date

    @property
    def id(self):
        """Gets the id of this LocalSolutionsFRBankMatch.  # noqa: E501

        The unique identifier of the match record.  # noqa: E501

        :return: The id of this LocalSolutionsFRBankMatch.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LocalSolutionsFRBankMatch.

        The unique identifier of the match record.  # noqa: E501

        :param id: The id of this LocalSolutionsFRBankMatch.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def score(self):
        """Gets the score of this LocalSolutionsFRBankMatch.  # noqa: E501

        The score assigned to the match.  # noqa: E501

        :return: The score of this LocalSolutionsFRBankMatch.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this LocalSolutionsFRBankMatch.

        The score assigned to the match.  # noqa: E501

        :param score: The score of this LocalSolutionsFRBankMatch.  # noqa: E501
        :type: int
        """

        self._score = score

    @property
    def classification(self):
        """Gets the classification of this LocalSolutionsFRBankMatch.  # noqa: E501

        The classification of the match.  # noqa: E501

        :return: The classification of this LocalSolutionsFRBankMatch.  # noqa: E501
        :rtype: str
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this LocalSolutionsFRBankMatch.

        The classification of the match.  # noqa: E501

        :param classification: The classification of this LocalSolutionsFRBankMatch.  # noqa: E501
        :type: str
        """

        self._classification = classification

    @property
    def status(self):
        """Gets the status of this LocalSolutionsFRBankMatch.  # noqa: E501

        The current status of the match.  # noqa: E501

        :return: The status of this LocalSolutionsFRBankMatch.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LocalSolutionsFRBankMatch.

        The current status of the match.  # noqa: E501

        :param status: The status of this LocalSolutionsFRBankMatch.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def entity(self):
        """Gets the entity of this LocalSolutionsFRBankMatch.  # noqa: E501


        :return: The entity of this LocalSolutionsFRBankMatch.  # noqa: E501
        :rtype: LocalSolutionsFRBankMatchEntity
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this LocalSolutionsFRBankMatch.


        :param entity: The entity of this LocalSolutionsFRBankMatch.  # noqa: E501
        :type: LocalSolutionsFRBankMatchEntity
        """

        self._entity = entity

    @property
    def issuer_company(self):
        """Gets the issuer_company of this LocalSolutionsFRBankMatch.  # noqa: E501


        :return: The issuer_company of this LocalSolutionsFRBankMatch.  # noqa: E501
        :rtype: LocalSolutionsFRBankMatchIssuerCompany
        """
        return self._issuer_company

    @issuer_company.setter
    def issuer_company(self, issuer_company):
        """Sets the issuer_company of this LocalSolutionsFRBankMatch.


        :param issuer_company: The issuer_company of this LocalSolutionsFRBankMatch.  # noqa: E501
        :type: LocalSolutionsFRBankMatchIssuerCompany
        """

        self._issuer_company = issuer_company

    @property
    def input(self):
        """Gets the input of this LocalSolutionsFRBankMatch.  # noqa: E501


        :return: The input of this LocalSolutionsFRBankMatch.  # noqa: E501
        :rtype: LocalSolutionsFRBankMatchInput
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this LocalSolutionsFRBankMatch.


        :param input: The input of this LocalSolutionsFRBankMatch.  # noqa: E501
        :type: LocalSolutionsFRBankMatchInput
        """

        self._input = input

    @property
    def with_deferred_result(self):
        """Gets the with_deferred_result of this LocalSolutionsFRBankMatch.  # noqa: E501

        Indicates if the match result is deferred.  # noqa: E501

        :return: The with_deferred_result of this LocalSolutionsFRBankMatch.  # noqa: E501
        :rtype: bool
        """
        return self._with_deferred_result

    @with_deferred_result.setter
    def with_deferred_result(self, with_deferred_result):
        """Sets the with_deferred_result of this LocalSolutionsFRBankMatch.

        Indicates if the match result is deferred.  # noqa: E501

        :param with_deferred_result: The with_deferred_result of this LocalSolutionsFRBankMatch.  # noqa: E501
        :type: bool
        """

        self._with_deferred_result = with_deferred_result

    @property
    def by_api(self):
        """Gets the by_api of this LocalSolutionsFRBankMatch.  # noqa: E501

        Indicates if the match was processed via API.  # noqa: E501

        :return: The by_api of this LocalSolutionsFRBankMatch.  # noqa: E501
        :rtype: bool
        """
        return self._by_api

    @by_api.setter
    def by_api(self, by_api):
        """Sets the by_api of this LocalSolutionsFRBankMatch.

        Indicates if the match was processed via API.  # noqa: E501

        :param by_api: The by_api of this LocalSolutionsFRBankMatch.  # noqa: E501
        :type: bool
        """

        self._by_api = by_api

    @property
    def by_ftp(self):
        """Gets the by_ftp of this LocalSolutionsFRBankMatch.  # noqa: E501

        Indicates if the match was processed via FTP.  # noqa: E501

        :return: The by_ftp of this LocalSolutionsFRBankMatch.  # noqa: E501
        :rtype: bool
        """
        return self._by_ftp

    @by_ftp.setter
    def by_ftp(self, by_ftp):
        """Sets the by_ftp of this LocalSolutionsFRBankMatch.

        Indicates if the match was processed via FTP.  # noqa: E501

        :param by_ftp: The by_ftp of this LocalSolutionsFRBankMatch.  # noqa: E501
        :type: bool
        """

        self._by_ftp = by_ftp

    @property
    def workflow(self):
        """Gets the workflow of this LocalSolutionsFRBankMatch.  # noqa: E501

        The workflow associated with the match.  # noqa: E501

        :return: The workflow of this LocalSolutionsFRBankMatch.  # noqa: E501
        :rtype: str
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """Sets the workflow of this LocalSolutionsFRBankMatch.

        The workflow associated with the match.  # noqa: E501

        :param workflow: The workflow of this LocalSolutionsFRBankMatch.  # noqa: E501
        :type: str
        """

        self._workflow = workflow

    @property
    def reasons(self):
        """Gets the reasons of this LocalSolutionsFRBankMatch.  # noqa: E501

        The reasons associated with the match.  # noqa: E501

        :return: The reasons of this LocalSolutionsFRBankMatch.  # noqa: E501
        :rtype: list[str]
        """
        return self._reasons

    @reasons.setter
    def reasons(self, reasons):
        """Sets the reasons of this LocalSolutionsFRBankMatch.

        The reasons associated with the match.  # noqa: E501

        :param reasons: The reasons of this LocalSolutionsFRBankMatch.  # noqa: E501
        :type: list[str]
        """

        self._reasons = reasons

    @property
    def reason_labels(self):
        """Gets the reason_labels of this LocalSolutionsFRBankMatch.  # noqa: E501

        Labels for the reasons associated with the match.  # noqa: E501

        :return: The reason_labels of this LocalSolutionsFRBankMatch.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._reason_labels

    @reason_labels.setter
    def reason_labels(self, reason_labels):
        """Sets the reason_labels of this LocalSolutionsFRBankMatch.

        Labels for the reasons associated with the match.  # noqa: E501

        :param reason_labels: The reason_labels of this LocalSolutionsFRBankMatch.  # noqa: E501
        :type: dict(str, str)
        """

        self._reason_labels = reason_labels

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
        if issubclass(LocalSolutionsFRBankMatch, dict):
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
        if not isinstance(other, LocalSolutionsFRBankMatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

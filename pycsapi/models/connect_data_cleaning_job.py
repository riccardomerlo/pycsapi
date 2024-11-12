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

class ConnectDataCleaningJob(object):
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
        'created_at': 'datetime',
        'modified_at': 'datetime',
        'managing_user_id': 'int',
        'managing_customer_id': 'int',
        'owning_customer_id': 'int',
        'owning_user_id': 'int',
        'status': 'str',
        'country_code': 'str',
        'portfolio_id': 'str',
        'source': 'str',
        'job_summary': 'ConnectDataCleaningJobJobSummary',
        'job_enrichment_settings': 'ConnectDataCleaningJobJobEnrichmentSettings',
        'archived': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'created_at': 'createdAt',
        'modified_at': 'modifiedAT',
        'managing_user_id': 'managingUserId',
        'managing_customer_id': 'managingCustomerId',
        'owning_customer_id': 'owningCustomerId',
        'owning_user_id': 'owningUserId',
        'status': 'status',
        'country_code': 'countryCode',
        'portfolio_id': 'portfolioId',
        'source': 'source',
        'job_summary': 'jobSummary',
        'job_enrichment_settings': 'jobEnrichmentSettings',
        'archived': 'archived'
    }

    def __init__(self, id=None, name=None, created_at=None, modified_at=None, managing_user_id=None, managing_customer_id=None, owning_customer_id=None, owning_user_id=None, status=None, country_code=None, portfolio_id=None, source=None, job_summary=None, job_enrichment_settings=None, archived=None):  # noqa: E501
        """ConnectDataCleaningJob - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._created_at = None
        self._modified_at = None
        self._managing_user_id = None
        self._managing_customer_id = None
        self._owning_customer_id = None
        self._owning_user_id = None
        self._status = None
        self._country_code = None
        self._portfolio_id = None
        self._source = None
        self._job_summary = None
        self._job_enrichment_settings = None
        self._archived = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at
        if managing_user_id is not None:
            self.managing_user_id = managing_user_id
        if managing_customer_id is not None:
            self.managing_customer_id = managing_customer_id
        if owning_customer_id is not None:
            self.owning_customer_id = owning_customer_id
        if owning_user_id is not None:
            self.owning_user_id = owning_user_id
        if status is not None:
            self.status = status
        if country_code is not None:
            self.country_code = country_code
        if portfolio_id is not None:
            self.portfolio_id = portfolio_id
        if source is not None:
            self.source = source
        if job_summary is not None:
            self.job_summary = job_summary
        if job_enrichment_settings is not None:
            self.job_enrichment_settings = job_enrichment_settings
        if archived is not None:
            self.archived = archived

    @property
    def id(self):
        """Gets the id of this ConnectDataCleaningJob.  # noqa: E501

        ID number associated to the created job - used for future searches  # noqa: E501

        :return: The id of this ConnectDataCleaningJob.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConnectDataCleaningJob.

        ID number associated to the created job - used for future searches  # noqa: E501

        :param id: The id of this ConnectDataCleaningJob.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ConnectDataCleaningJob.  # noqa: E501

        The name associated to the 'Job Number' created by the user in the 'POST - Create Job Request'  # noqa: E501

        :return: The name of this ConnectDataCleaningJob.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectDataCleaningJob.

        The name associated to the 'Job Number' created by the user in the 'POST - Create Job Request'  # noqa: E501

        :param name: The name of this ConnectDataCleaningJob.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this ConnectDataCleaningJob.  # noqa: E501


        :return: The created_at of this ConnectDataCleaningJob.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ConnectDataCleaningJob.


        :param created_at: The created_at of this ConnectDataCleaningJob.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this ConnectDataCleaningJob.  # noqa: E501


        :return: The modified_at of this ConnectDataCleaningJob.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this ConnectDataCleaningJob.


        :param modified_at: The modified_at of this ConnectDataCleaningJob.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def managing_user_id(self):
        """Gets the managing_user_id of this ConnectDataCleaningJob.  # noqa: E501


        :return: The managing_user_id of this ConnectDataCleaningJob.  # noqa: E501
        :rtype: int
        """
        return self._managing_user_id

    @managing_user_id.setter
    def managing_user_id(self, managing_user_id):
        """Sets the managing_user_id of this ConnectDataCleaningJob.


        :param managing_user_id: The managing_user_id of this ConnectDataCleaningJob.  # noqa: E501
        :type: int
        """

        self._managing_user_id = managing_user_id

    @property
    def managing_customer_id(self):
        """Gets the managing_customer_id of this ConnectDataCleaningJob.  # noqa: E501


        :return: The managing_customer_id of this ConnectDataCleaningJob.  # noqa: E501
        :rtype: int
        """
        return self._managing_customer_id

    @managing_customer_id.setter
    def managing_customer_id(self, managing_customer_id):
        """Sets the managing_customer_id of this ConnectDataCleaningJob.


        :param managing_customer_id: The managing_customer_id of this ConnectDataCleaningJob.  # noqa: E501
        :type: int
        """

        self._managing_customer_id = managing_customer_id

    @property
    def owning_customer_id(self):
        """Gets the owning_customer_id of this ConnectDataCleaningJob.  # noqa: E501


        :return: The owning_customer_id of this ConnectDataCleaningJob.  # noqa: E501
        :rtype: int
        """
        return self._owning_customer_id

    @owning_customer_id.setter
    def owning_customer_id(self, owning_customer_id):
        """Sets the owning_customer_id of this ConnectDataCleaningJob.


        :param owning_customer_id: The owning_customer_id of this ConnectDataCleaningJob.  # noqa: E501
        :type: int
        """

        self._owning_customer_id = owning_customer_id

    @property
    def owning_user_id(self):
        """Gets the owning_user_id of this ConnectDataCleaningJob.  # noqa: E501


        :return: The owning_user_id of this ConnectDataCleaningJob.  # noqa: E501
        :rtype: int
        """
        return self._owning_user_id

    @owning_user_id.setter
    def owning_user_id(self, owning_user_id):
        """Sets the owning_user_id of this ConnectDataCleaningJob.


        :param owning_user_id: The owning_user_id of this ConnectDataCleaningJob.  # noqa: E501
        :type: int
        """

        self._owning_user_id = owning_user_id

    @property
    def status(self):
        """Gets the status of this ConnectDataCleaningJob.  # noqa: E501


        :return: The status of this ConnectDataCleaningJob.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConnectDataCleaningJob.


        :param status: The status of this ConnectDataCleaningJob.  # noqa: E501
        :type: str
        """
        allowed_values = ["created", "uploading", "uploadError", "uploaded", "ready", "matching", "matchingError", "matched", "addingToPortfolio", "addedToPortfolio", "addedToPortfolioError", "aggregating", "aggregatingComplete", "aggregatingError", "enriching", "enrichmentError", "enriched", "transformFileError", "generateTrilliumFileError", "jobMatchingCompletionError", "jobMatchingComplete", "readyForEnriching", "enrichmentComplete", "enrichmentCompletionError", "pdfGenerationError"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def country_code(self):
        """Gets the country_code of this ConnectDataCleaningJob.  # noqa: E501

        Available after Enrichment  # noqa: E501

        :return: The country_code of this ConnectDataCleaningJob.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this ConnectDataCleaningJob.

        Available after Enrichment  # noqa: E501

        :param country_code: The country_code of this ConnectDataCleaningJob.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def portfolio_id(self):
        """Gets the portfolio_id of this ConnectDataCleaningJob.  # noqa: E501

        Available after Enrichment  # noqa: E501

        :return: The portfolio_id of this ConnectDataCleaningJob.  # noqa: E501
        :rtype: str
        """
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, portfolio_id):
        """Sets the portfolio_id of this ConnectDataCleaningJob.

        Available after Enrichment  # noqa: E501

        :param portfolio_id: The portfolio_id of this ConnectDataCleaningJob.  # noqa: E501
        :type: str
        """

        self._portfolio_id = portfolio_id

    @property
    def source(self):
        """Gets the source of this ConnectDataCleaningJob.  # noqa: E501


        :return: The source of this ConnectDataCleaningJob.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this ConnectDataCleaningJob.


        :param source: The source of this ConnectDataCleaningJob.  # noqa: E501
        :type: str
        """
        allowed_values = ["dataCleaning", "prospects"]  # noqa: E501
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"  # noqa: E501
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def job_summary(self):
        """Gets the job_summary of this ConnectDataCleaningJob.  # noqa: E501


        :return: The job_summary of this ConnectDataCleaningJob.  # noqa: E501
        :rtype: ConnectDataCleaningJobJobSummary
        """
        return self._job_summary

    @job_summary.setter
    def job_summary(self, job_summary):
        """Sets the job_summary of this ConnectDataCleaningJob.


        :param job_summary: The job_summary of this ConnectDataCleaningJob.  # noqa: E501
        :type: ConnectDataCleaningJobJobSummary
        """

        self._job_summary = job_summary

    @property
    def job_enrichment_settings(self):
        """Gets the job_enrichment_settings of this ConnectDataCleaningJob.  # noqa: E501


        :return: The job_enrichment_settings of this ConnectDataCleaningJob.  # noqa: E501
        :rtype: ConnectDataCleaningJobJobEnrichmentSettings
        """
        return self._job_enrichment_settings

    @job_enrichment_settings.setter
    def job_enrichment_settings(self, job_enrichment_settings):
        """Sets the job_enrichment_settings of this ConnectDataCleaningJob.


        :param job_enrichment_settings: The job_enrichment_settings of this ConnectDataCleaningJob.  # noqa: E501
        :type: ConnectDataCleaningJobJobEnrichmentSettings
        """

        self._job_enrichment_settings = job_enrichment_settings

    @property
    def archived(self):
        """Gets the archived of this ConnectDataCleaningJob.  # noqa: E501


        :return: The archived of this ConnectDataCleaningJob.  # noqa: E501
        :rtype: bool
        """
        return self._archived

    @archived.setter
    def archived(self, archived):
        """Sets the archived of this ConnectDataCleaningJob.


        :param archived: The archived of this ConnectDataCleaningJob.  # noqa: E501
        :type: bool
        """

        self._archived = archived

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
        if issubclass(ConnectDataCleaningJob, dict):
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
        if not isinstance(other, ConnectDataCleaningJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

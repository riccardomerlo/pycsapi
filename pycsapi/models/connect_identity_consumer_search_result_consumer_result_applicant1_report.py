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

class ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report(object):
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
        'report_title': 'str',
        'report_type': 'str',
        'summary': 'ConsumerResultReportSummary',
        'score': 'ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportScore',
        'address': 'ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportAddress',
        'previous_address1': 'ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportPreviousAddress1',
        'previous_address2': 'ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportPreviousAddress1',
        'links': 'ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportLinks',
        'insolvencies': 'list[ConsumerResultInsolvencies]',
        'judgements': 'list[ConsumerResultJudgements]',
        'history': 'list[ConsumerResultHistory]',
        'notices': 'list[ConsumerResultNotices]',
        'demographics': 'ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics',
        'share': 'ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShare',
        'share_available': 'bool'
    }

    attribute_map = {
        'report_title': 'reportTitle',
        'report_type': 'reportType',
        'summary': 'summary',
        'score': 'score',
        'address': 'address',
        'previous_address1': 'previousAddress1',
        'previous_address2': 'previousAddress2',
        'links': 'links',
        'insolvencies': 'insolvencies',
        'judgements': 'judgements',
        'history': 'history',
        'notices': 'notices',
        'demographics': 'demographics',
        'share': 'share',
        'share_available': 'shareAvailable'
    }

    def __init__(self, report_title=None, report_type=None, summary=None, score=None, address=None, previous_address1=None, previous_address2=None, links=None, insolvencies=None, judgements=None, history=None, notices=None, demographics=None, share=None, share_available=None):  # noqa: E501
        """ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report - a model defined in Swagger"""  # noqa: E501
        self._report_title = None
        self._report_type = None
        self._summary = None
        self._score = None
        self._address = None
        self._previous_address1 = None
        self._previous_address2 = None
        self._links = None
        self._insolvencies = None
        self._judgements = None
        self._history = None
        self._notices = None
        self._demographics = None
        self._share = None
        self._share_available = None
        self.discriminator = None
        if report_title is not None:
            self.report_title = report_title
        if report_type is not None:
            self.report_type = report_type
        if summary is not None:
            self.summary = summary
        if score is not None:
            self.score = score
        if address is not None:
            self.address = address
        if previous_address1 is not None:
            self.previous_address1 = previous_address1
        if previous_address2 is not None:
            self.previous_address2 = previous_address2
        if links is not None:
            self.links = links
        if insolvencies is not None:
            self.insolvencies = insolvencies
        if judgements is not None:
            self.judgements = judgements
        if history is not None:
            self.history = history
        if notices is not None:
            self.notices = notices
        if demographics is not None:
            self.demographics = demographics
        if share is not None:
            self.share = share
        if share_available is not None:
            self.share_available = share_available

    @property
    def report_title(self):
        """Gets the report_title of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501


        :return: The report_title of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :rtype: str
        """
        return self._report_title

    @report_title.setter
    def report_title(self, report_title):
        """Sets the report_title of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.


        :param report_title: The report_title of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :type: str
        """

        self._report_title = report_title

    @property
    def report_type(self):
        """Gets the report_type of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501


        :return: The report_type of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.


        :param report_type: The report_type of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :type: str
        """

        self._report_type = report_type

    @property
    def summary(self):
        """Gets the summary of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501


        :return: The summary of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :rtype: ConsumerResultReportSummary
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.


        :param summary: The summary of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :type: ConsumerResultReportSummary
        """

        self._summary = summary

    @property
    def score(self):
        """Gets the score of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501


        :return: The score of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :rtype: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportScore
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.


        :param score: The score of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :type: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportScore
        """

        self._score = score

    @property
    def address(self):
        """Gets the address of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501


        :return: The address of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :rtype: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.


        :param address: The address of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :type: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportAddress
        """

        self._address = address

    @property
    def previous_address1(self):
        """Gets the previous_address1 of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501


        :return: The previous_address1 of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :rtype: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportPreviousAddress1
        """
        return self._previous_address1

    @previous_address1.setter
    def previous_address1(self, previous_address1):
        """Sets the previous_address1 of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.


        :param previous_address1: The previous_address1 of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :type: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportPreviousAddress1
        """

        self._previous_address1 = previous_address1

    @property
    def previous_address2(self):
        """Gets the previous_address2 of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501


        :return: The previous_address2 of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :rtype: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportPreviousAddress1
        """
        return self._previous_address2

    @previous_address2.setter
    def previous_address2(self, previous_address2):
        """Sets the previous_address2 of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.


        :param previous_address2: The previous_address2 of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :type: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportPreviousAddress1
        """

        self._previous_address2 = previous_address2

    @property
    def links(self):
        """Gets the links of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501


        :return: The links of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :rtype: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.


        :param links: The links of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :type: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportLinks
        """

        self._links = links

    @property
    def insolvencies(self):
        """Gets the insolvencies of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501


        :return: The insolvencies of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :rtype: list[ConsumerResultInsolvencies]
        """
        return self._insolvencies

    @insolvencies.setter
    def insolvencies(self, insolvencies):
        """Sets the insolvencies of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.


        :param insolvencies: The insolvencies of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :type: list[ConsumerResultInsolvencies]
        """

        self._insolvencies = insolvencies

    @property
    def judgements(self):
        """Gets the judgements of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501


        :return: The judgements of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :rtype: list[ConsumerResultJudgements]
        """
        return self._judgements

    @judgements.setter
    def judgements(self, judgements):
        """Sets the judgements of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.


        :param judgements: The judgements of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :type: list[ConsumerResultJudgements]
        """

        self._judgements = judgements

    @property
    def history(self):
        """Gets the history of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501


        :return: The history of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :rtype: list[ConsumerResultHistory]
        """
        return self._history

    @history.setter
    def history(self, history):
        """Sets the history of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.


        :param history: The history of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :type: list[ConsumerResultHistory]
        """

        self._history = history

    @property
    def notices(self):
        """Gets the notices of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501


        :return: The notices of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :rtype: list[ConsumerResultNotices]
        """
        return self._notices

    @notices.setter
    def notices(self, notices):
        """Sets the notices of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.


        :param notices: The notices of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :type: list[ConsumerResultNotices]
        """

        self._notices = notices

    @property
    def demographics(self):
        """Gets the demographics of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501


        :return: The demographics of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :rtype: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics
        """
        return self._demographics

    @demographics.setter
    def demographics(self, demographics):
        """Sets the demographics of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.


        :param demographics: The demographics of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :type: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographics
        """

        self._demographics = demographics

    @property
    def share(self):
        """Gets the share of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501


        :return: The share of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :rtype: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShare
        """
        return self._share

    @share.setter
    def share(self, share):
        """Sets the share of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.


        :param share: The share of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :type: ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportShare
        """

        self._share = share

    @property
    def share_available(self):
        """Gets the share_available of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501


        :return: The share_available of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :rtype: bool
        """
        return self._share_available

    @share_available.setter
    def share_available(self, share_available):
        """Sets the share_available of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.


        :param share_available: The share_available of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report.  # noqa: E501
        :type: bool
        """

        self._share_available = share_available

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
        if issubclass(ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report, dict):
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
        if not isinstance(other, ConnectIdentityConsumerSearchResultConsumerResultApplicant1Report):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

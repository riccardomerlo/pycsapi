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

class CreditsafeGlobalDataReportsCompanyReport(object):
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
        'company_id': 'str',
        'language': 'CreditsafeGlobalDataLanguage',
        'company_summary': 'CreditsafeGlobalDataReportsLtdCompanySummary',
        'company_identification': 'CreditsafeGlobalDataReportsLtdCompanyIdentification',
        'credit_score': 'CreditsafeGlobalDataReportsLtdCreditScore',
        'contact_information': 'CreditsafeGlobalDataReportsLtdContactInformation',
        'indicators': 'CreditsafeGlobalDataReportsIndicators',
        'share_capital_structure': 'CreditsafeGlobalDataReportsLtdShareCapitalStructure',
        'directors': 'CreditsafeGlobalDataReportsLtdDirectors',
        'directorships': 'CreditsafeGlobalDataReportsDirectorships',
        'other_information': 'CreditsafeGlobalDataReportsLtdOtherInformation',
        'group_structure': 'CreditsafeGlobalDataReportsLtdGroupStructure',
        'extended_group_structure': 'list[CreditsafeGlobalDataReportsCompanyInGroup]',
        'financial_statements': 'list[CreditsafeGlobalDataReportsGlobalFinancialsGGS]',
        'local_financial_statements': 'list[CreditsafeGlobalDataReportsLtdFinancialStatement]',
        'negative_information': 'CreditsafeGlobalDataReportsReportNegativeInformation',
        'additional_information': 'CreditsafeGlobalDataReportsReportAdditionalInformation',
        'directors_extra': 'CreditsafeGlobalDataReportsLtdDirectorsExtra',
        'extended_group_structure_extra': 'CreditsafeGlobalDataReportsLtdExtendedGroupStructureExtra',
        'payment_data': 'CreditsafeGlobalDataReportsReportPaymentData',
        'payment_data_extra': 'CreditsafeGlobalDataReportsReportPaymentDataExtra',
        'alternate_summary': 'CreditsafeGlobalDataReportsReportAlternateSummary',
        'negative_information_extra': 'CreditsafeGlobalDataReportsReportNegativeInformationExtra'
    }

    attribute_map = {
        'company_id': 'companyId',
        'language': 'language',
        'company_summary': 'companySummary',
        'company_identification': 'companyIdentification',
        'credit_score': 'creditScore',
        'contact_information': 'contactInformation',
        'indicators': 'indicators',
        'share_capital_structure': 'shareCapitalStructure',
        'directors': 'directors',
        'directorships': 'directorships',
        'other_information': 'otherInformation',
        'group_structure': 'groupStructure',
        'extended_group_structure': 'extendedGroupStructure',
        'financial_statements': 'financialStatements',
        'local_financial_statements': 'localFinancialStatements',
        'negative_information': 'negativeInformation',
        'additional_information': 'additionalInformation',
        'directors_extra': 'directorsExtra',
        'extended_group_structure_extra': 'extendedGroupStructureExtra',
        'payment_data': 'paymentData',
        'payment_data_extra': 'paymentDataExtra',
        'alternate_summary': 'alternateSummary',
        'negative_information_extra': 'negativeInformationExtra'
    }

    def __init__(self, company_id=None, language=None, company_summary=None, company_identification=None, credit_score=None, contact_information=None, indicators=None, share_capital_structure=None, directors=None, directorships=None, other_information=None, group_structure=None, extended_group_structure=None, financial_statements=None, local_financial_statements=None, negative_information=None, additional_information=None, directors_extra=None, extended_group_structure_extra=None, payment_data=None, payment_data_extra=None, alternate_summary=None, negative_information_extra=None):  # noqa: E501
        """CreditsafeGlobalDataReportsCompanyReport - a model defined in Swagger"""  # noqa: E501
        self._company_id = None
        self._language = None
        self._company_summary = None
        self._company_identification = None
        self._credit_score = None
        self._contact_information = None
        self._indicators = None
        self._share_capital_structure = None
        self._directors = None
        self._directorships = None
        self._other_information = None
        self._group_structure = None
        self._extended_group_structure = None
        self._financial_statements = None
        self._local_financial_statements = None
        self._negative_information = None
        self._additional_information = None
        self._directors_extra = None
        self._extended_group_structure_extra = None
        self._payment_data = None
        self._payment_data_extra = None
        self._alternate_summary = None
        self._negative_information_extra = None
        self.discriminator = None
        if company_id is not None:
            self.company_id = company_id
        if language is not None:
            self.language = language
        if company_summary is not None:
            self.company_summary = company_summary
        if company_identification is not None:
            self.company_identification = company_identification
        if credit_score is not None:
            self.credit_score = credit_score
        if contact_information is not None:
            self.contact_information = contact_information
        if indicators is not None:
            self.indicators = indicators
        if share_capital_structure is not None:
            self.share_capital_structure = share_capital_structure
        if directors is not None:
            self.directors = directors
        if directorships is not None:
            self.directorships = directorships
        if other_information is not None:
            self.other_information = other_information
        if group_structure is not None:
            self.group_structure = group_structure
        if extended_group_structure is not None:
            self.extended_group_structure = extended_group_structure
        if financial_statements is not None:
            self.financial_statements = financial_statements
        if local_financial_statements is not None:
            self.local_financial_statements = local_financial_statements
        if negative_information is not None:
            self.negative_information = negative_information
        if additional_information is not None:
            self.additional_information = additional_information
        if directors_extra is not None:
            self.directors_extra = directors_extra
        if extended_group_structure_extra is not None:
            self.extended_group_structure_extra = extended_group_structure_extra
        if payment_data is not None:
            self.payment_data = payment_data
        if payment_data_extra is not None:
            self.payment_data_extra = payment_data_extra
        if alternate_summary is not None:
            self.alternate_summary = alternate_summary
        if negative_information_extra is not None:
            self.negative_information_extra = negative_information_extra

    @property
    def company_id(self):
        """Gets the company_id of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The company_id of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this CreditsafeGlobalDataReportsCompanyReport.


        :param company_id: The company_id of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def language(self):
        """Gets the language of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The language of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataLanguage
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this CreditsafeGlobalDataReportsCompanyReport.


        :param language: The language of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: CreditsafeGlobalDataLanguage
        """

        self._language = language

    @property
    def company_summary(self):
        """Gets the company_summary of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The company_summary of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsLtdCompanySummary
        """
        return self._company_summary

    @company_summary.setter
    def company_summary(self, company_summary):
        """Sets the company_summary of this CreditsafeGlobalDataReportsCompanyReport.


        :param company_summary: The company_summary of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: CreditsafeGlobalDataReportsLtdCompanySummary
        """

        self._company_summary = company_summary

    @property
    def company_identification(self):
        """Gets the company_identification of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The company_identification of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsLtdCompanyIdentification
        """
        return self._company_identification

    @company_identification.setter
    def company_identification(self, company_identification):
        """Sets the company_identification of this CreditsafeGlobalDataReportsCompanyReport.


        :param company_identification: The company_identification of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: CreditsafeGlobalDataReportsLtdCompanyIdentification
        """

        self._company_identification = company_identification

    @property
    def credit_score(self):
        """Gets the credit_score of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The credit_score of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsLtdCreditScore
        """
        return self._credit_score

    @credit_score.setter
    def credit_score(self, credit_score):
        """Sets the credit_score of this CreditsafeGlobalDataReportsCompanyReport.


        :param credit_score: The credit_score of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: CreditsafeGlobalDataReportsLtdCreditScore
        """

        self._credit_score = credit_score

    @property
    def contact_information(self):
        """Gets the contact_information of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The contact_information of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsLtdContactInformation
        """
        return self._contact_information

    @contact_information.setter
    def contact_information(self, contact_information):
        """Sets the contact_information of this CreditsafeGlobalDataReportsCompanyReport.


        :param contact_information: The contact_information of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: CreditsafeGlobalDataReportsLtdContactInformation
        """

        self._contact_information = contact_information

    @property
    def indicators(self):
        """Gets the indicators of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The indicators of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsIndicators
        """
        return self._indicators

    @indicators.setter
    def indicators(self, indicators):
        """Sets the indicators of this CreditsafeGlobalDataReportsCompanyReport.


        :param indicators: The indicators of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: CreditsafeGlobalDataReportsIndicators
        """

        self._indicators = indicators

    @property
    def share_capital_structure(self):
        """Gets the share_capital_structure of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The share_capital_structure of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsLtdShareCapitalStructure
        """
        return self._share_capital_structure

    @share_capital_structure.setter
    def share_capital_structure(self, share_capital_structure):
        """Sets the share_capital_structure of this CreditsafeGlobalDataReportsCompanyReport.


        :param share_capital_structure: The share_capital_structure of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: CreditsafeGlobalDataReportsLtdShareCapitalStructure
        """

        self._share_capital_structure = share_capital_structure

    @property
    def directors(self):
        """Gets the directors of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The directors of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsLtdDirectors
        """
        return self._directors

    @directors.setter
    def directors(self, directors):
        """Sets the directors of this CreditsafeGlobalDataReportsCompanyReport.


        :param directors: The directors of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: CreditsafeGlobalDataReportsLtdDirectors
        """

        self._directors = directors

    @property
    def directorships(self):
        """Gets the directorships of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The directorships of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsDirectorships
        """
        return self._directorships

    @directorships.setter
    def directorships(self, directorships):
        """Sets the directorships of this CreditsafeGlobalDataReportsCompanyReport.


        :param directorships: The directorships of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: CreditsafeGlobalDataReportsDirectorships
        """

        self._directorships = directorships

    @property
    def other_information(self):
        """Gets the other_information of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The other_information of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsLtdOtherInformation
        """
        return self._other_information

    @other_information.setter
    def other_information(self, other_information):
        """Sets the other_information of this CreditsafeGlobalDataReportsCompanyReport.


        :param other_information: The other_information of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: CreditsafeGlobalDataReportsLtdOtherInformation
        """

        self._other_information = other_information

    @property
    def group_structure(self):
        """Gets the group_structure of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The group_structure of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsLtdGroupStructure
        """
        return self._group_structure

    @group_structure.setter
    def group_structure(self, group_structure):
        """Sets the group_structure of this CreditsafeGlobalDataReportsCompanyReport.


        :param group_structure: The group_structure of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: CreditsafeGlobalDataReportsLtdGroupStructure
        """

        self._group_structure = group_structure

    @property
    def extended_group_structure(self):
        """Gets the extended_group_structure of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The extended_group_structure of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: list[CreditsafeGlobalDataReportsCompanyInGroup]
        """
        return self._extended_group_structure

    @extended_group_structure.setter
    def extended_group_structure(self, extended_group_structure):
        """Sets the extended_group_structure of this CreditsafeGlobalDataReportsCompanyReport.


        :param extended_group_structure: The extended_group_structure of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: list[CreditsafeGlobalDataReportsCompanyInGroup]
        """

        self._extended_group_structure = extended_group_structure

    @property
    def financial_statements(self):
        """Gets the financial_statements of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The financial_statements of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: list[CreditsafeGlobalDataReportsGlobalFinancialsGGS]
        """
        return self._financial_statements

    @financial_statements.setter
    def financial_statements(self, financial_statements):
        """Sets the financial_statements of this CreditsafeGlobalDataReportsCompanyReport.


        :param financial_statements: The financial_statements of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: list[CreditsafeGlobalDataReportsGlobalFinancialsGGS]
        """

        self._financial_statements = financial_statements

    @property
    def local_financial_statements(self):
        """Gets the local_financial_statements of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The local_financial_statements of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: list[CreditsafeGlobalDataReportsLtdFinancialStatement]
        """
        return self._local_financial_statements

    @local_financial_statements.setter
    def local_financial_statements(self, local_financial_statements):
        """Sets the local_financial_statements of this CreditsafeGlobalDataReportsCompanyReport.


        :param local_financial_statements: The local_financial_statements of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: list[CreditsafeGlobalDataReportsLtdFinancialStatement]
        """

        self._local_financial_statements = local_financial_statements

    @property
    def negative_information(self):
        """Gets the negative_information of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The negative_information of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsReportNegativeInformation
        """
        return self._negative_information

    @negative_information.setter
    def negative_information(self, negative_information):
        """Sets the negative_information of this CreditsafeGlobalDataReportsCompanyReport.


        :param negative_information: The negative_information of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: CreditsafeGlobalDataReportsReportNegativeInformation
        """

        self._negative_information = negative_information

    @property
    def additional_information(self):
        """Gets the additional_information of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The additional_information of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsReportAdditionalInformation
        """
        return self._additional_information

    @additional_information.setter
    def additional_information(self, additional_information):
        """Sets the additional_information of this CreditsafeGlobalDataReportsCompanyReport.


        :param additional_information: The additional_information of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: CreditsafeGlobalDataReportsReportAdditionalInformation
        """

        self._additional_information = additional_information

    @property
    def directors_extra(self):
        """Gets the directors_extra of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The directors_extra of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsLtdDirectorsExtra
        """
        return self._directors_extra

    @directors_extra.setter
    def directors_extra(self, directors_extra):
        """Sets the directors_extra of this CreditsafeGlobalDataReportsCompanyReport.


        :param directors_extra: The directors_extra of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: CreditsafeGlobalDataReportsLtdDirectorsExtra
        """

        self._directors_extra = directors_extra

    @property
    def extended_group_structure_extra(self):
        """Gets the extended_group_structure_extra of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The extended_group_structure_extra of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsLtdExtendedGroupStructureExtra
        """
        return self._extended_group_structure_extra

    @extended_group_structure_extra.setter
    def extended_group_structure_extra(self, extended_group_structure_extra):
        """Sets the extended_group_structure_extra of this CreditsafeGlobalDataReportsCompanyReport.


        :param extended_group_structure_extra: The extended_group_structure_extra of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: CreditsafeGlobalDataReportsLtdExtendedGroupStructureExtra
        """

        self._extended_group_structure_extra = extended_group_structure_extra

    @property
    def payment_data(self):
        """Gets the payment_data of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The payment_data of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsReportPaymentData
        """
        return self._payment_data

    @payment_data.setter
    def payment_data(self, payment_data):
        """Sets the payment_data of this CreditsafeGlobalDataReportsCompanyReport.


        :param payment_data: The payment_data of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: CreditsafeGlobalDataReportsReportPaymentData
        """

        self._payment_data = payment_data

    @property
    def payment_data_extra(self):
        """Gets the payment_data_extra of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The payment_data_extra of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsReportPaymentDataExtra
        """
        return self._payment_data_extra

    @payment_data_extra.setter
    def payment_data_extra(self, payment_data_extra):
        """Sets the payment_data_extra of this CreditsafeGlobalDataReportsCompanyReport.


        :param payment_data_extra: The payment_data_extra of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: CreditsafeGlobalDataReportsReportPaymentDataExtra
        """

        self._payment_data_extra = payment_data_extra

    @property
    def alternate_summary(self):
        """Gets the alternate_summary of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The alternate_summary of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsReportAlternateSummary
        """
        return self._alternate_summary

    @alternate_summary.setter
    def alternate_summary(self, alternate_summary):
        """Sets the alternate_summary of this CreditsafeGlobalDataReportsCompanyReport.


        :param alternate_summary: The alternate_summary of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: CreditsafeGlobalDataReportsReportAlternateSummary
        """

        self._alternate_summary = alternate_summary

    @property
    def negative_information_extra(self):
        """Gets the negative_information_extra of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501


        :return: The negative_information_extra of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsReportNegativeInformationExtra
        """
        return self._negative_information_extra

    @negative_information_extra.setter
    def negative_information_extra(self, negative_information_extra):
        """Sets the negative_information_extra of this CreditsafeGlobalDataReportsCompanyReport.


        :param negative_information_extra: The negative_information_extra of this CreditsafeGlobalDataReportsCompanyReport.  # noqa: E501
        :type: CreditsafeGlobalDataReportsReportNegativeInformationExtra
        """

        self._negative_information_extra = negative_information_extra

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
        if issubclass(CreditsafeGlobalDataReportsCompanyReport, dict):
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
        if not isinstance(other, CreditsafeGlobalDataReportsCompanyReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

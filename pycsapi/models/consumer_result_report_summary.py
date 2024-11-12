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

class ConsumerResultReportSummary(object):
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
        'matched_data': 'list[ConsumerResultReportSummaryMatchedData]',
        'match_level': 'str',
        'notices_of_corrections': 'bool',
        'total_disputes': 'int',
        'confirmed_address': 'str',
        'residency': 'list[ConsumerResultReportSummaryResidency]',
        'credit_searches_at_current_address': 'ConsumerResultReportSummaryCreditSearchesAtCurrentAddress',
        'insolvency_at_address': 'ConsumerResultReportSummaryInsolvencyAtAddress',
        'links': 'ConsumerResultReportSummaryLinks',
        'judgements': 'ConsumerResultReportSummaryJudgements',
        'total_cifas': 'int',
        'rtr': 'bool',
        'impaired_credit_history': 'ConsumerResultReportSummaryImpairedCreditHistory',
        'third_party': 'ConsumerResultReportSummaryThirdParty',
        'address': 'ConsumerResultReportSummaryAddress',
        'card_data': 'ConsumerResultReportSummaryCardData'
    }

    attribute_map = {
        'matched_data': 'matchedData',
        'match_level': 'matchLevel',
        'notices_of_corrections': 'noticesOfCorrections',
        'total_disputes': 'totalDisputes',
        'confirmed_address': 'confirmedAddress',
        'residency': 'residency',
        'credit_searches_at_current_address': 'creditSearchesAtCurrentAddress',
        'insolvency_at_address': 'insolvencyAtAddress',
        'links': 'links',
        'judgements': 'judgements',
        'total_cifas': 'totalCifas',
        'rtr': 'rtr',
        'impaired_credit_history': 'impairedCreditHistory',
        'third_party': 'thirdParty',
        'address': 'address',
        'card_data': 'cardData'
    }

    def __init__(self, matched_data=None, match_level=None, notices_of_corrections=None, total_disputes=None, confirmed_address=None, residency=None, credit_searches_at_current_address=None, insolvency_at_address=None, links=None, judgements=None, total_cifas=None, rtr=None, impaired_credit_history=None, third_party=None, address=None, card_data=None):  # noqa: E501
        """ConsumerResultReportSummary - a model defined in Swagger"""  # noqa: E501
        self._matched_data = None
        self._match_level = None
        self._notices_of_corrections = None
        self._total_disputes = None
        self._confirmed_address = None
        self._residency = None
        self._credit_searches_at_current_address = None
        self._insolvency_at_address = None
        self._links = None
        self._judgements = None
        self._total_cifas = None
        self._rtr = None
        self._impaired_credit_history = None
        self._third_party = None
        self._address = None
        self._card_data = None
        self.discriminator = None
        if matched_data is not None:
            self.matched_data = matched_data
        if match_level is not None:
            self.match_level = match_level
        if notices_of_corrections is not None:
            self.notices_of_corrections = notices_of_corrections
        if total_disputes is not None:
            self.total_disputes = total_disputes
        if confirmed_address is not None:
            self.confirmed_address = confirmed_address
        if residency is not None:
            self.residency = residency
        if credit_searches_at_current_address is not None:
            self.credit_searches_at_current_address = credit_searches_at_current_address
        if insolvency_at_address is not None:
            self.insolvency_at_address = insolvency_at_address
        if links is not None:
            self.links = links
        if judgements is not None:
            self.judgements = judgements
        if total_cifas is not None:
            self.total_cifas = total_cifas
        if rtr is not None:
            self.rtr = rtr
        if impaired_credit_history is not None:
            self.impaired_credit_history = impaired_credit_history
        if third_party is not None:
            self.third_party = third_party
        if address is not None:
            self.address = address
        if card_data is not None:
            self.card_data = card_data

    @property
    def matched_data(self):
        """Gets the matched_data of this ConsumerResultReportSummary.  # noqa: E501


        :return: The matched_data of this ConsumerResultReportSummary.  # noqa: E501
        :rtype: list[ConsumerResultReportSummaryMatchedData]
        """
        return self._matched_data

    @matched_data.setter
    def matched_data(self, matched_data):
        """Sets the matched_data of this ConsumerResultReportSummary.


        :param matched_data: The matched_data of this ConsumerResultReportSummary.  # noqa: E501
        :type: list[ConsumerResultReportSummaryMatchedData]
        """

        self._matched_data = matched_data

    @property
    def match_level(self):
        """Gets the match_level of this ConsumerResultReportSummary.  # noqa: E501


        :return: The match_level of this ConsumerResultReportSummary.  # noqa: E501
        :rtype: str
        """
        return self._match_level

    @match_level.setter
    def match_level(self, match_level):
        """Sets the match_level of this ConsumerResultReportSummary.


        :param match_level: The match_level of this ConsumerResultReportSummary.  # noqa: E501
        :type: str
        """

        self._match_level = match_level

    @property
    def notices_of_corrections(self):
        """Gets the notices_of_corrections of this ConsumerResultReportSummary.  # noqa: E501


        :return: The notices_of_corrections of this ConsumerResultReportSummary.  # noqa: E501
        :rtype: bool
        """
        return self._notices_of_corrections

    @notices_of_corrections.setter
    def notices_of_corrections(self, notices_of_corrections):
        """Sets the notices_of_corrections of this ConsumerResultReportSummary.


        :param notices_of_corrections: The notices_of_corrections of this ConsumerResultReportSummary.  # noqa: E501
        :type: bool
        """

        self._notices_of_corrections = notices_of_corrections

    @property
    def total_disputes(self):
        """Gets the total_disputes of this ConsumerResultReportSummary.  # noqa: E501


        :return: The total_disputes of this ConsumerResultReportSummary.  # noqa: E501
        :rtype: int
        """
        return self._total_disputes

    @total_disputes.setter
    def total_disputes(self, total_disputes):
        """Sets the total_disputes of this ConsumerResultReportSummary.


        :param total_disputes: The total_disputes of this ConsumerResultReportSummary.  # noqa: E501
        :type: int
        """

        self._total_disputes = total_disputes

    @property
    def confirmed_address(self):
        """Gets the confirmed_address of this ConsumerResultReportSummary.  # noqa: E501


        :return: The confirmed_address of this ConsumerResultReportSummary.  # noqa: E501
        :rtype: str
        """
        return self._confirmed_address

    @confirmed_address.setter
    def confirmed_address(self, confirmed_address):
        """Sets the confirmed_address of this ConsumerResultReportSummary.


        :param confirmed_address: The confirmed_address of this ConsumerResultReportSummary.  # noqa: E501
        :type: str
        """

        self._confirmed_address = confirmed_address

    @property
    def residency(self):
        """Gets the residency of this ConsumerResultReportSummary.  # noqa: E501


        :return: The residency of this ConsumerResultReportSummary.  # noqa: E501
        :rtype: list[ConsumerResultReportSummaryResidency]
        """
        return self._residency

    @residency.setter
    def residency(self, residency):
        """Sets the residency of this ConsumerResultReportSummary.


        :param residency: The residency of this ConsumerResultReportSummary.  # noqa: E501
        :type: list[ConsumerResultReportSummaryResidency]
        """

        self._residency = residency

    @property
    def credit_searches_at_current_address(self):
        """Gets the credit_searches_at_current_address of this ConsumerResultReportSummary.  # noqa: E501


        :return: The credit_searches_at_current_address of this ConsumerResultReportSummary.  # noqa: E501
        :rtype: ConsumerResultReportSummaryCreditSearchesAtCurrentAddress
        """
        return self._credit_searches_at_current_address

    @credit_searches_at_current_address.setter
    def credit_searches_at_current_address(self, credit_searches_at_current_address):
        """Sets the credit_searches_at_current_address of this ConsumerResultReportSummary.


        :param credit_searches_at_current_address: The credit_searches_at_current_address of this ConsumerResultReportSummary.  # noqa: E501
        :type: ConsumerResultReportSummaryCreditSearchesAtCurrentAddress
        """

        self._credit_searches_at_current_address = credit_searches_at_current_address

    @property
    def insolvency_at_address(self):
        """Gets the insolvency_at_address of this ConsumerResultReportSummary.  # noqa: E501


        :return: The insolvency_at_address of this ConsumerResultReportSummary.  # noqa: E501
        :rtype: ConsumerResultReportSummaryInsolvencyAtAddress
        """
        return self._insolvency_at_address

    @insolvency_at_address.setter
    def insolvency_at_address(self, insolvency_at_address):
        """Sets the insolvency_at_address of this ConsumerResultReportSummary.


        :param insolvency_at_address: The insolvency_at_address of this ConsumerResultReportSummary.  # noqa: E501
        :type: ConsumerResultReportSummaryInsolvencyAtAddress
        """

        self._insolvency_at_address = insolvency_at_address

    @property
    def links(self):
        """Gets the links of this ConsumerResultReportSummary.  # noqa: E501


        :return: The links of this ConsumerResultReportSummary.  # noqa: E501
        :rtype: ConsumerResultReportSummaryLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ConsumerResultReportSummary.


        :param links: The links of this ConsumerResultReportSummary.  # noqa: E501
        :type: ConsumerResultReportSummaryLinks
        """

        self._links = links

    @property
    def judgements(self):
        """Gets the judgements of this ConsumerResultReportSummary.  # noqa: E501


        :return: The judgements of this ConsumerResultReportSummary.  # noqa: E501
        :rtype: ConsumerResultReportSummaryJudgements
        """
        return self._judgements

    @judgements.setter
    def judgements(self, judgements):
        """Sets the judgements of this ConsumerResultReportSummary.


        :param judgements: The judgements of this ConsumerResultReportSummary.  # noqa: E501
        :type: ConsumerResultReportSummaryJudgements
        """

        self._judgements = judgements

    @property
    def total_cifas(self):
        """Gets the total_cifas of this ConsumerResultReportSummary.  # noqa: E501


        :return: The total_cifas of this ConsumerResultReportSummary.  # noqa: E501
        :rtype: int
        """
        return self._total_cifas

    @total_cifas.setter
    def total_cifas(self, total_cifas):
        """Sets the total_cifas of this ConsumerResultReportSummary.


        :param total_cifas: The total_cifas of this ConsumerResultReportSummary.  # noqa: E501
        :type: int
        """

        self._total_cifas = total_cifas

    @property
    def rtr(self):
        """Gets the rtr of this ConsumerResultReportSummary.  # noqa: E501


        :return: The rtr of this ConsumerResultReportSummary.  # noqa: E501
        :rtype: bool
        """
        return self._rtr

    @rtr.setter
    def rtr(self, rtr):
        """Sets the rtr of this ConsumerResultReportSummary.


        :param rtr: The rtr of this ConsumerResultReportSummary.  # noqa: E501
        :type: bool
        """

        self._rtr = rtr

    @property
    def impaired_credit_history(self):
        """Gets the impaired_credit_history of this ConsumerResultReportSummary.  # noqa: E501


        :return: The impaired_credit_history of this ConsumerResultReportSummary.  # noqa: E501
        :rtype: ConsumerResultReportSummaryImpairedCreditHistory
        """
        return self._impaired_credit_history

    @impaired_credit_history.setter
    def impaired_credit_history(self, impaired_credit_history):
        """Sets the impaired_credit_history of this ConsumerResultReportSummary.


        :param impaired_credit_history: The impaired_credit_history of this ConsumerResultReportSummary.  # noqa: E501
        :type: ConsumerResultReportSummaryImpairedCreditHistory
        """

        self._impaired_credit_history = impaired_credit_history

    @property
    def third_party(self):
        """Gets the third_party of this ConsumerResultReportSummary.  # noqa: E501


        :return: The third_party of this ConsumerResultReportSummary.  # noqa: E501
        :rtype: ConsumerResultReportSummaryThirdParty
        """
        return self._third_party

    @third_party.setter
    def third_party(self, third_party):
        """Sets the third_party of this ConsumerResultReportSummary.


        :param third_party: The third_party of this ConsumerResultReportSummary.  # noqa: E501
        :type: ConsumerResultReportSummaryThirdParty
        """

        self._third_party = third_party

    @property
    def address(self):
        """Gets the address of this ConsumerResultReportSummary.  # noqa: E501


        :return: The address of this ConsumerResultReportSummary.  # noqa: E501
        :rtype: ConsumerResultReportSummaryAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ConsumerResultReportSummary.


        :param address: The address of this ConsumerResultReportSummary.  # noqa: E501
        :type: ConsumerResultReportSummaryAddress
        """

        self._address = address

    @property
    def card_data(self):
        """Gets the card_data of this ConsumerResultReportSummary.  # noqa: E501


        :return: The card_data of this ConsumerResultReportSummary.  # noqa: E501
        :rtype: ConsumerResultReportSummaryCardData
        """
        return self._card_data

    @card_data.setter
    def card_data(self, card_data):
        """Sets the card_data of this ConsumerResultReportSummary.


        :param card_data: The card_data of this ConsumerResultReportSummary.  # noqa: E501
        :type: ConsumerResultReportSummaryCardData
        """

        self._card_data = card_data

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
        if issubclass(ConsumerResultReportSummary, dict):
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
        if not isinstance(other, ConsumerResultReportSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

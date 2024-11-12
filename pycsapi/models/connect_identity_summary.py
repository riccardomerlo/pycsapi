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

class ConnectIdentitySummary(object):
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
        'name': 'str',
        'matched_data': 'list[ConnectIdentityReportMatchedData]',
        'match_level': 'str',
        'notices_of_corrections': 'bool',
        'total_disputes': 'int',
        'confirmed_address': 'str',
        'residency': 'list[ConnectIdentityReportResidencyConfirmation]',
        'credit_searches_at_current_address': 'ConnectIdentityReportCreditSearchesAtCurrentAddress',
        'insolvency_at_address': 'ConnectIdentityReportInsolvencyAtAddress',
        'links': 'ConnectIdentitySummaryLinks',
        'judgements': 'ConnectIdentityReportSummaryJudgements',
        'total_cifas': 'int',
        'rtr': 'bool',
        'share': 'ConnectIdentitySummaryShare',
        'behavioural_data': 'ConnectIdentitySummaryBehaviouralData',
        'impaired_credit_history': 'ConnectIdentitySummaryIch',
        'third_party': 'ConnectIdentitySummaryThirdParty',
        'address': 'ConnectIdentitySummaryAddress',
        'in_debt': 'ConnectIdentitySummaryInDebt',
        'card_data': 'ConnectIdentitySummaryCardData'
    }

    attribute_map = {
        'name': 'name',
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
        'share': 'share',
        'behavioural_data': 'behaviouralData',
        'impaired_credit_history': 'impairedCreditHistory',
        'third_party': 'thirdParty',
        'address': 'address',
        'in_debt': 'inDebt',
        'card_data': 'cardData'
    }

    def __init__(self, name=None, matched_data=None, match_level=None, notices_of_corrections=None, total_disputes=None, confirmed_address=None, residency=None, credit_searches_at_current_address=None, insolvency_at_address=None, links=None, judgements=None, total_cifas=None, rtr=None, share=None, behavioural_data=None, impaired_credit_history=None, third_party=None, address=None, in_debt=None, card_data=None):  # noqa: E501
        """ConnectIdentitySummary - a model defined in Swagger"""  # noqa: E501
        self._name = None
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
        self._share = None
        self._behavioural_data = None
        self._impaired_credit_history = None
        self._third_party = None
        self._address = None
        self._in_debt = None
        self._card_data = None
        self.discriminator = None
        if name is not None:
            self.name = name
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
        if share is not None:
            self.share = share
        if behavioural_data is not None:
            self.behavioural_data = behavioural_data
        if impaired_credit_history is not None:
            self.impaired_credit_history = impaired_credit_history
        if third_party is not None:
            self.third_party = third_party
        if address is not None:
            self.address = address
        if in_debt is not None:
            self.in_debt = in_debt
        if card_data is not None:
            self.card_data = card_data

    @property
    def name(self):
        """Gets the name of this ConnectIdentitySummary.  # noqa: E501


        :return: The name of this ConnectIdentitySummary.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectIdentitySummary.


        :param name: The name of this ConnectIdentitySummary.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def matched_data(self):
        """Gets the matched_data of this ConnectIdentitySummary.  # noqa: E501


        :return: The matched_data of this ConnectIdentitySummary.  # noqa: E501
        :rtype: list[ConnectIdentityReportMatchedData]
        """
        return self._matched_data

    @matched_data.setter
    def matched_data(self, matched_data):
        """Sets the matched_data of this ConnectIdentitySummary.


        :param matched_data: The matched_data of this ConnectIdentitySummary.  # noqa: E501
        :type: list[ConnectIdentityReportMatchedData]
        """

        self._matched_data = matched_data

    @property
    def match_level(self):
        """Gets the match_level of this ConnectIdentitySummary.  # noqa: E501


        :return: The match_level of this ConnectIdentitySummary.  # noqa: E501
        :rtype: str
        """
        return self._match_level

    @match_level.setter
    def match_level(self, match_level):
        """Sets the match_level of this ConnectIdentitySummary.


        :param match_level: The match_level of this ConnectIdentitySummary.  # noqa: E501
        :type: str
        """

        self._match_level = match_level

    @property
    def notices_of_corrections(self):
        """Gets the notices_of_corrections of this ConnectIdentitySummary.  # noqa: E501


        :return: The notices_of_corrections of this ConnectIdentitySummary.  # noqa: E501
        :rtype: bool
        """
        return self._notices_of_corrections

    @notices_of_corrections.setter
    def notices_of_corrections(self, notices_of_corrections):
        """Sets the notices_of_corrections of this ConnectIdentitySummary.


        :param notices_of_corrections: The notices_of_corrections of this ConnectIdentitySummary.  # noqa: E501
        :type: bool
        """

        self._notices_of_corrections = notices_of_corrections

    @property
    def total_disputes(self):
        """Gets the total_disputes of this ConnectIdentitySummary.  # noqa: E501


        :return: The total_disputes of this ConnectIdentitySummary.  # noqa: E501
        :rtype: int
        """
        return self._total_disputes

    @total_disputes.setter
    def total_disputes(self, total_disputes):
        """Sets the total_disputes of this ConnectIdentitySummary.


        :param total_disputes: The total_disputes of this ConnectIdentitySummary.  # noqa: E501
        :type: int
        """

        self._total_disputes = total_disputes

    @property
    def confirmed_address(self):
        """Gets the confirmed_address of this ConnectIdentitySummary.  # noqa: E501


        :return: The confirmed_address of this ConnectIdentitySummary.  # noqa: E501
        :rtype: str
        """
        return self._confirmed_address

    @confirmed_address.setter
    def confirmed_address(self, confirmed_address):
        """Sets the confirmed_address of this ConnectIdentitySummary.


        :param confirmed_address: The confirmed_address of this ConnectIdentitySummary.  # noqa: E501
        :type: str
        """

        self._confirmed_address = confirmed_address

    @property
    def residency(self):
        """Gets the residency of this ConnectIdentitySummary.  # noqa: E501


        :return: The residency of this ConnectIdentitySummary.  # noqa: E501
        :rtype: list[ConnectIdentityReportResidencyConfirmation]
        """
        return self._residency

    @residency.setter
    def residency(self, residency):
        """Sets the residency of this ConnectIdentitySummary.


        :param residency: The residency of this ConnectIdentitySummary.  # noqa: E501
        :type: list[ConnectIdentityReportResidencyConfirmation]
        """

        self._residency = residency

    @property
    def credit_searches_at_current_address(self):
        """Gets the credit_searches_at_current_address of this ConnectIdentitySummary.  # noqa: E501


        :return: The credit_searches_at_current_address of this ConnectIdentitySummary.  # noqa: E501
        :rtype: ConnectIdentityReportCreditSearchesAtCurrentAddress
        """
        return self._credit_searches_at_current_address

    @credit_searches_at_current_address.setter
    def credit_searches_at_current_address(self, credit_searches_at_current_address):
        """Sets the credit_searches_at_current_address of this ConnectIdentitySummary.


        :param credit_searches_at_current_address: The credit_searches_at_current_address of this ConnectIdentitySummary.  # noqa: E501
        :type: ConnectIdentityReportCreditSearchesAtCurrentAddress
        """

        self._credit_searches_at_current_address = credit_searches_at_current_address

    @property
    def insolvency_at_address(self):
        """Gets the insolvency_at_address of this ConnectIdentitySummary.  # noqa: E501


        :return: The insolvency_at_address of this ConnectIdentitySummary.  # noqa: E501
        :rtype: ConnectIdentityReportInsolvencyAtAddress
        """
        return self._insolvency_at_address

    @insolvency_at_address.setter
    def insolvency_at_address(self, insolvency_at_address):
        """Sets the insolvency_at_address of this ConnectIdentitySummary.


        :param insolvency_at_address: The insolvency_at_address of this ConnectIdentitySummary.  # noqa: E501
        :type: ConnectIdentityReportInsolvencyAtAddress
        """

        self._insolvency_at_address = insolvency_at_address

    @property
    def links(self):
        """Gets the links of this ConnectIdentitySummary.  # noqa: E501


        :return: The links of this ConnectIdentitySummary.  # noqa: E501
        :rtype: ConnectIdentitySummaryLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ConnectIdentitySummary.


        :param links: The links of this ConnectIdentitySummary.  # noqa: E501
        :type: ConnectIdentitySummaryLinks
        """

        self._links = links

    @property
    def judgements(self):
        """Gets the judgements of this ConnectIdentitySummary.  # noqa: E501


        :return: The judgements of this ConnectIdentitySummary.  # noqa: E501
        :rtype: ConnectIdentityReportSummaryJudgements
        """
        return self._judgements

    @judgements.setter
    def judgements(self, judgements):
        """Sets the judgements of this ConnectIdentitySummary.


        :param judgements: The judgements of this ConnectIdentitySummary.  # noqa: E501
        :type: ConnectIdentityReportSummaryJudgements
        """

        self._judgements = judgements

    @property
    def total_cifas(self):
        """Gets the total_cifas of this ConnectIdentitySummary.  # noqa: E501


        :return: The total_cifas of this ConnectIdentitySummary.  # noqa: E501
        :rtype: int
        """
        return self._total_cifas

    @total_cifas.setter
    def total_cifas(self, total_cifas):
        """Sets the total_cifas of this ConnectIdentitySummary.


        :param total_cifas: The total_cifas of this ConnectIdentitySummary.  # noqa: E501
        :type: int
        """

        self._total_cifas = total_cifas

    @property
    def rtr(self):
        """Gets the rtr of this ConnectIdentitySummary.  # noqa: E501


        :return: The rtr of this ConnectIdentitySummary.  # noqa: E501
        :rtype: bool
        """
        return self._rtr

    @rtr.setter
    def rtr(self, rtr):
        """Sets the rtr of this ConnectIdentitySummary.


        :param rtr: The rtr of this ConnectIdentitySummary.  # noqa: E501
        :type: bool
        """

        self._rtr = rtr

    @property
    def share(self):
        """Gets the share of this ConnectIdentitySummary.  # noqa: E501


        :return: The share of this ConnectIdentitySummary.  # noqa: E501
        :rtype: ConnectIdentitySummaryShare
        """
        return self._share

    @share.setter
    def share(self, share):
        """Sets the share of this ConnectIdentitySummary.


        :param share: The share of this ConnectIdentitySummary.  # noqa: E501
        :type: ConnectIdentitySummaryShare
        """

        self._share = share

    @property
    def behavioural_data(self):
        """Gets the behavioural_data of this ConnectIdentitySummary.  # noqa: E501


        :return: The behavioural_data of this ConnectIdentitySummary.  # noqa: E501
        :rtype: ConnectIdentitySummaryBehaviouralData
        """
        return self._behavioural_data

    @behavioural_data.setter
    def behavioural_data(self, behavioural_data):
        """Sets the behavioural_data of this ConnectIdentitySummary.


        :param behavioural_data: The behavioural_data of this ConnectIdentitySummary.  # noqa: E501
        :type: ConnectIdentitySummaryBehaviouralData
        """

        self._behavioural_data = behavioural_data

    @property
    def impaired_credit_history(self):
        """Gets the impaired_credit_history of this ConnectIdentitySummary.  # noqa: E501


        :return: The impaired_credit_history of this ConnectIdentitySummary.  # noqa: E501
        :rtype: ConnectIdentitySummaryIch
        """
        return self._impaired_credit_history

    @impaired_credit_history.setter
    def impaired_credit_history(self, impaired_credit_history):
        """Sets the impaired_credit_history of this ConnectIdentitySummary.


        :param impaired_credit_history: The impaired_credit_history of this ConnectIdentitySummary.  # noqa: E501
        :type: ConnectIdentitySummaryIch
        """

        self._impaired_credit_history = impaired_credit_history

    @property
    def third_party(self):
        """Gets the third_party of this ConnectIdentitySummary.  # noqa: E501


        :return: The third_party of this ConnectIdentitySummary.  # noqa: E501
        :rtype: ConnectIdentitySummaryThirdParty
        """
        return self._third_party

    @third_party.setter
    def third_party(self, third_party):
        """Sets the third_party of this ConnectIdentitySummary.


        :param third_party: The third_party of this ConnectIdentitySummary.  # noqa: E501
        :type: ConnectIdentitySummaryThirdParty
        """

        self._third_party = third_party

    @property
    def address(self):
        """Gets the address of this ConnectIdentitySummary.  # noqa: E501


        :return: The address of this ConnectIdentitySummary.  # noqa: E501
        :rtype: ConnectIdentitySummaryAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ConnectIdentitySummary.


        :param address: The address of this ConnectIdentitySummary.  # noqa: E501
        :type: ConnectIdentitySummaryAddress
        """

        self._address = address

    @property
    def in_debt(self):
        """Gets the in_debt of this ConnectIdentitySummary.  # noqa: E501


        :return: The in_debt of this ConnectIdentitySummary.  # noqa: E501
        :rtype: ConnectIdentitySummaryInDebt
        """
        return self._in_debt

    @in_debt.setter
    def in_debt(self, in_debt):
        """Sets the in_debt of this ConnectIdentitySummary.


        :param in_debt: The in_debt of this ConnectIdentitySummary.  # noqa: E501
        :type: ConnectIdentitySummaryInDebt
        """

        self._in_debt = in_debt

    @property
    def card_data(self):
        """Gets the card_data of this ConnectIdentitySummary.  # noqa: E501


        :return: The card_data of this ConnectIdentitySummary.  # noqa: E501
        :rtype: ConnectIdentitySummaryCardData
        """
        return self._card_data

    @card_data.setter
    def card_data(self, card_data):
        """Sets the card_data of this ConnectIdentitySummary.


        :param card_data: The card_data of this ConnectIdentitySummary.  # noqa: E501
        :type: ConnectIdentitySummaryCardData
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
        if issubclass(ConnectIdentitySummary, dict):
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
        if not isinstance(other, ConnectIdentitySummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

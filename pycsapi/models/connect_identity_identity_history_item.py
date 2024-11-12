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

class ConnectIdentityIdentityHistoryItem(object):
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
        'unique_id': 'str',
        'customer_id': 'int',
        'user_id': 'int',
        'search_time': 'datetime',
        'search_text': 'str',
        'reference': 'str',
        'has_consumer_int': 'int',
        'has_consumer': 'bool',
        'has_id_int': 'int',
        'has_id': 'bool',
        'has_aml_int': 'int',
        'has_aml': 'bool',
        'has_bank_match_int': 'int',
        'has_bank_match': 'bool',
        'has_aml_with_bank_match_int': 'int',
        'has_aml_with_bank_match': 'bool',
        'consumer_id': 'str',
        'consumer_original_id': 'str',
        'consumer_band1': 'int',
        'consumer_score1': 'int',
        'consumer_band2': 'int',
        'consumer_score2': 'int',
        'gauge_version': 'str',
        'consumer_reason': 'str',
        'linked_report': 'str',
        'id_id': 'str',
        'id_authentication_id': 'str',
        'id_chain_id': 'str',
        'id_validation_id': 'str',
        'id_legacy_id': 'str',
        'id_result': 'ConnectIdentityAmlResultCode',
        'id_has_alerts_int': 'int',
        'id_has_alerts': 'bool',
        'aml_type': 'ConnectIdentityProduct',
        'aml_id': 'str',
        'aml_authentication_id': 'str',
        'aml_chain_id': 'str',
        'aml_validation_id': 'str',
        'aml_legacy_id': 'str',
        'aml_result': 'ConnectIdentityAmlResultCode',
        'aml_has_alerts_int': 'int',
        'aml_has_alerts': 'bool',
        'id_revalidated_int': 'int',
        'id_has_revalidated': 'bool',
        'id_can_revalidate': 'bool',
        'aml_revalidated_int': 'int',
        'aml_has_revalidated': 'bool',
        'aml_can_revalidate': 'bool',
        'input': 'ConnectIdentityAMLSearchRequest',
        'consumer': 'ConnectIdentityTransUnionResult',
        'id': 'ConnectIdentityIdAmlResult',
        'aml': 'ConnectIdentityIdAmlResult'
    }

    attribute_map = {
        'unique_id': 'uniqueId',
        'customer_id': 'customerId',
        'user_id': 'userId',
        'search_time': 'searchTime',
        'search_text': 'searchText',
        'reference': 'reference',
        'has_consumer_int': 'hasConsumerInt',
        'has_consumer': 'hasConsumer',
        'has_id_int': 'hasIdInt',
        'has_id': 'hasId',
        'has_aml_int': 'hasAmlInt',
        'has_aml': 'hasAml',
        'has_bank_match_int': 'hasBankMatchInt',
        'has_bank_match': 'hasBankMatch',
        'has_aml_with_bank_match_int': 'hasAmlWithBankMatchInt',
        'has_aml_with_bank_match': 'hasAmlWithBankMatch',
        'consumer_id': 'consumerId',
        'consumer_original_id': 'consumerOriginalId',
        'consumer_band1': 'consumerBand1',
        'consumer_score1': 'consumerScore1',
        'consumer_band2': 'consumerBand2',
        'consumer_score2': 'consumerScore2',
        'gauge_version': 'gaugeVersion',
        'consumer_reason': 'consumerReason',
        'linked_report': 'linkedReport',
        'id_id': 'idId',
        'id_authentication_id': 'idAuthenticationId',
        'id_chain_id': 'idChainId',
        'id_validation_id': 'idValidationId',
        'id_legacy_id': 'idLegacyID',
        'id_result': 'idResult',
        'id_has_alerts_int': 'idHasAlertsInt',
        'id_has_alerts': 'idHasAlerts',
        'aml_type': 'amlType',
        'aml_id': 'amlId',
        'aml_authentication_id': 'amlAuthenticationId',
        'aml_chain_id': 'amlChainId',
        'aml_validation_id': 'amlValidationId',
        'aml_legacy_id': 'amlLegacyID',
        'aml_result': 'amlResult',
        'aml_has_alerts_int': 'amlHasAlertsInt',
        'aml_has_alerts': 'amlHasAlerts',
        'id_revalidated_int': 'idRevalidatedInt',
        'id_has_revalidated': 'idHasRevalidated',
        'id_can_revalidate': 'idCanRevalidate',
        'aml_revalidated_int': 'amlRevalidatedInt',
        'aml_has_revalidated': 'amlHasRevalidated',
        'aml_can_revalidate': 'amlCanRevalidate',
        'input': 'input',
        'consumer': 'consumer',
        'id': 'id',
        'aml': 'aml'
    }

    def __init__(self, unique_id=None, customer_id=None, user_id=None, search_time=None, search_text=None, reference=None, has_consumer_int=None, has_consumer=None, has_id_int=None, has_id=None, has_aml_int=None, has_aml=None, has_bank_match_int=None, has_bank_match=None, has_aml_with_bank_match_int=None, has_aml_with_bank_match=None, consumer_id=None, consumer_original_id=None, consumer_band1=None, consumer_score1=None, consumer_band2=None, consumer_score2=None, gauge_version=None, consumer_reason=None, linked_report=None, id_id=None, id_authentication_id=None, id_chain_id=None, id_validation_id=None, id_legacy_id=None, id_result=None, id_has_alerts_int=None, id_has_alerts=None, aml_type=None, aml_id=None, aml_authentication_id=None, aml_chain_id=None, aml_validation_id=None, aml_legacy_id=None, aml_result=None, aml_has_alerts_int=None, aml_has_alerts=None, id_revalidated_int=None, id_has_revalidated=None, id_can_revalidate=None, aml_revalidated_int=None, aml_has_revalidated=None, aml_can_revalidate=None, input=None, consumer=None, id=None, aml=None):  # noqa: E501
        """ConnectIdentityIdentityHistoryItem - a model defined in Swagger"""  # noqa: E501
        self._unique_id = None
        self._customer_id = None
        self._user_id = None
        self._search_time = None
        self._search_text = None
        self._reference = None
        self._has_consumer_int = None
        self._has_consumer = None
        self._has_id_int = None
        self._has_id = None
        self._has_aml_int = None
        self._has_aml = None
        self._has_bank_match_int = None
        self._has_bank_match = None
        self._has_aml_with_bank_match_int = None
        self._has_aml_with_bank_match = None
        self._consumer_id = None
        self._consumer_original_id = None
        self._consumer_band1 = None
        self._consumer_score1 = None
        self._consumer_band2 = None
        self._consumer_score2 = None
        self._gauge_version = None
        self._consumer_reason = None
        self._linked_report = None
        self._id_id = None
        self._id_authentication_id = None
        self._id_chain_id = None
        self._id_validation_id = None
        self._id_legacy_id = None
        self._id_result = None
        self._id_has_alerts_int = None
        self._id_has_alerts = None
        self._aml_type = None
        self._aml_id = None
        self._aml_authentication_id = None
        self._aml_chain_id = None
        self._aml_validation_id = None
        self._aml_legacy_id = None
        self._aml_result = None
        self._aml_has_alerts_int = None
        self._aml_has_alerts = None
        self._id_revalidated_int = None
        self._id_has_revalidated = None
        self._id_can_revalidate = None
        self._aml_revalidated_int = None
        self._aml_has_revalidated = None
        self._aml_can_revalidate = None
        self._input = None
        self._consumer = None
        self._id = None
        self._aml = None
        self.discriminator = None
        if unique_id is not None:
            self.unique_id = unique_id
        if customer_id is not None:
            self.customer_id = customer_id
        if user_id is not None:
            self.user_id = user_id
        if search_time is not None:
            self.search_time = search_time
        if search_text is not None:
            self.search_text = search_text
        if reference is not None:
            self.reference = reference
        if has_consumer_int is not None:
            self.has_consumer_int = has_consumer_int
        if has_consumer is not None:
            self.has_consumer = has_consumer
        if has_id_int is not None:
            self.has_id_int = has_id_int
        if has_id is not None:
            self.has_id = has_id
        if has_aml_int is not None:
            self.has_aml_int = has_aml_int
        if has_aml is not None:
            self.has_aml = has_aml
        if has_bank_match_int is not None:
            self.has_bank_match_int = has_bank_match_int
        if has_bank_match is not None:
            self.has_bank_match = has_bank_match
        if has_aml_with_bank_match_int is not None:
            self.has_aml_with_bank_match_int = has_aml_with_bank_match_int
        if has_aml_with_bank_match is not None:
            self.has_aml_with_bank_match = has_aml_with_bank_match
        if consumer_id is not None:
            self.consumer_id = consumer_id
        if consumer_original_id is not None:
            self.consumer_original_id = consumer_original_id
        if consumer_band1 is not None:
            self.consumer_band1 = consumer_band1
        if consumer_score1 is not None:
            self.consumer_score1 = consumer_score1
        if consumer_band2 is not None:
            self.consumer_band2 = consumer_band2
        if consumer_score2 is not None:
            self.consumer_score2 = consumer_score2
        if gauge_version is not None:
            self.gauge_version = gauge_version
        if consumer_reason is not None:
            self.consumer_reason = consumer_reason
        if linked_report is not None:
            self.linked_report = linked_report
        if id_id is not None:
            self.id_id = id_id
        if id_authentication_id is not None:
            self.id_authentication_id = id_authentication_id
        if id_chain_id is not None:
            self.id_chain_id = id_chain_id
        if id_validation_id is not None:
            self.id_validation_id = id_validation_id
        if id_legacy_id is not None:
            self.id_legacy_id = id_legacy_id
        if id_result is not None:
            self.id_result = id_result
        if id_has_alerts_int is not None:
            self.id_has_alerts_int = id_has_alerts_int
        if id_has_alerts is not None:
            self.id_has_alerts = id_has_alerts
        if aml_type is not None:
            self.aml_type = aml_type
        if aml_id is not None:
            self.aml_id = aml_id
        if aml_authentication_id is not None:
            self.aml_authentication_id = aml_authentication_id
        if aml_chain_id is not None:
            self.aml_chain_id = aml_chain_id
        if aml_validation_id is not None:
            self.aml_validation_id = aml_validation_id
        if aml_legacy_id is not None:
            self.aml_legacy_id = aml_legacy_id
        if aml_result is not None:
            self.aml_result = aml_result
        if aml_has_alerts_int is not None:
            self.aml_has_alerts_int = aml_has_alerts_int
        if aml_has_alerts is not None:
            self.aml_has_alerts = aml_has_alerts
        if id_revalidated_int is not None:
            self.id_revalidated_int = id_revalidated_int
        if id_has_revalidated is not None:
            self.id_has_revalidated = id_has_revalidated
        if id_can_revalidate is not None:
            self.id_can_revalidate = id_can_revalidate
        if aml_revalidated_int is not None:
            self.aml_revalidated_int = aml_revalidated_int
        if aml_has_revalidated is not None:
            self.aml_has_revalidated = aml_has_revalidated
        if aml_can_revalidate is not None:
            self.aml_can_revalidate = aml_can_revalidate
        if input is not None:
            self.input = input
        if consumer is not None:
            self.consumer = consumer
        if id is not None:
            self.id = id
        if aml is not None:
            self.aml = aml

    @property
    def unique_id(self):
        """Gets the unique_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The unique_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """Sets the unique_id of this ConnectIdentityIdentityHistoryItem.


        :param unique_id: The unique_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: str
        """

        self._unique_id = unique_id

    @property
    def customer_id(self):
        """Gets the customer_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The customer_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: int
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ConnectIdentityIdentityHistoryItem.


        :param customer_id: The customer_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: int
        """

        self._customer_id = customer_id

    @property
    def user_id(self):
        """Gets the user_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The user_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ConnectIdentityIdentityHistoryItem.


        :param user_id: The user_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def search_time(self):
        """Gets the search_time of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The search_time of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: datetime
        """
        return self._search_time

    @search_time.setter
    def search_time(self, search_time):
        """Sets the search_time of this ConnectIdentityIdentityHistoryItem.


        :param search_time: The search_time of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: datetime
        """

        self._search_time = search_time

    @property
    def search_text(self):
        """Gets the search_text of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The search_text of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._search_text

    @search_text.setter
    def search_text(self, search_text):
        """Sets the search_text of this ConnectIdentityIdentityHistoryItem.


        :param search_text: The search_text of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: str
        """

        self._search_text = search_text

    @property
    def reference(self):
        """Gets the reference of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The reference of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this ConnectIdentityIdentityHistoryItem.


        :param reference: The reference of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def has_consumer_int(self):
        """Gets the has_consumer_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The has_consumer_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: int
        """
        return self._has_consumer_int

    @has_consumer_int.setter
    def has_consumer_int(self, has_consumer_int):
        """Sets the has_consumer_int of this ConnectIdentityIdentityHistoryItem.


        :param has_consumer_int: The has_consumer_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: int
        """

        self._has_consumer_int = has_consumer_int

    @property
    def has_consumer(self):
        """Gets the has_consumer of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The has_consumer of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: bool
        """
        return self._has_consumer

    @has_consumer.setter
    def has_consumer(self, has_consumer):
        """Sets the has_consumer of this ConnectIdentityIdentityHistoryItem.


        :param has_consumer: The has_consumer of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: bool
        """

        self._has_consumer = has_consumer

    @property
    def has_id_int(self):
        """Gets the has_id_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The has_id_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: int
        """
        return self._has_id_int

    @has_id_int.setter
    def has_id_int(self, has_id_int):
        """Sets the has_id_int of this ConnectIdentityIdentityHistoryItem.


        :param has_id_int: The has_id_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: int
        """

        self._has_id_int = has_id_int

    @property
    def has_id(self):
        """Gets the has_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The has_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: bool
        """
        return self._has_id

    @has_id.setter
    def has_id(self, has_id):
        """Sets the has_id of this ConnectIdentityIdentityHistoryItem.


        :param has_id: The has_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: bool
        """

        self._has_id = has_id

    @property
    def has_aml_int(self):
        """Gets the has_aml_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The has_aml_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: int
        """
        return self._has_aml_int

    @has_aml_int.setter
    def has_aml_int(self, has_aml_int):
        """Sets the has_aml_int of this ConnectIdentityIdentityHistoryItem.


        :param has_aml_int: The has_aml_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: int
        """

        self._has_aml_int = has_aml_int

    @property
    def has_aml(self):
        """Gets the has_aml of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The has_aml of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: bool
        """
        return self._has_aml

    @has_aml.setter
    def has_aml(self, has_aml):
        """Sets the has_aml of this ConnectIdentityIdentityHistoryItem.


        :param has_aml: The has_aml of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: bool
        """

        self._has_aml = has_aml

    @property
    def has_bank_match_int(self):
        """Gets the has_bank_match_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The has_bank_match_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: int
        """
        return self._has_bank_match_int

    @has_bank_match_int.setter
    def has_bank_match_int(self, has_bank_match_int):
        """Sets the has_bank_match_int of this ConnectIdentityIdentityHistoryItem.


        :param has_bank_match_int: The has_bank_match_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: int
        """

        self._has_bank_match_int = has_bank_match_int

    @property
    def has_bank_match(self):
        """Gets the has_bank_match of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The has_bank_match of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: bool
        """
        return self._has_bank_match

    @has_bank_match.setter
    def has_bank_match(self, has_bank_match):
        """Sets the has_bank_match of this ConnectIdentityIdentityHistoryItem.


        :param has_bank_match: The has_bank_match of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: bool
        """

        self._has_bank_match = has_bank_match

    @property
    def has_aml_with_bank_match_int(self):
        """Gets the has_aml_with_bank_match_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The has_aml_with_bank_match_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: int
        """
        return self._has_aml_with_bank_match_int

    @has_aml_with_bank_match_int.setter
    def has_aml_with_bank_match_int(self, has_aml_with_bank_match_int):
        """Sets the has_aml_with_bank_match_int of this ConnectIdentityIdentityHistoryItem.


        :param has_aml_with_bank_match_int: The has_aml_with_bank_match_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: int
        """

        self._has_aml_with_bank_match_int = has_aml_with_bank_match_int

    @property
    def has_aml_with_bank_match(self):
        """Gets the has_aml_with_bank_match of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The has_aml_with_bank_match of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: bool
        """
        return self._has_aml_with_bank_match

    @has_aml_with_bank_match.setter
    def has_aml_with_bank_match(self, has_aml_with_bank_match):
        """Sets the has_aml_with_bank_match of this ConnectIdentityIdentityHistoryItem.


        :param has_aml_with_bank_match: The has_aml_with_bank_match of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: bool
        """

        self._has_aml_with_bank_match = has_aml_with_bank_match

    @property
    def consumer_id(self):
        """Gets the consumer_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The consumer_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._consumer_id

    @consumer_id.setter
    def consumer_id(self, consumer_id):
        """Sets the consumer_id of this ConnectIdentityIdentityHistoryItem.


        :param consumer_id: The consumer_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: str
        """

        self._consumer_id = consumer_id

    @property
    def consumer_original_id(self):
        """Gets the consumer_original_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The consumer_original_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._consumer_original_id

    @consumer_original_id.setter
    def consumer_original_id(self, consumer_original_id):
        """Sets the consumer_original_id of this ConnectIdentityIdentityHistoryItem.


        :param consumer_original_id: The consumer_original_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: str
        """

        self._consumer_original_id = consumer_original_id

    @property
    def consumer_band1(self):
        """Gets the consumer_band1 of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The consumer_band1 of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: int
        """
        return self._consumer_band1

    @consumer_band1.setter
    def consumer_band1(self, consumer_band1):
        """Sets the consumer_band1 of this ConnectIdentityIdentityHistoryItem.


        :param consumer_band1: The consumer_band1 of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: int
        """

        self._consumer_band1 = consumer_band1

    @property
    def consumer_score1(self):
        """Gets the consumer_score1 of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The consumer_score1 of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: int
        """
        return self._consumer_score1

    @consumer_score1.setter
    def consumer_score1(self, consumer_score1):
        """Sets the consumer_score1 of this ConnectIdentityIdentityHistoryItem.


        :param consumer_score1: The consumer_score1 of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: int
        """

        self._consumer_score1 = consumer_score1

    @property
    def consumer_band2(self):
        """Gets the consumer_band2 of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The consumer_band2 of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: int
        """
        return self._consumer_band2

    @consumer_band2.setter
    def consumer_band2(self, consumer_band2):
        """Sets the consumer_band2 of this ConnectIdentityIdentityHistoryItem.


        :param consumer_band2: The consumer_band2 of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: int
        """

        self._consumer_band2 = consumer_band2

    @property
    def consumer_score2(self):
        """Gets the consumer_score2 of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The consumer_score2 of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: int
        """
        return self._consumer_score2

    @consumer_score2.setter
    def consumer_score2(self, consumer_score2):
        """Sets the consumer_score2 of this ConnectIdentityIdentityHistoryItem.


        :param consumer_score2: The consumer_score2 of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: int
        """

        self._consumer_score2 = consumer_score2

    @property
    def gauge_version(self):
        """Gets the gauge_version of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The gauge_version of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._gauge_version

    @gauge_version.setter
    def gauge_version(self, gauge_version):
        """Sets the gauge_version of this ConnectIdentityIdentityHistoryItem.


        :param gauge_version: The gauge_version of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: str
        """

        self._gauge_version = gauge_version

    @property
    def consumer_reason(self):
        """Gets the consumer_reason of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The consumer_reason of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._consumer_reason

    @consumer_reason.setter
    def consumer_reason(self, consumer_reason):
        """Sets the consumer_reason of this ConnectIdentityIdentityHistoryItem.


        :param consumer_reason: The consumer_reason of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: str
        """

        self._consumer_reason = consumer_reason

    @property
    def linked_report(self):
        """Gets the linked_report of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The linked_report of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._linked_report

    @linked_report.setter
    def linked_report(self, linked_report):
        """Sets the linked_report of this ConnectIdentityIdentityHistoryItem.


        :param linked_report: The linked_report of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: str
        """

        self._linked_report = linked_report

    @property
    def id_id(self):
        """Gets the id_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The id_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._id_id

    @id_id.setter
    def id_id(self, id_id):
        """Sets the id_id of this ConnectIdentityIdentityHistoryItem.


        :param id_id: The id_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: str
        """

        self._id_id = id_id

    @property
    def id_authentication_id(self):
        """Gets the id_authentication_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The id_authentication_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._id_authentication_id

    @id_authentication_id.setter
    def id_authentication_id(self, id_authentication_id):
        """Sets the id_authentication_id of this ConnectIdentityIdentityHistoryItem.


        :param id_authentication_id: The id_authentication_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: str
        """

        self._id_authentication_id = id_authentication_id

    @property
    def id_chain_id(self):
        """Gets the id_chain_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The id_chain_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._id_chain_id

    @id_chain_id.setter
    def id_chain_id(self, id_chain_id):
        """Sets the id_chain_id of this ConnectIdentityIdentityHistoryItem.


        :param id_chain_id: The id_chain_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: str
        """

        self._id_chain_id = id_chain_id

    @property
    def id_validation_id(self):
        """Gets the id_validation_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The id_validation_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._id_validation_id

    @id_validation_id.setter
    def id_validation_id(self, id_validation_id):
        """Sets the id_validation_id of this ConnectIdentityIdentityHistoryItem.


        :param id_validation_id: The id_validation_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: str
        """

        self._id_validation_id = id_validation_id

    @property
    def id_legacy_id(self):
        """Gets the id_legacy_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The id_legacy_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._id_legacy_id

    @id_legacy_id.setter
    def id_legacy_id(self, id_legacy_id):
        """Sets the id_legacy_id of this ConnectIdentityIdentityHistoryItem.


        :param id_legacy_id: The id_legacy_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: str
        """

        self._id_legacy_id = id_legacy_id

    @property
    def id_result(self):
        """Gets the id_result of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The id_result of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: ConnectIdentityAmlResultCode
        """
        return self._id_result

    @id_result.setter
    def id_result(self, id_result):
        """Sets the id_result of this ConnectIdentityIdentityHistoryItem.


        :param id_result: The id_result of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: ConnectIdentityAmlResultCode
        """

        self._id_result = id_result

    @property
    def id_has_alerts_int(self):
        """Gets the id_has_alerts_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The id_has_alerts_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: int
        """
        return self._id_has_alerts_int

    @id_has_alerts_int.setter
    def id_has_alerts_int(self, id_has_alerts_int):
        """Sets the id_has_alerts_int of this ConnectIdentityIdentityHistoryItem.


        :param id_has_alerts_int: The id_has_alerts_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: int
        """

        self._id_has_alerts_int = id_has_alerts_int

    @property
    def id_has_alerts(self):
        """Gets the id_has_alerts of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The id_has_alerts of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: bool
        """
        return self._id_has_alerts

    @id_has_alerts.setter
    def id_has_alerts(self, id_has_alerts):
        """Sets the id_has_alerts of this ConnectIdentityIdentityHistoryItem.


        :param id_has_alerts: The id_has_alerts of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: bool
        """

        self._id_has_alerts = id_has_alerts

    @property
    def aml_type(self):
        """Gets the aml_type of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The aml_type of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: ConnectIdentityProduct
        """
        return self._aml_type

    @aml_type.setter
    def aml_type(self, aml_type):
        """Sets the aml_type of this ConnectIdentityIdentityHistoryItem.


        :param aml_type: The aml_type of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: ConnectIdentityProduct
        """

        self._aml_type = aml_type

    @property
    def aml_id(self):
        """Gets the aml_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The aml_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._aml_id

    @aml_id.setter
    def aml_id(self, aml_id):
        """Sets the aml_id of this ConnectIdentityIdentityHistoryItem.


        :param aml_id: The aml_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: str
        """

        self._aml_id = aml_id

    @property
    def aml_authentication_id(self):
        """Gets the aml_authentication_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The aml_authentication_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._aml_authentication_id

    @aml_authentication_id.setter
    def aml_authentication_id(self, aml_authentication_id):
        """Sets the aml_authentication_id of this ConnectIdentityIdentityHistoryItem.


        :param aml_authentication_id: The aml_authentication_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: str
        """

        self._aml_authentication_id = aml_authentication_id

    @property
    def aml_chain_id(self):
        """Gets the aml_chain_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The aml_chain_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._aml_chain_id

    @aml_chain_id.setter
    def aml_chain_id(self, aml_chain_id):
        """Sets the aml_chain_id of this ConnectIdentityIdentityHistoryItem.


        :param aml_chain_id: The aml_chain_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: str
        """

        self._aml_chain_id = aml_chain_id

    @property
    def aml_validation_id(self):
        """Gets the aml_validation_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The aml_validation_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._aml_validation_id

    @aml_validation_id.setter
    def aml_validation_id(self, aml_validation_id):
        """Sets the aml_validation_id of this ConnectIdentityIdentityHistoryItem.


        :param aml_validation_id: The aml_validation_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: str
        """

        self._aml_validation_id = aml_validation_id

    @property
    def aml_legacy_id(self):
        """Gets the aml_legacy_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The aml_legacy_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: str
        """
        return self._aml_legacy_id

    @aml_legacy_id.setter
    def aml_legacy_id(self, aml_legacy_id):
        """Sets the aml_legacy_id of this ConnectIdentityIdentityHistoryItem.


        :param aml_legacy_id: The aml_legacy_id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: str
        """

        self._aml_legacy_id = aml_legacy_id

    @property
    def aml_result(self):
        """Gets the aml_result of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The aml_result of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: ConnectIdentityAmlResultCode
        """
        return self._aml_result

    @aml_result.setter
    def aml_result(self, aml_result):
        """Sets the aml_result of this ConnectIdentityIdentityHistoryItem.


        :param aml_result: The aml_result of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: ConnectIdentityAmlResultCode
        """

        self._aml_result = aml_result

    @property
    def aml_has_alerts_int(self):
        """Gets the aml_has_alerts_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The aml_has_alerts_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: int
        """
        return self._aml_has_alerts_int

    @aml_has_alerts_int.setter
    def aml_has_alerts_int(self, aml_has_alerts_int):
        """Sets the aml_has_alerts_int of this ConnectIdentityIdentityHistoryItem.


        :param aml_has_alerts_int: The aml_has_alerts_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: int
        """

        self._aml_has_alerts_int = aml_has_alerts_int

    @property
    def aml_has_alerts(self):
        """Gets the aml_has_alerts of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The aml_has_alerts of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: bool
        """
        return self._aml_has_alerts

    @aml_has_alerts.setter
    def aml_has_alerts(self, aml_has_alerts):
        """Sets the aml_has_alerts of this ConnectIdentityIdentityHistoryItem.


        :param aml_has_alerts: The aml_has_alerts of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: bool
        """

        self._aml_has_alerts = aml_has_alerts

    @property
    def id_revalidated_int(self):
        """Gets the id_revalidated_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The id_revalidated_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: int
        """
        return self._id_revalidated_int

    @id_revalidated_int.setter
    def id_revalidated_int(self, id_revalidated_int):
        """Sets the id_revalidated_int of this ConnectIdentityIdentityHistoryItem.


        :param id_revalidated_int: The id_revalidated_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: int
        """

        self._id_revalidated_int = id_revalidated_int

    @property
    def id_has_revalidated(self):
        """Gets the id_has_revalidated of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The id_has_revalidated of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: bool
        """
        return self._id_has_revalidated

    @id_has_revalidated.setter
    def id_has_revalidated(self, id_has_revalidated):
        """Sets the id_has_revalidated of this ConnectIdentityIdentityHistoryItem.


        :param id_has_revalidated: The id_has_revalidated of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: bool
        """

        self._id_has_revalidated = id_has_revalidated

    @property
    def id_can_revalidate(self):
        """Gets the id_can_revalidate of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The id_can_revalidate of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: bool
        """
        return self._id_can_revalidate

    @id_can_revalidate.setter
    def id_can_revalidate(self, id_can_revalidate):
        """Sets the id_can_revalidate of this ConnectIdentityIdentityHistoryItem.


        :param id_can_revalidate: The id_can_revalidate of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: bool
        """

        self._id_can_revalidate = id_can_revalidate

    @property
    def aml_revalidated_int(self):
        """Gets the aml_revalidated_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The aml_revalidated_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: int
        """
        return self._aml_revalidated_int

    @aml_revalidated_int.setter
    def aml_revalidated_int(self, aml_revalidated_int):
        """Sets the aml_revalidated_int of this ConnectIdentityIdentityHistoryItem.


        :param aml_revalidated_int: The aml_revalidated_int of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: int
        """

        self._aml_revalidated_int = aml_revalidated_int

    @property
    def aml_has_revalidated(self):
        """Gets the aml_has_revalidated of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The aml_has_revalidated of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: bool
        """
        return self._aml_has_revalidated

    @aml_has_revalidated.setter
    def aml_has_revalidated(self, aml_has_revalidated):
        """Sets the aml_has_revalidated of this ConnectIdentityIdentityHistoryItem.


        :param aml_has_revalidated: The aml_has_revalidated of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: bool
        """

        self._aml_has_revalidated = aml_has_revalidated

    @property
    def aml_can_revalidate(self):
        """Gets the aml_can_revalidate of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The aml_can_revalidate of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: bool
        """
        return self._aml_can_revalidate

    @aml_can_revalidate.setter
    def aml_can_revalidate(self, aml_can_revalidate):
        """Sets the aml_can_revalidate of this ConnectIdentityIdentityHistoryItem.


        :param aml_can_revalidate: The aml_can_revalidate of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: bool
        """

        self._aml_can_revalidate = aml_can_revalidate

    @property
    def input(self):
        """Gets the input of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The input of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: ConnectIdentityAMLSearchRequest
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this ConnectIdentityIdentityHistoryItem.


        :param input: The input of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: ConnectIdentityAMLSearchRequest
        """

        self._input = input

    @property
    def consumer(self):
        """Gets the consumer of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The consumer of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: ConnectIdentityTransUnionResult
        """
        return self._consumer

    @consumer.setter
    def consumer(self, consumer):
        """Sets the consumer of this ConnectIdentityIdentityHistoryItem.


        :param consumer: The consumer of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: ConnectIdentityTransUnionResult
        """

        self._consumer = consumer

    @property
    def id(self):
        """Gets the id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: ConnectIdentityIdAmlResult
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConnectIdentityIdentityHistoryItem.


        :param id: The id of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: ConnectIdentityIdAmlResult
        """

        self._id = id

    @property
    def aml(self):
        """Gets the aml of this ConnectIdentityIdentityHistoryItem.  # noqa: E501


        :return: The aml of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :rtype: ConnectIdentityIdAmlResult
        """
        return self._aml

    @aml.setter
    def aml(self, aml):
        """Sets the aml of this ConnectIdentityIdentityHistoryItem.


        :param aml: The aml of this ConnectIdentityIdentityHistoryItem.  # noqa: E501
        :type: ConnectIdentityIdAmlResult
        """

        self._aml = aml

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
        if issubclass(ConnectIdentityIdentityHistoryItem, dict):
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
        if not isinstance(other, ConnectIdentityIdentityHistoryItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

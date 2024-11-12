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

class ConnectIdentitySearchResult(object):
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
        'correlation_id': 'str',
        'unique_id': 'str',
        'input': 'ConnectIdentityAMLSearchRequest',
        'common': 'ConnectIdentityCommonResult',
        'consumer': 'ConnectIdentitySupplierResult',
        'id': 'ConnectIdentitySupplierResult',
        'aml_result': 'ConnectIdentitySupplierResult',
        'bank_match': 'ConnectIdentitySupplierResult',
        'picklist': 'list[ConnectIdentityPicklist]',
        'message': 'str',
        'errors': 'dict(str, list[str])'
    }

    attribute_map = {
        'correlation_id': 'correlationId',
        'unique_id': 'uniqueId',
        'input': 'input',
        'common': 'common',
        'consumer': 'consumer',
        'id': 'id',
        'aml_result': 'amlResult',
        'bank_match': 'bankMatch',
        'picklist': 'picklist',
        'message': 'message',
        'errors': 'errors'
    }

    def __init__(self, correlation_id=None, unique_id=None, input=None, common=None, consumer=None, id=None, aml_result=None, bank_match=None, picklist=None, message=None, errors=None):  # noqa: E501
        """ConnectIdentitySearchResult - a model defined in Swagger"""  # noqa: E501
        self._correlation_id = None
        self._unique_id = None
        self._input = None
        self._common = None
        self._consumer = None
        self._id = None
        self._aml_result = None
        self._bank_match = None
        self._picklist = None
        self._message = None
        self._errors = None
        self.discriminator = None
        if correlation_id is not None:
            self.correlation_id = correlation_id
        if unique_id is not None:
            self.unique_id = unique_id
        if input is not None:
            self.input = input
        if common is not None:
            self.common = common
        if consumer is not None:
            self.consumer = consumer
        if id is not None:
            self.id = id
        if aml_result is not None:
            self.aml_result = aml_result
        if bank_match is not None:
            self.bank_match = bank_match
        if picklist is not None:
            self.picklist = picklist
        if message is not None:
            self.message = message
        if errors is not None:
            self.errors = errors

    @property
    def correlation_id(self):
        """Gets the correlation_id of this ConnectIdentitySearchResult.  # noqa: E501

        A unique ID assigned to this request.  # noqa: E501

        :return: The correlation_id of this ConnectIdentitySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this ConnectIdentitySearchResult.

        A unique ID assigned to this request.  # noqa: E501

        :param correlation_id: The correlation_id of this ConnectIdentitySearchResult.  # noqa: E501
        :type: str
        """

        self._correlation_id = correlation_id

    @property
    def unique_id(self):
        """Gets the unique_id of this ConnectIdentitySearchResult.  # noqa: E501


        :return: The unique_id of this ConnectIdentitySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """Sets the unique_id of this ConnectIdentitySearchResult.


        :param unique_id: The unique_id of this ConnectIdentitySearchResult.  # noqa: E501
        :type: str
        """

        self._unique_id = unique_id

    @property
    def input(self):
        """Gets the input of this ConnectIdentitySearchResult.  # noqa: E501


        :return: The input of this ConnectIdentitySearchResult.  # noqa: E501
        :rtype: ConnectIdentityAMLSearchRequest
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this ConnectIdentitySearchResult.


        :param input: The input of this ConnectIdentitySearchResult.  # noqa: E501
        :type: ConnectIdentityAMLSearchRequest
        """

        self._input = input

    @property
    def common(self):
        """Gets the common of this ConnectIdentitySearchResult.  # noqa: E501


        :return: The common of this ConnectIdentitySearchResult.  # noqa: E501
        :rtype: ConnectIdentityCommonResult
        """
        return self._common

    @common.setter
    def common(self, common):
        """Sets the common of this ConnectIdentitySearchResult.


        :param common: The common of this ConnectIdentitySearchResult.  # noqa: E501
        :type: ConnectIdentityCommonResult
        """

        self._common = common

    @property
    def consumer(self):
        """Gets the consumer of this ConnectIdentitySearchResult.  # noqa: E501


        :return: The consumer of this ConnectIdentitySearchResult.  # noqa: E501
        :rtype: ConnectIdentitySupplierResult
        """
        return self._consumer

    @consumer.setter
    def consumer(self, consumer):
        """Sets the consumer of this ConnectIdentitySearchResult.


        :param consumer: The consumer of this ConnectIdentitySearchResult.  # noqa: E501
        :type: ConnectIdentitySupplierResult
        """

        self._consumer = consumer

    @property
    def id(self):
        """Gets the id of this ConnectIdentitySearchResult.  # noqa: E501


        :return: The id of this ConnectIdentitySearchResult.  # noqa: E501
        :rtype: ConnectIdentitySupplierResult
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConnectIdentitySearchResult.


        :param id: The id of this ConnectIdentitySearchResult.  # noqa: E501
        :type: ConnectIdentitySupplierResult
        """

        self._id = id

    @property
    def aml_result(self):
        """Gets the aml_result of this ConnectIdentitySearchResult.  # noqa: E501


        :return: The aml_result of this ConnectIdentitySearchResult.  # noqa: E501
        :rtype: ConnectIdentitySupplierResult
        """
        return self._aml_result

    @aml_result.setter
    def aml_result(self, aml_result):
        """Sets the aml_result of this ConnectIdentitySearchResult.


        :param aml_result: The aml_result of this ConnectIdentitySearchResult.  # noqa: E501
        :type: ConnectIdentitySupplierResult
        """

        self._aml_result = aml_result

    @property
    def bank_match(self):
        """Gets the bank_match of this ConnectIdentitySearchResult.  # noqa: E501


        :return: The bank_match of this ConnectIdentitySearchResult.  # noqa: E501
        :rtype: ConnectIdentitySupplierResult
        """
        return self._bank_match

    @bank_match.setter
    def bank_match(self, bank_match):
        """Sets the bank_match of this ConnectIdentitySearchResult.


        :param bank_match: The bank_match of this ConnectIdentitySearchResult.  # noqa: E501
        :type: ConnectIdentitySupplierResult
        """

        self._bank_match = bank_match

    @property
    def picklist(self):
        """Gets the picklist of this ConnectIdentitySearchResult.  # noqa: E501


        :return: The picklist of this ConnectIdentitySearchResult.  # noqa: E501
        :rtype: list[ConnectIdentityPicklist]
        """
        return self._picklist

    @picklist.setter
    def picklist(self, picklist):
        """Sets the picklist of this ConnectIdentitySearchResult.


        :param picklist: The picklist of this ConnectIdentitySearchResult.  # noqa: E501
        :type: list[ConnectIdentityPicklist]
        """

        self._picklist = picklist

    @property
    def message(self):
        """Gets the message of this ConnectIdentitySearchResult.  # noqa: E501


        :return: The message of this ConnectIdentitySearchResult.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ConnectIdentitySearchResult.


        :param message: The message of this ConnectIdentitySearchResult.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def errors(self):
        """Gets the errors of this ConnectIdentitySearchResult.  # noqa: E501


        :return: The errors of this ConnectIdentitySearchResult.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ConnectIdentitySearchResult.


        :param errors: The errors of this ConnectIdentitySearchResult.  # noqa: E501
        :type: dict(str, list[str])
        """

        self._errors = errors

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
        if issubclass(ConnectIdentitySearchResult, dict):
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
        if not isinstance(other, ConnectIdentitySearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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

class GBLocalSolutionGetHistoryRequestResponse(object):
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
        'supplier_request_data': 'GBLocalSolutionGetHistoryRequestResponseSupplierRequestData',
        'customer_reference': 'str',
        'supplier_response': 'GBLocalSolutionGetHistoryRequestResponseSupplierResponse',
        'request_datetime': 'str',
        'request_id': 'str'
    }

    attribute_map = {
        'supplier_request_data': 'supplierRequestData',
        'customer_reference': 'customerReference',
        'supplier_response': 'supplierResponse',
        'request_datetime': 'requestDatetime',
        'request_id': 'requestId'
    }

    def __init__(self, supplier_request_data=None, customer_reference=None, supplier_response=None, request_datetime=None, request_id=None):  # noqa: E501
        """GBLocalSolutionGetHistoryRequestResponse - a model defined in Swagger"""  # noqa: E501
        self._supplier_request_data = None
        self._customer_reference = None
        self._supplier_response = None
        self._request_datetime = None
        self._request_id = None
        self.discriminator = None
        if supplier_request_data is not None:
            self.supplier_request_data = supplier_request_data
        if customer_reference is not None:
            self.customer_reference = customer_reference
        if supplier_response is not None:
            self.supplier_response = supplier_response
        if request_datetime is not None:
            self.request_datetime = request_datetime
        if request_id is not None:
            self.request_id = request_id

    @property
    def supplier_request_data(self):
        """Gets the supplier_request_data of this GBLocalSolutionGetHistoryRequestResponse.  # noqa: E501


        :return: The supplier_request_data of this GBLocalSolutionGetHistoryRequestResponse.  # noqa: E501
        :rtype: GBLocalSolutionGetHistoryRequestResponseSupplierRequestData
        """
        return self._supplier_request_data

    @supplier_request_data.setter
    def supplier_request_data(self, supplier_request_data):
        """Sets the supplier_request_data of this GBLocalSolutionGetHistoryRequestResponse.


        :param supplier_request_data: The supplier_request_data of this GBLocalSolutionGetHistoryRequestResponse.  # noqa: E501
        :type: GBLocalSolutionGetHistoryRequestResponseSupplierRequestData
        """

        self._supplier_request_data = supplier_request_data

    @property
    def customer_reference(self):
        """Gets the customer_reference of this GBLocalSolutionGetHistoryRequestResponse.  # noqa: E501

        Your Customer reference  # noqa: E501

        :return: The customer_reference of this GBLocalSolutionGetHistoryRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._customer_reference

    @customer_reference.setter
    def customer_reference(self, customer_reference):
        """Sets the customer_reference of this GBLocalSolutionGetHistoryRequestResponse.

        Your Customer reference  # noqa: E501

        :param customer_reference: The customer_reference of this GBLocalSolutionGetHistoryRequestResponse.  # noqa: E501
        :type: str
        """

        self._customer_reference = customer_reference

    @property
    def supplier_response(self):
        """Gets the supplier_response of this GBLocalSolutionGetHistoryRequestResponse.  # noqa: E501


        :return: The supplier_response of this GBLocalSolutionGetHistoryRequestResponse.  # noqa: E501
        :rtype: GBLocalSolutionGetHistoryRequestResponseSupplierResponse
        """
        return self._supplier_response

    @supplier_response.setter
    def supplier_response(self, supplier_response):
        """Sets the supplier_response of this GBLocalSolutionGetHistoryRequestResponse.


        :param supplier_response: The supplier_response of this GBLocalSolutionGetHistoryRequestResponse.  # noqa: E501
        :type: GBLocalSolutionGetHistoryRequestResponseSupplierResponse
        """

        self._supplier_response = supplier_response

    @property
    def request_datetime(self):
        """Gets the request_datetime of this GBLocalSolutionGetHistoryRequestResponse.  # noqa: E501

        The date time this request was returned  # noqa: E501

        :return: The request_datetime of this GBLocalSolutionGetHistoryRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_datetime

    @request_datetime.setter
    def request_datetime(self, request_datetime):
        """Sets the request_datetime of this GBLocalSolutionGetHistoryRequestResponse.

        The date time this request was returned  # noqa: E501

        :param request_datetime: The request_datetime of this GBLocalSolutionGetHistoryRequestResponse.  # noqa: E501
        :type: str
        """

        self._request_datetime = request_datetime

    @property
    def request_id(self):
        """Gets the request_id of this GBLocalSolutionGetHistoryRequestResponse.  # noqa: E501

        A unique reference to your request used for querying the endpoints where {id} is required  # noqa: E501

        :return: The request_id of this GBLocalSolutionGetHistoryRequestResponse.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this GBLocalSolutionGetHistoryRequestResponse.

        A unique reference to your request used for querying the endpoints where {id} is required  # noqa: E501

        :param request_id: The request_id of this GBLocalSolutionGetHistoryRequestResponse.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

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
        if issubclass(GBLocalSolutionGetHistoryRequestResponse, dict):
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
        if not isinstance(other, GBLocalSolutionGetHistoryRequestResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

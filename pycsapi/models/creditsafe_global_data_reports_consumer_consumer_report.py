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

class CreditsafeGlobalDataReportsConsumerConsumerReport(object):
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
        'consumer_information': 'CreditsafeGlobalDataReportsConsumerConsumerInformation',
        'incomes': 'list[CreditsafeGlobalDataReportsConsumerConsumerIncome]',
        'registered_property': 'int',
        'registered_housing_share': 'int',
        'directorships': 'list[CreditsafeGlobalDataReportsConsumerConsumerDirectorship]',
        'payment_remarks': 'list[CreditsafeGlobalDataReportsConsumerConsumerPaymentSummary]',
        'payment_remarks_details': 'list[CreditsafeGlobalDataReportsConsumerConsumerRemarkOfPayment]',
        'voluntary_pledges': 'list[CreditsafeGlobalDataReportsConsumerConsumerRemarkOfPayment]',
        'consumer_rating': 'CreditsafeGlobalDataReportsConsumerConsumerCreditScore',
        'additional_information': 'CreditsafeGlobalDataReportsConsumerConsumerAdditionalInformation'
    }

    attribute_map = {
        'consumer_information': 'consumerInformation',
        'incomes': 'incomes',
        'registered_property': 'registeredProperty',
        'registered_housing_share': 'registeredHousingShare',
        'directorships': 'directorships',
        'payment_remarks': 'paymentRemarks',
        'payment_remarks_details': 'paymentRemarksDetails',
        'voluntary_pledges': 'voluntaryPledges',
        'consumer_rating': 'consumerRating',
        'additional_information': 'additionalInformation'
    }

    def __init__(self, consumer_information=None, incomes=None, registered_property=None, registered_housing_share=None, directorships=None, payment_remarks=None, payment_remarks_details=None, voluntary_pledges=None, consumer_rating=None, additional_information=None):  # noqa: E501
        """CreditsafeGlobalDataReportsConsumerConsumerReport - a model defined in Swagger"""  # noqa: E501
        self._consumer_information = None
        self._incomes = None
        self._registered_property = None
        self._registered_housing_share = None
        self._directorships = None
        self._payment_remarks = None
        self._payment_remarks_details = None
        self._voluntary_pledges = None
        self._consumer_rating = None
        self._additional_information = None
        self.discriminator = None
        if consumer_information is not None:
            self.consumer_information = consumer_information
        if incomes is not None:
            self.incomes = incomes
        if registered_property is not None:
            self.registered_property = registered_property
        if registered_housing_share is not None:
            self.registered_housing_share = registered_housing_share
        if directorships is not None:
            self.directorships = directorships
        if payment_remarks is not None:
            self.payment_remarks = payment_remarks
        if payment_remarks_details is not None:
            self.payment_remarks_details = payment_remarks_details
        if voluntary_pledges is not None:
            self.voluntary_pledges = voluntary_pledges
        if consumer_rating is not None:
            self.consumer_rating = consumer_rating
        if additional_information is not None:
            self.additional_information = additional_information

    @property
    def consumer_information(self):
        """Gets the consumer_information of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501


        :return: The consumer_information of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsConsumerConsumerInformation
        """
        return self._consumer_information

    @consumer_information.setter
    def consumer_information(self, consumer_information):
        """Sets the consumer_information of this CreditsafeGlobalDataReportsConsumerConsumerReport.


        :param consumer_information: The consumer_information of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501
        :type: CreditsafeGlobalDataReportsConsumerConsumerInformation
        """

        self._consumer_information = consumer_information

    @property
    def incomes(self):
        """Gets the incomes of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501


        :return: The incomes of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501
        :rtype: list[CreditsafeGlobalDataReportsConsumerConsumerIncome]
        """
        return self._incomes

    @incomes.setter
    def incomes(self, incomes):
        """Sets the incomes of this CreditsafeGlobalDataReportsConsumerConsumerReport.


        :param incomes: The incomes of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501
        :type: list[CreditsafeGlobalDataReportsConsumerConsumerIncome]
        """

        self._incomes = incomes

    @property
    def registered_property(self):
        """Gets the registered_property of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501


        :return: The registered_property of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501
        :rtype: int
        """
        return self._registered_property

    @registered_property.setter
    def registered_property(self, registered_property):
        """Sets the registered_property of this CreditsafeGlobalDataReportsConsumerConsumerReport.


        :param registered_property: The registered_property of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501
        :type: int
        """

        self._registered_property = registered_property

    @property
    def registered_housing_share(self):
        """Gets the registered_housing_share of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501


        :return: The registered_housing_share of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501
        :rtype: int
        """
        return self._registered_housing_share

    @registered_housing_share.setter
    def registered_housing_share(self, registered_housing_share):
        """Sets the registered_housing_share of this CreditsafeGlobalDataReportsConsumerConsumerReport.


        :param registered_housing_share: The registered_housing_share of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501
        :type: int
        """

        self._registered_housing_share = registered_housing_share

    @property
    def directorships(self):
        """Gets the directorships of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501


        :return: The directorships of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501
        :rtype: list[CreditsafeGlobalDataReportsConsumerConsumerDirectorship]
        """
        return self._directorships

    @directorships.setter
    def directorships(self, directorships):
        """Sets the directorships of this CreditsafeGlobalDataReportsConsumerConsumerReport.


        :param directorships: The directorships of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501
        :type: list[CreditsafeGlobalDataReportsConsumerConsumerDirectorship]
        """

        self._directorships = directorships

    @property
    def payment_remarks(self):
        """Gets the payment_remarks of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501


        :return: The payment_remarks of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501
        :rtype: list[CreditsafeGlobalDataReportsConsumerConsumerPaymentSummary]
        """
        return self._payment_remarks

    @payment_remarks.setter
    def payment_remarks(self, payment_remarks):
        """Sets the payment_remarks of this CreditsafeGlobalDataReportsConsumerConsumerReport.


        :param payment_remarks: The payment_remarks of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501
        :type: list[CreditsafeGlobalDataReportsConsumerConsumerPaymentSummary]
        """

        self._payment_remarks = payment_remarks

    @property
    def payment_remarks_details(self):
        """Gets the payment_remarks_details of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501


        :return: The payment_remarks_details of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501
        :rtype: list[CreditsafeGlobalDataReportsConsumerConsumerRemarkOfPayment]
        """
        return self._payment_remarks_details

    @payment_remarks_details.setter
    def payment_remarks_details(self, payment_remarks_details):
        """Sets the payment_remarks_details of this CreditsafeGlobalDataReportsConsumerConsumerReport.


        :param payment_remarks_details: The payment_remarks_details of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501
        :type: list[CreditsafeGlobalDataReportsConsumerConsumerRemarkOfPayment]
        """

        self._payment_remarks_details = payment_remarks_details

    @property
    def voluntary_pledges(self):
        """Gets the voluntary_pledges of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501


        :return: The voluntary_pledges of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501
        :rtype: list[CreditsafeGlobalDataReportsConsumerConsumerRemarkOfPayment]
        """
        return self._voluntary_pledges

    @voluntary_pledges.setter
    def voluntary_pledges(self, voluntary_pledges):
        """Sets the voluntary_pledges of this CreditsafeGlobalDataReportsConsumerConsumerReport.


        :param voluntary_pledges: The voluntary_pledges of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501
        :type: list[CreditsafeGlobalDataReportsConsumerConsumerRemarkOfPayment]
        """

        self._voluntary_pledges = voluntary_pledges

    @property
    def consumer_rating(self):
        """Gets the consumer_rating of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501


        :return: The consumer_rating of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsConsumerConsumerCreditScore
        """
        return self._consumer_rating

    @consumer_rating.setter
    def consumer_rating(self, consumer_rating):
        """Sets the consumer_rating of this CreditsafeGlobalDataReportsConsumerConsumerReport.


        :param consumer_rating: The consumer_rating of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501
        :type: CreditsafeGlobalDataReportsConsumerConsumerCreditScore
        """

        self._consumer_rating = consumer_rating

    @property
    def additional_information(self):
        """Gets the additional_information of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501


        :return: The additional_information of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsConsumerConsumerAdditionalInformation
        """
        return self._additional_information

    @additional_information.setter
    def additional_information(self, additional_information):
        """Sets the additional_information of this CreditsafeGlobalDataReportsConsumerConsumerReport.


        :param additional_information: The additional_information of this CreditsafeGlobalDataReportsConsumerConsumerReport.  # noqa: E501
        :type: CreditsafeGlobalDataReportsConsumerConsumerAdditionalInformation
        """

        self._additional_information = additional_information

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
        if issubclass(CreditsafeGlobalDataReportsConsumerConsumerReport, dict):
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
        if not isinstance(other, CreditsafeGlobalDataReportsConsumerConsumerReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

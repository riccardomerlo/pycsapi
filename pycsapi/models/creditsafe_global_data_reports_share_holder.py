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
from pycsapi.models.creditsafe_global_data_reports_entity_full_name import (
    CreditsafeGlobalDataReportsEntityFullName,
)  # noqa: F401,E501


class CreditsafeGlobalDataReportsShareHolder(CreditsafeGlobalDataReportsEntityFullName):
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
        "shareholder_type": "CreditsafeGlobalDataReportsEntityType",
        "share_type": "str",
        "currency": "CreditsafeGlobalDataCurrency",
        "total_value_of_shares_owned": "float",
        "total_number_of_shares_owned": "int",
        "percent_shares_held": "float",
        "start_date": "datetime",
        "end_date": "datetime",
        "has_negative_info": "bool",
        "share_classes": "list[CreditsafeGlobalDataReportsShareClass]",
    }
    if hasattr(CreditsafeGlobalDataReportsEntityFullName, "swagger_types"):
        swagger_types.update(CreditsafeGlobalDataReportsEntityFullName.swagger_types)

    attribute_map = {
        "shareholder_type": "shareholderType",
        "share_type": "shareType",
        "currency": "currency",
        "total_value_of_shares_owned": "totalValueOfSharesOwned",
        "total_number_of_shares_owned": "totalNumberOfSharesOwned",
        "percent_shares_held": "percentSharesHeld",
        "start_date": "startDate",
        "end_date": "endDate",
        "has_negative_info": "hasNegativeInfo",
        "share_classes": "shareClasses",
    }
    if hasattr(CreditsafeGlobalDataReportsEntityFullName, "attribute_map"):
        attribute_map.update(CreditsafeGlobalDataReportsEntityFullName.attribute_map)

    def __init__(
        self,
        shareholder_type=None,
        share_type=None,
        currency=None,
        total_value_of_shares_owned=None,
        total_number_of_shares_owned=None,
        percent_shares_held=None,
        start_date=None,
        end_date=None,
        has_negative_info=None,
        share_classes=None,
        *args,
        **kwargs
    ):  # noqa: E501
        """CreditsafeGlobalDataReportsShareHolder - a model defined in Swagger"""  # noqa: E501
        self._shareholder_type = None
        self._share_type = None
        self._currency = None
        self._total_value_of_shares_owned = None
        self._total_number_of_shares_owned = None
        self._percent_shares_held = None
        self._start_date = None
        self._end_date = None
        self._has_negative_info = None
        self._share_classes = None
        self.discriminator = None
        if shareholder_type is not None:
            self.shareholder_type = shareholder_type
        if share_type is not None:
            self.share_type = share_type
        if currency is not None:
            self.currency = currency
        if total_value_of_shares_owned is not None:
            self.total_value_of_shares_owned = total_value_of_shares_owned
        if total_number_of_shares_owned is not None:
            self.total_number_of_shares_owned = total_number_of_shares_owned
        if percent_shares_held is not None:
            self.percent_shares_held = percent_shares_held
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if has_negative_info is not None:
            self.has_negative_info = has_negative_info
        if share_classes is not None:
            self.share_classes = share_classes
        CreditsafeGlobalDataReportsEntityFullName.__init__(self, *args, **kwargs)

    @property
    def shareholder_type(self):
        """Gets the shareholder_type of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501


        :return: The shareholder_type of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsEntityType
        """
        return self._shareholder_type

    @shareholder_type.setter
    def shareholder_type(self, shareholder_type):
        """Sets the shareholder_type of this CreditsafeGlobalDataReportsShareHolder.


        :param shareholder_type: The shareholder_type of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501
        :type: CreditsafeGlobalDataReportsEntityType
        """

        self._shareholder_type = shareholder_type

    @property
    def share_type(self):
        """Gets the share_type of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501


        :return: The share_type of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        """Sets the share_type of this CreditsafeGlobalDataReportsShareHolder.


        :param share_type: The share_type of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501
        :type: str
        """

        self._share_type = share_type

    @property
    def currency(self):
        """Gets the currency of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501


        :return: The currency of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501
        :rtype: CreditsafeGlobalDataCurrency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CreditsafeGlobalDataReportsShareHolder.


        :param currency: The currency of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501
        :type: CreditsafeGlobalDataCurrency
        """

        self._currency = currency

    @property
    def total_value_of_shares_owned(self):
        """Gets the total_value_of_shares_owned of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501


        :return: The total_value_of_shares_owned of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501
        :rtype: float
        """
        return self._total_value_of_shares_owned

    @total_value_of_shares_owned.setter
    def total_value_of_shares_owned(self, total_value_of_shares_owned):
        """Sets the total_value_of_shares_owned of this CreditsafeGlobalDataReportsShareHolder.


        :param total_value_of_shares_owned: The total_value_of_shares_owned of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501
        :type: float
        """

        self._total_value_of_shares_owned = total_value_of_shares_owned

    @property
    def total_number_of_shares_owned(self):
        """Gets the total_number_of_shares_owned of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501


        :return: The total_number_of_shares_owned of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501
        :rtype: int
        """
        return self._total_number_of_shares_owned

    @total_number_of_shares_owned.setter
    def total_number_of_shares_owned(self, total_number_of_shares_owned):
        """Sets the total_number_of_shares_owned of this CreditsafeGlobalDataReportsShareHolder.


        :param total_number_of_shares_owned: The total_number_of_shares_owned of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501
        :type: int
        """

        self._total_number_of_shares_owned = total_number_of_shares_owned

    @property
    def percent_shares_held(self):
        """Gets the percent_shares_held of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501


        :return: The percent_shares_held of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501
        :rtype: float
        """
        return self._percent_shares_held

    @percent_shares_held.setter
    def percent_shares_held(self, percent_shares_held):
        """Sets the percent_shares_held of this CreditsafeGlobalDataReportsShareHolder.


        :param percent_shares_held: The percent_shares_held of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501
        :type: float
        """

        self._percent_shares_held = percent_shares_held

    @property
    def start_date(self):
        """Gets the start_date of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501


        :return: The start_date of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CreditsafeGlobalDataReportsShareHolder.


        :param start_date: The start_date of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501


        :return: The end_date of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this CreditsafeGlobalDataReportsShareHolder.


        :param end_date: The end_date of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def has_negative_info(self):
        """Gets the has_negative_info of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501


        :return: The has_negative_info of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501
        :rtype: bool
        """
        return self._has_negative_info

    @has_negative_info.setter
    def has_negative_info(self, has_negative_info):
        """Sets the has_negative_info of this CreditsafeGlobalDataReportsShareHolder.


        :param has_negative_info: The has_negative_info of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501
        :type: bool
        """

        self._has_negative_info = has_negative_info

    @property
    def share_classes(self):
        """Gets the share_classes of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501


        :return: The share_classes of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501
        :rtype: list[CreditsafeGlobalDataReportsShareClass]
        """
        return self._share_classes

    @share_classes.setter
    def share_classes(self, share_classes):
        """Sets the share_classes of this CreditsafeGlobalDataReportsShareHolder.


        :param share_classes: The share_classes of this CreditsafeGlobalDataReportsShareHolder.  # noqa: E501
        :type: list[CreditsafeGlobalDataReportsShareClass]
        """

        self._share_classes = share_classes

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (
                            (item[0], item[1].to_dict())
                            if hasattr(item[1], "to_dict")
                            else item
                        ),
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(CreditsafeGlobalDataReportsShareHolder, dict):
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
        if not isinstance(other, CreditsafeGlobalDataReportsShareHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

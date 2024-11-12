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

class CreditsafeGlobalDataReportsLtdCompanySummary(object):
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
        'business_name': 'str',
        'country': 'CreditsafeGlobalDataCountryCode',
        'company_number': 'str',
        'company_registration_number': 'str',
        'ggs_id': 'str',
        'main_activity': 'CreditsafeGlobalDataCompanyActivityClassification',
        'company_status': 'CreditsafeGlobalDataReportsCompanyStatusDescription',
        'latest_turnover_figure': 'CreditsafeGlobalDataReportsFinancialValue1SystemDecimal',
        'latest_shareholders_equity_figure': 'CreditsafeGlobalDataReportsFinancialValue1SystemDecimal',
        'credit_rating': 'CreditsafeGlobalDataReportsCreditRating'
    }

    attribute_map = {
        'business_name': 'businessName',
        'country': 'country',
        'company_number': 'companyNumber',
        'company_registration_number': 'companyRegistrationNumber',
        'ggs_id': 'ggsID',
        'main_activity': 'mainActivity',
        'company_status': 'companyStatus',
        'latest_turnover_figure': 'latestTurnoverFigure',
        'latest_shareholders_equity_figure': 'latestShareholdersEquityFigure',
        'credit_rating': 'creditRating'
    }

    def __init__(self, business_name=None, country=None, company_number=None, company_registration_number=None, ggs_id=None, main_activity=None, company_status=None, latest_turnover_figure=None, latest_shareholders_equity_figure=None, credit_rating=None):  # noqa: E501
        """CreditsafeGlobalDataReportsLtdCompanySummary - a model defined in Swagger"""  # noqa: E501
        self._business_name = None
        self._country = None
        self._company_number = None
        self._company_registration_number = None
        self._ggs_id = None
        self._main_activity = None
        self._company_status = None
        self._latest_turnover_figure = None
        self._latest_shareholders_equity_figure = None
        self._credit_rating = None
        self.discriminator = None
        if business_name is not None:
            self.business_name = business_name
        if country is not None:
            self.country = country
        if company_number is not None:
            self.company_number = company_number
        if company_registration_number is not None:
            self.company_registration_number = company_registration_number
        if ggs_id is not None:
            self.ggs_id = ggs_id
        if main_activity is not None:
            self.main_activity = main_activity
        if company_status is not None:
            self.company_status = company_status
        if latest_turnover_figure is not None:
            self.latest_turnover_figure = latest_turnover_figure
        if latest_shareholders_equity_figure is not None:
            self.latest_shareholders_equity_figure = latest_shareholders_equity_figure
        if credit_rating is not None:
            self.credit_rating = credit_rating

    @property
    def business_name(self):
        """Gets the business_name of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501


        :return: The business_name of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        """Sets the business_name of this CreditsafeGlobalDataReportsLtdCompanySummary.


        :param business_name: The business_name of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501
        :type: str
        """

        self._business_name = business_name

    @property
    def country(self):
        """Gets the country of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501


        :return: The country of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501
        :rtype: CreditsafeGlobalDataCountryCode
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CreditsafeGlobalDataReportsLtdCompanySummary.


        :param country: The country of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501
        :type: CreditsafeGlobalDataCountryCode
        """

        self._country = country

    @property
    def company_number(self):
        """Gets the company_number of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501


        :return: The company_number of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501
        :rtype: str
        """
        return self._company_number

    @company_number.setter
    def company_number(self, company_number):
        """Sets the company_number of this CreditsafeGlobalDataReportsLtdCompanySummary.


        :param company_number: The company_number of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501
        :type: str
        """

        self._company_number = company_number

    @property
    def company_registration_number(self):
        """Gets the company_registration_number of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501


        :return: The company_registration_number of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501
        :rtype: str
        """
        return self._company_registration_number

    @company_registration_number.setter
    def company_registration_number(self, company_registration_number):
        """Sets the company_registration_number of this CreditsafeGlobalDataReportsLtdCompanySummary.


        :param company_registration_number: The company_registration_number of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501
        :type: str
        """

        self._company_registration_number = company_registration_number

    @property
    def ggs_id(self):
        """Gets the ggs_id of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501


        :return: The ggs_id of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501
        :rtype: str
        """
        return self._ggs_id

    @ggs_id.setter
    def ggs_id(self, ggs_id):
        """Sets the ggs_id of this CreditsafeGlobalDataReportsLtdCompanySummary.


        :param ggs_id: The ggs_id of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501
        :type: str
        """

        self._ggs_id = ggs_id

    @property
    def main_activity(self):
        """Gets the main_activity of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501


        :return: The main_activity of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501
        :rtype: CreditsafeGlobalDataCompanyActivityClassification
        """
        return self._main_activity

    @main_activity.setter
    def main_activity(self, main_activity):
        """Sets the main_activity of this CreditsafeGlobalDataReportsLtdCompanySummary.


        :param main_activity: The main_activity of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501
        :type: CreditsafeGlobalDataCompanyActivityClassification
        """

        self._main_activity = main_activity

    @property
    def company_status(self):
        """Gets the company_status of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501


        :return: The company_status of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsCompanyStatusDescription
        """
        return self._company_status

    @company_status.setter
    def company_status(self, company_status):
        """Sets the company_status of this CreditsafeGlobalDataReportsLtdCompanySummary.


        :param company_status: The company_status of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501
        :type: CreditsafeGlobalDataReportsCompanyStatusDescription
        """

        self._company_status = company_status

    @property
    def latest_turnover_figure(self):
        """Gets the latest_turnover_figure of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501


        :return: The latest_turnover_figure of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsFinancialValue1SystemDecimal
        """
        return self._latest_turnover_figure

    @latest_turnover_figure.setter
    def latest_turnover_figure(self, latest_turnover_figure):
        """Sets the latest_turnover_figure of this CreditsafeGlobalDataReportsLtdCompanySummary.


        :param latest_turnover_figure: The latest_turnover_figure of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501
        :type: CreditsafeGlobalDataReportsFinancialValue1SystemDecimal
        """

        self._latest_turnover_figure = latest_turnover_figure

    @property
    def latest_shareholders_equity_figure(self):
        """Gets the latest_shareholders_equity_figure of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501


        :return: The latest_shareholders_equity_figure of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsFinancialValue1SystemDecimal
        """
        return self._latest_shareholders_equity_figure

    @latest_shareholders_equity_figure.setter
    def latest_shareholders_equity_figure(self, latest_shareholders_equity_figure):
        """Sets the latest_shareholders_equity_figure of this CreditsafeGlobalDataReportsLtdCompanySummary.


        :param latest_shareholders_equity_figure: The latest_shareholders_equity_figure of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501
        :type: CreditsafeGlobalDataReportsFinancialValue1SystemDecimal
        """

        self._latest_shareholders_equity_figure = latest_shareholders_equity_figure

    @property
    def credit_rating(self):
        """Gets the credit_rating of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501


        :return: The credit_rating of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501
        :rtype: CreditsafeGlobalDataReportsCreditRating
        """
        return self._credit_rating

    @credit_rating.setter
    def credit_rating(self, credit_rating):
        """Sets the credit_rating of this CreditsafeGlobalDataReportsLtdCompanySummary.


        :param credit_rating: The credit_rating of this CreditsafeGlobalDataReportsLtdCompanySummary.  # noqa: E501
        :type: CreditsafeGlobalDataReportsCreditRating
        """

        self._credit_rating = credit_rating

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
        if issubclass(CreditsafeGlobalDataReportsLtdCompanySummary, dict):
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
        if not isinstance(other, CreditsafeGlobalDataReportsLtdCompanySummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

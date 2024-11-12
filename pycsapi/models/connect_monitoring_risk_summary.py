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

class ConnectMonitoringRiskSummary(object):
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
        'total_companies': 'float',
        'band_a_count': 'float',
        'band_apc': 'float',
        'band_b_count': 'float',
        'band_bpc': 'float',
        'band_c_count': 'float',
        'band_cpc': 'float',
        'band_d_count': 'float',
        'band_dpc': 'float',
        'band_e_count': 'float',
        'band_epc': 'float'
    }

    attribute_map = {
        'correlation_id': 'correlationId',
        'total_companies': 'totalCompanies',
        'band_a_count': 'bandACount',
        'band_apc': 'bandApc',
        'band_b_count': 'bandBCount',
        'band_bpc': 'bandBpc',
        'band_c_count': 'bandCCount',
        'band_cpc': 'bandCpc',
        'band_d_count': 'bandDCount',
        'band_dpc': 'bandDpc',
        'band_e_count': 'bandECount',
        'band_epc': 'bandEpc'
    }

    def __init__(self, correlation_id=None, total_companies=None, band_a_count=None, band_apc=None, band_b_count=None, band_bpc=None, band_c_count=None, band_cpc=None, band_d_count=None, band_dpc=None, band_e_count=None, band_epc=None):  # noqa: E501
        """ConnectMonitoringRiskSummary - a model defined in Swagger"""  # noqa: E501
        self._correlation_id = None
        self._total_companies = None
        self._band_a_count = None
        self._band_apc = None
        self._band_b_count = None
        self._band_bpc = None
        self._band_c_count = None
        self._band_cpc = None
        self._band_d_count = None
        self._band_dpc = None
        self._band_e_count = None
        self._band_epc = None
        self.discriminator = None
        if correlation_id is not None:
            self.correlation_id = correlation_id
        if total_companies is not None:
            self.total_companies = total_companies
        if band_a_count is not None:
            self.band_a_count = band_a_count
        if band_apc is not None:
            self.band_apc = band_apc
        if band_b_count is not None:
            self.band_b_count = band_b_count
        if band_bpc is not None:
            self.band_bpc = band_bpc
        if band_c_count is not None:
            self.band_c_count = band_c_count
        if band_cpc is not None:
            self.band_cpc = band_cpc
        if band_d_count is not None:
            self.band_d_count = band_d_count
        if band_dpc is not None:
            self.band_dpc = band_dpc
        if band_e_count is not None:
            self.band_e_count = band_e_count
        if band_epc is not None:
            self.band_epc = band_epc

    @property
    def correlation_id(self):
        """Gets the correlation_id of this ConnectMonitoringRiskSummary.  # noqa: E501

        A unique ID assigned to this request.  # noqa: E501

        :return: The correlation_id of this ConnectMonitoringRiskSummary.  # noqa: E501
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this ConnectMonitoringRiskSummary.

        A unique ID assigned to this request.  # noqa: E501

        :param correlation_id: The correlation_id of this ConnectMonitoringRiskSummary.  # noqa: E501
        :type: str
        """

        self._correlation_id = correlation_id

    @property
    def total_companies(self):
        """Gets the total_companies of this ConnectMonitoringRiskSummary.  # noqa: E501

        Total Companies in the portfolio  # noqa: E501

        :return: The total_companies of this ConnectMonitoringRiskSummary.  # noqa: E501
        :rtype: float
        """
        return self._total_companies

    @total_companies.setter
    def total_companies(self, total_companies):
        """Sets the total_companies of this ConnectMonitoringRiskSummary.

        Total Companies in the portfolio  # noqa: E501

        :param total_companies: The total_companies of this ConnectMonitoringRiskSummary.  # noqa: E501
        :type: float
        """

        self._total_companies = total_companies

    @property
    def band_a_count(self):
        """Gets the band_a_count of this ConnectMonitoringRiskSummary.  # noqa: E501


        :return: The band_a_count of this ConnectMonitoringRiskSummary.  # noqa: E501
        :rtype: float
        """
        return self._band_a_count

    @band_a_count.setter
    def band_a_count(self, band_a_count):
        """Sets the band_a_count of this ConnectMonitoringRiskSummary.


        :param band_a_count: The band_a_count of this ConnectMonitoringRiskSummary.  # noqa: E501
        :type: float
        """

        self._band_a_count = band_a_count

    @property
    def band_apc(self):
        """Gets the band_apc of this ConnectMonitoringRiskSummary.  # noqa: E501


        :return: The band_apc of this ConnectMonitoringRiskSummary.  # noqa: E501
        :rtype: float
        """
        return self._band_apc

    @band_apc.setter
    def band_apc(self, band_apc):
        """Sets the band_apc of this ConnectMonitoringRiskSummary.


        :param band_apc: The band_apc of this ConnectMonitoringRiskSummary.  # noqa: E501
        :type: float
        """

        self._band_apc = band_apc

    @property
    def band_b_count(self):
        """Gets the band_b_count of this ConnectMonitoringRiskSummary.  # noqa: E501


        :return: The band_b_count of this ConnectMonitoringRiskSummary.  # noqa: E501
        :rtype: float
        """
        return self._band_b_count

    @band_b_count.setter
    def band_b_count(self, band_b_count):
        """Sets the band_b_count of this ConnectMonitoringRiskSummary.


        :param band_b_count: The band_b_count of this ConnectMonitoringRiskSummary.  # noqa: E501
        :type: float
        """

        self._band_b_count = band_b_count

    @property
    def band_bpc(self):
        """Gets the band_bpc of this ConnectMonitoringRiskSummary.  # noqa: E501


        :return: The band_bpc of this ConnectMonitoringRiskSummary.  # noqa: E501
        :rtype: float
        """
        return self._band_bpc

    @band_bpc.setter
    def band_bpc(self, band_bpc):
        """Sets the band_bpc of this ConnectMonitoringRiskSummary.


        :param band_bpc: The band_bpc of this ConnectMonitoringRiskSummary.  # noqa: E501
        :type: float
        """

        self._band_bpc = band_bpc

    @property
    def band_c_count(self):
        """Gets the band_c_count of this ConnectMonitoringRiskSummary.  # noqa: E501


        :return: The band_c_count of this ConnectMonitoringRiskSummary.  # noqa: E501
        :rtype: float
        """
        return self._band_c_count

    @band_c_count.setter
    def band_c_count(self, band_c_count):
        """Sets the band_c_count of this ConnectMonitoringRiskSummary.


        :param band_c_count: The band_c_count of this ConnectMonitoringRiskSummary.  # noqa: E501
        :type: float
        """

        self._band_c_count = band_c_count

    @property
    def band_cpc(self):
        """Gets the band_cpc of this ConnectMonitoringRiskSummary.  # noqa: E501


        :return: The band_cpc of this ConnectMonitoringRiskSummary.  # noqa: E501
        :rtype: float
        """
        return self._band_cpc

    @band_cpc.setter
    def band_cpc(self, band_cpc):
        """Sets the band_cpc of this ConnectMonitoringRiskSummary.


        :param band_cpc: The band_cpc of this ConnectMonitoringRiskSummary.  # noqa: E501
        :type: float
        """

        self._band_cpc = band_cpc

    @property
    def band_d_count(self):
        """Gets the band_d_count of this ConnectMonitoringRiskSummary.  # noqa: E501


        :return: The band_d_count of this ConnectMonitoringRiskSummary.  # noqa: E501
        :rtype: float
        """
        return self._band_d_count

    @band_d_count.setter
    def band_d_count(self, band_d_count):
        """Sets the band_d_count of this ConnectMonitoringRiskSummary.


        :param band_d_count: The band_d_count of this ConnectMonitoringRiskSummary.  # noqa: E501
        :type: float
        """

        self._band_d_count = band_d_count

    @property
    def band_dpc(self):
        """Gets the band_dpc of this ConnectMonitoringRiskSummary.  # noqa: E501


        :return: The band_dpc of this ConnectMonitoringRiskSummary.  # noqa: E501
        :rtype: float
        """
        return self._band_dpc

    @band_dpc.setter
    def band_dpc(self, band_dpc):
        """Sets the band_dpc of this ConnectMonitoringRiskSummary.


        :param band_dpc: The band_dpc of this ConnectMonitoringRiskSummary.  # noqa: E501
        :type: float
        """

        self._band_dpc = band_dpc

    @property
    def band_e_count(self):
        """Gets the band_e_count of this ConnectMonitoringRiskSummary.  # noqa: E501


        :return: The band_e_count of this ConnectMonitoringRiskSummary.  # noqa: E501
        :rtype: float
        """
        return self._band_e_count

    @band_e_count.setter
    def band_e_count(self, band_e_count):
        """Sets the band_e_count of this ConnectMonitoringRiskSummary.


        :param band_e_count: The band_e_count of this ConnectMonitoringRiskSummary.  # noqa: E501
        :type: float
        """

        self._band_e_count = band_e_count

    @property
    def band_epc(self):
        """Gets the band_epc of this ConnectMonitoringRiskSummary.  # noqa: E501


        :return: The band_epc of this ConnectMonitoringRiskSummary.  # noqa: E501
        :rtype: float
        """
        return self._band_epc

    @band_epc.setter
    def band_epc(self, band_epc):
        """Sets the band_epc of this ConnectMonitoringRiskSummary.


        :param band_epc: The band_epc of this ConnectMonitoringRiskSummary.  # noqa: E501
        :type: float
        """

        self._band_epc = band_epc

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
        if issubclass(ConnectMonitoringRiskSummary, dict):
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
        if not isinstance(other, ConnectMonitoringRiskSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

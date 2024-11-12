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

class ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition(object):
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
        'activity': 'int',
        'average_detached_property_value': 'str',
        'average_detached_property_value_description': 'str',
        'average_detached_property_index': 'int',
        'average_flat_property_value': 'str',
        'average_flat_property_index': 'int',
        'average_house_age': 'str',
        'average_semi_detached_property_value': 'str',
        'average_semi_detached_property_value_description': 'str',
        'average_semi_detached_property_index': 'int',
        'average_terrace_property_value': 'str',
        'average_terrace_property_value_description': 'str',
        'average_terrace_property_index': 'int',
        'council_tax_band': 'str',
        'council_tax_band_description': 'str',
        'household_density': 'str',
        'location_type': 'str',
        'national_average_house_price': 'str',
        'national_average_house_price_above_or_below': 'str',
        'national_average_house_price_difference': 'str',
        'national_average_house_price_index': 'int',
        'average_flat_property_value_description': 'str'
    }

    attribute_map = {
        'activity': 'activity',
        'average_detached_property_value': 'averageDetachedPropertyValue',
        'average_detached_property_value_description': 'averageDetachedPropertyValueDescription',
        'average_detached_property_index': 'averageDetachedPropertyIndex',
        'average_flat_property_value': 'averageFlatPropertyValue',
        'average_flat_property_index': 'averageFlatPropertyIndex',
        'average_house_age': 'averageHouseAge',
        'average_semi_detached_property_value': 'averageSemiDetachedPropertyValue',
        'average_semi_detached_property_value_description': 'averageSemiDetachedPropertyValueDescription',
        'average_semi_detached_property_index': 'averageSemiDetachedPropertyIndex',
        'average_terrace_property_value': 'averageTerracePropertyValue',
        'average_terrace_property_value_description': 'averageTerracePropertyValueDescription',
        'average_terrace_property_index': 'averageTerracePropertyIndex',
        'council_tax_band': 'councilTaxBand',
        'council_tax_band_description': 'councilTaxBandDescription',
        'household_density': 'householdDensity',
        'location_type': 'locationType',
        'national_average_house_price': 'nationalAverageHousePrice',
        'national_average_house_price_above_or_below': 'nationalAverageHousePriceAboveOrBelow',
        'national_average_house_price_difference': 'nationalAverageHousePriceDifference',
        'national_average_house_price_index': 'nationalAverageHousePriceIndex',
        'average_flat_property_value_description': 'averageFlatPropertyValueDescription'
    }

    def __init__(self, activity=None, average_detached_property_value=None, average_detached_property_value_description=None, average_detached_property_index=None, average_flat_property_value=None, average_flat_property_index=None, average_house_age=None, average_semi_detached_property_value=None, average_semi_detached_property_value_description=None, average_semi_detached_property_index=None, average_terrace_property_value=None, average_terrace_property_value_description=None, average_terrace_property_index=None, council_tax_band=None, council_tax_band_description=None, household_density=None, location_type=None, national_average_house_price=None, national_average_house_price_above_or_below=None, national_average_house_price_difference=None, national_average_house_price_index=None, average_flat_property_value_description=None):  # noqa: E501
        """ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition - a model defined in Swagger"""  # noqa: E501
        self._activity = None
        self._average_detached_property_value = None
        self._average_detached_property_value_description = None
        self._average_detached_property_index = None
        self._average_flat_property_value = None
        self._average_flat_property_index = None
        self._average_house_age = None
        self._average_semi_detached_property_value = None
        self._average_semi_detached_property_value_description = None
        self._average_semi_detached_property_index = None
        self._average_terrace_property_value = None
        self._average_terrace_property_value_description = None
        self._average_terrace_property_index = None
        self._council_tax_band = None
        self._council_tax_band_description = None
        self._household_density = None
        self._location_type = None
        self._national_average_house_price = None
        self._national_average_house_price_above_or_below = None
        self._national_average_house_price_difference = None
        self._national_average_house_price_index = None
        self._average_flat_property_value_description = None
        self.discriminator = None
        if activity is not None:
            self.activity = activity
        if average_detached_property_value is not None:
            self.average_detached_property_value = average_detached_property_value
        if average_detached_property_value_description is not None:
            self.average_detached_property_value_description = average_detached_property_value_description
        if average_detached_property_index is not None:
            self.average_detached_property_index = average_detached_property_index
        if average_flat_property_value is not None:
            self.average_flat_property_value = average_flat_property_value
        if average_flat_property_index is not None:
            self.average_flat_property_index = average_flat_property_index
        if average_house_age is not None:
            self.average_house_age = average_house_age
        if average_semi_detached_property_value is not None:
            self.average_semi_detached_property_value = average_semi_detached_property_value
        if average_semi_detached_property_value_description is not None:
            self.average_semi_detached_property_value_description = average_semi_detached_property_value_description
        if average_semi_detached_property_index is not None:
            self.average_semi_detached_property_index = average_semi_detached_property_index
        if average_terrace_property_value is not None:
            self.average_terrace_property_value = average_terrace_property_value
        if average_terrace_property_value_description is not None:
            self.average_terrace_property_value_description = average_terrace_property_value_description
        if average_terrace_property_index is not None:
            self.average_terrace_property_index = average_terrace_property_index
        if council_tax_band is not None:
            self.council_tax_band = council_tax_band
        if council_tax_band_description is not None:
            self.council_tax_band_description = council_tax_band_description
        if household_density is not None:
            self.household_density = household_density
        if location_type is not None:
            self.location_type = location_type
        if national_average_house_price is not None:
            self.national_average_house_price = national_average_house_price
        if national_average_house_price_above_or_below is not None:
            self.national_average_house_price_above_or_below = national_average_house_price_above_or_below
        if national_average_house_price_difference is not None:
            self.national_average_house_price_difference = national_average_house_price_difference
        if national_average_house_price_index is not None:
            self.national_average_house_price_index = national_average_house_price_index
        if average_flat_property_value_description is not None:
            self.average_flat_property_value_description = average_flat_property_value_description

    @property
    def activity(self):
        """Gets the activity of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The activity of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: int
        """
        return self._activity

    @activity.setter
    def activity(self, activity):
        """Sets the activity of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param activity: The activity of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: int
        """

        self._activity = activity

    @property
    def average_detached_property_value(self):
        """Gets the average_detached_property_value of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The average_detached_property_value of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: str
        """
        return self._average_detached_property_value

    @average_detached_property_value.setter
    def average_detached_property_value(self, average_detached_property_value):
        """Sets the average_detached_property_value of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param average_detached_property_value: The average_detached_property_value of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: str
        """

        self._average_detached_property_value = average_detached_property_value

    @property
    def average_detached_property_value_description(self):
        """Gets the average_detached_property_value_description of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The average_detached_property_value_description of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: str
        """
        return self._average_detached_property_value_description

    @average_detached_property_value_description.setter
    def average_detached_property_value_description(self, average_detached_property_value_description):
        """Sets the average_detached_property_value_description of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param average_detached_property_value_description: The average_detached_property_value_description of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: str
        """

        self._average_detached_property_value_description = average_detached_property_value_description

    @property
    def average_detached_property_index(self):
        """Gets the average_detached_property_index of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The average_detached_property_index of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: int
        """
        return self._average_detached_property_index

    @average_detached_property_index.setter
    def average_detached_property_index(self, average_detached_property_index):
        """Sets the average_detached_property_index of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param average_detached_property_index: The average_detached_property_index of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: int
        """

        self._average_detached_property_index = average_detached_property_index

    @property
    def average_flat_property_value(self):
        """Gets the average_flat_property_value of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The average_flat_property_value of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: str
        """
        return self._average_flat_property_value

    @average_flat_property_value.setter
    def average_flat_property_value(self, average_flat_property_value):
        """Sets the average_flat_property_value of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param average_flat_property_value: The average_flat_property_value of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: str
        """

        self._average_flat_property_value = average_flat_property_value

    @property
    def average_flat_property_index(self):
        """Gets the average_flat_property_index of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The average_flat_property_index of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: int
        """
        return self._average_flat_property_index

    @average_flat_property_index.setter
    def average_flat_property_index(self, average_flat_property_index):
        """Sets the average_flat_property_index of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param average_flat_property_index: The average_flat_property_index of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: int
        """

        self._average_flat_property_index = average_flat_property_index

    @property
    def average_house_age(self):
        """Gets the average_house_age of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The average_house_age of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: str
        """
        return self._average_house_age

    @average_house_age.setter
    def average_house_age(self, average_house_age):
        """Sets the average_house_age of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param average_house_age: The average_house_age of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: str
        """

        self._average_house_age = average_house_age

    @property
    def average_semi_detached_property_value(self):
        """Gets the average_semi_detached_property_value of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The average_semi_detached_property_value of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: str
        """
        return self._average_semi_detached_property_value

    @average_semi_detached_property_value.setter
    def average_semi_detached_property_value(self, average_semi_detached_property_value):
        """Sets the average_semi_detached_property_value of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param average_semi_detached_property_value: The average_semi_detached_property_value of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: str
        """

        self._average_semi_detached_property_value = average_semi_detached_property_value

    @property
    def average_semi_detached_property_value_description(self):
        """Gets the average_semi_detached_property_value_description of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The average_semi_detached_property_value_description of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: str
        """
        return self._average_semi_detached_property_value_description

    @average_semi_detached_property_value_description.setter
    def average_semi_detached_property_value_description(self, average_semi_detached_property_value_description):
        """Sets the average_semi_detached_property_value_description of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param average_semi_detached_property_value_description: The average_semi_detached_property_value_description of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: str
        """

        self._average_semi_detached_property_value_description = average_semi_detached_property_value_description

    @property
    def average_semi_detached_property_index(self):
        """Gets the average_semi_detached_property_index of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The average_semi_detached_property_index of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: int
        """
        return self._average_semi_detached_property_index

    @average_semi_detached_property_index.setter
    def average_semi_detached_property_index(self, average_semi_detached_property_index):
        """Sets the average_semi_detached_property_index of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param average_semi_detached_property_index: The average_semi_detached_property_index of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: int
        """

        self._average_semi_detached_property_index = average_semi_detached_property_index

    @property
    def average_terrace_property_value(self):
        """Gets the average_terrace_property_value of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The average_terrace_property_value of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: str
        """
        return self._average_terrace_property_value

    @average_terrace_property_value.setter
    def average_terrace_property_value(self, average_terrace_property_value):
        """Sets the average_terrace_property_value of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param average_terrace_property_value: The average_terrace_property_value of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: str
        """

        self._average_terrace_property_value = average_terrace_property_value

    @property
    def average_terrace_property_value_description(self):
        """Gets the average_terrace_property_value_description of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The average_terrace_property_value_description of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: str
        """
        return self._average_terrace_property_value_description

    @average_terrace_property_value_description.setter
    def average_terrace_property_value_description(self, average_terrace_property_value_description):
        """Sets the average_terrace_property_value_description of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param average_terrace_property_value_description: The average_terrace_property_value_description of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: str
        """

        self._average_terrace_property_value_description = average_terrace_property_value_description

    @property
    def average_terrace_property_index(self):
        """Gets the average_terrace_property_index of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The average_terrace_property_index of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: int
        """
        return self._average_terrace_property_index

    @average_terrace_property_index.setter
    def average_terrace_property_index(self, average_terrace_property_index):
        """Sets the average_terrace_property_index of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param average_terrace_property_index: The average_terrace_property_index of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: int
        """

        self._average_terrace_property_index = average_terrace_property_index

    @property
    def council_tax_band(self):
        """Gets the council_tax_band of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The council_tax_band of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: str
        """
        return self._council_tax_band

    @council_tax_band.setter
    def council_tax_band(self, council_tax_band):
        """Sets the council_tax_band of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param council_tax_band: The council_tax_band of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: str
        """

        self._council_tax_band = council_tax_band

    @property
    def council_tax_band_description(self):
        """Gets the council_tax_band_description of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The council_tax_band_description of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: str
        """
        return self._council_tax_band_description

    @council_tax_band_description.setter
    def council_tax_band_description(self, council_tax_band_description):
        """Sets the council_tax_band_description of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param council_tax_band_description: The council_tax_band_description of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: str
        """

        self._council_tax_band_description = council_tax_band_description

    @property
    def household_density(self):
        """Gets the household_density of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The household_density of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: str
        """
        return self._household_density

    @household_density.setter
    def household_density(self, household_density):
        """Sets the household_density of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param household_density: The household_density of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: str
        """

        self._household_density = household_density

    @property
    def location_type(self):
        """Gets the location_type of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The location_type of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: str
        """
        return self._location_type

    @location_type.setter
    def location_type(self, location_type):
        """Sets the location_type of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param location_type: The location_type of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: str
        """

        self._location_type = location_type

    @property
    def national_average_house_price(self):
        """Gets the national_average_house_price of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The national_average_house_price of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: str
        """
        return self._national_average_house_price

    @national_average_house_price.setter
    def national_average_house_price(self, national_average_house_price):
        """Sets the national_average_house_price of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param national_average_house_price: The national_average_house_price of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: str
        """

        self._national_average_house_price = national_average_house_price

    @property
    def national_average_house_price_above_or_below(self):
        """Gets the national_average_house_price_above_or_below of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The national_average_house_price_above_or_below of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: str
        """
        return self._national_average_house_price_above_or_below

    @national_average_house_price_above_or_below.setter
    def national_average_house_price_above_or_below(self, national_average_house_price_above_or_below):
        """Sets the national_average_house_price_above_or_below of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param national_average_house_price_above_or_below: The national_average_house_price_above_or_below of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: str
        """

        self._national_average_house_price_above_or_below = national_average_house_price_above_or_below

    @property
    def national_average_house_price_difference(self):
        """Gets the national_average_house_price_difference of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The national_average_house_price_difference of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: str
        """
        return self._national_average_house_price_difference

    @national_average_house_price_difference.setter
    def national_average_house_price_difference(self, national_average_house_price_difference):
        """Sets the national_average_house_price_difference of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param national_average_house_price_difference: The national_average_house_price_difference of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: str
        """

        self._national_average_house_price_difference = national_average_house_price_difference

    @property
    def national_average_house_price_index(self):
        """Gets the national_average_house_price_index of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The national_average_house_price_index of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: int
        """
        return self._national_average_house_price_index

    @national_average_house_price_index.setter
    def national_average_house_price_index(self, national_average_house_price_index):
        """Sets the national_average_house_price_index of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param national_average_house_price_index: The national_average_house_price_index of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: int
        """

        self._national_average_house_price_index = national_average_house_price_index

    @property
    def average_flat_property_value_description(self):
        """Gets the average_flat_property_value_description of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501


        :return: The average_flat_property_value_description of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :rtype: str
        """
        return self._average_flat_property_value_description

    @average_flat_property_value_description.setter
    def average_flat_property_value_description(self, average_flat_property_value_description):
        """Sets the average_flat_property_value_description of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.


        :param average_flat_property_value_description: The average_flat_property_value_description of this ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition.  # noqa: E501
        :type: str
        """

        self._average_flat_property_value_description = average_flat_property_value_description

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
        if issubclass(ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition, dict):
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
        if not isinstance(other, ConnectIdentityConsumerSearchResultConsumerResultApplicant1ReportDemographicsPropertyComposition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

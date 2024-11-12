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

class ConnectIdentityAddress(object):
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
        'abode_no': 'str',
        'building_no': 'str',
        'building_name': 'str',
        'street': 'str',
        'sub_street': 'str',
        'city': 'str',
        'post_code': 'str',
        'organisation': 'str',
        'sub_building': 'str',
        'district': 'str'
    }

    attribute_map = {
        'abode_no': 'abodeNo',
        'building_no': 'buildingNo',
        'building_name': 'buildingName',
        'street': 'street',
        'sub_street': 'subStreet',
        'city': 'city',
        'post_code': 'postCode',
        'organisation': 'organisation',
        'sub_building': 'subBuilding',
        'district': 'district'
    }

    def __init__(self, abode_no=None, building_no=None, building_name=None, street=None, sub_street=None, city=None, post_code=None, organisation=None, sub_building=None, district=None):  # noqa: E501
        """ConnectIdentityAddress - a model defined in Swagger"""  # noqa: E501
        self._abode_no = None
        self._building_no = None
        self._building_name = None
        self._street = None
        self._sub_street = None
        self._city = None
        self._post_code = None
        self._organisation = None
        self._sub_building = None
        self._district = None
        self.discriminator = None
        if abode_no is not None:
            self.abode_no = abode_no
        if building_no is not None:
            self.building_no = building_no
        if building_name is not None:
            self.building_name = building_name
        if street is not None:
            self.street = street
        if sub_street is not None:
            self.sub_street = sub_street
        if city is not None:
            self.city = city
        self.post_code = post_code
        if organisation is not None:
            self.organisation = organisation
        if sub_building is not None:
            self.sub_building = sub_building
        if district is not None:
            self.district = district

    @property
    def abode_no(self):
        """Gets the abode_no of this ConnectIdentityAddress.  # noqa: E501

        The specific abode number within a building complex or estate.  # noqa: E501

        :return: The abode_no of this ConnectIdentityAddress.  # noqa: E501
        :rtype: str
        """
        return self._abode_no

    @abode_no.setter
    def abode_no(self, abode_no):
        """Sets the abode_no of this ConnectIdentityAddress.

        The specific abode number within a building complex or estate.  # noqa: E501

        :param abode_no: The abode_no of this ConnectIdentityAddress.  # noqa: E501
        :type: str
        """

        self._abode_no = abode_no

    @property
    def building_no(self):
        """Gets the building_no of this ConnectIdentityAddress.  # noqa: E501

        The number identifying the building within a street or area.  # noqa: E501

        :return: The building_no of this ConnectIdentityAddress.  # noqa: E501
        :rtype: str
        """
        return self._building_no

    @building_no.setter
    def building_no(self, building_no):
        """Sets the building_no of this ConnectIdentityAddress.

        The number identifying the building within a street or area.  # noqa: E501

        :param building_no: The building_no of this ConnectIdentityAddress.  # noqa: E501
        :type: str
        """

        self._building_no = building_no

    @property
    def building_name(self):
        """Gets the building_name of this ConnectIdentityAddress.  # noqa: E501

        The official name of the building, if applicable.  # noqa: E501

        :return: The building_name of this ConnectIdentityAddress.  # noqa: E501
        :rtype: str
        """
        return self._building_name

    @building_name.setter
    def building_name(self, building_name):
        """Sets the building_name of this ConnectIdentityAddress.

        The official name of the building, if applicable.  # noqa: E501

        :param building_name: The building_name of this ConnectIdentityAddress.  # noqa: E501
        :type: str
        """

        self._building_name = building_name

    @property
    def street(self):
        """Gets the street of this ConnectIdentityAddress.  # noqa: E501

        The street name where the building is located.  # noqa: E501

        :return: The street of this ConnectIdentityAddress.  # noqa: E501
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this ConnectIdentityAddress.

        The street name where the building is located.  # noqa: E501

        :param street: The street of this ConnectIdentityAddress.  # noqa: E501
        :type: str
        """

        self._street = street

    @property
    def sub_street(self):
        """Gets the sub_street of this ConnectIdentityAddress.  # noqa: E501

        Any additional street-level details, like a quadrant or alley.  # noqa: E501

        :return: The sub_street of this ConnectIdentityAddress.  # noqa: E501
        :rtype: str
        """
        return self._sub_street

    @sub_street.setter
    def sub_street(self, sub_street):
        """Sets the sub_street of this ConnectIdentityAddress.

        Any additional street-level details, like a quadrant or alley.  # noqa: E501

        :param sub_street: The sub_street of this ConnectIdentityAddress.  # noqa: E501
        :type: str
        """

        self._sub_street = sub_street

    @property
    def city(self):
        """Gets the city of this ConnectIdentityAddress.  # noqa: E501

        The city or locality of the address.  # noqa: E501

        :return: The city of this ConnectIdentityAddress.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ConnectIdentityAddress.

        The city or locality of the address.  # noqa: E501

        :param city: The city of this ConnectIdentityAddress.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def post_code(self):
        """Gets the post_code of this ConnectIdentityAddress.  # noqa: E501

        The postal code for the address, aiding mail delivery and geographic identification.  # noqa: E501

        :return: The post_code of this ConnectIdentityAddress.  # noqa: E501
        :rtype: str
        """
        return self._post_code

    @post_code.setter
    def post_code(self, post_code):
        """Sets the post_code of this ConnectIdentityAddress.

        The postal code for the address, aiding mail delivery and geographic identification.  # noqa: E501

        :param post_code: The post_code of this ConnectIdentityAddress.  # noqa: E501
        :type: str
        """
        if post_code is None:
            raise ValueError("Invalid value for `post_code`, must not be `None`")  # noqa: E501

        self._post_code = post_code

    @property
    def organisation(self):
        """Gets the organisation of this ConnectIdentityAddress.  # noqa: E501

        The name of any organisation associated with the address.  # noqa: E501

        :return: The organisation of this ConnectIdentityAddress.  # noqa: E501
        :rtype: str
        """
        return self._organisation

    @organisation.setter
    def organisation(self, organisation):
        """Sets the organisation of this ConnectIdentityAddress.

        The name of any organisation associated with the address.  # noqa: E501

        :param organisation: The organisation of this ConnectIdentityAddress.  # noqa: E501
        :type: str
        """

        self._organisation = organisation

    @property
    def sub_building(self):
        """Gets the sub_building of this ConnectIdentityAddress.  # noqa: E501

        Specific information about a part of a building, like a suite or apartment number.  # noqa: E501

        :return: The sub_building of this ConnectIdentityAddress.  # noqa: E501
        :rtype: str
        """
        return self._sub_building

    @sub_building.setter
    def sub_building(self, sub_building):
        """Sets the sub_building of this ConnectIdentityAddress.

        Specific information about a part of a building, like a suite or apartment number.  # noqa: E501

        :param sub_building: The sub_building of this ConnectIdentityAddress.  # noqa: E501
        :type: str
        """

        self._sub_building = sub_building

    @property
    def district(self):
        """Gets the district of this ConnectIdentityAddress.  # noqa: E501

        A broader area or district encompassing the address, often used in urban address schemas.  # noqa: E501

        :return: The district of this ConnectIdentityAddress.  # noqa: E501
        :rtype: str
        """
        return self._district

    @district.setter
    def district(self, district):
        """Sets the district of this ConnectIdentityAddress.

        A broader area or district encompassing the address, often used in urban address schemas.  # noqa: E501

        :param district: The district of this ConnectIdentityAddress.  # noqa: E501
        :type: str
        """

        self._district = district

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
        if issubclass(ConnectIdentityAddress, dict):
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
        if not isinstance(other, ConnectIdentityAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

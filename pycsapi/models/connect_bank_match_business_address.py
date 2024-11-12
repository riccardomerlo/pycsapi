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

class ConnectBankMatchBusinessAddress(object):
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
        'line1': 'str',
        'line2': 'str',
        'line3': 'str',
        'line4': 'str',
        'line5': 'str',
        'line6': 'str',
        'postcode': 'str'
    }

    attribute_map = {
        'line1': 'line1',
        'line2': 'line2',
        'line3': 'line3',
        'line4': 'line4',
        'line5': 'line5',
        'line6': 'line6',
        'postcode': 'postcode'
    }

    def __init__(self, line1=None, line2=None, line3=None, line4=None, line5=None, line6=None, postcode=None):  # noqa: E501
        """ConnectBankMatchBusinessAddress - a model defined in Swagger"""  # noqa: E501
        self._line1 = None
        self._line2 = None
        self._line3 = None
        self._line4 = None
        self._line5 = None
        self._line6 = None
        self._postcode = None
        self.discriminator = None
        if line1 is not None:
            self.line1 = line1
        if line2 is not None:
            self.line2 = line2
        if line3 is not None:
            self.line3 = line3
        if line4 is not None:
            self.line4 = line4
        if line5 is not None:
            self.line5 = line5
        if line6 is not None:
            self.line6 = line6
        if postcode is not None:
            self.postcode = postcode

    @property
    def line1(self):
        """Gets the line1 of this ConnectBankMatchBusinessAddress.  # noqa: E501


        :return: The line1 of this ConnectBankMatchBusinessAddress.  # noqa: E501
        :rtype: str
        """
        return self._line1

    @line1.setter
    def line1(self, line1):
        """Sets the line1 of this ConnectBankMatchBusinessAddress.


        :param line1: The line1 of this ConnectBankMatchBusinessAddress.  # noqa: E501
        :type: str
        """

        self._line1 = line1

    @property
    def line2(self):
        """Gets the line2 of this ConnectBankMatchBusinessAddress.  # noqa: E501


        :return: The line2 of this ConnectBankMatchBusinessAddress.  # noqa: E501
        :rtype: str
        """
        return self._line2

    @line2.setter
    def line2(self, line2):
        """Sets the line2 of this ConnectBankMatchBusinessAddress.


        :param line2: The line2 of this ConnectBankMatchBusinessAddress.  # noqa: E501
        :type: str
        """

        self._line2 = line2

    @property
    def line3(self):
        """Gets the line3 of this ConnectBankMatchBusinessAddress.  # noqa: E501


        :return: The line3 of this ConnectBankMatchBusinessAddress.  # noqa: E501
        :rtype: str
        """
        return self._line3

    @line3.setter
    def line3(self, line3):
        """Sets the line3 of this ConnectBankMatchBusinessAddress.


        :param line3: The line3 of this ConnectBankMatchBusinessAddress.  # noqa: E501
        :type: str
        """

        self._line3 = line3

    @property
    def line4(self):
        """Gets the line4 of this ConnectBankMatchBusinessAddress.  # noqa: E501


        :return: The line4 of this ConnectBankMatchBusinessAddress.  # noqa: E501
        :rtype: str
        """
        return self._line4

    @line4.setter
    def line4(self, line4):
        """Sets the line4 of this ConnectBankMatchBusinessAddress.


        :param line4: The line4 of this ConnectBankMatchBusinessAddress.  # noqa: E501
        :type: str
        """

        self._line4 = line4

    @property
    def line5(self):
        """Gets the line5 of this ConnectBankMatchBusinessAddress.  # noqa: E501


        :return: The line5 of this ConnectBankMatchBusinessAddress.  # noqa: E501
        :rtype: str
        """
        return self._line5

    @line5.setter
    def line5(self, line5):
        """Sets the line5 of this ConnectBankMatchBusinessAddress.


        :param line5: The line5 of this ConnectBankMatchBusinessAddress.  # noqa: E501
        :type: str
        """

        self._line5 = line5

    @property
    def line6(self):
        """Gets the line6 of this ConnectBankMatchBusinessAddress.  # noqa: E501


        :return: The line6 of this ConnectBankMatchBusinessAddress.  # noqa: E501
        :rtype: str
        """
        return self._line6

    @line6.setter
    def line6(self, line6):
        """Sets the line6 of this ConnectBankMatchBusinessAddress.


        :param line6: The line6 of this ConnectBankMatchBusinessAddress.  # noqa: E501
        :type: str
        """

        self._line6 = line6

    @property
    def postcode(self):
        """Gets the postcode of this ConnectBankMatchBusinessAddress.  # noqa: E501


        :return: The postcode of this ConnectBankMatchBusinessAddress.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this ConnectBankMatchBusinessAddress.


        :param postcode: The postcode of this ConnectBankMatchBusinessAddress.  # noqa: E501
        :type: str
        """

        self._postcode = postcode

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
        if issubclass(ConnectBankMatchBusinessAddress, dict):
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
        if not isinstance(other, ConnectBankMatchBusinessAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

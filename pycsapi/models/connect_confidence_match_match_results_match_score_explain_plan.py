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

class ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan(object):
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
        'match_score': 'int',
        'match_score_alpha': 'str',
        'match_score_local_id': 'str',
        'match_score_name': 'str',
        'match_score_house_no': 'str',
        'match_score_street': 'str',
        'match_score_po_box': 'str',
        'match_score_city': 'str',
        'match_score_state': 'str',
        'match_score_post_code': 'str',
        'match_score_country': 'str',
        'match_score_vat_no': 'str',
        'match_score_reg_no': 'str',
        'match_score_phone_no': 'str',
        'match_score_simple_value': 'str',
        'match_score_num': 'str'
    }

    attribute_map = {
        'match_score': 'matchScore',
        'match_score_alpha': 'matchScoreAlpha',
        'match_score_local_id': 'matchScoreLocal Id',
        'match_score_name': 'matchScoreName',
        'match_score_house_no': 'matchScoreHouseNo',
        'match_score_street': 'matchScoreStreet',
        'match_score_po_box': 'matchScorePoBox',
        'match_score_city': 'matchScoreCity',
        'match_score_state': 'matchScoreState',
        'match_score_post_code': 'matchScorePostCode',
        'match_score_country': 'matchScoreCountry',
        'match_score_vat_no': 'matchScoreVatNo',
        'match_score_reg_no': 'matchScoreRegNo',
        'match_score_phone_no': 'matchScorePhoneNo',
        'match_score_simple_value': 'matchScoreSimpleValue',
        'match_score_num': 'matchScoreNum'
    }

    def __init__(self, match_score=None, match_score_alpha=None, match_score_local_id=None, match_score_name=None, match_score_house_no=None, match_score_street=None, match_score_po_box=None, match_score_city=None, match_score_state=None, match_score_post_code=None, match_score_country=None, match_score_vat_no=None, match_score_reg_no=None, match_score_phone_no=None, match_score_simple_value=None, match_score_num=None):  # noqa: E501
        """ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan - a model defined in Swagger"""  # noqa: E501
        self._match_score = None
        self._match_score_alpha = None
        self._match_score_local_id = None
        self._match_score_name = None
        self._match_score_house_no = None
        self._match_score_street = None
        self._match_score_po_box = None
        self._match_score_city = None
        self._match_score_state = None
        self._match_score_post_code = None
        self._match_score_country = None
        self._match_score_vat_no = None
        self._match_score_reg_no = None
        self._match_score_phone_no = None
        self._match_score_simple_value = None
        self._match_score_num = None
        self.discriminator = None
        if match_score is not None:
            self.match_score = match_score
        if match_score_alpha is not None:
            self.match_score_alpha = match_score_alpha
        if match_score_local_id is not None:
            self.match_score_local_id = match_score_local_id
        if match_score_name is not None:
            self.match_score_name = match_score_name
        if match_score_house_no is not None:
            self.match_score_house_no = match_score_house_no
        if match_score_street is not None:
            self.match_score_street = match_score_street
        if match_score_po_box is not None:
            self.match_score_po_box = match_score_po_box
        if match_score_city is not None:
            self.match_score_city = match_score_city
        if match_score_state is not None:
            self.match_score_state = match_score_state
        if match_score_post_code is not None:
            self.match_score_post_code = match_score_post_code
        if match_score_country is not None:
            self.match_score_country = match_score_country
        if match_score_vat_no is not None:
            self.match_score_vat_no = match_score_vat_no
        if match_score_reg_no is not None:
            self.match_score_reg_no = match_score_reg_no
        if match_score_phone_no is not None:
            self.match_score_phone_no = match_score_phone_no
        if match_score_simple_value is not None:
            self.match_score_simple_value = match_score_simple_value
        if match_score_num is not None:
            self.match_score_num = match_score_num

    @property
    def match_score(self):
        """Gets the match_score of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501


        :return: The match_score of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :rtype: int
        """
        return self._match_score

    @match_score.setter
    def match_score(self, match_score):
        """Sets the match_score of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.


        :param match_score: The match_score of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :type: int
        """

        self._match_score = match_score

    @property
    def match_score_alpha(self):
        """Gets the match_score_alpha of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501


        :return: The match_score_alpha of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :rtype: str
        """
        return self._match_score_alpha

    @match_score_alpha.setter
    def match_score_alpha(self, match_score_alpha):
        """Sets the match_score_alpha of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.


        :param match_score_alpha: The match_score_alpha of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :type: str
        """

        self._match_score_alpha = match_score_alpha

    @property
    def match_score_local_id(self):
        """Gets the match_score_local_id of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501


        :return: The match_score_local_id of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :rtype: str
        """
        return self._match_score_local_id

    @match_score_local_id.setter
    def match_score_local_id(self, match_score_local_id):
        """Sets the match_score_local_id of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.


        :param match_score_local_id: The match_score_local_id of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :type: str
        """

        self._match_score_local_id = match_score_local_id

    @property
    def match_score_name(self):
        """Gets the match_score_name of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501


        :return: The match_score_name of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :rtype: str
        """
        return self._match_score_name

    @match_score_name.setter
    def match_score_name(self, match_score_name):
        """Sets the match_score_name of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.


        :param match_score_name: The match_score_name of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :type: str
        """

        self._match_score_name = match_score_name

    @property
    def match_score_house_no(self):
        """Gets the match_score_house_no of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501


        :return: The match_score_house_no of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :rtype: str
        """
        return self._match_score_house_no

    @match_score_house_no.setter
    def match_score_house_no(self, match_score_house_no):
        """Sets the match_score_house_no of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.


        :param match_score_house_no: The match_score_house_no of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :type: str
        """

        self._match_score_house_no = match_score_house_no

    @property
    def match_score_street(self):
        """Gets the match_score_street of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501


        :return: The match_score_street of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :rtype: str
        """
        return self._match_score_street

    @match_score_street.setter
    def match_score_street(self, match_score_street):
        """Sets the match_score_street of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.


        :param match_score_street: The match_score_street of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :type: str
        """

        self._match_score_street = match_score_street

    @property
    def match_score_po_box(self):
        """Gets the match_score_po_box of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501


        :return: The match_score_po_box of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :rtype: str
        """
        return self._match_score_po_box

    @match_score_po_box.setter
    def match_score_po_box(self, match_score_po_box):
        """Sets the match_score_po_box of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.


        :param match_score_po_box: The match_score_po_box of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :type: str
        """

        self._match_score_po_box = match_score_po_box

    @property
    def match_score_city(self):
        """Gets the match_score_city of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501


        :return: The match_score_city of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :rtype: str
        """
        return self._match_score_city

    @match_score_city.setter
    def match_score_city(self, match_score_city):
        """Sets the match_score_city of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.


        :param match_score_city: The match_score_city of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :type: str
        """

        self._match_score_city = match_score_city

    @property
    def match_score_state(self):
        """Gets the match_score_state of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501


        :return: The match_score_state of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :rtype: str
        """
        return self._match_score_state

    @match_score_state.setter
    def match_score_state(self, match_score_state):
        """Sets the match_score_state of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.


        :param match_score_state: The match_score_state of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :type: str
        """

        self._match_score_state = match_score_state

    @property
    def match_score_post_code(self):
        """Gets the match_score_post_code of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501


        :return: The match_score_post_code of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :rtype: str
        """
        return self._match_score_post_code

    @match_score_post_code.setter
    def match_score_post_code(self, match_score_post_code):
        """Sets the match_score_post_code of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.


        :param match_score_post_code: The match_score_post_code of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :type: str
        """

        self._match_score_post_code = match_score_post_code

    @property
    def match_score_country(self):
        """Gets the match_score_country of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501


        :return: The match_score_country of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :rtype: str
        """
        return self._match_score_country

    @match_score_country.setter
    def match_score_country(self, match_score_country):
        """Sets the match_score_country of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.


        :param match_score_country: The match_score_country of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :type: str
        """

        self._match_score_country = match_score_country

    @property
    def match_score_vat_no(self):
        """Gets the match_score_vat_no of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501


        :return: The match_score_vat_no of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :rtype: str
        """
        return self._match_score_vat_no

    @match_score_vat_no.setter
    def match_score_vat_no(self, match_score_vat_no):
        """Sets the match_score_vat_no of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.


        :param match_score_vat_no: The match_score_vat_no of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :type: str
        """

        self._match_score_vat_no = match_score_vat_no

    @property
    def match_score_reg_no(self):
        """Gets the match_score_reg_no of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501


        :return: The match_score_reg_no of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :rtype: str
        """
        return self._match_score_reg_no

    @match_score_reg_no.setter
    def match_score_reg_no(self, match_score_reg_no):
        """Sets the match_score_reg_no of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.


        :param match_score_reg_no: The match_score_reg_no of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :type: str
        """

        self._match_score_reg_no = match_score_reg_no

    @property
    def match_score_phone_no(self):
        """Gets the match_score_phone_no of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501


        :return: The match_score_phone_no of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :rtype: str
        """
        return self._match_score_phone_no

    @match_score_phone_no.setter
    def match_score_phone_no(self, match_score_phone_no):
        """Sets the match_score_phone_no of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.


        :param match_score_phone_no: The match_score_phone_no of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :type: str
        """

        self._match_score_phone_no = match_score_phone_no

    @property
    def match_score_simple_value(self):
        """Gets the match_score_simple_value of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501


        :return: The match_score_simple_value of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :rtype: str
        """
        return self._match_score_simple_value

    @match_score_simple_value.setter
    def match_score_simple_value(self, match_score_simple_value):
        """Sets the match_score_simple_value of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.


        :param match_score_simple_value: The match_score_simple_value of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :type: str
        """

        self._match_score_simple_value = match_score_simple_value

    @property
    def match_score_num(self):
        """Gets the match_score_num of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501


        :return: The match_score_num of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :rtype: str
        """
        return self._match_score_num

    @match_score_num.setter
    def match_score_num(self, match_score_num):
        """Sets the match_score_num of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.


        :param match_score_num: The match_score_num of this ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan.  # noqa: E501
        :type: str
        """

        self._match_score_num = match_score_num

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
        if issubclass(ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan, dict):
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
        if not isinstance(other, ConnectConfidenceMatchMatchResultsMatchScoreExplainPlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

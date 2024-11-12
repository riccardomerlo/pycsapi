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

class ConnectDecisionEngineUserDataFieldsResponseFields(object):
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
        'order_index': 'float',
        'label': 'str',
        'param_name': 'str',
        'field_type': 'str',
        'mandatory': 'bool',
        'dropdown_details': 'list[ConnectDecisionEngineUserDataFieldsResponseDropdownDetails]',
        'validation': 'list[ConnectDecisionEngineUserDataFieldsResponseValidation]'
    }

    attribute_map = {
        'order_index': 'orderIndex',
        'label': 'label',
        'param_name': 'paramName',
        'field_type': 'fieldType',
        'mandatory': 'mandatory',
        'dropdown_details': 'dropdownDetails',
        'validation': 'validation'
    }

    def __init__(self, order_index=None, label=None, param_name=None, field_type=None, mandatory=None, dropdown_details=None, validation=None):  # noqa: E501
        """ConnectDecisionEngineUserDataFieldsResponseFields - a model defined in Swagger"""  # noqa: E501
        self._order_index = None
        self._label = None
        self._param_name = None
        self._field_type = None
        self._mandatory = None
        self._dropdown_details = None
        self._validation = None
        self.discriminator = None
        if order_index is not None:
            self.order_index = order_index
        if label is not None:
            self.label = label
        if param_name is not None:
            self.param_name = param_name
        if field_type is not None:
            self.field_type = field_type
        if mandatory is not None:
            self.mandatory = mandatory
        if dropdown_details is not None:
            self.dropdown_details = dropdown_details
        if validation is not None:
            self.validation = validation

    @property
    def order_index(self):
        """Gets the order_index of this ConnectDecisionEngineUserDataFieldsResponseFields.  # noqa: E501

        Used to assist ordering of the user data fields on a UI.  # noqa: E501

        :return: The order_index of this ConnectDecisionEngineUserDataFieldsResponseFields.  # noqa: E501
        :rtype: float
        """
        return self._order_index

    @order_index.setter
    def order_index(self, order_index):
        """Sets the order_index of this ConnectDecisionEngineUserDataFieldsResponseFields.

        Used to assist ordering of the user data fields on a UI.  # noqa: E501

        :param order_index: The order_index of this ConnectDecisionEngineUserDataFieldsResponseFields.  # noqa: E501
        :type: float
        """

        self._order_index = order_index

    @property
    def label(self):
        """Gets the label of this ConnectDecisionEngineUserDataFieldsResponseFields.  # noqa: E501

        The user-friendly label for the field for display on a UI.  # noqa: E501

        :return: The label of this ConnectDecisionEngineUserDataFieldsResponseFields.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ConnectDecisionEngineUserDataFieldsResponseFields.

        The user-friendly label for the field for display on a UI.  # noqa: E501

        :param label: The label of this ConnectDecisionEngineUserDataFieldsResponseFields.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def param_name(self):
        """Gets the param_name of this ConnectDecisionEngineUserDataFieldsResponseFields.  # noqa: E501

        The string value for the parameter to be used when calling the `/{guid}` endpoint.  # noqa: E501

        :return: The param_name of this ConnectDecisionEngineUserDataFieldsResponseFields.  # noqa: E501
        :rtype: str
        """
        return self._param_name

    @param_name.setter
    def param_name(self, param_name):
        """Sets the param_name of this ConnectDecisionEngineUserDataFieldsResponseFields.

        The string value for the parameter to be used when calling the `/{guid}` endpoint.  # noqa: E501

        :param param_name: The param_name of this ConnectDecisionEngineUserDataFieldsResponseFields.  # noqa: E501
        :type: str
        """

        self._param_name = param_name

    @property
    def field_type(self):
        """Gets the field_type of this ConnectDecisionEngineUserDataFieldsResponseFields.  # noqa: E501

        The type of user data field.  # noqa: E501

        :return: The field_type of this ConnectDecisionEngineUserDataFieldsResponseFields.  # noqa: E501
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        """Sets the field_type of this ConnectDecisionEngineUserDataFieldsResponseFields.

        The type of user data field.  # noqa: E501

        :param field_type: The field_type of this ConnectDecisionEngineUserDataFieldsResponseFields.  # noqa: E501
        :type: str
        """
        allowed_values = ["Text", "Integer", "Dropdown"]  # noqa: E501
        if field_type not in allowed_values:
            raise ValueError(
                "Invalid value for `field_type` ({0}), must be one of {1}"  # noqa: E501
                .format(field_type, allowed_values)
            )

        self._field_type = field_type

    @property
    def mandatory(self):
        """Gets the mandatory of this ConnectDecisionEngineUserDataFieldsResponseFields.  # noqa: E501

        Flag to dictate whether the user data field is required when running the associated decision tree.  # noqa: E501

        :return: The mandatory of this ConnectDecisionEngineUserDataFieldsResponseFields.  # noqa: E501
        :rtype: bool
        """
        return self._mandatory

    @mandatory.setter
    def mandatory(self, mandatory):
        """Sets the mandatory of this ConnectDecisionEngineUserDataFieldsResponseFields.

        Flag to dictate whether the user data field is required when running the associated decision tree.  # noqa: E501

        :param mandatory: The mandatory of this ConnectDecisionEngineUserDataFieldsResponseFields.  # noqa: E501
        :type: bool
        """

        self._mandatory = mandatory

    @property
    def dropdown_details(self):
        """Gets the dropdown_details of this ConnectDecisionEngineUserDataFieldsResponseFields.  # noqa: E501


        :return: The dropdown_details of this ConnectDecisionEngineUserDataFieldsResponseFields.  # noqa: E501
        :rtype: list[ConnectDecisionEngineUserDataFieldsResponseDropdownDetails]
        """
        return self._dropdown_details

    @dropdown_details.setter
    def dropdown_details(self, dropdown_details):
        """Sets the dropdown_details of this ConnectDecisionEngineUserDataFieldsResponseFields.


        :param dropdown_details: The dropdown_details of this ConnectDecisionEngineUserDataFieldsResponseFields.  # noqa: E501
        :type: list[ConnectDecisionEngineUserDataFieldsResponseDropdownDetails]
        """

        self._dropdown_details = dropdown_details

    @property
    def validation(self):
        """Gets the validation of this ConnectDecisionEngineUserDataFieldsResponseFields.  # noqa: E501

        Optional validation rules that should be applied to the corresponding user data field prior to running the decision tree.  # noqa: E501

        :return: The validation of this ConnectDecisionEngineUserDataFieldsResponseFields.  # noqa: E501
        :rtype: list[ConnectDecisionEngineUserDataFieldsResponseValidation]
        """
        return self._validation

    @validation.setter
    def validation(self, validation):
        """Sets the validation of this ConnectDecisionEngineUserDataFieldsResponseFields.

        Optional validation rules that should be applied to the corresponding user data field prior to running the decision tree.  # noqa: E501

        :param validation: The validation of this ConnectDecisionEngineUserDataFieldsResponseFields.  # noqa: E501
        :type: list[ConnectDecisionEngineUserDataFieldsResponseValidation]
        """

        self._validation = validation

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
        if issubclass(ConnectDecisionEngineUserDataFieldsResponseFields, dict):
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
        if not isinstance(other, ConnectDecisionEngineUserDataFieldsResponseFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

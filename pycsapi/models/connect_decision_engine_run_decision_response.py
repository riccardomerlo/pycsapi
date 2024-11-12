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

class ConnectDecisionEngineRunDecisionResponse(object):
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
        'decision': 'str',
        'decision_text': 'str',
        'audits': 'list[ConnectDecisionEngineRunDecisionResponseAudits]',
        'origination_id': 'str',
        'status_code': 'str'
    }

    attribute_map = {
        'decision': 'Decision',
        'decision_text': 'DecisionText',
        'audits': 'Audits',
        'origination_id': 'originationId',
        'status_code': 'statusCode'
    }

    def __init__(self, decision=None, decision_text=None, audits=None, origination_id=None, status_code=None):  # noqa: E501
        """ConnectDecisionEngineRunDecisionResponse - a model defined in Swagger"""  # noqa: E501
        self._decision = None
        self._decision_text = None
        self._audits = None
        self._origination_id = None
        self._status_code = None
        self.discriminator = None
        if decision is not None:
            self.decision = decision
        if decision_text is not None:
            self.decision_text = decision_text
        if audits is not None:
            self.audits = audits
        if origination_id is not None:
            self.origination_id = origination_id
        if status_code is not None:
            self.status_code = status_code

    @property
    def decision(self):
        """Gets the decision of this ConnectDecisionEngineRunDecisionResponse.  # noqa: E501

        The decision returned by the automated decision model.  # noqa: E501

        :return: The decision of this ConnectDecisionEngineRunDecisionResponse.  # noqa: E501
        :rtype: str
        """
        return self._decision

    @decision.setter
    def decision(self, decision):
        """Sets the decision of this ConnectDecisionEngineRunDecisionResponse.

        The decision returned by the automated decision model.  # noqa: E501

        :param decision: The decision of this ConnectDecisionEngineRunDecisionResponse.  # noqa: E501
        :type: str
        """

        self._decision = decision

    @property
    def decision_text(self):
        """Gets the decision_text of this ConnectDecisionEngineRunDecisionResponse.  # noqa: E501

        The text output to accompany the decision returned by the decision model.  # noqa: E501

        :return: The decision_text of this ConnectDecisionEngineRunDecisionResponse.  # noqa: E501
        :rtype: str
        """
        return self._decision_text

    @decision_text.setter
    def decision_text(self, decision_text):
        """Sets the decision_text of this ConnectDecisionEngineRunDecisionResponse.

        The text output to accompany the decision returned by the decision model.  # noqa: E501

        :param decision_text: The decision_text of this ConnectDecisionEngineRunDecisionResponse.  # noqa: E501
        :type: str
        """

        self._decision_text = decision_text

    @property
    def audits(self):
        """Gets the audits of this ConnectDecisionEngineRunDecisionResponse.  # noqa: E501

        An array of audit values. The parameters output for audit are tailored and bespoke to each decision tree.  # noqa: E501

        :return: The audits of this ConnectDecisionEngineRunDecisionResponse.  # noqa: E501
        :rtype: list[ConnectDecisionEngineRunDecisionResponseAudits]
        """
        return self._audits

    @audits.setter
    def audits(self, audits):
        """Sets the audits of this ConnectDecisionEngineRunDecisionResponse.

        An array of audit values. The parameters output for audit are tailored and bespoke to each decision tree.  # noqa: E501

        :param audits: The audits of this ConnectDecisionEngineRunDecisionResponse.  # noqa: E501
        :type: list[ConnectDecisionEngineRunDecisionResponseAudits]
        """

        self._audits = audits

    @property
    def origination_id(self):
        """Gets the origination_id of this ConnectDecisionEngineRunDecisionResponse.  # noqa: E501

        Displays the optional text passed through to be stored against the decision in the original call to `/{provenirId}`. Typically used for internal identifiers (e.g. SalesForce IDs).  # noqa: E501

        :return: The origination_id of this ConnectDecisionEngineRunDecisionResponse.  # noqa: E501
        :rtype: str
        """
        return self._origination_id

    @origination_id.setter
    def origination_id(self, origination_id):
        """Sets the origination_id of this ConnectDecisionEngineRunDecisionResponse.

        Displays the optional text passed through to be stored against the decision in the original call to `/{provenirId}`. Typically used for internal identifiers (e.g. SalesForce IDs).  # noqa: E501

        :param origination_id: The origination_id of this ConnectDecisionEngineRunDecisionResponse.  # noqa: E501
        :type: str
        """

        self._origination_id = origination_id

    @property
    def status_code(self):
        """Gets the status_code of this ConnectDecisionEngineRunDecisionResponse.  # noqa: E501

        The status of the decision. typically, 1 is reserved for positive outcomes, 2 for pending status and 3 for negative outcomes.  # noqa: E501

        :return: The status_code of this ConnectDecisionEngineRunDecisionResponse.  # noqa: E501
        :rtype: str
        """
        return self._status_code

    @status_code.setter
    def status_code(self, status_code):
        """Sets the status_code of this ConnectDecisionEngineRunDecisionResponse.

        The status of the decision. typically, 1 is reserved for positive outcomes, 2 for pending status and 3 for negative outcomes.  # noqa: E501

        :param status_code: The status_code of this ConnectDecisionEngineRunDecisionResponse.  # noqa: E501
        :type: str
        """

        self._status_code = status_code

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
        if issubclass(ConnectDecisionEngineRunDecisionResponse, dict):
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
        if not isinstance(other, ConnectDecisionEngineRunDecisionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

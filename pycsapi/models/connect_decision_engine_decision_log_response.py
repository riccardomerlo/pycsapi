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

class ConnectDecisionEngineDecisionLogResponse(object):
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
        'decision_log_id': 'float',
        'provenir_id': 'str',
        'friendly_name': 'str',
        'user_id': 'float',
        'company_id': 'str',
        'company_name': 'str',
        'response': 'ConnectDecisionEngineDecisionLogResponseResponse',
        'decision_date': 'datetime',
        'origination_id': 'str',
        'status': 'float',
        'notes': 'str',
        'modified_date': 'datetime'
    }

    attribute_map = {
        'correlation_id': 'correlationId',
        'decision_log_id': 'decisionLogId',
        'provenir_id': 'provenirId',
        'friendly_name': 'friendlyName',
        'user_id': 'userId',
        'company_id': 'companyId',
        'company_name': 'companyName',
        'response': 'response',
        'decision_date': 'decisionDate',
        'origination_id': 'originationId',
        'status': 'status',
        'notes': 'notes',
        'modified_date': 'modifiedDate'
    }

    def __init__(self, correlation_id=None, decision_log_id=None, provenir_id=None, friendly_name=None, user_id=None, company_id=None, company_name=None, response=None, decision_date=None, origination_id=None, status=None, notes=None, modified_date=None):  # noqa: E501
        """ConnectDecisionEngineDecisionLogResponse - a model defined in Swagger"""  # noqa: E501
        self._correlation_id = None
        self._decision_log_id = None
        self._provenir_id = None
        self._friendly_name = None
        self._user_id = None
        self._company_id = None
        self._company_name = None
        self._response = None
        self._decision_date = None
        self._origination_id = None
        self._status = None
        self._notes = None
        self._modified_date = None
        self.discriminator = None
        if correlation_id is not None:
            self.correlation_id = correlation_id
        if decision_log_id is not None:
            self.decision_log_id = decision_log_id
        if provenir_id is not None:
            self.provenir_id = provenir_id
        if friendly_name is not None:
            self.friendly_name = friendly_name
        if user_id is not None:
            self.user_id = user_id
        if company_id is not None:
            self.company_id = company_id
        if company_name is not None:
            self.company_name = company_name
        if response is not None:
            self.response = response
        if decision_date is not None:
            self.decision_date = decision_date
        if origination_id is not None:
            self.origination_id = origination_id
        if status is not None:
            self.status = status
        if notes is not None:
            self.notes = notes
        if modified_date is not None:
            self.modified_date = modified_date

    @property
    def correlation_id(self):
        """Gets the correlation_id of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501

        A unique ID assigned to this request.  # noqa: E501

        :return: The correlation_id of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this ConnectDecisionEngineDecisionLogResponse.

        A unique ID assigned to this request.  # noqa: E501

        :param correlation_id: The correlation_id of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :type: str
        """

        self._correlation_id = correlation_id

    @property
    def decision_log_id(self):
        """Gets the decision_log_id of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501

        The unique identifier for the decision log.  # noqa: E501

        :return: The decision_log_id of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :rtype: float
        """
        return self._decision_log_id

    @decision_log_id.setter
    def decision_log_id(self, decision_log_id):
        """Sets the decision_log_id of this ConnectDecisionEngineDecisionLogResponse.

        The unique identifier for the decision log.  # noqa: E501

        :param decision_log_id: The decision_log_id of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :type: float
        """

        self._decision_log_id = decision_log_id

    @property
    def provenir_id(self):
        """Gets the provenir_id of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501

        The unique identifier of the decision tree.  # noqa: E501

        :return: The provenir_id of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._provenir_id

    @provenir_id.setter
    def provenir_id(self, provenir_id):
        """Sets the provenir_id of this ConnectDecisionEngineDecisionLogResponse.

        The unique identifier of the decision tree.  # noqa: E501

        :param provenir_id: The provenir_id of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :type: str
        """

        self._provenir_id = provenir_id

    @property
    def friendly_name(self):
        """Gets the friendly_name of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501

        The name of the decision tree.  # noqa: E501

        :return: The friendly_name of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, friendly_name):
        """Sets the friendly_name of this ConnectDecisionEngineDecisionLogResponse.

        The name of the decision tree.  # noqa: E501

        :param friendly_name: The friendly_name of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :type: str
        """

        self._friendly_name = friendly_name

    @property
    def user_id(self):
        """Gets the user_id of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501

        The unique identifier for the user's account, used across the Creditsafe product suite.  # noqa: E501

        :return: The user_id of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :rtype: float
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ConnectDecisionEngineDecisionLogResponse.

        The unique identifier for the user's account, used across the Creditsafe product suite.  # noqa: E501

        :param user_id: The user_id of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :type: float
        """

        self._user_id = user_id

    @property
    def company_id(self):
        """Gets the company_id of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501

        The connectId of the company that the decision was ran on. A connectId is the primary Company identifier that is used to uniquely identify all companies across Creditsafe's Universe and Partner Network.  # noqa: E501

        :return: The company_id of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._company_id

    @company_id.setter
    def company_id(self, company_id):
        """Sets the company_id of this ConnectDecisionEngineDecisionLogResponse.

        The connectId of the company that the decision was ran on. A connectId is the primary Company identifier that is used to uniquely identify all companies across Creditsafe's Universe and Partner Network.  # noqa: E501

        :param company_id: The company_id of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :type: str
        """

        self._company_id = company_id

    @property
    def company_name(self):
        """Gets the company_name of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501

        The name of the company that the decision was ran on.  # noqa: E501

        :return: The company_name of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ConnectDecisionEngineDecisionLogResponse.

        The name of the company that the decision was ran on.  # noqa: E501

        :param company_name: The company_name of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def response(self):
        """Gets the response of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501


        :return: The response of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :rtype: ConnectDecisionEngineDecisionLogResponseResponse
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this ConnectDecisionEngineDecisionLogResponse.


        :param response: The response of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :type: ConnectDecisionEngineDecisionLogResponseResponse
        """

        self._response = response

    @property
    def decision_date(self):
        """Gets the decision_date of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501

        The timestamp that the decision model was run.  # noqa: E501

        :return: The decision_date of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._decision_date

    @decision_date.setter
    def decision_date(self, decision_date):
        """Sets the decision_date of this ConnectDecisionEngineDecisionLogResponse.

        The timestamp that the decision model was run.  # noqa: E501

        :param decision_date: The decision_date of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :type: datetime
        """

        self._decision_date = decision_date

    @property
    def origination_id(self):
        """Gets the origination_id of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501

        Displays the optional text passed through to be stored against the decision in the original call to `/{provenirId}`. Typically used for internal identifiers (e.g. SalesForce IDs).  # noqa: E501

        :return: The origination_id of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._origination_id

    @origination_id.setter
    def origination_id(self, origination_id):
        """Sets the origination_id of this ConnectDecisionEngineDecisionLogResponse.

        Displays the optional text passed through to be stored against the decision in the original call to `/{provenirId}`. Typically used for internal identifiers (e.g. SalesForce IDs).  # noqa: E501

        :param origination_id: The origination_id of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :type: str
        """

        self._origination_id = origination_id

    @property
    def status(self):
        """Gets the status of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501

        The status of the decision. typically, 1 is reserved for positive outcomes, 2 for pending status and 3 for negative outcomes.  # noqa: E501

        :return: The status of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :rtype: float
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConnectDecisionEngineDecisionLogResponse.

        The status of the decision. typically, 1 is reserved for positive outcomes, 2 for pending status and 3 for negative outcomes.  # noqa: E501

        :param status: The status of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :type: float
        """

        self._status = status

    @property
    def notes(self):
        """Gets the notes of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501

        The notes associated with this decision.  # noqa: E501

        :return: The notes of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this ConnectDecisionEngineDecisionLogResponse.

        The notes associated with this decision.  # noqa: E501

        :param notes: The notes of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def modified_date(self):
        """Gets the modified_date of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501

        The timestamp that this decision was last modified.  # noqa: E501

        :return: The modified_date of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        """Sets the modified_date of this ConnectDecisionEngineDecisionLogResponse.

        The timestamp that this decision was last modified.  # noqa: E501

        :param modified_date: The modified_date of this ConnectDecisionEngineDecisionLogResponse.  # noqa: E501
        :type: datetime
        """

        self._modified_date = modified_date

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
        if issubclass(ConnectDecisionEngineDecisionLogResponse, dict):
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
        if not isinstance(other, ConnectDecisionEngineDecisionLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

class ConnectFreshInvListInvestigationsOrders(object):
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
        'order_id': 'int',
        'user_id': 'str',
        'creation_date': 'str',
        'last_status_change_date': 'str',
        'transaction_id': 'int',
        'charge_reference': 'str',
        'contact_details': 'ConnectFreshInvListInvestigationsContactDetails',
        'section_names': 'str',
        'status': 'ConnectFreshInvListInvestigationsStatus',
        'consent': 'bool',
        'search_criteria': 'ConnectFreshInvListInvestigationsSearchCriteria',
        'report_date': 'datetime'
    }

    attribute_map = {
        'order_id': 'orderID',
        'user_id': 'userID',
        'creation_date': 'creationDate',
        'last_status_change_date': 'lastStatusChangeDate',
        'transaction_id': 'transactionID',
        'charge_reference': 'chargeReference',
        'contact_details': 'contactDetails',
        'section_names': 'sectionNames',
        'status': 'status',
        'consent': 'consent',
        'search_criteria': 'searchCriteria',
        'report_date': 'reportDate'
    }

    def __init__(self, order_id=None, user_id=None, creation_date=None, last_status_change_date=None, transaction_id=None, charge_reference=None, contact_details=None, section_names=None, status=None, consent=None, search_criteria=None, report_date=None):  # noqa: E501
        """ConnectFreshInvListInvestigationsOrders - a model defined in Swagger"""  # noqa: E501
        self._order_id = None
        self._user_id = None
        self._creation_date = None
        self._last_status_change_date = None
        self._transaction_id = None
        self._charge_reference = None
        self._contact_details = None
        self._section_names = None
        self._status = None
        self._consent = None
        self._search_criteria = None
        self._report_date = None
        self.discriminator = None
        if order_id is not None:
            self.order_id = order_id
        if user_id is not None:
            self.user_id = user_id
        if creation_date is not None:
            self.creation_date = creation_date
        if last_status_change_date is not None:
            self.last_status_change_date = last_status_change_date
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if charge_reference is not None:
            self.charge_reference = charge_reference
        if contact_details is not None:
            self.contact_details = contact_details
        if section_names is not None:
            self.section_names = section_names
        if status is not None:
            self.status = status
        if consent is not None:
            self.consent = consent
        if search_criteria is not None:
            self.search_criteria = search_criteria
        if report_date is not None:
            self.report_date = report_date

    @property
    def order_id(self):
        """Gets the order_id of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501

        Fresh Investigation Unique Identifier  # noqa: E501

        :return: The order_id of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :rtype: int
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ConnectFreshInvListInvestigationsOrders.

        Fresh Investigation Unique Identifier  # noqa: E501

        :param order_id: The order_id of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :type: int
        """

        self._order_id = order_id

    @property
    def user_id(self):
        """Gets the user_id of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501

        Fresh Investigation user Identifier  # noqa: E501

        :return: The user_id of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ConnectFreshInvListInvestigationsOrders.

        Fresh Investigation user Identifier  # noqa: E501

        :param user_id: The user_id of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def creation_date(self):
        """Gets the creation_date of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501

        Fresh Investigation Creation Date  # noqa: E501

        :return: The creation_date of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this ConnectFreshInvListInvestigationsOrders.

        Fresh Investigation Creation Date  # noqa: E501

        :param creation_date: The creation_date of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :type: str
        """

        self._creation_date = creation_date

    @property
    def last_status_change_date(self):
        """Gets the last_status_change_date of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501

        Fresh Investigation Last Status Change Date  # noqa: E501

        :return: The last_status_change_date of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :rtype: str
        """
        return self._last_status_change_date

    @last_status_change_date.setter
    def last_status_change_date(self, last_status_change_date):
        """Sets the last_status_change_date of this ConnectFreshInvListInvestigationsOrders.

        Fresh Investigation Last Status Change Date  # noqa: E501

        :param last_status_change_date: The last_status_change_date of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :type: str
        """

        self._last_status_change_date = last_status_change_date

    @property
    def transaction_id(self):
        """Gets the transaction_id of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501

        Fresh Investigation Internal Identifier  # noqa: E501

        :return: The transaction_id of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :rtype: int
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this ConnectFreshInvListInvestigationsOrders.

        Fresh Investigation Internal Identifier  # noqa: E501

        :param transaction_id: The transaction_id of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :type: int
        """

        self._transaction_id = transaction_id

    @property
    def charge_reference(self):
        """Gets the charge_reference of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501


        :return: The charge_reference of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :rtype: str
        """
        return self._charge_reference

    @charge_reference.setter
    def charge_reference(self, charge_reference):
        """Sets the charge_reference of this ConnectFreshInvListInvestigationsOrders.


        :param charge_reference: The charge_reference of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :type: str
        """

        self._charge_reference = charge_reference

    @property
    def contact_details(self):
        """Gets the contact_details of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501


        :return: The contact_details of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :rtype: ConnectFreshInvListInvestigationsContactDetails
        """
        return self._contact_details

    @contact_details.setter
    def contact_details(self, contact_details):
        """Sets the contact_details of this ConnectFreshInvListInvestigationsOrders.


        :param contact_details: The contact_details of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :type: ConnectFreshInvListInvestigationsContactDetails
        """

        self._contact_details = contact_details

    @property
    def section_names(self):
        """Gets the section_names of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501


        :return: The section_names of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :rtype: str
        """
        return self._section_names

    @section_names.setter
    def section_names(self, section_names):
        """Sets the section_names of this ConnectFreshInvListInvestigationsOrders.


        :param section_names: The section_names of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :type: str
        """

        self._section_names = section_names

    @property
    def status(self):
        """Gets the status of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501


        :return: The status of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :rtype: ConnectFreshInvListInvestigationsStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConnectFreshInvListInvestigationsOrders.


        :param status: The status of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :type: ConnectFreshInvListInvestigationsStatus
        """

        self._status = status

    @property
    def consent(self):
        """Gets the consent of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501

        Whether permission was granted by the requesting company to disclose the identity of the investigating party to the target company.  # noqa: E501

        :return: The consent of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :rtype: bool
        """
        return self._consent

    @consent.setter
    def consent(self, consent):
        """Sets the consent of this ConnectFreshInvListInvestigationsOrders.

        Whether permission was granted by the requesting company to disclose the identity of the investigating party to the target company.  # noqa: E501

        :param consent: The consent of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :type: bool
        """

        self._consent = consent

    @property
    def search_criteria(self):
        """Gets the search_criteria of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501


        :return: The search_criteria of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :rtype: ConnectFreshInvListInvestigationsSearchCriteria
        """
        return self._search_criteria

    @search_criteria.setter
    def search_criteria(self, search_criteria):
        """Sets the search_criteria of this ConnectFreshInvListInvestigationsOrders.


        :param search_criteria: The search_criteria of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :type: ConnectFreshInvListInvestigationsSearchCriteria
        """

        self._search_criteria = search_criteria

    @property
    def report_date(self):
        """Gets the report_date of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501


        :return: The report_date of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :rtype: datetime
        """
        return self._report_date

    @report_date.setter
    def report_date(self, report_date):
        """Sets the report_date of this ConnectFreshInvListInvestigationsOrders.


        :param report_date: The report_date of this ConnectFreshInvListInvestigationsOrders.  # noqa: E501
        :type: datetime
        """

        self._report_date = report_date

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
        if issubclass(ConnectFreshInvListInvestigationsOrders, dict):
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
        if not isinstance(other, ConnectFreshInvListInvestigationsOrders):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

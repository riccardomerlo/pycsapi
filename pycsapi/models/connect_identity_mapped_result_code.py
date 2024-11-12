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

class ConnectIdentityMappedResultCode(object):
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
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'address': 'ConnectIdentityMatchValue',
        'alert': 'ConnectIdentityMatchValue',
        'date_of_birth': 'ConnectIdentityMatchValue',
        'forename': 'ConnectIdentityMatchValue',
        'surname': 'ConnectIdentityMatchValue',
        '_pass': 'ConnectIdentityMatchValue',
        'comments': 'list[ConnectIdentityMappedResultCodeDetails]',
        'match': 'list[ConnectIdentityMappedResultCodeDetails]',
        'mis_match': 'list[ConnectIdentityMappedResultCodeDetails]',
        'sanctions': 'list[ConnectIdentityMappedSanctionMatch]',
        'peps': 'list[ConnectIdentityMappedPepMatch]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'address': 'address',
        'alert': 'alert',
        'date_of_birth': 'dateOfBirth',
        'forename': 'forename',
        'surname': 'surname',
        '_pass': 'pass',
        'comments': 'comments',
        'match': 'match',
        'mis_match': 'misMatch',
        'sanctions': 'sanctions',
        'peps': 'peps'
    }

    def __init__(self, id=None, name=None, description=None, address=None, alert=None, date_of_birth=None, forename=None, surname=None, _pass=None, comments=None, match=None, mis_match=None, sanctions=None, peps=None):  # noqa: E501
        """ConnectIdentityMappedResultCode - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._address = None
        self._alert = None
        self._date_of_birth = None
        self._forename = None
        self._surname = None
        self.__pass = None
        self._comments = None
        self._match = None
        self._mis_match = None
        self._sanctions = None
        self._peps = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if address is not None:
            self.address = address
        if alert is not None:
            self.alert = alert
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if forename is not None:
            self.forename = forename
        if surname is not None:
            self.surname = surname
        if _pass is not None:
            self._pass = _pass
        if comments is not None:
            self.comments = comments
        if match is not None:
            self.match = match
        if mis_match is not None:
            self.mis_match = mis_match
        if sanctions is not None:
            self.sanctions = sanctions
        if peps is not None:
            self.peps = peps

    @property
    def id(self):
        """Gets the id of this ConnectIdentityMappedResultCode.  # noqa: E501


        :return: The id of this ConnectIdentityMappedResultCode.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConnectIdentityMappedResultCode.


        :param id: The id of this ConnectIdentityMappedResultCode.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ConnectIdentityMappedResultCode.  # noqa: E501


        :return: The name of this ConnectIdentityMappedResultCode.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConnectIdentityMappedResultCode.


        :param name: The name of this ConnectIdentityMappedResultCode.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this ConnectIdentityMappedResultCode.  # noqa: E501


        :return: The description of this ConnectIdentityMappedResultCode.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConnectIdentityMappedResultCode.


        :param description: The description of this ConnectIdentityMappedResultCode.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def address(self):
        """Gets the address of this ConnectIdentityMappedResultCode.  # noqa: E501


        :return: The address of this ConnectIdentityMappedResultCode.  # noqa: E501
        :rtype: ConnectIdentityMatchValue
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ConnectIdentityMappedResultCode.


        :param address: The address of this ConnectIdentityMappedResultCode.  # noqa: E501
        :type: ConnectIdentityMatchValue
        """

        self._address = address

    @property
    def alert(self):
        """Gets the alert of this ConnectIdentityMappedResultCode.  # noqa: E501


        :return: The alert of this ConnectIdentityMappedResultCode.  # noqa: E501
        :rtype: ConnectIdentityMatchValue
        """
        return self._alert

    @alert.setter
    def alert(self, alert):
        """Sets the alert of this ConnectIdentityMappedResultCode.


        :param alert: The alert of this ConnectIdentityMappedResultCode.  # noqa: E501
        :type: ConnectIdentityMatchValue
        """

        self._alert = alert

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this ConnectIdentityMappedResultCode.  # noqa: E501


        :return: The date_of_birth of this ConnectIdentityMappedResultCode.  # noqa: E501
        :rtype: ConnectIdentityMatchValue
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this ConnectIdentityMappedResultCode.


        :param date_of_birth: The date_of_birth of this ConnectIdentityMappedResultCode.  # noqa: E501
        :type: ConnectIdentityMatchValue
        """

        self._date_of_birth = date_of_birth

    @property
    def forename(self):
        """Gets the forename of this ConnectIdentityMappedResultCode.  # noqa: E501


        :return: The forename of this ConnectIdentityMappedResultCode.  # noqa: E501
        :rtype: ConnectIdentityMatchValue
        """
        return self._forename

    @forename.setter
    def forename(self, forename):
        """Sets the forename of this ConnectIdentityMappedResultCode.


        :param forename: The forename of this ConnectIdentityMappedResultCode.  # noqa: E501
        :type: ConnectIdentityMatchValue
        """

        self._forename = forename

    @property
    def surname(self):
        """Gets the surname of this ConnectIdentityMappedResultCode.  # noqa: E501


        :return: The surname of this ConnectIdentityMappedResultCode.  # noqa: E501
        :rtype: ConnectIdentityMatchValue
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this ConnectIdentityMappedResultCode.


        :param surname: The surname of this ConnectIdentityMappedResultCode.  # noqa: E501
        :type: ConnectIdentityMatchValue
        """

        self._surname = surname

    @property
    def _pass(self):
        """Gets the _pass of this ConnectIdentityMappedResultCode.  # noqa: E501


        :return: The _pass of this ConnectIdentityMappedResultCode.  # noqa: E501
        :rtype: ConnectIdentityMatchValue
        """
        return self.__pass

    @_pass.setter
    def _pass(self, _pass):
        """Sets the _pass of this ConnectIdentityMappedResultCode.


        :param _pass: The _pass of this ConnectIdentityMappedResultCode.  # noqa: E501
        :type: ConnectIdentityMatchValue
        """

        self.__pass = _pass

    @property
    def comments(self):
        """Gets the comments of this ConnectIdentityMappedResultCode.  # noqa: E501


        :return: The comments of this ConnectIdentityMappedResultCode.  # noqa: E501
        :rtype: list[ConnectIdentityMappedResultCodeDetails]
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this ConnectIdentityMappedResultCode.


        :param comments: The comments of this ConnectIdentityMappedResultCode.  # noqa: E501
        :type: list[ConnectIdentityMappedResultCodeDetails]
        """

        self._comments = comments

    @property
    def match(self):
        """Gets the match of this ConnectIdentityMappedResultCode.  # noqa: E501


        :return: The match of this ConnectIdentityMappedResultCode.  # noqa: E501
        :rtype: list[ConnectIdentityMappedResultCodeDetails]
        """
        return self._match

    @match.setter
    def match(self, match):
        """Sets the match of this ConnectIdentityMappedResultCode.


        :param match: The match of this ConnectIdentityMappedResultCode.  # noqa: E501
        :type: list[ConnectIdentityMappedResultCodeDetails]
        """

        self._match = match

    @property
    def mis_match(self):
        """Gets the mis_match of this ConnectIdentityMappedResultCode.  # noqa: E501


        :return: The mis_match of this ConnectIdentityMappedResultCode.  # noqa: E501
        :rtype: list[ConnectIdentityMappedResultCodeDetails]
        """
        return self._mis_match

    @mis_match.setter
    def mis_match(self, mis_match):
        """Sets the mis_match of this ConnectIdentityMappedResultCode.


        :param mis_match: The mis_match of this ConnectIdentityMappedResultCode.  # noqa: E501
        :type: list[ConnectIdentityMappedResultCodeDetails]
        """

        self._mis_match = mis_match

    @property
    def sanctions(self):
        """Gets the sanctions of this ConnectIdentityMappedResultCode.  # noqa: E501


        :return: The sanctions of this ConnectIdentityMappedResultCode.  # noqa: E501
        :rtype: list[ConnectIdentityMappedSanctionMatch]
        """
        return self._sanctions

    @sanctions.setter
    def sanctions(self, sanctions):
        """Sets the sanctions of this ConnectIdentityMappedResultCode.


        :param sanctions: The sanctions of this ConnectIdentityMappedResultCode.  # noqa: E501
        :type: list[ConnectIdentityMappedSanctionMatch]
        """

        self._sanctions = sanctions

    @property
    def peps(self):
        """Gets the peps of this ConnectIdentityMappedResultCode.  # noqa: E501


        :return: The peps of this ConnectIdentityMappedResultCode.  # noqa: E501
        :rtype: list[ConnectIdentityMappedPepMatch]
        """
        return self._peps

    @peps.setter
    def peps(self, peps):
        """Sets the peps of this ConnectIdentityMappedResultCode.


        :param peps: The peps of this ConnectIdentityMappedResultCode.  # noqa: E501
        :type: list[ConnectIdentityMappedPepMatch]
        """

        self._peps = peps

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
        if issubclass(ConnectIdentityMappedResultCode, dict):
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
        if not isinstance(other, ConnectIdentityMappedResultCode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

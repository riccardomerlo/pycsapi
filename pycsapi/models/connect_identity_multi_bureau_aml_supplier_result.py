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

class ConnectIdentityMultiBureauAmlSupplierResult(object):
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
        'band_text': 'str',
        'birth_index_match': 'bool',
        'no_retry': 'bool',
        'result_codes': 'ConnectIdentityMultiBureauAmlSupplierResultResultCodes',
        'score': 'int',
        'search_text': 'str',
        'legacy_unique_id': 'str',
        'validation_id': 'str',
        'has_alerts': 'bool',
        'success': 'bool',
        'credits_incurred': 'int'
    }

    attribute_map = {
        'band_text': 'bandText',
        'birth_index_match': 'birthIndexMatch',
        'no_retry': 'noRetry',
        'result_codes': 'resultCodes',
        'score': 'score',
        'search_text': 'searchText',
        'legacy_unique_id': 'legacyUniqueID',
        'validation_id': 'validationID',
        'has_alerts': 'hasAlerts',
        'success': 'success',
        'credits_incurred': 'creditsIncurred'
    }

    def __init__(self, band_text=None, birth_index_match=None, no_retry=None, result_codes=None, score=None, search_text=None, legacy_unique_id=None, validation_id=None, has_alerts=None, success=None, credits_incurred=None):  # noqa: E501
        """ConnectIdentityMultiBureauAmlSupplierResult - a model defined in Swagger"""  # noqa: E501
        self._band_text = None
        self._birth_index_match = None
        self._no_retry = None
        self._result_codes = None
        self._score = None
        self._search_text = None
        self._legacy_unique_id = None
        self._validation_id = None
        self._has_alerts = None
        self._success = None
        self._credits_incurred = None
        self.discriminator = None
        if band_text is not None:
            self.band_text = band_text
        if birth_index_match is not None:
            self.birth_index_match = birth_index_match
        if no_retry is not None:
            self.no_retry = no_retry
        if result_codes is not None:
            self.result_codes = result_codes
        if score is not None:
            self.score = score
        if search_text is not None:
            self.search_text = search_text
        if legacy_unique_id is not None:
            self.legacy_unique_id = legacy_unique_id
        if validation_id is not None:
            self.validation_id = validation_id
        if has_alerts is not None:
            self.has_alerts = has_alerts
        if success is not None:
            self.success = success
        if credits_incurred is not None:
            self.credits_incurred = credits_incurred

    @property
    def band_text(self):
        """Gets the band_text of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501

        A descriptive label or category assigned based on the results of the AML checks. Typically, this text will indicate the level of risk or compliance category identified through the verification process.  # noqa: E501

        :return: The band_text of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :rtype: str
        """
        return self._band_text

    @band_text.setter
    def band_text(self, band_text):
        """Sets the band_text of this ConnectIdentityMultiBureauAmlSupplierResult.

        A descriptive label or category assigned based on the results of the AML checks. Typically, this text will indicate the level of risk or compliance category identified through the verification process.  # noqa: E501

        :param band_text: The band_text of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :type: str
        """

        self._band_text = band_text

    @property
    def birth_index_match(self):
        """Gets the birth_index_match of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501

        Indicates whether there was a match found in the birth index database, a critical aspect of verifying an individual's identity against official records.  # noqa: E501

        :return: The birth_index_match of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :rtype: bool
        """
        return self._birth_index_match

    @birth_index_match.setter
    def birth_index_match(self, birth_index_match):
        """Sets the birth_index_match of this ConnectIdentityMultiBureauAmlSupplierResult.

        Indicates whether there was a match found in the birth index database, a critical aspect of verifying an individual's identity against official records.  # noqa: E501

        :param birth_index_match: The birth_index_match of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :type: bool
        """

        self._birth_index_match = birth_index_match

    @property
    def no_retry(self):
        """Gets the no_retry of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501

        A flag to indicate whether the AML process should not be retried for this individual. This can be set to true in scenarios where repeated verification attempts are unlikely to yield different results.  # noqa: E501

        :return: The no_retry of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :rtype: bool
        """
        return self._no_retry

    @no_retry.setter
    def no_retry(self, no_retry):
        """Sets the no_retry of this ConnectIdentityMultiBureauAmlSupplierResult.

        A flag to indicate whether the AML process should not be retried for this individual. This can be set to true in scenarios where repeated verification attempts are unlikely to yield different results.  # noqa: E501

        :param no_retry: The no_retry of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :type: bool
        """

        self._no_retry = no_retry

    @property
    def result_codes(self):
        """Gets the result_codes of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501


        :return: The result_codes of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :rtype: ConnectIdentityMultiBureauAmlSupplierResultResultCodes
        """
        return self._result_codes

    @result_codes.setter
    def result_codes(self, result_codes):
        """Sets the result_codes of this ConnectIdentityMultiBureauAmlSupplierResult.


        :param result_codes: The result_codes of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :type: ConnectIdentityMultiBureauAmlSupplierResultResultCodes
        """

        self._result_codes = result_codes

    @property
    def score(self):
        """Gets the score of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501

        A numerical value representing the calculated risk score or validation level derived from the AML checks. This score can guide decision-making processes regarding the subject's verification status.  # noqa: E501

        :return: The score of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this ConnectIdentityMultiBureauAmlSupplierResult.

        A numerical value representing the calculated risk score or validation level derived from the AML checks. This score can guide decision-making processes regarding the subject's verification status.  # noqa: E501

        :param score: The score of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :type: int
        """

        self._score = score

    @property
    def search_text(self):
        """Gets the search_text of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501

        The exact query text used in the search, allowing for audit and review of the search parameters and terms used.  # noqa: E501

        :return: The search_text of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :rtype: str
        """
        return self._search_text

    @search_text.setter
    def search_text(self, search_text):
        """Sets the search_text of this ConnectIdentityMultiBureauAmlSupplierResult.

        The exact query text used in the search, allowing for audit and review of the search parameters and terms used.  # noqa: E501

        :param search_text: The search_text of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :type: str
        """

        self._search_text = search_text

    @property
    def legacy_unique_id(self):
        """Gets the legacy_unique_id of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501

        A unique identifier from a legacy system that may still be used to track or reference the subject within older datasets or parallel systems.  # noqa: E501

        :return: The legacy_unique_id of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :rtype: str
        """
        return self._legacy_unique_id

    @legacy_unique_id.setter
    def legacy_unique_id(self, legacy_unique_id):
        """Sets the legacy_unique_id of this ConnectIdentityMultiBureauAmlSupplierResult.

        A unique identifier from a legacy system that may still be used to track or reference the subject within older datasets or parallel systems.  # noqa: E501

        :param legacy_unique_id: The legacy_unique_id of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :type: str
        """

        self._legacy_unique_id = legacy_unique_id

    @property
    def validation_id(self):
        """Gets the validation_id of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501

        A unique identifier assigned to the validation process, facilitating tracking and cross-referencing of the validation attempts across multiple systems.  # noqa: E501

        :return: The validation_id of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :rtype: str
        """
        return self._validation_id

    @validation_id.setter
    def validation_id(self, validation_id):
        """Sets the validation_id of this ConnectIdentityMultiBureauAmlSupplierResult.

        A unique identifier assigned to the validation process, facilitating tracking and cross-referencing of the validation attempts across multiple systems.  # noqa: E501

        :param validation_id: The validation_id of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :type: str
        """

        self._validation_id = validation_id

    @property
    def has_alerts(self):
        """Gets the has_alerts of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501

        Indicates whether any alerts were triggered during the verification process. This is typically used to flag profiles that require further investigation or immediate attention.  # noqa: E501

        :return: The has_alerts of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :rtype: bool
        """
        return self._has_alerts

    @has_alerts.setter
    def has_alerts(self, has_alerts):
        """Sets the has_alerts of this ConnectIdentityMultiBureauAmlSupplierResult.

        Indicates whether any alerts were triggered during the verification process. This is typically used to flag profiles that require further investigation or immediate attention.  # noqa: E501

        :param has_alerts: The has_alerts of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :type: bool
        """

        self._has_alerts = has_alerts

    @property
    def success(self):
        """Gets the success of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501

        Reflects whether the AML search and verification process was successful, based on the predefined criteria and thresholds set within the system.  # noqa: E501

        :return: The success of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this ConnectIdentityMultiBureauAmlSupplierResult.

        Reflects whether the AML search and verification process was successful, based on the predefined criteria and thresholds set within the system.  # noqa: E501

        :param success: The success of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def credits_incurred(self):
        """Gets the credits_incurred of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501

        The number of credits or cost units consumed during the AML search process. This is relevant for systems where operations incur a variable cost based on usage or complexity.  # noqa: E501

        :return: The credits_incurred of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :rtype: int
        """
        return self._credits_incurred

    @credits_incurred.setter
    def credits_incurred(self, credits_incurred):
        """Sets the credits_incurred of this ConnectIdentityMultiBureauAmlSupplierResult.

        The number of credits or cost units consumed during the AML search process. This is relevant for systems where operations incur a variable cost based on usage or complexity.  # noqa: E501

        :param credits_incurred: The credits_incurred of this ConnectIdentityMultiBureauAmlSupplierResult.  # noqa: E501
        :type: int
        """

        self._credits_incurred = credits_incurred

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
        if issubclass(ConnectIdentityMultiBureauAmlSupplierResult, dict):
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
        if not isinstance(other, ConnectIdentityMultiBureauAmlSupplierResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

"""
    Creditsafe Connect

     Last Updated: 09th July 2024<br>  # Introduction   Creditsafe Connect is a REST API that provides access to the <a href=\"https://www.creditsafe.com/gb/en/more/about/our-data.html\" target=\"_blank\">Creditsafe Global Company Database.</a> This allows you to: <ul><li>Control your master data</li><li>Utilize up-to-date Business and Director information, enhancing your onboarding and qualification processes</li><li>Receive alerts when your customer's and supplier's Credit Report changes</li></ul><br>Check the status of Creditsafe Services <a href=\"https://status.creditsafe.com/\" target=\"_blank\">HERE</a>     ## Customer Feedback  Use the buttons below to let us know what you think of this documentation. Please leave comments in your feedback for the author to consider for future versions.<br><br><a href=\"https://app.customerthermometer.com/?template=log_feedback&hash=f49570f5&embed_data=dGVtcGVyYXR1cmVfaWQ9MSZ0aGVybW9tZXRlcl9pZD0xNjM2NTImbnBzX3JhdGluZz0=&e=&f=&l=&c=&c1=&c2=&c3=&c4=&c5=&c6=&c7=&c8=&c9=&c10=\" target=\"_blank\"> <img src=\"https://app.customerthermometer.com/sites/app/images/icon_sets/icon_set_3s/gold.png\" /></a><a href=\"https://app.customerthermometer.com/?template=log_feedback&hash=601a6fd1&embed_data=dGVtcGVyYXR1cmVfaWQ9MiZ0aGVybW9tZXRlcl9pZD0xNjM2NTImbnBzX3JhdGluZz0=&e=&f=&l=&c=&c1=&c2=&c3=&c4=&c5=&c6=&c7=&c8=&c9=&c10=\" target=\"_blank\"><img src=\"https://app.customerthermometer.com/sites/app/images/icon_sets/icon_set_3s/green.png\" /></a><a href=\"https://app.customerthermometer.com/?template=log_feedback&hash=f1f7701c&embed_data=dGVtcGVyYXR1cmVfaWQ9MyZ0aGVybW9tZXRlcl9pZD0xNjM2NTImbnBzX3JhdGluZz0=&e=&f=&l=&c=&c1=&c2=&c3=&c4=&c5=&c6=&c7=&c8=&c9=&c10=\" target=\"_blank\"><img src=\"https://app.customerthermometer.com/sites/app/images/icon_sets/icon_set_3s/amber.png\" /></a><a href=\"https://app.customerthermometer.com/?template=log_feedback&hash=73951e8b&embed_data=dGVtcGVyYXR1cmVfaWQ9NCZ0aGVybW9tZXRlcl9pZD0xNjM2NTImbnBzX3JhdGluZz0=&e=&f=&l=&c=&c1=&c2=&c3=&c4=&c5=&c6=&c7=&c8=&c9=&c10=\" target=\"_blank\"><img src=\"https://app.customerthermometer.com/sites/app/images/icon_sets/icon_set_3s/red.png\" /></a> <br><br> Selecting one of the buttons above will open a new tab to the feedback portal.   ## Quick Start  To start your Creditsafe Connect API integration you will need to have activated your account and set a password by following the instructions in your Welcome Email. If you have not received a Welcome Email please contact your Creditsafe Account Manager.</br></br>By default, you will have been setup on our Sandbox environment.</br></br>  Using a REST API client construct an `/authenticate` POST request and enter your username & password (case-sensitive) into the POST body. A successful response will return an  `authentication token`.</br></br>  Use the `authentication token` in an `Authorization` header on all other Creditsafe Connect calls as proof of your authenticity.   ## Environments  Production Environment baseurl: <code> https://connect.creditsafe.com/v1 </code> </br> Sandbox Test Environment baseurl:  <code>https://connect.sandbox.creditsafe.com/v1</code>    ## Resources   | Item | Description | |----------------|----------------| | <a href=\"https://connect-portal.creditsafe.com\" target=\"_blank\"> A Front End Demo Site</a> | Opens a friendly UI to test the Connect API | | <a href=\"https://creditsafe.github.io/connect-docs/cs_connectv1-15.html\" target=\"_blank\"> Open API Spec </a>  | This will allow you to view the documentation in the swagger portal - this will be discontinued | <a href=\"https://help.creditsafeuk.com/en/support/solutions\" target=\"_blank\"> Help Articles</a> | Opens the Help Hub with a list of common questions and answers | | <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000053487-connect-api-data-dictionaries\" target=\"_blank\"> Data Dictionaries </a> | The connect documentation shows the general use case, the data dictionaries include the additional specific data that is returned by individual countries | | <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000054765-connect-api-data-availability-per-country\" target=\"_blank\"> Data Availability per Country </a> | The Data Matrix is a document that outlines all the fields that are available in the company report for an online territory | | <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000054656-connect-api-feature-availability-per-country\" target=\"_blank\"> Creditsafe Online Country Feature Availability</a> | This matrix displays what features are available with the online Creditsafe Countries and the partner network | | <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000063360-connect-report-templates-glossary-availability\" target=\"_blank\"> Connect Report Templates </a> | The document identifies the templates available for specific parts of the Company Credit Report, avoiding the need to order the full report object in one API call. | | <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000081984-connect-api-server-response-codes\" target=\"_blank\"> Connect API Response Codes </a> | Opens up a basic table of response codes, provides a link to a more detailed response code list |   <br>    ## Versioning and Changes    ### Non-Breaking Changes   Non-breaking changes will generally include additive functions or bug fixes. It is crucial for the integration of the code to be done in such a way that it does not depend on the sequence in which items are returned. This ensures that updates can be applied seamlessly without affecting the existing functionality.    ### Breaking Changes   Breaking changes refer to any modifications to the API's functionality that could disrupt the current contract of the API. Such changes necessitate communication with stakeholders and will lead to a major version number update, indicating the significant nature of these changes.   # noqa: E501

    OpenAPI spec version: 1.10.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pycsapi.api_client import ApiClient


class KYCProfileKeyPartiesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def compliancedeletekyckeypartiesbyprofileid(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Delete a batch of key parties  # noqa: E501

        Delete a selection of key parties from a specific profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliancedeletekyckeypartiesbyprofileid(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of the profile (required)
        :param ProfileIdKeypartiesBody body:
        :return: DeleteKeyPartiesResponseByProfileId
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.compliancedeletekyckeypartiesbyprofileid_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.compliancedeletekyckeypartiesbyprofileid_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
            return data

    def compliancedeletekyckeypartiesbyprofileid_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Delete a batch of key parties  # noqa: E501

        Delete a selection of key parties from a specific profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliancedeletekyckeypartiesbyprofileid_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of the profile (required)
        :param ProfileIdKeypartiesBody body:
        :return: DeleteKeyPartiesResponseByProfileId
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method compliancedeletekyckeypartiesbyprofileid" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `compliancedeletekyckeypartiesbyprofileid`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = (
            self.api_client.select_header_content_type(  # noqa: E501
                ["application/json"]
            )
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/compliance/kyc-protect/profiles/{profileId}/keyparties",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="DeleteKeyPartiesResponseByProfileId",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def compliancedeletekyckeypartiessearches(self, profile_id, **kwargs):  # noqa: E501
        """Deletes A Batch Of Key Party Searches  # noqa: E501

        Delete a batch of key parties searches  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliancedeletekyckeypartiessearches(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param DeleteKeyPartySearchContractRequest body:
        :return: DeleteKeyPartySearchContractResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.compliancedeletekyckeypartiessearches_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.compliancedeletekyckeypartiessearches_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
            return data

    def compliancedeletekyckeypartiessearches_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Deletes A Batch Of Key Party Searches  # noqa: E501

        Delete a batch of key parties searches  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliancedeletekyckeypartiessearches_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param DeleteKeyPartySearchContractRequest body:
        :return: DeleteKeyPartySearchContractResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method compliancedeletekyckeypartiessearches" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `compliancedeletekyckeypartiessearches`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = (
            self.api_client.select_header_content_type(  # noqa: E501
                ["application/json"]
            )
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/compliance/kyc-protect/profiles/{profileId}/keyparties/searches",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="DeleteKeyPartySearchContractResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def compliancegetkyckeypartiesbyprofileid(self, profile_id, **kwargs):  # noqa: E501
        """Return All Key Party Records Linked To A Profile  # noqa: E501

        This endpoint will return all created Key Party folders linked to the profile id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliancegetkyckeypartiesbyprofileid(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of the profile (required)
        :param str entity_type: Entity type of the key party. Available values are individual, business.
        :param str key_party_types: Type of the key party. Available values are director, shareholder and ubo.
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :return: GetKeyPartiesResponseByProfileId
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.compliancegetkyckeypartiesbyprofileid_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.compliancegetkyckeypartiesbyprofileid_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
            return data

    def compliancegetkyckeypartiesbyprofileid_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Return All Key Party Records Linked To A Profile  # noqa: E501

        This endpoint will return all created Key Party folders linked to the profile id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliancegetkyckeypartiesbyprofileid_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of the profile (required)
        :param str entity_type: Entity type of the key party. Available values are individual, business.
        :param str key_party_types: Type of the key party. Available values are director, shareholder and ubo.
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :return: GetKeyPartiesResponseByProfileId
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "profile_id",
            "entity_type",
            "key_party_types",
            "page",
            "page_size",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method compliancegetkyckeypartiesbyprofileid" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `compliancegetkyckeypartiesbyprofileid`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501

        query_params = []
        if "entity_type" in params:
            query_params.append(("entityType", params["entity_type"]))  # noqa: E501
        if "key_party_types" in params:
            query_params.append(
                ("keyPartyTypes", params["key_party_types"])
            )  # noqa: E501
        if "page" in params:
            query_params.append(("page", params["page"]))  # noqa: E501
        if "page_size" in params:
            query_params.append(("pageSize", params["page_size"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/compliance/kyc-protect/profiles/{profileId}/keyparties",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="GetKeyPartiesResponseByProfileId",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def compliancegetkyckeypartiessearches(self, profile_id, **kwargs):  # noqa: E501
        """Return All Key Party Searches  # noqa: E501

        Get profile key party searches for the user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliancegetkyckeypartiessearches(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :param str type: type of searches. Available values: individual, business
        :param str key_party_types: keyparty types. Available values: director, shareHolder, ubo
        :param bool is_scheduled: schedule check.
        :return: GetKeyPartySearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.compliancegetkyckeypartiessearches_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.compliancegetkyckeypartiessearches_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
            return data

    def compliancegetkyckeypartiessearches_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Return All Key Party Searches  # noqa: E501

        Get profile key party searches for the user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliancegetkyckeypartiessearches_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :param str type: type of searches. Available values: individual, business
        :param str key_party_types: keyparty types. Available values: director, shareHolder, ubo
        :param bool is_scheduled: schedule check.
        :return: GetKeyPartySearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "profile_id",
            "page",
            "page_size",
            "type",
            "key_party_types",
            "is_scheduled",
        ]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method compliancegetkyckeypartiessearches" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `compliancegetkyckeypartiessearches`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501

        query_params = []
        if "page" in params:
            query_params.append(("page", params["page"]))  # noqa: E501
        if "page_size" in params:
            query_params.append(("pageSize", params["page_size"]))  # noqa: E501
        if "type" in params:
            query_params.append(("type", params["type"]))  # noqa: E501
        if "key_party_types" in params:
            query_params.append(
                ("keyPartyTypes", params["key_party_types"])
            )  # noqa: E501
        if "is_scheduled" in params:
            query_params.append(("isScheduled", params["is_scheduled"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/compliance/kyc-protect/profiles/{profileId}/keyparties/searches",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="GetKeyPartySearchResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def compliancepostkyckeypartiesbyprofileid(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Creates A Key Party Folder Linked To The Profile Id  # noqa: E501

        Uses the details provided by the user to create key parties. Returns the created key parties information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliancepostkyckeypartiesbyprofileid(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param PostKYCKeypartiesByProfileIdRequest body:
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.compliancepostkyckeypartiesbyprofileid_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.compliancepostkyckeypartiesbyprofileid_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
            return data

    def compliancepostkyckeypartiesbyprofileid_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Creates A Key Party Folder Linked To The Profile Id  # noqa: E501

        Uses the details provided by the user to create key parties. Returns the created key parties information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliancepostkyckeypartiesbyprofileid_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param PostKYCKeypartiesByProfileIdRequest body:
        :return: InlineResponse201
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method compliancepostkyckeypartiesbyprofileid" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `compliancepostkyckeypartiesbyprofileid`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = (
            self.api_client.select_header_content_type(  # noqa: E501
                ["application/json"]
            )
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/compliance/kyc-protect/profiles/{profileId}/keyparties",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse201",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def compliancepostkyckeypartiessearchesbulkbyprofileid(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Request Multiple Searches Linked To A Key Party Asynchronously  # noqa: E501

        Request multiple searches to be performed and linked to a key party asynchronously  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliancepostkyckeypartiessearchesbulkbyprofileid(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param SearchesBulkBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return (
                self.compliancepostkyckeypartiessearchesbulkbyprofileid_with_http_info(
                    profile_id, **kwargs
                )
            )  # noqa: E501
        else:
            (data) = (
                self.compliancepostkyckeypartiessearchesbulkbyprofileid_with_http_info(
                    profile_id, **kwargs
                )
            )  # noqa: E501
            return data

    def compliancepostkyckeypartiessearchesbulkbyprofileid_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Request Multiple Searches Linked To A Key Party Asynchronously  # noqa: E501

        Request multiple searches to be performed and linked to a key party asynchronously  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliancepostkyckeypartiessearchesbulkbyprofileid_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param SearchesBulkBody body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method compliancepostkyckeypartiessearchesbulkbyprofileid"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `compliancepostkyckeypartiessearchesbulkbyprofileid`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = (
            self.api_client.select_header_content_type(  # noqa: E501
                ["application/json"]
            )
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/compliance/kyc-protect/profiles/{profileId}/keyparties/searches/bulk",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def compliancepostkyckeypartiessearcheslinkbyprofileid(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Links Searches To Key Parties  # noqa: E501

        Add searches link to key parties for the current logged in user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliancepostkyckeypartiessearcheslinkbyprofileid(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param SearchesLinkBody body:
        :return: PostKYCKeypartiesSearchesLinkByProfileIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return (
                self.compliancepostkyckeypartiessearcheslinkbyprofileid_with_http_info(
                    profile_id, **kwargs
                )
            )  # noqa: E501
        else:
            (data) = (
                self.compliancepostkyckeypartiessearcheslinkbyprofileid_with_http_info(
                    profile_id, **kwargs
                )
            )  # noqa: E501
            return data

    def compliancepostkyckeypartiessearcheslinkbyprofileid_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Links Searches To Key Parties  # noqa: E501

        Add searches link to key parties for the current logged in user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliancepostkyckeypartiessearcheslinkbyprofileid_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param SearchesLinkBody body:
        :return: PostKYCKeypartiesSearchesLinkByProfileIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method compliancepostkyckeypartiessearcheslinkbyprofileid"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `compliancepostkyckeypartiessearcheslinkbyprofileid`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = (
            self.api_client.select_header_content_type(  # noqa: E501
                ["application/json"]
            )
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/compliance/kyc-protect/profiles/{profileId}/keyparties/searches/link",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="PostKYCKeypartiesSearchesLinkByProfileIdResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def complianceprotectdeletekycprofileskeypartiesbyprofileidandkeypartyid(
        self, profile_id, key_party_id, **kwargs
    ):  # noqa: E501
        """Deletes a Key PArty By Key Party Id  # noqa: E501

        Delete a key party by Id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.complianceprotectdeletekycprofileskeypartiesbyprofileidandkeypartyid(profile_id, key_party_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param str key_party_id: id of the keyParty (required)
        :return: DeleteKeyPartyByIdNoContent
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.complianceprotectdeletekycprofileskeypartiesbyprofileidandkeypartyid_with_http_info(
                profile_id, key_party_id, **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.complianceprotectdeletekycprofileskeypartiesbyprofileidandkeypartyid_with_http_info(
                    profile_id, key_party_id, **kwargs
                )
            )  # noqa: E501
            return data

    def complianceprotectdeletekycprofileskeypartiesbyprofileidandkeypartyid_with_http_info(
        self, profile_id, key_party_id, **kwargs
    ):  # noqa: E501
        """Deletes a Key PArty By Key Party Id  # noqa: E501

        Delete a key party by Id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.complianceprotectdeletekycprofileskeypartiesbyprofileidandkeypartyid_with_http_info(profile_id, key_party_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param str key_party_id: id of the keyParty (required)
        :return: DeleteKeyPartyByIdNoContent
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "key_party_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method complianceprotectdeletekycprofileskeypartiesbyprofileidandkeypartyid"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `complianceprotectdeletekycprofileskeypartiesbyprofileidandkeypartyid`"
            )  # noqa: E501
        # verify the required parameter 'key_party_id' is set
        if "key_party_id" not in params or params["key_party_id"] is None:
            raise ValueError(
                "Missing the required parameter `key_party_id` when calling `complianceprotectdeletekycprofileskeypartiesbyprofileidandkeypartyid`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501
        if "key_party_id" in params:
            path_params["keyPartyId"] = params["key_party_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/compliance/kyc-protect/profiles/{profileId}/keyparties/{keyPartyId}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="DeleteKeyPartyByIdNoContent",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def complianceprotectputkycprofileskeypartiesbyprofileidandkeypartyid(
        self, profile_id, key_party_id, **kwargs
    ):  # noqa: E501
        """Updates The Key Party By Profile Id and Key Party Id  # noqa: E501

        Updates a key party on a profile by Id. Returns the updated key party data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.complianceprotectputkycprofileskeypartiesbyprofileidandkeypartyid(profile_id, key_party_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param str key_party_id: id of the keyParty (required)
        :param UpdateKeyPartyById body: Modified key party
        :return: KeyPartyByIdReturn
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.complianceprotectputkycprofileskeypartiesbyprofileidandkeypartyid_with_http_info(
                profile_id, key_party_id, **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.complianceprotectputkycprofileskeypartiesbyprofileidandkeypartyid_with_http_info(
                    profile_id, key_party_id, **kwargs
                )
            )  # noqa: E501
            return data

    def complianceprotectputkycprofileskeypartiesbyprofileidandkeypartyid_with_http_info(
        self, profile_id, key_party_id, **kwargs
    ):  # noqa: E501
        """Updates The Key Party By Profile Id and Key Party Id  # noqa: E501

        Updates a key party on a profile by Id. Returns the updated key party data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.complianceprotectputkycprofileskeypartiesbyprofileidandkeypartyid_with_http_info(profile_id, key_party_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param str key_party_id: id of the keyParty (required)
        :param UpdateKeyPartyById body: Modified key party
        :return: KeyPartyByIdReturn
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "key_party_id", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method complianceprotectputkycprofileskeypartiesbyprofileidandkeypartyid"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `complianceprotectputkycprofileskeypartiesbyprofileidandkeypartyid`"
            )  # noqa: E501
        # verify the required parameter 'key_party_id' is set
        if "key_party_id" not in params or params["key_party_id"] is None:
            raise ValueError(
                "Missing the required parameter `key_party_id` when calling `complianceprotectputkycprofileskeypartiesbyprofileidandkeypartyid`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501
        if "key_party_id" in params:
            path_params["keyPartyId"] = params["key_party_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = (
            self.api_client.select_header_content_type(  # noqa: E501
                ["application/json"]
            )
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/compliance/kyc-protect/profiles/{profileId}/keyparties/{keyPartyId}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="KeyPartyByIdReturn",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def complianceputkyckeypartiesbyprofileid(self, profile_id, **kwargs):  # noqa: E501
        """Update A Batch Of Key Parties  # noqa: E501

        Updates a batch of key parties  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.complianceputkyckeypartiesbyprofileid(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param PutKYCKeypartiesByProfileIdRequest body:
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.complianceputkyckeypartiesbyprofileid_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.complianceputkyckeypartiesbyprofileid_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
            return data

    def complianceputkyckeypartiesbyprofileid_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Update A Batch Of Key Parties  # noqa: E501

        Updates a batch of key parties  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.complianceputkyckeypartiesbyprofileid_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param PutKYCKeypartiesByProfileIdRequest body:
        :return: InlineResponse20010
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method complianceputkyckeypartiesbyprofileid" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `complianceputkyckeypartiesbyprofileid`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = (
            self.api_client.select_header_content_type(  # noqa: E501
                ["application/json"]
            )
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/compliance/kyc-protect/profiles/{profileId}/keyparties",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse20010",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

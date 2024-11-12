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


class KYCProfileManagementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def compliance_protect_delete_kyc_profiles(self, **kwargs):  # noqa: E501
        """Delete All Profiles  # noqa: E501

        Deletes list of profiles. <br>This will delete all its dependencies/child items associated to that profileId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliance_protect_delete_kyc_profiles(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body:
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.compliance_protect_delete_kyc_profiles_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (data) = self.compliance_protect_delete_kyc_profiles_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def compliance_protect_delete_kyc_profiles_with_http_info(
        self, **kwargs
    ):  # noqa: E501
        """Delete All Profiles  # noqa: E501

        Deletes list of profiles. <br>This will delete all its dependencies/child items associated to that profileId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliance_protect_delete_kyc_profiles_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[str] body:
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method compliance_protect_delete_kyc_profiles" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

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
            "/compliance/kyc-protect/profiles",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="bool",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def compliance_protect_get_kyc_profiles(self, **kwargs):  # noqa: E501
        """Return Created Profiles  # noqa: E501

        Returns a list of profiles ordered by modified date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliance_protect_get_kyc_profiles(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :param str search_term: A search term to filter by. The search term will be matched against names, and internal ids containing the search term.
        :param int assignees: The ids of assigned users to filter by.
        :param date kyc_review_after: Filters results based on profiles with a kyc review date after this date.
        :param date kyc_review_before: Filters results based on profiles with a kyc review date after this date.
        :param list[str] risk_ratings: The risk ratings to filter by. Available values: notApplicable, veryLow, low, medium, high, veryHigh
        :param str sort_order: The order in which the items should be sorted. Available values: asc, desc
        :param str sort_by: The field by which the items should be sorted. Available values: modifiedAt, name
        :return: GetKYCProfiles
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.compliance_protect_get_kyc_profiles_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (data) = self.compliance_protect_get_kyc_profiles_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def compliance_protect_get_kyc_profiles_with_http_info(
        self, **kwargs
    ):  # noqa: E501
        """Return Created Profiles  # noqa: E501

        Returns a list of profiles ordered by modified date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliance_protect_get_kyc_profiles_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :param str search_term: A search term to filter by. The search term will be matched against names, and internal ids containing the search term.
        :param int assignees: The ids of assigned users to filter by.
        :param date kyc_review_after: Filters results based on profiles with a kyc review date after this date.
        :param date kyc_review_before: Filters results based on profiles with a kyc review date after this date.
        :param list[str] risk_ratings: The risk ratings to filter by. Available values: notApplicable, veryLow, low, medium, high, veryHigh
        :param str sort_order: The order in which the items should be sorted. Available values: asc, desc
        :param str sort_by: The field by which the items should be sorted. Available values: modifiedAt, name
        :return: GetKYCProfiles
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "page",
            "page_size",
            "search_term",
            "assignees",
            "kyc_review_after",
            "kyc_review_before",
            "risk_ratings",
            "sort_order",
            "sort_by",
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
                    " to method compliance_protect_get_kyc_profiles" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "page" in params:
            query_params.append(("page", params["page"]))  # noqa: E501
        if "page_size" in params:
            query_params.append(("pageSize", params["page_size"]))  # noqa: E501
        if "search_term" in params:
            query_params.append(("searchTerm", params["search_term"]))  # noqa: E501
        if "assignees" in params:
            query_params.append(("assignees", params["assignees"]))  # noqa: E501
        if "kyc_review_after" in params:
            query_params.append(
                ("kycReviewAfter", params["kyc_review_after"])
            )  # noqa: E501
        if "kyc_review_before" in params:
            query_params.append(
                ("kycReviewBefore", params["kyc_review_before"])
            )  # noqa: E501
        if "risk_ratings" in params:
            query_params.append(("riskRatings", params["risk_ratings"]))  # noqa: E501
            collection_formats["riskRatings"] = "multi"  # noqa: E501
        if "sort_order" in params:
            query_params.append(("sortOrder", params["sort_order"]))  # noqa: E501
        if "sort_by" in params:
            query_params.append(("sortBy", params["sort_by"]))  # noqa: E501

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
            "/compliance/kyc-protect/profiles",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="GetKYCProfiles",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def k_yc_protect_assigns_list_of_profiles_to_user(self, **kwargs):  # noqa: E501
        """Assigns A List Of Profiles To User  # noqa: E501

        Assigns list of profiles to a user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_protect_assigns_list_of_profiles_to_user(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MODEL4df4ca body:
        :return: list[KycProtectProfileAssignBulkResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.k_yc_protect_assigns_list_of_profiles_to_user_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (data) = self.k_yc_protect_assigns_list_of_profiles_to_user_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def k_yc_protect_assigns_list_of_profiles_to_user_with_http_info(
        self, **kwargs
    ):  # noqa: E501
        """Assigns A List Of Profiles To User  # noqa: E501

        Assigns list of profiles to a user.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_protect_assigns_list_of_profiles_to_user_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MODEL4df4ca body:
        :return: list[KycProtectProfileAssignBulkResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k_yc_protect_assigns_list_of_profiles_to_user" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

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
            "/compliance/kyc-protect/profiles/assign/bulk",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[KycProtectProfileAssignBulkResponse]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def k_yc_protect_create_profile(self, **kwargs):  # noqa: E501
        """Create Profile  # noqa: E501

        Uses the name and type provided by the user to create a profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_protect_create_profile(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param KycProtectPostProfilesRequest body:
        :return: KycProtectProfileCreatedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.k_yc_protect_create_profile_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (data) = self.k_yc_protect_create_profile_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def k_yc_protect_create_profile_with_http_info(self, **kwargs):  # noqa: E501
        """Create Profile  # noqa: E501

        Uses the name and type provided by the user to create a profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_protect_create_profile_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param KycProtectPostProfilesRequest body:
        :return: KycProtectProfileCreatedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k_yc_protect_create_profile" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

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
            "/compliance/kyc-protect/profiles",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="KycProtectProfileCreatedResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def protect_assign_profiles(self, profile_id, **kwargs):  # noqa: E501
        """Assign Profile To User  # noqa: E501

        Assign a profile to a user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_assign_profiles(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of the profile being assigned to a user (required)
        :param str user_id: User Id to assign the Profile to
        :return: PutKYCProfileAssign
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.protect_assign_profiles_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.protect_assign_profiles_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
            return data

    def protect_assign_profiles_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Assign Profile To User  # noqa: E501

        Assign a profile to a user  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_assign_profiles_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of the profile being assigned to a user (required)
        :param str user_id: User Id to assign the Profile to
        :return: PutKYCProfileAssign
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "user_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method protect_assign_profiles" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `protect_assign_profiles`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if "profile_id" in params:
            query_params.append(("profileId", params["profile_id"]))  # noqa: E501
        if "user_id" in params:
            query_params.append(("userId", params["user_id"]))  # noqa: E501

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
            "/compliance/kyc-protect/profiles/assign",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="PutKYCProfileAssign",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def protect_delete_kyc_profiles_by_id(self, profile_id, **kwargs):  # noqa: E501
        """Delete Profile By Profile Id  # noqa: E501

        Deletes a single profile by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_delete_kyc_profiles_by_id(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.protect_delete_kyc_profiles_by_id_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.protect_delete_kyc_profiles_by_id_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
            return data

    def protect_delete_kyc_profiles_by_id_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Delete Profile By Profile Id  # noqa: E501

        Deletes a single profile by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_delete_kyc_profiles_by_id_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method protect_delete_kyc_profiles_by_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `protect_delete_kyc_profiles_by_id`"
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
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/compliance/kyc-protect/profiles/{profileId}",
            "DELETE",
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

    def protect_get_kyc_profiles_by_profile_id(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Return Profile By Profile Id  # noqa: E501

        Returns a single profile by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_get_kyc_profiles_by_profile_id(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :return: GetKYCProfileByProfileId
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.protect_get_kyc_profiles_by_profile_id_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.protect_get_kyc_profiles_by_profile_id_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
            return data

    def protect_get_kyc_profiles_by_profile_id_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Return Profile By Profile Id  # noqa: E501

        Returns a single profile by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_get_kyc_profiles_by_profile_id_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :return: GetKYCProfileByProfileId
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method protect_get_kyc_profiles_by_profile_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `protect_get_kyc_profiles_by_profile_id`"
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
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/compliance/kyc-protect/profiles/{profileId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="GetKYCProfileByProfileId",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

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


class GBConsumersAndAMLApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def local_solutions_gb_identitysearch_history_get(self, **kwargs):  # noqa: E501
        """Gets a list of identitysearch history items  # noqa: E501

        Retrieves a paginated history list for the specified customer/user, filtered based on the include* parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.local_solutions_gb_identitysearch_history_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The 1-indexed page number to fetch
        :param int page_size: The page size number to fetch
        :param bool include_customer: If true, returns all results for this customer. Valid for senior users only.
        :param list[ConnectIdentityProduct] products: The array of products to include  **Below is a list of Definitions for the ENUM** * 0 - Consumer * 1 - Id * 2 - AML * 3 - Bank Match * 4 - AML with Bank Match
        :param datetime date_from: The earliest date to include
        :param datetime date_to: The latest date to include
        :param str keyword: Include this string
        :param str result: Return only items with this result
        :return: ConnectIdentityHistoryListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.local_solutions_gb_identitysearch_history_get_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (data) = self.local_solutions_gb_identitysearch_history_get_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def local_solutions_gb_identitysearch_history_get_with_http_info(
        self, **kwargs
    ):  # noqa: E501
        """Gets a list of identitysearch history items  # noqa: E501

        Retrieves a paginated history list for the specified customer/user, filtered based on the include* parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.local_solutions_gb_identitysearch_history_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: The 1-indexed page number to fetch
        :param int page_size: The page size number to fetch
        :param bool include_customer: If true, returns all results for this customer. Valid for senior users only.
        :param list[ConnectIdentityProduct] products: The array of products to include  **Below is a list of Definitions for the ENUM** * 0 - Consumer * 1 - Id * 2 - AML * 3 - Bank Match * 4 - AML with Bank Match
        :param datetime date_from: The earliest date to include
        :param datetime date_to: The latest date to include
        :param str keyword: Include this string
        :param str result: Return only items with this result
        :return: ConnectIdentityHistoryListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "page",
            "page_size",
            "include_customer",
            "products",
            "date_from",
            "date_to",
            "keyword",
            "result",
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
                    " to method local_solutions_gb_identitysearch_history_get" % key
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
        if "include_customer" in params:
            query_params.append(
                ("IncludeCustomer", params["include_customer"])
            )  # noqa: E501
        if "products" in params:
            query_params.append(("Products", params["products"]))  # noqa: E501
            collection_formats["Products"] = "multi"  # noqa: E501
        if "date_from" in params:
            query_params.append(("DateFrom", params["date_from"]))  # noqa: E501
        if "date_to" in params:
            query_params.append(("DateTo", params["date_to"]))  # noqa: E501
        if "keyword" in params:
            query_params.append(("Keyword", params["keyword"]))  # noqa: E501
        if "result" in params:
            query_params.append(("Result", params["result"]))  # noqa: E501

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
            "/localSolutions/GB/identitysearch/history",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectIdentityHistoryListResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def local_solutions_gb_identitysearch_searchreasons_get(
        self, **kwargs
    ):  # noqa: E501
        """Gets identitysearch Reasons.  # noqa: E501

        Returns an object describing which Reasons for Search are available and which are selected by a given customer. All reasons are always listed, with selected reasons specified as true.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.local_solutions_gb_identitysearch_searchreasons_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ConnectIdentityReasonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return (
                self.local_solutions_gb_identitysearch_searchreasons_get_with_http_info(
                    **kwargs
                )
            )  # noqa: E501
        else:
            (data) = (
                self.local_solutions_gb_identitysearch_searchreasons_get_with_http_info(
                    **kwargs
                )
            )  # noqa: E501
            return data

    def local_solutions_gb_identitysearch_searchreasons_get_with_http_info(
        self, **kwargs
    ):  # noqa: E501
        """Gets identitysearch Reasons.  # noqa: E501

        Returns an object describing which Reasons for Search are available and which are selected by a given customer. All reasons are always listed, with selected reasons specified as true.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.local_solutions_gb_identitysearch_searchreasons_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ConnectIdentityReasonResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method local_solutions_gb_identitysearch_searchreasons_get"
                    % key
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
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/localSolutions/GB/identitysearch/searchreasons",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectIdentityReasonResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def resolves_a_picklist_against_a_given_unique_id(self, **kwargs):  # noqa: E501
        """Resolves a picklist against a given UniqueId  # noqa: E501

        Resolves a picklist belonging to the specified UniqueID, which would have been generated during a prior search. Guids (and thus cached searches) expire after fifteen minutes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resolves_a_picklist_against_a_given_unique_id(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :param list[str] resolved:
        :return: ConnectIdentitySearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.resolves_a_picklist_against_a_given_unique_id_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (data) = self.resolves_a_picklist_against_a_given_unique_id_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def resolves_a_picklist_against_a_given_unique_id_with_http_info(
        self, **kwargs
    ):  # noqa: E501
        """Resolves a picklist against a given UniqueId  # noqa: E501

        Resolves a picklist belonging to the specified UniqueID, which would have been generated during a prior search. Guids (and thus cached searches) expire after fifteen minutes.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.resolves_a_picklist_against_a_given_unique_id_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body:
        :param list[str] resolved:
        :return: ConnectIdentitySearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body", "resolved"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method resolves_a_picklist_against_a_given_unique_id" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "resolved" in params:
            query_params.append(("resolved", params["resolved"]))  # noqa: E501
            collection_formats["resolved"] = "multi"  # noqa: E501

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
            "/localSolutions/GB/identitysearch",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectIdentitySearchResult",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def retrieves_a_prior_identity_search_result(
        self, unique_id, **kwargs
    ):  # noqa: E501
        """Retrieves a prior identitysearch result.  # noqa: E501

        Retrieves a prior search result. This will include the search input and any ID/AML searches, but as we cannot hold Consumer search results these are not included. Resubmission is necessary if an updated Consumer result is needed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieves_a_prior_identity_search_result(unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str unique_id: (required)
        :return: ConnectIdentitySearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.retrieves_a_prior_identity_search_result_with_http_info(
                unique_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.retrieves_a_prior_identity_search_result_with_http_info(
                unique_id, **kwargs
            )  # noqa: E501
            return data

    def retrieves_a_prior_identity_search_result_with_http_info(
        self, unique_id, **kwargs
    ):  # noqa: E501
        """Retrieves a prior identitysearch result.  # noqa: E501

        Retrieves a prior search result. This will include the search input and any ID/AML searches, but as we cannot hold Consumer search results these are not included. Resubmission is necessary if an updated Consumer result is needed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieves_a_prior_identity_search_result_with_http_info(unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str unique_id: (required)
        :return: ConnectIdentitySearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["unique_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieves_a_prior_identity_search_result" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'unique_id' is set
        if "unique_id" not in params or params["unique_id"] is None:
            raise ValueError(
                "Missing the required parameter `unique_id` when calling `retrieves_a_prior_identity_search_result`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "unique_id" in params:
            path_params["uniqueId"] = params["unique_id"]  # noqa: E501

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
            "/localSolutions/GB/identitysearch/history/{uniqueId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectIdentitySearchResult",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def retrieves_a_prior_identity_searchs_input(
        self, unique_id, **kwargs
    ):  # noqa: E501
        """Retrieves a prior identitysearch's input  # noqa: E501

        This will return the input criteria used in a search for a specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieves_a_prior_identity_searchs_input(unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str unique_id: (required)
        :return: ConnectIdentitySearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.retrieves_a_prior_identity_searchs_input_with_http_info(
                unique_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.retrieves_a_prior_identity_searchs_input_with_http_info(
                unique_id, **kwargs
            )  # noqa: E501
            return data

    def retrieves_a_prior_identity_searchs_input_with_http_info(
        self, unique_id, **kwargs
    ):  # noqa: E501
        """Retrieves a prior identitysearch's input  # noqa: E501

        This will return the input criteria used in a search for a specified id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieves_a_prior_identity_searchs_input_with_http_info(unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str unique_id: (required)
        :return: ConnectIdentitySearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["unique_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieves_a_prior_identity_searchs_input" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'unique_id' is set
        if "unique_id" not in params or params["unique_id"] is None:
            raise ValueError(
                "Missing the required parameter `unique_id` when calling `retrieves_a_prior_identity_searchs_input`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "unique_id" in params:
            path_params["uniqueId"] = params["unique_id"]  # noqa: E501

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
            "/localSolutions/GB/identitysearch/history/{uniqueId}/input",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectIdentitySearchResult",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def revalidate_a_given_identitysearch_with_additional_documents(
        self, body, unique_id, **kwargs
    ):  # noqa: E501
        """Revalidate a given identitysearch with additional documents  # noqa: E501

        Revalidate's a given identitysearch with additional documents.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revalidate_a_given_identitysearch_with_additional_documents(body, unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectIdentityRevalidateRequest body: (required)
        :param str unique_id: The ID of the record to update (required)
        :return: ConnectIdentitySearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.revalidate_a_given_identitysearch_with_additional_documents_with_http_info(
                body, unique_id, **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.revalidate_a_given_identitysearch_with_additional_documents_with_http_info(
                    body, unique_id, **kwargs
                )
            )  # noqa: E501
            return data

    def revalidate_a_given_identitysearch_with_additional_documents_with_http_info(
        self, body, unique_id, **kwargs
    ):  # noqa: E501
        """Revalidate a given identitysearch with additional documents  # noqa: E501

        Revalidate's a given identitysearch with additional documents.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.revalidate_a_given_identitysearch_with_additional_documents_with_http_info(body, unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectIdentityRevalidateRequest body: (required)
        :param str unique_id: The ID of the record to update (required)
        :return: ConnectIdentitySearchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body", "unique_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method revalidate_a_given_identitysearch_with_additional_documents"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `revalidate_a_given_identitysearch_with_additional_documents`"
            )  # noqa: E501
        # verify the required parameter 'unique_id' is set
        if "unique_id" not in params or params["unique_id"] is None:
            raise ValueError(
                "Missing the required parameter `unique_id` when calling `revalidate_a_given_identitysearch_with_additional_documents`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "unique_id" in params:
            path_params["uniqueId"] = params["unique_id"]  # noqa: E501

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
            "/localSolutions/GB/identitysearch/revalidation/{uniqueId}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectIdentitySearchResult",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def sets_the_reference_for_an_existing_history_item(
        self, body, unique_id, **kwargs
    ):  # noqa: E501
        """Sets the reference for an existing history item  # noqa: E501

        Allows you to set a reference for an existing history item. This is useful for storing a reference to the record in your own system.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sets_the_reference_for_an_existing_history_item(body, unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: (required)
        :param str unique_id: The ID of the record to update (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.sets_the_reference_for_an_existing_history_item_with_http_info(
                body, unique_id, **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.sets_the_reference_for_an_existing_history_item_with_http_info(
                    body, unique_id, **kwargs
                )
            )  # noqa: E501
            return data

    def sets_the_reference_for_an_existing_history_item_with_http_info(
        self, body, unique_id, **kwargs
    ):  # noqa: E501
        """Sets the reference for an existing history item  # noqa: E501

        Allows you to set a reference for an existing history item. This is useful for storing a reference to the record in your own system.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.sets_the_reference_for_an_existing_history_item_with_http_info(body, unique_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str body: (required)
        :param str unique_id: The ID of the record to update (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body", "unique_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sets_the_reference_for_an_existing_history_item" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `sets_the_reference_for_an_existing_history_item`"
            )  # noqa: E501
        # verify the required parameter 'unique_id' is set
        if "unique_id" not in params or params["unique_id"] is None:
            raise ValueError(
                "Missing the required parameter `unique_id` when calling `sets_the_reference_for_an_existing_history_item`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "unique_id" in params:
            path_params["uniqueId"] = params["unique_id"]  # noqa: E501

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
            "/localSolutions/GB/identitysearch/history/{uniqueId}/reference",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="str",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def submits_agb_consumer_or_aml_search(self, **kwargs):  # noqa: E501
        """Submits a GB Consumer or AML Search  # noqa: E501

        Submits a GB Consumer or AML depending on the Product provided. Validates criteria for each individual search before submitting, and may return a list of error strings instead.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submits_agb_consumer_or_aml_search(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: Select the relevant tab for the request body for one of the products `AML`, `AMLMultiBureau` or `Consumer`. <br> <br> NOTE:' If a previous address is used in addition to current the `postCode` becomes required.
        :return: InlineResponse2008
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.submits_agb_consumer_or_aml_search_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (data) = self.submits_agb_consumer_or_aml_search_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def submits_agb_consumer_or_aml_search_with_http_info(self, **kwargs):  # noqa: E501
        """Submits a GB Consumer or AML Search  # noqa: E501

        Submits a GB Consumer or AML depending on the Product provided. Validates criteria for each individual search before submitting, and may return a list of error strings instead.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submits_agb_consumer_or_aml_search_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object body: Select the relevant tab for the request body for one of the products `AML`, `AMLMultiBureau` or `Consumer`. <br> <br> NOTE:' If a previous address is used in addition to current the `postCode` becomes required.
        :return: InlineResponse2008
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
                    " to method submits_agb_consumer_or_aml_search" % key
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
            "/localSolutions/GB/identitysearch",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse2008",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

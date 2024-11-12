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


class KYCAMLScreeningIndividualsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def compliance_kyc_protect_create_individuals_search(self, **kwargs):  # noqa: E501
        """Performs An AML Search For An Individual And Saves The Results To The Database  # noqa: E501

        A request requires a name, or first name and last name, at least one valid dataset and a threshold.<br><br> Length of name or combination of first name, middle name and last name must not exceed 200 characters. If user is providing first name, middle name and last name combination, the max characters limit includes the formatted name in this format {lastName} {firstName} {middleName}.<br><br> User will be deducted 1 credit for each search.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliance_kyc_protect_create_individuals_search(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param KYCPostIndividualSearchContract body:
        :return: KycProtectPostPostIndividualSearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.compliance_kyc_protect_create_individuals_search_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.compliance_kyc_protect_create_individuals_search_with_http_info(
                    **kwargs
                )
            )  # noqa: E501
            return data

    def compliance_kyc_protect_create_individuals_search_with_http_info(
        self, **kwargs
    ):  # noqa: E501
        """Performs An AML Search For An Individual And Saves The Results To The Database  # noqa: E501

        A request requires a name, or first name and last name, at least one valid dataset and a threshold.<br><br> Length of name or combination of first name, middle name and last name must not exceed 200 characters. If user is providing first name, middle name and last name combination, the max characters limit includes the formatted name in this format {lastName} {firstName} {middleName}.<br><br> User will be deducted 1 credit for each search.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliance_kyc_protect_create_individuals_search_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param KYCPostIndividualSearchContract body:
        :return: KycProtectPostPostIndividualSearchResponse
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
                    " to method compliance_kyc_protect_create_individuals_search" % key
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
            "/compliance/kyc-protect/searches/individuals",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="KycProtectPostPostIndividualSearchResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def compliance_kyc_protect_get_individuals_search(self, **kwargs):  # noqa: E501
        """Returns Individual AML Searches  # noqa: E501

        Returns a list of individual AML searches ordered by modified date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliance_kyc_protect_get_individuals_search(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Starting page number.
        :param int page_size: Number of items to return per Page.
        :param bool is_scheduled:
        :return: KycProtectIndividualSearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.compliance_kyc_protect_get_individuals_search_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (data) = self.compliance_kyc_protect_get_individuals_search_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def compliance_kyc_protect_get_individuals_search_with_http_info(
        self, **kwargs
    ):  # noqa: E501
        """Returns Individual AML Searches  # noqa: E501

        Returns a list of individual AML searches ordered by modified date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliance_kyc_protect_get_individuals_search_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Starting page number.
        :param int page_size: Number of items to return per Page.
        :param bool is_scheduled:
        :return: KycProtectIndividualSearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["page", "page_size", "is_scheduled"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method compliance_kyc_protect_get_individuals_search" % key
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
            "/compliance/kyc-protect/searches/individuals",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="KycProtectIndividualSearchResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def compliance_kyc_protect_update_individuals_search(self, **kwargs):  # noqa: E501
        """Update Individual AML Searches  # noqa: E501

        Updates a batch of individual AML searches.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliance_kyc_protect_update_individuals_search(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PutKYCIndividualSearchRequest body:
        :return: PutKYCSearchIndividualResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.compliance_kyc_protect_update_individuals_search_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.compliance_kyc_protect_update_individuals_search_with_http_info(
                    **kwargs
                )
            )  # noqa: E501
            return data

    def compliance_kyc_protect_update_individuals_search_with_http_info(
        self, **kwargs
    ):  # noqa: E501
        """Update Individual AML Searches  # noqa: E501

        Updates a batch of individual AML searches.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliance_kyc_protect_update_individuals_search_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PutKYCIndividualSearchRequest body:
        :return: PutKYCSearchIndividualResponse
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
                    " to method compliance_kyc_protect_update_individuals_search" % key
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
            "/compliance/kyc-protect/searches/individuals",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="PutKYCSearchIndividualResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def gets_an_individual_search_for_the_current_logged_in_users_customer_based_on_search_id(
        self, search_id, **kwargs
    ):  # noqa: E501
        """Return Individual AML Search By Search Id  # noqa: E501

        Returns a single AML Search based on searchId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gets_an_individual_search_for_the_current_logged_in_users_customer_based_on_search_id(search_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: search id to fetch (required)
        :return: KYCGetSearchIndividualBySearchIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.gets_an_individual_search_for_the_current_logged_in_users_customer_based_on_search_id_with_http_info(
                search_id, **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.gets_an_individual_search_for_the_current_logged_in_users_customer_based_on_search_id_with_http_info(
                    search_id, **kwargs
                )
            )  # noqa: E501
            return data

    def gets_an_individual_search_for_the_current_logged_in_users_customer_based_on_search_id_with_http_info(
        self, search_id, **kwargs
    ):  # noqa: E501
        """Return Individual AML Search By Search Id  # noqa: E501

        Returns a single AML Search based on searchId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gets_an_individual_search_for_the_current_logged_in_users_customer_based_on_search_id_with_http_info(search_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: search id to fetch (required)
        :return: KYCGetSearchIndividualBySearchIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["search_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method gets_an_individual_search_for_the_current_logged_in_users_customer_based_on_search_id"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'search_id' is set
        if "search_id" not in params or params["search_id"] is None:
            raise ValueError(
                "Missing the required parameter `search_id` when calling `gets_an_individual_search_for_the_current_logged_in_users_customer_based_on_search_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "search_id" in params:
            path_params["searchId"] = params["search_id"]  # noqa: E501

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
            "/compliance/kyc-protect/searches/individuals/{searchId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="KYCGetSearchIndividualBySearchIdResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def gets_the_individual_search_hits(self, search_id, **kwargs):  # noqa: E501
        """Returns Individual AML Search Hits  # noqa: E501

        Returns the individual AML search hits from the AML search results.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gets_the_individual_search_hits(search_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: The search identifier. (required)
        :param str hit_decisions: The hit decisions. It can be the collection of undecided, trueMatch, falsePositive, discarded
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :return: GetIndividualSearchIdHitsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.gets_the_individual_search_hits_with_http_info(
                search_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.gets_the_individual_search_hits_with_http_info(
                search_id, **kwargs
            )  # noqa: E501
            return data

    def gets_the_individual_search_hits_with_http_info(
        self, search_id, **kwargs
    ):  # noqa: E501
        """Returns Individual AML Search Hits  # noqa: E501

        Returns the individual AML search hits from the AML search results.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.gets_the_individual_search_hits_with_http_info(search_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: The search identifier. (required)
        :param str hit_decisions: The hit decisions. It can be the collection of undecided, trueMatch, falsePositive, discarded
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :return: GetIndividualSearchIdHitsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["search_id", "hit_decisions", "page", "page_size"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method gets_the_individual_search_hits" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'search_id' is set
        if "search_id" not in params or params["search_id"] is None:
            raise ValueError(
                "Missing the required parameter `search_id` when calling `gets_the_individual_search_hits`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "search_id" in params:
            path_params["searchId"] = params["search_id"]  # noqa: E501

        query_params = []
        if "hit_decisions" in params:
            query_params.append(("hitDecisions", params["hit_decisions"]))  # noqa: E501
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
            "/compliance/kyc-protect/searches/individuals/{searchId}/hits",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="GetIndividualSearchIdHitsResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def returns_full_profile_information_of_a_individual_hit_by_hit_id(
        self, search_id, hit_id, **kwargs
    ):  # noqa: E501
        """Return Full AML Search Hit Information By SearchId And HitId  # noqa: E501

        This endpoint will return the full hit information by search Id and hitId. <br> Once this information is requested the information returned is stored to the database as a snap shot of that point in time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.returns_full_profile_information_of_a_individual_hit_by_hit_id(search_id, hit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: Id of the search (required)
        :param str hit_id: Id of the hit (required)
        :return: IndividualSearchResultHitResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.returns_full_profile_information_of_a_individual_hit_by_hit_id_with_http_info(
                search_id, hit_id, **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.returns_full_profile_information_of_a_individual_hit_by_hit_id_with_http_info(
                    search_id, hit_id, **kwargs
                )
            )  # noqa: E501
            return data

    def returns_full_profile_information_of_a_individual_hit_by_hit_id_with_http_info(
        self, search_id, hit_id, **kwargs
    ):  # noqa: E501
        """Return Full AML Search Hit Information By SearchId And HitId  # noqa: E501

        This endpoint will return the full hit information by search Id and hitId. <br> Once this information is requested the information returned is stored to the database as a snap shot of that point in time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.returns_full_profile_information_of_a_individual_hit_by_hit_id_with_http_info(search_id, hit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: Id of the search (required)
        :param str hit_id: Id of the hit (required)
        :return: IndividualSearchResultHitResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["search_id", "hit_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method returns_full_profile_information_of_a_individual_hit_by_hit_id"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'search_id' is set
        if "search_id" not in params or params["search_id"] is None:
            raise ValueError(
                "Missing the required parameter `search_id` when calling `returns_full_profile_information_of_a_individual_hit_by_hit_id`"
            )  # noqa: E501
        # verify the required parameter 'hit_id' is set
        if "hit_id" not in params or params["hit_id"] is None:
            raise ValueError(
                "Missing the required parameter `hit_id` when calling `returns_full_profile_information_of_a_individual_hit_by_hit_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "search_id" in params:
            path_params["searchId"] = params["search_id"]  # noqa: E501
        if "hit_id" in params:
            path_params["hitId"] = params["hit_id"]  # noqa: E501

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
            "/compliance/kyc-protect/searches/individuals/{searchId}/hits/{hitId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="IndividualSearchResultHitResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update_single_individual_hit(self, search_id, hit_id, **kwargs):  # noqa: E501
        """Update A Single Individual Hit  # noqa: E501

        This endpoint will update a single individual AML search hit by searchId and hitId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_single_individual_hit(search_id, hit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: Id of the search (required)
        :param str hit_id: Id of the hit (required)
        :param IndividualsSearchResultUpdateHits body:
        :return: PutIndividualSearchIdHitsByHitIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.update_single_individual_hit_with_http_info(
                search_id, hit_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.update_single_individual_hit_with_http_info(
                search_id, hit_id, **kwargs
            )  # noqa: E501
            return data

    def update_single_individual_hit_with_http_info(
        self, search_id, hit_id, **kwargs
    ):  # noqa: E501
        """Update A Single Individual Hit  # noqa: E501

        This endpoint will update a single individual AML search hit by searchId and hitId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_single_individual_hit_with_http_info(search_id, hit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: Id of the search (required)
        :param str hit_id: Id of the hit (required)
        :param IndividualsSearchResultUpdateHits body:
        :return: PutIndividualSearchIdHitsByHitIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["search_id", "hit_id", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_single_individual_hit" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'search_id' is set
        if "search_id" not in params or params["search_id"] is None:
            raise ValueError(
                "Missing the required parameter `search_id` when calling `update_single_individual_hit`"
            )  # noqa: E501
        # verify the required parameter 'hit_id' is set
        if "hit_id" not in params or params["hit_id"] is None:
            raise ValueError(
                "Missing the required parameter `hit_id` when calling `update_single_individual_hit`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "search_id" in params:
            path_params["searchId"] = params["search_id"]  # noqa: E501
        if "hit_id" in params:
            path_params["hitId"] = params["hit_id"]  # noqa: E501

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
            "/compliance/kyc-protect/searches/individuals/{searchId}/hits/{hitId}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="PutIndividualSearchIdHitsByHitIdResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def updates_a_batch_of_individual_hits(self, search_id, **kwargs):  # noqa: E501
        """Updates A Batch Of individual AML search Hits  # noqa: E501

        Update a batch of Individual AML Search Hits.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.updates_a_batch_of_individual_hits(search_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: Id of the search (required)
        :param MODEL20274f body:
        :return: PutIndividualSearchIdHitsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.updates_a_batch_of_individual_hits_with_http_info(
                search_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.updates_a_batch_of_individual_hits_with_http_info(
                search_id, **kwargs
            )  # noqa: E501
            return data

    def updates_a_batch_of_individual_hits_with_http_info(
        self, search_id, **kwargs
    ):  # noqa: E501
        """Updates A Batch Of individual AML search Hits  # noqa: E501

        Update a batch of Individual AML Search Hits.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.updates_a_batch_of_individual_hits_with_http_info(search_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: Id of the search (required)
        :param MODEL20274f body:
        :return: PutIndividualSearchIdHitsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["search_id", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method updates_a_batch_of_individual_hits" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'search_id' is set
        if "search_id" not in params or params["search_id"] is None:
            raise ValueError(
                "Missing the required parameter `search_id` when calling `updates_a_batch_of_individual_hits`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "search_id" in params:
            path_params["searchId"] = params["search_id"]  # noqa: E501

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
            "/compliance/kyc-protect/searches/individuals/{searchId}/hits",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="PutIndividualSearchIdHitsResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def updates_an_individual_search(self, search_id, **kwargs):  # noqa: E501
        """Updates An Individual AML Search By SearchID  # noqa: E501

        Updates an Individual AML Search by Search Id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.updates_an_individual_search(search_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: search id to update (required)
        :param PutKYCIndividualSearchBySearchIdRequest body:
        :return: KYCPutSearchIndividualBySearchIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.updates_an_individual_search_with_http_info(
                search_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.updates_an_individual_search_with_http_info(
                search_id, **kwargs
            )  # noqa: E501
            return data

    def updates_an_individual_search_with_http_info(
        self, search_id, **kwargs
    ):  # noqa: E501
        """Updates An Individual AML Search By SearchID  # noqa: E501

        Updates an Individual AML Search by Search Id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.updates_an_individual_search_with_http_info(search_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: search id to update (required)
        :param PutKYCIndividualSearchBySearchIdRequest body:
        :return: KYCPutSearchIndividualBySearchIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["search_id", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method updates_an_individual_search" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'search_id' is set
        if "search_id" not in params or params["search_id"] is None:
            raise ValueError(
                "Missing the required parameter `search_id` when calling `updates_an_individual_search`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "search_id" in params:
            path_params["searchId"] = params["search_id"]  # noqa: E501

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
            "/compliance/kyc-protect/searches/individuals/{searchId}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="KYCPutSearchIndividualBySearchIdResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

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


class BankVerificationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def bank_verification_get_history_by_id(self, id, **kwargs):  # noqa: E501
        """Returns Request History By ID  # noqa: E501

        This endpoint will return details of a past request by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bank_verification_get_history_by_id(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: request id to fetch details (required)
        :return: GBLocalSolutionGetHistoryRequestResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.bank_verification_get_history_by_id_with_http_info(
                id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.bank_verification_get_history_by_id_with_http_info(
                id, **kwargs
            )  # noqa: E501
            return data

    def bank_verification_get_history_by_id_with_http_info(
        self, id, **kwargs
    ):  # noqa: E501
        """Returns Request History By ID  # noqa: E501

        This endpoint will return details of a past request by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bank_verification_get_history_by_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: request id to fetch details (required)
        :return: GBLocalSolutionGetHistoryRequestResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bank_verification_get_history_by_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `bank_verification_get_history_by_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

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
            "/localSolutions/GB/bankVerification/history/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="GBLocalSolutionGetHistoryRequestResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def bank_verification_get_history_list(
        self, search_by_customer, **kwargs
    ):  # noqa: E501
        """Requests Search History  # noqa: E501

        Bank Verification History list Request<br><br> Note:- All property fields need to be submitted with the request, if information for a specific property is not needed, it is required to pass an empty string.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bank_verification_get_history_list(search_by_customer, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool search_by_customer: A value of false will only search records for your account. If your account manager has configured your account to be able to view other users records within your company, a value of true will search all records made by all accounts within your company. (required)
        :param str customer_name: Name of the customer returned by the supplier.
        :param str match_result: Whether a match or not a match returned by the supplier. Values are 'Full', 'Close' and 'No Match'.
        :param str date_from: Start date for filtering the results list by.
        :param str date_to: End date for filtering the results list by.
        :param str account_type: Type of account queried with the the supplier. Values are 'Business' and 'Personal'.
        :param str customer_reference: Your Customer reference.
        :return: list[GBLocalSolutionGetHistoryListResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.bank_verification_get_history_list_with_http_info(
                search_by_customer, **kwargs
            )  # noqa: E501
        else:
            (data) = self.bank_verification_get_history_list_with_http_info(
                search_by_customer, **kwargs
            )  # noqa: E501
            return data

    def bank_verification_get_history_list_with_http_info(
        self, search_by_customer, **kwargs
    ):  # noqa: E501
        """Requests Search History  # noqa: E501

        Bank Verification History list Request<br><br> Note:- All property fields need to be submitted with the request, if information for a specific property is not needed, it is required to pass an empty string.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bank_verification_get_history_list_with_http_info(search_by_customer, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool search_by_customer: A value of false will only search records for your account. If your account manager has configured your account to be able to view other users records within your company, a value of true will search all records made by all accounts within your company. (required)
        :param str customer_name: Name of the customer returned by the supplier.
        :param str match_result: Whether a match or not a match returned by the supplier. Values are 'Full', 'Close' and 'No Match'.
        :param str date_from: Start date for filtering the results list by.
        :param str date_to: End date for filtering the results list by.
        :param str account_type: Type of account queried with the the supplier. Values are 'Business' and 'Personal'.
        :param str customer_reference: Your Customer reference.
        :return: list[GBLocalSolutionGetHistoryListResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "search_by_customer",
            "customer_name",
            "match_result",
            "date_from",
            "date_to",
            "account_type",
            "customer_reference",
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
                    " to method bank_verification_get_history_list" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'search_by_customer' is set
        if "search_by_customer" not in params or params["search_by_customer"] is None:
            raise ValueError(
                "Missing the required parameter `search_by_customer` when calling `bank_verification_get_history_list`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if "search_by_customer" in params:
            query_params.append(
                ("searchByCustomer", params["search_by_customer"])
            )  # noqa: E501
        if "customer_name" in params:
            query_params.append(("customerName", params["customer_name"]))  # noqa: E501
        if "match_result" in params:
            query_params.append(("matchResult", params["match_result"]))  # noqa: E501
        if "date_from" in params:
            query_params.append(("dateFrom", params["date_from"]))  # noqa: E501
        if "date_to" in params:
            query_params.append(("dateTo", params["date_to"]))  # noqa: E501
        if "account_type" in params:
            query_params.append(("accountType", params["account_type"]))  # noqa: E501
        if "customer_reference" in params:
            query_params.append(
                ("customerReference", params["customer_reference"])
            )  # noqa: E501

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
            "/localSolutions/GB/bankVerification/history",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[GBLocalSolutionGetHistoryListResponse]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def bank_verification_search(self, **kwargs):  # noqa: E501
        """Single Request  # noqa: E501

        This endpoint will perform a search with the supplied data against a bank or building society.<br><br> NOTE:- This endpoint will charge when a successful request is made to a bank or building society. This endpoint will charge when a result is returned. This includes charging if the no match is found.<br><br> All property fields need to be submitted with the request, if information for a specific property is not needed, it is required to pass an empty string.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bank_verification_search(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GBLocalSolutionBankVerificationSearchRequest body:
        :return: GBLocalSolutionBankVerificationSearchResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.bank_verification_search_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.bank_verification_search_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def bank_verification_search_with_http_info(self, **kwargs):  # noqa: E501
        """Single Request  # noqa: E501

        This endpoint will perform a search with the supplied data against a bank or building society.<br><br> NOTE:- This endpoint will charge when a successful request is made to a bank or building society. This endpoint will charge when a result is returned. This includes charging if the no match is found.<br><br> All property fields need to be submitted with the request, if information for a specific property is not needed, it is required to pass an empty string.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bank_verification_search_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GBLocalSolutionBankVerificationSearchRequest body:
        :return: GBLocalSolutionBankVerificationSearchResponse
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
                    " to method bank_verification_search" % key
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
            "/localSolutions/GB/bankVerification/search",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="GBLocalSolutionBankVerificationSearchResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def bank_verification_update_history(self, id, **kwargs):  # noqa: E501
        """Update CustomerReference by HistoryId  # noqa: E501

        This endpoint will update the stored customerReference field of a past request with the provided ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bank_verification_update_history(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The id of the history record (required)
        :param GBLocalSolutionCPHistoryRequestByIdRequest body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.bank_verification_update_history_with_http_info(
                id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.bank_verification_update_history_with_http_info(
                id, **kwargs
            )  # noqa: E501
            return data

    def bank_verification_update_history_with_http_info(
        self, id, **kwargs
    ):  # noqa: E501
        """Update CustomerReference by HistoryId  # noqa: E501

        This endpoint will update the stored customerReference field of a past request with the provided ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bank_verification_update_history_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The id of the history record (required)
        :param GBLocalSolutionCPHistoryRequestByIdRequest body:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["id", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bank_verification_update_history" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `bank_verification_update_history`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

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
            "/localSolutions/GB/bankVerification/history/{id}/reference",
            "PATCH",
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

    def bank_verification_validate(self, id, **kwargs):  # noqa: E501
        """Validate Bank Verification Request  # noqa: E501

        This endpoint will return whether the sort code and bank account number match the sort code and bank account number that was provided for the given single request.<br><br> Note:- A valid request requires all fields to exist in the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bank_verification_validate(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: request id to fetch details (required)
        :param ValidateIdBody body:
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.bank_verification_validate_with_http_info(
                id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.bank_verification_validate_with_http_info(
                id, **kwargs
            )  # noqa: E501
            return data

    def bank_verification_validate_with_http_info(self, id, **kwargs):  # noqa: E501
        """Validate Bank Verification Request  # noqa: E501

        This endpoint will return whether the sort code and bank account number match the sort code and bank account number that was provided for the given single request.<br><br> Note:- A valid request requires all fields to exist in the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bank_verification_validate_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: request id to fetch details (required)
        :param ValidateIdBody body:
        :return: InlineResponse2007
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["id", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bank_verification_validate" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `bank_verification_validate`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

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
            "/localSolutions/GB/bankVerification/validate/{id}",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse2007",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

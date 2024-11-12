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


class KYCAMLScreeningBusinessesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_kyc_search_business_by_search_id(self, search_id, **kwargs):  # noqa: E501
        """Return Business AML Search By Search Id  # noqa: E501

        Returns a single AML search based on Search id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_kyc_search_business_by_search_id(search_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: (required)
        :return: KYCGetSearchBusinessesBySearchIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_kyc_search_business_by_search_id_with_http_info(
                search_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_kyc_search_business_by_search_id_with_http_info(
                search_id, **kwargs
            )  # noqa: E501
            return data

    def get_kyc_search_business_by_search_id_with_http_info(
        self, search_id, **kwargs
    ):  # noqa: E501
        """Return Business AML Search By Search Id  # noqa: E501

        Returns a single AML search based on Search id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_kyc_search_business_by_search_id_with_http_info(search_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: (required)
        :return: KYCGetSearchBusinessesBySearchIdResponse
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
                    " to method get_kyc_search_business_by_search_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'search_id' is set
        if "search_id" not in params or params["search_id"] is None:
            raise ValueError(
                "Missing the required parameter `search_id` when calling `get_kyc_search_business_by_search_id`"
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
            "/compliance/kyc-protect/searches/businesses/{searchId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="KYCGetSearchBusinessesBySearchIdResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_kyc_search_business_hits_by_search_id(
        self, search_id, **kwargs
    ):  # noqa: E501
        """Return Business AML Search Hits  # noqa: E501

        Returns the business AML search hits from the AML search results.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_kyc_search_business_hits_by_search_id(search_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: (required)
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :param str hit_decisions: The hit decisions. <br> Available Values - [undecided, truematch, falsepositive, discarded]
        :return: KYCGetSearchBusinessesBySearchIdHitsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_kyc_search_business_hits_by_search_id_with_http_info(
                search_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_kyc_search_business_hits_by_search_id_with_http_info(
                search_id, **kwargs
            )  # noqa: E501
            return data

    def get_kyc_search_business_hits_by_search_id_with_http_info(
        self, search_id, **kwargs
    ):  # noqa: E501
        """Return Business AML Search Hits  # noqa: E501

        Returns the business AML search hits from the AML search results.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_kyc_search_business_hits_by_search_id_with_http_info(search_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: (required)
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :param str hit_decisions: The hit decisions. <br> Available Values - [undecided, truematch, falsepositive, discarded]
        :return: KYCGetSearchBusinessesBySearchIdHitsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["search_id", "page", "page_size", "hit_decisions"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_kyc_search_business_hits_by_search_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'search_id' is set
        if "search_id" not in params or params["search_id"] is None:
            raise ValueError(
                "Missing the required parameter `search_id` when calling `get_kyc_search_business_hits_by_search_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "search_id" in params:
            path_params["searchId"] = params["search_id"]  # noqa: E501

        query_params = []
        if "page" in params:
            query_params.append(("page", params["page"]))  # noqa: E501
        if "page_size" in params:
            query_params.append(("pageSize", params["page_size"]))  # noqa: E501
        if "hit_decisions" in params:
            query_params.append(("hitDecisions", params["hit_decisions"]))  # noqa: E501

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
            "/compliance/kyc-protect/searches/businesses/{searchId}/hits",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="KYCGetSearchBusinessesBySearchIdHitsResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_kyc_search_business_hits_by_search_id_and_hit_id(
        self, search_id, hit_id, **kwargs
    ):  # noqa: E501
        """Return Full AML Search Hit Information By SearchId And HitId  # noqa: E501

        This endpoint will return the full hit information by search Id and hitId. <br> Once this information is requested the information returned is stored to the database as a snap shot of that point in time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_kyc_search_business_hits_by_search_id_and_hit_id(search_id, hit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: Id of the search (required)
        :param str hit_id: Id of the hit (required)
        :return: WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_kyc_search_business_hits_by_search_id_and_hit_id_with_http_info(
                search_id, hit_id, **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.get_kyc_search_business_hits_by_search_id_and_hit_id_with_http_info(
                    search_id, hit_id, **kwargs
                )
            )  # noqa: E501
            return data

    def get_kyc_search_business_hits_by_search_id_and_hit_id_with_http_info(
        self, search_id, hit_id, **kwargs
    ):  # noqa: E501
        """Return Full AML Search Hit Information By SearchId And HitId  # noqa: E501

        This endpoint will return the full hit information by search Id and hitId. <br> Once this information is requested the information returned is stored to the database as a snap shot of that point in time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_kyc_search_business_hits_by_search_id_and_hit_id_with_http_info(search_id, hit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: Id of the search (required)
        :param str hit_id: Id of the hit (required)
        :return: WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse
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
                    " to method get_kyc_search_business_hits_by_search_id_and_hit_id"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'search_id' is set
        if "search_id" not in params or params["search_id"] is None:
            raise ValueError(
                "Missing the required parameter `search_id` when calling `get_kyc_search_business_hits_by_search_id_and_hit_id`"
            )  # noqa: E501
        # verify the required parameter 'hit_id' is set
        if "hit_id" not in params or params["hit_id"] is None:
            raise ValueError(
                "Missing the required parameter `hit_id` when calling `get_kyc_search_business_hits_by_search_id_and_hit_id`"
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
            "/compliance/kyc-protect/searches/businesses/{searchId}/hits/{hitId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def k_yc_search_business(self, body, **kwargs):  # noqa: E501
        """Performs An AML Search For A Business And Saves The Results To The Database  # noqa: E501

        A request requires a name, at least one valid dataset, and a threshold. User will be deducted 1 credit for each AML search.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_search_business(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SearchesBusinessesBody1 body: (required)
        :return: MODEL931a1b
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.k_yc_search_business_with_http_info(
                body, **kwargs
            )  # noqa: E501
        else:
            (data) = self.k_yc_search_business_with_http_info(
                body, **kwargs
            )  # noqa: E501
            return data

    def k_yc_search_business_with_http_info(self, body, **kwargs):  # noqa: E501
        """Performs An AML Search For A Business And Saves The Results To The Database  # noqa: E501

        A request requires a name, at least one valid dataset, and a threshold. User will be deducted 1 credit for each AML search.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_search_business_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SearchesBusinessesBody1 body: (required)
        :return: MODEL931a1b
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
                    " to method k_yc_search_business" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `k_yc_search_business`"
            )  # noqa: E501

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
            "/compliance/kyc-protect/searches/businesses",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="MODEL931a1b",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def k_yc_search_business_get(self, **kwargs):  # noqa: E501
        """Returns Business AML Searches  # noqa: E501

        Returns a list of business AML searches ordered by modified date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_search_business_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :param bool is_scheduled:
        :return: MODELf73bb1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.k_yc_search_business_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.k_yc_search_business_get_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def k_yc_search_business_get_with_http_info(self, **kwargs):  # noqa: E501
        """Returns Business AML Searches  # noqa: E501

        Returns a list of business AML searches ordered by modified date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_search_business_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :param bool is_scheduled:
        :return: MODELf73bb1
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
                    " to method k_yc_search_business_get" % key
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
            "/compliance/kyc-protect/searches/businesses",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="MODELf73bb1",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def k_yc_search_business_put(self, **kwargs):  # noqa: E501
        """Update Business AML Searches  # noqa: E501

        Updates a batch of business AML searches.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_search_business_put(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SearchesBusinessesBody body:
        :return: KYCPUTSearchBusinessesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.k_yc_search_business_put_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.k_yc_search_business_put_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def k_yc_search_business_put_with_http_info(self, **kwargs):  # noqa: E501
        """Update Business AML Searches  # noqa: E501

        Updates a batch of business AML searches.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_search_business_put_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SearchesBusinessesBody body:
        :return: KYCPUTSearchBusinessesResponse
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
                    " to method k_yc_search_business_put" % key
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
            "/compliance/kyc-protect/searches/businesses",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="KYCPUTSearchBusinessesResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def put_kyc_search_business_by_search_id(self, search_id, **kwargs):  # noqa: E501
        """Update A Business AML Search By Search Id  # noqa: E501

        Updates a business AML search.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_kyc_search_business_by_search_id(search_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: (required)
        :param BusinessesSearchIdBody body:
        :return: KYCPutSearchBusinessesBySearchIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.put_kyc_search_business_by_search_id_with_http_info(
                search_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.put_kyc_search_business_by_search_id_with_http_info(
                search_id, **kwargs
            )  # noqa: E501
            return data

    def put_kyc_search_business_by_search_id_with_http_info(
        self, search_id, **kwargs
    ):  # noqa: E501
        """Update A Business AML Search By Search Id  # noqa: E501

        Updates a business AML search.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_kyc_search_business_by_search_id_with_http_info(search_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: (required)
        :param BusinessesSearchIdBody body:
        :return: KYCPutSearchBusinessesBySearchIdResponse
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
                    " to method put_kyc_search_business_by_search_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'search_id' is set
        if "search_id" not in params or params["search_id"] is None:
            raise ValueError(
                "Missing the required parameter `search_id` when calling `put_kyc_search_business_by_search_id`"
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
            "/compliance/kyc-protect/searches/businesses/{searchId}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="KYCPutSearchBusinessesBySearchIdResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def put_kyc_search_business_by_search_id_and_hit_id(
        self, search_id, hit_id, **kwargs
    ):  # noqa: E501
        """Update A Single Business Hit  # noqa: E501

        This endpoint will update a single business AML search hit by searchId and hitId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_kyc_search_business_by_search_id_and_hit_id(search_id, hit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: (required)
        :param str hit_id: (required)
        :param HitsHitIdBody body:
        :return: KYCBusinessSearchResultHitSummaryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.put_kyc_search_business_by_search_id_and_hit_id_with_http_info(
                search_id, hit_id, **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.put_kyc_search_business_by_search_id_and_hit_id_with_http_info(
                    search_id, hit_id, **kwargs
                )
            )  # noqa: E501
            return data

    def put_kyc_search_business_by_search_id_and_hit_id_with_http_info(
        self, search_id, hit_id, **kwargs
    ):  # noqa: E501
        """Update A Single Business Hit  # noqa: E501

        This endpoint will update a single business AML search hit by searchId and hitId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_kyc_search_business_by_search_id_and_hit_id_with_http_info(search_id, hit_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: (required)
        :param str hit_id: (required)
        :param HitsHitIdBody body:
        :return: KYCBusinessSearchResultHitSummaryResponse
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
                    " to method put_kyc_search_business_by_search_id_and_hit_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'search_id' is set
        if "search_id" not in params or params["search_id"] is None:
            raise ValueError(
                "Missing the required parameter `search_id` when calling `put_kyc_search_business_by_search_id_and_hit_id`"
            )  # noqa: E501
        # verify the required parameter 'hit_id' is set
        if "hit_id" not in params or params["hit_id"] is None:
            raise ValueError(
                "Missing the required parameter `hit_id` when calling `put_kyc_search_business_by_search_id_and_hit_id`"
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
            "/compliance/kyc-protect/searches/businesses/{searchId}/hits/{hitId}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="KYCBusinessSearchResultHitSummaryResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def put_kyc_search_business_hits_by_search_id(
        self, search_id, **kwargs
    ):  # noqa: E501
        """Update Batch Of Business AML Search Hits  # noqa: E501

        Updates a batch of business AML search hits.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_kyc_search_business_hits_by_search_id(search_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: (required)
        :param MODEL7b2457 body:
        :return: KYCPutSearchBusinessesBySearchIdHitsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.put_kyc_search_business_hits_by_search_id_with_http_info(
                search_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.put_kyc_search_business_hits_by_search_id_with_http_info(
                search_id, **kwargs
            )  # noqa: E501
            return data

    def put_kyc_search_business_hits_by_search_id_with_http_info(
        self, search_id, **kwargs
    ):  # noqa: E501
        """Update Batch Of Business AML Search Hits  # noqa: E501

        Updates a batch of business AML search hits.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_kyc_search_business_hits_by_search_id_with_http_info(search_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_id: (required)
        :param MODEL7b2457 body:
        :return: KYCPutSearchBusinessesBySearchIdHitsResponse
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
                    " to method put_kyc_search_business_hits_by_search_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'search_id' is set
        if "search_id" not in params or params["search_id"] is None:
            raise ValueError(
                "Missing the required parameter `search_id` when calling `put_kyc_search_business_hits_by_search_id`"
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
            "/compliance/kyc-protect/searches/businesses/{searchId}/hits",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="KYCPutSearchBusinessesBySearchIdHitsResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

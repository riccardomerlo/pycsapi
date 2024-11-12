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


class DecisionLogsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def decision_history(self, **kwargs):  # noqa: E501
        """Decision History  # noqa: E501

        Returns a log of all previously ran decisions that the user has permission to access, optionally filtered.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.decision_history(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provenir_id: Filter the returned usage log by the GUID for the associated decision trees, obtained from `/GUID`.
        :param str company_id: Filter the returned usage log by the Connect ID for the associated companies for each decision.
        :param str company_name: Filter the returned usage log by the Company Name for the associated companies for each decision.
        :param float status: Filter the returned usage log by the status for each decision.
        :param datetime from_date: Filter the returned usage log by the date the the decision was run.
        :param datetime to_date: Filter the returned usage log by the date the the decision was run.
        :param int page: Starting page number.
        :param int page_size: Number of items to return per Page.
        :return: ConnectDecisionEngineUsageLogResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.decision_history_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.decision_history_with_http_info(**kwargs)  # noqa: E501
            return data

    def decision_history_with_http_info(self, **kwargs):  # noqa: E501
        """Decision History  # noqa: E501

        Returns a log of all previously ran decisions that the user has permission to access, optionally filtered.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.decision_history_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str provenir_id: Filter the returned usage log by the GUID for the associated decision trees, obtained from `/GUID`.
        :param str company_id: Filter the returned usage log by the Connect ID for the associated companies for each decision.
        :param str company_name: Filter the returned usage log by the Company Name for the associated companies for each decision.
        :param float status: Filter the returned usage log by the status for each decision.
        :param datetime from_date: Filter the returned usage log by the date the the decision was run.
        :param datetime to_date: Filter the returned usage log by the date the the decision was run.
        :param int page: Starting page number.
        :param int page_size: Number of items to return per Page.
        :return: ConnectDecisionEngineUsageLogResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "provenir_id",
            "company_id",
            "company_name",
            "status",
            "from_date",
            "to_date",
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
                    " to method decision_history" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "provenir_id" in params:
            query_params.append(("provenirId", params["provenir_id"]))  # noqa: E501
        if "company_id" in params:
            query_params.append(("companyId", params["company_id"]))  # noqa: E501
        if "company_name" in params:
            query_params.append(("companyName", params["company_name"]))  # noqa: E501
        if "status" in params:
            query_params.append(("status", params["status"]))  # noqa: E501
        if "from_date" in params:
            query_params.append(("fromDate", params["from_date"]))  # noqa: E501
        if "to_date" in params:
            query_params.append(("toDate", params["to_date"]))  # noqa: E501
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
            "/decisionEngine/usageLog",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectDecisionEngineUsageLogResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_decision_log(self, decision_log_id, **kwargs):  # noqa: E501
        """Get Decision Log  # noqa: E501

        Returns a specified decision log for a previously ran decision.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_decision_log(decision_log_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str decision_log_id: The unique identifier of the decision log to retrieve, obtained from `/usageLog`. (required)
        :return: ConnectDecisionEngineDecisionLogResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_decision_log_with_http_info(
                decision_log_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_decision_log_with_http_info(
                decision_log_id, **kwargs
            )  # noqa: E501
            return data

    def get_decision_log_with_http_info(self, decision_log_id, **kwargs):  # noqa: E501
        """Get Decision Log  # noqa: E501

        Returns a specified decision log for a previously ran decision.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_decision_log_with_http_info(decision_log_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str decision_log_id: The unique identifier of the decision log to retrieve, obtained from `/usageLog`. (required)
        :return: ConnectDecisionEngineDecisionLogResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["decision_log_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_decision_log" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'decision_log_id' is set
        if "decision_log_id" not in params or params["decision_log_id"] is None:
            raise ValueError(
                "Missing the required parameter `decision_log_id` when calling `get_decision_log`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "decision_log_id" in params:
            path_params["decisionLogId"] = params["decision_log_id"]  # noqa: E501

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
            "/decisionEngine/usageLog/{decisionLogId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectDecisionEngineDecisionLogResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update_decision_log(self, decision_log_id, **kwargs):  # noqa: E501
        """Update Decision Log  # noqa: E501

        Updates the status and/or notes for a specified decision.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_decision_log(decision_log_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str decision_log_id: The unique identifier of the decision log to retrieve, obtained from `/usageLog`. (required)
        :param ConnectDecisionEngineUpdateDecisionRequest body:
        :return: ConnectDecisionEngineDecisionLogResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.update_decision_log_with_http_info(
                decision_log_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.update_decision_log_with_http_info(
                decision_log_id, **kwargs
            )  # noqa: E501
            return data

    def update_decision_log_with_http_info(
        self, decision_log_id, **kwargs
    ):  # noqa: E501
        """Update Decision Log  # noqa: E501

        Updates the status and/or notes for a specified decision.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_decision_log_with_http_info(decision_log_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str decision_log_id: The unique identifier of the decision log to retrieve, obtained from `/usageLog`. (required)
        :param ConnectDecisionEngineUpdateDecisionRequest body:
        :return: ConnectDecisionEngineDecisionLogResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["decision_log_id", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_decision_log" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'decision_log_id' is set
        if "decision_log_id" not in params or params["decision_log_id"] is None:
            raise ValueError(
                "Missing the required parameter `decision_log_id` when calling `update_decision_log`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "decision_log_id" in params:
            path_params["decisionLogId"] = params["decision_log_id"]  # noqa: E501

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
            "/decisionEngine/usageLog/{decisionLogId}",
            "PATCH",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectDecisionEngineDecisionLogResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
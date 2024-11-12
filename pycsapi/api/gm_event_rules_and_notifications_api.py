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


class GMEventRulesAndNotificationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def all_event_rules(self, **kwargs):  # noqa: E501
        """All EventRules  # noqa: E501

        Get all available notification event rules. Notification event rules allow you to control which events you wish to monitor for the `companies` contained within a given `portfolio`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.all_event_rules(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ConnectMonitoringEventRulesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.all_event_rules_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.all_event_rules_with_http_info(**kwargs)  # noqa: E501
            return data

    def all_event_rules_with_http_info(self, **kwargs):  # noqa: E501
        """All EventRules  # noqa: E501

        Get all available notification event rules. Notification event rules allow you to control which events you wish to monitor for the `companies` contained within a given `portfolio`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.all_event_rules_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ConnectMonitoringEventRulesResponse
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
                    " to method all_event_rules" % key
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
            "/monitoring/eventRules",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectMonitoringEventRulesResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def all_notification_events(self, **kwargs):  # noqa: E501
        """All Notification Events  # noqa: E501

        Get all notification events generated for companies monitored in your portfolios, based on the notification rules enabled. The notification events returned will be filtered based upon the supplied search criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.all_notification_events(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_query: Return notificationEvents that match the given value
        :param str sort_by: Sort results by this column. Null values of sort column are listed after non-nulls.
        :param str sort_dir: The direction that you wish to sort results by.
        :param datetime start_date: The start date on which results are filtered.
        :param datetime end_date: The end date on which results are filtered.
        :param int page: Starting page number inGlobal Monitoring is `0`. If all items are displayed on one page this can also be left blank.
        :param int page_size: Number of items to return per Page.
        :param bool filter_by_created_date: Set to `true` to filter the Notification Events of the \"createdDate\" field when using `startDate` and `endDate` parameters. By default this is set to `false`, with the date parameters filtering using the \"eventDate\" field.
        :return: ConnectMonitoringAllNotificationsEvents
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.all_notification_events_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.all_notification_events_with_http_info(**kwargs)  # noqa: E501
            return data

    def all_notification_events_with_http_info(self, **kwargs):  # noqa: E501
        """All Notification Events  # noqa: E501

        Get all notification events generated for companies monitored in your portfolios, based on the notification rules enabled. The notification events returned will be filtered based upon the supplied search criteria.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.all_notification_events_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str search_query: Return notificationEvents that match the given value
        :param str sort_by: Sort results by this column. Null values of sort column are listed after non-nulls.
        :param str sort_dir: The direction that you wish to sort results by.
        :param datetime start_date: The start date on which results are filtered.
        :param datetime end_date: The end date on which results are filtered.
        :param int page: Starting page number inGlobal Monitoring is `0`. If all items are displayed on one page this can also be left blank.
        :param int page_size: Number of items to return per Page.
        :param bool filter_by_created_date: Set to `true` to filter the Notification Events of the \"createdDate\" field when using `startDate` and `endDate` parameters. By default this is set to `false`, with the date parameters filtering using the \"eventDate\" field.
        :return: ConnectMonitoringAllNotificationsEvents
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "search_query",
            "sort_by",
            "sort_dir",
            "start_date",
            "end_date",
            "page",
            "page_size",
            "filter_by_created_date",
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
                    " to method all_notification_events" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "search_query" in params:
            query_params.append(("searchQuery", params["search_query"]))  # noqa: E501
        if "sort_by" in params:
            query_params.append(("sortBy", params["sort_by"]))  # noqa: E501
        if "sort_dir" in params:
            query_params.append(("sortDir", params["sort_dir"]))  # noqa: E501
        if "start_date" in params:
            query_params.append(("startDate", params["start_date"]))  # noqa: E501
        if "end_date" in params:
            query_params.append(("endDate", params["end_date"]))  # noqa: E501
        if "page" in params:
            query_params.append(("page", params["page"]))  # noqa: E501
        if "page_size" in params:
            query_params.append(("pageSize", params["page_size"]))  # noqa: E501
        if "filter_by_created_date" in params:
            query_params.append(
                ("filterByCreatedDate", params["filter_by_created_date"])
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
            "/monitoring/notificationEvents",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectMonitoringAllNotificationsEvents",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def filtered_event_rules(self, country_code, **kwargs):  # noqa: E501
        """Filtered EventRules  # noqa: E501

        Get all available notification event rules for the given `countryCode`. Notification event rules allow you to control which events you wish to monitor for the `companies` contained within a given `portfolio`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.filtered_event_rules(country_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country_code: ISO/Alpha 2 format country code for which notification event rules will be returned. (required)
        :return: ConnectMonitoringEventRulesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.filtered_event_rules_with_http_info(
                country_code, **kwargs
            )  # noqa: E501
        else:
            (data) = self.filtered_event_rules_with_http_info(
                country_code, **kwargs
            )  # noqa: E501
            return data

    def filtered_event_rules_with_http_info(self, country_code, **kwargs):  # noqa: E501
        """Filtered EventRules  # noqa: E501

        Get all available notification event rules for the given `countryCode`. Notification event rules allow you to control which events you wish to monitor for the `companies` contained within a given `portfolio`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.filtered_event_rules_with_http_info(country_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country_code: ISO/Alpha 2 format country code for which notification event rules will be returned. (required)
        :return: ConnectMonitoringEventRulesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["country_code"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method filtered_event_rules" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'country_code' is set
        if "country_code" not in params or params["country_code"] is None:
            raise ValueError(
                "Missing the required parameter `country_code` when calling `filtered_event_rules`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "country_code" in params:
            path_params["countryCode"] = params["country_code"]  # noqa: E501

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
            "/monitoring/eventRules/{countryCode}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectMonitoringEventRulesResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def list_company_events(self, id, **kwargs):  # noqa: E501
        """List Company Events  # noqa: E501

        Endpoint to return a collection of `events` for the given company, optionally filtered on the supplied search criteria. Event information will only be returned if the company exists in at least one of your `portfolios`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_company_events(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The connectId of the company that you wish to retrieve events for. (required)
        :param datetime start_date: The start date on which results are filtered.
        :param datetime end_date: The end date on which results are filtered.
        :param int page: Starting page number inGlobal Monitoring is `0`. If all items are displayed on one page this can also be left blank.
        :param int page_size: Number of items to return per Page.
        :return: ConnectMonitoringCompanyEvents
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.list_company_events_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_company_events_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_company_events_with_http_info(self, id, **kwargs):  # noqa: E501
        """List Company Events  # noqa: E501

        Endpoint to return a collection of `events` for the given company, optionally filtered on the supplied search criteria. Event information will only be returned if the company exists in at least one of your `portfolios`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_company_events_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The connectId of the company that you wish to retrieve events for. (required)
        :param datetime start_date: The start date on which results are filtered.
        :param datetime end_date: The end date on which results are filtered.
        :param int page: Starting page number inGlobal Monitoring is `0`. If all items are displayed on one page this can also be left blank.
        :param int page_size: Number of items to return per Page.
        :return: ConnectMonitoringCompanyEvents
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["id", "start_date", "end_date", "page", "page_size"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_company_events" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `list_company_events`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []
        if "start_date" in params:
            query_params.append(("startDate", params["start_date"]))  # noqa: E501
        if "end_date" in params:
            query_params.append(("endDate", params["end_date"]))  # noqa: E501
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
            "/monitoring/companies/{id}/events",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectMonitoringCompanyEvents",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

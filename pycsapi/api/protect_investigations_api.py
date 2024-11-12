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


class ProtectInvestigationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_investigations_records(
        self, body, investigation_id, **kwargs
    ):  # noqa: E501
        """Add Investigations Records  # noqa: E501

        Requires the 'Investigation Id' in path, followed by 'Record Id' in the request body to add a record to the previously created Investigation.<br><br>By adding InvestigationRecords you are confirming that the result is a match to your search criteria. <br><br>To return to the original Investigation search to allocate other records, use \"GET Investigation results by ID.\".  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_investigations_records(body, investigation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectProtectCreateInvestigationRecordBody body: (required)
        :param str investigation_id: (required)
        :return: list[ConnectProtectRecord]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.add_investigations_records_with_http_info(
                body, investigation_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.add_investigations_records_with_http_info(
                body, investigation_id, **kwargs
            )  # noqa: E501
            return data

    def add_investigations_records_with_http_info(
        self, body, investigation_id, **kwargs
    ):  # noqa: E501
        """Add Investigations Records  # noqa: E501

        Requires the 'Investigation Id' in path, followed by 'Record Id' in the request body to add a record to the previously created Investigation.<br><br>By adding InvestigationRecords you are confirming that the result is a match to your search criteria. <br><br>To return to the original Investigation search to allocate other records, use \"GET Investigation results by ID.\".  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_investigations_records_with_http_info(body, investigation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectProtectCreateInvestigationRecordBody body: (required)
        :param str investigation_id: (required)
        :return: list[ConnectProtectRecord]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body", "investigation_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_investigations_records" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `add_investigations_records`"
            )  # noqa: E501
        # verify the required parameter 'investigation_id' is set
        if "investigation_id" not in params or params["investigation_id"] is None:
            raise ValueError(
                "Missing the required parameter `investigation_id` when calling `add_investigations_records`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "investigation_id" in params:
            path_params["investigationId"] = params["investigation_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "text/json", "text/plain"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = (
            self.api_client.select_header_content_type(  # noqa: E501
                ["application/json", "text/json", "application/*+json"]
            )
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/protect/investigations/{investigationId}/records",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[ConnectProtectRecord]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def assign_risk_to_investigation(self, body, id, **kwargs):  # noqa: E501
        """Assign Risk to Investigation  # noqa: E501

        Allows user to update the risk with an Investigation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.assign_risk_to_investigation(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AssignRiskToInvestigationDto body: (required)
        :param str id: (required)
        :return: InvestigationRiskResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.assign_risk_to_investigation_with_http_info(
                body, id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.assign_risk_to_investigation_with_http_info(
                body, id, **kwargs
            )  # noqa: E501
            return data

    def assign_risk_to_investigation_with_http_info(
        self, body, id, **kwargs
    ):  # noqa: E501
        """Assign Risk to Investigation  # noqa: E501

        Allows user to update the risk with an Investigation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.assign_risk_to_investigation_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AssignRiskToInvestigationDto body: (required)
        :param str id: (required)
        :return: InvestigationRiskResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body", "id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method assign_risk_to_investigation" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `assign_risk_to_investigation`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `assign_risk_to_investigation`"
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
            ["application/json", "text/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = (
            self.api_client.select_header_content_type(  # noqa: E501
                ["application/json", "text/json", "application/*+json"]
            )
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/protect/investigations/{id}/risk",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InvestigationRiskResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def create_investigation_and_return_report_link(self, body, **kwargs):  # noqa: E501
        """Create Investigation And Return Report Link  # noqa: E501

        Creates an investigation and returns a link to the report.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_investigation_and_return_report_link(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateInvestigationQueryDto body: (required)
        :return: FileDownloadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.create_investigation_and_return_report_link_with_http_info(
                body, **kwargs
            )  # noqa: E501
        else:
            (data) = self.create_investigation_and_return_report_link_with_http_info(
                body, **kwargs
            )  # noqa: E501
            return data

    def create_investigation_and_return_report_link_with_http_info(
        self, body, **kwargs
    ):  # noqa: E501
        """Create Investigation And Return Report Link  # noqa: E501

        Creates an investigation and returns a link to the report.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_investigation_and_return_report_link_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateInvestigationQueryDto body: (required)
        :return: FileDownloadResponse
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
                    " to method create_investigation_and_return_report_link" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `create_investigation_and_return_report_link`"
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
            ["application/json", "text/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = (
            self.api_client.select_header_content_type(  # noqa: E501
                ["application/json", "text/json", "application/*+json"]
            )
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/protect/investigations/file",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="FileDownloadResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def create_investigation_note(self, body, id, **kwargs):  # noqa: E501
        """Create Investigation Note  # noqa: E501

        Creates a note to a specific investigation ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_investigation_note(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateInvestigationNoteDto body: (required)
        :param str id: (required)
        :return: InvestigationNote
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.create_investigation_note_with_http_info(
                body, id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.create_investigation_note_with_http_info(
                body, id, **kwargs
            )  # noqa: E501
            return data

    def create_investigation_note_with_http_info(
        self, body, id, **kwargs
    ):  # noqa: E501
        """Create Investigation Note  # noqa: E501

        Creates a note to a specific investigation ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_investigation_note_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreateInvestigationNoteDto body: (required)
        :param str id: (required)
        :return: InvestigationNote
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body", "id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_investigation_note" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `create_investigation_note`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `create_investigation_note`"
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
            ["application/json", "text/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = (
            self.api_client.select_header_content_type(  # noqa: E501
                ["application/json", "text/json", "application/*+json"]
            )
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/protect/investigations/{id}/notes",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InvestigationNote",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def create_protect_investigation(self, body, **kwargs):  # noqa: E501
        """Create Protect Investigation  # noqa: E501

        Creates an Investigation according to the provided Investigation criteria. Each result is potential match which is attributed a relevancy/match score between 1-100 and a high level reason for it's inclusion in the World Compliance Database by looking at the Reason Listed and Comments to firstly ascertain whether the entry is a match for you search criteria and then utilize the data available for your own onboarding needs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_protect_investigation(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectProtectCreateInvestigationQueryDto body: (required)
        :return: ConnectProtectInvestigationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.create_protect_investigation_with_http_info(
                body, **kwargs
            )  # noqa: E501
        else:
            (data) = self.create_protect_investigation_with_http_info(
                body, **kwargs
            )  # noqa: E501
            return data

    def create_protect_investigation_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create Protect Investigation  # noqa: E501

        Creates an Investigation according to the provided Investigation criteria. Each result is potential match which is attributed a relevancy/match score between 1-100 and a high level reason for it's inclusion in the World Compliance Database by looking at the Reason Listed and Comments to firstly ascertain whether the entry is a match for you search criteria and then utilize the data available for your own onboarding needs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_protect_investigation_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectProtectCreateInvestigationQueryDto body: (required)
        :return: ConnectProtectInvestigationResponse
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
                    " to method create_protect_investigation" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `create_protect_investigation`"
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
            "/protect/investigations",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectProtectInvestigationResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def create_protect_investigation_pdf(
        self, body, investigation_id, **kwargs
    ):  # noqa: E501
        """Create Protect Investigation PDF  # noqa: E501

        Creates a PDF that shows the full report for the selected entities. This report will include search criteria used, user, time/date stamp and full World Compliance Report. It is recommended to call this endpoint before adding InvestigationRecords to an Investigation, as only non-processed alerts populate the PDF.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_protect_investigation_pdf(body, investigation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectProtectGetInvestigationFileBodyDto body: (required)
        :param str investigation_id: (required)
        :return: ConnectProtectInvestigationFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.create_protect_investigation_pdf_with_http_info(
                body, investigation_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.create_protect_investigation_pdf_with_http_info(
                body, investigation_id, **kwargs
            )  # noqa: E501
            return data

    def create_protect_investigation_pdf_with_http_info(
        self, body, investigation_id, **kwargs
    ):  # noqa: E501
        """Create Protect Investigation PDF  # noqa: E501

        Creates a PDF that shows the full report for the selected entities. This report will include search criteria used, user, time/date stamp and full World Compliance Report. It is recommended to call this endpoint before adding InvestigationRecords to an Investigation, as only non-processed alerts populate the PDF.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_protect_investigation_pdf_with_http_info(body, investigation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectProtectGetInvestigationFileBodyDto body: (required)
        :param str investigation_id: (required)
        :return: ConnectProtectInvestigationFileResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body", "investigation_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_protect_investigation_pdf" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `create_protect_investigation_pdf`"
            )  # noqa: E501
        # verify the required parameter 'investigation_id' is set
        if "investigation_id" not in params or params["investigation_id"] is None:
            raise ValueError(
                "Missing the required parameter `investigation_id` when calling `create_protect_investigation_pdf`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "investigation_id" in params:
            path_params["investigationId"] = params["investigation_id"]  # noqa: E501

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
            "/protect/investigations/{investigationId}/file",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectProtectInvestigationFileResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def delete_investigation(self, investigation_id, **kwargs):  # noqa: E501
        """Delete Investigation  # noqa: E501

        Deletes an Investigation by {Id} number. This will remove the entire Investigation and all results within it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_investigation(investigation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str investigation_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_investigation_with_http_info(
                investigation_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.delete_investigation_with_http_info(
                investigation_id, **kwargs
            )  # noqa: E501
            return data

    def delete_investigation_with_http_info(
        self, investigation_id, **kwargs
    ):  # noqa: E501
        """Delete Investigation  # noqa: E501

        Deletes an Investigation by {Id} number. This will remove the entire Investigation and all results within it.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_investigation_with_http_info(investigation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str investigation_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["investigation_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_investigation" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'investigation_id' is set
        if "investigation_id" not in params or params["investigation_id"] is None:
            raise ValueError(
                "Missing the required parameter `investigation_id` when calling `delete_investigation`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "investigation_id" in params:
            path_params["investigationId"] = params["investigation_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "text/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/protect/investigations/{investigationId}",
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

    def delete_investigation_records(
        self, body, investigation_id, **kwargs
    ):  # noqa: E501
        """Delete Investigation Records  # noqa: E501

        Deletes a record from an Investigation ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_investigation_records(body, investigation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeleteRecordsDto body: (required)
        :param str investigation_id: (required)
        :return: list[Record]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_investigation_records_with_http_info(
                body, investigation_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.delete_investigation_records_with_http_info(
                body, investigation_id, **kwargs
            )  # noqa: E501
            return data

    def delete_investigation_records_with_http_info(
        self, body, investigation_id, **kwargs
    ):  # noqa: E501
        """Delete Investigation Records  # noqa: E501

        Deletes a record from an Investigation ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_investigation_records_with_http_info(body, investigation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeleteRecordsDto body: (required)
        :param str investigation_id: (required)
        :return: list[Record]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body", "investigation_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_investigation_records" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `delete_investigation_records`"
            )  # noqa: E501
        # verify the required parameter 'investigation_id' is set
        if "investigation_id" not in params or params["investigation_id"] is None:
            raise ValueError(
                "Missing the required parameter `investigation_id` when calling `delete_investigation_records`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "investigation_id" in params:
            path_params["investigationId"] = params["investigation_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "text/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = (
            self.api_client.select_header_content_type(  # noqa: E501
                ["application/json", "text/json", "application/*+json"]
            )
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/protect/investigations/{investigationId}/records",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[Record]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_investigation_notes(self, id, **kwargs):  # noqa: E501
        """Get Investigation Notes  # noqa: E501

        Returns the notes created against a specific investigation ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_investigation_notes(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param int page:
        :param int limit:
        :return: list[InvestigationNote]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_investigation_notes_with_http_info(
                id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_investigation_notes_with_http_info(
                id, **kwargs
            )  # noqa: E501
            return data

    def get_investigation_notes_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Investigation Notes  # noqa: E501

        Returns the notes created against a specific investigation ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_investigation_notes_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :param int page:
        :param int limit:
        :return: list[InvestigationNote]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["id", "page", "limit"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_investigation_notes" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_investigation_notes`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []
        if "page" in params:
            query_params.append(("page", params["page"]))  # noqa: E501
        if "limit" in params:
            query_params.append(("limit", params["limit"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "text/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/protect/investigations/{id}/notes",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[InvestigationNote]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_investigation_results_by_id(self, investigation_id, **kwargs):  # noqa: E501
        """Get Investigation Results By Id  # noqa: E501

        Returns original Investigation search results to assign any other results to the records.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_investigation_results_by_id(investigation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str investigation_id: (required)
        :param int page:
        :param int limit:
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_investigation_results_by_id_with_http_info(
                investigation_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_investigation_results_by_id_with_http_info(
                investigation_id, **kwargs
            )  # noqa: E501
            return data

    def get_investigation_results_by_id_with_http_info(
        self, investigation_id, **kwargs
    ):  # noqa: E501
        """Get Investigation Results By Id  # noqa: E501

        Returns original Investigation search results to assign any other results to the records.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_investigation_results_by_id_with_http_info(investigation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str investigation_id: (required)
        :param int page:
        :param int limit:
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["investigation_id", "page", "limit"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_investigation_results_by_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'investigation_id' is set
        if "investigation_id" not in params or params["investigation_id"] is None:
            raise ValueError(
                "Missing the required parameter `investigation_id` when calling `get_investigation_results_by_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "investigation_id" in params:
            path_params["investigationId"] = params["investigation_id"]  # noqa: E501

        query_params = []
        if "page" in params:
            query_params.append(("page", params["page"]))  # noqa: E501
        if "limit" in params:
            query_params.append(("limit", params["limit"]))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "text/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/protect/investigations/{investigationId}/results",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse2006",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def list_all_protect_investigations(self, **kwargs):  # noqa: E501
        """List All Protect Investigations  # noqa: E501

        Endpoint to return all investigations. Filter response by using query parameters. Use the alertsCount parameter to only return Investigations with alerts greater than the supplied value.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_all_protect_investigations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool scheduled:
        :param int alerts_count:
        :param str type:
        :param str q: Keyword search: It searches in the 'name' fields of the investigation.
        :param str order:
        :param str order_by:
        :param int page: Starting page number.
        :param int page_size: Number of items to return per Page.
        :return: list[ConnectProtectInvestigation]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.list_all_protect_investigations_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (data) = self.list_all_protect_investigations_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def list_all_protect_investigations_with_http_info(self, **kwargs):  # noqa: E501
        """List All Protect Investigations  # noqa: E501

        Endpoint to return all investigations. Filter response by using query parameters. Use the alertsCount parameter to only return Investigations with alerts greater than the supplied value.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_all_protect_investigations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param bool scheduled:
        :param int alerts_count:
        :param str type:
        :param str q: Keyword search: It searches in the 'name' fields of the investigation.
        :param str order:
        :param str order_by:
        :param int page: Starting page number.
        :param int page_size: Number of items to return per Page.
        :return: list[ConnectProtectInvestigation]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "scheduled",
            "alerts_count",
            "type",
            "q",
            "order",
            "order_by",
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
                    " to method list_all_protect_investigations" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "scheduled" in params:
            query_params.append(("scheduled", params["scheduled"]))  # noqa: E501
        if "alerts_count" in params:
            query_params.append(("alertsCount", params["alerts_count"]))  # noqa: E501
        if "type" in params:
            query_params.append(("type", params["type"]))  # noqa: E501
        if "q" in params:
            query_params.append(("q", params["q"]))  # noqa: E501
        if "order" in params:
            query_params.append(("order", params["order"]))  # noqa: E501
        if "order_by" in params:
            query_params.append(("orderBy", params["order_by"]))  # noqa: E501
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
            "/protect/investigations",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[ConnectProtectInvestigation]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def return_investigations_records(self, investigation_id, **kwargs):  # noqa: E501
        """Return Investigation Records  # noqa: E501

        Requires the 'Investigation Id' in path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.return_investigations_records(investigation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str investigation_id: Investigation Id (required)
        :param int page: Starting page number.
        :param int page_size: Number of items to return per Page.
        :return: list[ConnectProtectRecord]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.return_investigations_records_with_http_info(
                investigation_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.return_investigations_records_with_http_info(
                investigation_id, **kwargs
            )  # noqa: E501
            return data

    def return_investigations_records_with_http_info(
        self, investigation_id, **kwargs
    ):  # noqa: E501
        """Return Investigation Records  # noqa: E501

        Requires the 'Investigation Id' in path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.return_investigations_records_with_http_info(investigation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str investigation_id: Investigation Id (required)
        :param int page: Starting page number.
        :param int page_size: Number of items to return per Page.
        :return: list[ConnectProtectRecord]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["investigation_id", "page", "page_size"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method return_investigations_records" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'investigation_id' is set
        if "investigation_id" not in params or params["investigation_id"] is None:
            raise ValueError(
                "Missing the required parameter `investigation_id` when calling `return_investigations_records`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "investigation_id" in params:
            path_params["investigationId"] = params["investigation_id"]  # noqa: E501

        query_params = []
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
            "/protect/investigations/{investigationId}/records",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[ConnectProtectRecord]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def return_protect_investigation_by_id(
        self, investigation_id, **kwargs
    ):  # noqa: E501
        """Return Protect Investigation By Id  # noqa: E501

        Endpoint to return a specific Investigation by ID. Can also be used to retrieve the associated Schedule Id that has been linked to the Investigation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.return_protect_investigation_by_id(investigation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str investigation_id: (required)
        :return: ConnectProtectInvestigationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.return_protect_investigation_by_id_with_http_info(
                investigation_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.return_protect_investigation_by_id_with_http_info(
                investigation_id, **kwargs
            )  # noqa: E501
            return data

    def return_protect_investigation_by_id_with_http_info(
        self, investigation_id, **kwargs
    ):  # noqa: E501
        """Return Protect Investigation By Id  # noqa: E501

        Endpoint to return a specific Investigation by ID. Can also be used to retrieve the associated Schedule Id that has been linked to the Investigation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.return_protect_investigation_by_id_with_http_info(investigation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str investigation_id: (required)
        :return: ConnectProtectInvestigationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["investigation_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method return_protect_investigation_by_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'investigation_id' is set
        if "investigation_id" not in params or params["investigation_id"] is None:
            raise ValueError(
                "Missing the required parameter `investigation_id` when calling `return_protect_investigation_by_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "investigation_id" in params:
            path_params["investigationId"] = params["investigation_id"]  # noqa: E501

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
            "/protect/investigations/{investigationId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectProtectInvestigationResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def returns_investigation_report(
        self, body, investigation_id, **kwargs
    ):  # noqa: E501
        """Returns Investigation Report  # noqa: E501

        This endpoint will Return a report by providing a file path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.returns_investigation_report(body, investigation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GetInvestigationFileBodyDto body: (required)
        :param str investigation_id: (required)
        :return: FileDownloadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.returns_investigation_report_with_http_info(
                body, investigation_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.returns_investigation_report_with_http_info(
                body, investigation_id, **kwargs
            )  # noqa: E501
            return data

    def returns_investigation_report_with_http_info(
        self, body, investigation_id, **kwargs
    ):  # noqa: E501
        """Returns Investigation Report  # noqa: E501

        This endpoint will Return a report by providing a file path.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.returns_investigation_report_with_http_info(body, investigation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param GetInvestigationFileBodyDto body: (required)
        :param str investigation_id: (required)
        :return: FileDownloadResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body", "investigation_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method returns_investigation_report" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `returns_investigation_report`"
            )  # noqa: E501
        # verify the required parameter 'investigation_id' is set
        if "investigation_id" not in params or params["investigation_id"] is None:
            raise ValueError(
                "Missing the required parameter `investigation_id` when calling `returns_investigation_report`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "investigation_id" in params:
            path_params["investigationId"] = params["investigation_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["text/plain", "application/json", "text/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = (
            self.api_client.select_header_content_type(  # noqa: E501
                ["application/json", "text/json", "application/*+json"]
            )
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/protect/investigations/{investigationId}/records/file",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="FileDownloadResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update_investigations_records(
        self, body, investigation_id, **kwargs
    ):  # noqa: E501
        """Update Investigation Records  # noqa: E501

        Sends an update to the investigation specified by the ID and changes will be reflected within that investigation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_investigations_records(body, investigation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateInvestigationRecordsDto body: (required)
        :param str investigation_id: (required)
        :return: list[Record]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.update_investigations_records_with_http_info(
                body, investigation_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.update_investigations_records_with_http_info(
                body, investigation_id, **kwargs
            )  # noqa: E501
            return data

    def update_investigations_records_with_http_info(
        self, body, investigation_id, **kwargs
    ):  # noqa: E501
        """Update Investigation Records  # noqa: E501

        Sends an update to the investigation specified by the ID and changes will be reflected within that investigation.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_investigations_records_with_http_info(body, investigation_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateInvestigationRecordsDto body: (required)
        :param str investigation_id: (required)
        :return: list[Record]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body", "investigation_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_investigations_records" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `update_investigations_records`"
            )  # noqa: E501
        # verify the required parameter 'investigation_id' is set
        if "investigation_id" not in params or params["investigation_id"] is None:
            raise ValueError(
                "Missing the required parameter `investigation_id` when calling `update_investigations_records`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "investigation_id" in params:
            path_params["investigationId"] = params["investigation_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "body" in params:
            body_params = params["body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "text/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = (
            self.api_client.select_header_content_type(  # noqa: E501
                ["application/json", "text/json", "application/*+json"]
            )
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/protect/investigations/{investigationId}/records",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[Record]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

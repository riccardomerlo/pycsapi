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


class FreshInvestigationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def comments_for_fresh_investigation_order_id(
        self, body, order_id, **kwargs
    ):  # noqa: E501
        """Comments for fresh investigation orderId  # noqa: E501

        Returns the status of comments for the particular order.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.comments_for_fresh_investigation_order_id(body, order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FreshInvestigationCommentsForOrderRequest body: (required)
        :param str order_id: fresh investigation orderId (required)
        :return: FreshInvestigationCommentsForOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.comments_for_fresh_investigation_order_id_with_http_info(
                body, order_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.comments_for_fresh_investigation_order_id_with_http_info(
                body, order_id, **kwargs
            )  # noqa: E501
            return data

    def comments_for_fresh_investigation_order_id_with_http_info(
        self, body, order_id, **kwargs
    ):  # noqa: E501
        """Comments for fresh investigation orderId  # noqa: E501

        Returns the status of comments for the particular order.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.comments_for_fresh_investigation_order_id_with_http_info(body, order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FreshInvestigationCommentsForOrderRequest body: (required)
        :param str order_id: fresh investigation orderId (required)
        :return: FreshInvestigationCommentsForOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body", "order_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method comments_for_fresh_investigation_order_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `comments_for_fresh_investigation_order_id`"
            )  # noqa: E501
        # verify the required parameter 'order_id' is set
        if "order_id" not in params or params["order_id"] is None:
            raise ValueError(
                "Missing the required parameter `order_id` when calling `comments_for_fresh_investigation_order_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "order_id" in params:
            path_params["orderId"] = params["order_id"]  # noqa: E501

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
            "/freshinvestigations/{orderId}/comments",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="FreshInvestigationCommentsForOrderResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def create_fresh_investigation(self, **kwargs):  # noqa: E501
        """Create Fresh Investigation  # noqa: E501

        Places an order for a Fresh Investigation (Offline Report). Providing as much detail as possible about the Company, our team will use official sources and registries to quickly answer questions about a company's stability and financial health. Fresh Investigations take 5.5 days on average to complete. By adding `consent:true` to the request, you are allowing Creditsafe to disclose your company details to the company you have requested the Investigation against, to be used only in the aim of improving our Investigation report.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_fresh_investigation(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectFreshInvCreateInvestigation body:
        :return: ConnectFreshInvInvestigationConfirmed
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.create_fresh_investigation_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (data) = self.create_fresh_investigation_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def create_fresh_investigation_with_http_info(self, **kwargs):  # noqa: E501
        """Create Fresh Investigation  # noqa: E501

        Places an order for a Fresh Investigation (Offline Report). Providing as much detail as possible about the Company, our team will use official sources and registries to quickly answer questions about a company's stability and financial health. Fresh Investigations take 5.5 days on average to complete. By adding `consent:true` to the request, you are allowing Creditsafe to disclose your company details to the company you have requested the Investigation against, to be used only in the aim of improving our Investigation report.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_fresh_investigation_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectFreshInvCreateInvestigation body:
        :return: ConnectFreshInvInvestigationConfirmed
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
                    " to method create_fresh_investigation" % key
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
            "/freshinvestigations",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectFreshInvInvestigationConfirmed",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def delete_fresh_investigations(self, order_id, **kwargs):  # noqa: E501
        """Delete Fresh Investigations  # noqa: E501

        Deletes specified investigations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_fresh_investigations(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: Investigation id. (required)
        :return: DeleteFreshInvetigationsByOrderId
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_fresh_investigations_with_http_info(
                order_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.delete_fresh_investigations_with_http_info(
                order_id, **kwargs
            )  # noqa: E501
            return data

    def delete_fresh_investigations_with_http_info(
        self, order_id, **kwargs
    ):  # noqa: E501
        """Delete Fresh Investigations  # noqa: E501

        Deletes specified investigations.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_fresh_investigations_with_http_info(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: Investigation id. (required)
        :return: DeleteFreshInvetigationsByOrderId
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["order_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_fresh_investigations" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'order_id' is set
        if "order_id" not in params or params["order_id"] is None:
            raise ValueError(
                "Missing the required parameter `order_id` when calling `delete_fresh_investigations`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "order_id" in params:
            path_params["orderId"] = params["order_id"]  # noqa: E501

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
            "/freshinvestigations/{orderId}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="DeleteFreshInvetigationsByOrderId",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_attachment_for_the_given_fresh_investigation_attachment_id(
        self, order_id, id, **kwargs
    ):  # noqa: E501
        """Get attachment for the given fresh investigation attachment Id  # noqa: E501

        Retrieve attachment for the given attachmentId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_attachment_for_the_given_fresh_investigation_attachment_id(order_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: fresh investigation orderId (required)
        :param str id: fresh investigation attachment id for the given order (required)
        :return: CreditsafeFreshInvestigationGlobalDataCoreAttachmentBinaryAttachment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_attachment_for_the_given_fresh_investigation_attachment_id_with_http_info(
                order_id, id, **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.get_attachment_for_the_given_fresh_investigation_attachment_id_with_http_info(
                    order_id, id, **kwargs
                )
            )  # noqa: E501
            return data

    def get_attachment_for_the_given_fresh_investigation_attachment_id_with_http_info(
        self, order_id, id, **kwargs
    ):  # noqa: E501
        """Get attachment for the given fresh investigation attachment Id  # noqa: E501

        Retrieve attachment for the given attachmentId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_attachment_for_the_given_fresh_investigation_attachment_id_with_http_info(order_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: fresh investigation orderId (required)
        :param str id: fresh investigation attachment id for the given order (required)
        :return: CreditsafeFreshInvestigationGlobalDataCoreAttachmentBinaryAttachment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["order_id", "id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_attachment_for_the_given_fresh_investigation_attachment_id"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'order_id' is set
        if "order_id" not in params or params["order_id"] is None:
            raise ValueError(
                "Missing the required parameter `order_id` when calling `get_attachment_for_the_given_fresh_investigation_attachment_id`"
            )  # noqa: E501
        # verify the required parameter 'id' is set
        if "id" not in params or params["id"] is None:
            raise ValueError(
                "Missing the required parameter `id` when calling `get_attachment_for_the_given_fresh_investigation_attachment_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "order_id" in params:
            path_params["orderId"] = params["order_id"]  # noqa: E501
        if "id" in params:
            path_params["id"] = params["id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/*", "text/*", "image/*", "application/json"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/freshinvestigations/{orderId}/attachments/{id}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="CreditsafeFreshInvestigationGlobalDataCoreAttachmentBinaryAttachment",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_attachments_for_the_given_fresh_investigation_order_id(
        self, order_id, **kwargs
    ):  # noqa: E501
        """Get attachments for the given fresh investigation orderId  # noqa: E501

        Returns attachments available for that particular order.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_attachments_for_the_given_fresh_investigation_order_id(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: fresh investigation orderId (required)
        :return: FreshInvestigationGetAttachmentsForOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_attachments_for_the_given_fresh_investigation_order_id_with_http_info(
                order_id, **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.get_attachments_for_the_given_fresh_investigation_order_id_with_http_info(
                    order_id, **kwargs
                )
            )  # noqa: E501
            return data

    def get_attachments_for_the_given_fresh_investigation_order_id_with_http_info(
        self, order_id, **kwargs
    ):  # noqa: E501
        """Get attachments for the given fresh investigation orderId  # noqa: E501

        Returns attachments available for that particular order.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_attachments_for_the_given_fresh_investigation_order_id_with_http_info(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: fresh investigation orderId (required)
        :return: FreshInvestigationGetAttachmentsForOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["order_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_attachments_for_the_given_fresh_investigation_order_id"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'order_id' is set
        if "order_id" not in params or params["order_id"] is None:
            raise ValueError(
                "Missing the required parameter `order_id` when calling `get_attachments_for_the_given_fresh_investigation_order_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "order_id" in params:
            path_params["orderId"] = params["order_id"]  # noqa: E501

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
            "/freshinvestigations/{orderId}/attachments",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="FreshInvestigationGetAttachmentsForOrderResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_fresh_investigations(self, **kwargs):  # noqa: E501
        """Get Fresh Investigations  # noqa: E501

        Returns a list of your submitted Fresh Investigation Orders.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fresh_investigations(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Starting page number.
        :param int page_size: Number of items to return per Page.
        :param str transaction_id: Fresh Investigation Identifier used internally and with our data partners.
        :param str report_created_after: Returns Fresh Investigations processed after this date
        :param str report_created_before: Returns ordered Fresh Investigations that were processed before this date
        :param str created_before: Returns Fresh Investigations created before this date
        :param str created_since: Returns ordered Fresh Investigations created after this date
        :param str look_up_order_by: Use to search for your Fresh Investigations by either the returned Company Details in the `GET` `freshInvestigations/{orderId}` endpoint or your supplied Search Criteria in the `POST` `/freshInvestigations` endpoint
        :param str company_details_country: Looks for your returned Fresh Investigations where the returned Company Country is named this. Use with lookUpOrderBy=CompanyDetails
        :param str company_details_name: Looks for your returned Fresh Investigations where the returned Company Name is named this. Use with lookUpOrderBy=CompanyDetails
        :param str search_criteria_country: Looks for your returned Fresh Investigations where your submitted Search Criteria Company Country is this. Use with lookUpOrderBy=searchCriteria
        :param str search_criteria_name: Looks for your Fresh Investigations where your submitted Search Criteria Company Name is this. Use with lookUpOrderBy=searchCriteria
        :param str sort_by: Sorts  returned Fresh Investigations by this field
        :param str sort_dir: The direction that you wish to sort results by.
        :return: ConnectFreshInvListInvestigations
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_fresh_investigations_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_fresh_investigations_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def get_fresh_investigations_with_http_info(self, **kwargs):  # noqa: E501
        """Get Fresh Investigations  # noqa: E501

        Returns a list of your submitted Fresh Investigation Orders.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_fresh_investigations_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Starting page number.
        :param int page_size: Number of items to return per Page.
        :param str transaction_id: Fresh Investigation Identifier used internally and with our data partners.
        :param str report_created_after: Returns Fresh Investigations processed after this date
        :param str report_created_before: Returns ordered Fresh Investigations that were processed before this date
        :param str created_before: Returns Fresh Investigations created before this date
        :param str created_since: Returns ordered Fresh Investigations created after this date
        :param str look_up_order_by: Use to search for your Fresh Investigations by either the returned Company Details in the `GET` `freshInvestigations/{orderId}` endpoint or your supplied Search Criteria in the `POST` `/freshInvestigations` endpoint
        :param str company_details_country: Looks for your returned Fresh Investigations where the returned Company Country is named this. Use with lookUpOrderBy=CompanyDetails
        :param str company_details_name: Looks for your returned Fresh Investigations where the returned Company Name is named this. Use with lookUpOrderBy=CompanyDetails
        :param str search_criteria_country: Looks for your returned Fresh Investigations where your submitted Search Criteria Company Country is this. Use with lookUpOrderBy=searchCriteria
        :param str search_criteria_name: Looks for your Fresh Investigations where your submitted Search Criteria Company Name is this. Use with lookUpOrderBy=searchCriteria
        :param str sort_by: Sorts  returned Fresh Investigations by this field
        :param str sort_dir: The direction that you wish to sort results by.
        :return: ConnectFreshInvListInvestigations
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "page",
            "page_size",
            "transaction_id",
            "report_created_after",
            "report_created_before",
            "created_before",
            "created_since",
            "look_up_order_by",
            "company_details_country",
            "company_details_name",
            "search_criteria_country",
            "search_criteria_name",
            "sort_by",
            "sort_dir",
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
                    " to method get_fresh_investigations" % key
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
        if "transaction_id" in params:
            query_params.append(
                ("transactionId", params["transaction_id"])
            )  # noqa: E501
        if "report_created_after" in params:
            query_params.append(
                ("reportCreatedAfter", params["report_created_after"])
            )  # noqa: E501
        if "report_created_before" in params:
            query_params.append(
                ("reportCreatedBefore", params["report_created_before"])
            )  # noqa: E501
        if "created_before" in params:
            query_params.append(
                ("createdBefore", params["created_before"])
            )  # noqa: E501
        if "created_since" in params:
            query_params.append(("createdSince", params["created_since"]))  # noqa: E501
        if "look_up_order_by" in params:
            query_params.append(
                ("lookUpOrderBy", params["look_up_order_by"])
            )  # noqa: E501
        if "company_details_country" in params:
            query_params.append(
                ("companyDetailsCountry", params["company_details_country"])
            )  # noqa: E501
        if "company_details_name" in params:
            query_params.append(
                ("companyDetailsName", params["company_details_name"])
            )  # noqa: E501
        if "search_criteria_country" in params:
            query_params.append(
                ("searchCriteriaCountry", params["search_criteria_country"])
            )  # noqa: E501
        if "search_criteria_name" in params:
            query_params.append(
                ("searchCriteriaName", params["search_criteria_name"])
            )  # noqa: E501
        if "sort_by" in params:
            query_params.append(("sortBy", params["sort_by"]))  # noqa: E501
        if "sort_dir" in params:
            query_params.append(("sortDir", params["sort_dir"]))  # noqa: E501

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
            "/freshinvestigations",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectFreshInvListInvestigations",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def retrieve_comments_of_specified_fresh_investigation_report(
        self, order_id, **kwargs
    ):  # noqa: E501
        """Retrieve comments of specified FreshInvestigation Report  # noqa: E501

        Returns the Fresh Investigation Report comments for a specific order.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_comments_of_specified_fresh_investigation_report(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: FreshInvestigation Report Id (required)
        :return: GetFreshInvestigationCommentsByOrderIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.retrieve_comments_of_specified_fresh_investigation_report_with_http_info(
                order_id, **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.retrieve_comments_of_specified_fresh_investigation_report_with_http_info(
                    order_id, **kwargs
                )
            )  # noqa: E501
            return data

    def retrieve_comments_of_specified_fresh_investigation_report_with_http_info(
        self, order_id, **kwargs
    ):  # noqa: E501
        """Retrieve comments of specified FreshInvestigation Report  # noqa: E501

        Returns the Fresh Investigation Report comments for a specific order.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_comments_of_specified_fresh_investigation_report_with_http_info(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: FreshInvestigation Report Id (required)
        :return: GetFreshInvestigationCommentsByOrderIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["order_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_comments_of_specified_fresh_investigation_report"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'order_id' is set
        if "order_id" not in params or params["order_id"] is None:
            raise ValueError(
                "Missing the required parameter `order_id` when calling `retrieve_comments_of_specified_fresh_investigation_report`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "order_id" in params:
            path_params["orderId"] = params["order_id"]  # noqa: E501

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
            "/freshinvestigations/{orderId}/comments",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="GetFreshInvestigationCommentsByOrderIdResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def retrieve_fresh_investigation_order(self, order_id, **kwargs):  # noqa: E501
        """Retrieve FreshInvestigation Order  # noqa: E501

        Returns a specific Fresh Investigation order.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_fresh_investigation_order(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: (required)
        :param str sections: Specify a value to return a single section, or multiple-comma separated sections of the completed Fresh Investigation. Leave null to return all sections. Available sections; - `companyIdentification` - `creditScore` - `contactInformation` - `directors` - `otherInformation` - `groupStructure` - `extendedGroupStructure` - `financialStatements` - `negativeInformation` - `additionalInformation`- `directorships` - `localFinancialStatements` - `paymentData` - `companySummary` - `alternateSummary`
        :param str comments: Selects number of comments which should be returned with the order details.
        :return: ConnectFreshInvCompletedInvestigation
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.retrieve_fresh_investigation_order_with_http_info(
                order_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.retrieve_fresh_investigation_order_with_http_info(
                order_id, **kwargs
            )  # noqa: E501
            return data

    def retrieve_fresh_investigation_order_with_http_info(
        self, order_id, **kwargs
    ):  # noqa: E501
        """Retrieve FreshInvestigation Order  # noqa: E501

        Returns a specific Fresh Investigation order.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_fresh_investigation_order_with_http_info(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: (required)
        :param str sections: Specify a value to return a single section, or multiple-comma separated sections of the completed Fresh Investigation. Leave null to return all sections. Available sections; - `companyIdentification` - `creditScore` - `contactInformation` - `directors` - `otherInformation` - `groupStructure` - `extendedGroupStructure` - `financialStatements` - `negativeInformation` - `additionalInformation`- `directorships` - `localFinancialStatements` - `paymentData` - `companySummary` - `alternateSummary`
        :param str comments: Selects number of comments which should be returned with the order details.
        :return: ConnectFreshInvCompletedInvestigation
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["order_id", "sections", "comments"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_fresh_investigation_order" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'order_id' is set
        if "order_id" not in params or params["order_id"] is None:
            raise ValueError(
                "Missing the required parameter `order_id` when calling `retrieve_fresh_investigation_order`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "order_id" in params:
            path_params["orderId"] = params["order_id"]  # noqa: E501

        query_params = []
        if "sections" in params:
            query_params.append(("sections", params["sections"]))  # noqa: E501
        if "comments" in params:
            query_params.append(("comments", params["comments"]))  # noqa: E501

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
            "/freshinvestigations/{orderId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectFreshInvCompletedInvestigation",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def retrieve_fresh_investigation_report_content(
        self, order_id, **kwargs
    ):  # noqa: E501
        """Retrieve FreshInvestigation Report Content  # noqa: E501

        Returns the Fresh Investigation Report data for a specific order, after the order has a status of delivered.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_fresh_investigation_report_content(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: (required)
        :return: CreditsafeGlobalDataReportsCompanyReportResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.retrieve_fresh_investigation_report_content_with_http_info(
                order_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.retrieve_fresh_investigation_report_content_with_http_info(
                order_id, **kwargs
            )  # noqa: E501
            return data

    def retrieve_fresh_investigation_report_content_with_http_info(
        self, order_id, **kwargs
    ):  # noqa: E501
        """Retrieve FreshInvestigation Report Content  # noqa: E501

        Returns the Fresh Investigation Report data for a specific order, after the order has a status of delivered.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.retrieve_fresh_investigation_report_content_with_http_info(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: (required)
        :return: CreditsafeGlobalDataReportsCompanyReportResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["order_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method retrieve_fresh_investigation_report_content" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'order_id' is set
        if "order_id" not in params or params["order_id"] is None:
            raise ValueError(
                "Missing the required parameter `order_id` when calling `retrieve_fresh_investigation_report_content`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "order_id" in params:
            path_params["orderId"] = params["order_id"]  # noqa: E501

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
            "/freshinvestigations/{orderId}/report",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="CreditsafeGlobalDataReportsCompanyReportResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update_fresh_investigation_report_content(
        self, order_id, **kwargs
    ):  # noqa: E501
        """Update FreshInvestigation Report Content  # noqa: E501

        Update the Fresh Investigation Report data for a specific order, after the order has a status of delivered.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_fresh_investigation_report_content(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: Fresh investigation orderId (required)
        :param ConnectUpdateFreshInvestigation body:
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.update_fresh_investigation_report_content_with_http_info(
                order_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.update_fresh_investigation_report_content_with_http_info(
                order_id, **kwargs
            )  # noqa: E501
            return data

    def update_fresh_investigation_report_content_with_http_info(
        self, order_id, **kwargs
    ):  # noqa: E501
        """Update FreshInvestigation Report Content  # noqa: E501

        Update the Fresh Investigation Report data for a specific order, after the order has a status of delivered.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_fresh_investigation_report_content_with_http_info(order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str order_id: Fresh investigation orderId (required)
        :param ConnectUpdateFreshInvestigation body:
        :return: InlineResponse2003
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["order_id", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_fresh_investigation_report_content" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'order_id' is set
        if "order_id" not in params or params["order_id"] is None:
            raise ValueError(
                "Missing the required parameter `order_id` when calling `update_fresh_investigation_report_content`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "order_id" in params:
            path_params["orderId"] = params["order_id"]  # noqa: E501

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
            "/freshinvestigations/{orderId}",
            "PATCH",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse2003",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def upload_attachments_for_fresh_investigation_order_id(
        self, import_file, description, order_id, **kwargs
    ):  # noqa: E501
        """Upload attachments for fresh investigation orderId  # noqa: E501

        Returns the status of attachment upload for the particular order.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_attachments_for_fresh_investigation_order_id(import_file, description, order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str import_file: (required)
        :param str description: (required)
        :param str order_id: Fresh investigation orderId (required)
        :return: FreshInvestigationAttachmentUploadForOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return (
                self.upload_attachments_for_fresh_investigation_order_id_with_http_info(
                    import_file, description, order_id, **kwargs
                )
            )  # noqa: E501
        else:
            (data) = (
                self.upload_attachments_for_fresh_investigation_order_id_with_http_info(
                    import_file, description, order_id, **kwargs
                )
            )  # noqa: E501
            return data

    def upload_attachments_for_fresh_investigation_order_id_with_http_info(
        self, import_file, description, order_id, **kwargs
    ):  # noqa: E501
        """Upload attachments for fresh investigation orderId  # noqa: E501

        Returns the status of attachment upload for the particular order.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upload_attachments_for_fresh_investigation_order_id_with_http_info(import_file, description, order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str import_file: (required)
        :param str description: (required)
        :param str order_id: Fresh investigation orderId (required)
        :return: FreshInvestigationAttachmentUploadForOrderResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["import_file", "description", "order_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_attachments_for_fresh_investigation_order_id"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'import_file' is set
        if "import_file" not in params or params["import_file"] is None:
            raise ValueError(
                "Missing the required parameter `import_file` when calling `upload_attachments_for_fresh_investigation_order_id`"
            )  # noqa: E501
        # verify the required parameter 'description' is set
        if "description" not in params or params["description"] is None:
            raise ValueError(
                "Missing the required parameter `description` when calling `upload_attachments_for_fresh_investigation_order_id`"
            )  # noqa: E501
        # verify the required parameter 'order_id' is set
        if "order_id" not in params or params["order_id"] is None:
            raise ValueError(
                "Missing the required parameter `order_id` when calling `upload_attachments_for_fresh_investigation_order_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "order_id" in params:
            path_params["orderId"] = params["order_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "import_file" in params:
            local_var_files["importFile"] = params["import_file"]  # noqa: E501
        if "description" in params:
            form_params.append(("description", params["description"]))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = (
            self.api_client.select_header_content_type(  # noqa: E501
                ["multipart/form-data"]
            )
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/freshinvestigations/{orderId}/attachments",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="FreshInvestigationAttachmentUploadForOrderResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

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


class KYCProfileUpdatesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def k_yc_protect_add_an_attachment_to_the_given_profile(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Add An Attachment To The Given Profile  # noqa: E501

        Adds an attachment to a profile. Returns the details of the added attachment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_protect_add_an_attachment_to_the_given_profile(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param str file:
        :param str document_type:
        :param str description:
        :return: KycProtectProfileAttachmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return (
                self.k_yc_protect_add_an_attachment_to_the_given_profile_with_http_info(
                    profile_id, **kwargs
                )
            )  # noqa: E501
        else:
            (data) = (
                self.k_yc_protect_add_an_attachment_to_the_given_profile_with_http_info(
                    profile_id, **kwargs
                )
            )  # noqa: E501
            return data

    def k_yc_protect_add_an_attachment_to_the_given_profile_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Add An Attachment To The Given Profile  # noqa: E501

        Adds an attachment to a profile. Returns the details of the added attachment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_protect_add_an_attachment_to_the_given_profile_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param str file:
        :param str document_type:
        :param str description:
        :return: KycProtectProfileAttachmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "profile_id",
            "file",
            "document_type",
            "description",
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
                    " to method k_yc_protect_add_an_attachment_to_the_given_profile"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `k_yc_protect_add_an_attachment_to_the_given_profile`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "file" in params:
            local_var_files["File"] = params["file"]  # noqa: E501
        if "document_type" in params:
            form_params.append(("DocumentType", params["document_type"]))  # noqa: E501
        if "description" in params:
            form_params.append(("Description", params["description"]))  # noqa: E501

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
            "/compliance/kyc-protect/profiles/{profileId}/attachments",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="KycProtectProfileAttachmentResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def k_yc_protect_get_list_of_attachments_on_the_given_profile(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Return List Of Attachments On The Given Profile  # noqa: E501

        Gets a list of attachments on the given profile ordered by modified date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_protect_get_list_of_attachments_on_the_given_profile(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param int page: The page number to fetch. Should be a positive integer.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :return: InlineResponse20011
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.k_yc_protect_get_list_of_attachments_on_the_given_profile_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.k_yc_protect_get_list_of_attachments_on_the_given_profile_with_http_info(
                    profile_id, **kwargs
                )
            )  # noqa: E501
            return data

    def k_yc_protect_get_list_of_attachments_on_the_given_profile_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Return List Of Attachments On The Given Profile  # noqa: E501

        Gets a list of attachments on the given profile ordered by modified date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_protect_get_list_of_attachments_on_the_given_profile_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param int page: The page number to fetch. Should be a positive integer.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :return: InlineResponse20011
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "page", "page_size"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k_yc_protect_get_list_of_attachments_on_the_given_profile"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `k_yc_protect_get_list_of_attachments_on_the_given_profile`"
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
            "/compliance/kyc-protect/profiles/{profileId}/attachments",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse20011",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def protect_delete_kyc_profile_attachment_by_profile_id_and_attachment_id(
        self, profile_id, attachment_id, **kwargs
    ):  # noqa: E501
        """Delete Attachment By Profile And Attachment Id  # noqa: E501

        Deletes A Profile Attachment By Profile And Attachment Id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_delete_kyc_profile_attachment_by_profile_id_and_attachment_id(profile_id, attachment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :param str attachment_id: Id of a attachmentId. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.protect_delete_kyc_profile_attachment_by_profile_id_and_attachment_id_with_http_info(
                profile_id, attachment_id, **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.protect_delete_kyc_profile_attachment_by_profile_id_and_attachment_id_with_http_info(
                    profile_id, attachment_id, **kwargs
                )
            )  # noqa: E501
            return data

    def protect_delete_kyc_profile_attachment_by_profile_id_and_attachment_id_with_http_info(
        self, profile_id, attachment_id, **kwargs
    ):  # noqa: E501
        """Delete Attachment By Profile And Attachment Id  # noqa: E501

        Deletes A Profile Attachment By Profile And Attachment Id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_delete_kyc_profile_attachment_by_profile_id_and_attachment_id_with_http_info(profile_id, attachment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :param str attachment_id: Id of a attachmentId. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "attachment_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method protect_delete_kyc_profile_attachment_by_profile_id_and_attachment_id"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `protect_delete_kyc_profile_attachment_by_profile_id_and_attachment_id`"
            )  # noqa: E501
        # verify the required parameter 'attachment_id' is set
        if "attachment_id" not in params or params["attachment_id"] is None:
            raise ValueError(
                "Missing the required parameter `attachment_id` when calling `protect_delete_kyc_profile_attachment_by_profile_id_and_attachment_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501
        if "attachment_id" in params:
            path_params["attachmentId"] = params["attachment_id"]  # noqa: E501

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
            "/compliance/kyc-protect/profiles/{profileId}/attachments/{attachmentId}",
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

    def protect_deletekyc_profile_id_by_note_id(
        self, profile_id, note_id, **kwargs
    ):  # noqa: E501
        """Deletes Profile Note By Note Id  # noqa: E501

        Deletes a profile note based on profile id and note id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_deletekyc_profile_id_by_note_id(profile_id, note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :param str note_id: Id of a note. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.protect_deletekyc_profile_id_by_note_id_with_http_info(
                profile_id, note_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.protect_deletekyc_profile_id_by_note_id_with_http_info(
                profile_id, note_id, **kwargs
            )  # noqa: E501
            return data

    def protect_deletekyc_profile_id_by_note_id_with_http_info(
        self, profile_id, note_id, **kwargs
    ):  # noqa: E501
        """Deletes Profile Note By Note Id  # noqa: E501

        Deletes a profile note based on profile id and note id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_deletekyc_profile_id_by_note_id_with_http_info(profile_id, note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :param str note_id: Id of a note. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "note_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method protect_deletekyc_profile_id_by_note_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `protect_deletekyc_profile_id_by_note_id`"
            )  # noqa: E501
        # verify the required parameter 'note_id' is set
        if "note_id" not in params or params["note_id"] is None:
            raise ValueError(
                "Missing the required parameter `note_id` when calling `protect_deletekyc_profile_id_by_note_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501
        if "note_id" in params:
            path_params["noteId"] = params["note_id"]  # noqa: E501

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
            "/compliance/kyc-protect/profiles/{profileId}/notes/{noteId}",
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

    def protect_download_kyc_profile_attachment_by_profile_id_and_attachment_id(
        self, profile_id, attachment_id, **kwargs
    ):  # noqa: E501
        """Download Profile Attachment By Profile And Attachment Id  # noqa: E501

        Gets profile attachment's download link.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_download_kyc_profile_attachment_by_profile_id_and_attachment_id(profile_id, attachment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :param str attachment_id: Id of a note. (required)
        :return: DownloadAttachmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.protect_download_kyc_profile_attachment_by_profile_id_and_attachment_id_with_http_info(
                profile_id, attachment_id, **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.protect_download_kyc_profile_attachment_by_profile_id_and_attachment_id_with_http_info(
                    profile_id, attachment_id, **kwargs
                )
            )  # noqa: E501
            return data

    def protect_download_kyc_profile_attachment_by_profile_id_and_attachment_id_with_http_info(
        self, profile_id, attachment_id, **kwargs
    ):  # noqa: E501
        """Download Profile Attachment By Profile And Attachment Id  # noqa: E501

        Gets profile attachment's download link.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_download_kyc_profile_attachment_by_profile_id_and_attachment_id_with_http_info(profile_id, attachment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :param str attachment_id: Id of a note. (required)
        :return: DownloadAttachmentResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "attachment_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method protect_download_kyc_profile_attachment_by_profile_id_and_attachment_id"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `protect_download_kyc_profile_attachment_by_profile_id_and_attachment_id`"
            )  # noqa: E501
        # verify the required parameter 'attachment_id' is set
        if "attachment_id" not in params or params["attachment_id"] is None:
            raise ValueError(
                "Missing the required parameter `attachment_id` when calling `protect_download_kyc_profile_attachment_by_profile_id_and_attachment_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501
        if "attachment_id" in params:
            path_params["attachmentId"] = params["attachment_id"]  # noqa: E501

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
            "/compliance/kyc-protect/profiles/{profileId}/attachments/{attachmentId}/download",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="DownloadAttachmentResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def protect_getkyc_profile_attachment_by_profile_id_and_attachment_id(
        self, profile_id, attachment_id, **kwargs
    ):  # noqa: E501
        """Return A Profile Attachment By Profile And Attachment Id  # noqa: E501

        Returns an attachment by the provided attachment Id and profile Id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_getkyc_profile_attachment_by_profile_id_and_attachment_id(profile_id, attachment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :param str attachment_id: Id of an attachment. (required)
        :return: GetKYCProfileAttachmentDetailsByAttachmentId
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.protect_getkyc_profile_attachment_by_profile_id_and_attachment_id_with_http_info(
                profile_id, attachment_id, **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.protect_getkyc_profile_attachment_by_profile_id_and_attachment_id_with_http_info(
                    profile_id, attachment_id, **kwargs
                )
            )  # noqa: E501
            return data

    def protect_getkyc_profile_attachment_by_profile_id_and_attachment_id_with_http_info(
        self, profile_id, attachment_id, **kwargs
    ):  # noqa: E501
        """Return A Profile Attachment By Profile And Attachment Id  # noqa: E501

        Returns an attachment by the provided attachment Id and profile Id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_getkyc_profile_attachment_by_profile_id_and_attachment_id_with_http_info(profile_id, attachment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :param str attachment_id: Id of an attachment. (required)
        :return: GetKYCProfileAttachmentDetailsByAttachmentId
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "attachment_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method protect_getkyc_profile_attachment_by_profile_id_and_attachment_id"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `protect_getkyc_profile_attachment_by_profile_id_and_attachment_id`"
            )  # noqa: E501
        # verify the required parameter 'attachment_id' is set
        if "attachment_id" not in params or params["attachment_id"] is None:
            raise ValueError(
                "Missing the required parameter `attachment_id` when calling `protect_getkyc_profile_attachment_by_profile_id_and_attachment_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501
        if "attachment_id" in params:
            path_params["attachmentId"] = params["attachment_id"]  # noqa: E501

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
            "/compliance/kyc-protect/profiles/{profileId}/attachments/{attachmentId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="GetKYCProfileAttachmentDetailsByAttachmentId",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def protect_getkyc_profile_notes(self, profile_id, **kwargs):  # noqa: E501
        """Return Profile Notes  # noqa: E501

        Returns a list of profile notes for the given profile id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_getkyc_profile_notes(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :param str search_term: Filters the note list by notes with body containing the provided string
        :param bool is_archived: Get archived notes based on this flag. Allowed values are true, false or null
        :return: GetKYCProtectProfileIdNotesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.protect_getkyc_profile_notes_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.protect_getkyc_profile_notes_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
            return data

    def protect_getkyc_profile_notes_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Return Profile Notes  # noqa: E501

        Returns a list of profile notes for the given profile id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_getkyc_profile_notes_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :param str search_term: Filters the note list by notes with body containing the provided string
        :param bool is_archived: Get archived notes based on this flag. Allowed values are true, false or null
        :return: GetKYCProtectProfileIdNotesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "profile_id",
            "page",
            "page_size",
            "search_term",
            "is_archived",
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
                    " to method protect_getkyc_profile_notes" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `protect_getkyc_profile_notes`"
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
        if "search_term" in params:
            query_params.append(("searchTerm", params["search_term"]))  # noqa: E501
        if "is_archived" in params:
            query_params.append(("isArchived", params["is_archived"]))  # noqa: E501

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
            "/compliance/kyc-protect/profiles/{profileId}/notes",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="GetKYCProtectProfileIdNotesResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def protect_getkyc_profile_notes_by_note_id(
        self, profile_id, note_id, **kwargs
    ):  # noqa: E501
        """Return Profile Notes By Note Id  # noqa: E501

        Returns a profile note based on profile id and note id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_getkyc_profile_notes_by_note_id(profile_id, note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :param str note_id: Id of a note. (required)
        :return: GetKYCProtectProfileIdNoteIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.protect_getkyc_profile_notes_by_note_id_with_http_info(
                profile_id, note_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.protect_getkyc_profile_notes_by_note_id_with_http_info(
                profile_id, note_id, **kwargs
            )  # noqa: E501
            return data

    def protect_getkyc_profile_notes_by_note_id_with_http_info(
        self, profile_id, note_id, **kwargs
    ):  # noqa: E501
        """Return Profile Notes By Note Id  # noqa: E501

        Returns a profile note based on profile id and note id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_getkyc_profile_notes_by_note_id_with_http_info(profile_id, note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :param str note_id: Id of a note. (required)
        :return: GetKYCProtectProfileIdNoteIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "note_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method protect_getkyc_profile_notes_by_note_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `protect_getkyc_profile_notes_by_note_id`"
            )  # noqa: E501
        # verify the required parameter 'note_id' is set
        if "note_id" not in params or params["note_id"] is None:
            raise ValueError(
                "Missing the required parameter `note_id` when calling `protect_getkyc_profile_notes_by_note_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501
        if "note_id" in params:
            path_params["noteId"] = params["note_id"]  # noqa: E501

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
            "/compliance/kyc-protect/profiles/{profileId}/notes/{noteId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="GetKYCProtectProfileIdNoteIdResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def protect_postkyc_profile_notes(self, profile_id, **kwargs):  # noqa: E501
        """Create Profile Note  # noqa: E501

        Adds a note to a profile then Returns the details of the added note.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_postkyc_profile_notes(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :param PostKYCProfileNotesRequest body:
        :return: PostKYCProfileNotes
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.protect_postkyc_profile_notes_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.protect_postkyc_profile_notes_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
            return data

    def protect_postkyc_profile_notes_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Create Profile Note  # noqa: E501

        Adds a note to a profile then Returns the details of the added note.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_postkyc_profile_notes_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :param PostKYCProfileNotesRequest body:
        :return: PostKYCProfileNotes
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
                    " to method protect_postkyc_profile_notes" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `protect_postkyc_profile_notes`"
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
            "/compliance/kyc-protect/profiles/{profileId}/notes",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="PostKYCProfileNotes",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def protect_put_kyc_profile_attachment_by_profile_id_and_attachment_id(
        self, profile_id, attachment_id, **kwargs
    ):  # noqa: E501
        """Update Profile Attachment By Profile And Attachment Id  # noqa: E501

        Updates A Profile Attachment By Profile And Attachment Id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_put_kyc_profile_attachment_by_profile_id_and_attachment_id(profile_id, attachment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :param str attachment_id: Id of a attachmentId. (required)
        :param str document_type:
        :param str description:
        :return: UpdateKYCAttachmentsByAttachmentId
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.protect_put_kyc_profile_attachment_by_profile_id_and_attachment_id_with_http_info(
                profile_id, attachment_id, **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.protect_put_kyc_profile_attachment_by_profile_id_and_attachment_id_with_http_info(
                    profile_id, attachment_id, **kwargs
                )
            )  # noqa: E501
            return data

    def protect_put_kyc_profile_attachment_by_profile_id_and_attachment_id_with_http_info(
        self, profile_id, attachment_id, **kwargs
    ):  # noqa: E501
        """Update Profile Attachment By Profile And Attachment Id  # noqa: E501

        Updates A Profile Attachment By Profile And Attachment Id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_put_kyc_profile_attachment_by_profile_id_and_attachment_id_with_http_info(profile_id, attachment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :param str attachment_id: Id of a attachmentId. (required)
        :param str document_type:
        :param str description:
        :return: UpdateKYCAttachmentsByAttachmentId
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "profile_id",
            "attachment_id",
            "document_type",
            "description",
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
                    " to method protect_put_kyc_profile_attachment_by_profile_id_and_attachment_id"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `protect_put_kyc_profile_attachment_by_profile_id_and_attachment_id`"
            )  # noqa: E501
        # verify the required parameter 'attachment_id' is set
        if "attachment_id" not in params or params["attachment_id"] is None:
            raise ValueError(
                "Missing the required parameter `attachment_id` when calling `protect_put_kyc_profile_attachment_by_profile_id_and_attachment_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501
        if "attachment_id" in params:
            path_params["attachmentId"] = params["attachment_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if "document_type" in params:
            form_params.append(("documentType", params["document_type"]))  # noqa: E501
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
            "/compliance/kyc-protect/profiles/{profileId}/attachments/{attachmentId}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="UpdateKYCAttachmentsByAttachmentId",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def protect_update_kyc_profile_notes_by_note_id(
        self, profile_id, note_id, **kwargs
    ):  # noqa: E501
        """Update Profile Note By Note Id  # noqa: E501

        Updates a profile note based on profile id and note id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_update_kyc_profile_notes_by_note_id(profile_id, note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :param str note_id: Id of a note. (required)
        :param PutKYCProfileNotesByNoteIdRequest body:
        :return: PutKYCProfileNotesByNoteId
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.protect_update_kyc_profile_notes_by_note_id_with_http_info(
                profile_id, note_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.protect_update_kyc_profile_notes_by_note_id_with_http_info(
                profile_id, note_id, **kwargs
            )  # noqa: E501
            return data

    def protect_update_kyc_profile_notes_by_note_id_with_http_info(
        self, profile_id, note_id, **kwargs
    ):  # noqa: E501
        """Update Profile Note By Note Id  # noqa: E501

        Updates a profile note based on profile id and note id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_update_kyc_profile_notes_by_note_id_with_http_info(profile_id, note_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :param str note_id: Id of a note. (required)
        :param PutKYCProfileNotesByNoteIdRequest body:
        :return: PutKYCProfileNotesByNoteId
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "note_id", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method protect_update_kyc_profile_notes_by_note_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `protect_update_kyc_profile_notes_by_note_id`"
            )  # noqa: E501
        # verify the required parameter 'note_id' is set
        if "note_id" not in params or params["note_id"] is None:
            raise ValueError(
                "Missing the required parameter `note_id` when calling `protect_update_kyc_profile_notes_by_note_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501
        if "note_id" in params:
            path_params["noteId"] = params["note_id"]  # noqa: E501

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
            "/compliance/kyc-protect/profiles/{profileId}/notes/{noteId}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="PutKYCProfileNotesByNoteId",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def protect_updates_kyc_profile_by_id(self, profile_id, **kwargs):  # noqa: E501
        """Update Profile By Profile Id  # noqa: E501

        Updates a single profile by profile Id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_updates_kyc_profile_by_id(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :param UpdateKYCProfileByProfileIdRequest body:
        :return: UpdateKYCProfileByProfileId
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.protect_updates_kyc_profile_by_id_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.protect_updates_kyc_profile_by_id_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
            return data

    def protect_updates_kyc_profile_by_id_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Update Profile By Profile Id  # noqa: E501

        Updates a single profile by profile Id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.protect_updates_kyc_profile_by_id_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of a profile. (required)
        :param UpdateKYCProfileByProfileIdRequest body:
        :return: UpdateKYCProfileByProfileId
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
                    " to method protect_updates_kyc_profile_by_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `protect_updates_kyc_profile_by_id`"
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
            "/compliance/kyc-protect/profiles/{profileId}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="UpdateKYCProfileByProfileId",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

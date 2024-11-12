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


class KYCAMLScreeningProfileManagementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_kyc_profile_searches_by_profile_id(
        self, body, profile_id, **kwargs
    ):  # noqa: E501
        """Deletes AML searches linked to a profile  # noqa: E501

        Deletes AML searches from a profile by profile Id and Search Id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_kyc_profile_searches_by_profile_id(body, profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeleteKYCProfileSearchesByProfileIdRequestBody body: (required)
        :param str profile_id: Id of a profile. (required)
        :return: DeleteKYCProfileSearchesByProfileIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_kyc_profile_searches_by_profile_id_with_http_info(
                body, profile_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.delete_kyc_profile_searches_by_profile_id_with_http_info(
                body, profile_id, **kwargs
            )  # noqa: E501
            return data

    def delete_kyc_profile_searches_by_profile_id_with_http_info(
        self, body, profile_id, **kwargs
    ):  # noqa: E501
        """Deletes AML searches linked to a profile  # noqa: E501

        Deletes AML searches from a profile by profile Id and Search Id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_kyc_profile_searches_by_profile_id_with_http_info(body, profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeleteKYCProfileSearchesByProfileIdRequestBody body: (required)
        :param str profile_id: Id of a profile. (required)
        :return: DeleteKYCProfileSearchesByProfileIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body", "profile_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_kyc_profile_searches_by_profile_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `delete_kyc_profile_searches_by_profile_id`"
            )  # noqa: E501
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `delete_kyc_profile_searches_by_profile_id`"
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
            "/compliance/kyc-protect/profiles/{profileId}/searches/link",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="DeleteKYCProfileSearchesByProfileIdResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def getkychitsofthesearcheslinkedtoprofile(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Return All Hits Of Searches Linked To A Profile  # noqa: E501

        Return hits of the searches linked to a profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getkychitsofthesearcheslinkedtoprofile(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of the profile (required)
        :param list[str] hit_decisions: The hit decisions. It can be the collection of undecided, truematch, falsepositive, discarded
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :return: GetProfileHitsByProfileIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.getkychitsofthesearcheslinkedtoprofile_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.getkychitsofthesearcheslinkedtoprofile_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
            return data

    def getkychitsofthesearcheslinkedtoprofile_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Return All Hits Of Searches Linked To A Profile  # noqa: E501

        Return hits of the searches linked to a profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getkychitsofthesearcheslinkedtoprofile_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: Id of the profile (required)
        :param list[str] hit_decisions: The hit decisions. It can be the collection of undecided, truematch, falsepositive, discarded
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :return: GetProfileHitsByProfileIdResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "hit_decisions", "page", "page_size"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getkychitsofthesearcheslinkedtoprofile" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `getkychitsofthesearcheslinkedtoprofile`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501

        query_params = []
        if "hit_decisions" in params:
            query_params.append(("hitDecisions", params["hit_decisions"]))  # noqa: E501
            collection_formats["hitDecisions"] = "multi"  # noqa: E501
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
            "/compliance/kyc-protect/profiles/{profileId}/hits",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="GetProfileHitsByProfileIdResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def k_yc_protect_adds_a_search_to_the_given_profile(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Adds AML Searches To The Given Profile  # noqa: E501

        Adds a list of searches to a profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_protect_adds_a_search_to_the_given_profile(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param SearchesLinkBody1 body:
        :return: InlineResponse20012
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.k_yc_protect_adds_a_search_to_the_given_profile_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.k_yc_protect_adds_a_search_to_the_given_profile_with_http_info(
                    profile_id, **kwargs
                )
            )  # noqa: E501
            return data

    def k_yc_protect_adds_a_search_to_the_given_profile_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Adds AML Searches To The Given Profile  # noqa: E501

        Adds a list of searches to a profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_protect_adds_a_search_to_the_given_profile_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param SearchesLinkBody1 body:
        :return: InlineResponse20012
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
                    " to method k_yc_protect_adds_a_search_to_the_given_profile" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `k_yc_protect_adds_a_search_to_the_given_profile`"
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
            "/compliance/kyc-protect/profiles/{profileId}/searches/link",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse20012",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def k_yc_protect_get_aml_alerts_by_profile_id(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Return All Hits Linked To The Profile  # noqa: E501

        Returns hits of all searches linked to the profile and key parties.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_protect_get_aml_alerts_by_profile_id(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :param list[str] hit_decisions: The hit decisions to filter by. It can be the collection of undecided, truematch, falsepositive, discarded
        :return: InlineResponse20015
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.k_yc_protect_get_aml_alerts_by_profile_id_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.k_yc_protect_get_aml_alerts_by_profile_id_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
            return data

    def k_yc_protect_get_aml_alerts_by_profile_id_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Return All Hits Linked To The Profile  # noqa: E501

        Returns hits of all searches linked to the profile and key parties.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_protect_get_aml_alerts_by_profile_id_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :param list[str] hit_decisions: The hit decisions to filter by. It can be the collection of undecided, truematch, falsepositive, discarded
        :return: InlineResponse20015
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "page", "page_size", "hit_decisions"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k_yc_protect_get_aml_alerts_by_profile_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `k_yc_protect_get_aml_alerts_by_profile_id`"
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
        if "hit_decisions" in params:
            query_params.append(("hitDecisions", params["hit_decisions"]))  # noqa: E501
            collection_formats["hitDecisions"] = "multi"  # noqa: E501

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
            "/compliance/kyc-protect/profiles/{profileId}/amlAlerts",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse20015",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def k_yc_protect_get_profile_schedules(self, profile_id, **kwargs):  # noqa: E501
        """Return All Schedules By ProfileId And Modified Date  # noqa: E501

        Returns all schedules based on profileId ordered by modified date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_protect_get_profile_schedules(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :return: KYCProfileScheduleResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.k_yc_protect_get_profile_schedules_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.k_yc_protect_get_profile_schedules_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
            return data

    def k_yc_protect_get_profile_schedules_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Return All Schedules By ProfileId And Modified Date  # noqa: E501

        Returns all schedules based on profileId ordered by modified date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_protect_get_profile_schedules_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :return: KYCProfileScheduleResponse
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
                    " to method k_yc_protect_get_profile_schedules" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `k_yc_protect_get_profile_schedules`"
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
            "/compliance/kyc-protect/profiles/{profileId}/schedules",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="KYCProfileScheduleResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def k_yc_protect_get_profile_schedules_by_schedule_id(
        self, profile_id, schedule_id, **kwargs
    ):  # noqa: E501
        """Return Schedule By ProfileId And ScheduleId  # noqa: E501

        Returns a schedule by profileId and scheduleId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_protect_get_profile_schedules_by_schedule_id(profile_id, schedule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param str schedule_id: id of the schedule (required)
        :return: InlineResponse20014
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return (
                self.k_yc_protect_get_profile_schedules_by_schedule_id_with_http_info(
                    profile_id, schedule_id, **kwargs
                )
            )  # noqa: E501
        else:
            (data) = (
                self.k_yc_protect_get_profile_schedules_by_schedule_id_with_http_info(
                    profile_id, schedule_id, **kwargs
                )
            )  # noqa: E501
            return data

    def k_yc_protect_get_profile_schedules_by_schedule_id_with_http_info(
        self, profile_id, schedule_id, **kwargs
    ):  # noqa: E501
        """Return Schedule By ProfileId And ScheduleId  # noqa: E501

        Returns a schedule by profileId and scheduleId.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_protect_get_profile_schedules_by_schedule_id_with_http_info(profile_id, schedule_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param str schedule_id: id of the schedule (required)
        :return: InlineResponse20014
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "schedule_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k_yc_protect_get_profile_schedules_by_schedule_id" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `k_yc_protect_get_profile_schedules_by_schedule_id`"
            )  # noqa: E501
        # verify the required parameter 'schedule_id' is set
        if "schedule_id" not in params or params["schedule_id"] is None:
            raise ValueError(
                "Missing the required parameter `schedule_id` when calling `k_yc_protect_get_profile_schedules_by_schedule_id`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501
        if "schedule_id" in params:
            path_params["scheduleId"] = params["schedule_id"]  # noqa: E501

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
            "/compliance/kyc-protect/profiles/{profileId}/schedules/{scheduleId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse20014",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def k_yc_protect_get_s_list_of_searches_on_the_given_profile(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Return List Of AML Searches On The Given Profile  # noqa: E501

        Returns a list of searches both business and individual associated to the profile for the profile Id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_protect_get_s_list_of_searches_on_the_given_profile(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :param bool is_scheduled:
        :return: MODEL5941c0
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.k_yc_protect_get_s_list_of_searches_on_the_given_profile_with_http_info(
                profile_id, **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.k_yc_protect_get_s_list_of_searches_on_the_given_profile_with_http_info(
                    profile_id, **kwargs
                )
            )  # noqa: E501
            return data

    def k_yc_protect_get_s_list_of_searches_on_the_given_profile_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Return List Of AML Searches On The Given Profile  # noqa: E501

        Returns a list of searches both business and individual associated to the profile for the profile Id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.k_yc_protect_get_s_list_of_searches_on_the_given_profile_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :param bool is_scheduled:
        :return: MODEL5941c0
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "page", "page_size", "is_scheduled"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method k_yc_protect_get_s_list_of_searches_on_the_given_profile"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `k_yc_protect_get_s_list_of_searches_on_the_given_profile`"
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
            "/compliance/kyc-protect/profiles/{profileId}/searches",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="MODEL5941c0",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

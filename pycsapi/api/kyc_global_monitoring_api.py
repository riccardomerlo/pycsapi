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


class KYCGlobalMonitoringApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def compliance_delete_kyc_monitoring_profiles(self, **kwargs):  # noqa: E501
        """Delete Profiles From Monitoring  # noqa: E501

        Removes list of profiles from kyc monitoring  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliance_delete_kyc_monitoring_profiles(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeleteKYCMonitoringProfilesResquest body:
        :return: DeleteKYCMonitoringProfilesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.compliance_delete_kyc_monitoring_profiles_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (data) = self.compliance_delete_kyc_monitoring_profiles_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def compliance_delete_kyc_monitoring_profiles_with_http_info(
        self, **kwargs
    ):  # noqa: E501
        """Delete Profiles From Monitoring  # noqa: E501

        Removes list of profiles from kyc monitoring  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliance_delete_kyc_monitoring_profiles_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DeleteKYCMonitoringProfilesResquest body:
        :return: DeleteKYCMonitoringProfilesResponse
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
                    " to method compliance_delete_kyc_monitoring_profiles" % key
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
            "/compliance/kyc-protect/kycMonitoring/profiles",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="DeleteKYCMonitoringProfilesResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def compliance_post_kyc_monitoring_profiles_bulk(self, **kwargs):  # noqa: E501
        """Add Profiles To Monitoring  # noqa: E501

        Adds a list of profile/s to monitoring.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliance_post_kyc_monitoring_profiles_bulk(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostKYCMonitoringProfilesBulkResquest body:
        :return: PostKYCMonitoringProfilesBulkResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.compliance_post_kyc_monitoring_profiles_bulk_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (data) = self.compliance_post_kyc_monitoring_profiles_bulk_with_http_info(
                **kwargs
            )  # noqa: E501
            return data

    def compliance_post_kyc_monitoring_profiles_bulk_with_http_info(
        self, **kwargs
    ):  # noqa: E501
        """Add Profiles To Monitoring  # noqa: E501

        Adds a list of profile/s to monitoring.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliance_post_kyc_monitoring_profiles_bulk_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PostKYCMonitoringProfilesBulkResquest body:
        :return: PostKYCMonitoringProfilesBulkResponse
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
                    " to method compliance_post_kyc_monitoring_profiles_bulk" % key
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
            "/compliance/kyc-protect/kycMonitoring/profiles/bulk",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="PostKYCMonitoringProfilesBulkResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def compliance_protect_get_lookup_monitoring_country_codes(
        self, **kwargs
    ):  # noqa: E501
        """Returns Available Country Codes  # noqa: E501

        Gets the list of acceptable country codes for kyc monitoring.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliance_protect_get_lookup_monitoring_country_codes(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.compliance_protect_get_lookup_monitoring_country_codes_with_http_info(
                **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.compliance_protect_get_lookup_monitoring_country_codes_with_http_info(
                    **kwargs
                )
            )  # noqa: E501
            return data

    def compliance_protect_get_lookup_monitoring_country_codes_with_http_info(
        self, **kwargs
    ):  # noqa: E501
        """Returns Available Country Codes  # noqa: E501

        Gets the list of acceptable country codes for kyc monitoring.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliance_protect_get_lookup_monitoring_country_codes_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[str]
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
                    " to method compliance_protect_get_lookup_monitoring_country_codes"
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
            "/compliance/kyc-protect/lookup/kycMonitoring/countryCodes",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[str]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def compliancegetkycmonitoringindividualprofilealertsbyalertid(
        self, profile_id, alert_id, **kwargs
    ):  # noqa: E501
        """Return Alert By Alert Id And ProfileId  # noqa: E501

        Gets a kyc alert associated with a given profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliancegetkycmonitoringindividualprofilealertsbyalertid(profile_id, alert_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param str alert_id: id of the kyc alert (required)
        :return: KycMonitoringKycAlertResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.compliancegetkycmonitoringindividualprofilealertsbyalertid_with_http_info(
                profile_id, alert_id, **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.compliancegetkycmonitoringindividualprofilealertsbyalertid_with_http_info(
                    profile_id, alert_id, **kwargs
                )
            )  # noqa: E501
            return data

    def compliancegetkycmonitoringindividualprofilealertsbyalertid_with_http_info(
        self, profile_id, alert_id, **kwargs
    ):  # noqa: E501
        """Return Alert By Alert Id And ProfileId  # noqa: E501

        Gets a kyc alert associated with a given profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliancegetkycmonitoringindividualprofilealertsbyalertid_with_http_info(profile_id, alert_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param str alert_id: id of the kyc alert (required)
        :return: KycMonitoringKycAlertResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "alert_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method compliancegetkycmonitoringindividualprofilealertsbyalertid"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `compliancegetkycmonitoringindividualprofilealertsbyalertid`"
            )  # noqa: E501
        # verify the required parameter 'alert_id' is set
        if "alert_id" not in params or params["alert_id"] is None:
            raise ValueError(
                "Missing the required parameter `alert_id` when calling `compliancegetkycmonitoringindividualprofilealertsbyalertid`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501
        if "alert_id" in params:
            path_params["alertId"] = params["alert_id"]  # noqa: E501

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
            "/compliance/kyc-protect/kycMonitoring/profiles/{profileId}/alerts/{alertId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="KycMonitoringKycAlertResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def compliancegetkycmonitoringprofilealertsbyprofileid(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Return List Of Alerts By Profile  # noqa: E501

        Gets a list of kyc alerts by profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliancegetkycmonitoringprofilealertsbyprofileid(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :param list[str] statuses: Statuses of kyc alert to filter. Allowed values are Open, ClosedProcessed and ClosedUnprocessed
        :return: InlineResponse20016
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return (
                self.compliancegetkycmonitoringprofilealertsbyprofileid_with_http_info(
                    profile_id, **kwargs
                )
            )  # noqa: E501
        else:
            (data) = (
                self.compliancegetkycmonitoringprofilealertsbyprofileid_with_http_info(
                    profile_id, **kwargs
                )
            )  # noqa: E501
            return data

    def compliancegetkycmonitoringprofilealertsbyprofileid_with_http_info(
        self, profile_id, **kwargs
    ):  # noqa: E501
        """Return List Of Alerts By Profile  # noqa: E501

        Gets a list of kyc alerts by profile.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.compliancegetkycmonitoringprofilealertsbyprofileid_with_http_info(profile_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param int page: Starting page number.
        :param int page_size: Specifies the number of items to be displayed per page. Allowed values are between 1 and 100.
        :param list[str] statuses: Statuses of kyc alert to filter. Allowed values are Open, ClosedProcessed and ClosedUnprocessed
        :return: InlineResponse20016
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "page", "page_size", "statuses"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method compliancegetkycmonitoringprofilealertsbyprofileid"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `compliancegetkycmonitoringprofilealertsbyprofileid`"
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
        if "statuses" in params:
            query_params.append(("statuses", params["statuses"]))  # noqa: E501
            collection_formats["statuses"] = "multi"  # noqa: E501

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
            "/compliance/kyc-protect/kycMonitoring/profiles/{profileId}/alerts",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse20016",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def complianceputkycmonitoringindividualprofilealertsbyalertid(
        self, profile_id, alert_id, **kwargs
    ):  # noqa: E501
        """Update Status of Alert By Profile Id And Alert Id  # noqa: E501

        Updates a kyc alert associated with a given profile  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.complianceputkycmonitoringindividualprofilealertsbyalertid(profile_id, alert_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param str alert_id: id of the kyc alert (required)
        :param UpdateKycAlertContract body:
        :return: KycMonitoringKycAlertResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.complianceputkycmonitoringindividualprofilealertsbyalertid_with_http_info(
                profile_id, alert_id, **kwargs
            )  # noqa: E501
        else:
            (data) = (
                self.complianceputkycmonitoringindividualprofilealertsbyalertid_with_http_info(
                    profile_id, alert_id, **kwargs
                )
            )  # noqa: E501
            return data

    def complianceputkycmonitoringindividualprofilealertsbyalertid_with_http_info(
        self, profile_id, alert_id, **kwargs
    ):  # noqa: E501
        """Update Status of Alert By Profile Id And Alert Id  # noqa: E501

        Updates a kyc alert associated with a given profile  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.complianceputkycmonitoringindividualprofilealertsbyalertid_with_http_info(profile_id, alert_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str profile_id: id of the profile (required)
        :param str alert_id: id of the kyc alert (required)
        :param UpdateKycAlertContract body:
        :return: KycMonitoringKycAlertResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["profile_id", "alert_id", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method complianceputkycmonitoringindividualprofilealertsbyalertid"
                    % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'profile_id' is set
        if "profile_id" not in params or params["profile_id"] is None:
            raise ValueError(
                "Missing the required parameter `profile_id` when calling `complianceputkycmonitoringindividualprofilealertsbyalertid`"
            )  # noqa: E501
        # verify the required parameter 'alert_id' is set
        if "alert_id" not in params or params["alert_id"] is None:
            raise ValueError(
                "Missing the required parameter `alert_id` when calling `complianceputkycmonitoringindividualprofilealertsbyalertid`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "profile_id" in params:
            path_params["profileId"] = params["profile_id"]  # noqa: E501
        if "alert_id" in params:
            path_params["alertId"] = params["alert_id"]  # noqa: E501

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
            "/compliance/kyc-protect/kycMonitoring/profiles/{profileId}/alerts/{alertId}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="KycMonitoringKycAlertResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

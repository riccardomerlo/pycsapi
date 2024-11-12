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


class ConsumersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def consumer_report(
        self,
        countries,
        first_name,
        last_name,
        street,
        house_no,
        city,
        post_code,
        **kwargs
    ):  # noqa: E501
        """Consumer Report  # noqa: E501

        Consumer Search and Report endpoint. When sufficient information has been provided to filter potential Consumer results down to one record then the Consumer Report will be returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.consumer_report(countries, first_name, last_name, street, house_no, city, post_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreditsafeGlobalDataCountryCode countries: ISO-2 country code (required)
        :param str first_name: Consumer's First Name (required)
        :param str last_name: Consumer's Last Name (required)
        :param str street: Address part identifier - Street of the Consumer (required)
        :param str house_no: Address part identifier - House/Building Number of the Consumer (required)
        :param str city: Address part identifier - City of the Consumer (required)
        :param str post_code: Address part identifier - Postcode/Zip Code of the Consumer (required)
        :param str language:
        :param datetime date_of_birth:
        :param str custom_data:
        :param str call_ref: This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions.
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.consumer_report_with_http_info(
                countries,
                first_name,
                last_name,
                street,
                house_no,
                city,
                post_code,
                **kwargs
            )  # noqa: E501
        else:
            (data) = self.consumer_report_with_http_info(
                countries,
                first_name,
                last_name,
                street,
                house_no,
                city,
                post_code,
                **kwargs
            )  # noqa: E501
            return data

    def consumer_report_with_http_info(
        self,
        countries,
        first_name,
        last_name,
        street,
        house_no,
        city,
        post_code,
        **kwargs
    ):  # noqa: E501
        """Consumer Report  # noqa: E501

        Consumer Search and Report endpoint. When sufficient information has been provided to filter potential Consumer results down to one record then the Consumer Report will be returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.consumer_report_with_http_info(countries, first_name, last_name, street, house_no, city, post_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreditsafeGlobalDataCountryCode countries: ISO-2 country code (required)
        :param str first_name: Consumer's First Name (required)
        :param str last_name: Consumer's Last Name (required)
        :param str street: Address part identifier - Street of the Consumer (required)
        :param str house_no: Address part identifier - House/Building Number of the Consumer (required)
        :param str city: Address part identifier - City of the Consumer (required)
        :param str post_code: Address part identifier - Postcode/Zip Code of the Consumer (required)
        :param str language:
        :param datetime date_of_birth:
        :param str custom_data:
        :param str call_ref: This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions.
        :return: InlineResponse2005
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "countries",
            "first_name",
            "last_name",
            "street",
            "house_no",
            "city",
            "post_code",
            "language",
            "date_of_birth",
            "custom_data",
            "call_ref",
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
                    " to method consumer_report" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'countries' is set
        if "countries" not in params or params["countries"] is None:
            raise ValueError(
                "Missing the required parameter `countries` when calling `consumer_report`"
            )  # noqa: E501
        # verify the required parameter 'first_name' is set
        if "first_name" not in params or params["first_name"] is None:
            raise ValueError(
                "Missing the required parameter `first_name` when calling `consumer_report`"
            )  # noqa: E501
        # verify the required parameter 'last_name' is set
        if "last_name" not in params or params["last_name"] is None:
            raise ValueError(
                "Missing the required parameter `last_name` when calling `consumer_report`"
            )  # noqa: E501
        # verify the required parameter 'street' is set
        if "street" not in params or params["street"] is None:
            raise ValueError(
                "Missing the required parameter `street` when calling `consumer_report`"
            )  # noqa: E501
        # verify the required parameter 'house_no' is set
        if "house_no" not in params or params["house_no"] is None:
            raise ValueError(
                "Missing the required parameter `house_no` when calling `consumer_report`"
            )  # noqa: E501
        # verify the required parameter 'city' is set
        if "city" not in params or params["city"] is None:
            raise ValueError(
                "Missing the required parameter `city` when calling `consumer_report`"
            )  # noqa: E501
        # verify the required parameter 'post_code' is set
        if "post_code" not in params or params["post_code"] is None:
            raise ValueError(
                "Missing the required parameter `post_code` when calling `consumer_report`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if "countries" in params:
            query_params.append(("countries", params["countries"]))  # noqa: E501
        if "language" in params:
            query_params.append(("language", params["language"]))  # noqa: E501
        if "first_name" in params:
            query_params.append(("firstName", params["first_name"]))  # noqa: E501
        if "last_name" in params:
            query_params.append(("lastName", params["last_name"]))  # noqa: E501
        if "street" in params:
            query_params.append(("street", params["street"]))  # noqa: E501
        if "house_no" in params:
            query_params.append(("houseNo", params["house_no"]))  # noqa: E501
        if "city" in params:
            query_params.append(("city", params["city"]))  # noqa: E501
        if "post_code" in params:
            query_params.append(("postCode", params["post_code"]))  # noqa: E501
        if "date_of_birth" in params:
            query_params.append(("dateOfBirth", params["date_of_birth"]))  # noqa: E501
        if "custom_data" in params:
            query_params.append(("customData", params["custom_data"]))  # noqa: E501
        if "call_ref" in params:
            query_params.append(("callRef", params["call_ref"]))  # noqa: E501

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
            "/consumers",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse2005",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def consumer_search_criteria(self, countries, **kwargs):  # noqa: E501
        """Consumer Search Criteria  # noqa: E501

        Returns country specific fields that can be used to search for a Consumer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.consumer_search_criteria(countries, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str countries: Comma-separated list of ISO-2 country codes (required)
        :param str call_ref: This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions.
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.consumer_search_criteria_with_http_info(
                countries, **kwargs
            )  # noqa: E501
        else:
            (data) = self.consumer_search_criteria_with_http_info(
                countries, **kwargs
            )  # noqa: E501
            return data

    def consumer_search_criteria_with_http_info(
        self, countries, **kwargs
    ):  # noqa: E501
        """Consumer Search Criteria  # noqa: E501

        Returns country specific fields that can be used to search for a Consumer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.consumer_search_criteria_with_http_info(countries, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str countries: Comma-separated list of ISO-2 country codes (required)
        :param str call_ref: This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions.
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["countries", "call_ref"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method consumer_search_criteria" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'countries' is set
        if "countries" not in params or params["countries"] is None:
            raise ValueError(
                "Missing the required parameter `countries` when calling `consumer_search_criteria`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if "countries" in params:
            query_params.append(("countries", params["countries"]))  # noqa: E501
        if "call_ref" in params:
            query_params.append(("callRef", params["call_ref"]))  # noqa: E501

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
            "/consumers/searchcriteria",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[object]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

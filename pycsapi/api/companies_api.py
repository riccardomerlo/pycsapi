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


class CompaniesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def company_credit_report(self, connect_id, **kwargs):  # noqa: E501
        """Company Credit Report  # noqa: E501

        Orders a Company Credit Report by connectId.<br><br> To acquire a PDF version of the report use the optional request in 'Header'.<br><br> This request will provide a 'Base64-encoded' script to convert to a PDF, this will appear at the end of the JSON response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.company_credit_report(connect_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str connect_id: The connectId (optionally Safe Number where available) of the Company required to order their Credit Report. Obtained from `/companies` search results. (required)
        :param str accept: Applies request for PDF link to Company Report.
        :param str language: Report Language - The JSON structure of the Report is language invariant, but field content will return as the given language, where available.
        :param str template: Optional parameter to request a Templated Company Report. A Template adds/reduces sections of the Credit Report depending on your subscription. Do not include this parameter if you have not been given a template to use.<br> <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000063360-connect-report-templates-glossary-availability\" target=\"_blank\"> Connect Report Templates </a>
        :param bool include_indicators: Optional parameter to include the indicator scores in to a company report -`fsi = Financial Strength` , `pbi = Payment Behaviour Indicator`, `eti = Estimated Turnover`, `pei = Payment Expectation Indicator`<br><br> Addition information on indicator acronyms can be found <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000084411-connect-report-indicator-definitions\" target=\"_blank\">HERE.</a><br><br> Addition information on understanding indicators can be found <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000078780-what-are-indicators-in-the-scores-and-indicators-tab-\" target=\"_blank\">HERE.</a>
        :param str custom_data: Additional Report Parameters e.g.  German Report Reason Code value is `de_reason_code::1` . Use /reportcustomdata/{country} endpoint to see all values.
        :param str call_ref: This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions.
        :return: CreditsafeGlobalDataReportsCompanyReportResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.company_credit_report_with_http_info(
                connect_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.company_credit_report_with_http_info(
                connect_id, **kwargs
            )  # noqa: E501
            return data

    def company_credit_report_with_http_info(self, connect_id, **kwargs):  # noqa: E501
        """Company Credit Report  # noqa: E501

        Orders a Company Credit Report by connectId.<br><br> To acquire a PDF version of the report use the optional request in 'Header'.<br><br> This request will provide a 'Base64-encoded' script to convert to a PDF, this will appear at the end of the JSON response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.company_credit_report_with_http_info(connect_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str connect_id: The connectId (optionally Safe Number where available) of the Company required to order their Credit Report. Obtained from `/companies` search results. (required)
        :param str accept: Applies request for PDF link to Company Report.
        :param str language: Report Language - The JSON structure of the Report is language invariant, but field content will return as the given language, where available.
        :param str template: Optional parameter to request a Templated Company Report. A Template adds/reduces sections of the Credit Report depending on your subscription. Do not include this parameter if you have not been given a template to use.<br> <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000063360-connect-report-templates-glossary-availability\" target=\"_blank\"> Connect Report Templates </a>
        :param bool include_indicators: Optional parameter to include the indicator scores in to a company report -`fsi = Financial Strength` , `pbi = Payment Behaviour Indicator`, `eti = Estimated Turnover`, `pei = Payment Expectation Indicator`<br><br> Addition information on indicator acronyms can be found <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000084411-connect-report-indicator-definitions\" target=\"_blank\">HERE.</a><br><br> Addition information on understanding indicators can be found <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000078780-what-are-indicators-in-the-scores-and-indicators-tab-\" target=\"_blank\">HERE.</a>
        :param str custom_data: Additional Report Parameters e.g.  German Report Reason Code value is `de_reason_code::1` . Use /reportcustomdata/{country} endpoint to see all values.
        :param str call_ref: This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions.
        :return: CreditsafeGlobalDataReportsCompanyReportResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "connect_id",
            "accept",
            "language",
            "template",
            "include_indicators",
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
                    " to method company_credit_report" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'connect_id' is set
        if "connect_id" not in params or params["connect_id"] is None:
            raise ValueError(
                "Missing the required parameter `connect_id` when calling `company_credit_report`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "connect_id" in params:
            path_params["connectId"] = params["connect_id"]  # noqa: E501

        query_params = []
        if "language" in params:
            query_params.append(("language", params["language"]))  # noqa: E501
        if "template" in params:
            query_params.append(("template", params["template"]))  # noqa: E501
        if "include_indicators" in params:
            query_params.append(
                ("includeIndicators", params["include_indicators"])
            )  # noqa: E501
        if "custom_data" in params:
            query_params.append(("customData", params["custom_data"]))  # noqa: E501
        if "call_ref" in params:
            query_params.append(("callRef", params["call_ref"]))  # noqa: E501

        header_params = {}
        if "accept" in params:
            header_params["Accept"] = params["accept"]  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "application/json+pdf"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = ["bearerToken"]  # noqa: E501

        return self.api_client.call_api(
            "/companies/{connectId}",
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

    def company_search(self, countries, **kwargs):  # noqa: E501
        """Company Search  # noqa: E501

        Endpoint to search for Companies according to the provided Search Criteria. To get the most relevant results, it is recommended to use a unique identifier such as `regNo` where available. If a unique identifier is not available, use a combination of the companies registered `postCode` and `name` for the next best hit rate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.company_search(countries, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreditsafeGlobalDataCountryCode countries: comma-separated list of iso-2 country codes.<br>The code `PLC` can be used here to search for companies of this type across all countries. (required)
        :param int page: Starting page number.
        :param int page_size: Number of items to return per Page.
        :param str language: Only used for Countries where more than one Company Name exists for different languages e.g.  Japanese Kanji and English.<br>Country -  Languages Available<br>Japan [JP] - EN & JA
        :param str id: connectId - The primary Company identifier that is used to uniquely identify all companies across Creditsafe's Universe and Partner Network. This is returned on all Company Search Results. Use this field to use in other operations such as Ordering Company Credit Report by Id, and Adding Company to Monitoring Portfolio.
        :param str safe_no: Safe Number - Identifier for Companies in Creditsafe's Home Countries.
        :param str reg_no: Local Company Identifier - The Company identifier associated with it's Domestic Filing Agency. i.e. French SIREN/SIRET, United Kingdom Companies House CRN.
        :param str vat_no: Company VAT Number
        :param str name: Company Name
        :param str trade_name: Trade Name of the Company, typically used in Countries where Name is not uniquely registered.
        :param str acronym: A (non-unique) identifier to look for Companies by their more commonly known acronym rather than their lesser known full name. Acronym is predominantly available on French Companies.
        :param bool exact: Provide as `true` to find Companies matching a Name exactly.<br>A list of countries this is available at <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000083702-company-search-exact-parameter-availability\" target=\"_blank\">Here.
        :param str address:
        :param str street: Address part identifier - Street of the Company
        :param str house_no: Address part identifier - House/Building Number of the Company
        :param str city: Address part identifier - City of the Company
        :param str post_code: Address part identifier - Postcode/Zip Code of the Company. Can be provided partially to extend to a region with a * as a wildcard. I.e. CF* can represent all postcodes starting with CF.
        :param str province: Address part identifier - Province/State of the Company
        :param str call_ref: This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions.
        :param CreditsafeGlobalDataOfficeType office_type:
        :param list[str] phone_no: Provides Array of phone numbers or Null
        :param CreditsafeGlobalDataCompanyStatus status:
        :param CreditsafeGlobalDataCompanyType type:
        :param str website:
        :param str custom_data: Not currently used.
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.company_search_with_http_info(countries, **kwargs)  # noqa: E501
        else:
            (data) = self.company_search_with_http_info(
                countries, **kwargs
            )  # noqa: E501
            return data

    def company_search_with_http_info(self, countries, **kwargs):  # noqa: E501
        """Company Search  # noqa: E501

        Endpoint to search for Companies according to the provided Search Criteria. To get the most relevant results, it is recommended to use a unique identifier such as `regNo` where available. If a unique identifier is not available, use a combination of the companies registered `postCode` and `name` for the next best hit rate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.company_search_with_http_info(countries, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CreditsafeGlobalDataCountryCode countries: comma-separated list of iso-2 country codes.<br>The code `PLC` can be used here to search for companies of this type across all countries. (required)
        :param int page: Starting page number.
        :param int page_size: Number of items to return per Page.
        :param str language: Only used for Countries where more than one Company Name exists for different languages e.g.  Japanese Kanji and English.<br>Country -  Languages Available<br>Japan [JP] - EN & JA
        :param str id: connectId - The primary Company identifier that is used to uniquely identify all companies across Creditsafe's Universe and Partner Network. This is returned on all Company Search Results. Use this field to use in other operations such as Ordering Company Credit Report by Id, and Adding Company to Monitoring Portfolio.
        :param str safe_no: Safe Number - Identifier for Companies in Creditsafe's Home Countries.
        :param str reg_no: Local Company Identifier - The Company identifier associated with it's Domestic Filing Agency. i.e. French SIREN/SIRET, United Kingdom Companies House CRN.
        :param str vat_no: Company VAT Number
        :param str name: Company Name
        :param str trade_name: Trade Name of the Company, typically used in Countries where Name is not uniquely registered.
        :param str acronym: A (non-unique) identifier to look for Companies by their more commonly known acronym rather than their lesser known full name. Acronym is predominantly available on French Companies.
        :param bool exact: Provide as `true` to find Companies matching a Name exactly.<br>A list of countries this is available at <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000083702-company-search-exact-parameter-availability\" target=\"_blank\">Here.
        :param str address:
        :param str street: Address part identifier - Street of the Company
        :param str house_no: Address part identifier - House/Building Number of the Company
        :param str city: Address part identifier - City of the Company
        :param str post_code: Address part identifier - Postcode/Zip Code of the Company. Can be provided partially to extend to a region with a * as a wildcard. I.e. CF* can represent all postcodes starting with CF.
        :param str province: Address part identifier - Province/State of the Company
        :param str call_ref: This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions.
        :param CreditsafeGlobalDataOfficeType office_type:
        :param list[str] phone_no: Provides Array of phone numbers or Null
        :param CreditsafeGlobalDataCompanyStatus status:
        :param CreditsafeGlobalDataCompanyType type:
        :param str website:
        :param str custom_data: Not currently used.
        :return: InlineResponse200
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "countries",
            "page",
            "page_size",
            "language",
            "id",
            "safe_no",
            "reg_no",
            "vat_no",
            "name",
            "trade_name",
            "acronym",
            "exact",
            "address",
            "street",
            "house_no",
            "city",
            "post_code",
            "province",
            "call_ref",
            "office_type",
            "phone_no",
            "status",
            "type",
            "website",
            "custom_data",
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
                    " to method company_search" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'countries' is set
        if "countries" not in params or params["countries"] is None:
            raise ValueError(
                "Missing the required parameter `countries` when calling `company_search`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if "page" in params:
            query_params.append(("page", params["page"]))  # noqa: E501
        if "page_size" in params:
            query_params.append(("pageSize", params["page_size"]))  # noqa: E501
        if "countries" in params:
            query_params.append(("countries", params["countries"]))  # noqa: E501
        if "language" in params:
            query_params.append(("language", params["language"]))  # noqa: E501
        if "id" in params:
            query_params.append(("id", params["id"]))  # noqa: E501
        if "safe_no" in params:
            query_params.append(("safeNo", params["safe_no"]))  # noqa: E501
        if "reg_no" in params:
            query_params.append(("regNo", params["reg_no"]))  # noqa: E501
        if "vat_no" in params:
            query_params.append(("vatNo", params["vat_no"]))  # noqa: E501
        if "name" in params:
            query_params.append(("name", params["name"]))  # noqa: E501
        if "trade_name" in params:
            query_params.append(("tradeName", params["trade_name"]))  # noqa: E501
        if "acronym" in params:
            query_params.append(("acronym", params["acronym"]))  # noqa: E501
        if "exact" in params:
            query_params.append(("exact", params["exact"]))  # noqa: E501
        if "address" in params:
            query_params.append(("address", params["address"]))  # noqa: E501
        if "street" in params:
            query_params.append(("street", params["street"]))  # noqa: E501
        if "house_no" in params:
            query_params.append(("houseNo", params["house_no"]))  # noqa: E501
        if "city" in params:
            query_params.append(("city", params["city"]))  # noqa: E501
        if "post_code" in params:
            query_params.append(("postCode", params["post_code"]))  # noqa: E501
        if "province" in params:
            query_params.append(("province", params["province"]))  # noqa: E501
        if "call_ref" in params:
            query_params.append(("callRef", params["call_ref"]))  # noqa: E501
        if "office_type" in params:
            query_params.append(("officeType", params["office_type"]))  # noqa: E501
        if "phone_no" in params:
            query_params.append(("phoneNo", params["phone_no"]))  # noqa: E501
            collection_formats["phoneNo"] = "multi"  # noqa: E501
        if "status" in params:
            query_params.append(("status", params["status"]))  # noqa: E501
        if "type" in params:
            query_params.append(("type", params["type"]))  # noqa: E501
        if "website" in params:
            query_params.append(("website", params["website"]))  # noqa: E501
        if "custom_data" in params:
            query_params.append(("customData", params["custom_data"]))  # noqa: E501

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
            "/companies",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse200",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def company_search_criteria(self, countries, **kwargs):  # noqa: E501
        """Company Search Criteria  # noqa: E501

        Returns the set of available Company Search parameters/fields for a provided list of countries.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.company_search_criteria(countries, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str countries: A comma separated list of ISO/Alpha 2 format country codes, or singular country Code. e.g. US,GB will return the common searchable Company fields in the United States and Great Britain. (required)
        :return: CreditsafeGlobalDataSearchCriteriaSchemaCountry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.company_search_criteria_with_http_info(
                countries, **kwargs
            )  # noqa: E501
        else:
            (data) = self.company_search_criteria_with_http_info(
                countries, **kwargs
            )  # noqa: E501
            return data

    def company_search_criteria_with_http_info(self, countries, **kwargs):  # noqa: E501
        """Company Search Criteria  # noqa: E501

        Returns the set of available Company Search parameters/fields for a provided list of countries.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.company_search_criteria_with_http_info(countries, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str countries: A comma separated list of ISO/Alpha 2 format country codes, or singular country Code. e.g. US,GB will return the common searchable Company fields in the United States and Great Britain. (required)
        :return: CreditsafeGlobalDataSearchCriteriaSchemaCountry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["countries"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method company_search_criteria" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'countries' is set
        if "countries" not in params or params["countries"] is None:
            raise ValueError(
                "Missing the required parameter `countries` when calling `company_search_criteria`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if "countries" in params:
            query_params.append(("countries", params["countries"]))  # noqa: E501

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
            "/companies/searchcriteria",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="CreditsafeGlobalDataSearchCriteriaSchemaCountry",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def confidence_match_search(self, country, match_threshold, **kwargs):  # noqa: E501
        """Confidence Match Search  # noqa: E501

        Supply all company search criteria to find potential company matches ranked by a `single score`.   - <a href=\"https://creditsafe.freshdesk.com/en/support/solutions/articles/7000059769-interpreting-confidence-match-scores\" target=\"_blank\">See here for more information</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.confidence_match_search(country, match_threshold, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country: Iso-2 country code (required)
        :param int match_threshold: There are 3 main score bands to use for a successful response.<br> - Use score `898` for a 'good' match on 'name'.<br> - Use score `899` for a 'good' match on 'name' and 'ok' response on an address component.<br> - Use scores between `900 - 999` for use on the other searches adjusting for level of 'match' response. (required)
        :param str reg_no: Local Company Identifier - The Company identifier associated with it's Domestic Filing Agency. i.e. French SIREN/SIRET, United Kingdom Companies House CRN.
        :param str vat_no: Company VAT Number
        :param str name: Company Name
        :param str street: Address part identifier - Street of the Company
        :param str house_no: Address part identifier - House/Building Number of the Company
        :param str city: Address part identifier - City of the Company
        :param str post_code: Address part identifier - Postcode/Zip Code of the Company.
        :param str province: Address part identifier - Province of the Company
        :param str state: Address part identifier - State of the Company
        :param str phone_no:
        :param str reference1: Customer supplied free text reference 1 of 3
        :param str reference2: Customer supplied free text reference 2 of 3
        :param str reference3: Customer supplied free text reference 3 of 3
        :param str call_ref: This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.confidence_match_search_with_http_info(
                country, match_threshold, **kwargs
            )  # noqa: E501
        else:
            (data) = self.confidence_match_search_with_http_info(
                country, match_threshold, **kwargs
            )  # noqa: E501
            return data

    def confidence_match_search_with_http_info(
        self, country, match_threshold, **kwargs
    ):  # noqa: E501
        """Confidence Match Search  # noqa: E501

        Supply all company search criteria to find potential company matches ranked by a `single score`.   - <a href=\"https://creditsafe.freshdesk.com/en/support/solutions/articles/7000059769-interpreting-confidence-match-scores\" target=\"_blank\">See here for more information</a>.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.confidence_match_search_with_http_info(country, match_threshold, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str country: Iso-2 country code (required)
        :param int match_threshold: There are 3 main score bands to use for a successful response.<br> - Use score `898` for a 'good' match on 'name'.<br> - Use score `899` for a 'good' match on 'name' and 'ok' response on an address component.<br> - Use scores between `900 - 999` for use on the other searches adjusting for level of 'match' response. (required)
        :param str reg_no: Local Company Identifier - The Company identifier associated with it's Domestic Filing Agency. i.e. French SIREN/SIRET, United Kingdom Companies House CRN.
        :param str vat_no: Company VAT Number
        :param str name: Company Name
        :param str street: Address part identifier - Street of the Company
        :param str house_no: Address part identifier - House/Building Number of the Company
        :param str city: Address part identifier - City of the Company
        :param str post_code: Address part identifier - Postcode/Zip Code of the Company.
        :param str province: Address part identifier - Province of the Company
        :param str state: Address part identifier - State of the Company
        :param str phone_no:
        :param str reference1: Customer supplied free text reference 1 of 3
        :param str reference2: Customer supplied free text reference 2 of 3
        :param str reference3: Customer supplied free text reference 3 of 3
        :param str call_ref: This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions.
        :return: InlineResponse2001
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "country",
            "match_threshold",
            "reg_no",
            "vat_no",
            "name",
            "street",
            "house_no",
            "city",
            "post_code",
            "province",
            "state",
            "phone_no",
            "reference1",
            "reference2",
            "reference3",
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
                    " to method confidence_match_search" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'country' is set
        if "country" not in params or params["country"] is None:
            raise ValueError(
                "Missing the required parameter `country` when calling `confidence_match_search`"
            )  # noqa: E501
        # verify the required parameter 'match_threshold' is set
        if "match_threshold" not in params or params["match_threshold"] is None:
            raise ValueError(
                "Missing the required parameter `match_threshold` when calling `confidence_match_search`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if "country" in params:
            query_params.append(("country", params["country"]))  # noqa: E501
        if "match_threshold" in params:
            query_params.append(
                ("matchThreshold", params["match_threshold"])
            )  # noqa: E501
        if "reg_no" in params:
            query_params.append(("regNo", params["reg_no"]))  # noqa: E501
        if "vat_no" in params:
            query_params.append(("vatNo", params["vat_no"]))  # noqa: E501
        if "name" in params:
            query_params.append(("name", params["name"]))  # noqa: E501
        if "street" in params:
            query_params.append(("street", params["street"]))  # noqa: E501
        if "house_no" in params:
            query_params.append(("houseNo", params["house_no"]))  # noqa: E501
        if "city" in params:
            query_params.append(("city", params["city"]))  # noqa: E501
        if "post_code" in params:
            query_params.append(("postCode", params["post_code"]))  # noqa: E501
        if "province" in params:
            query_params.append(("province", params["province"]))  # noqa: E501
        if "state" in params:
            query_params.append(("state", params["state"]))  # noqa: E501
        if "phone_no" in params:
            query_params.append(("phoneNo", params["phone_no"]))  # noqa: E501
        if "reference1" in params:
            query_params.append(("reference1", params["reference1"]))  # noqa: E501
        if "reference2" in params:
            query_params.append(("reference2", params["reference2"]))  # noqa: E501
        if "reference3" in params:
            query_params.append(("reference3", params["reference3"]))  # noqa: E501
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
            "/companies/match",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse2001",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

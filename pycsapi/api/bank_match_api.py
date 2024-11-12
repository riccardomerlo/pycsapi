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


class BankMatchApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def bank_match(self, check_type, company_id, **kwargs):  # noqa: E501
        """Bank Match  # noqa: E501

        The Bank Verification tool allows customers to instantly verify that small and medium sized companies you are working with are providing correct bank details, to reduce fraud and avoid delays in your on boarding process. The bank data for these companies is provided to Creditsafe by various financial providers, including major banks. When you provide us with a company number and their bank details, we are able to perform instant checks to verify that those bank details are associated with that company and return - </br> Match – We have bank information on the company, and the data provided by the customer matches the company records </br> No Match – We have bank information on the company, but the data provided does not match any of the company records </br> Data Unavailable - We do not have bank information on the company.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bank_match(check_type, company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_type: Validation uses an algorithm to determine if a SCAN or IBAN exists, but does not let you know if that SCAN or IBAN actually belongs to the company who has provided it. Verification takes this a step further and checks the Creditsafe database for a match on the SCAN/IBAN, and tells you if the bank details actually belong to the company, so you can be assured that you are sending your money to the correct entity. (required)
        :param str company_id: The connectId or safeNumber of the company to check against. (required)
        :param str sort_code: Sort Code to check - Must be passed in with Account Number to form a SCAN Result
        :param str account_number: Account Number to check - Must be passed in with Sort Code to form a SCAN Result
        :param str iban: IBAN to check
        :param str vat_number: VAT Number to check
        :return: ConnectBankMatchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.bank_match_with_http_info(
                check_type, company_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.bank_match_with_http_info(
                check_type, company_id, **kwargs
            )  # noqa: E501
            return data

    def bank_match_with_http_info(self, check_type, company_id, **kwargs):  # noqa: E501
        """Bank Match  # noqa: E501

        The Bank Verification tool allows customers to instantly verify that small and medium sized companies you are working with are providing correct bank details, to reduce fraud and avoid delays in your on boarding process. The bank data for these companies is provided to Creditsafe by various financial providers, including major banks. When you provide us with a company number and their bank details, we are able to perform instant checks to verify that those bank details are associated with that company and return - </br> Match – We have bank information on the company, and the data provided by the customer matches the company records </br> No Match – We have bank information on the company, but the data provided does not match any of the company records </br> Data Unavailable - We do not have bank information on the company.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bank_match_with_http_info(check_type, company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str check_type: Validation uses an algorithm to determine if a SCAN or IBAN exists, but does not let you know if that SCAN or IBAN actually belongs to the company who has provided it. Verification takes this a step further and checks the Creditsafe database for a match on the SCAN/IBAN, and tells you if the bank details actually belong to the company, so you can be assured that you are sending your money to the correct entity. (required)
        :param str company_id: The connectId or safeNumber of the company to check against. (required)
        :param str sort_code: Sort Code to check - Must be passed in with Account Number to form a SCAN Result
        :param str account_number: Account Number to check - Must be passed in with Sort Code to form a SCAN Result
        :param str iban: IBAN to check
        :param str vat_number: VAT Number to check
        :return: ConnectBankMatchResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "check_type",
            "company_id",
            "sort_code",
            "account_number",
            "iban",
            "vat_number",
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
                    " to method bank_match" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'check_type' is set
        if "check_type" not in params or params["check_type"] is None:
            raise ValueError(
                "Missing the required parameter `check_type` when calling `bank_match`"
            )  # noqa: E501
        # verify the required parameter 'company_id' is set
        if "company_id" not in params or params["company_id"] is None:
            raise ValueError(
                "Missing the required parameter `company_id` when calling `bank_match`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if "check_type" in params:
            query_params.append(("checkType", params["check_type"]))  # noqa: E501
        if "company_id" in params:
            query_params.append(("companyId", params["company_id"]))  # noqa: E501
        if "sort_code" in params:
            query_params.append(("sortCode", params["sort_code"]))  # noqa: E501
        if "account_number" in params:
            query_params.append(
                ("accountNumber", params["account_number"])
            )  # noqa: E501
        if "iban" in params:
            query_params.append(("iban", params["iban"]))  # noqa: E501
        if "vat_number" in params:
            query_params.append(("vatNumber", params["vat_number"]))  # noqa: E501

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
            "/localSolutions/GB/bankmatch",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectBankMatchResult",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

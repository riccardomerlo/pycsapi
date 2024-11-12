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


class GMIndividualPortfolioManagementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_company_to_portfolio(self, portfolio_id, **kwargs):  # noqa: E501
        """Add Company To Portfolio  # noqa: E501

        Endpoint to add a company using a company id, into a portfolio provided in as a path parameter. Additional fields can be used to add a personalReference, freeText, and personalLimit. These fields need to be submitted in the requestBody but can be 'nulled' if not required. See the two examples of the submission with and without these fields.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_company_to_portfolio(portfolio_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :param ConnectMonitoringAddCompanyToPortfolioRequest body:
        :return: ConnectMonitoringAddCompanyToPortfolioResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.add_company_to_portfolio_with_http_info(
                portfolio_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.add_company_to_portfolio_with_http_info(
                portfolio_id, **kwargs
            )  # noqa: E501
            return data

    def add_company_to_portfolio_with_http_info(
        self, portfolio_id, **kwargs
    ):  # noqa: E501
        """Add Company To Portfolio  # noqa: E501

        Endpoint to add a company using a company id, into a portfolio provided in as a path parameter. Additional fields can be used to add a personalReference, freeText, and personalLimit. These fields need to be submitted in the requestBody but can be 'nulled' if not required. See the two examples of the submission with and without these fields.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_company_to_portfolio_with_http_info(portfolio_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :param ConnectMonitoringAddCompanyToPortfolioRequest body:
        :return: ConnectMonitoringAddCompanyToPortfolioResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["portfolio_id", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_company_to_portfolio" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'portfolio_id' is set
        if "portfolio_id" not in params or params["portfolio_id"] is None:
            raise ValueError(
                "Missing the required parameter `portfolio_id` when calling `add_company_to_portfolio`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "portfolio_id" in params:
            path_params["portfolioId"] = params["portfolio_id"]  # noqa: E501

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
            "/monitoring/portfolios/{portfolioId}/companies",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectMonitoringAddCompanyToPortfolioResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def clear_companies_from_portfolio(
        self, body, portfolio_id, **kwargs
    ):  # noqa: E501
        """Clear Companies From Portfolio  # noqa: E501

        This endpoint allows for companies to be deleted from the specified portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clear_companies_from_portfolio(body, portfolio_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectMonitoringClearCompaniesRequest body: (required)
        :param float portfolio_id: The unique identifier of the portfolio you want to delete companies from, obtained from `/portfolios`. (required)
        :param bool clear_all: When ClearAll query parameter is False,Companies List needs to be passed. When ClearAll query parameter is True, Companies List must be empty. All companies will be deleted
        :return: ConnectMonitoringClearCompaniesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.clear_companies_from_portfolio_with_http_info(
                body, portfolio_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.clear_companies_from_portfolio_with_http_info(
                body, portfolio_id, **kwargs
            )  # noqa: E501
            return data

    def clear_companies_from_portfolio_with_http_info(
        self, body, portfolio_id, **kwargs
    ):  # noqa: E501
        """Clear Companies From Portfolio  # noqa: E501

        This endpoint allows for companies to be deleted from the specified portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.clear_companies_from_portfolio_with_http_info(body, portfolio_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ConnectMonitoringClearCompaniesRequest body: (required)
        :param float portfolio_id: The unique identifier of the portfolio you want to delete companies from, obtained from `/portfolios`. (required)
        :param bool clear_all: When ClearAll query parameter is False,Companies List needs to be passed. When ClearAll query parameter is True, Companies List must be empty. All companies will be deleted
        :return: ConnectMonitoringClearCompaniesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body", "portfolio_id", "clear_all"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method clear_companies_from_portfolio" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `clear_companies_from_portfolio`"
            )  # noqa: E501
        # verify the required parameter 'portfolio_id' is set
        if "portfolio_id" not in params or params["portfolio_id"] is None:
            raise ValueError(
                "Missing the required parameter `portfolio_id` when calling `clear_companies_from_portfolio`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "portfolio_id" in params:
            path_params["portfolioId"] = params["portfolio_id"]  # noqa: E501

        query_params = []
        if "clear_all" in params:
            query_params.append(("clearAll", params["clear_all"]))  # noqa: E501

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
            "/monitoring/portfolios/{portfolioId}/companies/clear",
            "PATCH",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectMonitoringClearCompaniesResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def delete_company_from_portfolio(
        self, portfolio_id, company_id, **kwargs
    ):  # noqa: E501
        """Delete Company From Portfolio  # noqa: E501

        Endpoint to delete a company from a portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_company_from_portfolio(portfolio_id, company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :param str company_id: A company Safe Number or Connect ID. (required)
        :return: ConnectMonitoringDeleteCompanyFromPortfolio
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_company_from_portfolio_with_http_info(
                portfolio_id, company_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.delete_company_from_portfolio_with_http_info(
                portfolio_id, company_id, **kwargs
            )  # noqa: E501
            return data

    def delete_company_from_portfolio_with_http_info(
        self, portfolio_id, company_id, **kwargs
    ):  # noqa: E501
        """Delete Company From Portfolio  # noqa: E501

        Endpoint to delete a company from a portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_company_from_portfolio_with_http_info(portfolio_id, company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :param str company_id: A company Safe Number or Connect ID. (required)
        :return: ConnectMonitoringDeleteCompanyFromPortfolio
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["portfolio_id", "company_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_company_from_portfolio" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'portfolio_id' is set
        if "portfolio_id" not in params or params["portfolio_id"] is None:
            raise ValueError(
                "Missing the required parameter `portfolio_id` when calling `delete_company_from_portfolio`"
            )  # noqa: E501
        # verify the required parameter 'company_id' is set
        if "company_id" not in params or params["company_id"] is None:
            raise ValueError(
                "Missing the required parameter `company_id` when calling `delete_company_from_portfolio`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "portfolio_id" in params:
            path_params["portfolioId"] = params["portfolio_id"]  # noqa: E501
        if "company_id" in params:
            path_params["companyId"] = params["company_id"]  # noqa: E501

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
            "/monitoring/portfolios/{portfolioId}/companies/{companyId}",
            "DELETE",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectMonitoringDeleteCompanyFromPortfolio",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_company_details_from_a_portfolio(
        self, portfolio_id, company_id, **kwargs
    ):  # noqa: E501
        """Get Company Details From A Portfolio  # noqa: E501

        This endpoint allows you to get various company details from a portfolio. Requires a portfolioID and companyID in the PATH of the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_details_from_a_portfolio(portfolio_id, company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :param str company_id: A company Safe Number or Connect ID. (required)
        :return: ConnectMonitoringGetCompanyFromPortfolio
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_company_details_from_a_portfolio_with_http_info(
                portfolio_id, company_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_company_details_from_a_portfolio_with_http_info(
                portfolio_id, company_id, **kwargs
            )  # noqa: E501
            return data

    def get_company_details_from_a_portfolio_with_http_info(
        self, portfolio_id, company_id, **kwargs
    ):  # noqa: E501
        """Get Company Details From A Portfolio  # noqa: E501

        This endpoint allows you to get various company details from a portfolio. Requires a portfolioID and companyID in the PATH of the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_company_details_from_a_portfolio_with_http_info(portfolio_id, company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :param str company_id: A company Safe Number or Connect ID. (required)
        :return: ConnectMonitoringGetCompanyFromPortfolio
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["portfolio_id", "company_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_company_details_from_a_portfolio" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'portfolio_id' is set
        if "portfolio_id" not in params or params["portfolio_id"] is None:
            raise ValueError(
                "Missing the required parameter `portfolio_id` when calling `get_company_details_from_a_portfolio`"
            )  # noqa: E501
        # verify the required parameter 'company_id' is set
        if "company_id" not in params or params["company_id"] is None:
            raise ValueError(
                "Missing the required parameter `company_id` when calling `get_company_details_from_a_portfolio`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "portfolio_id" in params:
            path_params["portfolioId"] = params["portfolio_id"]  # noqa: E501
        if "company_id" in params:
            path_params["companyId"] = params["company_id"]  # noqa: E501

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
            "/monitoring/portfolios/{portfolioId}/companies/{companyId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectMonitoringGetCompanyFromPortfolio",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def list_companies_in_a_portfolio(self, portfolio_id, **kwargs):  # noqa: E501
        """List Companies In A Portfolio  # noqa: E501

        This endpoints gets all companies from a specific portfolio based on the portfolio id, optionally filter with query parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_companies_in_a_portfolio(portfolio_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :param str search_query: Return companies that match the given value
        :param int page_size: Number of items to return per Page.
        :param int page: Starting page number inGlobal Monitoring is `0`. If all items are displayed on one page this can also be left blank.
        :param str country_code: Return <<resourcePathName>> that match the given countryCode
        :return: ConnectMonitoringCompaniesInAPortfolio
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.list_companies_in_a_portfolio_with_http_info(
                portfolio_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.list_companies_in_a_portfolio_with_http_info(
                portfolio_id, **kwargs
            )  # noqa: E501
            return data

    def list_companies_in_a_portfolio_with_http_info(
        self, portfolio_id, **kwargs
    ):  # noqa: E501
        """List Companies In A Portfolio  # noqa: E501

        This endpoints gets all companies from a specific portfolio based on the portfolio id, optionally filter with query parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_companies_in_a_portfolio_with_http_info(portfolio_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :param str search_query: Return companies that match the given value
        :param int page_size: Number of items to return per Page.
        :param int page: Starting page number inGlobal Monitoring is `0`. If all items are displayed on one page this can also be left blank.
        :param str country_code: Return <<resourcePathName>> that match the given countryCode
        :return: ConnectMonitoringCompaniesInAPortfolio
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "portfolio_id",
            "search_query",
            "page_size",
            "page",
            "country_code",
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
                    " to method list_companies_in_a_portfolio" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'portfolio_id' is set
        if "portfolio_id" not in params or params["portfolio_id"] is None:
            raise ValueError(
                "Missing the required parameter `portfolio_id` when calling `list_companies_in_a_portfolio`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "portfolio_id" in params:
            path_params["portfolioId"] = params["portfolio_id"]  # noqa: E501

        query_params = []
        if "search_query" in params:
            query_params.append(("searchQuery", params["search_query"]))  # noqa: E501
        if "page_size" in params:
            query_params.append(("pageSize", params["page_size"]))  # noqa: E501
        if "page" in params:
            query_params.append(("page", params["page"]))  # noqa: E501
        if "country_code" in params:
            query_params.append(("countryCode", params["country_code"]))  # noqa: E501

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
            "/monitoring/portfolios/{portfolioId}/companies",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectMonitoringCompaniesInAPortfolio",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def list_company_specific_notification_events(
        self, portfolio_id, company_id, **kwargs
    ):  # noqa: E501
        """List Company Specific NotificationEvents  # noqa: E501

        List of notification events based on the company id,optionally filtered with query parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_company_specific_notification_events(portfolio_id, company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :param str company_id: A company Safe Number or Connect ID. (required)
        :param str search_query: Return notificationEvents that match the given value
        :param str sort_dir: The direction that you wish to sort results by.
        :param int page_size: Number of items to return per Page (max 1000)
        :param int page: Starting page number inGlobal Monitoring is `0`. If all items are displayed on one page this can also be left blank.
        :param bool is_processed: A flag that can be set to `true` boolean value to mark it as an event that has been actioned.
        :param str sort_by: Sort results by this column. Null values of sort column are listed after non-nulls.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.list_company_specific_notification_events_with_http_info(
                portfolio_id, company_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.list_company_specific_notification_events_with_http_info(
                portfolio_id, company_id, **kwargs
            )  # noqa: E501
            return data

    def list_company_specific_notification_events_with_http_info(
        self, portfolio_id, company_id, **kwargs
    ):  # noqa: E501
        """List Company Specific NotificationEvents  # noqa: E501

        List of notification events based on the company id,optionally filtered with query parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_company_specific_notification_events_with_http_info(portfolio_id, company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :param str company_id: A company Safe Number or Connect ID. (required)
        :param str search_query: Return notificationEvents that match the given value
        :param str sort_dir: The direction that you wish to sort results by.
        :param int page_size: Number of items to return per Page (max 1000)
        :param int page: Starting page number inGlobal Monitoring is `0`. If all items are displayed on one page this can also be left blank.
        :param bool is_processed: A flag that can be set to `true` boolean value to mark it as an event that has been actioned.
        :param str sort_by: Sort results by this column. Null values of sort column are listed after non-nulls.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "portfolio_id",
            "company_id",
            "search_query",
            "sort_dir",
            "page_size",
            "page",
            "is_processed",
            "sort_by",
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
                    " to method list_company_specific_notification_events" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'portfolio_id' is set
        if "portfolio_id" not in params or params["portfolio_id"] is None:
            raise ValueError(
                "Missing the required parameter `portfolio_id` when calling `list_company_specific_notification_events`"
            )  # noqa: E501
        # verify the required parameter 'company_id' is set
        if "company_id" not in params or params["company_id"] is None:
            raise ValueError(
                "Missing the required parameter `company_id` when calling `list_company_specific_notification_events`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "portfolio_id" in params:
            path_params["portfolioId"] = params["portfolio_id"]  # noqa: E501
        if "company_id" in params:
            path_params["companyId"] = params["company_id"]  # noqa: E501

        query_params = []
        if "search_query" in params:
            query_params.append(("searchQuery", params["search_query"]))  # noqa: E501
        if "sort_dir" in params:
            query_params.append(("sortDir", params["sort_dir"]))  # noqa: E501
        if "page_size" in params:
            query_params.append(("pageSize", params["page_size"]))  # noqa: E501
        if "page" in params:
            query_params.append(("page", params["page"]))  # noqa: E501
        if "is_processed" in params:
            query_params.append(("isProcessed", params["is_processed"]))  # noqa: E501
        if "sort_by" in params:
            query_params.append(("sortBy", params["sort_by"]))  # noqa: E501

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
            "/monitoring/portfolios/{portfolioId}/companies/{companyId}/notificationEvents",
            "GET",
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

    def list_countries_of_monitored_companies(
        self, portfolio_id, **kwargs
    ):  # noqa: E501
        """List Countries of Monitored Companies  # noqa: E501

        This endpoint provides a list of distinct countries associated with the companies monitored within a specific portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_countries_of_monitored_companies(portfolio_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :return: ConnectMonitoringMonitoredCountriesInPortfolio
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.list_countries_of_monitored_companies_with_http_info(
                portfolio_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.list_countries_of_monitored_companies_with_http_info(
                portfolio_id, **kwargs
            )  # noqa: E501
            return data

    def list_countries_of_monitored_companies_with_http_info(
        self, portfolio_id, **kwargs
    ):  # noqa: E501
        """List Countries of Monitored Companies  # noqa: E501

        This endpoint provides a list of distinct countries associated with the companies monitored within a specific portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_countries_of_monitored_companies_with_http_info(portfolio_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :return: ConnectMonitoringMonitoredCountriesInPortfolio
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["portfolio_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_countries_of_monitored_companies" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'portfolio_id' is set
        if "portfolio_id" not in params or params["portfolio_id"] is None:
            raise ValueError(
                "Missing the required parameter `portfolio_id` when calling `list_countries_of_monitored_companies`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "portfolio_id" in params:
            path_params["portfolioId"] = params["portfolio_id"]  # noqa: E501

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
            "/monitoring/portfolios/{portfolioId}/countries",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectMonitoringMonitoredCountriesInPortfolio",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def list_portfolio_event_rules(self, portfolio_id, **kwargs):  # noqa: E501
        """List Portfolio Event Rules  # noqa: E501

        Get all notification `eventRules` for the given `portfolioId`. Notification event rules allow you to control which events you wish to monitor for the `companies` contained within the given `portfolio`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_portfolio_event_rules(portfolio_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier for the portfolio that you wish to retrieve notification event rules for, obtained from `/portfolios`. (required)
        :return: ConnectMonitoringListPortfolioEventRules
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.list_portfolio_event_rules_with_http_info(
                portfolio_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.list_portfolio_event_rules_with_http_info(
                portfolio_id, **kwargs
            )  # noqa: E501
            return data

    def list_portfolio_event_rules_with_http_info(
        self, portfolio_id, **kwargs
    ):  # noqa: E501
        """List Portfolio Event Rules  # noqa: E501

        Get all notification `eventRules` for the given `portfolioId`. Notification event rules allow you to control which events you wish to monitor for the `companies` contained within the given `portfolio`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_portfolio_event_rules_with_http_info(portfolio_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier for the portfolio that you wish to retrieve notification event rules for, obtained from `/portfolios`. (required)
        :return: ConnectMonitoringListPortfolioEventRules
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["portfolio_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_portfolio_event_rules" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'portfolio_id' is set
        if "portfolio_id" not in params or params["portfolio_id"] is None:
            raise ValueError(
                "Missing the required parameter `portfolio_id` when calling `list_portfolio_event_rules`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "portfolio_id" in params:
            path_params["portfolioId"] = params["portfolio_id"]  # noqa: E501

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
            "/monitoring/portfolios/{portfolioId}/eventRules",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectMonitoringListPortfolioEventRules",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def list_portfolio_event_rules_by_country(
        self, portfolio_id, country_code, **kwargs
    ):  # noqa: E501
        """List Portfolio Event Rules By Country  # noqa: E501

        Endpoint to that lists all the eventRules, their status and parameters based on a portfolio Id, filtered by country. Newly created portfolios are without any notification event rules by default, but you can switch rules on/off per country or on a global basis. There are different rules available for each country due to the different type of change event data that's available. The following GET request lists all the available rules for a portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_portfolio_event_rules_by_country(portfolio_id, country_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :param str country_code: Country code to show events for. <br> Please note that there is one exception in that `PLC` is the only 3-character that can be accepted here. (required)
        :return: ConnectMonitoringListPortfolioEventRules
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.list_portfolio_event_rules_by_country_with_http_info(
                portfolio_id, country_code, **kwargs
            )  # noqa: E501
        else:
            (data) = self.list_portfolio_event_rules_by_country_with_http_info(
                portfolio_id, country_code, **kwargs
            )  # noqa: E501
            return data

    def list_portfolio_event_rules_by_country_with_http_info(
        self, portfolio_id, country_code, **kwargs
    ):  # noqa: E501
        """List Portfolio Event Rules By Country  # noqa: E501

        Endpoint to that lists all the eventRules, their status and parameters based on a portfolio Id, filtered by country. Newly created portfolios are without any notification event rules by default, but you can switch rules on/off per country or on a global basis. There are different rules available for each country due to the different type of change event data that's available. The following GET request lists all the available rules for a portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_portfolio_event_rules_by_country_with_http_info(portfolio_id, country_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :param str country_code: Country code to show events for. <br> Please note that there is one exception in that `PLC` is the only 3-character that can be accepted here. (required)
        :return: ConnectMonitoringListPortfolioEventRules
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["portfolio_id", "country_code"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_portfolio_event_rules_by_country" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'portfolio_id' is set
        if "portfolio_id" not in params or params["portfolio_id"] is None:
            raise ValueError(
                "Missing the required parameter `portfolio_id` when calling `list_portfolio_event_rules_by_country`"
            )  # noqa: E501
        # verify the required parameter 'country_code' is set
        if "country_code" not in params or params["country_code"] is None:
            raise ValueError(
                "Missing the required parameter `country_code` when calling `list_portfolio_event_rules_by_country`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "portfolio_id" in params:
            path_params["portfolioId"] = params["portfolio_id"]  # noqa: E501
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
            "/monitoring/portfolios/{portfolioId}/eventRules/{countryCode}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectMonitoringListPortfolioEventRules",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def list_portfolio_notifications(self, portfolio_id, **kwargs):  # noqa: E501
        """List Portfolio Notifications  # noqa: E501

        Get all notificationEvents based on the portfolio id, optionally filter with query parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_portfolio_notifications(portfolio_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :param str search_query: Return notificationEvents that match the given value
        :param str sort_by: Sort results by this column. Null values of sort column are listed after non-nulls.
        :param str sort_dir: The direction that you wish to sort results by.
        :param int page_size: Number of items to return per Page.
        :param int page: Starting page number inGlobal Monitoring is `0`. If all items are displayed on one page this can also be left blank.
        :param datetime start_date: The start date on which results are filtered.
        :param datetime end_date: The end date on which results are filtered.
        :param bool filter_by_created_date: Set to `true` to filter the Notification Events of the \"createdDate\" field when using `startDate` and `endDate` parameters. By default this is set to `false`, with the date parameters filtering using the \"eventDate\" field.
        :return: ConnectMonitoringAllNotificationsEvents
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.list_portfolio_notifications_with_http_info(
                portfolio_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.list_portfolio_notifications_with_http_info(
                portfolio_id, **kwargs
            )  # noqa: E501
            return data

    def list_portfolio_notifications_with_http_info(
        self, portfolio_id, **kwargs
    ):  # noqa: E501
        """List Portfolio Notifications  # noqa: E501

        Get all notificationEvents based on the portfolio id, optionally filter with query parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_portfolio_notifications_with_http_info(portfolio_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :param str search_query: Return notificationEvents that match the given value
        :param str sort_by: Sort results by this column. Null values of sort column are listed after non-nulls.
        :param str sort_dir: The direction that you wish to sort results by.
        :param int page_size: Number of items to return per Page.
        :param int page: Starting page number inGlobal Monitoring is `0`. If all items are displayed on one page this can also be left blank.
        :param datetime start_date: The start date on which results are filtered.
        :param datetime end_date: The end date on which results are filtered.
        :param bool filter_by_created_date: Set to `true` to filter the Notification Events of the \"createdDate\" field when using `startDate` and `endDate` parameters. By default this is set to `false`, with the date parameters filtering using the \"eventDate\" field.
        :return: ConnectMonitoringAllNotificationsEvents
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = [
            "portfolio_id",
            "search_query",
            "sort_by",
            "sort_dir",
            "page_size",
            "page",
            "start_date",
            "end_date",
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
                    " to method list_portfolio_notifications" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'portfolio_id' is set
        if "portfolio_id" not in params or params["portfolio_id"] is None:
            raise ValueError(
                "Missing the required parameter `portfolio_id` when calling `list_portfolio_notifications`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "portfolio_id" in params:
            path_params["portfolioId"] = params["portfolio_id"]  # noqa: E501

        query_params = []
        if "search_query" in params:
            query_params.append(("searchQuery", params["search_query"]))  # noqa: E501
        if "sort_by" in params:
            query_params.append(("sortBy", params["sort_by"]))  # noqa: E501
        if "sort_dir" in params:
            query_params.append(("sortDir", params["sort_dir"]))  # noqa: E501
        if "page_size" in params:
            query_params.append(("pageSize", params["page_size"]))  # noqa: E501
        if "page" in params:
            query_params.append(("page", params["page"]))  # noqa: E501
        if "start_date" in params:
            query_params.append(("startDate", params["start_date"]))  # noqa: E501
        if "end_date" in params:
            query_params.append(("endDate", params["end_date"]))  # noqa: E501
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
            "/monitoring/portfolios/{portfolioId}/notificationEvents",
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

    def portfolio_risk_summary(self, portfolio_id, **kwargs):  # noqa: E501
        """Portfolio Risk Summary  # noqa: E501

        Get current portfolio risk summary information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.portfolio_risk_summary(portfolio_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :return: ConnectMonitoringRiskSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.portfolio_risk_summary_with_http_info(
                portfolio_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.portfolio_risk_summary_with_http_info(
                portfolio_id, **kwargs
            )  # noqa: E501
            return data

    def portfolio_risk_summary_with_http_info(
        self, portfolio_id, **kwargs
    ):  # noqa: E501
        """Portfolio Risk Summary  # noqa: E501

        Get current portfolio risk summary information.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.portfolio_risk_summary_with_http_info(portfolio_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :return: ConnectMonitoringRiskSummary
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["portfolio_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method portfolio_risk_summary" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'portfolio_id' is set
        if "portfolio_id" not in params or params["portfolio_id"] is None:
            raise ValueError(
                "Missing the required parameter `portfolio_id` when calling `portfolio_risk_summary`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "portfolio_id" in params:
            path_params["portfolioId"] = params["portfolio_id"]  # noqa: E501

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
            "/monitoring/portfolios/{portfolioId}/riskSummary",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectMonitoringRiskSummary",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def set_portfolio_default_rules(self, portfolio_id, **kwargs):  # noqa: E501
        """Set Portfolio Default Rules  # noqa: E501

        Update a portfolios event rules to default state. In Connect, default state means all rules are turned off.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_portfolio_default_rules(portfolio_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :return: InlineResponse204
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.set_portfolio_default_rules_with_http_info(
                portfolio_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.set_portfolio_default_rules_with_http_info(
                portfolio_id, **kwargs
            )  # noqa: E501
            return data

    def set_portfolio_default_rules_with_http_info(
        self, portfolio_id, **kwargs
    ):  # noqa: E501
        """Set Portfolio Default Rules  # noqa: E501

        Update a portfolios event rules to default state. In Connect, default state means all rules are turned off.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.set_portfolio_default_rules_with_http_info(portfolio_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :return: InlineResponse204
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["portfolio_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_portfolio_default_rules" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'portfolio_id' is set
        if "portfolio_id" not in params or params["portfolio_id"] is None:
            raise ValueError(
                "Missing the required parameter `portfolio_id` when calling `set_portfolio_default_rules`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "portfolio_id" in params:
            path_params["portfolioId"] = params["portfolio_id"]  # noqa: E501

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
            "/monitoring/portfolios/{portfolioId}/eventRules/setDefault",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse204",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update_company_details_in_portfolio(
        self, portfolio_id, company_id, **kwargs
    ):  # noqa: E501
        """Update Company Details In Portfolio  # noqa: E501

        Updates the company details in a specified portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_company_details_in_portfolio(portfolio_id, company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :param str company_id: A company Safe Number or Connect ID. (required)
        :param ConnectMonitoringUpdateCompanyDetailsInPortfolioRequest body:
        :return: ConnectMonitoringUpdateCompanyInPortfolio
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.update_company_details_in_portfolio_with_http_info(
                portfolio_id, company_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.update_company_details_in_portfolio_with_http_info(
                portfolio_id, company_id, **kwargs
            )  # noqa: E501
            return data

    def update_company_details_in_portfolio_with_http_info(
        self, portfolio_id, company_id, **kwargs
    ):  # noqa: E501
        """Update Company Details In Portfolio  # noqa: E501

        Updates the company details in a specified portfolio.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_company_details_in_portfolio_with_http_info(portfolio_id, company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :param str company_id: A company Safe Number or Connect ID. (required)
        :param ConnectMonitoringUpdateCompanyDetailsInPortfolioRequest body:
        :return: ConnectMonitoringUpdateCompanyInPortfolio
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["portfolio_id", "company_id", "body"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_company_details_in_portfolio" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'portfolio_id' is set
        if "portfolio_id" not in params or params["portfolio_id"] is None:
            raise ValueError(
                "Missing the required parameter `portfolio_id` when calling `update_company_details_in_portfolio`"
            )  # noqa: E501
        # verify the required parameter 'company_id' is set
        if "company_id" not in params or params["company_id"] is None:
            raise ValueError(
                "Missing the required parameter `company_id` when calling `update_company_details_in_portfolio`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "portfolio_id" in params:
            path_params["portfolioId"] = params["portfolio_id"]  # noqa: E501
        if "company_id" in params:
            path_params["companyId"] = params["company_id"]  # noqa: E501

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
            "/monitoring/portfolios/{portfolioId}/companies/{companyId}",
            "PATCH",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="ConnectMonitoringUpdateCompanyInPortfolio",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update_event_rules(
        self, body, portfolio_id, country_code, **kwargs
    ):  # noqa: E501
        """Update EventRules  # noqa: E501

        Endpoint to update an eventRule in a portfolio. Must provide a portfolio unique identifier and a country code in the URL of the PUT request. The Body of the request must contain the `ruleCode` number of the eventRule you want to update, with an `isActive` parameter. Some event rules may also contain specific parameters, which can be set with `param0`, `param1` and `param2`. parameters. Get the above information by calling the List All eventRules endpoint. <br><br> **Important Note**<br> It is recommended that any changes made to the `Event Rules` are verified using the [List Portfolio Event Rules Endpoint](#listPortfolioEventRules) after the PUT call has been made.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_event_rules(body, portfolio_id, country_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[ConnectMonitoringUpdateEventRulesBody] body: To ensure optimal processing efficiency when updating live event rules—whether for removal, addition, or status change—it is best practice to update the entire list of rules in a single operation. (required)
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :param str country_code: Country code to show events for (required)
        :return: InlineResponse204
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.update_event_rules_with_http_info(
                body, portfolio_id, country_code, **kwargs
            )  # noqa: E501
        else:
            (data) = self.update_event_rules_with_http_info(
                body, portfolio_id, country_code, **kwargs
            )  # noqa: E501
            return data

    def update_event_rules_with_http_info(
        self, body, portfolio_id, country_code, **kwargs
    ):  # noqa: E501
        """Update EventRules  # noqa: E501

        Endpoint to update an eventRule in a portfolio. Must provide a portfolio unique identifier and a country code in the URL of the PUT request. The Body of the request must contain the `ruleCode` number of the eventRule you want to update, with an `isActive` parameter. Some event rules may also contain specific parameters, which can be set with `param0`, `param1` and `param2`. parameters. Get the above information by calling the List All eventRules endpoint. <br><br> **Important Note**<br> It is recommended that any changes made to the `Event Rules` are verified using the [List Portfolio Event Rules Endpoint](#listPortfolioEventRules) after the PUT call has been made.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_event_rules_with_http_info(body, portfolio_id, country_code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[ConnectMonitoringUpdateEventRulesBody] body: To ensure optimal processing efficiency when updating live event rules—whether for removal, addition, or status change—it is best practice to update the entire list of rules in a single operation. (required)
        :param float portfolio_id: The unique identifier of the portfolio, obtained from `/portfolios`. (required)
        :param str country_code: Country code to show events for (required)
        :return: InlineResponse204
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["body", "portfolio_id", "country_code"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_event_rules" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'body' is set
        if "body" not in params or params["body"] is None:
            raise ValueError(
                "Missing the required parameter `body` when calling `update_event_rules`"
            )  # noqa: E501
        # verify the required parameter 'portfolio_id' is set
        if "portfolio_id" not in params or params["portfolio_id"] is None:
            raise ValueError(
                "Missing the required parameter `portfolio_id` when calling `update_event_rules`"
            )  # noqa: E501
        # verify the required parameter 'country_code' is set
        if "country_code" not in params or params["country_code"] is None:
            raise ValueError(
                "Missing the required parameter `country_code` when calling `update_event_rules`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "portfolio_id" in params:
            path_params["portfolioId"] = params["portfolio_id"]  # noqa: E501
        if "country_code" in params:
            path_params["countryCode"] = params["country_code"]  # noqa: E501

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
            "/monitoring/portfolios/{portfolioId}/eventRules/{countryCode}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="InlineResponse204",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

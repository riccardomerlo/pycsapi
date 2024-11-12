# pycsapi.GMIndividualPortfolioManagementApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_company_to_portfolio**](GMIndividualPortfolioManagementApi.md#add_company_to_portfolio) | **POST** /monitoring/portfolios/{portfolioId}/companies | Add Company To Portfolio
[**clear_companies_from_portfolio**](GMIndividualPortfolioManagementApi.md#clear_companies_from_portfolio) | **PATCH** /monitoring/portfolios/{portfolioId}/companies/clear | Clear Companies From Portfolio
[**delete_company_from_portfolio**](GMIndividualPortfolioManagementApi.md#delete_company_from_portfolio) | **DELETE** /monitoring/portfolios/{portfolioId}/companies/{companyId} | Delete Company From Portfolio
[**get_company_details_from_a_portfolio**](GMIndividualPortfolioManagementApi.md#get_company_details_from_a_portfolio) | **GET** /monitoring/portfolios/{portfolioId}/companies/{companyId} | Get Company Details From A Portfolio
[**list_companies_in_a_portfolio**](GMIndividualPortfolioManagementApi.md#list_companies_in_a_portfolio) | **GET** /monitoring/portfolios/{portfolioId}/companies | List Companies In A Portfolio
[**list_company_specific_notification_events**](GMIndividualPortfolioManagementApi.md#list_company_specific_notification_events) | **GET** /monitoring/portfolios/{portfolioId}/companies/{companyId}/notificationEvents | List Company Specific NotificationEvents
[**list_countries_of_monitored_companies**](GMIndividualPortfolioManagementApi.md#list_countries_of_monitored_companies) | **GET** /monitoring/portfolios/{portfolioId}/countries | List Countries of Monitored Companies
[**list_portfolio_event_rules**](GMIndividualPortfolioManagementApi.md#list_portfolio_event_rules) | **GET** /monitoring/portfolios/{portfolioId}/eventRules | List Portfolio Event Rules
[**list_portfolio_event_rules_by_country**](GMIndividualPortfolioManagementApi.md#list_portfolio_event_rules_by_country) | **GET** /monitoring/portfolios/{portfolioId}/eventRules/{countryCode} | List Portfolio Event Rules By Country
[**list_portfolio_notifications**](GMIndividualPortfolioManagementApi.md#list_portfolio_notifications) | **GET** /monitoring/portfolios/{portfolioId}/notificationEvents | List Portfolio Notifications
[**portfolio_risk_summary**](GMIndividualPortfolioManagementApi.md#portfolio_risk_summary) | **GET** /monitoring/portfolios/{portfolioId}/riskSummary | Portfolio Risk Summary
[**set_portfolio_default_rules**](GMIndividualPortfolioManagementApi.md#set_portfolio_default_rules) | **PUT** /monitoring/portfolios/{portfolioId}/eventRules/setDefault | Set Portfolio Default Rules
[**update_company_details_in_portfolio**](GMIndividualPortfolioManagementApi.md#update_company_details_in_portfolio) | **PATCH** /monitoring/portfolios/{portfolioId}/companies/{companyId} | Update Company Details In Portfolio
[**update_event_rules**](GMIndividualPortfolioManagementApi.md#update_event_rules) | **PUT** /monitoring/portfolios/{portfolioId}/eventRules/{countryCode} | Update EventRules

# **add_company_to_portfolio**
> ConnectMonitoringAddCompanyToPortfolioResponse add_company_to_portfolio(portfolio_id, body=body)

Add Company To Portfolio

Endpoint to add a company using a company id, into a portfolio provided in as a path parameter. Additional fields can be used to add a personalReference, freeText, and personalLimit. These fields need to be submitted in the requestBody but can be 'nulled' if not required. See the two examples of the submission with and without these fields.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMIndividualPortfolioManagementApi(pycsapi.ApiClient(configuration))
portfolio_id = 1.2 # float | The unique identifier of the portfolio, obtained from `/portfolios`.
body = pycsapi.ConnectMonitoringAddCompanyToPortfolioRequest() # ConnectMonitoringAddCompanyToPortfolioRequest |  (optional)

try:
    # Add Company To Portfolio
    api_response = api_instance.add_company_to_portfolio(portfolio_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMIndividualPortfolioManagementApi->add_company_to_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_id** | **float**| The unique identifier of the portfolio, obtained from &#x60;/portfolios&#x60;. | 
 **body** | [**ConnectMonitoringAddCompanyToPortfolioRequest**](ConnectMonitoringAddCompanyToPortfolioRequest.md)|  | [optional] 

### Return type

[**ConnectMonitoringAddCompanyToPortfolioResponse**](ConnectMonitoringAddCompanyToPortfolioResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_companies_from_portfolio**
> ConnectMonitoringClearCompaniesResponse clear_companies_from_portfolio(body, portfolio_id, clear_all=clear_all)

Clear Companies From Portfolio

This endpoint allows for companies to be deleted from the specified portfolio.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMIndividualPortfolioManagementApi(pycsapi.ApiClient(configuration))
body = pycsapi.ConnectMonitoringClearCompaniesRequest() # ConnectMonitoringClearCompaniesRequest | 
portfolio_id = 1.2 # float | The unique identifier of the portfolio you want to delete companies from, obtained from `/portfolios`.
clear_all = false # bool | When ClearAll query parameter is False,Companies List needs to be passed. When ClearAll query parameter is True, Companies List must be empty. All companies will be deleted (optional) (default to false)

try:
    # Clear Companies From Portfolio
    api_response = api_instance.clear_companies_from_portfolio(body, portfolio_id, clear_all=clear_all)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMIndividualPortfolioManagementApi->clear_companies_from_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectMonitoringClearCompaniesRequest**](ConnectMonitoringClearCompaniesRequest.md)|  | 
 **portfolio_id** | **float**| The unique identifier of the portfolio you want to delete companies from, obtained from &#x60;/portfolios&#x60;. | 
 **clear_all** | **bool**| When ClearAll query parameter is False,Companies List needs to be passed. When ClearAll query parameter is True, Companies List must be empty. All companies will be deleted | [optional] [default to false]

### Return type

[**ConnectMonitoringClearCompaniesResponse**](ConnectMonitoringClearCompaniesResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_company_from_portfolio**
> ConnectMonitoringDeleteCompanyFromPortfolio delete_company_from_portfolio(portfolio_id, company_id)

Delete Company From Portfolio

Endpoint to delete a company from a portfolio.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMIndividualPortfolioManagementApi(pycsapi.ApiClient(configuration))
portfolio_id = 1.2 # float | The unique identifier of the portfolio, obtained from `/portfolios`.
company_id = 'company_id_example' # str | A company Safe Number or Connect ID.

try:
    # Delete Company From Portfolio
    api_response = api_instance.delete_company_from_portfolio(portfolio_id, company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMIndividualPortfolioManagementApi->delete_company_from_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_id** | **float**| The unique identifier of the portfolio, obtained from &#x60;/portfolios&#x60;. | 
 **company_id** | **str**| A company Safe Number or Connect ID. | 

### Return type

[**ConnectMonitoringDeleteCompanyFromPortfolio**](ConnectMonitoringDeleteCompanyFromPortfolio.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_details_from_a_portfolio**
> ConnectMonitoringGetCompanyFromPortfolio get_company_details_from_a_portfolio(portfolio_id, company_id)

Get Company Details From A Portfolio

This endpoint allows you to get various company details from a portfolio. Requires a portfolioID and companyID in the PATH of the request.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMIndividualPortfolioManagementApi(pycsapi.ApiClient(configuration))
portfolio_id = 1.2 # float | The unique identifier of the portfolio, obtained from `/portfolios`.
company_id = 'company_id_example' # str | A company Safe Number or Connect ID.

try:
    # Get Company Details From A Portfolio
    api_response = api_instance.get_company_details_from_a_portfolio(portfolio_id, company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMIndividualPortfolioManagementApi->get_company_details_from_a_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_id** | **float**| The unique identifier of the portfolio, obtained from &#x60;/portfolios&#x60;. | 
 **company_id** | **str**| A company Safe Number or Connect ID. | 

### Return type

[**ConnectMonitoringGetCompanyFromPortfolio**](ConnectMonitoringGetCompanyFromPortfolio.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_companies_in_a_portfolio**
> ConnectMonitoringCompaniesInAPortfolio list_companies_in_a_portfolio(portfolio_id, search_query=search_query, page_size=page_size, page=page, country_code=country_code)

List Companies In A Portfolio

This endpoints gets all companies from a specific portfolio based on the portfolio id, optionally filter with query parameters.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMIndividualPortfolioManagementApi(pycsapi.ApiClient(configuration))
portfolio_id = 1.2 # float | The unique identifier of the portfolio, obtained from `/portfolios`.
search_query = 'search_query_example' # str | Return companies that match the given value (optional)
page_size = 56 # int | Number of items to return per Page. (optional)
page = 0 # int | Starting page number inGlobal Monitoring is `0`. If all items are displayed on one page this can also be left blank. (optional) (default to 0)
country_code = 'country_code_example' # str | Return <<resourcePathName>> that match the given countryCode (optional)

try:
    # List Companies In A Portfolio
    api_response = api_instance.list_companies_in_a_portfolio(portfolio_id, search_query=search_query, page_size=page_size, page=page, country_code=country_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMIndividualPortfolioManagementApi->list_companies_in_a_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_id** | **float**| The unique identifier of the portfolio, obtained from &#x60;/portfolios&#x60;. | 
 **search_query** | **str**| Return companies that match the given value | [optional] 
 **page_size** | **int**| Number of items to return per Page. | [optional] 
 **page** | **int**| Starting page number inGlobal Monitoring is &#x60;0&#x60;. If all items are displayed on one page this can also be left blank. | [optional] [default to 0]
 **country_code** | **str**| Return &lt;&lt;resourcePathName&gt;&gt; that match the given countryCode | [optional] 

### Return type

[**ConnectMonitoringCompaniesInAPortfolio**](ConnectMonitoringCompaniesInAPortfolio.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_company_specific_notification_events**
> list_company_specific_notification_events(portfolio_id, company_id, search_query=search_query, sort_dir=sort_dir, page_size=page_size, page=page, is_processed=is_processed, sort_by=sort_by)

List Company Specific NotificationEvents

List of notification events based on the company id,optionally filtered with query parameters.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMIndividualPortfolioManagementApi(pycsapi.ApiClient(configuration))
portfolio_id = 'portfolio_id_example' # str | The unique identifier of the portfolio, obtained from `/portfolios`.
company_id = 'company_id_example' # str | A company Safe Number or Connect ID.
search_query = 'search_query_example' # str | Return notificationEvents that match the given value (optional)
sort_dir = 'asc' # str | The direction that you wish to sort results by. (optional) (default to asc)
page_size = 50 # int | Number of items to return per Page (max 1000) (optional) (default to 50)
page = 0 # int | Starting page number inGlobal Monitoring is `0`. If all items are displayed on one page this can also be left blank. (optional) (default to 0)
is_processed = true # bool | A flag that can be set to `true` boolean value to mark it as an event that has been actioned. (optional)
sort_by = 'companyName' # str | Sort results by this column. Null values of sort column are listed after non-nulls. (optional) (default to companyName)

try:
    # List Company Specific NotificationEvents
    api_instance.list_company_specific_notification_events(portfolio_id, company_id, search_query=search_query, sort_dir=sort_dir, page_size=page_size, page=page, is_processed=is_processed, sort_by=sort_by)
except ApiException as e:
    print("Exception when calling GMIndividualPortfolioManagementApi->list_company_specific_notification_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_id** | **str**| The unique identifier of the portfolio, obtained from &#x60;/portfolios&#x60;. | 
 **company_id** | **str**| A company Safe Number or Connect ID. | 
 **search_query** | **str**| Return notificationEvents that match the given value | [optional] 
 **sort_dir** | **str**| The direction that you wish to sort results by. | [optional] [default to asc]
 **page_size** | **int**| Number of items to return per Page (max 1000) | [optional] [default to 50]
 **page** | **int**| Starting page number inGlobal Monitoring is &#x60;0&#x60;. If all items are displayed on one page this can also be left blank. | [optional] [default to 0]
 **is_processed** | **bool**| A flag that can be set to &#x60;true&#x60; boolean value to mark it as an event that has been actioned. | [optional] 
 **sort_by** | **str**| Sort results by this column. Null values of sort column are listed after non-nulls. | [optional] [default to companyName]

### Return type

void (empty response body)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_countries_of_monitored_companies**
> ConnectMonitoringMonitoredCountriesInPortfolio list_countries_of_monitored_companies(portfolio_id)

List Countries of Monitored Companies

This endpoint provides a list of distinct countries associated with the companies monitored within a specific portfolio.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMIndividualPortfolioManagementApi(pycsapi.ApiClient(configuration))
portfolio_id = 1.2 # float | The unique identifier of the portfolio, obtained from `/portfolios`.

try:
    # List Countries of Monitored Companies
    api_response = api_instance.list_countries_of_monitored_companies(portfolio_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMIndividualPortfolioManagementApi->list_countries_of_monitored_companies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_id** | **float**| The unique identifier of the portfolio, obtained from &#x60;/portfolios&#x60;. | 

### Return type

[**ConnectMonitoringMonitoredCountriesInPortfolio**](ConnectMonitoringMonitoredCountriesInPortfolio.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_portfolio_event_rules**
> ConnectMonitoringListPortfolioEventRules list_portfolio_event_rules(portfolio_id)

List Portfolio Event Rules

Get all notification `eventRules` for the given `portfolioId`. Notification event rules allow you to control which events you wish to monitor for the `companies` contained within the given `portfolio`.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMIndividualPortfolioManagementApi(pycsapi.ApiClient(configuration))
portfolio_id = 1.2 # float | The unique identifier for the portfolio that you wish to retrieve notification event rules for, obtained from `/portfolios`.

try:
    # List Portfolio Event Rules
    api_response = api_instance.list_portfolio_event_rules(portfolio_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMIndividualPortfolioManagementApi->list_portfolio_event_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_id** | **float**| The unique identifier for the portfolio that you wish to retrieve notification event rules for, obtained from &#x60;/portfolios&#x60;. | 

### Return type

[**ConnectMonitoringListPortfolioEventRules**](ConnectMonitoringListPortfolioEventRules.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_portfolio_event_rules_by_country**
> ConnectMonitoringListPortfolioEventRules list_portfolio_event_rules_by_country(portfolio_id, country_code)

List Portfolio Event Rules By Country

Endpoint to that lists all the eventRules, their status and parameters based on a portfolio Id, filtered by country. Newly created portfolios are without any notification event rules by default, but you can switch rules on/off per country or on a global basis. There are different rules available for each country due to the different type of change event data that's available. The following GET request lists all the available rules for a portfolio.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMIndividualPortfolioManagementApi(pycsapi.ApiClient(configuration))
portfolio_id = 1.2 # float | The unique identifier of the portfolio, obtained from `/portfolios`.
country_code = 'country_code_example' # str | Country code to show events for. <br> Please note that there is one exception in that `PLC` is the only 3-character that can be accepted here.

try:
    # List Portfolio Event Rules By Country
    api_response = api_instance.list_portfolio_event_rules_by_country(portfolio_id, country_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMIndividualPortfolioManagementApi->list_portfolio_event_rules_by_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_id** | **float**| The unique identifier of the portfolio, obtained from &#x60;/portfolios&#x60;. | 
 **country_code** | **str**| Country code to show events for. &lt;br&gt; Please note that there is one exception in that &#x60;PLC&#x60; is the only 3-character that can be accepted here. | 

### Return type

[**ConnectMonitoringListPortfolioEventRules**](ConnectMonitoringListPortfolioEventRules.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_portfolio_notifications**
> ConnectMonitoringAllNotificationsEvents list_portfolio_notifications(portfolio_id, search_query=search_query, sort_by=sort_by, sort_dir=sort_dir, page_size=page_size, page=page, start_date=start_date, end_date=end_date, filter_by_created_date=filter_by_created_date)

List Portfolio Notifications

Get all notificationEvents based on the portfolio id, optionally filter with query parameters.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMIndividualPortfolioManagementApi(pycsapi.ApiClient(configuration))
portfolio_id = 1.2 # float | The unique identifier of the portfolio, obtained from `/portfolios`.
search_query = 'search_query_example' # str | Return notificationEvents that match the given value (optional)
sort_by = 'companyName' # str | Sort results by this column. Null values of sort column are listed after non-nulls. (optional) (default to companyName)
sort_dir = 'asc' # str | The direction that you wish to sort results by. (optional) (default to asc)
page_size = 56 # int | Number of items to return per Page. (optional)
page = 0 # int | Starting page number inGlobal Monitoring is `0`. If all items are displayed on one page this can also be left blank. (optional) (default to 0)
start_date = '2013-10-20T19:20:30+01:00' # datetime | The start date on which results are filtered. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | The end date on which results are filtered. (optional)
filter_by_created_date = false # bool | Set to `true` to filter the Notification Events of the \"createdDate\" field when using `startDate` and `endDate` parameters. By default this is set to `false`, with the date parameters filtering using the \"eventDate\" field. (optional) (default to false)

try:
    # List Portfolio Notifications
    api_response = api_instance.list_portfolio_notifications(portfolio_id, search_query=search_query, sort_by=sort_by, sort_dir=sort_dir, page_size=page_size, page=page, start_date=start_date, end_date=end_date, filter_by_created_date=filter_by_created_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMIndividualPortfolioManagementApi->list_portfolio_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_id** | **float**| The unique identifier of the portfolio, obtained from &#x60;/portfolios&#x60;. | 
 **search_query** | **str**| Return notificationEvents that match the given value | [optional] 
 **sort_by** | **str**| Sort results by this column. Null values of sort column are listed after non-nulls. | [optional] [default to companyName]
 **sort_dir** | **str**| The direction that you wish to sort results by. | [optional] [default to asc]
 **page_size** | **int**| Number of items to return per Page. | [optional] 
 **page** | **int**| Starting page number inGlobal Monitoring is &#x60;0&#x60;. If all items are displayed on one page this can also be left blank. | [optional] [default to 0]
 **start_date** | **datetime**| The start date on which results are filtered. | [optional] 
 **end_date** | **datetime**| The end date on which results are filtered. | [optional] 
 **filter_by_created_date** | **bool**| Set to &#x60;true&#x60; to filter the Notification Events of the \&quot;createdDate\&quot; field when using &#x60;startDate&#x60; and &#x60;endDate&#x60; parameters. By default this is set to &#x60;false&#x60;, with the date parameters filtering using the \&quot;eventDate\&quot; field. | [optional] [default to false]

### Return type

[**ConnectMonitoringAllNotificationsEvents**](ConnectMonitoringAllNotificationsEvents.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portfolio_risk_summary**
> ConnectMonitoringRiskSummary portfolio_risk_summary(portfolio_id)

Portfolio Risk Summary

Get current portfolio risk summary information.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMIndividualPortfolioManagementApi(pycsapi.ApiClient(configuration))
portfolio_id = 1.2 # float | The unique identifier of the portfolio, obtained from `/portfolios`.

try:
    # Portfolio Risk Summary
    api_response = api_instance.portfolio_risk_summary(portfolio_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMIndividualPortfolioManagementApi->portfolio_risk_summary: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_id** | **float**| The unique identifier of the portfolio, obtained from &#x60;/portfolios&#x60;. | 

### Return type

[**ConnectMonitoringRiskSummary**](ConnectMonitoringRiskSummary.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_portfolio_default_rules**
> InlineResponse204 set_portfolio_default_rules(portfolio_id)

Set Portfolio Default Rules

Update a portfolios event rules to default state. In Connect, default state means all rules are turned off.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMIndividualPortfolioManagementApi(pycsapi.ApiClient(configuration))
portfolio_id = 1.2 # float | The unique identifier of the portfolio, obtained from `/portfolios`.

try:
    # Set Portfolio Default Rules
    api_response = api_instance.set_portfolio_default_rules(portfolio_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMIndividualPortfolioManagementApi->set_portfolio_default_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_id** | **float**| The unique identifier of the portfolio, obtained from &#x60;/portfolios&#x60;. | 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_company_details_in_portfolio**
> ConnectMonitoringUpdateCompanyInPortfolio update_company_details_in_portfolio(portfolio_id, company_id, body=body)

Update Company Details In Portfolio

Updates the company details in a specified portfolio.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMIndividualPortfolioManagementApi(pycsapi.ApiClient(configuration))
portfolio_id = 1.2 # float | The unique identifier of the portfolio, obtained from `/portfolios`.
company_id = 'company_id_example' # str | A company Safe Number or Connect ID.
body = pycsapi.ConnectMonitoringUpdateCompanyDetailsInPortfolioRequest() # ConnectMonitoringUpdateCompanyDetailsInPortfolioRequest |  (optional)

try:
    # Update Company Details In Portfolio
    api_response = api_instance.update_company_details_in_portfolio(portfolio_id, company_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMIndividualPortfolioManagementApi->update_company_details_in_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_id** | **float**| The unique identifier of the portfolio, obtained from &#x60;/portfolios&#x60;. | 
 **company_id** | **str**| A company Safe Number or Connect ID. | 
 **body** | [**ConnectMonitoringUpdateCompanyDetailsInPortfolioRequest**](ConnectMonitoringUpdateCompanyDetailsInPortfolioRequest.md)|  | [optional] 

### Return type

[**ConnectMonitoringUpdateCompanyInPortfolio**](ConnectMonitoringUpdateCompanyInPortfolio.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event_rules**
> InlineResponse204 update_event_rules(body, portfolio_id, country_code)

Update EventRules

Endpoint to update an eventRule in a portfolio. Must provide a portfolio unique identifier and a country code in the URL of the PUT request. The Body of the request must contain the `ruleCode` number of the eventRule you want to update, with an `isActive` parameter. Some event rules may also contain specific parameters, which can be set with `param0`, `param1` and `param2`. parameters. Get the above information by calling the List All eventRules endpoint. <br><br> **Important Note**<br> It is recommended that any changes made to the `Event Rules` are verified using the [List Portfolio Event Rules Endpoint](#listPortfolioEventRules) after the PUT call has been made.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMIndividualPortfolioManagementApi(pycsapi.ApiClient(configuration))
body = [pycsapi.ConnectMonitoringUpdateEventRulesBody()] # list[ConnectMonitoringUpdateEventRulesBody] | To ensure optimal processing efficiency when updating live event rules—whether for removal, addition, or status change—it is best practice to update the entire list of rules in a single operation.
portfolio_id = 1.2 # float | The unique identifier of the portfolio, obtained from `/portfolios`.
country_code = 'country_code_example' # str | Country code to show events for

try:
    # Update EventRules
    api_response = api_instance.update_event_rules(body, portfolio_id, country_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMIndividualPortfolioManagementApi->update_event_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[ConnectMonitoringUpdateEventRulesBody]**](ConnectMonitoringUpdateEventRulesBody.md)| To ensure optimal processing efficiency when updating live event rules—whether for removal, addition, or status change—it is best practice to update the entire list of rules in a single operation. | 
 **portfolio_id** | **float**| The unique identifier of the portfolio, obtained from &#x60;/portfolios&#x60;. | 
 **country_code** | **str**| Country code to show events for | 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


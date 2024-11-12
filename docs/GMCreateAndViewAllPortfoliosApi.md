# pycsapi.GMCreateAndViewAllPortfoliosApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_monitoring_portfolio**](GMCreateAndViewAllPortfoliosApi.md#create_monitoring_portfolio) | **POST** /monitoring/portfolios | Create Monitoring Portfolio
[**list_all_portfolios**](GMCreateAndViewAllPortfoliosApi.md#list_all_portfolios) | **GET** /monitoring/portfolios | List All Portfolios

# **create_monitoring_portfolio**
> ConnectMonitoringCreatePortfolioResponse create_monitoring_portfolio(body)

Create Monitoring Portfolio

This endpoint to create a new Portfolio based on the supplied criteria.<br><br> A portfolio can contain any number of companies that you wish to monitor changes to. The only required Body parameter is \"name\" for Connect users.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMCreateAndViewAllPortfoliosApi(pycsapi.ApiClient(configuration))
body = pycsapi.ConnectMonitoringCreatePortfolioRequest() # ConnectMonitoringCreatePortfolioRequest | 

try:
    # Create Monitoring Portfolio
    api_response = api_instance.create_monitoring_portfolio(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMCreateAndViewAllPortfoliosApi->create_monitoring_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectMonitoringCreatePortfolioRequest**](ConnectMonitoringCreatePortfolioRequest.md)|  | 

### Return type

[**ConnectMonitoringCreatePortfolioResponse**](ConnectMonitoringCreatePortfolioResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_portfolios**
> ConnectMonitoringListPortfolios list_all_portfolios(search_query=search_query, page=page, page_size=page_size)

List All Portfolios

This endpoint allows you to manage portfolios. You can use the GET method to retrieve all portfolios associated with the user.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMCreateAndViewAllPortfoliosApi(pycsapi.ApiClient(configuration))
search_query = 'search_query_example' # str | Return portfolios that match the given value (optional)
page = 0 # int | Starting page number inGlobal Monitoring is `0`. If all items are displayed on one page this can also be left blank. (optional) (default to 0)
page_size = 56 # int | Number of items to return per Page. (optional)

try:
    # List All Portfolios
    api_response = api_instance.list_all_portfolios(search_query=search_query, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMCreateAndViewAllPortfoliosApi->list_all_portfolios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_query** | **str**| Return portfolios that match the given value | [optional] 
 **page** | **int**| Starting page number inGlobal Monitoring is &#x60;0&#x60;. If all items are displayed on one page this can also be left blank. | [optional] [default to 0]
 **page_size** | **int**| Number of items to return per Page. | [optional] 

### Return type

[**ConnectMonitoringListPortfolios**](ConnectMonitoringListPortfolios.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


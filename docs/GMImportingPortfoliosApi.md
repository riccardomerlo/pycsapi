# pycsapi.GMImportingPortfoliosApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_a_portfolio_file**](GMImportingPortfoliosApi.md#import_a_portfolio_file) | **POST** /monitoring/portfolios/{portfolioId}/import | Import A Portfolio File
[**sync_a_portfolio_file**](GMImportingPortfoliosApi.md#sync_a_portfolio_file) | **POST** /monitoring/portfolios/{portfolioId}/sync | Sync A Portfolio File

# **import_a_portfolio_file**
> ConnectMonitoringImportAndSyncPortfolioResponse import_a_portfolio_file(importcsv, email, portfolio_id)

Import A Portfolio File

Endpoint allows you to import a list of companies to add to the selected portfolio along with some personal information for the company. Importing a portfolio will add the companies to the specified portfolio, duplicates in the import file will be ignored.You may also optionally add an email to the body of the request and get an email notification when the import is processed..

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMImportingPortfoliosApi(pycsapi.ApiClient(configuration))
importcsv = 'importcsv_example' # str | 
email = 'email_example' # str | 
portfolio_id = 1.2 # float | The unique identifier of the portfolio, obtained from `/portfolios`.

try:
    # Import A Portfolio File
    api_response = api_instance.import_a_portfolio_file(importcsv, email, portfolio_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMImportingPortfoliosApi->import_a_portfolio_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **importcsv** | **str**|  | 
 **email** | **str**|  | 
 **portfolio_id** | **float**| The unique identifier of the portfolio, obtained from &#x60;/portfolios&#x60;. | 

### Return type

[**ConnectMonitoringImportAndSyncPortfolioResponse**](ConnectMonitoringImportAndSyncPortfolioResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_a_portfolio_file**
> ConnectMonitoringImportAndSyncPortfolioResponse sync_a_portfolio_file(importcsv, email, portfolio_id)

Sync A Portfolio File

Endpoint allows you to sync a portfolio file with your portfolio. Sync action will delete all companies in your specified portfolio, and then add the companies from the file into the portfolio.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMImportingPortfoliosApi(pycsapi.ApiClient(configuration))
importcsv = 'importcsv_example' # str | 
email = 'email_example' # str | 
portfolio_id = 1.2 # float | The unique identifier of the portfolio, obtained from `/portfolios`.

try:
    # Sync A Portfolio File
    api_response = api_instance.sync_a_portfolio_file(importcsv, email, portfolio_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMImportingPortfoliosApi->sync_a_portfolio_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **importcsv** | **str**|  | 
 **email** | **str**|  | 
 **portfolio_id** | **float**| The unique identifier of the portfolio, obtained from &#x60;/portfolios&#x60;. | 

### Return type

[**ConnectMonitoringImportAndSyncPortfolioResponse**](ConnectMonitoringImportAndSyncPortfolioResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


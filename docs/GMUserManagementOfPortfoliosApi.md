# pycsapi.GMUserManagementOfPortfoliosApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copy_companies_between_portfolios**](GMUserManagementOfPortfoliosApi.md#copy_companies_between_portfolios) | **POST** /monitoring/portfolios/{portfolioId}/companies/copy | Copy Companies Between Portfolios
[**delete_portfolio**](GMUserManagementOfPortfoliosApi.md#delete_portfolio) | **DELETE** /monitoring/portfolios/{portfolioId} | Delete Portfolio
[**move_companies_between_portfolios**](GMUserManagementOfPortfoliosApi.md#move_companies_between_portfolios) | **POST** /monitoring/portfolios/{portfolioId}/companies/remove | Move Companies Between Portfolios
[**portfolio_user_permissions**](GMUserManagementOfPortfoliosApi.md#portfolio_user_permissions) | **GET** /monitoring/portfolios/{portfolioId}/sharingPermissions | Portfolio User Permissions
[**retrieve_portfolio_by_id**](GMUserManagementOfPortfoliosApi.md#retrieve_portfolio_by_id) | **GET** /monitoring/portfolios/{portfolioId} | Retrieve Portfolio By Id
[**share_portfolio_with_users**](GMUserManagementOfPortfoliosApi.md#share_portfolio_with_users) | **PATCH** /monitoring/portfolios/{portfolioId}/sharingPermissions | Share Portfolio With Users
[**update_portfolio_details**](GMUserManagementOfPortfoliosApi.md#update_portfolio_details) | **PATCH** /monitoring/portfolios/{portfolioId} | Update Portfolio Details

# **copy_companies_between_portfolios**
> ConnectMonitoringCopyAndMoveCompaniesResponse copy_companies_between_portfolios(body, portfolio_id, copy_all=copy_all)

Copy Companies Between Portfolios

This endpoint allows you to copy companies from one portfolio to another. You can specify the source and destination portfolios to perform the copy operation.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMUserManagementOfPortfoliosApi(pycsapi.ApiClient(configuration))
body = pycsapi.ConnectMonitoringCopyAndMoveCompaniesRequest() # ConnectMonitoringCopyAndMoveCompaniesRequest | 
portfolio_id = 1.2 # float | The unique identifier of the portfolio you want to copy companies from, obtained from `/portfolios`.
copy_all = false # bool | When CopyAll query parameter is False, portfolios and companies list needs to be passed. When CopyAll query parameter is True, only portfolios need to be passed and companies List must be empty. All companies are copied from current portfolio are considered here. (optional) (default to false)

try:
    # Copy Companies Between Portfolios
    api_response = api_instance.copy_companies_between_portfolios(body, portfolio_id, copy_all=copy_all)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMUserManagementOfPortfoliosApi->copy_companies_between_portfolios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectMonitoringCopyAndMoveCompaniesRequest**](ConnectMonitoringCopyAndMoveCompaniesRequest.md)|  | 
 **portfolio_id** | **float**| The unique identifier of the portfolio you want to copy companies from, obtained from &#x60;/portfolios&#x60;. | 
 **copy_all** | **bool**| When CopyAll query parameter is False, portfolios and companies list needs to be passed. When CopyAll query parameter is True, only portfolios need to be passed and companies List must be empty. All companies are copied from current portfolio are considered here. | [optional] [default to false]

### Return type

[**ConnectMonitoringCopyAndMoveCompaniesResponse**](ConnectMonitoringCopyAndMoveCompaniesResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_portfolio**
> ConnectMonitoringDeletePortfolio delete_portfolio(portfolio_id)

Delete Portfolio

This endpoint allows you to delete the portfolio using the portfolioId.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMUserManagementOfPortfoliosApi(pycsapi.ApiClient(configuration))
portfolio_id = 1.2 # float | The unique identifier of the portfolio that you wish to delete, obtained from `/portfolios`.

try:
    # Delete Portfolio
    api_response = api_instance.delete_portfolio(portfolio_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMUserManagementOfPortfoliosApi->delete_portfolio: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_id** | **float**| The unique identifier of the portfolio that you wish to delete, obtained from &#x60;/portfolios&#x60;. | 

### Return type

[**ConnectMonitoringDeletePortfolio**](ConnectMonitoringDeletePortfolio.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_companies_between_portfolios**
> ConnectMonitoringCopyAndMoveCompaniesResponse move_companies_between_portfolios(body, portfolio_id, remove_all=remove_all)

Move Companies Between Portfolios

This endpoint allows you to move companies from one portfolio to single (or) multiple portfolios. Removes the companies from the portfolio provided in the path parameter.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMUserManagementOfPortfoliosApi(pycsapi.ApiClient(configuration))
body = pycsapi.ConnectMonitoringCopyAndMoveCompaniesRequest() # ConnectMonitoringCopyAndMoveCompaniesRequest | 
portfolio_id = 1.2 # float | The unique identifier of the portfolio you want to move companies from, obtained from `/portfolios`.
remove_all = false # bool | When RemoveAll query parameter is False, a portfolios and companies list needs to be passed. When RemoveAll query parameter is True, only portfolios need to be passed and companies List must be empty. All companies are moved and deleted from current portfolio. (optional) (default to false)

try:
    # Move Companies Between Portfolios
    api_response = api_instance.move_companies_between_portfolios(body, portfolio_id, remove_all=remove_all)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMUserManagementOfPortfoliosApi->move_companies_between_portfolios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectMonitoringCopyAndMoveCompaniesRequest**](ConnectMonitoringCopyAndMoveCompaniesRequest.md)|  | 
 **portfolio_id** | **float**| The unique identifier of the portfolio you want to move companies from, obtained from &#x60;/portfolios&#x60;. | 
 **remove_all** | **bool**| When RemoveAll query parameter is False, a portfolios and companies list needs to be passed. When RemoveAll query parameter is True, only portfolios need to be passed and companies List must be empty. All companies are moved and deleted from current portfolio. | [optional] [default to false]

### Return type

[**ConnectMonitoringCopyAndMoveCompaniesResponse**](ConnectMonitoringCopyAndMoveCompaniesResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portfolio_user_permissions**
> ConnectMonitoringListSharingPermissions portfolio_user_permissions(portfolio_id)

Portfolio User Permissions

Retrieve user permissions within the customer for a portfolio.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMUserManagementOfPortfoliosApi(pycsapi.ApiClient(configuration))
portfolio_id = 1.2 # float | The unique identifier of the portfolio, obtained from `/portfolios`.

try:
    # Portfolio User Permissions
    api_response = api_instance.portfolio_user_permissions(portfolio_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMUserManagementOfPortfoliosApi->portfolio_user_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_id** | **float**| The unique identifier of the portfolio, obtained from &#x60;/portfolios&#x60;. | 

### Return type

[**ConnectMonitoringListSharingPermissions**](ConnectMonitoringListSharingPermissions.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_portfolio_by_id**
> ConnectMonitoringGetPortfolioById retrieve_portfolio_by_id(portfolio_id)

Retrieve Portfolio By Id

This endpoint allows you to retrieve the portfolio details from the portfolioId.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMUserManagementOfPortfoliosApi(pycsapi.ApiClient(configuration))
portfolio_id = 1.2 # float | The unique identifier for the portfolio that you wish to retrieve, obtained from `/portfolios`.

try:
    # Retrieve Portfolio By Id
    api_response = api_instance.retrieve_portfolio_by_id(portfolio_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMUserManagementOfPortfoliosApi->retrieve_portfolio_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_id** | **float**| The unique identifier for the portfolio that you wish to retrieve, obtained from &#x60;/portfolios&#x60;. | 

### Return type

[**ConnectMonitoringGetPortfolioById**](ConnectMonitoringGetPortfolioById.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_portfolio_with_users**
> ConnectMonitoringSharePortfolioRequestResponse share_portfolio_with_users(body, portfolio_id)

Share Portfolio With Users

Update/Create user permissions within the customer for portfolio.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMUserManagementOfPortfoliosApi(pycsapi.ApiClient(configuration))
body = pycsapi.ConnectMonitoringSharePortfolioRequest() # ConnectMonitoringSharePortfolioRequest | 
portfolio_id = 1.2 # float | The unique identifier of the portfolio, obtained from `/portfolios`.

try:
    # Share Portfolio With Users
    api_response = api_instance.share_portfolio_with_users(body, portfolio_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMUserManagementOfPortfoliosApi->share_portfolio_with_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectMonitoringSharePortfolioRequest**](ConnectMonitoringSharePortfolioRequest.md)|  | 
 **portfolio_id** | **float**| The unique identifier of the portfolio, obtained from &#x60;/portfolios&#x60;. | 

### Return type

[**ConnectMonitoringSharePortfolioRequestResponse**](ConnectMonitoringSharePortfolioRequestResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_portfolio_details**
> InlineResponse204 update_portfolio_details(body, portfolio_id)

Update Portfolio Details

This endpoint allows you to update Portfolio details such as Name, email recipients, language and subject line.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMUserManagementOfPortfoliosApi(pycsapi.ApiClient(configuration))
body = pycsapi.ConnectMonitoringUpdatePortfolioRequest() # ConnectMonitoringUpdatePortfolioRequest | 
portfolio_id = 1.2 # float | The unique identifier of the portfolio, obtained from `/portfolios`.

try:
    # Update Portfolio Details
    api_response = api_instance.update_portfolio_details(body, portfolio_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMUserManagementOfPortfoliosApi->update_portfolio_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectMonitoringUpdatePortfolioRequest**](ConnectMonitoringUpdatePortfolioRequest.md)|  | 
 **portfolio_id** | **float**| The unique identifier of the portfolio, obtained from &#x60;/portfolios&#x60;. | 

### Return type

[**InlineResponse204**](InlineResponse204.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


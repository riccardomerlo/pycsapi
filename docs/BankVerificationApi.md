# pycsapi.BankVerificationApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bank_verification_get_history_by_id**](BankVerificationApi.md#bank_verification_get_history_by_id) | **GET** /localSolutions/GB/bankVerification/history/{id} | Returns Request History By ID
[**bank_verification_get_history_list**](BankVerificationApi.md#bank_verification_get_history_list) | **GET** /localSolutions/GB/bankVerification/history | Requests Search History
[**bank_verification_search**](BankVerificationApi.md#bank_verification_search) | **POST** /localSolutions/GB/bankVerification/search | Single Request
[**bank_verification_update_history**](BankVerificationApi.md#bank_verification_update_history) | **PATCH** /localSolutions/GB/bankVerification/history/{id}/reference | Update CustomerReference by HistoryId
[**bank_verification_validate**](BankVerificationApi.md#bank_verification_validate) | **POST** /localSolutions/GB/bankVerification/validate/{id} | Validate Bank Verification Request

# **bank_verification_get_history_by_id**
> GBLocalSolutionGetHistoryRequestResponse bank_verification_get_history_by_id(id)

Returns Request History By ID

This endpoint will return details of a past request by id.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.BankVerificationApi(pycsapi.ApiClient(configuration))
id = 'id_example' # str | request id to fetch details

try:
    # Returns Request History By ID
    api_response = api_instance.bank_verification_get_history_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankVerificationApi->bank_verification_get_history_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| request id to fetch details | 

### Return type

[**GBLocalSolutionGetHistoryRequestResponse**](GBLocalSolutionGetHistoryRequestResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_verification_get_history_list**
> list[GBLocalSolutionGetHistoryListResponse] bank_verification_get_history_list(search_by_customer, customer_name=customer_name, match_result=match_result, date_from=date_from, date_to=date_to, account_type=account_type, customer_reference=customer_reference)

Requests Search History

Bank Verification History list Request<br><br> Note:- All property fields need to be submitted with the request, if information for a specific property is not needed, it is required to pass an empty string.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.BankVerificationApi(pycsapi.ApiClient(configuration))
search_by_customer = true # bool | A value of false will only search records for your account. If your account manager has configured your account to be able to view other users records within your company, a value of true will search all records made by all accounts within your company.
customer_name = 'customer_name_example' # str | Name of the customer returned by the supplier. (optional)
match_result = 'match_result_example' # str | Whether a match or not a match returned by the supplier. Values are 'Full', 'Close' and 'No Match'. (optional)
date_from = 'date_from_example' # str | Start date for filtering the results list by. (optional)
date_to = 'date_to_example' # str | End date for filtering the results list by. (optional)
account_type = 'account_type_example' # str | Type of account queried with the the supplier. Values are 'Business' and 'Personal'. (optional)
customer_reference = 'customer_reference_example' # str | Your Customer reference. (optional)

try:
    # Requests Search History
    api_response = api_instance.bank_verification_get_history_list(search_by_customer, customer_name=customer_name, match_result=match_result, date_from=date_from, date_to=date_to, account_type=account_type, customer_reference=customer_reference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankVerificationApi->bank_verification_get_history_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_by_customer** | **bool**| A value of false will only search records for your account. If your account manager has configured your account to be able to view other users records within your company, a value of true will search all records made by all accounts within your company. | 
 **customer_name** | **str**| Name of the customer returned by the supplier. | [optional] 
 **match_result** | **str**| Whether a match or not a match returned by the supplier. Values are &#x27;Full&#x27;, &#x27;Close&#x27; and &#x27;No Match&#x27;. | [optional] 
 **date_from** | **str**| Start date for filtering the results list by. | [optional] 
 **date_to** | **str**| End date for filtering the results list by. | [optional] 
 **account_type** | **str**| Type of account queried with the the supplier. Values are &#x27;Business&#x27; and &#x27;Personal&#x27;. | [optional] 
 **customer_reference** | **str**| Your Customer reference. | [optional] 

### Return type

[**list[GBLocalSolutionGetHistoryListResponse]**](GBLocalSolutionGetHistoryListResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_verification_search**
> GBLocalSolutionBankVerificationSearchResponse bank_verification_search(body=body)

Single Request

This endpoint will perform a search with the supplied data against a bank or building society.<br><br> NOTE:- This endpoint will charge when a successful request is made to a bank or building society. This endpoint will charge when a result is returned. This includes charging if the no match is found.<br><br> All property fields need to be submitted with the request, if information for a specific property is not needed, it is required to pass an empty string.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.BankVerificationApi(pycsapi.ApiClient(configuration))
body = pycsapi.GBLocalSolutionBankVerificationSearchRequest() # GBLocalSolutionBankVerificationSearchRequest |  (optional)

try:
    # Single Request
    api_response = api_instance.bank_verification_search(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankVerificationApi->bank_verification_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GBLocalSolutionBankVerificationSearchRequest**](GBLocalSolutionBankVerificationSearchRequest.md)|  | [optional] 

### Return type

[**GBLocalSolutionBankVerificationSearchResponse**](GBLocalSolutionBankVerificationSearchResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_verification_update_history**
> bank_verification_update_history(id, body=body)

Update CustomerReference by HistoryId

This endpoint will update the stored customerReference field of a past request with the provided ID.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.BankVerificationApi(pycsapi.ApiClient(configuration))
id = 'id_example' # str | The id of the history record
body = pycsapi.GBLocalSolutionCPHistoryRequestByIdRequest() # GBLocalSolutionCPHistoryRequestByIdRequest |  (optional)

try:
    # Update CustomerReference by HistoryId
    api_instance.bank_verification_update_history(id, body=body)
except ApiException as e:
    print("Exception when calling BankVerificationApi->bank_verification_update_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the history record | 
 **body** | [**GBLocalSolutionCPHistoryRequestByIdRequest**](GBLocalSolutionCPHistoryRequestByIdRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bank_verification_validate**
> InlineResponse2007 bank_verification_validate(id, body=body)

Validate Bank Verification Request

This endpoint will return whether the sort code and bank account number match the sort code and bank account number that was provided for the given single request.<br><br> Note:- A valid request requires all fields to exist in the request.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.BankVerificationApi(pycsapi.ApiClient(configuration))
id = 'id_example' # str | request id to fetch details
body = pycsapi.ValidateIdBody() # ValidateIdBody |  (optional)

try:
    # Validate Bank Verification Request
    api_response = api_instance.bank_verification_validate(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankVerificationApi->bank_verification_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| request id to fetch details | 
 **body** | [**ValidateIdBody**](ValidateIdBody.md)|  | [optional] 

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


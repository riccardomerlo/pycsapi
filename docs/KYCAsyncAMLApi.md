# pycsapi.KYCAsyncAMLApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compliancegetkycasyncamljobs**](KYCAsyncAMLApi.md#compliancegetkycasyncamljobs) | **GET** /compliance/kyc-protect/asyncAmlJobs | Return All Async AML Jobs
[**compliancegetkycasyncamljobsjobid**](KYCAsyncAMLApi.md#compliancegetkycasyncamljobsjobid) | **GET** /compliance/kyc-protect/asyncAmlJobs/{jobId} | Return Async AML Jobs By Id
[**compliancegetkycasyncamljobsjobidcriteria**](KYCAsyncAMLApi.md#compliancegetkycasyncamljobsjobidcriteria) | **GET** /compliance/kyc-protect/asyncAmlJobs/{jobId}/criteria | Return Async Job Criteria By Id

# **compliancegetkycasyncamljobs**
> GetKycProtectAsyncAmlJobResponse compliancegetkycasyncamljobs(page=page, page_size=page_size, statuses=statuses, target_type=target_type)

Return All Async AML Jobs

Gets a list of async aml jobs for user.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAsyncAMLApi(pycsapi.ApiClient(configuration))
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 10 # int | Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. (optional) (default to 10)
statuses = ['statuses_example'] # list[str] | The async job statuses. It can be the collection of created, processing, completed (optional)
target_type = 'target_type_example' # str | The async job's target type. It can be either Profile or KeyParty (optional)

try:
    # Return All Async AML Jobs
    api_response = api_instance.compliancegetkycasyncamljobs(page=page, page_size=page_size, statuses=statuses, target_type=target_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAsyncAMLApi->compliancegetkycasyncamljobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. | [optional] [default to 10]
 **statuses** | [**list[str]**](str.md)| The async job statuses. It can be the collection of created, processing, completed | [optional] 
 **target_type** | **str**| The async job&#x27;s target type. It can be either Profile or KeyParty | [optional] 

### Return type

[**GetKycProtectAsyncAmlJobResponse**](GetKycProtectAsyncAmlJobResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliancegetkycasyncamljobsjobid**
> GetKycProtectAsyncAmlJobItemResponse compliancegetkycasyncamljobsjobid(job_id, page=page, page_size=page_size)

Return Async AML Jobs By Id

Returns a list of async aml jobs for user.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAsyncAMLApi(pycsapi.ApiClient(configuration))
job_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the async aml job
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 10 # int | Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. (optional) (default to 10)

try:
    # Return Async AML Jobs By Id
    api_response = api_instance.compliancegetkycasyncamljobsjobid(job_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAsyncAMLApi->compliancegetkycasyncamljobsjobid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | [**str**](.md)| id of the async aml job | 
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. | [optional] [default to 10]

### Return type

[**GetKycProtectAsyncAmlJobItemResponse**](GetKycProtectAsyncAmlJobItemResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliancegetkycasyncamljobsjobidcriteria**
> GetKycProtectAsyncAmlJobCriteriaResponse compliancegetkycasyncamljobsjobidcriteria(job_id, page=page, page_size=page_size, statuses=statuses)

Return Async Job Criteria By Id

Gets a list of job criteria by async job id for user.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAsyncAMLApi(pycsapi.ApiClient(configuration))
job_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the async aml job
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 10 # int | Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. (optional) (default to 10)
statuses = ['statuses_example'] # list[str] | The async job criteria statuses. It can be the collection of submitted, processing, completed, failed. (optional)

try:
    # Return Async Job Criteria By Id
    api_response = api_instance.compliancegetkycasyncamljobsjobidcriteria(job_id, page=page, page_size=page_size, statuses=statuses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAsyncAMLApi->compliancegetkycasyncamljobsjobidcriteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | [**str**](.md)| id of the async aml job | 
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. | [optional] [default to 10]
 **statuses** | [**list[str]**](str.md)| The async job criteria statuses. It can be the collection of submitted, processing, completed, failed. | [optional] 

### Return type

[**GetKycProtectAsyncAmlJobCriteriaResponse**](GetKycProtectAsyncAmlJobCriteriaResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


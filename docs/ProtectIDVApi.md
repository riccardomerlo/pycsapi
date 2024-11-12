# pycsapi.ProtectIDVApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**idv_search**](ProtectIDVApi.md#idv_search) | **POST** /protect/idv/gdc/search | IDV Search
[**returns_idv_report**](ProtectIDVApi.md#returns_idv_report) | **GET** /protect/idv/file | Returns IDV Report

# **idv_search**
> IdvResponseDto idv_search(body)

IDV Search

Creates a search request for a GDC IDV search.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectIDVApi(pycsapi.ApiClient(configuration))
body = pycsapi.IdvRequestDto() # IdvRequestDto | 

try:
    # IDV Search
    api_response = api_instance.idv_search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectIDVApi->idv_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdvRequestDto**](IdvRequestDto.md)|  | 

### Return type

[**IdvResponseDto**](IdvResponseDto.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, text/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **returns_idv_report**
> str returns_idv_report(idv_search_id=idv_search_id)

Returns IDV Report

Returns an IDV Report with the potential results and the sources they were matched against.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectIDVApi(pycsapi.ApiClient(configuration))
idv_search_id = 'idv_search_id_example' # str |  (optional)

try:
    # Returns IDV Report
    api_response = api_instance.returns_idv_report(idv_search_id=idv_search_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectIDVApi->returns_idv_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idv_search_id** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


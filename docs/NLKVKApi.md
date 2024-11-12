# pycsapi.NLKVKApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extract_nl_kvk_number**](NLKVKApi.md#extract_nl_kvk_number) | **GET** /localSolutions/NL/extract/{kvkNumber} | Return NL Extract

# **extract_nl_kvk_number**
> str extract_nl_kvk_number(kvk_number)

Return NL Extract

NL extract from KVK Number

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.NLKVKApi(pycsapi.ApiClient(configuration))
kvk_number = 'kvk_number_example' # str | kvkNumber to fetch details

try:
    # Return NL Extract
    api_response = api_instance.extract_nl_kvk_number(kvk_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NLKVKApi->extract_nl_kvk_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kvk_number** | **str**| kvkNumber to fetch details | 

### Return type

**str**

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


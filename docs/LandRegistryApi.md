# pycsapi.LandRegistryApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gb_land_registry**](LandRegistryApi.md#gb_land_registry) | **GET** /localSolutions/GB/landRegistry/{companyId} | GB Land Registry

# **gb_land_registry**
> CreditsafeLocalSolutionsGBLandRegistry gb_land_registry(company_id, language=language, page=page, page_size=page_size)

GB Land Registry

Allows users to return Land Registry details of a company.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.LandRegistryApi(pycsapi.ApiClient(configuration))
company_id = 'company_id_example' # str | A company Safe Number or Connect ID.
language = 'en' # str | language the report is requested in. (optional) (default to en)
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 56 # int | Number of items to return per Page. (optional)

try:
    # GB Land Registry
    api_response = api_instance.gb_land_registry(company_id, language=language, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LandRegistryApi->gb_land_registry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| A company Safe Number or Connect ID. | 
 **language** | **str**| language the report is requested in. | [optional] [default to en]
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Number of items to return per Page. | [optional] 

### Return type

[**CreditsafeLocalSolutionsGBLandRegistry**](CreditsafeLocalSolutionsGBLandRegistry.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


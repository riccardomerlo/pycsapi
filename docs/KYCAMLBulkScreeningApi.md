# pycsapi.KYCAMLBulkScreeningApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compliancepostkycsearchesbulkbyprofileid**](KYCAMLBulkScreeningApi.md#compliancepostkycsearchesbulkbyprofileid) | **POST** /compliance/kyc-protect/profiles/{profileId}/searches/bulk | Perform Bulk AML Screening

# **compliancepostkycsearchesbulkbyprofileid**
> compliancepostkycsearchesbulkbyprofileid(profile_id, body=body)

Perform Bulk AML Screening

Request multiple searches to be performed and linked to a profile asynchronously

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLBulkScreeningApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile
body = pycsapi.SearchesBulkBody1() # SearchesBulkBody1 |  (optional)

try:
    # Perform Bulk AML Screening
    api_instance.compliancepostkycsearchesbulkbyprofileid(profile_id, body=body)
except ApiException as e:
    print("Exception when calling KYCAMLBulkScreeningApi->compliancepostkycsearchesbulkbyprofileid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| id of the profile | 
 **body** | [**SearchesBulkBody1**](SearchesBulkBody1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


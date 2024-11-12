# pycsapi.KYCAuditApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compliance_get_kyc_audits**](KYCAuditApi.md#compliance_get_kyc_audits) | **GET** /compliance/kyc-protect/audits | Return Audit Trail

# **compliance_get_kyc_audits**
> GetAuditsResponse compliance_get_kyc_audits(profile_ids=profile_ids, categories=categories, subcategories=subcategories, actions=actions, user_ids=user_ids, start_date=start_date, end_date=end_date, page=page, page_size=page_size)

Return Audit Trail

Returns a list of audits which can be filtered by various categories.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAuditApi(pycsapi.ApiClient(configuration))
profile_ids = ['profile_ids_example'] # list[str] | Select the profileId's for the filter. (optional)
categories = ['categories_example'] # list[str] | Available categories for the filter. (optional)
subcategories = ['subcategories_example'] # list[str] | Available subcategories for the filter. (optional)
actions = ['actions_example'] # list[str] | Available actions for the filter. (optional)
user_ids = [56] # list[int] | User Ids for the filter. (optional)
start_date = '2013-10-20' # date | Start date for the filter. (optional)
end_date = '2013-10-20' # date | End date for the filter. (optional)
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 10 # int | Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. (optional) (default to 10)

try:
    # Return Audit Trail
    api_response = api_instance.compliance_get_kyc_audits(profile_ids=profile_ids, categories=categories, subcategories=subcategories, actions=actions, user_ids=user_ids, start_date=start_date, end_date=end_date, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAuditApi->compliance_get_kyc_audits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_ids** | [**list[str]**](str.md)| Select the profileId&#x27;s for the filter. | [optional] 
 **categories** | [**list[str]**](str.md)| Available categories for the filter. | [optional] 
 **subcategories** | [**list[str]**](str.md)| Available subcategories for the filter. | [optional] 
 **actions** | [**list[str]**](str.md)| Available actions for the filter. | [optional] 
 **user_ids** | [**list[int]**](int.md)| User Ids for the filter. | [optional] 
 **start_date** | **date**| Start date for the filter. | [optional] 
 **end_date** | **date**| End date for the filter. | [optional] 
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. | [optional] [default to 10]

### Return type

[**GetAuditsResponse**](GetAuditsResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


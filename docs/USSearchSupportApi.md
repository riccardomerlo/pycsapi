# pycsapi.USSearchSupportApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_freshinvestigation_for_us_country**](USSearchSupportApi.md#create_freshinvestigation_for_us_country) | **POST** /localSolutions/US/searchSupport | US Fresh Investigation Request

# **create_freshinvestigation_for_us_country**
> CreditsafeUSLocalFIResponse create_freshinvestigation_for_us_country(attachment=attachment, fi_body=fi_body, operation_type=operation_type)

US Fresh Investigation Request

Places an order for a Fresh Investigation (Offline Report). Providing as much detail as possible about the Company, our team will use official sources and registries to quickly answer questions about a company's stability and financial health. Fresh Investigations take 5.5 days on average to complete. By adding `consent:true` to the request, you are allowing Creditsafe to disclose your company details to the company you have requested the Investigation against, to be used only in the aim of improving our Investigation report.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.USSearchSupportApi(pycsapi.ApiClient(configuration))
attachment = 'attachment_example' # str |  (optional)
fi_body = pycsapi.ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody() # ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody |  (optional)
operation_type = 'operation_type_example' # str | type of check (optional)

try:
    # US Fresh Investigation Request
    api_response = api_instance.create_freshinvestigation_for_us_country(attachment=attachment, fi_body=fi_body, operation_type=operation_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling USSearchSupportApi->create_freshinvestigation_for_us_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachment** | **str**|  | [optional] 
 **fi_body** | [**ConnectUSLocalSolutionsFreshInvCreateInvestigationFormDataFiBody**](.md)|  | [optional] 
 **operation_type** | **str**| type of check | [optional] 

### Return type

[**CreditsafeUSLocalFIResponse**](CreditsafeUSLocalFIResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


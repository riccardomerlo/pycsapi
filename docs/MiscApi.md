# pycsapi.MiscApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**custom_report_parameters**](MiscApi.md#custom_report_parameters) | **GET** /reportcustomdata/{country} | Custom Report Parameters
[**report_schema**](MiscApi.md#report_schema) | **GET** /companies/schema/{countryCode} | Report Schema

# **custom_report_parameters**
> object custom_report_parameters(country)

Custom Report Parameters

Returns the allowed values of the customData parameter, used in the GET Company Report and Director Report endpoints.  I.e. Supplying `DE` as a country code will return a list of reasons for requesting a DE Credit Report (a legal requirement to supply with each Credit Report request in Germany). This will provide a list of allowedValues to enter into the mandatory Parameter `customData` = `de_reason_code::allowedValue`.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.MiscApi(pycsapi.ApiClient(configuration))
country = 'country_example' # str | An ISO/Alpha-2 country code to display any special mandatory parameters when ordering a Credit Report in that territory.

try:
    # Custom Report Parameters
    api_response = api_instance.custom_report_parameters(country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscApi->custom_report_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| An ISO/Alpha-2 country code to display any special mandatory parameters when ordering a Credit Report in that territory. | 

### Return type

**object**

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_schema**
> object report_schema(country_code, section=section, template=template)

Report Schema

Returns the Company Report JSON schema of the provided country. Largely redundant as the Company Report 200 response is defined as a superset of all country's JSON schemas and can be used for any country.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.MiscApi(pycsapi.ApiClient(configuration))
country_code = 'country_code_example' # str | ISO2 / Alpha 2 Country Code
section = 'section_example' # str | Use CompanyReportResponse for the Company Credit Report JSON schema, DirectorReportResponse for the Director Report JSON schema. (optional)
template = 'template_example' # str | For Templated Company Report JSON Schemas (optional)

try:
    # Report Schema
    api_response = api_instance.report_schema(country_code, section=section, template=template)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiscApi->report_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| ISO2 / Alpha 2 Country Code | 
 **section** | **str**| Use CompanyReportResponse for the Company Credit Report JSON schema, DirectorReportResponse for the Director Report JSON schema. | [optional] 
 **template** | **str**| For Templated Company Report JSON Schemas | [optional] 

### Return type

**object**

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


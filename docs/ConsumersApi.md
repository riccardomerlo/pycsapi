# pycsapi.ConsumersApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consumer_report**](ConsumersApi.md#consumer_report) | **GET** /consumers | Consumer Report
[**consumer_search_criteria**](ConsumersApi.md#consumer_search_criteria) | **GET** /consumers/searchcriteria | Consumer Search Criteria

# **consumer_report**
> InlineResponse2005 consumer_report(countries, first_name, last_name, street, house_no, city, post_code, language=language, date_of_birth=date_of_birth, custom_data=custom_data, call_ref=call_ref)

Consumer Report

Consumer Search and Report endpoint. When sufficient information has been provided to filter potential Consumer results down to one record then the Consumer Report will be returned.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ConsumersApi(pycsapi.ApiClient(configuration))
countries = pycsapi.CreditsafeGlobalDataCountryCode() # CreditsafeGlobalDataCountryCode | ISO-2 country code
first_name = 'first_name_example' # str | Consumer's First Name
last_name = 'last_name_example' # str | Consumer's Last Name
street = 'street_example' # str | Address part identifier - Street of the Consumer
house_no = 'house_no_example' # str | Address part identifier - House/Building Number of the Consumer
city = 'city_example' # str | Address part identifier - City of the Consumer
post_code = 'post_code_example' # str | Address part identifier - Postcode/Zip Code of the Consumer
language = 'EN' # str |  (optional) (default to EN)
date_of_birth = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
custom_data = 'custom_data_example' # str |  (optional)
call_ref = 'call_ref_example' # str | This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions. (optional)

try:
    # Consumer Report
    api_response = api_instance.consumer_report(countries, first_name, last_name, street, house_no, city, post_code, language=language, date_of_birth=date_of_birth, custom_data=custom_data, call_ref=call_ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsumersApi->consumer_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countries** | [**CreditsafeGlobalDataCountryCode**](.md)| ISO-2 country code | 
 **first_name** | **str**| Consumer&#x27;s First Name | 
 **last_name** | **str**| Consumer&#x27;s Last Name | 
 **street** | **str**| Address part identifier - Street of the Consumer | 
 **house_no** | **str**| Address part identifier - House/Building Number of the Consumer | 
 **city** | **str**| Address part identifier - City of the Consumer | 
 **post_code** | **str**| Address part identifier - Postcode/Zip Code of the Consumer | 
 **language** | **str**|  | [optional] [default to EN]
 **date_of_birth** | **datetime**|  | [optional] 
 **custom_data** | **str**|  | [optional] 
 **call_ref** | **str**| This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions. | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **consumer_search_criteria**
> list[object] consumer_search_criteria(countries, call_ref=call_ref)

Consumer Search Criteria

Returns country specific fields that can be used to search for a Consumer.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ConsumersApi(pycsapi.ApiClient(configuration))
countries = 'countries_example' # str | Comma-separated list of ISO-2 country codes
call_ref = 'call_ref_example' # str | This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions. (optional)

try:
    # Consumer Search Criteria
    api_response = api_instance.consumer_search_criteria(countries, call_ref=call_ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConsumersApi->consumer_search_criteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countries** | **str**| Comma-separated list of ISO-2 country codes | 
 **call_ref** | **str**| This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions. | [optional] 

### Return type

**list[object]**

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


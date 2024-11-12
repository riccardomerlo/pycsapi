# pycsapi.PeopleDirectorsApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**director_report**](PeopleDirectorsApi.md#director_report) | **GET** /people/{peopleId} | Director Report
[**director_s_search**](PeopleDirectorsApi.md#director_s_search) | **GET** /people | Director Search
[**people_director_search_criteria**](PeopleDirectorsApi.md#people_director_search_criteria) | **GET** /people/searchcriteria | People/Director Search Criteria

# **director_report**
> CreditsafeGlobalDataReportsDirectorsDirectorReportResponse director_report(people_id, language=language, call_ref=call_ref)

Director Report

Returns a report from the ID supplied to the search.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.PeopleDirectorsApi(pycsapi.ApiClient(configuration))
people_id = 'people_id_example' # str | Identifier of the Person/Director required to order their Director Report. Obtained from `/people` search results.
language = 'en' # str | Report Language - The JSON structure of the Report is language invariant, but field content will return as the given language, where available. (optional) (default to en)
call_ref = 'call_ref_example' # str | This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions. (optional)

try:
    # Director Report
    api_response = api_instance.director_report(people_id, language=language, call_ref=call_ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleDirectorsApi->director_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **people_id** | **str**| Identifier of the Person/Director required to order their Director Report. Obtained from &#x60;/people&#x60; search results. | 
 **language** | **str**| Report Language - The JSON structure of the Report is language invariant, but field content will return as the given language, where available. | [optional] [default to en]
 **call_ref** | **str**| This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions. | [optional] 

### Return type

[**CreditsafeGlobalDataReportsDirectorsDirectorReportResponse**](CreditsafeGlobalDataReportsDirectorsDirectorReportResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **director_s_search**
> InlineResponse2002 director_s_search(countries, page=page, page_size=page_size, people_id=people_id, first_name=first_name, last_name=last_name, local_director_number=local_director_number, date_of_birth=date_of_birth, call_ref=call_ref)

Director Search

Endpoint to find Directors based on search criteria to order a Creditsafe Director Report.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.PeopleDirectorsApi(pycsapi.ApiClient(configuration))
countries = [pycsapi.CreditsafeGlobalDataCountryCode()] # list[CreditsafeGlobalDataCountryCode] | comma-separated list of iso-2 country codes
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 56 # int | Number of items to return per Page. (optional)
people_id = 'people_id_example' # str | Person/Director Identifier - used to order a Director Report. (optional)
first_name = 'first_name_example' # str | Person's First Name. (optional)
last_name = 'last_name_example' # str | Person's Last Name (optional)
local_director_number = 'local_director_number_example' # str | Local Identifier of the Director, the PNR in GB. (optional)
date_of_birth = 'date_of_birth_example' # str | Person DOB - provide YYYY-MM-DD or YYYY-MM format. (optional)
call_ref = 'call_ref_example' # str | This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions. (optional)

try:
    # Director Search
    api_response = api_instance.director_s_search(countries, page=page, page_size=page_size, people_id=people_id, first_name=first_name, last_name=last_name, local_director_number=local_director_number, date_of_birth=date_of_birth, call_ref=call_ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleDirectorsApi->director_s_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countries** | [**list[CreditsafeGlobalDataCountryCode]**](CreditsafeGlobalDataCountryCode.md)| comma-separated list of iso-2 country codes | 
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Number of items to return per Page. | [optional] 
 **people_id** | **str**| Person/Director Identifier - used to order a Director Report. | [optional] 
 **first_name** | **str**| Person&#x27;s First Name. | [optional] 
 **last_name** | **str**| Person&#x27;s Last Name | [optional] 
 **local_director_number** | **str**| Local Identifier of the Director, the PNR in GB. | [optional] 
 **date_of_birth** | **str**| Person DOB - provide YYYY-MM-DD or YYYY-MM format. | [optional] 
 **call_ref** | **str**| This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions. | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_director_search_criteria**
> CreditsafeGlobalDataSearchCriteriaSchemaSetDirector people_director_search_criteria(countries=countries)

People/Director Search Criteria

Returns the set of available People Search parameters/fields for a provided list of countries.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.PeopleDirectorsApi(pycsapi.ApiClient(configuration))
countries = 'countries_example' # str | A comma separated list of ISO/Alpha 2 format country codes, or singular country Code. e.g. US,GB will return the common searchable People/Director fields in the United States and Great Britain. (optional)

try:
    # People/Director Search Criteria
    api_response = api_instance.people_director_search_criteria(countries=countries)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PeopleDirectorsApi->people_director_search_criteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countries** | **str**| A comma separated list of ISO/Alpha 2 format country codes, or singular country Code. e.g. US,GB will return the common searchable People/Director fields in the United States and Great Britain. | [optional] 

### Return type

[**CreditsafeGlobalDataSearchCriteriaSchemaSetDirector**](CreditsafeGlobalDataSearchCriteriaSchemaSetDirector.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


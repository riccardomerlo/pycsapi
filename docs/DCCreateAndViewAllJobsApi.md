# pycsapi.DCCreateAndViewAllJobsApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job**](DCCreateAndViewAllJobsApi.md#create_job) | **POST** /dataCleaning/jobs | Create Job Request
[**get_all_jobs**](DCCreateAndViewAllJobsApi.md#get_all_jobs) | **GET** /dataCleaning/jobs | Returns all Data Cleaning Jobs

# **create_job**
> ConnectDataCleaningJob create_job(body)

Create Job Request

Enter a name for the 'Job Request' to be associated to the file going to be processed.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.DCCreateAndViewAllJobsApi(pycsapi.ApiClient(configuration))
body = pycsapi.ConnectDataCleaningCreateJobRequest() # ConnectDataCleaningCreateJobRequest | 

try:
    # Create Job Request
    api_response = api_instance.create_job(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DCCreateAndViewAllJobsApi->create_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectDataCleaningCreateJobRequest**](ConnectDataCleaningCreateJobRequest.md)|  | 

### Return type

[**ConnectDataCleaningJob**](ConnectDataCleaningJob.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application:json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_jobs**
> ArrayOfConnectDataCleaningJob get_all_jobs(countries=countries, status=status, job_name=job_name, from_date=from_date, customer_id=customer_id, to_date=to_date, user_id=user_id, page_size=page_size, company_name=company_name, page=page, archived=archived)

Returns all Data Cleaning Jobs

This endpoint can be used to retrieve all created data cleaning job requests as defined by the query parameters.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.DCCreateAndViewAllJobsApi(pycsapi.ApiClient(configuration))
countries = 'countries_example' # str | Comma separated list of ISO/Alpha-2 country codes to filter the results by. (optional)
status = 'status_example' # str | Returns the individual jobs by status. Possible values are: `pending`, `processing`, `completed`, `failed`. (optional)
job_name = 'job_name_example' # str | Returns the individual jobs by name. (optional)
from_date = 56 # int | Returns the individual jobs created after the specified date. (optional)
customer_id = 56 # int | Returns the individual jobs by customer id. (optional)
to_date = 56 # int | Returns the individual jobs created before the specified date. (optional)
user_id = 56 # int | Returns the individual jobs by user id. (optional)
page_size = 56 # int | Returns the number of individual jobs per page. (optional)
company_name = 'company_name_example' # str | Returns the individual jobs by company name. (optional)
page = 56 # int | Returns the page number of the individual jobs. (optional)
archived = true # bool | Returns the individual jobs by archived status. (optional)

try:
    # Returns all Data Cleaning Jobs
    api_response = api_instance.get_all_jobs(countries=countries, status=status, job_name=job_name, from_date=from_date, customer_id=customer_id, to_date=to_date, user_id=user_id, page_size=page_size, company_name=company_name, page=page, archived=archived)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DCCreateAndViewAllJobsApi->get_all_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countries** | **str**| Comma separated list of ISO/Alpha-2 country codes to filter the results by. | [optional] 
 **status** | **str**| Returns the individual jobs by status. Possible values are: &#x60;pending&#x60;, &#x60;processing&#x60;, &#x60;completed&#x60;, &#x60;failed&#x60;. | [optional] 
 **job_name** | **str**| Returns the individual jobs by name. | [optional] 
 **from_date** | **int**| Returns the individual jobs created after the specified date. | [optional] 
 **customer_id** | **int**| Returns the individual jobs by customer id. | [optional] 
 **to_date** | **int**| Returns the individual jobs created before the specified date. | [optional] 
 **user_id** | **int**| Returns the individual jobs by user id. | [optional] 
 **page_size** | **int**| Returns the number of individual jobs per page. | [optional] 
 **company_name** | **str**| Returns the individual jobs by company name. | [optional] 
 **page** | **int**| Returns the page number of the individual jobs. | [optional] 
 **archived** | **bool**| Returns the individual jobs by archived status. | [optional] 

### Return type

[**ArrayOfConnectDataCleaningJob**](ArrayOfConnectDataCleaningJob.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


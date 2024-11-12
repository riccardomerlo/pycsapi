# pycsapi.ProtectSchedulesApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_protect_schedule**](ProtectSchedulesApi.md#create_protect_schedule) | **POST** /protect/schedules | Create Protect Schedule
[**deletes_schedule_from_investigation**](ProtectSchedulesApi.md#deletes_schedule_from_investigation) | **DELETE** /protect/schedules/{id} | Deletes Schedule from Investigation
[**retrieve_schedule_by_id**](ProtectSchedulesApi.md#retrieve_schedule_by_id) | **GET** /protect/schedules/{id} | Retrieve Schedule By Id
[**updates_schedule**](ProtectSchedulesApi.md#updates_schedule) | **PUT** /protect/schedules/{id} |  Updates Schedule

# **create_protect_schedule**
> ConnectProtectSchedule create_protect_schedule(body)

Create Protect Schedule

Creates a Schedule to check against new sanctions that effect your chosen Investigation. <br>The frequency of the schedule is set to 'daily' as a default.<br><br> To receive notifications of alerts you need to follow this POST call with PUT/Update Schedules to set the 'isEmailRequired' to `true`.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectSchedulesApi(pycsapi.ApiClient(configuration))
body = pycsapi.ConnectProtectCreateScheduleRequest() # ConnectProtectCreateScheduleRequest | 

try:
    # Create Protect Schedule
    api_response = api_instance.create_protect_schedule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectSchedulesApi->create_protect_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectProtectCreateScheduleRequest**](ConnectProtectCreateScheduleRequest.md)|  | 

### Return type

[**ConnectProtectSchedule**](ConnectProtectSchedule.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletes_schedule_from_investigation**
> deletes_schedule_from_investigation(id)

Deletes Schedule from Investigation

Deletes a Schedule from an Investigation meaning entity will no longer be monitored on a nightly basis but record will still remain in the audit trail.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectSchedulesApi(pycsapi.ApiClient(configuration))
id = 'id_example' # str | Enter the schedule id.

try:
    # Deletes Schedule from Investigation
    api_instance.deletes_schedule_from_investigation(id)
except ApiException as e:
    print("Exception when calling ProtectSchedulesApi->deletes_schedule_from_investigation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Enter the schedule id. | 

### Return type

void (empty response body)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_schedule_by_id**
> ConnectProtectSchedule retrieve_schedule_by_id(id)

Retrieve Schedule By Id

Endpoint to retrieve a specific Schedule by Id. A Schedule Id can be retrieved from the associated Investigation.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectSchedulesApi(pycsapi.ApiClient(configuration))
id = 'id_example' # str | Enter the schedule id.

try:
    # Retrieve Schedule By Id
    api_response = api_instance.retrieve_schedule_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectSchedulesApi->retrieve_schedule_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Enter the schedule id. | 

### Return type

[**ConnectProtectSchedule**](ConnectProtectSchedule.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updates_schedule**
> Schedule updates_schedule(body, id)

 Updates Schedule

Endpoint will update the details around the schedule.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectSchedulesApi(pycsapi.ApiClient(configuration))
body = pycsapi.CreateScheduleDto() # CreateScheduleDto | 
id = 'id_example' # str | Enter the schedule id.

try:
    #  Updates Schedule
    api_response = api_instance.updates_schedule(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectSchedulesApi->updates_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateScheduleDto**](CreateScheduleDto.md)|  | 
 **id** | **str**| Enter the schedule id. | 

### Return type

[**Schedule**](Schedule.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


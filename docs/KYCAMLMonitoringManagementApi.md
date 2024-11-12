# pycsapi.KYCAMLMonitoringManagementApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**k_yc_protect_create_schedule**](KYCAMLMonitoringManagementApi.md#k_yc_protect_create_schedule) | **POST** /compliance/kyc-protect/schedules | Add Search To AML Monitoring
[**k_yc_protect_delete_schedules**](KYCAMLMonitoringManagementApi.md#k_yc_protect_delete_schedules) | **DELETE** /compliance/kyc-protect/schedules | Delete Searches From AML Monitoring
[**k_yc_protect_delete_schedules_by_schedule_id**](KYCAMLMonitoringManagementApi.md#k_yc_protect_delete_schedules_by_schedule_id) | **DELETE** /compliance/kyc-protect/schedules/{scheduleId} | Delete A Search From AML Monitoring
[**k_yc_protect_get_schedules**](KYCAMLMonitoringManagementApi.md#k_yc_protect_get_schedules) | **GET** /compliance/kyc-protect/schedules | Return All Ordered Schedules
[**k_yc_protect_get_schedules_aml_alerts**](KYCAMLMonitoringManagementApi.md#k_yc_protect_get_schedules_aml_alerts) | **GET** /compliance/kyc-protect/schedules/amlAlerts | Return All Hits For A Schedule By Created Date
[**k_yc_protect_put_schedules**](KYCAMLMonitoringManagementApi.md#k_yc_protect_put_schedules) | **PUT** /compliance/kyc-protect/schedules | Update Schedules
[**k_yc_protect_put_schedules_by_schedule_id**](KYCAMLMonitoringManagementApi.md#k_yc_protect_put_schedules_by_schedule_id) | **PUT** /compliance/kyc-protect/schedules/{scheduleId} | Update A Schedule In Monitoring
[**kycprotectgetschedulesbyscheduleid**](KYCAMLMonitoringManagementApi.md#kycprotectgetschedulesbyscheduleid) | **GET** /compliance/kyc-protect/schedules/{scheduleId} | Returns A Schedule

# **k_yc_protect_create_schedule**
> PostKYCProtectSchedulesResponse k_yc_protect_create_schedule(body=body)

Add Search To AML Monitoring

Adds the specified searches to AML monitoring, i.e. schedules them for screening. If thresholds and datasets are amended from the original search, new results will generated. Any existing hits will be overridden and any previous match decisions will be reset.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLMonitoringManagementApi(pycsapi.ApiClient(configuration))
body = pycsapi.KycprotectSchedulesBody() # KycprotectSchedulesBody |  (optional)

try:
    # Add Search To AML Monitoring
    api_response = api_instance.k_yc_protect_create_schedule(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLMonitoringManagementApi->k_yc_protect_create_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KycprotectSchedulesBody**](KycprotectSchedulesBody.md)|  | [optional] 

### Return type

[**PostKYCProtectSchedulesResponse**](PostKYCProtectSchedulesResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_yc_protect_delete_schedules**
> DeleteKYCProtectSchedulesResponse k_yc_protect_delete_schedules(body=body)

Delete Searches From AML Monitoring

Removes the specified searches from AML monitoring.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLMonitoringManagementApi(pycsapi.ApiClient(configuration))
body = pycsapi.KycprotectSchedulesBody1() # KycprotectSchedulesBody1 |  (optional)

try:
    # Delete Searches From AML Monitoring
    api_response = api_instance.k_yc_protect_delete_schedules(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLMonitoringManagementApi->k_yc_protect_delete_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KycprotectSchedulesBody1**](KycprotectSchedulesBody1.md)|  | [optional] 

### Return type

[**DeleteKYCProtectSchedulesResponse**](DeleteKYCProtectSchedulesResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_yc_protect_delete_schedules_by_schedule_id**
> k_yc_protect_delete_schedules_by_schedule_id(schedule_id)

Delete A Search From AML Monitoring

Removes a search from AML monitoring.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLMonitoringManagementApi(pycsapi.ApiClient(configuration))
schedule_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile

try:
    # Delete A Search From AML Monitoring
    api_instance.k_yc_protect_delete_schedules_by_schedule_id(schedule_id)
except ApiException as e:
    print("Exception when calling KYCAMLMonitoringManagementApi->k_yc_protect_delete_schedules_by_schedule_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | [**str**](.md)| id of the profile | 

### Return type

void (empty response body)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_yc_protect_get_schedules**
> ScheduleResponse k_yc_protect_get_schedules(page=page, page_size=page_size)

Return All Ordered Schedules

Returns all schedules ordered by modified date.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLMonitoringManagementApi(pycsapi.ApiClient(configuration))
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 10 # int | Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. (optional) (default to 10)

try:
    # Return All Ordered Schedules
    api_response = api_instance.k_yc_protect_get_schedules(page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLMonitoringManagementApi->k_yc_protect_get_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. | [optional] [default to 10]

### Return type

[**ScheduleResponse**](ScheduleResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_yc_protect_get_schedules_aml_alerts**
> KYCProtectScheduleHitResponse k_yc_protect_get_schedules_aml_alerts(page=page, page_size=page_size, hit_decisions=hit_decisions)

Return All Hits For A Schedule By Created Date

Get all hits for an AML monitoring schedule ordered by hit created date.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLMonitoringManagementApi(pycsapi.ApiClient(configuration))
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 10 # int | Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. (optional) (default to 10)
hit_decisions = ['hit_decisions_example'] # list[str] | The hit decisions to filter by. It can be the collection of undecided, truematch, falsepositive, discarded (optional)

try:
    # Return All Hits For A Schedule By Created Date
    api_response = api_instance.k_yc_protect_get_schedules_aml_alerts(page=page, page_size=page_size, hit_decisions=hit_decisions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLMonitoringManagementApi->k_yc_protect_get_schedules_aml_alerts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. | [optional] [default to 10]
 **hit_decisions** | [**list[str]**](str.md)| The hit decisions to filter by. It can be the collection of undecided, truematch, falsepositive, discarded | [optional] 

### Return type

[**KYCProtectScheduleHitResponse**](KYCProtectScheduleHitResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_yc_protect_put_schedules**
> PutKYCProtectSchedulesResponse k_yc_protect_put_schedules(body=body)

Update Schedules

Updates schedules in AML monitoring.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLMonitoringManagementApi(pycsapi.ApiClient(configuration))
body = pycsapi.MODEL1e2683() # MODEL1e2683 |  (optional)

try:
    # Update Schedules
    api_response = api_instance.k_yc_protect_put_schedules(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLMonitoringManagementApi->k_yc_protect_put_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MODEL1e2683**](MODEL1e2683.md)|  | [optional] 

### Return type

[**PutKYCProtectSchedulesResponse**](PutKYCProtectSchedulesResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_yc_protect_put_schedules_by_schedule_id**
> MODEL1c736e k_yc_protect_put_schedules_by_schedule_id(schedule_id, body=body)

Update A Schedule In Monitoring

Updates a schedule in AML monitoring. <br><br> When there is a change in threshold or datasets, the system will deduct one credit for screening.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLMonitoringManagementApi(pycsapi.ApiClient(configuration))
schedule_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile
body = pycsapi.MODEL6bcc20() # MODEL6bcc20 |  (optional)

try:
    # Update A Schedule In Monitoring
    api_response = api_instance.k_yc_protect_put_schedules_by_schedule_id(schedule_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLMonitoringManagementApi->k_yc_protect_put_schedules_by_schedule_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | [**str**](.md)| id of the profile | 
 **body** | [**MODEL6bcc20**](MODEL6bcc20.md)|  | [optional] 

### Return type

[**MODEL1c736e**](MODEL1c736e.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kycprotectgetschedulesbyscheduleid**
> InlineResponse20013 kycprotectgetschedulesbyscheduleid(schedule_id)

Returns A Schedule

Returns a schedule in AML monitoring.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLMonitoringManagementApi(pycsapi.ApiClient(configuration))
schedule_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile

try:
    # Returns A Schedule
    api_response = api_instance.kycprotectgetschedulesbyscheduleid(schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLMonitoringManagementApi->kycprotectgetschedulesbyscheduleid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schedule_id** | [**str**](.md)| id of the profile | 

### Return type

[**InlineResponse20013**](InlineResponse20013.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


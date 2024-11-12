# pycsapi.ProtectAuditApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_audit_log_file**](ProtectAuditApi.md#export_audit_log_file) | **POST** /protect/audits | Export Audit Log File
[**retrieve_protect_audit_log**](ProtectAuditApi.md#retrieve_protect_audit_log) | **GET** /protect/audits | Retrieve Protect Audit Log

# **export_audit_log_file**
> ConnectProtectAuditsExportResponseDto export_audit_log_file(body)

Export Audit Log File

Produces a collection a csv of Audit records.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectAuditApi(pycsapi.ApiClient(configuration))
body = pycsapi.ConnectProtectAuditExportRequestDto() # ConnectProtectAuditExportRequestDto | 

try:
    # Export Audit Log File
    api_response = api_instance.export_audit_log_file(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectAuditApi->export_audit_log_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectProtectAuditExportRequestDto**](ConnectProtectAuditExportRequestDto.md)|  | 

### Return type

[**ConnectProtectAuditsExportResponseDto**](ConnectProtectAuditsExportResponseDto.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_protect_audit_log**
> list[ConnectProtectAuditDto] retrieve_protect_audit_log(page=page, page_size=page_size, type=type, newer_than=newer_than, older_than=older_than, profile_id=profile_id, order=order)

Retrieve Protect Audit Log

Returns logged interactions with Protect endpoints for audit purposes. Actions logged include creating an Investigation, Investigation Record and Schedule.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectAuditApi(pycsapi.ApiClient(configuration))
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 56 # int | Number of items to return per Page. (optional)
type = 'type_example' # str |  (optional)
newer_than = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
older_than = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
profile_id = 'profile_id_example' # str |  (optional)
order = 'order_example' # str |  (optional)

try:
    # Retrieve Protect Audit Log
    api_response = api_instance.retrieve_protect_audit_log(page=page, page_size=page_size, type=type, newer_than=newer_than, older_than=older_than, profile_id=profile_id, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectAuditApi->retrieve_protect_audit_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Number of items to return per Page. | [optional] 
 **type** | **str**|  | [optional] 
 **newer_than** | **datetime**|  | [optional] 
 **older_than** | **datetime**|  | [optional] 
 **profile_id** | **str**|  | [optional] 
 **order** | **str**|  | [optional] 

### Return type

[**list[ConnectProtectAuditDto]**](ConnectProtectAuditDto.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


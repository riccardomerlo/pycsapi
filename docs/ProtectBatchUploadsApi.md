# pycsapi.ProtectBatchUploadsApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_upload_file**](ProtectBatchUploadsApi.md#batch_upload_file) | **POST** /protect/batchUploads | Batch Upload File
[**returns_batch_upload_by_id**](ProtectBatchUploadsApi.md#returns_batch_upload_by_id) | **GET** /protect/batchUploads/{batchUploadId} | Returns Batch Uploads by ID
[**returns_batch_uploads**](ProtectBatchUploadsApi.md#returns_batch_uploads) | **GET** /protect/batchUploads | Returns Batch Uploads
[**returns_error_file_link**](ProtectBatchUploadsApi.md#returns_error_file_link) | **GET** /protect/batchUploads/{batchUploadId}/errorFile | Returns Error File Link
[**returns_selected_template_link**](ProtectBatchUploadsApi.md#returns_selected_template_link) | **GET** /protect/batchUploads/templates/{type} | Returns Selected Template Link

# **batch_upload_file**
> BatchUpload batch_upload_file(investigation_type=investigation_type, file=file)

Batch Upload File

Endpoint to upload a file that generates multiple searches and investigations. <br><br> Note - file needs to be structured as per the template.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectBatchUploadsApi(pycsapi.ApiClient(configuration))
investigation_type = 'investigation_type_example' # str |  (optional)
file = 'file_example' # str |  (optional)

try:
    # Batch Upload File
    api_response = api_instance.batch_upload_file(investigation_type=investigation_type, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectBatchUploadsApi->batch_upload_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_type** | **str**|  | [optional] 
 **file** | **str**|  | [optional] 

### Return type

[**BatchUpload**](BatchUpload.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **returns_batch_upload_by_id**
> BatchUpload returns_batch_upload_by_id(batch_upload_id)

Returns Batch Uploads by ID

Will return the batch upload details of a specific file id.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectBatchUploadsApi(pycsapi.ApiClient(configuration))
batch_upload_id = 'batch_upload_id_example' # str | 

try:
    # Returns Batch Uploads by ID
    api_response = api_instance.returns_batch_upload_by_id(batch_upload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectBatchUploadsApi->returns_batch_upload_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_upload_id** | **str**|  | 

### Return type

[**BatchUpload**](BatchUpload.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **returns_batch_uploads**
> list[BatchUpload] returns_batch_uploads(page=page, limit=limit)

Returns Batch Uploads

Returns all the Batch Uploads created by a user.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectBatchUploadsApi(pycsapi.ApiClient(configuration))
page = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    # Returns Batch Uploads
    api_response = api_instance.returns_batch_uploads(page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectBatchUploadsApi->returns_batch_uploads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**list[BatchUpload]**](BatchUpload.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **returns_error_file_link**
> FileDownloadResponse returns_error_file_link(batch_upload_id)

Returns Error File Link

Provides a link to the file in error.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectBatchUploadsApi(pycsapi.ApiClient(configuration))
batch_upload_id = 'batch_upload_id_example' # str | 

try:
    # Returns Error File Link
    api_response = api_instance.returns_error_file_link(batch_upload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectBatchUploadsApi->returns_error_file_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_upload_id** | **str**|  | 

### Return type

[**FileDownloadResponse**](FileDownloadResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **returns_selected_template_link**
> FileDownloadResponse returns_selected_template_link(type)

Returns Selected Template Link

Provides template for the file upload csv structure.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectBatchUploadsApi(pycsapi.ApiClient(configuration))
type = 'type_example' # str | 

try:
    # Returns Selected Template Link
    api_response = api_instance.returns_selected_template_link(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectBatchUploadsApi->returns_selected_template_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 

### Return type

[**FileDownloadResponse**](FileDownloadResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


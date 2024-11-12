# pycsapi.KYCBatchUploadsApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compliance_get_kyc_batch_upload_by_upload_id**](KYCBatchUploadsApi.md#compliance_get_kyc_batch_upload_by_upload_id) | **GET** /compliance/kyc-protect/batchUploads/{uploadId} | Return Batch Upload File Details
[**compliance_get_kyc_batch_uploads**](KYCBatchUploadsApi.md#compliance_get_kyc_batch_uploads) | **GET** /compliance/kyc-protect/batchUploads | Return A List Of Requested Uploads
[**compliance_get_kyc_batch_uploads_download_errors_by_upload_id**](KYCBatchUploadsApi.md#compliance_get_kyc_batch_uploads_download_errors_by_upload_id) | **GET** /compliance/kyc-protect/batchUploads/{uploadId}/errors/download | Download Batch Upload Error File
[**compliance_get_kyc_batch_uploads_retry_by_upload_id**](KYCBatchUploadsApi.md#compliance_get_kyc_batch_uploads_retry_by_upload_id) | **PUT** /compliance/kyc-protect/batchUploads/{uploadId}/retry | Retry Previous Upload
[**compliance_get_kyc_batch_uploads_template**](KYCBatchUploadsApi.md#compliance_get_kyc_batch_uploads_template) | **GET** /compliance/kyc-protect/batchUploads/template | Return Template For Batch Upload
[**compliance_post_kyc_batch_uploads**](KYCBatchUploadsApi.md#compliance_post_kyc_batch_uploads) | **POST** /compliance/kyc-protect/batchUploads | Request Batch Upload

# **compliance_get_kyc_batch_upload_by_upload_id**
> GetKycProtectBatchUploadsByUploadIdItemResponse compliance_get_kyc_batch_upload_by_upload_id(upload_id)

Return Batch Upload File Details

Returns a batch Upload response as specified by the provided id.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCBatchUploadsApi(pycsapi.ApiClient(configuration))
upload_id = 56 # int | id of the upload.

try:
    # Return Batch Upload File Details
    api_response = api_instance.compliance_get_kyc_batch_upload_by_upload_id(upload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCBatchUploadsApi->compliance_get_kyc_batch_upload_by_upload_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **int**| id of the upload. | 

### Return type

[**GetKycProtectBatchUploadsByUploadIdItemResponse**](GetKycProtectBatchUploadsByUploadIdItemResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliance_get_kyc_batch_uploads**
> GetKycProtectBatchUploadsByUploadsResponse compliance_get_kyc_batch_uploads(page=page, page_size=page_size, statuses=statuses, uploaded_by_id=uploaded_by_id)

Return A List Of Requested Uploads

Returns a list of uploads that have been requested.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCBatchUploadsApi(pycsapi.ApiClient(configuration))
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 10 # int | Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. (optional) (default to 10)
statuses = ['statuses_example'] # list[str] | The statuses list to filter by. It can be the collection of submitted, validating, rejected, validated, insufficientCredits, queued, inProgress, processed, completed, partiallyCompleted, failed. (optional)
uploaded_by_id = 56 # int | The id of the uploaded user to filter by. (optional)

try:
    # Return A List Of Requested Uploads
    api_response = api_instance.compliance_get_kyc_batch_uploads(page=page, page_size=page_size, statuses=statuses, uploaded_by_id=uploaded_by_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCBatchUploadsApi->compliance_get_kyc_batch_uploads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. | [optional] [default to 10]
 **statuses** | [**list[str]**](str.md)| The statuses list to filter by. It can be the collection of submitted, validating, rejected, validated, insufficientCredits, queued, inProgress, processed, completed, partiallyCompleted, failed. | [optional] 
 **uploaded_by_id** | **int**| The id of the uploaded user to filter by. | [optional] 

### Return type

[**GetKycProtectBatchUploadsByUploadsResponse**](GetKycProtectBatchUploadsByUploadsResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliance_get_kyc_batch_uploads_download_errors_by_upload_id**
> GetBatchUploadsDownloadErrorsByUploadIdResponse compliance_get_kyc_batch_uploads_download_errors_by_upload_id(upload_id)

Download Batch Upload Error File

Returns a link to download the error file if it has does fail during the upload this is acquired using the upload Id..

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCBatchUploadsApi(pycsapi.ApiClient(configuration))
upload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the upload

try:
    # Download Batch Upload Error File
    api_response = api_instance.compliance_get_kyc_batch_uploads_download_errors_by_upload_id(upload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCBatchUploadsApi->compliance_get_kyc_batch_uploads_download_errors_by_upload_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | [**str**](.md)| id of the upload | 

### Return type

[**GetBatchUploadsDownloadErrorsByUploadIdResponse**](GetBatchUploadsDownloadErrorsByUploadIdResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliance_get_kyc_batch_uploads_retry_by_upload_id**
> PutBatchUploadsRetryByIdResponse compliance_get_kyc_batch_uploads_retry_by_upload_id(upload_id)

Retry Previous Upload

Re-uploads the file if it was previously failed due to 'insufficientCredits' status.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCBatchUploadsApi(pycsapi.ApiClient(configuration))
upload_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the upload

try:
    # Retry Previous Upload
    api_response = api_instance.compliance_get_kyc_batch_uploads_retry_by_upload_id(upload_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCBatchUploadsApi->compliance_get_kyc_batch_uploads_retry_by_upload_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | [**str**](.md)| id of the upload | 

### Return type

[**PutBatchUploadsRetryByIdResponse**](PutBatchUploadsRetryByIdResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliance_get_kyc_batch_uploads_template**
> GetBatchUploadsTemplateResponse compliance_get_kyc_batch_uploads_template()

Return Template For Batch Upload

<h3>This endpoint the HTTP Request is planned to be altered in the next release</h3><br> Returns the template to complete a batch upload.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCBatchUploadsApi(pycsapi.ApiClient(configuration))

try:
    # Return Template For Batch Upload
    api_response = api_instance.compliance_get_kyc_batch_uploads_template()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCBatchUploadsApi->compliance_get_kyc_batch_uploads_template: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBatchUploadsTemplateResponse**](GetBatchUploadsTemplateResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliance_post_kyc_batch_uploads**
> PostKycProtectBatchUploadsResponse compliance_post_kyc_batch_uploads(file=file)

Request Batch Upload

Submits the batch file process request. Returns the details of the accepted request.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCBatchUploadsApi(pycsapi.ApiClient(configuration))
file = 'file_example' # str |  (optional)

try:
    # Request Batch Upload
    api_response = api_instance.compliance_post_kyc_batch_uploads(file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCBatchUploadsApi->compliance_post_kyc_batch_uploads: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **str**|  | [optional] 

### Return type

[**PostKycProtectBatchUploadsResponse**](PostKycProtectBatchUploadsResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


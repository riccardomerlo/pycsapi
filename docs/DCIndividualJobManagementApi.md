# pycsapi.DCIndividualJobManagementApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**archive_job**](DCIndividualJobManagementApi.md#archive_job) | **POST** /dataCleaning/jobs/{id}/archive | Archive Job by id
[**data_cleaning_job_enrich**](DCIndividualJobManagementApi.md#data_cleaning_job_enrich) | **POST** /dataCleaning/jobs/{id}/enrich | Start Enrichment Request
[**get_job_by_id_number**](DCIndividualJobManagementApi.md#get_job_by_id_number) | **GET** /dataCleaning/jobs/{id} | Returns Job by {id} number
[**job_file_upload_with_id**](DCIndividualJobManagementApi.md#job_file_upload_with_id) | **POST** /dataCleaning/jobs/{id}/upload | Upload a Job File with an {id}
[**job_update_mappings**](DCIndividualJobManagementApi.md#job_update_mappings) | **PUT** /dataCleaning/jobs/{id}/mappings | Update Mappings Request
[**returns_enriched_job_file**](DCIndividualJobManagementApi.md#returns_enriched_job_file) | **GET** /dataCleaning/jobs/{id}/enrichedFile | Returns Enriched Job File
[**submit_job_request**](DCIndividualJobManagementApi.md#submit_job_request) | **POST** /dataCleaning/jobs/{id}/submit | Submit Job Request
[**update_job_enrichments**](DCIndividualJobManagementApi.md#update_job_enrichments) | **PUT** /dataCleaning/jobs/{id}/enrichments | Update Enrichments Request

# **archive_job**
> ConnectDataCleaningArchiveResponse archive_job(body, id)

Archive Job by id

Archives the job, this can be done at any stage. To have a successful submission a blank response body (See example) is required to be posted.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.DCIndividualJobManagementApi(pycsapi.ApiClient(configuration))
body = pycsapi.ConnectDataCleaningArchiveJobRequest() # ConnectDataCleaningArchiveJobRequest | 
id = 'id_example' # str | 

try:
    # Archive Job by id
    api_response = api_instance.archive_job(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DCIndividualJobManagementApi->archive_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectDataCleaningArchiveJobRequest**](ConnectDataCleaningArchiveJobRequest.md)|  | 
 **id** | **str**|  | 

### Return type

[**ConnectDataCleaningArchiveResponse**](ConnectDataCleaningArchiveResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_cleaning_job_enrich**
> ArrayOfConnectDataCleaningResponse data_cleaning_job_enrich(body, id)

Start Enrichment Request

Commencing the Job enrichment to the uploaded file after mapping the enrichment requirements. To have a successful submission a blank response body (See example) is required to be posted.<br><br> POST 'enrich' will not commence unless the `Job Status` is `jobMatchingComplete`.<br><br>Use the GET/dataCleaning/jobs/{id} to check Status of job.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.DCIndividualJobManagementApi(pycsapi.ApiClient(configuration))
body = pycsapi.ConnectDataCleaningEnrichRequest() # ConnectDataCleaningEnrichRequest | 
id = 'id_example' # str | 

try:
    # Start Enrichment Request
    api_response = api_instance.data_cleaning_job_enrich(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DCIndividualJobManagementApi->data_cleaning_job_enrich: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectDataCleaningEnrichRequest**](ConnectDataCleaningEnrichRequest.md)|  | 
 **id** | **str**|  | 

### Return type

[**ArrayOfConnectDataCleaningResponse**](ArrayOfConnectDataCleaningResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_by_id_number**
> ConnectDataCleaningJob get_job_by_id_number(id)

Returns Job by {id} number

Returns Job by {id} number which is generated from 'Creating Job Request' stage. This endpoint is used to check the `status` of the job.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.DCIndividualJobManagementApi(pycsapi.ApiClient(configuration))
id = 'id_example' # str | 

try:
    # Returns Job by {id} number
    api_response = api_instance.get_job_by_id_number(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DCIndividualJobManagementApi->get_job_by_id_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ConnectDataCleaningJob**](ConnectDataCleaningJob.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_file_upload_with_id**
> ConnectDataCleaningUploadResponse job_file_upload_with_id(id, job_file=job_file, has_header=has_header)

Upload a Job File with an {id}

Upload a Job File for processing, you need to link to the {id} number generated from the 'Job Request'.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.DCIndividualJobManagementApi(pycsapi.ApiClient(configuration))
id = 'id_example' # str | The {id} number generated from the 'Job Request'.
job_file = 'job_file_example' # str |  (optional)
has_header = true # bool |  (optional)

try:
    # Upload a Job File with an {id}
    api_response = api_instance.job_file_upload_with_id(id, job_file=job_file, has_header=has_header)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DCIndividualJobManagementApi->job_file_upload_with_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The {id} number generated from the &#x27;Job Request&#x27;. | 
 **job_file** | **str**|  | [optional] 
 **has_header** | **bool**|  | [optional] 

### Return type

[**ConnectDataCleaningUploadResponse**](ConnectDataCleaningUploadResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **job_update_mappings**
> ConnectDataCleaningMappingResponse job_update_mappings(body, id)

Update Mappings Request

Update the mapping of the uploaded file to match that of the header within it. You can add or remove the required number of mapping points in the Request Body.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.DCIndividualJobManagementApi(pycsapi.ApiClient(configuration))
body = pycsapi.ConnectDataCleaningUpdateMappingsRequest() # ConnectDataCleaningUpdateMappingsRequest | 
id = 'id_example' # str | 

try:
    # Update Mappings Request
    api_response = api_instance.job_update_mappings(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DCIndividualJobManagementApi->job_update_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectDataCleaningUpdateMappingsRequest**](ConnectDataCleaningUpdateMappingsRequest.md)|  | 
 **id** | **str**|  | 

### Return type

[**ConnectDataCleaningMappingResponse**](ConnectDataCleaningMappingResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **returns_enriched_job_file**
> ConnectDataCleaningResponse returns_enriched_job_file(id, file_type=file_type)

Returns Enriched Job File

Returns the enriched file after enrichment is complete. Identify the file type to be returned via the query parameter.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.DCIndividualJobManagementApi(pycsapi.ApiClient(configuration))
id = 'id_example' # str | 
file_type = 'file_type_example' # str |  (optional)

try:
    # Returns Enriched Job File
    api_response = api_instance.returns_enriched_job_file(id, file_type=file_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DCIndividualJobManagementApi->returns_enriched_job_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **file_type** | **str**|  | [optional] 

### Return type

[**ConnectDataCleaningResponse**](ConnectDataCleaningResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_job_request**
> ConnectDataCleaningResponse submit_job_request(body, id)

Submit Job Request

Submission of the file after mappings have been carried out. To have a successful submission a blank response body (See example) is required to be posted.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.DCIndividualJobManagementApi(pycsapi.ApiClient(configuration))
body = pycsapi.ConnectDataCleaningSubmitJobRequest() # ConnectDataCleaningSubmitJobRequest | 
id = 'id_example' # str | 

try:
    # Submit Job Request
    api_response = api_instance.submit_job_request(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DCIndividualJobManagementApi->submit_job_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectDataCleaningSubmitJobRequest**](ConnectDataCleaningSubmitJobRequest.md)|  | 
 **id** | **str**|  | 

### Return type

[**ConnectDataCleaningResponse**](ConnectDataCleaningResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_job_enrichments**
> ConnectDataCleaningResponse update_job_enrichments(body, id)

Update Enrichments Request

Detail which package of enrichment settings are to be applied to the uploaded file.<br><br> Select one of the three creditTypes to acquire the JSON Enrichment tag schema possible for that product.<br><br> Removal of Enrichment tags is possible from each creditType. Addition of Enrichment tags to a creditType is not possible beyond the maximum schema for each.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.DCIndividualJobManagementApi(pycsapi.ApiClient(configuration))
body = pycsapi.IdEnrichmentsBody() # IdEnrichmentsBody | 
id = 'id_example' # str | 

try:
    # Update Enrichments Request
    api_response = api_instance.update_job_enrichments(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DCIndividualJobManagementApi->update_job_enrichments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdEnrichmentsBody**](IdEnrichmentsBody.md)|  | 
 **id** | **str**|  | 

### Return type

[**ConnectDataCleaningResponse**](ConnectDataCleaningResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


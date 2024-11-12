# pycsapi.ProtectInvestigationsApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_investigations_records**](ProtectInvestigationsApi.md#add_investigations_records) | **POST** /protect/investigations/{investigationId}/records | Add Investigations Records
[**assign_risk_to_investigation**](ProtectInvestigationsApi.md#assign_risk_to_investigation) | **PUT** /protect/investigations/{id}/risk | Assign Risk to Investigation
[**create_investigation_and_return_report_link**](ProtectInvestigationsApi.md#create_investigation_and_return_report_link) | **POST** /protect/investigations/file | Create Investigation And Return Report Link
[**create_investigation_note**](ProtectInvestigationsApi.md#create_investigation_note) | **POST** /protect/investigations/{id}/notes | Create Investigation Note
[**create_protect_investigation**](ProtectInvestigationsApi.md#create_protect_investigation) | **POST** /protect/investigations | Create Protect Investigation
[**create_protect_investigation_pdf**](ProtectInvestigationsApi.md#create_protect_investigation_pdf) | **POST** /protect/investigations/{investigationId}/file | Create Protect Investigation PDF
[**delete_investigation**](ProtectInvestigationsApi.md#delete_investigation) | **DELETE** /protect/investigations/{investigationId} | Delete Investigation
[**delete_investigation_records**](ProtectInvestigationsApi.md#delete_investigation_records) | **DELETE** /protect/investigations/{investigationId}/records | Delete Investigation Records
[**get_investigation_notes**](ProtectInvestigationsApi.md#get_investigation_notes) | **GET** /protect/investigations/{id}/notes | Get Investigation Notes
[**get_investigation_results_by_id**](ProtectInvestigationsApi.md#get_investigation_results_by_id) | **GET** /protect/investigations/{investigationId}/results | Get Investigation Results By Id
[**list_all_protect_investigations**](ProtectInvestigationsApi.md#list_all_protect_investigations) | **GET** /protect/investigations | List All Protect Investigations
[**return_investigations_records**](ProtectInvestigationsApi.md#return_investigations_records) | **GET** /protect/investigations/{investigationId}/records | Return Investigation Records
[**return_protect_investigation_by_id**](ProtectInvestigationsApi.md#return_protect_investigation_by_id) | **GET** /protect/investigations/{investigationId} | Return Protect Investigation By Id
[**returns_investigation_report**](ProtectInvestigationsApi.md#returns_investigation_report) | **POST** /protect/investigations/{investigationId}/records/file | Returns Investigation Report
[**update_investigations_records**](ProtectInvestigationsApi.md#update_investigations_records) | **PUT** /protect/investigations/{investigationId}/records | Update Investigation Records

# **add_investigations_records**
> list[ConnectProtectRecord] add_investigations_records(body, investigation_id)

Add Investigations Records

Requires the 'Investigation Id' in path, followed by 'Record Id' in the request body to add a record to the previously created Investigation.<br><br>By adding InvestigationRecords you are confirming that the result is a match to your search criteria. <br><br>To return to the original Investigation search to allocate other records, use \"GET Investigation results by ID.\".

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectInvestigationsApi(pycsapi.ApiClient(configuration))
body = pycsapi.ConnectProtectCreateInvestigationRecordBody() # ConnectProtectCreateInvestigationRecordBody | 
investigation_id = 'investigation_id_example' # str | 

try:
    # Add Investigations Records
    api_response = api_instance.add_investigations_records(body, investigation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectInvestigationsApi->add_investigations_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectProtectCreateInvestigationRecordBody**](ConnectProtectCreateInvestigationRecordBody.md)|  | 
 **investigation_id** | **str**|  | 

### Return type

[**list[ConnectProtectRecord]**](ConnectProtectRecord.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, text/json, text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_risk_to_investigation**
> InvestigationRiskResponse assign_risk_to_investigation(body, id)

Assign Risk to Investigation

Allows user to update the risk with an Investigation.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectInvestigationsApi(pycsapi.ApiClient(configuration))
body = pycsapi.AssignRiskToInvestigationDto() # AssignRiskToInvestigationDto | 
id = 'id_example' # str | 

try:
    # Assign Risk to Investigation
    api_response = api_instance.assign_risk_to_investigation(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectInvestigationsApi->assign_risk_to_investigation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssignRiskToInvestigationDto**](AssignRiskToInvestigationDto.md)|  | 
 **id** | **str**|  | 

### Return type

[**InvestigationRiskResponse**](InvestigationRiskResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_investigation_and_return_report_link**
> FileDownloadResponse create_investigation_and_return_report_link(body)

Create Investigation And Return Report Link

Creates an investigation and returns a link to the report.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectInvestigationsApi(pycsapi.ApiClient(configuration))
body = pycsapi.CreateInvestigationQueryDto() # CreateInvestigationQueryDto | 

try:
    # Create Investigation And Return Report Link
    api_response = api_instance.create_investigation_and_return_report_link(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectInvestigationsApi->create_investigation_and_return_report_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateInvestigationQueryDto**](CreateInvestigationQueryDto.md)|  | 

### Return type

[**FileDownloadResponse**](FileDownloadResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_investigation_note**
> InvestigationNote create_investigation_note(body, id)

Create Investigation Note

Creates a note to a specific investigation ID.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectInvestigationsApi(pycsapi.ApiClient(configuration))
body = pycsapi.CreateInvestigationNoteDto() # CreateInvestigationNoteDto | 
id = 'id_example' # str | 

try:
    # Create Investigation Note
    api_response = api_instance.create_investigation_note(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectInvestigationsApi->create_investigation_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateInvestigationNoteDto**](CreateInvestigationNoteDto.md)|  | 
 **id** | **str**|  | 

### Return type

[**InvestigationNote**](InvestigationNote.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_protect_investigation**
> ConnectProtectInvestigationResponse create_protect_investigation(body)

Create Protect Investigation

Creates an Investigation according to the provided Investigation criteria. Each result is potential match which is attributed a relevancy/match score between 1-100 and a high level reason for it's inclusion in the World Compliance Database by looking at the Reason Listed and Comments to firstly ascertain whether the entry is a match for you search criteria and then utilize the data available for your own onboarding needs.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectInvestigationsApi(pycsapi.ApiClient(configuration))
body = pycsapi.ConnectProtectCreateInvestigationQueryDto() # ConnectProtectCreateInvestigationQueryDto | 

try:
    # Create Protect Investigation
    api_response = api_instance.create_protect_investigation(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectInvestigationsApi->create_protect_investigation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectProtectCreateInvestigationQueryDto**](ConnectProtectCreateInvestigationQueryDto.md)|  | 

### Return type

[**ConnectProtectInvestigationResponse**](ConnectProtectInvestigationResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_protect_investigation_pdf**
> ConnectProtectInvestigationFileResponse create_protect_investigation_pdf(body, investigation_id)

Create Protect Investigation PDF

Creates a PDF that shows the full report for the selected entities. This report will include search criteria used, user, time/date stamp and full World Compliance Report. It is recommended to call this endpoint before adding InvestigationRecords to an Investigation, as only non-processed alerts populate the PDF.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectInvestigationsApi(pycsapi.ApiClient(configuration))
body = pycsapi.ConnectProtectGetInvestigationFileBodyDto() # ConnectProtectGetInvestigationFileBodyDto | 
investigation_id = 'investigation_id_example' # str | 

try:
    # Create Protect Investigation PDF
    api_response = api_instance.create_protect_investigation_pdf(body, investigation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectInvestigationsApi->create_protect_investigation_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectProtectGetInvestigationFileBodyDto**](ConnectProtectGetInvestigationFileBodyDto.md)|  | 
 **investigation_id** | **str**|  | 

### Return type

[**ConnectProtectInvestigationFileResponse**](ConnectProtectInvestigationFileResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_investigation**
> delete_investigation(investigation_id)

Delete Investigation

Deletes an Investigation by {Id} number. This will remove the entire Investigation and all results within it.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectInvestigationsApi(pycsapi.ApiClient(configuration))
investigation_id = 'investigation_id_example' # str | 

try:
    # Delete Investigation
    api_instance.delete_investigation(investigation_id)
except ApiException as e:
    print("Exception when calling ProtectInvestigationsApi->delete_investigation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_investigation_records**
> list[Record] delete_investigation_records(body, investigation_id)

Delete Investigation Records

Deletes a record from an Investigation ID.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectInvestigationsApi(pycsapi.ApiClient(configuration))
body = pycsapi.DeleteRecordsDto() # DeleteRecordsDto | 
investigation_id = 'investigation_id_example' # str | 

try:
    # Delete Investigation Records
    api_response = api_instance.delete_investigation_records(body, investigation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectInvestigationsApi->delete_investigation_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteRecordsDto**](DeleteRecordsDto.md)|  | 
 **investigation_id** | **str**|  | 

### Return type

[**list[Record]**](Record.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_investigation_notes**
> list[InvestigationNote] get_investigation_notes(id, page=page, limit=limit)

Get Investigation Notes

Returns the notes created against a specific investigation ID.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectInvestigationsApi(pycsapi.ApiClient(configuration))
id = 'id_example' # str | 
page = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    # Get Investigation Notes
    api_response = api_instance.get_investigation_notes(id, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectInvestigationsApi->get_investigation_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**list[InvestigationNote]**](InvestigationNote.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_investigation_results_by_id**
> InlineResponse2006 get_investigation_results_by_id(investigation_id, page=page, limit=limit)

Get Investigation Results By Id

Returns original Investigation search results to assign any other results to the records.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectInvestigationsApi(pycsapi.ApiClient(configuration))
investigation_id = 'investigation_id_example' # str | 
page = 56 # int |  (optional)
limit = 56 # int |  (optional)

try:
    # Get Investigation Results By Id
    api_response = api_instance.get_investigation_results_by_id(investigation_id, page=page, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectInvestigationsApi->get_investigation_results_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_id** | **str**|  | 
 **page** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_protect_investigations**
> list[ConnectProtectInvestigation] list_all_protect_investigations(scheduled=scheduled, alerts_count=alerts_count, type=type, q=q, order=order, order_by=order_by, page=page, page_size=page_size)

List All Protect Investigations

Endpoint to return all investigations. Filter response by using query parameters. Use the alertsCount parameter to only return Investigations with alerts greater than the supplied value.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectInvestigationsApi(pycsapi.ApiClient(configuration))
scheduled = true # bool |  (optional)
alerts_count = 56 # int |  (optional)
type = 'type_example' # str |  (optional)
q = 'q_example' # str | Keyword search: It searches in the 'name' fields of the investigation. (optional)
order = 'order_example' # str |  (optional)
order_by = 'order_by_example' # str |  (optional)
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 56 # int | Number of items to return per Page. (optional)

try:
    # List All Protect Investigations
    api_response = api_instance.list_all_protect_investigations(scheduled=scheduled, alerts_count=alerts_count, type=type, q=q, order=order, order_by=order_by, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectInvestigationsApi->list_all_protect_investigations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled** | **bool**|  | [optional] 
 **alerts_count** | **int**|  | [optional] 
 **type** | **str**|  | [optional] 
 **q** | **str**| Keyword search: It searches in the &#x27;name&#x27; fields of the investigation. | [optional] 
 **order** | **str**|  | [optional] 
 **order_by** | **str**|  | [optional] 
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Number of items to return per Page. | [optional] 

### Return type

[**list[ConnectProtectInvestigation]**](ConnectProtectInvestigation.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_investigations_records**
> list[ConnectProtectRecord] return_investigations_records(investigation_id, page=page, page_size=page_size)

Return Investigation Records

Requires the 'Investigation Id' in path.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectInvestigationsApi(pycsapi.ApiClient(configuration))
investigation_id = 'investigation_id_example' # str | Investigation Id
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 56 # int | Number of items to return per Page. (optional)

try:
    # Return Investigation Records
    api_response = api_instance.return_investigations_records(investigation_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectInvestigationsApi->return_investigations_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_id** | **str**| Investigation Id | 
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Number of items to return per Page. | [optional] 

### Return type

[**list[ConnectProtectRecord]**](ConnectProtectRecord.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_protect_investigation_by_id**
> ConnectProtectInvestigationResponse return_protect_investigation_by_id(investigation_id)

Return Protect Investigation By Id

Endpoint to return a specific Investigation by ID. Can also be used to retrieve the associated Schedule Id that has been linked to the Investigation.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectInvestigationsApi(pycsapi.ApiClient(configuration))
investigation_id = 'investigation_id_example' # str | 

try:
    # Return Protect Investigation By Id
    api_response = api_instance.return_protect_investigation_by_id(investigation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectInvestigationsApi->return_protect_investigation_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **investigation_id** | **str**|  | 

### Return type

[**ConnectProtectInvestigationResponse**](ConnectProtectInvestigationResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **returns_investigation_report**
> FileDownloadResponse returns_investigation_report(body, investigation_id)

Returns Investigation Report

This endpoint will Return a report by providing a file path.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectInvestigationsApi(pycsapi.ApiClient(configuration))
body = pycsapi.GetInvestigationFileBodyDto() # GetInvestigationFileBodyDto | 
investigation_id = 'investigation_id_example' # str | 

try:
    # Returns Investigation Report
    api_response = api_instance.returns_investigation_report(body, investigation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectInvestigationsApi->returns_investigation_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetInvestigationFileBodyDto**](GetInvestigationFileBodyDto.md)|  | 
 **investigation_id** | **str**|  | 

### Return type

[**FileDownloadResponse**](FileDownloadResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_investigations_records**
> list[Record] update_investigations_records(body, investigation_id)

Update Investigation Records

Sends an update to the investigation specified by the ID and changes will be reflected within that investigation.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectInvestigationsApi(pycsapi.ApiClient(configuration))
body = pycsapi.UpdateInvestigationRecordsDto() # UpdateInvestigationRecordsDto | 
investigation_id = 'investigation_id_example' # str | 

try:
    # Update Investigation Records
    api_response = api_instance.update_investigations_records(body, investigation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectInvestigationsApi->update_investigations_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateInvestigationRecordsDto**](UpdateInvestigationRecordsDto.md)|  | 
 **investigation_id** | **str**|  | 

### Return type

[**list[Record]**](Record.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


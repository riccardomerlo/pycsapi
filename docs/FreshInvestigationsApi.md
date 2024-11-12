# pycsapi.FreshInvestigationsApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comments_for_fresh_investigation_order_id**](FreshInvestigationsApi.md#comments_for_fresh_investigation_order_id) | **POST** /freshinvestigations/{orderId}/comments | Comments for fresh investigation orderId
[**create_fresh_investigation**](FreshInvestigationsApi.md#create_fresh_investigation) | **POST** /freshinvestigations | Create Fresh Investigation
[**delete_fresh_investigations**](FreshInvestigationsApi.md#delete_fresh_investigations) | **DELETE** /freshinvestigations/{orderId} | Delete Fresh Investigations
[**get_attachment_for_the_given_fresh_investigation_attachment_id**](FreshInvestigationsApi.md#get_attachment_for_the_given_fresh_investigation_attachment_id) | **GET** /freshinvestigations/{orderId}/attachments/{id} | Get attachment for the given fresh investigation attachment Id
[**get_attachments_for_the_given_fresh_investigation_order_id**](FreshInvestigationsApi.md#get_attachments_for_the_given_fresh_investigation_order_id) | **GET** /freshinvestigations/{orderId}/attachments | Get attachments for the given fresh investigation orderId
[**get_fresh_investigations**](FreshInvestigationsApi.md#get_fresh_investigations) | **GET** /freshinvestigations | Get Fresh Investigations
[**retrieve_comments_of_specified_fresh_investigation_report**](FreshInvestigationsApi.md#retrieve_comments_of_specified_fresh_investigation_report) | **GET** /freshinvestigations/{orderId}/comments | Retrieve comments of specified FreshInvestigation Report
[**retrieve_fresh_investigation_order**](FreshInvestigationsApi.md#retrieve_fresh_investigation_order) | **GET** /freshinvestigations/{orderId} | Retrieve FreshInvestigation Order
[**retrieve_fresh_investigation_report_content**](FreshInvestigationsApi.md#retrieve_fresh_investigation_report_content) | **GET** /freshinvestigations/{orderId}/report | Retrieve FreshInvestigation Report Content
[**update_fresh_investigation_report_content**](FreshInvestigationsApi.md#update_fresh_investigation_report_content) | **PATCH** /freshinvestigations/{orderId} | Update FreshInvestigation Report Content
[**upload_attachments_for_fresh_investigation_order_id**](FreshInvestigationsApi.md#upload_attachments_for_fresh_investigation_order_id) | **POST** /freshinvestigations/{orderId}/attachments | Upload attachments for fresh investigation orderId

# **comments_for_fresh_investigation_order_id**
> FreshInvestigationCommentsForOrderResponse comments_for_fresh_investigation_order_id(body, order_id)

Comments for fresh investigation orderId

Returns the status of comments for the particular order.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.FreshInvestigationsApi(pycsapi.ApiClient(configuration))
body = pycsapi.FreshInvestigationCommentsForOrderRequest() # FreshInvestigationCommentsForOrderRequest | 
order_id = 'order_id_example' # str | fresh investigation orderId

try:
    # Comments for fresh investigation orderId
    api_response = api_instance.comments_for_fresh_investigation_order_id(body, order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreshInvestigationsApi->comments_for_fresh_investigation_order_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FreshInvestigationCommentsForOrderRequest**](FreshInvestigationCommentsForOrderRequest.md)|  | 
 **order_id** | **str**| fresh investigation orderId | 

### Return type

[**FreshInvestigationCommentsForOrderResponse**](FreshInvestigationCommentsForOrderResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_fresh_investigation**
> ConnectFreshInvInvestigationConfirmed create_fresh_investigation(body=body)

Create Fresh Investigation

Places an order for a Fresh Investigation (Offline Report). Providing as much detail as possible about the Company, our team will use official sources and registries to quickly answer questions about a company's stability and financial health. Fresh Investigations take 5.5 days on average to complete. By adding `consent:true` to the request, you are allowing Creditsafe to disclose your company details to the company you have requested the Investigation against, to be used only in the aim of improving our Investigation report.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.FreshInvestigationsApi(pycsapi.ApiClient(configuration))
body = pycsapi.ConnectFreshInvCreateInvestigation() # ConnectFreshInvCreateInvestigation |  (optional)

try:
    # Create Fresh Investigation
    api_response = api_instance.create_fresh_investigation(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreshInvestigationsApi->create_fresh_investigation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectFreshInvCreateInvestigation**](ConnectFreshInvCreateInvestigation.md)|  | [optional] 

### Return type

[**ConnectFreshInvInvestigationConfirmed**](ConnectFreshInvInvestigationConfirmed.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_fresh_investigations**
> DeleteFreshInvetigationsByOrderId delete_fresh_investigations(order_id)

Delete Fresh Investigations

Deletes specified investigations.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.FreshInvestigationsApi(pycsapi.ApiClient(configuration))
order_id = 'order_id_example' # str | Investigation id.

try:
    # Delete Fresh Investigations
    api_response = api_instance.delete_fresh_investigations(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreshInvestigationsApi->delete_fresh_investigations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Investigation id. | 

### Return type

[**DeleteFreshInvetigationsByOrderId**](DeleteFreshInvetigationsByOrderId.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachment_for_the_given_fresh_investigation_attachment_id**
> CreditsafeFreshInvestigationGlobalDataCoreAttachmentBinaryAttachment get_attachment_for_the_given_fresh_investigation_attachment_id(order_id, id)

Get attachment for the given fresh investigation attachment Id

Retrieve attachment for the given attachmentId.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.FreshInvestigationsApi(pycsapi.ApiClient(configuration))
order_id = 'order_id_example' # str | fresh investigation orderId
id = 'id_example' # str | fresh investigation attachment id for the given order

try:
    # Get attachment for the given fresh investigation attachment Id
    api_response = api_instance.get_attachment_for_the_given_fresh_investigation_attachment_id(order_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreshInvestigationsApi->get_attachment_for_the_given_fresh_investigation_attachment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| fresh investigation orderId | 
 **id** | **str**| fresh investigation attachment id for the given order | 

### Return type

[**CreditsafeFreshInvestigationGlobalDataCoreAttachmentBinaryAttachment**](CreditsafeFreshInvestigationGlobalDataCoreAttachmentBinaryAttachment.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/*, text/*, image/*, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachments_for_the_given_fresh_investigation_order_id**
> FreshInvestigationGetAttachmentsForOrderResponse get_attachments_for_the_given_fresh_investigation_order_id(order_id)

Get attachments for the given fresh investigation orderId

Returns attachments available for that particular order.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.FreshInvestigationsApi(pycsapi.ApiClient(configuration))
order_id = 'order_id_example' # str | fresh investigation orderId

try:
    # Get attachments for the given fresh investigation orderId
    api_response = api_instance.get_attachments_for_the_given_fresh_investigation_order_id(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreshInvestigationsApi->get_attachments_for_the_given_fresh_investigation_order_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| fresh investigation orderId | 

### Return type

[**FreshInvestigationGetAttachmentsForOrderResponse**](FreshInvestigationGetAttachmentsForOrderResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_fresh_investigations**
> ConnectFreshInvListInvestigations get_fresh_investigations(page=page, page_size=page_size, transaction_id=transaction_id, report_created_after=report_created_after, report_created_before=report_created_before, created_before=created_before, created_since=created_since, look_up_order_by=look_up_order_by, company_details_country=company_details_country, company_details_name=company_details_name, search_criteria_country=search_criteria_country, search_criteria_name=search_criteria_name, sort_by=sort_by, sort_dir=sort_dir)

Get Fresh Investigations

Returns a list of your submitted Fresh Investigation Orders.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.FreshInvestigationsApi(pycsapi.ApiClient(configuration))
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 56 # int | Number of items to return per Page. (optional)
transaction_id = 'transaction_id_example' # str | Fresh Investigation Identifier used internally and with our data partners. (optional)
report_created_after = 'report_created_after_example' # str | Returns Fresh Investigations processed after this date (optional)
report_created_before = 'report_created_before_example' # str | Returns ordered Fresh Investigations that were processed before this date (optional)
created_before = 'created_before_example' # str | Returns Fresh Investigations created before this date (optional)
created_since = 'created_since_example' # str | Returns ordered Fresh Investigations created after this date (optional)
look_up_order_by = 'look_up_order_by_example' # str | Use to search for your Fresh Investigations by either the returned Company Details in the `GET` `freshInvestigations/{orderId}` endpoint or your supplied Search Criteria in the `POST` `/freshInvestigations` endpoint (optional)
company_details_country = 'company_details_country_example' # str | Looks for your returned Fresh Investigations where the returned Company Country is named this. Use with lookUpOrderBy=CompanyDetails (optional)
company_details_name = 'company_details_name_example' # str | Looks for your returned Fresh Investigations where the returned Company Name is named this. Use with lookUpOrderBy=CompanyDetails (optional)
search_criteria_country = 'search_criteria_country_example' # str | Looks for your returned Fresh Investigations where your submitted Search Criteria Company Country is this. Use with lookUpOrderBy=searchCriteria (optional)
search_criteria_name = 'search_criteria_name_example' # str | Looks for your Fresh Investigations where your submitted Search Criteria Company Name is this. Use with lookUpOrderBy=searchCriteria (optional)
sort_by = 'sort_by_example' # str | Sorts  returned Fresh Investigations by this field (optional)
sort_dir = 'asc' # str | The direction that you wish to sort results by. (optional) (default to asc)

try:
    # Get Fresh Investigations
    api_response = api_instance.get_fresh_investigations(page=page, page_size=page_size, transaction_id=transaction_id, report_created_after=report_created_after, report_created_before=report_created_before, created_before=created_before, created_since=created_since, look_up_order_by=look_up_order_by, company_details_country=company_details_country, company_details_name=company_details_name, search_criteria_country=search_criteria_country, search_criteria_name=search_criteria_name, sort_by=sort_by, sort_dir=sort_dir)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreshInvestigationsApi->get_fresh_investigations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Number of items to return per Page. | [optional] 
 **transaction_id** | **str**| Fresh Investigation Identifier used internally and with our data partners. | [optional] 
 **report_created_after** | **str**| Returns Fresh Investigations processed after this date | [optional] 
 **report_created_before** | **str**| Returns ordered Fresh Investigations that were processed before this date | [optional] 
 **created_before** | **str**| Returns Fresh Investigations created before this date | [optional] 
 **created_since** | **str**| Returns ordered Fresh Investigations created after this date | [optional] 
 **look_up_order_by** | **str**| Use to search for your Fresh Investigations by either the returned Company Details in the &#x60;GET&#x60; &#x60;freshInvestigations/{orderId}&#x60; endpoint or your supplied Search Criteria in the &#x60;POST&#x60; &#x60;/freshInvestigations&#x60; endpoint | [optional] 
 **company_details_country** | **str**| Looks for your returned Fresh Investigations where the returned Company Country is named this. Use with lookUpOrderBy&#x3D;CompanyDetails | [optional] 
 **company_details_name** | **str**| Looks for your returned Fresh Investigations where the returned Company Name is named this. Use with lookUpOrderBy&#x3D;CompanyDetails | [optional] 
 **search_criteria_country** | **str**| Looks for your returned Fresh Investigations where your submitted Search Criteria Company Country is this. Use with lookUpOrderBy&#x3D;searchCriteria | [optional] 
 **search_criteria_name** | **str**| Looks for your Fresh Investigations where your submitted Search Criteria Company Name is this. Use with lookUpOrderBy&#x3D;searchCriteria | [optional] 
 **sort_by** | **str**| Sorts  returned Fresh Investigations by this field | [optional] 
 **sort_dir** | **str**| The direction that you wish to sort results by. | [optional] [default to asc]

### Return type

[**ConnectFreshInvListInvestigations**](ConnectFreshInvListInvestigations.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_comments_of_specified_fresh_investigation_report**
> GetFreshInvestigationCommentsByOrderIdResponse retrieve_comments_of_specified_fresh_investigation_report(order_id)

Retrieve comments of specified FreshInvestigation Report

Returns the Fresh Investigation Report comments for a specific order.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.FreshInvestigationsApi(pycsapi.ApiClient(configuration))
order_id = 'order_id_example' # str | FreshInvestigation Report Id

try:
    # Retrieve comments of specified FreshInvestigation Report
    api_response = api_instance.retrieve_comments_of_specified_fresh_investigation_report(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreshInvestigationsApi->retrieve_comments_of_specified_fresh_investigation_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| FreshInvestigation Report Id | 

### Return type

[**GetFreshInvestigationCommentsByOrderIdResponse**](GetFreshInvestigationCommentsByOrderIdResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_fresh_investigation_order**
> ConnectFreshInvCompletedInvestigation retrieve_fresh_investigation_order(order_id, sections=sections, comments=comments)

Retrieve FreshInvestigation Order

Returns a specific Fresh Investigation order.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.FreshInvestigationsApi(pycsapi.ApiClient(configuration))
order_id = 'order_id_example' # str | 
sections = 'sections_example' # str | Specify a value to return a single section, or multiple-comma separated sections of the completed Fresh Investigation. Leave null to return all sections. Available sections; - `companyIdentification` - `creditScore` - `contactInformation` - `directors` - `otherInformation` - `groupStructure` - `extendedGroupStructure` - `financialStatements` - `negativeInformation` - `additionalInformation`- `directorships` - `localFinancialStatements` - `paymentData` - `companySummary` - `alternateSummary` (optional)
comments = 'last' # str | Selects number of comments which should be returned with the order details. (optional) (default to last)

try:
    # Retrieve FreshInvestigation Order
    api_response = api_instance.retrieve_fresh_investigation_order(order_id, sections=sections, comments=comments)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreshInvestigationsApi->retrieve_fresh_investigation_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 
 **sections** | **str**| Specify a value to return a single section, or multiple-comma separated sections of the completed Fresh Investigation. Leave null to return all sections. Available sections; - &#x60;companyIdentification&#x60; - &#x60;creditScore&#x60; - &#x60;contactInformation&#x60; - &#x60;directors&#x60; - &#x60;otherInformation&#x60; - &#x60;groupStructure&#x60; - &#x60;extendedGroupStructure&#x60; - &#x60;financialStatements&#x60; - &#x60;negativeInformation&#x60; - &#x60;additionalInformation&#x60;- &#x60;directorships&#x60; - &#x60;localFinancialStatements&#x60; - &#x60;paymentData&#x60; - &#x60;companySummary&#x60; - &#x60;alternateSummary&#x60; | [optional] 
 **comments** | **str**| Selects number of comments which should be returned with the order details. | [optional] [default to last]

### Return type

[**ConnectFreshInvCompletedInvestigation**](ConnectFreshInvCompletedInvestigation.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_fresh_investigation_report_content**
> CreditsafeGlobalDataReportsCompanyReportResponse retrieve_fresh_investigation_report_content(order_id)

Retrieve FreshInvestigation Report Content

Returns the Fresh Investigation Report data for a specific order, after the order has a status of delivered.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.FreshInvestigationsApi(pycsapi.ApiClient(configuration))
order_id = 'order_id_example' # str | 

try:
    # Retrieve FreshInvestigation Report Content
    api_response = api_instance.retrieve_fresh_investigation_report_content(order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreshInvestigationsApi->retrieve_fresh_investigation_report_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**|  | 

### Return type

[**CreditsafeGlobalDataReportsCompanyReportResponse**](CreditsafeGlobalDataReportsCompanyReportResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_fresh_investigation_report_content**
> InlineResponse2003 update_fresh_investigation_report_content(order_id, body=body)

Update FreshInvestigation Report Content

Update the Fresh Investigation Report data for a specific order, after the order has a status of delivered.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.FreshInvestigationsApi(pycsapi.ApiClient(configuration))
order_id = 'order_id_example' # str | Fresh investigation orderId
body = pycsapi.ConnectUpdateFreshInvestigation() # ConnectUpdateFreshInvestigation |  (optional)

try:
    # Update FreshInvestigation Report Content
    api_response = api_instance.update_fresh_investigation_report_content(order_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreshInvestigationsApi->update_fresh_investigation_report_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| Fresh investigation orderId | 
 **body** | [**ConnectUpdateFreshInvestigation**](ConnectUpdateFreshInvestigation.md)|  | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_attachments_for_fresh_investigation_order_id**
> FreshInvestigationAttachmentUploadForOrderResponse upload_attachments_for_fresh_investigation_order_id(import_file, description, order_id)

Upload attachments for fresh investigation orderId

Returns the status of attachment upload for the particular order.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.FreshInvestigationsApi(pycsapi.ApiClient(configuration))
import_file = 'import_file_example' # str | 
description = 'description_example' # str | 
order_id = 'order_id_example' # str | Fresh investigation orderId

try:
    # Upload attachments for fresh investigation orderId
    api_response = api_instance.upload_attachments_for_fresh_investigation_order_id(import_file, description, order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FreshInvestigationsApi->upload_attachments_for_fresh_investigation_order_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_file** | **str**|  | 
 **description** | **str**|  | 
 **order_id** | **str**| Fresh investigation orderId | 

### Return type

[**FreshInvestigationAttachmentUploadForOrderResponse**](FreshInvestigationAttachmentUploadForOrderResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


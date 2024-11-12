# pycsapi.KYCProfileUpdatesApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**k_yc_protect_add_an_attachment_to_the_given_profile**](KYCProfileUpdatesApi.md#k_yc_protect_add_an_attachment_to_the_given_profile) | **POST** /compliance/kyc-protect/profiles/{profileId}/attachments | Add An Attachment To The Given Profile
[**k_yc_protect_get_list_of_attachments_on_the_given_profile**](KYCProfileUpdatesApi.md#k_yc_protect_get_list_of_attachments_on_the_given_profile) | **GET** /compliance/kyc-protect/profiles/{profileId}/attachments | Return List Of Attachments On The Given Profile
[**protect_delete_kyc_profile_attachment_by_profile_id_and_attachment_id**](KYCProfileUpdatesApi.md#protect_delete_kyc_profile_attachment_by_profile_id_and_attachment_id) | **DELETE** /compliance/kyc-protect/profiles/{profileId}/attachments/{attachmentId} | Delete Attachment By Profile And Attachment Id
[**protect_deletekyc_profile_id_by_note_id**](KYCProfileUpdatesApi.md#protect_deletekyc_profile_id_by_note_id) | **DELETE** /compliance/kyc-protect/profiles/{profileId}/notes/{noteId} | Deletes Profile Note By Note Id
[**protect_download_kyc_profile_attachment_by_profile_id_and_attachment_id**](KYCProfileUpdatesApi.md#protect_download_kyc_profile_attachment_by_profile_id_and_attachment_id) | **GET** /compliance/kyc-protect/profiles/{profileId}/attachments/{attachmentId}/download | Download Profile Attachment By Profile And Attachment Id
[**protect_getkyc_profile_attachment_by_profile_id_and_attachment_id**](KYCProfileUpdatesApi.md#protect_getkyc_profile_attachment_by_profile_id_and_attachment_id) | **GET** /compliance/kyc-protect/profiles/{profileId}/attachments/{attachmentId} | Return A Profile Attachment By Profile And Attachment Id
[**protect_getkyc_profile_notes**](KYCProfileUpdatesApi.md#protect_getkyc_profile_notes) | **GET** /compliance/kyc-protect/profiles/{profileId}/notes | Return Profile Notes
[**protect_getkyc_profile_notes_by_note_id**](KYCProfileUpdatesApi.md#protect_getkyc_profile_notes_by_note_id) | **GET** /compliance/kyc-protect/profiles/{profileId}/notes/{noteId} | Return Profile Notes By Note Id
[**protect_postkyc_profile_notes**](KYCProfileUpdatesApi.md#protect_postkyc_profile_notes) | **POST** /compliance/kyc-protect/profiles/{profileId}/notes | Create Profile Note
[**protect_put_kyc_profile_attachment_by_profile_id_and_attachment_id**](KYCProfileUpdatesApi.md#protect_put_kyc_profile_attachment_by_profile_id_and_attachment_id) | **PUT** /compliance/kyc-protect/profiles/{profileId}/attachments/{attachmentId} | Update Profile Attachment By Profile And Attachment Id
[**protect_update_kyc_profile_notes_by_note_id**](KYCProfileUpdatesApi.md#protect_update_kyc_profile_notes_by_note_id) | **PUT** /compliance/kyc-protect/profiles/{profileId}/notes/{noteId} | Update Profile Note By Note Id
[**protect_updates_kyc_profile_by_id**](KYCProfileUpdatesApi.md#protect_updates_kyc_profile_by_id) | **PUT** /compliance/kyc-protect/profiles/{profileId} | Update Profile By Profile Id

# **k_yc_protect_add_an_attachment_to_the_given_profile**
> KycProtectProfileAttachmentResponse k_yc_protect_add_an_attachment_to_the_given_profile(profile_id, file=file, document_type=document_type, description=description)

Add An Attachment To The Given Profile

Adds an attachment to a profile. Returns the details of the added attachment.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileUpdatesApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile
file = 'file_example' # str |  (optional)
document_type = 'document_type_example' # str |  (optional)
description = 'description_example' # str |  (optional)

try:
    # Add An Attachment To The Given Profile
    api_response = api_instance.k_yc_protect_add_an_attachment_to_the_given_profile(profile_id, file=file, document_type=document_type, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileUpdatesApi->k_yc_protect_add_an_attachment_to_the_given_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| id of the profile | 
 **file** | **str**|  | [optional] 
 **document_type** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 

### Return type

[**KycProtectProfileAttachmentResponse**](KycProtectProfileAttachmentResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_yc_protect_get_list_of_attachments_on_the_given_profile**
> InlineResponse20011 k_yc_protect_get_list_of_attachments_on_the_given_profile(profile_id, page=page, page_size=page_size)

Return List Of Attachments On The Given Profile

Gets a list of attachments on the given profile ordered by modified date.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileUpdatesApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile
page = 56 # int | The page number to fetch. Should be a positive integer. (optional)
page_size = 10 # int | Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. (optional) (default to 10)

try:
    # Return List Of Attachments On The Given Profile
    api_response = api_instance.k_yc_protect_get_list_of_attachments_on_the_given_profile(profile_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileUpdatesApi->k_yc_protect_get_list_of_attachments_on_the_given_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| id of the profile | 
 **page** | **int**| The page number to fetch. Should be a positive integer. | [optional] 
 **page_size** | **int**| Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. | [optional] [default to 10]

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_delete_kyc_profile_attachment_by_profile_id_and_attachment_id**
> protect_delete_kyc_profile_attachment_by_profile_id_and_attachment_id(profile_id, attachment_id)

Delete Attachment By Profile And Attachment Id

Deletes A Profile Attachment By Profile And Attachment Id

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileUpdatesApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of a profile.
attachment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of a attachmentId.

try:
    # Delete Attachment By Profile And Attachment Id
    api_instance.protect_delete_kyc_profile_attachment_by_profile_id_and_attachment_id(profile_id, attachment_id)
except ApiException as e:
    print("Exception when calling KYCProfileUpdatesApi->protect_delete_kyc_profile_attachment_by_profile_id_and_attachment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| Id of a profile. | 
 **attachment_id** | [**str**](.md)| Id of a attachmentId. | 

### Return type

void (empty response body)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_deletekyc_profile_id_by_note_id**
> protect_deletekyc_profile_id_by_note_id(profile_id, note_id)

Deletes Profile Note By Note Id

Deletes a profile note based on profile id and note id.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileUpdatesApi(pycsapi.ApiClient(configuration))
profile_id = 'profile_id_example' # str | Id of a profile.
note_id = 'note_id_example' # str | Id of a note.

try:
    # Deletes Profile Note By Note Id
    api_instance.protect_deletekyc_profile_id_by_note_id(profile_id, note_id)
except ApiException as e:
    print("Exception when calling KYCProfileUpdatesApi->protect_deletekyc_profile_id_by_note_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Id of a profile. | 
 **note_id** | **str**| Id of a note. | 

### Return type

void (empty response body)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_download_kyc_profile_attachment_by_profile_id_and_attachment_id**
> DownloadAttachmentResponse protect_download_kyc_profile_attachment_by_profile_id_and_attachment_id(profile_id, attachment_id)

Download Profile Attachment By Profile And Attachment Id

Gets profile attachment's download link.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileUpdatesApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of a profile.
attachment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of a note.

try:
    # Download Profile Attachment By Profile And Attachment Id
    api_response = api_instance.protect_download_kyc_profile_attachment_by_profile_id_and_attachment_id(profile_id, attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileUpdatesApi->protect_download_kyc_profile_attachment_by_profile_id_and_attachment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| Id of a profile. | 
 **attachment_id** | [**str**](.md)| Id of a note. | 

### Return type

[**DownloadAttachmentResponse**](DownloadAttachmentResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_getkyc_profile_attachment_by_profile_id_and_attachment_id**
> GetKYCProfileAttachmentDetailsByAttachmentId protect_getkyc_profile_attachment_by_profile_id_and_attachment_id(profile_id, attachment_id)

Return A Profile Attachment By Profile And Attachment Id

Returns an attachment by the provided attachment Id and profile Id.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileUpdatesApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of a profile.
attachment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of an attachment.

try:
    # Return A Profile Attachment By Profile And Attachment Id
    api_response = api_instance.protect_getkyc_profile_attachment_by_profile_id_and_attachment_id(profile_id, attachment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileUpdatesApi->protect_getkyc_profile_attachment_by_profile_id_and_attachment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| Id of a profile. | 
 **attachment_id** | [**str**](.md)| Id of an attachment. | 

### Return type

[**GetKYCProfileAttachmentDetailsByAttachmentId**](GetKYCProfileAttachmentDetailsByAttachmentId.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_getkyc_profile_notes**
> GetKYCProtectProfileIdNotesResponse protect_getkyc_profile_notes(profile_id, page=page, page_size=page_size, search_term=search_term, is_archived=is_archived)

Return Profile Notes

Returns a list of profile notes for the given profile id.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileUpdatesApi(pycsapi.ApiClient(configuration))
profile_id = 'profile_id_example' # str | Id of a profile.
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 10 # int | Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. (optional) (default to 10)
search_term = 'search_term_example' # str | Filters the note list by notes with body containing the provided string (optional)
is_archived = true # bool | Get archived notes based on this flag. Allowed values are true, false or null (optional)

try:
    # Return Profile Notes
    api_response = api_instance.protect_getkyc_profile_notes(profile_id, page=page, page_size=page_size, search_term=search_term, is_archived=is_archived)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileUpdatesApi->protect_getkyc_profile_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Id of a profile. | 
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. | [optional] [default to 10]
 **search_term** | **str**| Filters the note list by notes with body containing the provided string | [optional] 
 **is_archived** | **bool**| Get archived notes based on this flag. Allowed values are true, false or null | [optional] 

### Return type

[**GetKYCProtectProfileIdNotesResponse**](GetKYCProtectProfileIdNotesResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_getkyc_profile_notes_by_note_id**
> GetKYCProtectProfileIdNoteIdResponse protect_getkyc_profile_notes_by_note_id(profile_id, note_id)

Return Profile Notes By Note Id

Returns a profile note based on profile id and note id.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileUpdatesApi(pycsapi.ApiClient(configuration))
profile_id = 'profile_id_example' # str | Id of a profile.
note_id = 'note_id_example' # str | Id of a note.

try:
    # Return Profile Notes By Note Id
    api_response = api_instance.protect_getkyc_profile_notes_by_note_id(profile_id, note_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileUpdatesApi->protect_getkyc_profile_notes_by_note_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Id of a profile. | 
 **note_id** | **str**| Id of a note. | 

### Return type

[**GetKYCProtectProfileIdNoteIdResponse**](GetKYCProtectProfileIdNoteIdResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_postkyc_profile_notes**
> PostKYCProfileNotes protect_postkyc_profile_notes(profile_id, body=body)

Create Profile Note

Adds a note to a profile then Returns the details of the added note.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileUpdatesApi(pycsapi.ApiClient(configuration))
profile_id = 'profile_id_example' # str | Id of a profile.
body = pycsapi.PostKYCProfileNotesRequest() # PostKYCProfileNotesRequest |  (optional)

try:
    # Create Profile Note
    api_response = api_instance.protect_postkyc_profile_notes(profile_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileUpdatesApi->protect_postkyc_profile_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Id of a profile. | 
 **body** | [**PostKYCProfileNotesRequest**](PostKYCProfileNotesRequest.md)|  | [optional] 

### Return type

[**PostKYCProfileNotes**](PostKYCProfileNotes.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_put_kyc_profile_attachment_by_profile_id_and_attachment_id**
> UpdateKYCAttachmentsByAttachmentId protect_put_kyc_profile_attachment_by_profile_id_and_attachment_id(profile_id, attachment_id, document_type=document_type, description=description)

Update Profile Attachment By Profile And Attachment Id

Updates A Profile Attachment By Profile And Attachment Id

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileUpdatesApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of a profile.
attachment_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of a attachmentId.
document_type = 'document_type_example' # str |  (optional)
description = 'description_example' # str |  (optional)

try:
    # Update Profile Attachment By Profile And Attachment Id
    api_response = api_instance.protect_put_kyc_profile_attachment_by_profile_id_and_attachment_id(profile_id, attachment_id, document_type=document_type, description=description)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileUpdatesApi->protect_put_kyc_profile_attachment_by_profile_id_and_attachment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| Id of a profile. | 
 **attachment_id** | [**str**](.md)| Id of a attachmentId. | 
 **document_type** | **str**|  | [optional] 
 **description** | **str**|  | [optional] 

### Return type

[**UpdateKYCAttachmentsByAttachmentId**](UpdateKYCAttachmentsByAttachmentId.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_update_kyc_profile_notes_by_note_id**
> PutKYCProfileNotesByNoteId protect_update_kyc_profile_notes_by_note_id(profile_id, note_id, body=body)

Update Profile Note By Note Id

Updates a profile note based on profile id and note id.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileUpdatesApi(pycsapi.ApiClient(configuration))
profile_id = 'profile_id_example' # str | Id of a profile.
note_id = 'note_id_example' # str | Id of a note.
body = pycsapi.PutKYCProfileNotesByNoteIdRequest() # PutKYCProfileNotesByNoteIdRequest |  (optional)

try:
    # Update Profile Note By Note Id
    api_response = api_instance.protect_update_kyc_profile_notes_by_note_id(profile_id, note_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileUpdatesApi->protect_update_kyc_profile_notes_by_note_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Id of a profile. | 
 **note_id** | **str**| Id of a note. | 
 **body** | [**PutKYCProfileNotesByNoteIdRequest**](PutKYCProfileNotesByNoteIdRequest.md)|  | [optional] 

### Return type

[**PutKYCProfileNotesByNoteId**](PutKYCProfileNotesByNoteId.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_updates_kyc_profile_by_id**
> UpdateKYCProfileByProfileId protect_updates_kyc_profile_by_id(profile_id, body=body)

Update Profile By Profile Id

Updates a single profile by profile Id.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileUpdatesApi(pycsapi.ApiClient(configuration))
profile_id = 'profile_id_example' # str | Id of a profile.
body = pycsapi.UpdateKYCProfileByProfileIdRequest() # UpdateKYCProfileByProfileIdRequest |  (optional)

try:
    # Update Profile By Profile Id
    api_response = api_instance.protect_updates_kyc_profile_by_id(profile_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileUpdatesApi->protect_updates_kyc_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Id of a profile. | 
 **body** | [**UpdateKYCProfileByProfileIdRequest**](UpdateKYCProfileByProfileIdRequest.md)|  | [optional] 

### Return type

[**UpdateKYCProfileByProfileId**](UpdateKYCProfileByProfileId.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


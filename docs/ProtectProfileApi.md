# pycsapi.ProtectProfileApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_investigation_to_profile**](ProtectProfileApi.md#add_investigation_to_profile) | **PUT** /protect/profiles/{profileId}/investigations/{investigationId} | Add Investigation To Profile
[**create_protect_profile**](ProtectProfileApi.md#create_protect_profile) | **POST** /protect/profiles | Create Protect Profile
[**edit_protect_profile**](ProtectProfileApi.md#edit_protect_profile) | **PUT** /protect/profiles/{profileId} | Edit Protect Profile
[**list_all_protect_profiles**](ProtectProfileApi.md#list_all_protect_profiles) | **GET** /protect/profiles | List All Protect Profiles
[**list_investigations_in_a_profile**](ProtectProfileApi.md#list_investigations_in_a_profile) | **GET** /protect/profiles/{profileId}/investigations | List Investigations In A Profile.
[**retrieve_protect_profile_by_id**](ProtectProfileApi.md#retrieve_protect_profile_by_id) | **GET** /protect/profiles/{profileId} | Retrieve Protect Profile By ID

# **add_investigation_to_profile**
> add_investigation_to_profile(profile_id, investigation_id)

Add Investigation To Profile

Adds an Investigation to a Profile.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectProfileApi(pycsapi.ApiClient(configuration))
profile_id = 'profile_id_example' # str | 
investigation_id = 'investigation_id_example' # str | 

try:
    # Add Investigation To Profile
    api_instance.add_investigation_to_profile(profile_id, investigation_id)
except ApiException as e:
    print("Exception when calling ProtectProfileApi->add_investigation_to_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 
 **investigation_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_protect_profile**
> ConnectProtectProfile create_protect_profile(body)

Create Protect Profile

Creates an empty profile for collating investigations.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectProfileApi(pycsapi.ApiClient(configuration))
body = pycsapi.ConnectProtectCreateProfileDto() # ConnectProtectCreateProfileDto | 

try:
    # Create Protect Profile
    api_response = api_instance.create_protect_profile(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectProfileApi->create_protect_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectProtectCreateProfileDto**](ConnectProtectCreateProfileDto.md)|  | 

### Return type

[**ConnectProtectProfile**](ConnectProtectProfile.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_protect_profile**
> ConnectProtectProfile edit_protect_profile(body, profile_id)

Edit Protect Profile

Endpoint to change the name of a profile.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectProfileApi(pycsapi.ApiClient(configuration))
body = pycsapi.ConnectProtectCreateProfileDto() # ConnectProtectCreateProfileDto | 
profile_id = 'profile_id_example' # str | 

try:
    # Edit Protect Profile
    api_response = api_instance.edit_protect_profile(body, profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectProfileApi->edit_protect_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectProtectCreateProfileDto**](ConnectProtectCreateProfileDto.md)|  | 
 **profile_id** | **str**|  | 

### Return type

[**ConnectProtectProfile**](ConnectProtectProfile.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all_protect_profiles**
> list[ConnectProtectProfile] list_all_protect_profiles(name=name, page=page, page_size=page_size)

List All Protect Profiles

Returns all profiles for the logged in user or filtered with a matching profile name.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectProfileApi(pycsapi.ApiClient(configuration))
name = 'name_example' # str |  (optional)
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 56 # int | Number of items to return per Page. (optional)

try:
    # List All Protect Profiles
    api_response = api_instance.list_all_protect_profiles(name=name, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectProfileApi->list_all_protect_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Number of items to return per Page. | [optional] 

### Return type

[**list[ConnectProtectProfile]**](ConnectProtectProfile.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_investigations_in_a_profile**
> list[ConnectProtectInvestigation] list_investigations_in_a_profile(profile_id, query_type=query_type, page=page, page_size=page_size)

List Investigations In A Profile.

Endpoint to retrieve all Investigations associated with a specific Profile.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectProfileApi(pycsapi.ApiClient(configuration))
profile_id = 'profile_id_example' # str | 
query_type = pycsapi.ConnectProtectCreateInvestigationQueryDto() # ConnectProtectCreateInvestigationQueryDto |  (optional)
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 56 # int | Number of items to return per Page. (optional)

try:
    # List Investigations In A Profile.
    api_response = api_instance.list_investigations_in_a_profile(profile_id, query_type=query_type, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectProfileApi->list_investigations_in_a_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 
 **query_type** | [**ConnectProtectCreateInvestigationQueryDto**](.md)|  | [optional] 
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

# **retrieve_protect_profile_by_id**
> ConnectProtectProfile retrieve_protect_profile_by_id(profile_id)

Retrieve Protect Profile By ID

Retrieves a profile by Id in the Path.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ProtectProfileApi(pycsapi.ApiClient(configuration))
profile_id = 'profile_id_example' # str | 

try:
    # Retrieve Protect Profile By ID
    api_response = api_instance.retrieve_protect_profile_by_id(profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProtectProfileApi->retrieve_protect_profile_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 

### Return type

[**ConnectProtectProfile**](ConnectProtectProfile.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


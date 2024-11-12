# pycsapi.KYCProfileManagementApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compliance_protect_delete_kyc_profiles**](KYCProfileManagementApi.md#compliance_protect_delete_kyc_profiles) | **DELETE** /compliance/kyc-protect/profiles | Delete All Profiles
[**compliance_protect_get_kyc_profiles**](KYCProfileManagementApi.md#compliance_protect_get_kyc_profiles) | **GET** /compliance/kyc-protect/profiles | Return Created Profiles
[**k_yc_protect_assigns_list_of_profiles_to_user**](KYCProfileManagementApi.md#k_yc_protect_assigns_list_of_profiles_to_user) | **PUT** /compliance/kyc-protect/profiles/assign/bulk | Assigns A List Of Profiles To User
[**k_yc_protect_create_profile**](KYCProfileManagementApi.md#k_yc_protect_create_profile) | **POST** /compliance/kyc-protect/profiles | Create Profile
[**protect_assign_profiles**](KYCProfileManagementApi.md#protect_assign_profiles) | **PUT** /compliance/kyc-protect/profiles/assign | Assign Profile To User
[**protect_delete_kyc_profiles_by_id**](KYCProfileManagementApi.md#protect_delete_kyc_profiles_by_id) | **DELETE** /compliance/kyc-protect/profiles/{profileId} | Delete Profile By Profile Id
[**protect_get_kyc_profiles_by_profile_id**](KYCProfileManagementApi.md#protect_get_kyc_profiles_by_profile_id) | **GET** /compliance/kyc-protect/profiles/{profileId} | Return Profile By Profile Id

# **compliance_protect_delete_kyc_profiles**
> bool compliance_protect_delete_kyc_profiles(body=body)

Delete All Profiles

Deletes list of profiles. <br>This will delete all its dependencies/child items associated to that profileId.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileManagementApi(pycsapi.ApiClient(configuration))
body = ['body_example'] # list[str] |  (optional)

try:
    # Delete All Profiles
    api_response = api_instance.compliance_protect_delete_kyc_profiles(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileManagementApi->compliance_protect_delete_kyc_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[str]**](str.md)|  | [optional] 

### Return type

**bool**

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliance_protect_get_kyc_profiles**
> GetKYCProfiles compliance_protect_get_kyc_profiles(page=page, page_size=page_size, search_term=search_term, assignees=assignees, kyc_review_after=kyc_review_after, kyc_review_before=kyc_review_before, risk_ratings=risk_ratings, sort_order=sort_order, sort_by=sort_by)

Return Created Profiles

Returns a list of profiles ordered by modified date.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileManagementApi(pycsapi.ApiClient(configuration))
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 10 # int | Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. (optional) (default to 10)
search_term = 'search_term_example' # str | A search term to filter by. The search term will be matched against names, and internal ids containing the search term. (optional)
assignees = 56 # int | The ids of assigned users to filter by. (optional)
kyc_review_after = '2013-10-20' # date | Filters results based on profiles with a kyc review date after this date. (optional)
kyc_review_before = '2013-10-20' # date | Filters results based on profiles with a kyc review date after this date. (optional)
risk_ratings = ['risk_ratings_example'] # list[str] | The risk ratings to filter by. Available values: notApplicable, veryLow, low, medium, high, veryHigh (optional)
sort_order = 'sort_order_example' # str | The order in which the items should be sorted. Available values: asc, desc (optional)
sort_by = 'sort_by_example' # str | The field by which the items should be sorted. Available values: modifiedAt, name (optional)

try:
    # Return Created Profiles
    api_response = api_instance.compliance_protect_get_kyc_profiles(page=page, page_size=page_size, search_term=search_term, assignees=assignees, kyc_review_after=kyc_review_after, kyc_review_before=kyc_review_before, risk_ratings=risk_ratings, sort_order=sort_order, sort_by=sort_by)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileManagementApi->compliance_protect_get_kyc_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. | [optional] [default to 10]
 **search_term** | **str**| A search term to filter by. The search term will be matched against names, and internal ids containing the search term. | [optional] 
 **assignees** | **int**| The ids of assigned users to filter by. | [optional] 
 **kyc_review_after** | **date**| Filters results based on profiles with a kyc review date after this date. | [optional] 
 **kyc_review_before** | **date**| Filters results based on profiles with a kyc review date after this date. | [optional] 
 **risk_ratings** | [**list[str]**](str.md)| The risk ratings to filter by. Available values: notApplicable, veryLow, low, medium, high, veryHigh | [optional] 
 **sort_order** | **str**| The order in which the items should be sorted. Available values: asc, desc | [optional] 
 **sort_by** | **str**| The field by which the items should be sorted. Available values: modifiedAt, name | [optional] 

### Return type

[**GetKYCProfiles**](GetKYCProfiles.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_yc_protect_assigns_list_of_profiles_to_user**
> list[KycProtectProfileAssignBulkResponse] k_yc_protect_assigns_list_of_profiles_to_user(body=body)

Assigns A List Of Profiles To User

Assigns list of profiles to a user.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileManagementApi(pycsapi.ApiClient(configuration))
body = pycsapi.MODEL4df4ca() # MODEL4df4ca |  (optional)

try:
    # Assigns A List Of Profiles To User
    api_response = api_instance.k_yc_protect_assigns_list_of_profiles_to_user(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileManagementApi->k_yc_protect_assigns_list_of_profiles_to_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MODEL4df4ca**](MODEL4df4ca.md)|  | [optional] 

### Return type

[**list[KycProtectProfileAssignBulkResponse]**](KycProtectProfileAssignBulkResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_yc_protect_create_profile**
> KycProtectProfileCreatedResponse k_yc_protect_create_profile(body=body)

Create Profile

Uses the name and type provided by the user to create a profile.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileManagementApi(pycsapi.ApiClient(configuration))
body = pycsapi.KycProtectPostProfilesRequest() # KycProtectPostProfilesRequest |  (optional)

try:
    # Create Profile
    api_response = api_instance.k_yc_protect_create_profile(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileManagementApi->k_yc_protect_create_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KycProtectPostProfilesRequest**](KycProtectPostProfilesRequest.md)|  | [optional] 

### Return type

[**KycProtectProfileCreatedResponse**](KycProtectProfileCreatedResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_assign_profiles**
> PutKYCProfileAssign protect_assign_profiles(profile_id, user_id=user_id)

Assign Profile To User

Assign a profile to a user

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileManagementApi(pycsapi.ApiClient(configuration))
profile_id = 'profile_id_example' # str | Id of the profile being assigned to a user
user_id = 'user_id_example' # str | User Id to assign the Profile to (optional)

try:
    # Assign Profile To User
    api_response = api_instance.protect_assign_profiles(profile_id, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileManagementApi->protect_assign_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Id of the profile being assigned to a user | 
 **user_id** | **str**| User Id to assign the Profile to | [optional] 

### Return type

[**PutKYCProfileAssign**](PutKYCProfileAssign.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_delete_kyc_profiles_by_id**
> protect_delete_kyc_profiles_by_id(profile_id)

Delete Profile By Profile Id

Deletes a single profile by id.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileManagementApi(pycsapi.ApiClient(configuration))
profile_id = 'profile_id_example' # str | Id of a profile.

try:
    # Delete Profile By Profile Id
    api_instance.protect_delete_kyc_profiles_by_id(profile_id)
except ApiException as e:
    print("Exception when calling KYCProfileManagementApi->protect_delete_kyc_profiles_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Id of a profile. | 

### Return type

void (empty response body)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_get_kyc_profiles_by_profile_id**
> GetKYCProfileByProfileId protect_get_kyc_profiles_by_profile_id(profile_id)

Return Profile By Profile Id

Returns a single profile by id.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileManagementApi(pycsapi.ApiClient(configuration))
profile_id = 'profile_id_example' # str | Id of a profile.

try:
    # Return Profile By Profile Id
    api_response = api_instance.protect_get_kyc_profiles_by_profile_id(profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileManagementApi->protect_get_kyc_profiles_by_profile_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Id of a profile. | 

### Return type

[**GetKYCProfileByProfileId**](GetKYCProfileByProfileId.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


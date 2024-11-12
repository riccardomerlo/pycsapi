# pycsapi.KYCAMLScreeningProfileManagementApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_kyc_profile_searches_by_profile_id**](KYCAMLScreeningProfileManagementApi.md#delete_kyc_profile_searches_by_profile_id) | **DELETE** /compliance/kyc-protect/profiles/{profileId}/searches/link | Deletes AML searches linked to a profile
[**getkychitsofthesearcheslinkedtoprofile**](KYCAMLScreeningProfileManagementApi.md#getkychitsofthesearcheslinkedtoprofile) | **GET** /compliance/kyc-protect/profiles/{profileId}/hits | Return All Hits Of Searches Linked To A Profile
[**k_yc_protect_adds_a_search_to_the_given_profile**](KYCAMLScreeningProfileManagementApi.md#k_yc_protect_adds_a_search_to_the_given_profile) | **POST** /compliance/kyc-protect/profiles/{profileId}/searches/link | Adds AML Searches To The Given Profile
[**k_yc_protect_get_aml_alerts_by_profile_id**](KYCAMLScreeningProfileManagementApi.md#k_yc_protect_get_aml_alerts_by_profile_id) | **GET** /compliance/kyc-protect/profiles/{profileId}/amlAlerts | Return All Hits Linked To The Profile
[**k_yc_protect_get_profile_schedules**](KYCAMLScreeningProfileManagementApi.md#k_yc_protect_get_profile_schedules) | **GET** /compliance/kyc-protect/profiles/{profileId}/schedules | Return All Schedules By ProfileId And Modified Date
[**k_yc_protect_get_profile_schedules_by_schedule_id**](KYCAMLScreeningProfileManagementApi.md#k_yc_protect_get_profile_schedules_by_schedule_id) | **GET** /compliance/kyc-protect/profiles/{profileId}/schedules/{scheduleId} | Return Schedule By ProfileId And ScheduleId
[**k_yc_protect_get_s_list_of_searches_on_the_given_profile**](KYCAMLScreeningProfileManagementApi.md#k_yc_protect_get_s_list_of_searches_on_the_given_profile) | **GET** /compliance/kyc-protect/profiles/{profileId}/searches | Return List Of AML Searches On The Given Profile

# **delete_kyc_profile_searches_by_profile_id**
> DeleteKYCProfileSearchesByProfileIdResponse delete_kyc_profile_searches_by_profile_id(body, profile_id)

Deletes AML searches linked to a profile

Deletes AML searches from a profile by profile Id and Search Id.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningProfileManagementApi(pycsapi.ApiClient(configuration))
body = pycsapi.DeleteKYCProfileSearchesByProfileIdRequestBody() # DeleteKYCProfileSearchesByProfileIdRequestBody | 
profile_id = 'profile_id_example' # str | Id of a profile.

try:
    # Deletes AML searches linked to a profile
    api_response = api_instance.delete_kyc_profile_searches_by_profile_id(body, profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningProfileManagementApi->delete_kyc_profile_searches_by_profile_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteKYCProfileSearchesByProfileIdRequestBody**](DeleteKYCProfileSearchesByProfileIdRequestBody.md)|  | 
 **profile_id** | **str**| Id of a profile. | 

### Return type

[**DeleteKYCProfileSearchesByProfileIdResponse**](DeleteKYCProfileSearchesByProfileIdResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getkychitsofthesearcheslinkedtoprofile**
> GetProfileHitsByProfileIdResponse getkychitsofthesearcheslinkedtoprofile(profile_id, hit_decisions=hit_decisions, page=page, page_size=page_size)

Return All Hits Of Searches Linked To A Profile

Return hits of the searches linked to a profile.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningProfileManagementApi(pycsapi.ApiClient(configuration))
profile_id = 'profile_id_example' # str | Id of the profile
hit_decisions = ['hit_decisions_example'] # list[str] | The hit decisions. It can be the collection of undecided, truematch, falsepositive, discarded (optional)
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 10 # int | Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. (optional) (default to 10)

try:
    # Return All Hits Of Searches Linked To A Profile
    api_response = api_instance.getkychitsofthesearcheslinkedtoprofile(profile_id, hit_decisions=hit_decisions, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningProfileManagementApi->getkychitsofthesearcheslinkedtoprofile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Id of the profile | 
 **hit_decisions** | [**list[str]**](str.md)| The hit decisions. It can be the collection of undecided, truematch, falsepositive, discarded | [optional] 
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. | [optional] [default to 10]

### Return type

[**GetProfileHitsByProfileIdResponse**](GetProfileHitsByProfileIdResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_yc_protect_adds_a_search_to_the_given_profile**
> InlineResponse20012 k_yc_protect_adds_a_search_to_the_given_profile(profile_id, body=body)

Adds AML Searches To The Given Profile

Adds a list of searches to a profile.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningProfileManagementApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile
body = pycsapi.SearchesLinkBody1() # SearchesLinkBody1 |  (optional)

try:
    # Adds AML Searches To The Given Profile
    api_response = api_instance.k_yc_protect_adds_a_search_to_the_given_profile(profile_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningProfileManagementApi->k_yc_protect_adds_a_search_to_the_given_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| id of the profile | 
 **body** | [**SearchesLinkBody1**](SearchesLinkBody1.md)|  | [optional] 

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_yc_protect_get_aml_alerts_by_profile_id**
> InlineResponse20015 k_yc_protect_get_aml_alerts_by_profile_id(profile_id, page=page, page_size=page_size, hit_decisions=hit_decisions)

Return All Hits Linked To The Profile

Returns hits of all searches linked to the profile and key parties.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningProfileManagementApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 10 # int | Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. (optional) (default to 10)
hit_decisions = ['hit_decisions_example'] # list[str] | The hit decisions to filter by. It can be the collection of undecided, truematch, falsepositive, discarded (optional)

try:
    # Return All Hits Linked To The Profile
    api_response = api_instance.k_yc_protect_get_aml_alerts_by_profile_id(profile_id, page=page, page_size=page_size, hit_decisions=hit_decisions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningProfileManagementApi->k_yc_protect_get_aml_alerts_by_profile_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| id of the profile | 
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. | [optional] [default to 10]
 **hit_decisions** | [**list[str]**](str.md)| The hit decisions to filter by. It can be the collection of undecided, truematch, falsepositive, discarded | [optional] 

### Return type

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_yc_protect_get_profile_schedules**
> KYCProfileScheduleResponse k_yc_protect_get_profile_schedules(profile_id, page=page, page_size=page_size)

Return All Schedules By ProfileId And Modified Date

Returns all schedules based on profileId ordered by modified date.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningProfileManagementApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 10 # int | Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. (optional) (default to 10)

try:
    # Return All Schedules By ProfileId And Modified Date
    api_response = api_instance.k_yc_protect_get_profile_schedules(profile_id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningProfileManagementApi->k_yc_protect_get_profile_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| id of the profile | 
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. | [optional] [default to 10]

### Return type

[**KYCProfileScheduleResponse**](KYCProfileScheduleResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_yc_protect_get_profile_schedules_by_schedule_id**
> InlineResponse20014 k_yc_protect_get_profile_schedules_by_schedule_id(profile_id, schedule_id)

Return Schedule By ProfileId And ScheduleId

Returns a schedule by profileId and scheduleId.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningProfileManagementApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile
schedule_id = 'schedule_id_example' # str | id of the schedule

try:
    # Return Schedule By ProfileId And ScheduleId
    api_response = api_instance.k_yc_protect_get_profile_schedules_by_schedule_id(profile_id, schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningProfileManagementApi->k_yc_protect_get_profile_schedules_by_schedule_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| id of the profile | 
 **schedule_id** | **str**| id of the schedule | 

### Return type

[**InlineResponse20014**](InlineResponse20014.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_yc_protect_get_s_list_of_searches_on_the_given_profile**
> MODEL5941c0 k_yc_protect_get_s_list_of_searches_on_the_given_profile(profile_id, page=page, page_size=page_size, is_scheduled=is_scheduled)

Return List Of AML Searches On The Given Profile

Returns a list of searches both business and individual associated to the profile for the profile Id.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningProfileManagementApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 10 # int | Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. (optional) (default to 10)
is_scheduled = true # bool |  (optional)

try:
    # Return List Of AML Searches On The Given Profile
    api_response = api_instance.k_yc_protect_get_s_list_of_searches_on_the_given_profile(profile_id, page=page, page_size=page_size, is_scheduled=is_scheduled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningProfileManagementApi->k_yc_protect_get_s_list_of_searches_on_the_given_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| id of the profile | 
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. | [optional] [default to 10]
 **is_scheduled** | **bool**|  | [optional] 

### Return type

[**MODEL5941c0**](MODEL5941c0.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


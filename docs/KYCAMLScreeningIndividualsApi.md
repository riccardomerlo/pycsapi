# pycsapi.KYCAMLScreeningIndividualsApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compliance_kyc_protect_create_individuals_search**](KYCAMLScreeningIndividualsApi.md#compliance_kyc_protect_create_individuals_search) | **POST** /compliance/kyc-protect/searches/individuals | Performs An AML Search For An Individual And Saves The Results To The Database
[**compliance_kyc_protect_get_individuals_search**](KYCAMLScreeningIndividualsApi.md#compliance_kyc_protect_get_individuals_search) | **GET** /compliance/kyc-protect/searches/individuals | Returns Individual AML Searches
[**compliance_kyc_protect_update_individuals_search**](KYCAMLScreeningIndividualsApi.md#compliance_kyc_protect_update_individuals_search) | **PUT** /compliance/kyc-protect/searches/individuals | Update Individual AML Searches
[**gets_an_individual_search_for_the_current_logged_in_users_customer_based_on_search_id**](KYCAMLScreeningIndividualsApi.md#gets_an_individual_search_for_the_current_logged_in_users_customer_based_on_search_id) | **GET** /compliance/kyc-protect/searches/individuals/{searchId} | Return Individual AML Search By Search Id
[**gets_the_individual_search_hits**](KYCAMLScreeningIndividualsApi.md#gets_the_individual_search_hits) | **GET** /compliance/kyc-protect/searches/individuals/{searchId}/hits | Returns Individual AML Search Hits
[**returns_full_profile_information_of_a_individual_hit_by_hit_id**](KYCAMLScreeningIndividualsApi.md#returns_full_profile_information_of_a_individual_hit_by_hit_id) | **GET** /compliance/kyc-protect/searches/individuals/{searchId}/hits/{hitId} | Return Full AML Search Hit Information By SearchId And HitId
[**update_single_individual_hit**](KYCAMLScreeningIndividualsApi.md#update_single_individual_hit) | **PUT** /compliance/kyc-protect/searches/individuals/{searchId}/hits/{hitId} | Update A Single Individual Hit
[**updates_a_batch_of_individual_hits**](KYCAMLScreeningIndividualsApi.md#updates_a_batch_of_individual_hits) | **PUT** /compliance/kyc-protect/searches/individuals/{searchId}/hits | Updates A Batch Of individual AML search Hits
[**updates_an_individual_search**](KYCAMLScreeningIndividualsApi.md#updates_an_individual_search) | **PUT** /compliance/kyc-protect/searches/individuals/{searchId} | Updates An Individual AML Search By SearchID

# **compliance_kyc_protect_create_individuals_search**
> KycProtectPostPostIndividualSearchResponse compliance_kyc_protect_create_individuals_search(body=body)

Performs An AML Search For An Individual And Saves The Results To The Database

A request requires a name, or first name and last name, at least one valid dataset and a threshold.<br><br> Length of name or combination of first name, middle name and last name must not exceed 200 characters. If user is providing first name, middle name and last name combination, the max characters limit includes the formatted name in this format {lastName} {firstName} {middleName}.<br><br> User will be deducted 1 credit for each search.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningIndividualsApi(pycsapi.ApiClient(configuration))
body = pycsapi.KYCPostIndividualSearchContract() # KYCPostIndividualSearchContract |  (optional)

try:
    # Performs An AML Search For An Individual And Saves The Results To The Database
    api_response = api_instance.compliance_kyc_protect_create_individuals_search(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningIndividualsApi->compliance_kyc_protect_create_individuals_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KYCPostIndividualSearchContract**](KYCPostIndividualSearchContract.md)|  | [optional] 

### Return type

[**KycProtectPostPostIndividualSearchResponse**](KycProtectPostPostIndividualSearchResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliance_kyc_protect_get_individuals_search**
> KycProtectIndividualSearchResponse compliance_kyc_protect_get_individuals_search(page=page, page_size=page_size, is_scheduled=is_scheduled)

Returns Individual AML Searches

Returns a list of individual AML searches ordered by modified date.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningIndividualsApi(pycsapi.ApiClient(configuration))
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 56 # int | Number of items to return per Page. (optional)
is_scheduled = true # bool |  (optional)

try:
    # Returns Individual AML Searches
    api_response = api_instance.compliance_kyc_protect_get_individuals_search(page=page, page_size=page_size, is_scheduled=is_scheduled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningIndividualsApi->compliance_kyc_protect_get_individuals_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Number of items to return per Page. | [optional] 
 **is_scheduled** | **bool**|  | [optional] 

### Return type

[**KycProtectIndividualSearchResponse**](KycProtectIndividualSearchResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliance_kyc_protect_update_individuals_search**
> PutKYCSearchIndividualResponse compliance_kyc_protect_update_individuals_search(body=body)

Update Individual AML Searches

Updates a batch of individual AML searches.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningIndividualsApi(pycsapi.ApiClient(configuration))
body = pycsapi.PutKYCIndividualSearchRequest() # PutKYCIndividualSearchRequest |  (optional)

try:
    # Update Individual AML Searches
    api_response = api_instance.compliance_kyc_protect_update_individuals_search(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningIndividualsApi->compliance_kyc_protect_update_individuals_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PutKYCIndividualSearchRequest**](PutKYCIndividualSearchRequest.md)|  | [optional] 

### Return type

[**PutKYCSearchIndividualResponse**](PutKYCSearchIndividualResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gets_an_individual_search_for_the_current_logged_in_users_customer_based_on_search_id**
> KYCGetSearchIndividualBySearchIdResponse gets_an_individual_search_for_the_current_logged_in_users_customer_based_on_search_id(search_id)

Return Individual AML Search By Search Id

Returns a single AML Search based on searchId.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningIndividualsApi(pycsapi.ApiClient(configuration))
search_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | search id to fetch

try:
    # Return Individual AML Search By Search Id
    api_response = api_instance.gets_an_individual_search_for_the_current_logged_in_users_customer_based_on_search_id(search_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningIndividualsApi->gets_an_individual_search_for_the_current_logged_in_users_customer_based_on_search_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | [**str**](.md)| search id to fetch | 

### Return type

[**KYCGetSearchIndividualBySearchIdResponse**](KYCGetSearchIndividualBySearchIdResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gets_the_individual_search_hits**
> GetIndividualSearchIdHitsResponse gets_the_individual_search_hits(search_id, hit_decisions=hit_decisions, page=page, page_size=page_size)

Returns Individual AML Search Hits

Returns the individual AML search hits from the AML search results.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningIndividualsApi(pycsapi.ApiClient(configuration))
search_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | The search identifier.
hit_decisions = 'hit_decisions_example' # str | The hit decisions. It can be the collection of undecided, trueMatch, falsePositive, discarded (optional)
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 10 # int | Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. (optional) (default to 10)

try:
    # Returns Individual AML Search Hits
    api_response = api_instance.gets_the_individual_search_hits(search_id, hit_decisions=hit_decisions, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningIndividualsApi->gets_the_individual_search_hits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | [**str**](.md)| The search identifier. | 
 **hit_decisions** | **str**| The hit decisions. It can be the collection of undecided, trueMatch, falsePositive, discarded | [optional] 
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. | [optional] [default to 10]

### Return type

[**GetIndividualSearchIdHitsResponse**](GetIndividualSearchIdHitsResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **returns_full_profile_information_of_a_individual_hit_by_hit_id**
> IndividualSearchResultHitResponse returns_full_profile_information_of_a_individual_hit_by_hit_id(search_id, hit_id)

Return Full AML Search Hit Information By SearchId And HitId

This endpoint will return the full hit information by search Id and hitId. <br> Once this information is requested the information returned is stored to the database as a snap shot of that point in time.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningIndividualsApi(pycsapi.ApiClient(configuration))
search_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of the search
hit_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of the hit

try:
    # Return Full AML Search Hit Information By SearchId And HitId
    api_response = api_instance.returns_full_profile_information_of_a_individual_hit_by_hit_id(search_id, hit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningIndividualsApi->returns_full_profile_information_of_a_individual_hit_by_hit_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | [**str**](.md)| Id of the search | 
 **hit_id** | [**str**](.md)| Id of the hit | 

### Return type

[**IndividualSearchResultHitResponse**](IndividualSearchResultHitResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_single_individual_hit**
> PutIndividualSearchIdHitsByHitIdResponse update_single_individual_hit(search_id, hit_id, body=body)

Update A Single Individual Hit

This endpoint will update a single individual AML search hit by searchId and hitId.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningIndividualsApi(pycsapi.ApiClient(configuration))
search_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of the search
hit_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of the hit
body = pycsapi.IndividualsSearchResultUpdateHits() # IndividualsSearchResultUpdateHits |  (optional)

try:
    # Update A Single Individual Hit
    api_response = api_instance.update_single_individual_hit(search_id, hit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningIndividualsApi->update_single_individual_hit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | [**str**](.md)| Id of the search | 
 **hit_id** | [**str**](.md)| Id of the hit | 
 **body** | [**IndividualsSearchResultUpdateHits**](IndividualsSearchResultUpdateHits.md)|  | [optional] 

### Return type

[**PutIndividualSearchIdHitsByHitIdResponse**](PutIndividualSearchIdHitsByHitIdResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updates_a_batch_of_individual_hits**
> PutIndividualSearchIdHitsResponse updates_a_batch_of_individual_hits(search_id, body=body)

Updates A Batch Of individual AML search Hits

Update a batch of Individual AML Search Hits.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningIndividualsApi(pycsapi.ApiClient(configuration))
search_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of the search
body = pycsapi.MODEL20274f() # MODEL20274f |  (optional)

try:
    # Updates A Batch Of individual AML search Hits
    api_response = api_instance.updates_a_batch_of_individual_hits(search_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningIndividualsApi->updates_a_batch_of_individual_hits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | [**str**](.md)| Id of the search | 
 **body** | [**MODEL20274f**](MODEL20274f.md)|  | [optional] 

### Return type

[**PutIndividualSearchIdHitsResponse**](PutIndividualSearchIdHitsResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **updates_an_individual_search**
> KYCPutSearchIndividualBySearchIdResponse updates_an_individual_search(search_id, body=body)

Updates An Individual AML Search By SearchID

Updates an Individual AML Search by Search Id.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningIndividualsApi(pycsapi.ApiClient(configuration))
search_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | search id to update
body = pycsapi.PutKYCIndividualSearchBySearchIdRequest() # PutKYCIndividualSearchBySearchIdRequest |  (optional)

try:
    # Updates An Individual AML Search By SearchID
    api_response = api_instance.updates_an_individual_search(search_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningIndividualsApi->updates_an_individual_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | [**str**](.md)| search id to update | 
 **body** | [**PutKYCIndividualSearchBySearchIdRequest**](PutKYCIndividualSearchBySearchIdRequest.md)|  | [optional] 

### Return type

[**KYCPutSearchIndividualBySearchIdResponse**](KYCPutSearchIndividualBySearchIdResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# pycsapi.GBConsumersAndAMLApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**local_solutions_gb_identitysearch_history_get**](GBConsumersAndAMLApi.md#local_solutions_gb_identitysearch_history_get) | **GET** /localSolutions/GB/identitysearch/history | Gets a list of identitysearch history items
[**local_solutions_gb_identitysearch_searchreasons_get**](GBConsumersAndAMLApi.md#local_solutions_gb_identitysearch_searchreasons_get) | **GET** /localSolutions/GB/identitysearch/searchreasons | Gets identitysearch Reasons.
[**resolves_a_picklist_against_a_given_unique_id**](GBConsumersAndAMLApi.md#resolves_a_picklist_against_a_given_unique_id) | **PUT** /localSolutions/GB/identitysearch | Resolves a picklist against a given UniqueId
[**retrieves_a_prior_identity_search_result**](GBConsumersAndAMLApi.md#retrieves_a_prior_identity_search_result) | **GET** /localSolutions/GB/identitysearch/history/{uniqueId} | Retrieves a prior identitysearch result.
[**retrieves_a_prior_identity_searchs_input**](GBConsumersAndAMLApi.md#retrieves_a_prior_identity_searchs_input) | **GET** /localSolutions/GB/identitysearch/history/{uniqueId}/input | Retrieves a prior identitysearch&#x27;s input
[**revalidate_a_given_identitysearch_with_additional_documents**](GBConsumersAndAMLApi.md#revalidate_a_given_identitysearch_with_additional_documents) | **PUT** /localSolutions/GB/identitysearch/revalidation/{uniqueId} | Revalidate a given identitysearch with additional documents
[**sets_the_reference_for_an_existing_history_item**](GBConsumersAndAMLApi.md#sets_the_reference_for_an_existing_history_item) | **PUT** /localSolutions/GB/identitysearch/history/{uniqueId}/reference | Sets the reference for an existing history item
[**submits_agb_consumer_or_aml_search**](GBConsumersAndAMLApi.md#submits_agb_consumer_or_aml_search) | **POST** /localSolutions/GB/identitysearch | Submits a GB Consumer or AML Search

# **local_solutions_gb_identitysearch_history_get**
> ConnectIdentityHistoryListResponse local_solutions_gb_identitysearch_history_get(page=page, page_size=page_size, include_customer=include_customer, products=products, date_from=date_from, date_to=date_to, keyword=keyword, result=result)

Gets a list of identitysearch history items

Retrieves a paginated history list for the specified customer/user, filtered based on the include* parameters.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GBConsumersAndAMLApi(pycsapi.ApiClient(configuration))
page = 56 # int | The 1-indexed page number to fetch (optional)
page_size = 56 # int | The page size number to fetch (optional)
include_customer = true # bool | If true, returns all results for this customer. Valid for senior users only. (optional)
products = [pycsapi.ConnectIdentityProduct()] # list[ConnectIdentityProduct] | The array of products to include  **Below is a list of Definitions for the ENUM** * 0 - Consumer * 1 - Id * 2 - AML * 3 - Bank Match * 4 - AML with Bank Match (optional)
date_from = '2013-10-20T19:20:30+01:00' # datetime | The earliest date to include (optional)
date_to = '2013-10-20T19:20:30+01:00' # datetime | The latest date to include (optional)
keyword = 'keyword_example' # str | Include this string (optional)
result = 'result_example' # str | Return only items with this result (optional)

try:
    # Gets a list of identitysearch history items
    api_response = api_instance.local_solutions_gb_identitysearch_history_get(page=page, page_size=page_size, include_customer=include_customer, products=products, date_from=date_from, date_to=date_to, keyword=keyword, result=result)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GBConsumersAndAMLApi->local_solutions_gb_identitysearch_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The 1-indexed page number to fetch | [optional] 
 **page_size** | **int**| The page size number to fetch | [optional] 
 **include_customer** | **bool**| If true, returns all results for this customer. Valid for senior users only. | [optional] 
 **products** | [**list[ConnectIdentityProduct]**](ConnectIdentityProduct.md)| The array of products to include  **Below is a list of Definitions for the ENUM** * 0 - Consumer * 1 - Id * 2 - AML * 3 - Bank Match * 4 - AML with Bank Match | [optional] 
 **date_from** | **datetime**| The earliest date to include | [optional] 
 **date_to** | **datetime**| The latest date to include | [optional] 
 **keyword** | **str**| Include this string | [optional] 
 **result** | **str**| Return only items with this result | [optional] 

### Return type

[**ConnectIdentityHistoryListResponse**](ConnectIdentityHistoryListResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **local_solutions_gb_identitysearch_searchreasons_get**
> ConnectIdentityReasonResponse local_solutions_gb_identitysearch_searchreasons_get()

Gets identitysearch Reasons.

Returns an object describing which Reasons for Search are available and which are selected by a given customer. All reasons are always listed, with selected reasons specified as true.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GBConsumersAndAMLApi(pycsapi.ApiClient(configuration))

try:
    # Gets identitysearch Reasons.
    api_response = api_instance.local_solutions_gb_identitysearch_searchreasons_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GBConsumersAndAMLApi->local_solutions_gb_identitysearch_searchreasons_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConnectIdentityReasonResponse**](ConnectIdentityReasonResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolves_a_picklist_against_a_given_unique_id**
> ConnectIdentitySearchResult resolves_a_picklist_against_a_given_unique_id(body=body, resolved=resolved)

Resolves a picklist against a given UniqueId

Resolves a picklist belonging to the specified UniqueID, which would have been generated during a prior search. Guids (and thus cached searches) expire after fifteen minutes.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GBConsumersAndAMLApi(pycsapi.ApiClient(configuration))
body = NULL # object |  (optional)
resolved = ['resolved_example'] # list[str] |  (optional)

try:
    # Resolves a picklist against a given UniqueId
    api_response = api_instance.resolves_a_picklist_against_a_given_unique_id(body=body, resolved=resolved)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GBConsumersAndAMLApi->resolves_a_picklist_against_a_given_unique_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | [optional] 
 **resolved** | [**list[str]**](str.md)|  | [optional] 

### Return type

[**ConnectIdentitySearchResult**](ConnectIdentitySearchResult.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieves_a_prior_identity_search_result**
> ConnectIdentitySearchResult retrieves_a_prior_identity_search_result(unique_id)

Retrieves a prior identitysearch result.

Retrieves a prior search result. This will include the search input and any ID/AML searches, but as we cannot hold Consumer search results these are not included. Resubmission is necessary if an updated Consumer result is needed.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GBConsumersAndAMLApi(pycsapi.ApiClient(configuration))
unique_id = 'unique_id_example' # str | 

try:
    # Retrieves a prior identitysearch result.
    api_response = api_instance.retrieves_a_prior_identity_search_result(unique_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GBConsumersAndAMLApi->retrieves_a_prior_identity_search_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_id** | **str**|  | 

### Return type

[**ConnectIdentitySearchResult**](ConnectIdentitySearchResult.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieves_a_prior_identity_searchs_input**
> ConnectIdentitySearchResult retrieves_a_prior_identity_searchs_input(unique_id)

Retrieves a prior identitysearch's input

This will return the input criteria used in a search for a specified id.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GBConsumersAndAMLApi(pycsapi.ApiClient(configuration))
unique_id = 'unique_id_example' # str | 

try:
    # Retrieves a prior identitysearch's input
    api_response = api_instance.retrieves_a_prior_identity_searchs_input(unique_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GBConsumersAndAMLApi->retrieves_a_prior_identity_searchs_input: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **unique_id** | **str**|  | 

### Return type

[**ConnectIdentitySearchResult**](ConnectIdentitySearchResult.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revalidate_a_given_identitysearch_with_additional_documents**
> ConnectIdentitySearchResult revalidate_a_given_identitysearch_with_additional_documents(body, unique_id)

Revalidate a given identitysearch with additional documents

Revalidate's a given identitysearch with additional documents.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GBConsumersAndAMLApi(pycsapi.ApiClient(configuration))
body = pycsapi.ConnectIdentityRevalidateRequest() # ConnectIdentityRevalidateRequest | 
unique_id = 'unique_id_example' # str | The ID of the record to update

try:
    # Revalidate a given identitysearch with additional documents
    api_response = api_instance.revalidate_a_given_identitysearch_with_additional_documents(body, unique_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GBConsumersAndAMLApi->revalidate_a_given_identitysearch_with_additional_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectIdentityRevalidateRequest**](ConnectIdentityRevalidateRequest.md)|  | 
 **unique_id** | **str**| The ID of the record to update | 

### Return type

[**ConnectIdentitySearchResult**](ConnectIdentitySearchResult.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sets_the_reference_for_an_existing_history_item**
> str sets_the_reference_for_an_existing_history_item(body, unique_id)

Sets the reference for an existing history item

Allows you to set a reference for an existing history item. This is useful for storing a reference to the record in your own system.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GBConsumersAndAMLApi(pycsapi.ApiClient(configuration))
body = 'body_example' # str | 
unique_id = 'unique_id_example' # str | The ID of the record to update

try:
    # Sets the reference for an existing history item
    api_response = api_instance.sets_the_reference_for_an_existing_history_item(body, unique_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GBConsumersAndAMLApi->sets_the_reference_for_an_existing_history_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)|  | 
 **unique_id** | **str**| The ID of the record to update | 

### Return type

**str**

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submits_agb_consumer_or_aml_search**
> InlineResponse2008 submits_agb_consumer_or_aml_search(body=body)

Submits a GB Consumer or AML Search

Submits a GB Consumer or AML depending on the Product provided. Validates criteria for each individual search before submitting, and may return a list of error strings instead.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GBConsumersAndAMLApi(pycsapi.ApiClient(configuration))
body = NULL # object | Select the relevant tab for the request body for one of the products `AML`, `AMLMultiBureau` or `Consumer`. <br> <br> NOTE:' If a previous address is used in addition to current the `postCode` becomes required. (optional)

try:
    # Submits a GB Consumer or AML Search
    api_response = api_instance.submits_agb_consumer_or_aml_search(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GBConsumersAndAMLApi->submits_agb_consumer_or_aml_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)| Select the relevant tab for the request body for one of the products &#x60;AML&#x60;, &#x60;AMLMultiBureau&#x60; or &#x60;Consumer&#x60;. &lt;br&gt; &lt;br&gt; NOTE:&#x27; If a previous address is used in addition to current the &#x60;postCode&#x60; becomes required. | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


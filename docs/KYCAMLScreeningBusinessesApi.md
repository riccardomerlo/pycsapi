# pycsapi.KYCAMLScreeningBusinessesApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_kyc_search_business_by_search_id**](KYCAMLScreeningBusinessesApi.md#get_kyc_search_business_by_search_id) | **GET** /compliance/kyc-protect/searches/businesses/{searchId} | Return Business AML Search By Search Id
[**get_kyc_search_business_hits_by_search_id**](KYCAMLScreeningBusinessesApi.md#get_kyc_search_business_hits_by_search_id) | **GET** /compliance/kyc-protect/searches/businesses/{searchId}/hits | Return Business AML Search Hits
[**get_kyc_search_business_hits_by_search_id_and_hit_id**](KYCAMLScreeningBusinessesApi.md#get_kyc_search_business_hits_by_search_id_and_hit_id) | **GET** /compliance/kyc-protect/searches/businesses/{searchId}/hits/{hitId} | Return Full AML Search Hit Information By SearchId And HitId
[**k_yc_search_business**](KYCAMLScreeningBusinessesApi.md#k_yc_search_business) | **POST** /compliance/kyc-protect/searches/businesses | Performs An AML Search For A Business And Saves The Results To The Database
[**k_yc_search_business_get**](KYCAMLScreeningBusinessesApi.md#k_yc_search_business_get) | **GET** /compliance/kyc-protect/searches/businesses | Returns Business AML Searches
[**k_yc_search_business_put**](KYCAMLScreeningBusinessesApi.md#k_yc_search_business_put) | **PUT** /compliance/kyc-protect/searches/businesses | Update Business AML Searches
[**put_kyc_search_business_by_search_id**](KYCAMLScreeningBusinessesApi.md#put_kyc_search_business_by_search_id) | **PUT** /compliance/kyc-protect/searches/businesses/{searchId} | Update A Business AML Search By Search Id
[**put_kyc_search_business_by_search_id_and_hit_id**](KYCAMLScreeningBusinessesApi.md#put_kyc_search_business_by_search_id_and_hit_id) | **PUT** /compliance/kyc-protect/searches/businesses/{searchId}/hits/{hitId} | Update A Single Business Hit
[**put_kyc_search_business_hits_by_search_id**](KYCAMLScreeningBusinessesApi.md#put_kyc_search_business_hits_by_search_id) | **PUT** /compliance/kyc-protect/searches/businesses/{searchId}/hits | Update Batch Of Business AML Search Hits

# **get_kyc_search_business_by_search_id**
> KYCGetSearchBusinessesBySearchIdResponse get_kyc_search_business_by_search_id(search_id)

Return Business AML Search By Search Id

Returns a single AML search based on Search id.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningBusinessesApi(pycsapi.ApiClient(configuration))
search_id = 'search_id_example' # str | 

try:
    # Return Business AML Search By Search Id
    api_response = api_instance.get_kyc_search_business_by_search_id(search_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningBusinessesApi->get_kyc_search_business_by_search_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | **str**|  | 

### Return type

[**KYCGetSearchBusinessesBySearchIdResponse**](KYCGetSearchBusinessesBySearchIdResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kyc_search_business_hits_by_search_id**
> KYCGetSearchBusinessesBySearchIdHitsResponse get_kyc_search_business_hits_by_search_id(search_id, page=page, page_size=page_size, hit_decisions=hit_decisions)

Return Business AML Search Hits

Returns the business AML search hits from the AML search results.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningBusinessesApi(pycsapi.ApiClient(configuration))
search_id = 'search_id_example' # str | 
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 10 # int | Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. (optional) (default to 10)
hit_decisions = 'hit_decisions_example' # str | The hit decisions. <br> Available Values - [undecided, truematch, falsepositive, discarded] (optional)

try:
    # Return Business AML Search Hits
    api_response = api_instance.get_kyc_search_business_hits_by_search_id(search_id, page=page, page_size=page_size, hit_decisions=hit_decisions)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningBusinessesApi->get_kyc_search_business_hits_by_search_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | **str**|  | 
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. | [optional] [default to 10]
 **hit_decisions** | **str**| The hit decisions. &lt;br&gt; Available Values - [undecided, truematch, falsepositive, discarded] | [optional] 

### Return type

[**KYCGetSearchBusinessesBySearchIdHitsResponse**](KYCGetSearchBusinessesBySearchIdHitsResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kyc_search_business_hits_by_search_id_and_hit_id**
> WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse get_kyc_search_business_hits_by_search_id_and_hit_id(search_id, hit_id)

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
api_instance = pycsapi.KYCAMLScreeningBusinessesApi(pycsapi.ApiClient(configuration))
search_id = 'search_id_example' # str | Id of the search
hit_id = 'hit_id_example' # str | Id of the hit

try:
    # Return Full AML Search Hit Information By SearchId And HitId
    api_response = api_instance.get_kyc_search_business_hits_by_search_id_and_hit_id(search_id, hit_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningBusinessesApi->get_kyc_search_business_hits_by_search_id_and_hit_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | **str**| Id of the search | 
 **hit_id** | **str**| Id of the hit | 

### Return type

[**WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse**](WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_yc_search_business**
> MODEL931a1b k_yc_search_business(body)

Performs An AML Search For A Business And Saves The Results To The Database

A request requires a name, at least one valid dataset, and a threshold. User will be deducted 1 credit for each AML search.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningBusinessesApi(pycsapi.ApiClient(configuration))
body = pycsapi.SearchesBusinessesBody1() # SearchesBusinessesBody1 | 

try:
    # Performs An AML Search For A Business And Saves The Results To The Database
    api_response = api_instance.k_yc_search_business(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningBusinessesApi->k_yc_search_business: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchesBusinessesBody1**](SearchesBusinessesBody1.md)|  | 

### Return type

[**MODEL931a1b**](MODEL931a1b.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_yc_search_business_get**
> MODELf73bb1 k_yc_search_business_get(page=page, page_size=page_size, is_scheduled=is_scheduled)

Returns Business AML Searches

Returns a list of business AML searches ordered by modified date.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningBusinessesApi(pycsapi.ApiClient(configuration))
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 10 # int | Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. (optional) (default to 10)
is_scheduled = true # bool |  (optional)

try:
    # Returns Business AML Searches
    api_response = api_instance.k_yc_search_business_get(page=page, page_size=page_size, is_scheduled=is_scheduled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningBusinessesApi->k_yc_search_business_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. | [optional] [default to 10]
 **is_scheduled** | **bool**|  | [optional] 

### Return type

[**MODELf73bb1**](MODELf73bb1.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_yc_search_business_put**
> KYCPUTSearchBusinessesResponse k_yc_search_business_put(body=body)

Update Business AML Searches

Updates a batch of business AML searches.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningBusinessesApi(pycsapi.ApiClient(configuration))
body = pycsapi.SearchesBusinessesBody() # SearchesBusinessesBody |  (optional)

try:
    # Update Business AML Searches
    api_response = api_instance.k_yc_search_business_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningBusinessesApi->k_yc_search_business_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchesBusinessesBody**](SearchesBusinessesBody.md)|  | [optional] 

### Return type

[**KYCPUTSearchBusinessesResponse**](KYCPUTSearchBusinessesResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_kyc_search_business_by_search_id**
> KYCPutSearchBusinessesBySearchIdResponse put_kyc_search_business_by_search_id(search_id, body=body)

Update A Business AML Search By Search Id

Updates a business AML search.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningBusinessesApi(pycsapi.ApiClient(configuration))
search_id = 'search_id_example' # str | 
body = pycsapi.BusinessesSearchIdBody() # BusinessesSearchIdBody |  (optional)

try:
    # Update A Business AML Search By Search Id
    api_response = api_instance.put_kyc_search_business_by_search_id(search_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningBusinessesApi->put_kyc_search_business_by_search_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | **str**|  | 
 **body** | [**BusinessesSearchIdBody**](BusinessesSearchIdBody.md)|  | [optional] 

### Return type

[**KYCPutSearchBusinessesBySearchIdResponse**](KYCPutSearchBusinessesBySearchIdResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_kyc_search_business_by_search_id_and_hit_id**
> KYCBusinessSearchResultHitSummaryResponse put_kyc_search_business_by_search_id_and_hit_id(search_id, hit_id, body=body)

Update A Single Business Hit

This endpoint will update a single business AML search hit by searchId and hitId.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningBusinessesApi(pycsapi.ApiClient(configuration))
search_id = 'search_id_example' # str | 
hit_id = 'hit_id_example' # str | 
body = pycsapi.HitsHitIdBody() # HitsHitIdBody |  (optional)

try:
    # Update A Single Business Hit
    api_response = api_instance.put_kyc_search_business_by_search_id_and_hit_id(search_id, hit_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningBusinessesApi->put_kyc_search_business_by_search_id_and_hit_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | **str**|  | 
 **hit_id** | **str**|  | 
 **body** | [**HitsHitIdBody**](HitsHitIdBody.md)|  | [optional] 

### Return type

[**KYCBusinessSearchResultHitSummaryResponse**](KYCBusinessSearchResultHitSummaryResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_kyc_search_business_hits_by_search_id**
> KYCPutSearchBusinessesBySearchIdHitsResponse put_kyc_search_business_hits_by_search_id(search_id, body=body)

Update Batch Of Business AML Search Hits

Updates a batch of business AML search hits.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAMLScreeningBusinessesApi(pycsapi.ApiClient(configuration))
search_id = 'search_id_example' # str | 
body = pycsapi.MODEL7b2457() # MODEL7b2457 |  (optional)

try:
    # Update Batch Of Business AML Search Hits
    api_response = api_instance.put_kyc_search_business_hits_by_search_id(search_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAMLScreeningBusinessesApi->put_kyc_search_business_hits_by_search_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_id** | **str**|  | 
 **body** | [**MODEL7b2457**](MODEL7b2457.md)|  | [optional] 

### Return type

[**KYCPutSearchBusinessesBySearchIdHitsResponse**](KYCPutSearchBusinessesBySearchIdHitsResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# pycsapi.KYCProfileKeyPartiesApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compliancedeletekyckeypartiesbyprofileid**](KYCProfileKeyPartiesApi.md#compliancedeletekyckeypartiesbyprofileid) | **DELETE** /compliance/kyc-protect/profiles/{profileId}/keyparties | Delete a batch of key parties
[**compliancedeletekyckeypartiessearches**](KYCProfileKeyPartiesApi.md#compliancedeletekyckeypartiessearches) | **DELETE** /compliance/kyc-protect/profiles/{profileId}/keyparties/searches | Deletes A Batch Of Key Party Searches
[**compliancegetkyckeypartiesbyprofileid**](KYCProfileKeyPartiesApi.md#compliancegetkyckeypartiesbyprofileid) | **GET** /compliance/kyc-protect/profiles/{profileId}/keyparties | Return All Key Party Records Linked To A Profile
[**compliancegetkyckeypartiessearches**](KYCProfileKeyPartiesApi.md#compliancegetkyckeypartiessearches) | **GET** /compliance/kyc-protect/profiles/{profileId}/keyparties/searches | Return All Key Party Searches
[**compliancepostkyckeypartiesbyprofileid**](KYCProfileKeyPartiesApi.md#compliancepostkyckeypartiesbyprofileid) | **POST** /compliance/kyc-protect/profiles/{profileId}/keyparties | Creates A Key Party Folder Linked To The Profile Id
[**compliancepostkyckeypartiessearchesbulkbyprofileid**](KYCProfileKeyPartiesApi.md#compliancepostkyckeypartiessearchesbulkbyprofileid) | **POST** /compliance/kyc-protect/profiles/{profileId}/keyparties/searches/bulk | Request Multiple Searches Linked To A Key Party Asynchronously
[**compliancepostkyckeypartiessearcheslinkbyprofileid**](KYCProfileKeyPartiesApi.md#compliancepostkyckeypartiessearcheslinkbyprofileid) | **POST** /compliance/kyc-protect/profiles/{profileId}/keyparties/searches/link | Links Searches To Key Parties
[**complianceprotectdeletekycprofileskeypartiesbyprofileidandkeypartyid**](KYCProfileKeyPartiesApi.md#complianceprotectdeletekycprofileskeypartiesbyprofileidandkeypartyid) | **DELETE** /compliance/kyc-protect/profiles/{profileId}/keyparties/{keyPartyId} | Deletes a Key PArty By Key Party Id
[**complianceprotectputkycprofileskeypartiesbyprofileidandkeypartyid**](KYCProfileKeyPartiesApi.md#complianceprotectputkycprofileskeypartiesbyprofileidandkeypartyid) | **PUT** /compliance/kyc-protect/profiles/{profileId}/keyparties/{keyPartyId} | Updates The Key Party By Profile Id and Key Party Id
[**complianceputkyckeypartiesbyprofileid**](KYCProfileKeyPartiesApi.md#complianceputkyckeypartiesbyprofileid) | **PUT** /compliance/kyc-protect/profiles/{profileId}/keyparties | Update A Batch Of Key Parties

# **compliancedeletekyckeypartiesbyprofileid**
> DeleteKeyPartiesResponseByProfileId compliancedeletekyckeypartiesbyprofileid(profile_id, body=body)

Delete a batch of key parties

Delete a selection of key parties from a specific profile.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileKeyPartiesApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of the profile
body = pycsapi.ProfileIdKeypartiesBody() # ProfileIdKeypartiesBody |  (optional)

try:
    # Delete a batch of key parties
    api_response = api_instance.compliancedeletekyckeypartiesbyprofileid(profile_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileKeyPartiesApi->compliancedeletekyckeypartiesbyprofileid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| Id of the profile | 
 **body** | [**ProfileIdKeypartiesBody**](ProfileIdKeypartiesBody.md)|  | [optional] 

### Return type

[**DeleteKeyPartiesResponseByProfileId**](DeleteKeyPartiesResponseByProfileId.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliancedeletekyckeypartiessearches**
> DeleteKeyPartySearchContractResponse compliancedeletekyckeypartiessearches(profile_id, body=body)

Deletes A Batch Of Key Party Searches

Delete a batch of key parties searches

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileKeyPartiesApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile
body = pycsapi.DeleteKeyPartySearchContractRequest() # DeleteKeyPartySearchContractRequest |  (optional)

try:
    # Deletes A Batch Of Key Party Searches
    api_response = api_instance.compliancedeletekyckeypartiessearches(profile_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileKeyPartiesApi->compliancedeletekyckeypartiessearches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| id of the profile | 
 **body** | [**DeleteKeyPartySearchContractRequest**](DeleteKeyPartySearchContractRequest.md)|  | [optional] 

### Return type

[**DeleteKeyPartySearchContractResponse**](DeleteKeyPartySearchContractResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliancegetkyckeypartiesbyprofileid**
> GetKeyPartiesResponseByProfileId compliancegetkyckeypartiesbyprofileid(profile_id, entity_type=entity_type, key_party_types=key_party_types, page=page, page_size=page_size)

Return All Key Party Records Linked To A Profile

This endpoint will return all created Key Party folders linked to the profile id.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileKeyPartiesApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of the profile
entity_type = 'entity_type_example' # str | Entity type of the key party. Available values are individual, business. (optional)
key_party_types = 'key_party_types_example' # str | Type of the key party. Available values are director, shareholder and ubo. (optional)
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 10 # int | Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. (optional) (default to 10)

try:
    # Return All Key Party Records Linked To A Profile
    api_response = api_instance.compliancegetkyckeypartiesbyprofileid(profile_id, entity_type=entity_type, key_party_types=key_party_types, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileKeyPartiesApi->compliancegetkyckeypartiesbyprofileid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| Id of the profile | 
 **entity_type** | **str**| Entity type of the key party. Available values are individual, business. | [optional] 
 **key_party_types** | **str**| Type of the key party. Available values are director, shareholder and ubo. | [optional] 
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. | [optional] [default to 10]

### Return type

[**GetKeyPartiesResponseByProfileId**](GetKeyPartiesResponseByProfileId.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliancegetkyckeypartiessearches**
> GetKeyPartySearchResponse compliancegetkyckeypartiessearches(profile_id, page=page, page_size=page_size, type=type, key_party_types=key_party_types, is_scheduled=is_scheduled)

Return All Key Party Searches

Get profile key party searches for the user.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileKeyPartiesApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 10 # int | Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. (optional) (default to 10)
type = 'type_example' # str | type of searches. Available values: individual, business (optional)
key_party_types = 'key_party_types_example' # str | keyparty types. Available values: director, shareHolder, ubo (optional)
is_scheduled = true # bool | schedule check. (optional)

try:
    # Return All Key Party Searches
    api_response = api_instance.compliancegetkyckeypartiessearches(profile_id, page=page, page_size=page_size, type=type, key_party_types=key_party_types, is_scheduled=is_scheduled)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileKeyPartiesApi->compliancegetkyckeypartiessearches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| id of the profile | 
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. | [optional] [default to 10]
 **type** | **str**| type of searches. Available values: individual, business | [optional] 
 **key_party_types** | **str**| keyparty types. Available values: director, shareHolder, ubo | [optional] 
 **is_scheduled** | **bool**| schedule check. | [optional] 

### Return type

[**GetKeyPartySearchResponse**](GetKeyPartySearchResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliancepostkyckeypartiesbyprofileid**
> InlineResponse201 compliancepostkyckeypartiesbyprofileid(profile_id, body=body)

Creates A Key Party Folder Linked To The Profile Id

Uses the details provided by the user to create key parties. Returns the created key parties information.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileKeyPartiesApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile
body = pycsapi.PostKYCKeypartiesByProfileIdRequest() # PostKYCKeypartiesByProfileIdRequest |  (optional)

try:
    # Creates A Key Party Folder Linked To The Profile Id
    api_response = api_instance.compliancepostkyckeypartiesbyprofileid(profile_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileKeyPartiesApi->compliancepostkyckeypartiesbyprofileid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| id of the profile | 
 **body** | [**PostKYCKeypartiesByProfileIdRequest**](PostKYCKeypartiesByProfileIdRequest.md)|  | [optional] 

### Return type

[**InlineResponse201**](InlineResponse201.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliancepostkyckeypartiessearchesbulkbyprofileid**
> compliancepostkyckeypartiessearchesbulkbyprofileid(profile_id, body=body)

Request Multiple Searches Linked To A Key Party Asynchronously

Request multiple searches to be performed and linked to a key party asynchronously

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileKeyPartiesApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile
body = pycsapi.SearchesBulkBody() # SearchesBulkBody |  (optional)

try:
    # Request Multiple Searches Linked To A Key Party Asynchronously
    api_instance.compliancepostkyckeypartiessearchesbulkbyprofileid(profile_id, body=body)
except ApiException as e:
    print("Exception when calling KYCProfileKeyPartiesApi->compliancepostkyckeypartiessearchesbulkbyprofileid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| id of the profile | 
 **body** | [**SearchesBulkBody**](SearchesBulkBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliancepostkyckeypartiessearcheslinkbyprofileid**
> PostKYCKeypartiesSearchesLinkByProfileIdResponse compliancepostkyckeypartiessearcheslinkbyprofileid(profile_id, body=body)

Links Searches To Key Parties

Add searches link to key parties for the current logged in user.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileKeyPartiesApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile
body = pycsapi.SearchesLinkBody() # SearchesLinkBody |  (optional)

try:
    # Links Searches To Key Parties
    api_response = api_instance.compliancepostkyckeypartiessearcheslinkbyprofileid(profile_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileKeyPartiesApi->compliancepostkyckeypartiessearcheslinkbyprofileid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| id of the profile | 
 **body** | [**SearchesLinkBody**](SearchesLinkBody.md)|  | [optional] 

### Return type

[**PostKYCKeypartiesSearchesLinkByProfileIdResponse**](PostKYCKeypartiesSearchesLinkByProfileIdResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complianceprotectdeletekycprofileskeypartiesbyprofileidandkeypartyid**
> DeleteKeyPartyByIdNoContent complianceprotectdeletekycprofileskeypartiesbyprofileidandkeypartyid(profile_id, key_party_id)

Deletes a Key PArty By Key Party Id

Delete a key party by Id.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileKeyPartiesApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile
key_party_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the keyParty

try:
    # Deletes a Key PArty By Key Party Id
    api_response = api_instance.complianceprotectdeletekycprofileskeypartiesbyprofileidandkeypartyid(profile_id, key_party_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileKeyPartiesApi->complianceprotectdeletekycprofileskeypartiesbyprofileidandkeypartyid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| id of the profile | 
 **key_party_id** | [**str**](.md)| id of the keyParty | 

### Return type

[**DeleteKeyPartyByIdNoContent**](DeleteKeyPartyByIdNoContent.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complianceprotectputkycprofileskeypartiesbyprofileidandkeypartyid**
> KeyPartyByIdReturn complianceprotectputkycprofileskeypartiesbyprofileidandkeypartyid(profile_id, key_party_id, body=body)

Updates The Key Party By Profile Id and Key Party Id

Updates a key party on a profile by Id. Returns the updated key party data.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileKeyPartiesApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile
key_party_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the keyParty
body = pycsapi.UpdateKeyPartyById() # UpdateKeyPartyById | Modified key party (optional)

try:
    # Updates The Key Party By Profile Id and Key Party Id
    api_response = api_instance.complianceprotectputkycprofileskeypartiesbyprofileidandkeypartyid(profile_id, key_party_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileKeyPartiesApi->complianceprotectputkycprofileskeypartiesbyprofileidandkeypartyid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| id of the profile | 
 **key_party_id** | [**str**](.md)| id of the keyParty | 
 **body** | [**UpdateKeyPartyById**](UpdateKeyPartyById.md)| Modified key party | [optional] 

### Return type

[**KeyPartyByIdReturn**](KeyPartyByIdReturn.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complianceputkyckeypartiesbyprofileid**
> InlineResponse20010 complianceputkyckeypartiesbyprofileid(profile_id, body=body)

Update A Batch Of Key Parties

Updates a batch of key parties

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileKeyPartiesApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile
body = pycsapi.PutKYCKeypartiesByProfileIdRequest() # PutKYCKeypartiesByProfileIdRequest |  (optional)

try:
    # Update A Batch Of Key Parties
    api_response = api_instance.complianceputkyckeypartiesbyprofileid(profile_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileKeyPartiesApi->complianceputkyckeypartiesbyprofileid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| id of the profile | 
 **body** | [**PutKYCKeypartiesByProfileIdRequest**](PutKYCKeypartiesByProfileIdRequest.md)|  | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


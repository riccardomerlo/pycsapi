# pycsapi.KYCAdministratorResourcesApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**k_yc_protect_get_profile_document_types**](KYCAdministratorResourcesApi.md#k_yc_protect_get_profile_document_types) | **GET** /compliance/kyc-protect/profiles/document-types | Return Profile Document Types
[**protect_get_kyc_profile_types**](KYCAdministratorResourcesApi.md#protect_get_kyc_profile_types) | **GET** /compliance/kyc-protect/profiles/types | Return Profile Types
[**protect_get_lookup_country_codes**](KYCAdministratorResourcesApi.md#protect_get_lookup_country_codes) | **GET** /compliance/kyc-protect/lookup/countryCodes | Return Accepted Country Codes
[**protect_get_lookup_currency_codes**](KYCAdministratorResourcesApi.md#protect_get_lookup_currency_codes) | **GET** /compliance/kyc-protect/lookup/currencyCodes | Returns Accepted Currency Codes

# **k_yc_protect_get_profile_document_types**
> list[str] k_yc_protect_get_profile_document_types(type)

Return Profile Document Types

Returns a list of document types valid for the provided profile type.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAdministratorResourcesApi(pycsapi.ApiClient(configuration))
type = 'type_example' # str | The type of the profile the user wants to return.

try:
    # Return Profile Document Types
    api_response = api_instance.k_yc_protect_get_profile_document_types(type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAdministratorResourcesApi->k_yc_protect_get_profile_document_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of the profile the user wants to return. | 

### Return type

**list[str]**

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_get_kyc_profile_types**
> GetKYCProfileTypes protect_get_kyc_profile_types()

Return Profile Types

Returns all the profile Types

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAdministratorResourcesApi(pycsapi.ApiClient(configuration))

try:
    # Return Profile Types
    api_response = api_instance.protect_get_kyc_profile_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAdministratorResourcesApi->protect_get_kyc_profile_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetKYCProfileTypes**](GetKYCProfileTypes.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_get_lookup_country_codes**
> list[str] protect_get_lookup_country_codes()

Return Accepted Country Codes

Returns the list of accepted country-codes.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAdministratorResourcesApi(pycsapi.ApiClient(configuration))

try:
    # Return Accepted Country Codes
    api_response = api_instance.protect_get_lookup_country_codes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAdministratorResourcesApi->protect_get_lookup_country_codes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_get_lookup_currency_codes**
> list[str] protect_get_lookup_currency_codes()

Returns Accepted Currency Codes

Returns the list of accepted currency codes.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCAdministratorResourcesApi(pycsapi.ApiClient(configuration))

try:
    # Returns Accepted Currency Codes
    api_response = api_instance.protect_get_lookup_currency_codes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCAdministratorResourcesApi->protect_get_lookup_currency_codes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


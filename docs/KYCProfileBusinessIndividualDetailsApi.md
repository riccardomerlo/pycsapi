# pycsapi.KYCProfileBusinessIndividualDetailsApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**k_yc_protect_creates_an_address_for_the_user**](KYCProfileBusinessIndividualDetailsApi.md#k_yc_protect_creates_an_address_for_the_user) | **POST** /compliance/kyc-protect/profiles/{profileId}/details/addresses | Creates An Address For Profile
[**k_yc_protect_gets_list_of_addresses**](KYCProfileBusinessIndividualDetailsApi.md#k_yc_protect_gets_list_of_addresses) | **GET** /compliance/kyc-protect/profiles/{profileId}/details/addresses | Return Lists Of Addresses
[**protect_deletekyc_profile_address_details_by_profile_id_and_address_id**](KYCProfileBusinessIndividualDetailsApi.md#protect_deletekyc_profile_address_details_by_profile_id_and_address_id) | **DELETE** /compliance/kyc-protect/profiles/{profileId}/details/addresses/{addressId} | Delete Profile Address Details By Profile Id And Address Id
[**protect_getkyc_profile_address_details_by_profile_id_and_address_id**](KYCProfileBusinessIndividualDetailsApi.md#protect_getkyc_profile_address_details_by_profile_id_and_address_id) | **GET** /compliance/kyc-protect/profiles/{profileId}/details/addresses/{addressId} | Return Profile Address Details By Profile And Address Id
[**protect_getkyc_profile_details**](KYCProfileBusinessIndividualDetailsApi.md#protect_getkyc_profile_details) | **GET** /compliance/kyc-protect/profiles/{profileId}/details | Return Profile Details
[**protect_putkyc_profile_address_details_by_profile_id_and_address_id**](KYCProfileBusinessIndividualDetailsApi.md#protect_putkyc_profile_address_details_by_profile_id_and_address_id) | **PUT** /compliance/kyc-protect/profiles/{profileId}/details/addresses/{addressId} | Update Profile Address Details By Profile Id And Address Id
[**protect_putkyc_profile_details**](KYCProfileBusinessIndividualDetailsApi.md#protect_putkyc_profile_details) | **PUT** /compliance/kyc-protect/profiles/{profileId}/details | Update Profile Details

# **k_yc_protect_creates_an_address_for_the_user**
> KycProtectProfileAddressResponse k_yc_protect_creates_an_address_for_the_user(profile_id, body=body)

Creates An Address For Profile

Creates an address for the given profileId. Returns the created address information.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileBusinessIndividualDetailsApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile
body = pycsapi.DetailsAddressesBody() # DetailsAddressesBody |  (optional)

try:
    # Creates An Address For Profile
    api_response = api_instance.k_yc_protect_creates_an_address_for_the_user(profile_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileBusinessIndividualDetailsApi->k_yc_protect_creates_an_address_for_the_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| id of the profile | 
 **body** | [**DetailsAddressesBody**](DetailsAddressesBody.md)|  | [optional] 

### Return type

[**KycProtectProfileAddressResponse**](KycProtectProfileAddressResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **k_yc_protect_gets_list_of_addresses**
> list[KycProtectProfileGetDetailsAddressResponse] k_yc_protect_gets_list_of_addresses(profile_id)

Return Lists Of Addresses

Returns list of addresses for the current logged in user based on profileId.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileBusinessIndividualDetailsApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile

try:
    # Return Lists Of Addresses
    api_response = api_instance.k_yc_protect_gets_list_of_addresses(profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileBusinessIndividualDetailsApi->k_yc_protect_gets_list_of_addresses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| id of the profile | 

### Return type

[**list[KycProtectProfileGetDetailsAddressResponse]**](KycProtectProfileGetDetailsAddressResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_deletekyc_profile_address_details_by_profile_id_and_address_id**
> protect_deletekyc_profile_address_details_by_profile_id_and_address_id(profile_id, address_id)

Delete Profile Address Details By Profile Id And Address Id

Deletes the address by profile Id and address id.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileBusinessIndividualDetailsApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of a profile.
address_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of a addressId.

try:
    # Delete Profile Address Details By Profile Id And Address Id
    api_instance.protect_deletekyc_profile_address_details_by_profile_id_and_address_id(profile_id, address_id)
except ApiException as e:
    print("Exception when calling KYCProfileBusinessIndividualDetailsApi->protect_deletekyc_profile_address_details_by_profile_id_and_address_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| Id of a profile. | 
 **address_id** | [**str**](.md)| Id of a addressId. | 

### Return type

void (empty response body)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_getkyc_profile_address_details_by_profile_id_and_address_id**
> GetKYCAddressDetailsByTheGivenAddressIdForTheSuppliedProfileIdUser protect_getkyc_profile_address_details_by_profile_id_and_address_id(profile_id, address_id)

Return Profile Address Details By Profile And Address Id

Returns the address by profile Id and address Id.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileBusinessIndividualDetailsApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of a profile.
address_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of a user address.

try:
    # Return Profile Address Details By Profile And Address Id
    api_response = api_instance.protect_getkyc_profile_address_details_by_profile_id_and_address_id(profile_id, address_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileBusinessIndividualDetailsApi->protect_getkyc_profile_address_details_by_profile_id_and_address_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| Id of a profile. | 
 **address_id** | [**str**](.md)| Id of a user address. | 

### Return type

[**GetKYCAddressDetailsByTheGivenAddressIdForTheSuppliedProfileIdUser**](GetKYCAddressDetailsByTheGivenAddressIdForTheSuppliedProfileIdUser.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_getkyc_profile_details**
> GetKYCProfileDetailsByProfileId protect_getkyc_profile_details(profile_id)

Return Profile Details

Fetches details of a profile by profile Id.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileBusinessIndividualDetailsApi(pycsapi.ApiClient(configuration))
profile_id = 'profile_id_example' # str | Id of a profile.

try:
    # Return Profile Details
    api_response = api_instance.protect_getkyc_profile_details(profile_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileBusinessIndividualDetailsApi->protect_getkyc_profile_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Id of a profile. | 

### Return type

[**GetKYCProfileDetailsByProfileId**](GetKYCProfileDetailsByProfileId.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_putkyc_profile_address_details_by_profile_id_and_address_id**
> PutKYCAddressDetailsByTheGivenAddressIdForTheSuppliedProfileIdUser protect_putkyc_profile_address_details_by_profile_id_and_address_id(profile_id, address_id, body=body)

Update Profile Address Details By Profile Id And Address Id

Update Profile Address Details By Profile Id And Address Id

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileBusinessIndividualDetailsApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of a profile.
address_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | Id of a user address.
body = pycsapi.UpdateKYCAddressDetailsByTheGivenAddressIdForTheSuppliedProfileIdUserRequest() # UpdateKYCAddressDetailsByTheGivenAddressIdForTheSuppliedProfileIdUserRequest |  (optional)

try:
    # Update Profile Address Details By Profile Id And Address Id
    api_response = api_instance.protect_putkyc_profile_address_details_by_profile_id_and_address_id(profile_id, address_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileBusinessIndividualDetailsApi->protect_putkyc_profile_address_details_by_profile_id_and_address_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| Id of a profile. | 
 **address_id** | [**str**](.md)| Id of a user address. | 
 **body** | [**UpdateKYCAddressDetailsByTheGivenAddressIdForTheSuppliedProfileIdUserRequest**](UpdateKYCAddressDetailsByTheGivenAddressIdForTheSuppliedProfileIdUserRequest.md)|  | [optional] 

### Return type

[**PutKYCAddressDetailsByTheGivenAddressIdForTheSuppliedProfileIdUser**](PutKYCAddressDetailsByTheGivenAddressIdForTheSuppliedProfileIdUser.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_putkyc_profile_details**
> PutKYCProfileDetailsByProfileId protect_putkyc_profile_details(profile_id, body=body)

Update Profile Details

Updates the details of profile by the profileId.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCProfileBusinessIndividualDetailsApi(pycsapi.ApiClient(configuration))
profile_id = 'profile_id_example' # str | Id of a profile.
body = pycsapi.PutKYCProfileDetailsByProfileIdRequest() # PutKYCProfileDetailsByProfileIdRequest |  (optional)

try:
    # Update Profile Details
    api_response = api_instance.protect_putkyc_profile_details(profile_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCProfileBusinessIndividualDetailsApi->protect_putkyc_profile_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| Id of a profile. | 
 **body** | [**PutKYCProfileDetailsByProfileIdRequest**](PutKYCProfileDetailsByProfileIdRequest.md)|  | [optional] 

### Return type

[**PutKYCProfileDetailsByProfileId**](PutKYCProfileDetailsByProfileId.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# pycsapi.UserAdministrationApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**protect_get_active_customer_users**](UserAdministrationApi.md#protect_get_active_customer_users) | **GET** /access/users/active | List of Active Users
[**protect_get_details_of_logged_in_user**](UserAdministrationApi.md#protect_get_details_of_logged_in_user) | **GET** /access/users/me | Logged In User Details
[**subscription_details**](UserAdministrationApi.md#subscription_details) | **GET** /access | Subscription Details

# **protect_get_active_customer_users**
> KycProtectGetCustomerUsersDetailsResponse protect_get_active_customer_users()

List of Active Users

Returns a collection of user details with in the customer

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.UserAdministrationApi(pycsapi.ApiClient(configuration))

try:
    # List of Active Users
    api_response = api_instance.protect_get_active_customer_users()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAdministrationApi->protect_get_active_customer_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**KycProtectGetCustomerUsersDetailsResponse**](KycProtectGetCustomerUsersDetailsResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **protect_get_details_of_logged_in_user**
> KycProtectGetMyUserDetailsResponse protect_get_details_of_logged_in_user()

Logged In User Details

Returns the details of logged in user.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.UserAdministrationApi(pycsapi.ApiClient(configuration))

try:
    # Logged In User Details
    api_response = api_instance.protect_get_details_of_logged_in_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAdministrationApi->protect_get_details_of_logged_in_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**KycProtectGetMyUserDetailsResponse**](KycProtectGetMyUserDetailsResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscription_details**
> ConnectAuthenticationAccessCountries subscription_details()

Subscription Details

Returns the available countries in your subscription - Company Report, Director Report, Offline Reports and Monitoring.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.UserAdministrationApi(pycsapi.ApiClient(configuration))

try:
    # Subscription Details
    api_response = api_instance.subscription_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAdministrationApi->subscription_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConnectAuthenticationAccessCountries**](ConnectAuthenticationAccessCountries.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


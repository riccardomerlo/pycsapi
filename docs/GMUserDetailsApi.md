# pycsapi.GMUserDetailsApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**monitoring_user_details**](GMUserDetailsApi.md#monitoring_user_details) | **GET** /monitoring/user/details | Monitoring User Details

# **monitoring_user_details**
> ConnectMonitoringUserDetails monitoring_user_details()

Monitoring User Details

You would use this endpoint to retrieve the user details related to the Global Monitoring product, such as the user's information.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMUserDetailsApi(pycsapi.ApiClient(configuration))

try:
    # Monitoring User Details
    api_response = api_instance.monitoring_user_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMUserDetailsApi->monitoring_user_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConnectMonitoringUserDetails**](ConnectMonitoringUserDetails.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# pycsapi.AuthenticationApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate**](AuthenticationApi.md#authenticate) | **POST** /authenticate | Authenticate

# **authenticate**
> ConnectAuthenticationAuthResponse authenticate(body=body)

Authenticate

Supply username and password to generate Authentication Token. <br><br><h3>Rate Limiting Authenticate</h3>   Rate limiting is implemented on the authenticate endpoint to ensure fair usage and protect the service from excessive requests. Please take note of the following rate limiting rules:<br><br>   <ol><li>**Invalid Request Limit**:<br>   Up to 5 identical invalid requests are permitted within a 2-minute period. Upon reaching this limit:</li><br>   <ul><li>Subsequent identical requests will receive a 429 HTTP Status (Too Many Requests).</li>   <li>After a 2-minute waiting period, the endpoint can be called again. However, if the credentials remain invalid, 401 HTTP Status (Unauthorized) responses will be issued.</li>   </ul><br>   <li>**Overall Request Threshold**:<br>   There is also a threshold for the total number of authentication requests within a given time-frame:</li><br>   <ul><li>More than 10,000 requests to the authenticate endpoint within a 5-minute period will result in a lockout from the endpoint.</li>   <li>Note that the evaluation window for this threshold is 5 minutes. Importantly, 429 HTTP Status responses also count towards the 10,000 request limit.</li>   <li>In the event that the threshold is exceeded, you must wait a full 5 minutes before the endpoint will accept new requests again.</li>   </ul>   </ol>      

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = pycsapi.AuthenticationApi()
body = pycsapi.ConnectAuthenticationAuthRequest() # ConnectAuthenticationAuthRequest |  (optional)

try:
    # Authenticate
    api_response = api_instance.authenticate(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->authenticate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectAuthenticationAuthRequest**](ConnectAuthenticationAuthRequest.md)|  | [optional] 

### Return type

[**ConnectAuthenticationAuthResponse**](ConnectAuthenticationAuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


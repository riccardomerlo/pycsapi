# pycsapi.InstanceManagementApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**instance_configuration**](InstanceManagementApi.md#instance_configuration) | **GET** /decisionEngine/instance/{guid} | Instance Configuration
[**return_all_instances**](InstanceManagementApi.md#return_all_instances) | **GET** /decisionEngine/instances | Return All Available Instances
[**update_instance_configuration**](InstanceManagementApi.md#update_instance_configuration) | **PUT** /decisionEngine/instance/{guid} | Update Instance Configuration

# **instance_configuration**
> object instance_configuration(guid)

Instance Configuration

Returns instance user has permission to access.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.InstanceManagementApi(pycsapi.ApiClient(configuration))
guid = 'guid_example' # str | Get results by guid.

try:
    # Instance Configuration
    api_response = api_instance.instance_configuration(guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceManagementApi->instance_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| Get results by guid. | 

### Return type

**object**

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **return_all_instances**
> GetDecisionEngineInstancesResponse return_all_instances(customer_id=customer_id, user_id=user_id)

Return All Available Instances

Returns all instances (Decision Trees) a user has permission to access.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.InstanceManagementApi(pycsapi.ApiClient(configuration))
customer_id = 56 # int | The unique identifier of the customer. If used it will return all the Decision Trees associated to that customer. (optional)
user_id = 56 # int | The unique identifier of the user. If used it will return all the Decision Trees that user has access to. (optional)

try:
    # Return All Available Instances
    api_response = api_instance.return_all_instances(customer_id=customer_id, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceManagementApi->return_all_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **int**| The unique identifier of the customer. If used it will return all the Decision Trees associated to that customer. | [optional] 
 **user_id** | **int**| The unique identifier of the user. If used it will return all the Decision Trees that user has access to. | [optional] 

### Return type

[**GetDecisionEngineInstancesResponse**](GetDecisionEngineInstancesResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_instance_configuration**
> object update_instance_configuration(guid, body=body)

Update Instance Configuration

Update the instances information.<br><br>You will need to call the `GET /decisionEngine/instance/{guid}` endpoint to get the current configuration and then update the fields you want to change.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.InstanceManagementApi(pycsapi.ApiClient(configuration))
guid = 'guid_example' # str | get results by guid.
body = pycsapi.UpdateDecisionEngineInstanceRequestBodyWithExample() # UpdateDecisionEngineInstanceRequestBodyWithExample |  (optional)

try:
    # Update Instance Configuration
    api_response = api_instance.update_instance_configuration(guid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstanceManagementApi->update_instance_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| get results by guid. | 
 **body** | [**UpdateDecisionEngineInstanceRequestBodyWithExample**](UpdateDecisionEngineInstanceRequestBodyWithExample.md)|  | [optional] 

### Return type

**object**

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


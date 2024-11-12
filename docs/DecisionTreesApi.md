# pycsapi.DecisionTreesApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**decision_trees**](DecisionTreesApi.md#decision_trees) | **GET** /decisionEngine/GUID | Decision Trees
[**user_data_fields**](DecisionTreesApi.md#user_data_fields) | **GET** /decisionEngine/{provenirId}/userDataFields | User Data Fields

# **decision_trees**
> ConnectDecisionEngineGUIDListResponse decision_trees(sort_dir=sort_dir, type=type, sort_by=sort_by, decision_outcome=decision_outcome)

Decision Trees

Returns all decision trees that the user has permission to access.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.DecisionTreesApi(pycsapi.ApiClient(configuration))
sort_dir = 'asc' # str | The direction that you wish to sort results by. (optional) (default to asc)
type = 'type_example' # str | Filter the returned decision trees by their associated decision tree type. (optional)
sort_by = 'sort_by_example' # str | Sort results by this column. (optional)
decision_outcome = false # bool | Fetch decision outcome in guid list endpoint. (optional) (default to false)

try:
    # Decision Trees
    api_response = api_instance.decision_trees(sort_dir=sort_dir, type=type, sort_by=sort_by, decision_outcome=decision_outcome)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DecisionTreesApi->decision_trees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort_dir** | **str**| The direction that you wish to sort results by. | [optional] [default to asc]
 **type** | **str**| Filter the returned decision trees by their associated decision tree type. | [optional] 
 **sort_by** | **str**| Sort results by this column. | [optional] 
 **decision_outcome** | **bool**| Fetch decision outcome in guid list endpoint. | [optional] [default to false]

### Return type

[**ConnectDecisionEngineGUIDListResponse**](ConnectDecisionEngineGUIDListResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_data_fields**
> ConnectDecisionEngineUserDataFieldsResponse user_data_fields(provenir_id)

User Data Fields

Returns the user data fields defined for the given decision tree GUID.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.DecisionTreesApi(pycsapi.ApiClient(configuration))
provenir_id = 'provenir_id_example' # str | The unique identifier of the decision tree, obtained from `/GUID`.

try:
    # User Data Fields
    api_response = api_instance.user_data_fields(provenir_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DecisionTreesApi->user_data_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provenir_id** | **str**| The unique identifier of the decision tree, obtained from &#x60;/GUID&#x60;. | 

### Return type

[**ConnectDecisionEngineUserDataFieldsResponse**](ConnectDecisionEngineUserDataFieldsResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


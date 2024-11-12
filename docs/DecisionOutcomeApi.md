# pycsapi.DecisionOutcomeApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**decision_outcome**](DecisionOutcomeApi.md#decision_outcome) | **GET** /decisionEngine/decisionOutcome/{guid} | Return Decision Outcome
[**update_decision_engine_decision_outcome_details**](DecisionOutcomeApi.md#update_decision_engine_decision_outcome_details) | **PATCH** /decisionEngine/decisionOutcome/{guid} | Update Decision Outcome

# **decision_outcome**
> GetDecisionEngineDecisionOutcomeResponse decision_outcome(guid)

Return Decision Outcome

Returns decision outcomes which is set for decision tree.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.DecisionOutcomeApi(pycsapi.ApiClient(configuration))
guid = 'guid_example' # str | get results by guid.

try:
    # Return Decision Outcome
    api_response = api_instance.decision_outcome(guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DecisionOutcomeApi->decision_outcome: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| get results by guid. | 

### Return type

[**GetDecisionEngineDecisionOutcomeResponse**](GetDecisionEngineDecisionOutcomeResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_decision_engine_decision_outcome_details**
> InlineResponse2004 update_decision_engine_decision_outcome_details(guid, body=body)

Update Decision Outcome

This allows the user to manually update the decision outcome

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.DecisionOutcomeApi(pycsapi.ApiClient(configuration))
guid = 'guid_example' # str | updates decision outcomes by guid.
body = pycsapi.ConnectDecisionEnginePatchDecisionOutcomeRequest() # ConnectDecisionEnginePatchDecisionOutcomeRequest |  (optional)

try:
    # Update Decision Outcome
    api_response = api_instance.update_decision_engine_decision_outcome_details(guid, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DecisionOutcomeApi->update_decision_engine_decision_outcome_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| updates decision outcomes by guid. | 
 **body** | [**ConnectDecisionEnginePatchDecisionOutcomeRequest**](ConnectDecisionEnginePatchDecisionOutcomeRequest.md)|  | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


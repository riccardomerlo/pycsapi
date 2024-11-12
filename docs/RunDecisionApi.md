# pycsapi.RunDecisionApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**run_decision_tree**](RunDecisionApi.md#run_decision_tree) | **POST** /decisionEngine/{provenirId} | Run Decision Tree

# **run_decision_tree**
> ConnectDecisionEngineRunDecisionResponse run_decision_tree(company_id, provenir_id, body=body, origination_id=origination_id)

Run Decision Tree

Runs the provided decision tree for the given company, optionally using the data provided in the body of the call.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.RunDecisionApi(pycsapi.ApiClient(configuration))
company_id = 'company_id_example' # str | The Connect ID for the company that you wish to run the decision tree on. Obtained from `/companies` search results. A Connect ID is the primary Company identifier that is used to uniquely identify all companies across Creditsafe's Universe and Partner Network.
provenir_id = 'provenir_id_example' # str | The unique identifier of the decision tree to run, obtained from `/GUID`.
body = NULL # object |  (optional)
origination_id = 'origination_id_example' # str | An optional field that will allow text passed through to be stored against the decision. Typically used for internal identifiers (e.g. SalesForce IDs). (optional)

try:
    # Run Decision Tree
    api_response = api_instance.run_decision_tree(company_id, provenir_id, body=body, origination_id=origination_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RunDecisionApi->run_decision_tree: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The Connect ID for the company that you wish to run the decision tree on. Obtained from &#x60;/companies&#x60; search results. A Connect ID is the primary Company identifier that is used to uniquely identify all companies across Creditsafe&#x27;s Universe and Partner Network. | 
 **provenir_id** | **str**| The unique identifier of the decision tree to run, obtained from &#x60;/GUID&#x60;. | 
 **body** | [**object**](object.md)|  | [optional] 
 **origination_id** | **str**| An optional field that will allow text passed through to be stored against the decision. Typically used for internal identifiers (e.g. SalesForce IDs). | [optional] 

### Return type

[**ConnectDecisionEngineRunDecisionResponse**](ConnectDecisionEngineRunDecisionResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


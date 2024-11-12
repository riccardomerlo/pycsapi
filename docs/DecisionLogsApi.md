# pycsapi.DecisionLogsApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**decision_history**](DecisionLogsApi.md#decision_history) | **GET** /decisionEngine/usageLog | Decision History
[**get_decision_log**](DecisionLogsApi.md#get_decision_log) | **GET** /decisionEngine/usageLog/{decisionLogId} | Get Decision Log
[**update_decision_log**](DecisionLogsApi.md#update_decision_log) | **PATCH** /decisionEngine/usageLog/{decisionLogId} | Update Decision Log

# **decision_history**
> ConnectDecisionEngineUsageLogResponse decision_history(provenir_id=provenir_id, company_id=company_id, company_name=company_name, status=status, from_date=from_date, to_date=to_date, page=page, page_size=page_size)

Decision History

Returns a log of all previously ran decisions that the user has permission to access, optionally filtered.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.DecisionLogsApi(pycsapi.ApiClient(configuration))
provenir_id = 'provenir_id_example' # str | Filter the returned usage log by the GUID for the associated decision trees, obtained from `/GUID`. (optional)
company_id = 'company_id_example' # str | Filter the returned usage log by the Connect ID for the associated companies for each decision. (optional)
company_name = 'company_name_example' # str | Filter the returned usage log by the Company Name for the associated companies for each decision. (optional)
status = 1.2 # float | Filter the returned usage log by the status for each decision. (optional)
from_date = '2013-10-20T19:20:30+01:00' # datetime | Filter the returned usage log by the date the the decision was run. (optional)
to_date = '2013-10-20T19:20:30+01:00' # datetime | Filter the returned usage log by the date the the decision was run. (optional)
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 56 # int | Number of items to return per Page. (optional)

try:
    # Decision History
    api_response = api_instance.decision_history(provenir_id=provenir_id, company_id=company_id, company_name=company_name, status=status, from_date=from_date, to_date=to_date, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DecisionLogsApi->decision_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provenir_id** | **str**| Filter the returned usage log by the GUID for the associated decision trees, obtained from &#x60;/GUID&#x60;. | [optional] 
 **company_id** | **str**| Filter the returned usage log by the Connect ID for the associated companies for each decision. | [optional] 
 **company_name** | **str**| Filter the returned usage log by the Company Name for the associated companies for each decision. | [optional] 
 **status** | **float**| Filter the returned usage log by the status for each decision. | [optional] 
 **from_date** | **datetime**| Filter the returned usage log by the date the the decision was run. | [optional] 
 **to_date** | **datetime**| Filter the returned usage log by the date the the decision was run. | [optional] 
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Number of items to return per Page. | [optional] 

### Return type

[**ConnectDecisionEngineUsageLogResponse**](ConnectDecisionEngineUsageLogResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_decision_log**
> ConnectDecisionEngineDecisionLogResponse get_decision_log(decision_log_id)

Get Decision Log

Returns a specified decision log for a previously ran decision.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.DecisionLogsApi(pycsapi.ApiClient(configuration))
decision_log_id = 'decision_log_id_example' # str | The unique identifier of the decision log to retrieve, obtained from `/usageLog`.

try:
    # Get Decision Log
    api_response = api_instance.get_decision_log(decision_log_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DecisionLogsApi->get_decision_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **decision_log_id** | **str**| The unique identifier of the decision log to retrieve, obtained from &#x60;/usageLog&#x60;. | 

### Return type

[**ConnectDecisionEngineDecisionLogResponse**](ConnectDecisionEngineDecisionLogResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_decision_log**
> ConnectDecisionEngineDecisionLogResponse update_decision_log(decision_log_id, body=body)

Update Decision Log

Updates the status and/or notes for a specified decision.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.DecisionLogsApi(pycsapi.ApiClient(configuration))
decision_log_id = 'decision_log_id_example' # str | The unique identifier of the decision log to retrieve, obtained from `/usageLog`.
body = pycsapi.ConnectDecisionEngineUpdateDecisionRequest() # ConnectDecisionEngineUpdateDecisionRequest |  (optional)

try:
    # Update Decision Log
    api_response = api_instance.update_decision_log(decision_log_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DecisionLogsApi->update_decision_log: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **decision_log_id** | **str**| The unique identifier of the decision log to retrieve, obtained from &#x60;/usageLog&#x60;. | 
 **body** | [**ConnectDecisionEngineUpdateDecisionRequest**](ConnectDecisionEngineUpdateDecisionRequest.md)|  | [optional] 

### Return type

[**ConnectDecisionEngineDecisionLogResponse**](ConnectDecisionEngineDecisionLogResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


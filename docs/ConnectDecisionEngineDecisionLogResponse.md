# ConnectDecisionEngineDecisionLogResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | A unique ID assigned to this request. | [optional] 
**decision_log_id** | **float** | The unique identifier for the decision log. | [optional] 
**provenir_id** | **str** | The unique identifier of the decision tree. | [optional] 
**friendly_name** | **str** | The name of the decision tree. | [optional] 
**user_id** | **float** | The unique identifier for the user&#x27;s account, used across the Creditsafe product suite. | [optional] 
**company_id** | **str** | The connectId of the company that the decision was ran on. A connectId is the primary Company identifier that is used to uniquely identify all companies across Creditsafe&#x27;s Universe and Partner Network. | [optional] 
**company_name** | **str** | The name of the company that the decision was ran on. | [optional] 
**response** | [**ConnectDecisionEngineDecisionLogResponseResponse**](ConnectDecisionEngineDecisionLogResponseResponse.md) |  | [optional] 
**decision_date** | **datetime** | The timestamp that the decision model was run. | [optional] 
**origination_id** | **str** | Displays the optional text passed through to be stored against the decision in the original call to &#x60;/{provenirId}&#x60;. Typically used for internal identifiers (e.g. SalesForce IDs). | [optional] 
**status** | **float** | The status of the decision. typically, 1 is reserved for positive outcomes, 2 for pending status and 3 for negative outcomes. | [optional] 
**notes** | **str** | The notes associated with this decision. | [optional] 
**modified_date** | **datetime** | The timestamp that this decision was last modified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


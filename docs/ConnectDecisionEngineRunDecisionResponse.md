# ConnectDecisionEngineRunDecisionResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decision** | **str** | The decision returned by the automated decision model. | [optional] 
**decision_text** | **str** | The text output to accompany the decision returned by the decision model. | [optional] 
**audits** | [**list[ConnectDecisionEngineRunDecisionResponseAudits]**](ConnectDecisionEngineRunDecisionResponseAudits.md) | An array of audit values. The parameters output for audit are tailored and bespoke to each decision tree. | [optional] 
**origination_id** | **str** | Displays the optional text passed through to be stored against the decision in the original call to &#x60;/{provenirId}&#x60;. Typically used for internal identifiers (e.g. SalesForce IDs). | [optional] 
**status_code** | **str** | The status of the decision. typically, 1 is reserved for positive outcomes, 2 for pending status and 3 for negative outcomes. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


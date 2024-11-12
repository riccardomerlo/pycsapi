# UpdateDecisionEngineInstanceRequestBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** | The template ID of the decision tree to be updated. | 
**guid** | **str** | The GUID to be updated. | 
**decision_tree_name** | **str** | The name of the decision tree to be updated. | 
**customer_id** | **int** | The customer ID to be updated. | [optional] 
**input_params** | **object** | The input parameters to be updated can be obtained from the &#x60;GET/instance configuration&#x60; endpoint. | [optional] 
**configuration_variables** | **object** | The Configuration Variables to be updated can be obtained from the &#x60;GET/instance configuration&#x60; endpoint. | [optional] 
**scalar_variables** | **object** | The Scalar Variables to be updated can be obtained from the &#x60;GET/instance configuration&#x60; endpoint. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


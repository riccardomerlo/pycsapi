# ConnectDecisionEngineUserDataFieldsResponseFields

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_index** | **float** | Used to assist ordering of the user data fields on a UI. | [optional] 
**label** | **str** | The user-friendly label for the field for display on a UI. | [optional] 
**param_name** | **str** | The string value for the parameter to be used when calling the &#x60;/{guid}&#x60; endpoint. | [optional] 
**field_type** | **str** | The type of user data field. | [optional] 
**mandatory** | **bool** | Flag to dictate whether the user data field is required when running the associated decision tree. | [optional] 
**dropdown_details** | [**list[ConnectDecisionEngineUserDataFieldsResponseDropdownDetails]**](ConnectDecisionEngineUserDataFieldsResponseDropdownDetails.md) |  | [optional] 
**validation** | [**list[ConnectDecisionEngineUserDataFieldsResponseValidation]**](ConnectDecisionEngineUserDataFieldsResponseValidation.md) | Optional validation rules that should be applied to the corresponding user data field prior to running the decision tree. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


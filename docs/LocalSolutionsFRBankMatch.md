# LocalSolutionsFRBankMatch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | **str** | The domain associated with the match. | [optional] 
**created_by** | **str** | The user or system that created the match record. | [optional] 
**created_date** | **datetime** | The date and time when the match record was created. | [optional] 
**last_modified_by** | **str** | The user or system that last modified the match record. | [optional] 
**last_modified_date** | **datetime** | The date and time when the match record was last modified. | [optional] 
**id** | **str** | The unique identifier of the match record. | [optional] 
**score** | **int** | The score assigned to the match. | [optional] 
**classification** | **str** | The classification of the match. | [optional] 
**status** | **str** | The current status of the match. | [optional] 
**entity** | [**LocalSolutionsFRBankMatchEntity**](LocalSolutionsFRBankMatchEntity.md) |  | [optional] 
**issuer_company** | [**LocalSolutionsFRBankMatchIssuerCompany**](LocalSolutionsFRBankMatchIssuerCompany.md) |  | [optional] 
**input** | [**LocalSolutionsFRBankMatchInput**](LocalSolutionsFRBankMatchInput.md) |  | [optional] 
**with_deferred_result** | **bool** | Indicates if the match result is deferred. | [optional] 
**by_api** | **bool** | Indicates if the match was processed via API. | [optional] 
**by_ftp** | **bool** | Indicates if the match was processed via FTP. | [optional] 
**workflow** | **str** | The workflow associated with the match. | [optional] 
**reasons** | **list[str]** | The reasons associated with the match. | [optional] 
**reason_labels** | **dict(str, str)** | Labels for the reasons associated with the match. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


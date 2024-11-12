# InvestigationResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **datetime** |  | 
**created_by** | **int** |  | 
**search_criteria** | [**InvestigationQuery**](InvestigationQuery.md) |  | 
**schedule_id** | **str** |  | [optional] 
**profile_id** | **str** |  | [optional] 
**profile_name** | **str** |  | [optional] 
**alerts_count** | **int** |  | [optional] 
**current_alert** | [**InvestigationAlert**](InvestigationAlert.md) |  | [optional] 
**results** | [**list[Record]**](Record.md) |  | 
**not_found_record_ids** | **list[int]** |  | 
**investigation_name** | **str** |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


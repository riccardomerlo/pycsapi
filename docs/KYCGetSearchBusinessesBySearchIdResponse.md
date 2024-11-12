# KYCGetSearchBusinessesBySearchIdResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the search | [optional] 
**name** | **str** | Name provided for the search. Length must not exceed 200 characters | [optional] 
**country_codes** | **list[str]** | Countries provided to the search | [optional] 
**threshold** | **int** | Hits with scores below this value will not be shown. | [optional] 
**type** | **str** | Indicates whether search type is individual or business | [optional] 
**datasets** | **list[str]** | Provided datasets for the search | [optional] 
**status** | **str** | Status of the search. Available values are new, approved, declined, pending, cancelled, referred and closed. | [optional] 
**risk_rating** | **str** | The risk rating being assigned to the profile | [optional] 
**assigned_to_user_id** | **int** | Id of the user assigned to the search | [optional] 
**assigned_user** | **str** | Name of the user assigned to the search | [optional] 
**created_by_id** | **int** | Id of the user who created the search | [optional] 
**created_by** | **str** | Name of the user who created the search | [optional] 
**created_at** | **datetime** | Search created date time | [optional] 
**modified_by_id** | **int** | Id of the user who modified the search | [optional] 
**modified_by** | **str** | Name of the user who modified the search | [optional] 
**modified_at** | **datetime** | Search modified date time | [optional] 
**note** | **str** | Note associated with the search | [optional] 
**schedule_id** | **str** | Schedule Id linked to the search | [optional] 
**total_hit_count** | **int** | Total number of hits in the search | [optional] 
**true_positive_hits_count** | **int** | The number of true-positive hits in the search | [optional] 
**false_positive_hits_count** | **int** | The number of false-positive hits in the search | [optional] 
**undecided_hits_count** | **int** | The number of undecided hits in the search | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

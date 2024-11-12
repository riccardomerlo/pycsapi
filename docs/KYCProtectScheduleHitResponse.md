# KYCProtectScheduleHitResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Id of the search hit. | [optional] 
**hit_score** | **int** | The hit score associated to the search hit. | [optional] 
**name** | **str** | The name associated to the search hit. | [optional] 
**match** | **str** | The match string associated to the search hit. | [optional] 
**countries** | **list[str]** | The countries associated to the search hit. | [optional] 
**datasets** | **list[str]** | The datasets associated to the search hit. | [optional] 
**decision** | **str** | The decision made on the search hit. | [optional] 
**note** | **str** | The note added to the search hit. | [optional] 
**modified_by_id** | **int** | The search hit last modified by user id. | [optional] 
**modified_by** | **str** | The search hit last modified by user name. | [optional] 
**modified_at** | **datetime** | The search hit last modified date and time. | [optional] 
**created_at** | **datetime** | The search hit created date and time. | [optional] 
**first_name** | **str** | The first name of the search hit. | [optional] 
**middle_name** | **str** | The middle name of the search hit. | [optional] 
**last_name** | **str** | The last name of the search hit. | [optional] 
**gender** | **str** | The gender associated to the search hit. | [optional] 
**dates_of_birth** | **list[date]** | The dates of birth associated to the search hit. | [optional] 
**pep_tier** | **str** | The pep tier associated to the search hit. | [optional] 
**profile_images** | **list[str]** | The profile images associated to the search hit. | [optional] 
**superseded_hit** | [**KYCProtectBaseIndividualSearchResultHitSummaryResponse**](KYCProtectBaseIndividualSearchResultHitSummaryResponse.md) |  | [optional] 
**search_id** | **str** | The id of the search that was being scheduled | [optional] 
**profile_id** | **str** | The id of the profile linked to the search that was being scheduled | [optional] 
**schedule_id** | **str** | The id of the schedule | [optional] 
**key_party_id** | **str** | The id of the key party linked to the search that was being scheduled | [optional] 
**search_type** | **str** | The type of the search that was being scheduled | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

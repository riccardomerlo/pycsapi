# InlineResponse20013

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the schedule | [optional] 
**search_id** | **str** | The id of the search that was being scheduled | [optional] 
**is_email_required** | **bool** | Indicates whether the schedule requires an email to be sent when the search is run | [optional] 
**email_recipients** | **list[str]** | The email recipients that the email should be sent to when the search is run | [optional] 
**created_by_id** | **int** | The id of the user who created the schedule | [optional] 
**created_at** | **datetime** | The time the schedule was created | [optional] 
**created_by** | **str** | The name of the user who created the schedule | [optional] 
**modified_by_id** | **int** | The id of the user who last modified the schedule | [optional] 
**modified_at** | **datetime** | The time the schedule was last modified | [optional] 
**modified_by** | **str** | The name of the user who last modified the schedule | [optional] 
**type** | **str** | The type of the schedule, i.e. business or individual | [optional] 
**name** | **str** | The name used in the search criteria | [optional] 
**first_name** | **str** | The first name used in the search criteria | [optional] 
**middle_name** | **str** | The middle name used in the search criteria | [optional] 
**last_name** | **str** | The last name used in the search criteria | [optional] 
**gender** | **str** | The gender used in the search criteria, i.e. male or female | [optional] 
**date_of_birth** | **date** | The date of birth used in the search criteria | [optional] 
**countries** | **list[str]** | The list of country codes used in the search criteria | [optional] 
**threshold** | **int** | The threshold used in the search criteria | [optional] 
**datasets** | **list[str]** | The datasets used in the search criteria | [optional] 
**pep_tiers** | **list[str]** | The pep tiers used in the search criteria, i.e. pepTier1, pepTier2, pepTier3 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


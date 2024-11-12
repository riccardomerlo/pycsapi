# ConnectProtectCreateInvestigationQueryDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Individual relates to individuals &lt;br&gt; Business relates to businesses and organisations e.g political parties and terrorist groups. | 
**name** | **str** | The full or partial business or individual name | [optional] 
**screening_threshold** | **int** | Default Threshold is 85. Can only enter the following options: 85, 90, 95, 100 | [optional] 
**country_code** | **str** |  | [optional] 
**first_name** | **str** | Individual Only - To be used instead of &#x27;&#x27;name&#x27;&#x27; field should the user want to split out the name into first, middle, last. | [optional] 
**middle_name** | **str** | Individual Only - To be used instead of &#x27;&#x27;name&#x27;&#x27; field should the user want to split out the name into first, middle, last. | [optional] 
**last_name** | **str** | Individual Only - To be used instead of &#x27;&#x27;name&#x27;&#x27; field should the user want to split out the name into first, middle, last. | [optional] 
**date_of_birth** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


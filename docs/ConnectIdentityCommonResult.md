# ConnectIdentityCommonResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **int** | A unique identifier for the customer who initiated the search. This ID helps in associating the search with a specific customer in the database. | [optional] 
**user_id** | **int** | The unique identifier of the user who performed the search. This can be used for audit trails and to track user activity. | [optional] 
**unique_id** | **str** | An optional unique identifier for the search result, which can be used for referencing and retrieval in subsequent operations. | [optional] 
**search_text** | **str** | The text input provided by the user for the search. This field captures the query terms used in the search process. | [optional] 
**reference** | **str** | A reference code or string that may be used to link this search to other transactions or processes within the system. | [optional] 
**search_time** | **datetime** | The exact date and time when the search was executed, recorded in ISO 8601 format. This timestamp is crucial for logging and chronological analysis. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


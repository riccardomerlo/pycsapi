# PutBatchUploadsRetryByIdResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Batch upload request Id | [optional] 
**filename** | **str** | User given file name | [optional] 
**status** | **str** | Batch upload status (submitted, validating, rejected, validated, insufficientCredits, queued, inProgress, processed, completed, partiallyCompleted, failed) | [optional] 
**row_count** | **int** | Batch upload file record count | [optional] 
**success_count** | **int** | Successful record count in batch upload file | [optional] 
**uploaded_at** | **datetime** | Batch upload requested timestamp | [optional] 
**uploaded_by_id** | **int** | Batch upload requested by user id | [optional] 
**uploaded_by** | **str** | Batch file uploaded by user | [optional] 
**completed_at** | **datetime** | Batch upload completed timestamp | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


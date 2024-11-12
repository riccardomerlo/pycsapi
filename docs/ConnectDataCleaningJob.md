# ConnectDataCleaningJob

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID number associated to the created job - used for future searches | [optional] 
**name** | **str** | The name associated to the &#x27;Job Number&#x27; created by the user in the &#x27;POST - Create Job Request&#x27; | [optional] 
**created_at** | **datetime** |  | [optional] 
**modified_at** | **datetime** |  | [optional] 
**managing_user_id** | **int** |  | [optional] 
**managing_customer_id** | **int** |  | [optional] 
**owning_customer_id** | **int** |  | [optional] 
**owning_user_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**country_code** | **str** | Available after Enrichment | [optional] 
**portfolio_id** | **str** | Available after Enrichment | [optional] 
**source** | **str** |  | [optional] 
**job_summary** | [**ConnectDataCleaningJobJobSummary**](ConnectDataCleaningJobJobSummary.md) |  | [optional] 
**job_enrichment_settings** | [**ConnectDataCleaningJobJobEnrichmentSettings**](ConnectDataCleaningJobJobEnrichmentSettings.md) |  | [optional] 
**archived** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


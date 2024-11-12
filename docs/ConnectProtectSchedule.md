# ConnectProtectSchedule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | A unique ID assigned to this request. | [optional] 
**id** | **str** |  | 
**customer_id** | **int** |  | 
**user_id** | **int** |  | 
**investigation_id** | **str** |  | 
**investigation** | [**ConnectProtectInvestigation**](ConnectProtectInvestigation.md) |  | 
**frequency** | [**ConnectProtectAlertsFrequency**](ConnectProtectAlertsFrequency.md) |  | 
**screening_threshold** | **int** | Can only enter the following options: 85, 90, 95, 100 | 
**created_at** | **datetime** |  | 
**is_email_required** | **bool** |  | [optional] 
**is_disabled** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


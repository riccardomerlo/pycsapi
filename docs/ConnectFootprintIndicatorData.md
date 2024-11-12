# ConnectFootprintIndicatorData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | A unique ID assigned to this request. | [optional] 
**safe_number** | **str** | Safe Number - Identifier for Companies in Creditsafe&#x27;s Home Countries. | [optional] 
**credit_safe** | [**ConnectFootprintDataFinanceCreditSafe**](ConnectFootprintDataFinanceCreditSafe.md) |  | [optional] 
**overall_aggregations** | **AllOfConnectFootprintIndicatorDataOverallAggregations** |  | [optional] 
**history** | [**list[ConnectCcdsHistory]**](ConnectCcdsHistory.md) | List of accounts connected to the company, snapshot of account at point in time each month. | [optional] 
**financial_indicator** | [**ConnectFootprintIndicatorDataFinancialIndicator**](ConnectFootprintIndicatorDataFinancialIndicator.md) |  | [optional] 
**footprint_data** | [**ConnectFootprintIndicatorDataFootprintData**](ConnectFootprintIndicatorDataFootprintData.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


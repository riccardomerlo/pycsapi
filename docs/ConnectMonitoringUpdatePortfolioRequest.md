# ConnectMonitoringUpdatePortfolioRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the portfolio | 
**is_default** | **bool** | Change the setting of the portfolio as default for company monitoring events.&lt;br&gt;&lt;br&gt; Changing the default portfolio will automatically change the status of the previous default to &#x27;false&#x27;. | [optional] 
**emails** | [**list[ConnectMonitoringUpdatePortfolioRequestEmail]**](ConnectMonitoringUpdatePortfolioRequestEmail.md) | The email addresses of the user to receive the email notification. | [optional] 
**email_subject** | **str** | The subject of the email notification. | [optional] 
**email_language** | **str** | The language of the email notification. | [optional] 
**frequency** | **str** | For emails to be activated you must submit a value of &#x27;1&#x27; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


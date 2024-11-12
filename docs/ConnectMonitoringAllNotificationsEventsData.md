# ConnectMonitoringAllNotificationsEventsData

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | [**ConnectMonitoringCompanyInfo**](ConnectMonitoringCompanyInfo.md) |  | [optional] 
**event_id** | **float** | The unique identifier of the event that triggered the generation of the &#x60;notificationEvent&#x60;. This identifier is consistent across all portfolios in the Global Monitoring product. | [optional] 
**event_date** | **datetime** | The date that the event occurred. | [optional] 
**new_value** | **str** | Some events contain an &#x60;oldValue&#x60; and &#x60;newValue&#x60; (e.g. a change in Credit Limit). | [optional] 
**old_value** | **str** | Some events contain an &#x60;oldValue&#x60; and &#x60;newValue&#x60; (e.g. a change in Credit Limit). | [optional] 
**notification_event_id** | **float** | The unique identifier for the &#x60;notificationEvent&#x60;. This identifier is tied to a specific &#x60;eventId&#x60; and &#x60;portfolioId&#x60;. | [optional] 
**notification_id** | **float** | The unique identifier for the &#x60;notificationEvent&#x60;. This identifier is tied to a specific &#x60;eventId&#x60; and &#x60;portfolioId&#x60;. | [optional] 
**processed_date** | **datetime** | If the Notification was sent by email, the date will be populated with when the notification was sent. | [optional] 
**rule_code** | **float** | The unique identifier for the &#x60;ruleCode&#x60; that triggered the generation of the &#x60;notificationEvent&#x60;. | [optional] 
**rule_name** | **str** | The name of the notification event rule that triggered the generation of the &#x60;notificationEvent&#x60;. | [optional] 
**summary** | **str** | A short description of the notification event rule that triggered the &#x60;notificationEvent&#x60;. | [optional] 
**rule_text** | **str** | A short description of the notification event rule that triggered the &#x60;notificationEvent&#x60;. | [optional] 
**local_event_code** | **str** | The local code of the &#x60;notificationEvent&#x60;. | [optional] 
**is_processed** | **bool** | a &#x60;true&#x60; or &#x60;false&#x60; flag for each event. Can be updated using the PATCH endpoint. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


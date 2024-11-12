# MODEL6bcc20

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold** | **int** | The threshold to use when running the schedule. Must be one of 75, 80, 85, 90, 95, 100.  Changing threshold will cause even decided results to come back again and a new  decision will need to be made. | [optional] 
**datasets** | **list[str]** | The datasets to use when running the schedule.  Changing datasets will cause even decided results to come back again and a new  decision will need to be made.&lt;br&gt;&lt;br&gt; Note: Please refer to the corresponding endpoint that the schedule is set against for the correct dataset options | [optional] 
**is_email_required** | **bool** | Set to true to send an email when the schedule is run. If there are no email recipients set then  this will be ignored. | [optional] 
**email_recipients** | **list[str]** | The list of email recipients to send the email to when the schedule is run. Email will not be sent if IsEmailRequired is false. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


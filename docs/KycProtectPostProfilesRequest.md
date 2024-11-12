# KycProtectPostProfilesRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the profile being created.&lt;br&gt; This MUST be unique across your profiles. | 
**type** | **str** | The profile type to be created. This will effect searches later for validations.&lt;br&gt; i.e. Not being able to apply certain datasets (Example - State Owned Enterprises) to an Individual profile. Ensure the correct type is applied for intended search. | 
**internal_id** | **str** | Internal ID of the profile, this MUST be unique across your profiles. | [optional] 
**assigned_to_id** | **int** | Creditsafe Id of the user to assign the profile to. | [optional] 
**kyc_review_on** | **str** | The date to which the profile should be reviewed. &lt;br&gt; Format YYYY-MM-DD &lt;br&gt; Validates when the date changes and is either current or in the future. | [optional] 
**status** | **str** | Status of the profile. | [optional] 
**risk_rating** | **str** | Risk rating of the profile. | [optional] 
**kyc_comments** | **str** | Free text field for users to highlight key information to other users. &lt;br&gt; Maximum characters allowed is 250 | [optional] 
**details** | [**KycProtectPostProfilesRequestDetails**](KycProtectPostProfilesRequestDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


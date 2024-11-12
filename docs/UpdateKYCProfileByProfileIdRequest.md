# UpdateKYCProfileByProfileIdRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the profile to be updated. | 
**risk_rating** | **str** | Risk rating of the profile. | 
**status** | **str** | Status of the profile. | 
**internal_id** | **str** | Internal ID of the profile, this MUST be unique across your profiles. | [optional] 
**assigned_to_id** | **object** | Creditsafe Id of the user to assign the profile to. &lt;br&gt; Passing null will unassign the profile. | [optional] 
**kyc_review_on** | **object** | The date to which the profile should be reviewed. &lt;br&gt; Format YYYY-MM-DD &lt;br&gt; Validates when the date changes and is either current or in the future. | [optional] 
**kyc_comments** | **str** | Free text field for users to highlight key information to other users. &lt;br&gt; Maximum characters allowed is 250 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


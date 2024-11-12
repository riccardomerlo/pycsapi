# KycProtectProfileAssignBulkResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the Profile | [optional] 
**name** | **str** | Name of the Profile | [optional] 
**risk_rating** | **str** | Risk rating given to profile. Available values are notApplicable, veryLow, low, medium, high and veryHigh. | [optional] 
**status** | **str** | Status of the profile. Available values are new, approved, declined, pending, cancelled, referred, closed and approvedReviewDue. | [optional] 
**type** | **str** | Type of the profile. Available values are trust, individual, soleTrader, company, plc, partnership and otherEntity. | [optional] 
**internal_id** | **object** | Internal Id given to profile by customer | [optional] 
**assigned_to_id** | **object** | Id of the user assigned to the profile | [optional] 
**assigned_to** | **object** | Name of the user assigned to the profile | [optional] 
**safe_number** | **object** | safe number of the business linked to the profile | [optional] 
**company_id** | **object** | company id of the business linked to the profile | [optional] 
**formation_date** | **object** | Formation date of the business linked to the profile | [optional] 
**created_at** | **datetime** | Profile created time | [optional] 
**created_by_id** | **int** | Id of the user who created the profile | [optional] 
**created_by** | **str** | Name of the user who created the profile | [optional] 
**modified_at** | **object** | Profile last updated time | [optional] 
**modified_by_id** | **object** | Id of the user who last modified the profile | [optional] 
**modified_by** | **object** | Name of the user who last modified the profile | [optional] 
**kyc_approved_at** | **datetime** | Date when the profile got approved | [optional] 
**kyc_review_on** | **object** | Date when profile is to be reviewed | [optional] 
**kyc_status_updated_on** | **object** | Date when the profile status was last updated | [optional] 
**kyc_comments** | **object** | Profile comments | [optional] 
**note_count** | **int** | Count of notes associated with profile | [optional] 
**attachment_count** | **int** | Count of attachments associated with profile | [optional] 
**key_party_count** | **int** | Count of key parties associated with profile | [optional] 
**ubo_count** | **int** | Count of UBOs associated with profile | [optional] 
**open_alert_count** | **int** | Count of Open Alerts | [optional] 
**mode_of_creation** | **str** | Mode of profile creation. Available values are manual, import and batchUpload. | [optional] 
**import_status** | **object** | Status of profile creation. Available values are submitted, preprocessed, validated, queued, inProgress, processed, completed, partiallyCompleted and failed. | [optional] 
**is_locked** | **bool** | Value indicating whether the profile is locked | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


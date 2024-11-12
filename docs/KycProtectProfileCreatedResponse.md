# KycProtectProfileCreatedResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the Profile | [optional] 
**name** | **str** | Name of the Profile | [optional] 
**risk_rating** | **str** | Risk rating given to profile (notApplicable, veryLow, low, medium, high, veryHigh) | [optional] 
**status** | **str** | Status of the profile (new, approved, declined, pending, cancelled, referred, closed, approvedReviewDue) | [optional] 
**type** | **str** | Type of the profile (trust, individual, soleTrader, company, plc, partnership, otherEntity) | [optional] 
**internal_id** | **str** | Internal Id given to profile by customer | [optional] 
**assigned_to_id** | **int** | Id of the user assigned to the profile | [optional] 
**assigned_to** | **str** | Name of the user assigned to the profile | [optional] 
**safe_number** | **str** | safe number of the business linked to the profile | [optional] 
**company_id** | **str** | company id of the business linked to the profile | [optional] 
**formation_date** | **date** | Formation date of the business linked to the profile | [optional] 
**created_at** | **datetime** | Profile created time | [optional] 
**created_by_id** | **int** | Id of the user who created the profile | [optional] 
**created_by** | **str** | Name of the user who created the profile | [optional] 
**modified_at** | **datetime** | Profile last updated time | [optional] 
**modified_by_id** | **int** | Id of the user who last modified the profile | [optional] 
**modified_by** | **str** | Name of the user who last modified the profile | [optional] 
**kyc_approved_at** | **datetime** | Date when the profile got approved | [optional] 
**kyc_review_on** | **date** | Date when profile is to be reviewed | [optional] 
**kyc_status_updated_on** | **datetime** | Date when the profile status was last updated | [optional] 
**kyc_comments** | **str** | Profile comments | [optional] 
**note_count** | **int** | Count of notes associated with profile | [optional] 
**attachment_count** | **int** | Count of attachments associated with profile | [optional] 
**key_party_count** | **int** | Count of key parties associated with profile | [optional] 
**ubo_count** | **int** | Count of UBOs associated with profile | [optional] 
**open_alert_count** | **int** | Count of Open Alerts | [optional] 
**mode_of_creation** | **str** | Mode of profile creation (manual, import) | [optional] 
**import_status** | **str** | Status of profile creation (submitted, preprocessed, validated, queued, inProgress, processed, completed, partiallyCompleted, failed) | [optional] 
**is_locked** | **bool** | Value indicating whether the profile is locked | [optional] 
**details** | [**KycProtectProfileCreatedResponseDetails**](KycProtectProfileCreatedResponseDetails.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# KycProtectProfileCreatedResponseDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **str** | Id of the profile | [optional] 
**legal_name** | **str** | Name of the business/individual | [optional] 
**trading_name** | **str** | Trading name of the entity | [optional] 
**aliases** | **list[str]** | Alias names given for the entity | [optional] 
**activity** | **str** | Activity of the business e.g., NAICS/SIC codes | [optional] 
**description** | **str** | Description of the entity | [optional] 
**contact_name** | **str** | Contact person name | [optional] 
**email** | **str** | Contact email address | [optional] 
**website** | **str** | Entity website address | [optional] 
**telephone** | **str** | Contact telephone number | [optional] 
**turnover** | [**KycProtectProfileCreatedResponseDetailsTurnover**](KycProtectProfileCreatedResponseDetailsTurnover.md) |  | [optional] 
**assets_under_management** | [**KycProtectProfileCreatedResponseDetailsAssetsUnderManagement**](KycProtectProfileCreatedResponseDetailsAssetsUnderManagement.md) |  | [optional] 
**date_of_birth** | **date** | Date of birth of the individual | [optional] 
**country_code** | **str** | Two-letter country code ISO-3166-2 | [optional] 
**vat_no** | **str** | Tax Identification Number of the business | [optional] 
**is_listed_on_exchange** | **bool** | Details of company listed on exchange | [optional] 
**exchange_name** | **str** | Gets the name of the exchange. | [optional] 
**organization_number** | **str** | Gets the organisation number. | [optional] 
**internal_contact** | **str** | Gets the internal contact. | [optional] 
**internal_email** | **str** | Gets the internal email. | [optional] 
**international_score** | **str** | Gets the international score. | [optional] 
**created_at** | **datetime** | Profile details created time | [optional] 
**created_by_id** | **int** | Id of the user who created profile | [optional] 
**created_by** | **str** | Name of the user who created profile | [optional] 
**modified_at** | **datetime** | Profile details last updated time | [optional] 
**modified_by_id** | **int** | Id of the user who last modified the profile | [optional] 
**modified_by** | **str** | Name of the user who last modified the profile | [optional] 
**note_count** | **int** | Count of notes associated with profile details | [optional] 
**attachment_count** | **int** | Count of attachment associated with profile details | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# KycProtectPostProfilesRequestDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legal_name** | **str** | Name of the Business or Individual&lt;br&gt; Maximum length is 150 characters | 
**trading_name** | **str** | Valid for profile type - SoleTrader&lt;br&gt; Maximum length is 150 characters | [optional] 
**aliases** | **str** | Name of any Aliases&lt;br&gt; Maximum length of each alias is 150 characters | [optional] 
**activity** | **str** | Activity of the Business e.g. NAIC S/SIC Codes&lt;br&gt; Valid for profile types - Trust, Company, Partnership, OtherEntity and PLC&lt;br&gt; Maximum length of activity is 150 characters | [optional] 
**description** | **str** | Description of the business/individual entity&lt;br&gt; Valid for the profile types Trust, Company, Partnership, OtherEntity and PLC | [optional] 
**contact_name** | **str** | Contact person at the organisation. | [optional] 
**email** | **str** | Contact email address of the entity | [optional] 
**website** | **str** | Website address of the entity&lt;br&gt; Valid for the profile types Trust, Company, Partnership, OtherEntity and PLC | [optional] 
**telephone** | **str** | Telephone number of the entity.&lt;br&gt; Valid for the profile types Trust, Company, Partnership, OtherEntity and PLC | [optional] 
**turnover** | [**KycProtectPostProfilesRequestDetailsTurnover**](KycProtectPostProfilesRequestDetailsTurnover.md) |  | [optional] 
**assets_under_management** | [**KycProtectPostProfilesRequestDetailsAssetsUnderManagement**](KycProtectPostProfilesRequestDetailsAssetsUnderManagement.md) |  | [optional] 
**organization_number** | **str** | Property valid for profile type - Trust, Company, Partnership, OtherEntity and PLC | [optional] 
**internal_contact** | **str** | Internal contact name to contact regarding this profile,&lt;br&gt; Property valid for profile type - Trust, Company, Partnership, OtherEntity and PLC. | [optional] 
**internal_email** | **str** | Internal email address to contact regarding this profile.&lt;br&gt; Property valid for profile type - Trust, Company, Partnership, OtherEntity and PLC | [optional] 
**date_of_birth** | **date** | Date YYYY-MM-DD or YYYY format. Must be after 1900 and not in the future&lt;br&gt; Valid for the profile types Individual and SoleTrader | [optional] 
**country_code** | **str** | Two-letter country code ISO-3166-2.&lt;br&gt; Valid for the profile types Individual and SoleTrader | [optional] 
**vat_no** | **str** | Tax Identification Number of the business&lt;br&gt; Valid for the profile types Company, Partnership, OtherEntity and PLC | [optional] 
**is_listed_on_exchange** | **bool** | Property valid for profile type PLC | [optional] 
**exchange_name** | **str** | Property valid for profile type PLC | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


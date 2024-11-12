# KYCPostIndividualSearchContract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_codes** | **list[str]** | List of Two-letter country code ISO-3166-2. | [optional] 
**threshold** | **int** | Hits with scores below the chosen value will not be shown. &lt;br&gt; Must be one of 75, 80, 85, 90, 95, or 100 | 
**name** | **str** | Required if FirstName and LastName are not provided | [optional] 
**first_name** | **str** | If firstName is provided then lastName must also be provided | [optional] 
**middle_name** | **str** | middleName is optional, valid along with firstName and lastName only | [optional] 
**last_name** | **str** | If LastName is provided then FirstName must also be provided | [optional] 
**date_of_birth** | **date** | Date YYYY-MM-DD or YYYY format. Must be after 1900 and not in the future. | [optional] 
**gender** | **str** | Define the gender of the individual you are searching for. Available values are male and female. | [optional] 
**pep_tiers** | **list[str]** | When searching the PEP dataset, define what tiers of the PEP profiles should be included in the results.&lt;br&gt; PEP Tier 1 indicates senior roles&lt;br&gt; PEP Tier 2 - middle-ranking&lt;br&gt; PEP Tier 3 - junior officials &lt;br&gt;&lt;br&gt; If the PEP Dataset is NOT included on the list of searched datasets, then this value is ignored. &lt;br&gt;&lt;br&gt;The PEP Tier filter does not apply to PEP-LINKED Profiles.&lt;br&gt; | [optional] 
**datasets** | **list[str]** | Specifies which datasets will be searched &lt;br&gt; PEP - Politically Exposed Persons (All)&lt;br&gt; PEP-CURRENT - Only current PEPs&lt;br&gt; PEP-FORMER - Only former PEPs&lt;br&gt; PEP-LINKED - Only linked PEPs (PEP by Association)&lt;br&gt; SAN - Sanctioned (All)&lt;br&gt; SAN-CURRENT - Only current Sanctions &lt;br&gt; SAN-FORMER - Only former Sanctions&lt;br&gt; INS - Insolvency &lt;br&gt; AM - Averse Media &lt;br&gt; POI - Profile of Interest &lt;br&gt; ENF - Enforcement DD - Disqualified Director | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


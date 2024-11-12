# AddSearchContract

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The entity type of the search. Available values are individual and business. | [optional] 
**name** | **str** | Required if FirstName and LastName are not provided | [optional] 
**first_name** | **str** | If FirstName is provided then LastName must also be provided | [optional] 
**middle_name** | **str** | Middle name is optional, valid along with Firstname and LastName only | [optional] 
**last_name** | **str** | If LastName is provided then FirstName must also be provided | [optional] 
**date_of_birth** | **date** | Date YYYY-MM-DD or YYYY format. Must be after 1900 and not in the future. | [optional] 
**gender** | **str** | Define the gender of the individual you are searching for. | [optional] 
**pep_tiers** | **list[str]** | When searching the PEP dataset, define what tiers of the PEP profiles should be included in the results.&lt;br&gt;&lt;br&gt; PEP Tier 1 indicates senior roles&lt;br&gt; PEP Tier 2 - middle-ranking&lt;br&gt; PEP Tier 3 - junior officials&lt;br&gt;&lt;br&gt; If the PEP Dataset is NOT included on the list of searched datasets, then this value is ignored. The PEP Tier filter does not apply to PEP-LINKED Profiles. | [optional] 
**datasets** | **list[str]** | Specifies which datasets will be searched&lt;br&gt;&lt;br&gt; PEP - Politically Exposed Persons (All)&lt;br&gt; PEP-CURRENT - Only current PEPs&lt;br&gt; PEP-FORMER - Only former PEPs PEP-LINKED - Only linked PEPs (PEP by Association)&lt;br&gt; SAN - Sanctioned (All)&lt;br&gt; SAN-CURRENT - Only current Sanctions&lt;br&gt; SAN-FORMER - Only former Sanctions&lt;br&gt; INS - Insolvency &lt;br&gt; AM - Averse Media&lt;br&gt; POI - Profile of Interest&lt;br&gt; ENF - Enforcement &lt;br&gt; DD - Disqualified Director | [optional] 
**country_codes** | **list[str]** |  | [optional] 
**threshold** | **int** | Must be one of 75, 80, 85, 90, 95, or 100 | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


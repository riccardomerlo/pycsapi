# IndividualSearchResultHitResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Id of the search hit | [optional] 
**hit_score** | **int** | The hit score associated to the search hit. | [optional] 
**name** | **str** | The name associated to the search hit. | [optional] 
**match** | **str** | The match string associated to the search hit. | [optional] 
**note** | **str** | The note added to the search hit. | [optional] 
**countries** | **list[str]** | The countries associated to the search hit. | [optional] 
**datasets** | **list[str]** | The datasets associated to the search hit. | [optional] 
**profile_images** | **list[str]** | The profile images associated to the search hit. | [optional] 
**screening_notes** | **list[str]** | The screening notes associated to the search hit. | [optional] 
**modified_at** | **datetime** | The search hit modified date and time. | [optional] 
**modified_by_id** | **int** | The search hit modified by user id. | [optional] 
**modified_by** | **str** | The search hit modified by user name. | [optional] 
**created_at** | **datetime** | The search hit created date and time. | [optional] 
**decision** | **str** | The decision made on the search hit. | [optional] 
**identifiers** | [**list[SearchResultHitsIdentifierResponse]**](SearchResultHitsIdentifierResponse.md) | The identifiers associated to the search hit. | [optional] 
**addresses** | [**list[SearchResultHitsAddressResponse]**](SearchResultHitsAddressResponse.md) | The addresses associated to the search hit. | [optional] 
**contacts** | [**list[SearchResultHitsContactResponse]**](SearchResultHitsContactResponse.md) | The contact details associated to the search hit. | [optional] 
**business_links** | [**list[SearchResultHitsBusinessLinkResponse]**](SearchResultHitsBusinessLinkResponse.md) | The business links associated to the search hit. | [optional] 
**individual_links** | [**list[SearchResultHitsIndividualLinkResponse]**](SearchResultHitsIndividualLinkResponse.md) | The individual links associated to the search hit. | [optional] 
**sources** | [**list[SearchResultHitsSourceResponse]**](SearchResultHitsSourceResponse.md) | The sources associated to the search hit. | [optional] 
**first_name** | **str** | The first name of the individual search hit. | [optional] 
**middle_name** | **str** | The middle name of the individual search hit. | [optional] 
**last_name** | **str** | The last name of the individual search hit. | [optional] 
**gender** | **str** | The gender associated with the search hit. | [optional] 
**dates_of_birth** | **list[date]** | The dates of birth associated to the search hit. | [optional] 
**is_deceased** | **bool** | The deceased status of the individual associated to the search hit | [optional] 
**dates_of_death** | **list[date]** | The dates of death associated to the search hit. | [optional] 
**pep_tier** | **str** | The pep tier associated to the search hit. | [optional] 
**aliases** | [**list[SearchResultHitsIndividualAliasResponse]**](SearchResultHitsIndividualAliasResponse.md) | The aliases associated to the search hit. | [optional] 
**aml_results** | [**IndividualSearchResultHitResponseAmlResults**](IndividualSearchResultHitResponseAmlResults.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# WebApiModelsSearchesSearchResultHitsBusinessSearchResultHitResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Id of the search hit | [optional] 
**hit_score** | **int** | The hit score associated to the search hit | [optional] 
**name** | **str** | The name associated to the search hit | [optional] 
**match** | **str** | The match string associated to the search hit | [optional] 
**note** | **str** | The note added to the search hit | [optional] 
**countries** | **list[str]** | The countries associated to the search hit | [optional] 
**datasets** | **list[str]** | The datasets associated to the search hit | [optional] 
**profile_images** | **list[str]** | The profile images associated to the search hit | [optional] 
**screening_notes** | **list[str]** | The screening notes associated to the search hit | [optional] 
**modified_at** | **datetime** | The search hit modified date and time | [optional] 
**modified_by_id** | **int** | The search hit modified by user id | [optional] 
**modified_by** | **str** | The search hit modified by user name | [optional] 
**created_at** | **datetime** | The search hit created date and time | [optional] 
**decision** | **str** | The decision made on the search hit Avaialable values are undecided, trueMatch, falsePositive, discarded | [optional] 
**identifiers** | [**list[WebApiModelsSearchesSearchResultHitsHitIdentifierResponse]**](WebApiModelsSearchesSearchResultHitsHitIdentifierResponse.md) | The identifiers associated to the search hit | [optional] 
**addresses** | [**list[WebApiModelsSearchesSearchResultHitsHitAddressResponse]**](WebApiModelsSearchesSearchResultHitsHitAddressResponse.md) | The addresses associated to the search hit | [optional] 
**contacts** | [**list[WebApiModelsSearchesSearchResultHitsHitContactResponse]**](WebApiModelsSearchesSearchResultHitsHitContactResponse.md) | The contact details associated to the search hit | [optional] 
**business_links** | [**list[WebApiModelsSearchesSearchResultHitsHitBusinessLinkResponse]**](WebApiModelsSearchesSearchResultHitsHitBusinessLinkResponse.md) | The business links associated to the search hit | [optional] 
**individual_links** | [**list[WebApiModelsSearchesSearchResultHitsHitIndividualLinkResponse]**](WebApiModelsSearchesSearchResultHitsHitIndividualLinkResponse.md) | The individual links associated to the search hit | [optional] 
**sources** | [**list[WebApiModelsSearchesSearchResultHitsHitSourceResponse]**](WebApiModelsSearchesSearchResultHitsHitSourceResponse.md) | The sources associated to the search hit | [optional] 
**activities** | **list[str]** | The activities associated to the search hit | [optional] 
**aliases** | [**list[WebApiModelsSearchesSearchResultHitsHitBusinessAliasResponse]**](WebApiModelsSearchesSearchResultHitsHitBusinessAliasResponse.md) | The aliases associated to the search hit | [optional] 
**aml_results** | [**WebApiModelsSearchesSearchResultHitsBusinessHitAmlResultsResponse**](WebApiModelsSearchesSearchResultHitsBusinessHitAmlResultsResponse.md) |  | [optional] 
**description** | **str** | The description associated to the search hit | [optional] 
**business_types** | **list[str]** | The business types associated to the search hit | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# InternationalSanctionsDetail

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aliases** | **list[str]** | A list of alternative names or aliases used by the sanctioned individual or entity. | [optional] 
**full_name** | **str** | The full legal name of the sanctioned individual or entity. | [optional] 
**identity_information** | **list[object]** | Additional identity information which may include details like nationality, date of birth, and other identifying particulars. | [optional] 
**addresses** | [**list[InternationalSanctionsDetailAddresses]**](InternationalSanctionsDetailAddresses.md) | Lists the addresses associated with the individual or entity, providing detailed locational information. Each address entry includes city, country, the first line of the address, and the region, all of which contribute to a comprehensive understanding of the sanctioned party&#x27;s location. | [optional] 
**sanction_bodies** | **list[str]** | A list of sanctioning bodies that have imposed sanctions on the individual or entity, indicating the authority or government entity responsible. | [optional] 
**dates** | [**list[InternationalSanctionsDetailDates]**](InternationalSanctionsDetailDates.md) | Contains a list of significant dates related to the sanctions, such as the date of imposition, expiration, or review. Each date is associated with a specific type to clarify its relevance to the sanction details. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


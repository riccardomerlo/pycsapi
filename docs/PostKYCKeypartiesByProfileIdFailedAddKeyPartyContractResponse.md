# PostKYCKeypartiesByProfileIdFailedAddKeyPartyContractResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the key party  Maximum length is 200 characters | [optional] 
**first_name** | **str** | First name of the key party  &lt;br&gt; Valid for only entity type Individual &lt;br&gt; Maximum length is 200 characters combining First name, Middle name and Last name | [optional] 
**middle_name** | **str** | Middle name of the key party  &lt;br&gt; Valid for only entity type Individual &lt;br&gt; Maximum length is 200 characters combining First name, Middle name and Last name | [optional] 
**last_name** | **str** | Last name of the key party  &lt;br&gt; Valid for only entity type Individual &lt;br&gt; Maximum length is 200 characters combining First name, Middle name and Last name | [optional] 
**entity_type** | **str** | Entity type of the key party, individual, business | [optional] 
**key_party_type** | **str** | Type of the key party  &lt;br&gt; Valid Key Party types for entity type Individual are Director, Ubo and ShareHolder &lt;br&gt; Valid Key Party types for entity type Business are Ubo and ShareHolder , director, shareHolder, ubo | [optional] 
**gender** | **str** | Gender of the key party  Valid for entity type Individual, male, female | [optional] 
**date_of_birth** | **date** | Date of birth of the key party  Date YYYY-MM-DD or YYYY format. Must be after 1900 and not in the future  &lt;br&gt; Valid for the entity type Individual  | [optional] 
**organisation_number** | **str** | &lt;br&gt; Key party organisation number   &lt;br&gt; Valid for entity type Business  | [optional] 
**activity_code** | **str** | Activity code of the key party  &lt;br&gt; Valid for entity type Business  | [optional] 
**percentage_of_shares** | **float** | Share percentage of the key party  &lt;br&gt; Valid for key party type ShareHolder  | [optional] 
**role** | **str** | Role of the key party  &lt;br&gt; Valid for key party type Director  | [optional] 
**country_code** | **str** | Country code of the key party | [optional] 
**address** | [**PostKYCKeypartiesByProfileIdAddressRequestContractResponse**](PostKYCKeypartiesByProfileIdAddressRequestContractResponse.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# ConnectIdentityAmlSupplierResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**band_text** | **str** | A descriptive label or category assigned based on the results of the AML checks. Typically, this text will indicate the level of risk or compliance category identified through the verification process. | [optional] 
**birth_index_match** | **bool** | Indicates whether there was a match found in the birth index database, a critical aspect of verifying an individual&#x27;s identity against official records. | [optional] 
**no_retry** | **bool** | A flag to indicate whether the AML process should not be retried for this individual. This can be set to true in scenarios where repeated verification attempts are unlikely to yield different results. | [optional] 
**result_codes** | [**ConnectIdentityAmlSupplierResultResultCodes**](ConnectIdentityAmlSupplierResultResultCodes.md) |  | [optional] 
**score** | **int** | A numerical value representing the calculated risk score or validation level derived from the AML checks. This score can guide decision-making processes regarding the subject&#x27;s verification status. | [optional] 
**search_text** | **str** | The exact query text used in the search, allowing for audit and review of the search parameters and terms used. | [optional] 
**legacy_unique_id** | **str** | A unique identifier from a legacy system that may still be used to track or reference the subject within older datasets or parallel systems. | [optional] 
**validation_id** | **str** | A unique identifier assigned to the validation process, facilitating tracking and cross-referencing of the validation attempts across multiple systems. | [optional] 
**has_alerts** | **bool** | Indicates whether any alerts were triggered during the verification process. This is typically used to flag profiles that require further investigation or immediate attention. | [optional] 
**success** | **bool** | Reflects whether the AML search and verification process was successful, based on the predefined criteria and thresholds set within the system. | [optional] 
**credits_incurred** | **int** | The number of credits or cost units consumed during the AML search process. This is relevant for systems where operations incur a variable cost based on usage or complexity. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


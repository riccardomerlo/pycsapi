# ConnectIdentityAmlSearchResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**correlation_id** | **str** | A unique identifier for the AML search request, used to track and correlate responses with their respective requests. | [optional] 
**unique_id** | **str** | A unique identifier for the result, distinct from the correlation ID, which may be used internally for further processing or reference. | [optional] 
**input** | [**ConnectIdentityAMLSearchRequest**](ConnectIdentityAMLSearchRequest.md) |  | [optional] 
**common** | [**ConnectIdentityCommonResult**](ConnectIdentityCommonResult.md) |  | [optional] 
**aml_result** | [**ConnectIdentityAmlSupplierResult**](ConnectIdentityAmlSupplierResult.md) |  | [optional] 
**errors** | **dict(str, list[str])** | Contains any errors that occurred during the search process, listed as an array of string messages. Each string provides details on specific issues encountered. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


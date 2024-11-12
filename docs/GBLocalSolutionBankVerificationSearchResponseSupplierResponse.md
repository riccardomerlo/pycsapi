# GBLocalSolutionBankVerificationSearchResponseSupplierResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_name** | **str** | Name of the customer returned by the supplier | [optional] 
**bank_account** | **str** | The bank account number returned by the supplier | [optional] 
**sort_code** | **str** | The sort code returned by the supplier | [optional] 
**returned_customer_name** | **str** | A potential name of the customer returned by the supplier when the result is a close match returned by the supplier | [optional] 
**result** | **bool** | Whether the result is a match or not a match returned by the supplier | [optional] 
**result_text** | **str** | A detailed result returned by the supplier, this includes details of a close match | [optional] 
**name_match_result** | **str** | The name match result returned by the supplier. Values are \&quot;No Match\&quot;, \&quot;Full\&quot; or \&quot;Close\&quot; | [optional] 
**account_type_result** | **bool** | The account type match returned by the supplier. When &#x27;nameMatchResult&#x27; is \&quot;Full\&quot; or \&quot;Close\&quot; and this is false then this indicates that the \&quot;accountType\&quot; provided does not match | [optional] 
**reason_code** | **str** | A reason code returned by the supplier | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


# GBLocalSolutionBankVerificationSearchRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_name** | **str** | This field is for the name on the account you are matching against with the bankAccount, sortCode and secondaryReference fields | 
**bank_account** | **str** | Must be numeric and a length of 8 characters | 
**sort_code** | **str** | Must be numeric and a length of 6 characters | 
**account_type** | **str** | field must be either Business or Personal, it can not be blank or any other value | 
**secondary_reference** | **str** | Should not be used unless you have been advised to use this by a bank or building society&lt;br&gt; This field will affect the results data | [optional] 
**customer_reference** | **str** | Field is for text input and does not affect the search result&lt;br&gt; This field can be used for filtering your past results at a later date | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


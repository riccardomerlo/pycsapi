# ConnectIdentityCommonSearchCriteria

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person** | [**ConnectIdentityPerson**](ConnectIdentityPerson.md) |  | [optional] 
**customer_id** | **int** | ID value of a customer account, typically passed in to allow users to retrieve past searches on a customer. | [optional] 
**user_id** | **int** | ID value of the user account, a customer account may have multiple user accounts, this is typically passed in to retrieve past searches by a user. | [optional] 
**reference** | **str** | A string value that a user can submit during their search. This reference value is stored alongside the search details/customer/user ID values. Is typically passed in to allow users to retrieve past searches based on the reference value supplied. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


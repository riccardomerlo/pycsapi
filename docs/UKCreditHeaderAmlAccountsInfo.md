# UKCreditHeaderAmlAccountsInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lender_type** | **str** | Specifies the type of lender (e.g., bank, credit union, mortgage company) associated with the accounts listed. | [optional] 
**accounts** | **int** | The total number of accounts opened with the specified lender. This count includes both active and inactive accounts. | [optional] 
**active_accounts** | **int** | The number of currently active accounts, indicating those that are in use and have not been closed or written off. | [optional] 
**oldest_account_start_date** | **str** | The start date of the oldest account held by the individual with this lender, formatted as YYYY-MM-DD. Provides a timeline of the person&#x27;s credit history. | [optional] 
**youngest_account_start_date** | **str** | The start date of the most recently opened account with this lender, also formatted as YYYY-MM-DD. Indicates how recently the individual has engaged in new credit activities. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


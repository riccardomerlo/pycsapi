# UKCreditHeaderAml

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique identifier for the result entry, used internally for tracking individual results within the system. | [optional] 
**name** | **str** | The name associated with the identity check result, typically representing a label or category for quick reference. | [optional] 
**description** | **str** | A detailed description of the result or status indicated by this entry, providing deeper insight into the verification outcome. | [optional] 
**address** | **str** | The address information as returned or matched in the identity verification process. | [optional] 
**alert** | **str** | Indicates any alerts triggered by the verification process. This might include fraud warnings or other critical flags. | [optional] 
**date_of_birth** | **str** | The date of birth matched or verified against the input data, often used in age or identity confirmation. | [optional] 
**forename** | **str** | The first name as it was matched or verified during the identity check. | [optional] 
**surname** | **str** | The surname as it was matched or verified during the identity check. | [optional] 
**_pass** | **str** | Indicates whether the identity verification passed the set criteria or thresholds, typically as a simple &#x27;pass&#x27; or &#x27;fail&#x27; outcome. | [optional] 
**comments** | [**list[UKEditedVotersDatabaseComments]**](UKEditedVotersDatabaseComments.md) | An array of comments related to the verification process, where each item contains a code and its associated description. These comments are used to provide detailed feedback, notes, or annotations that clarify aspects of the verification findings. | [optional] 
**match** | [**list[UKEditedVotersDatabaseMatch]**](UKEditedVotersDatabaseMatch.md) | An array that captures all successful matches identified during the verification process. Each item in the array includes a code and a detailed description, explaining the matched data and its relevance, which helps in affirming the identity or data accuracy. | [optional] 
**mis_match** | [**list[UKEditedVotersDatabaseMisMatch]**](UKEditedVotersDatabaseMisMatch.md) | An array detailing mismatches or discrepancies encountered during the verification process. Each mismatch is noted with a code and a comprehensive description, which helps in understanding what information was incorrect or did not meet the verification criteria. | [optional] 
**warning** | [**list[UKEditedVotersDatabaseWarning]**](UKEditedVotersDatabaseWarning.md) | Contains warnings that were identified during the verification process. These are not severe enough to be considered alerts but are significant enough to be noted. Each warning is represented by a code and a description that outlines potential concerns or minor issues. | [optional] 
**accounts_info** | [**list[UKCreditHeaderAmlAccountsInfo]**](UKCreditHeaderAmlAccountsInfo.md) | A collection of financial account details, capturing various aspects of a person&#x27;s credit history with different lenders. This array provides insight into the types and statuses of accounts held by an individual. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


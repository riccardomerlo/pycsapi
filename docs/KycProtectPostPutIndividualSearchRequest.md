# KycProtectPostPutIndividualSearchRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_codes** | **list[str]** | Countries provided to the search | [optional] 
**threshold** | **int** | Hits with scores below the chosen value will not be shown.&lt;br&gt; Must be one of 75, 80, 85, 90, 95, or 100 | 
**name** | **str** | Name provided for the search. Length must not exceed 200 characters&lt;br&gt;&lt;br&gt; | [optional] 
**first_name** | **str** | First name provided in the search.  The combination of first name, middle name, and last name must not exceed 200 characters | [optional] 
**middle_name** | **str** | Middle name provided in the search.  The combination of first name, middle name, and last name must not exceed 200 characters | [optional] 
**last_name** | **str** | Last name provided in the search.  The combination of first name, middle name, and last name must not exceed 200 characters | [optional] 
**gender** | **str** | Gender provided in the search | [optional] 
**date_of_birth** | **date** | DOB provided in the search | [optional] 
**pep_tiers** | **list[str]** | Pep Tiers provided in the search | [optional] 
**datasets** | **list[str]** | Provided datasets for the search&lt;br&gt;&lt;br&gt; &#x60;AM&#x60; - Adverse Media&lt;br&gt; &#x60;DD&#x60; - Disqualified Director&lt;br&gt; &#x60;INS&#x60; - Insolvency&lt;br&gt; &#x60;PEP&#x60; - Politically Exposed Persons (All)&lt;br&gt; &#x60;PEP-CURRENT&#x60; - Only Current PEPS&lt;br&gt; &#x60;PEP-FORMER&#x60; - Only Former PEPS&lt;br&gt; &#x60;PEP-LINKED&#x60; - Only linked PEPs (PEP by Association)&lt;br&gt; &#x60;POI&#x60; - Profile of Interest&lt;br&gt; &#x60;ENF&#x60; - Enforcement&lt;br&gt; &#x60;SAN&#x60; - Sanctioned (All)&lt;br&gt; &#x60;SAN-CURRENT&#x60; - Only current Sanctions&lt;br&gt; &#x60;SAN-FORMER&#x60; - Only former Sanctions&lt;br&gt; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


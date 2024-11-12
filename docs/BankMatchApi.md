# pycsapi.BankMatchApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bank_match**](BankMatchApi.md#bank_match) | **GET** /localSolutions/GB/bankmatch | Bank Match

# **bank_match**
> ConnectBankMatchResult bank_match(check_type, company_id, sort_code=sort_code, account_number=account_number, iban=iban, vat_number=vat_number)

Bank Match

The Bank Verification tool allows customers to instantly verify that small and medium sized companies you are working with are providing correct bank details, to reduce fraud and avoid delays in your on boarding process. The bank data for these companies is provided to Creditsafe by various financial providers, including major banks. When you provide us with a company number and their bank details, we are able to perform instant checks to verify that those bank details are associated with that company and return - </br> Match – We have bank information on the company, and the data provided by the customer matches the company records </br> No Match – We have bank information on the company, but the data provided does not match any of the company records </br> Data Unavailable - We do not have bank information on the company.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.BankMatchApi(pycsapi.ApiClient(configuration))
check_type = 'check_type_example' # str | Validation uses an algorithm to determine if a SCAN or IBAN exists, but does not let you know if that SCAN or IBAN actually belongs to the company who has provided it. Verification takes this a step further and checks the Creditsafe database for a match on the SCAN/IBAN, and tells you if the bank details actually belong to the company, so you can be assured that you are sending your money to the correct entity.
company_id = 'company_id_example' # str | The connectId or safeNumber of the company to check against.
sort_code = 'sort_code_example' # str | Sort Code to check - Must be passed in with Account Number to form a SCAN Result (optional)
account_number = 'account_number_example' # str | Account Number to check - Must be passed in with Sort Code to form a SCAN Result (optional)
iban = 'iban_example' # str | IBAN to check (optional)
vat_number = 'vat_number_example' # str | VAT Number to check (optional)

try:
    # Bank Match
    api_response = api_instance.bank_match(check_type, company_id, sort_code=sort_code, account_number=account_number, iban=iban, vat_number=vat_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankMatchApi->bank_match: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **check_type** | [**str**](.md)| Validation uses an algorithm to determine if a SCAN or IBAN exists, but does not let you know if that SCAN or IBAN actually belongs to the company who has provided it. Verification takes this a step further and checks the Creditsafe database for a match on the SCAN/IBAN, and tells you if the bank details actually belong to the company, so you can be assured that you are sending your money to the correct entity. | 
 **company_id** | **str**| The connectId or safeNumber of the company to check against. | 
 **sort_code** | **str**| Sort Code to check - Must be passed in with Account Number to form a SCAN Result | [optional] 
 **account_number** | **str**| Account Number to check - Must be passed in with Sort Code to form a SCAN Result | [optional] 
 **iban** | **str**| IBAN to check | [optional] 
 **vat_number** | **str**| VAT Number to check | [optional] 

### Return type

[**ConnectBankMatchResult**](ConnectBankMatchResult.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# pycsapi.FRBankMatchApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fr_bankmatch**](FRBankMatchApi.md#fr_bankmatch) | **GET** /localSolutions/FR/bankmatch | Bank Match
[**fr_bankmatch_status**](FRBankMatchApi.md#fr_bankmatch_status) | **GET** /localSolutions/FR/bankmatch/audition | Bank Match Status

# **fr_bankmatch**
> LocalSolutionsFRBankMatch fr_bankmatch(registration_id, country_code, iban, bban=bban, bic=bic, routing_code=routing_code)

Bank Match

This endpoint can be used to check the reliability of a company/bank details combination,  and ensure that the IBAN is not linked to a risk of fraud. <br><br>  **NOTE** - There are a set of 'required' parameters for this endpoint, however please note the exceptions in the `countryCode` description. 

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.FRBankMatchApi(pycsapi.ApiClient(configuration))
registration_id = 'registration_id_example' # str | registrationId of company
country_code = 'country_code_example' # str | Country codes in iso-2 format <br>  The following counties do **NOT** support the `iban` parameter - <br> `AU`, `CA`,`CN`, `HK`, `IN`,`JP`,`KR`,`MX`, `MY`, `SG`, `US`, `ZA`<br><br> Please see the following link for required parameters on these countries: <br>   <a href=\"https://help.creditsafeuk.com/a/solutions/articles/7000088525?lang=en&portalId=7000000824\" target=\"_blank\">Unsupported Country parameter requirements</a> 
iban = 'iban_example' # str | Bank Account details in IBAN format
bban = 'bban_example' # str | Bank Account Number for countries where IBAN format doesn't support (optional)
bic = 'bic_example' # str | Business/Bank Identifier Code to identify the bank/branch holding the account along with BBAN (optional)
routing_code = 'routing_code_example' # str | Routing Code to identify the bank/branch holding the account along with BBAN (optional)

try:
    # Bank Match
    api_response = api_instance.fr_bankmatch(registration_id, country_code, iban, bban=bban, bic=bic, routing_code=routing_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FRBankMatchApi->fr_bankmatch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registration_id** | **str**| registrationId of company | 
 **country_code** | **str**| Country codes in iso-2 format &lt;br&gt;  The following counties do **NOT** support the &#x60;iban&#x60; parameter - &lt;br&gt; &#x60;AU&#x60;, &#x60;CA&#x60;,&#x60;CN&#x60;, &#x60;HK&#x60;, &#x60;IN&#x60;,&#x60;JP&#x60;,&#x60;KR&#x60;,&#x60;MX&#x60;, &#x60;MY&#x60;, &#x60;SG&#x60;, &#x60;US&#x60;, &#x60;ZA&#x60;&lt;br&gt;&lt;br&gt; Please see the following link for required parameters on these countries: &lt;br&gt;   &lt;a href&#x3D;\&quot;https://help.creditsafeuk.com/a/solutions/articles/7000088525?lang&#x3D;en&amp;portalId&#x3D;7000000824\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Unsupported Country parameter requirements&lt;/a&gt;  | 
 **iban** | **str**| Bank Account details in IBAN format | 
 **bban** | **str**| Bank Account Number for countries where IBAN format doesn&#x27;t support | [optional] 
 **bic** | **str**| Business/Bank Identifier Code to identify the bank/branch holding the account along with BBAN | [optional] 
 **routing_code** | **str**| Routing Code to identify the bank/branch holding the account along with BBAN | [optional] 

### Return type

[**LocalSolutionsFRBankMatch**](LocalSolutionsFRBankMatch.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fr_bankmatch_status**
> LocalSolutionsFRBankMatch fr_bankmatch_status(audition_id)

Bank Match Status

This endpoint is used to check the status of a verification whose status is ‘pending’.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.FRBankMatchApi(pycsapi.ApiClient(configuration))
audition_id = 'audition_id_example' # str | identifier to check status

try:
    # Bank Match Status
    api_response = api_instance.fr_bankmatch_status(audition_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FRBankMatchApi->fr_bankmatch_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audition_id** | **str**| identifier to check status | 

### Return type

[**LocalSolutionsFRBankMatch**](LocalSolutionsFRBankMatch.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


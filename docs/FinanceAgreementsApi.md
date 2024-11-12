# pycsapi.FinanceAgreementsApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**finance_agreements**](FinanceAgreementsApi.md#finance_agreements) | **GET** /localSolutions/GB/CCDS/{companyId} | Finance Agreements

# **finance_agreements**
> InlineResponse2009 finance_agreements(company_id)

Finance Agreements

This tool provides a detailed view of data supplied via the CCDS scheme(Commercial Credit Data Sharing ). It's tailored for users needing immediate access to current and accurate financial agreement information, enhancing decision-making with up-to-date data insights.<br><br> **1. Full CCDS Access** - Gain in-depth insights with access to up to 48 months of historical data on current accounts, loans, and credit card facilities. This tool is perfect for comprehensive long-term financial analysis, offering a thorough understanding of credit history and trends.<br><br> **2. Financial Footprint** - Get a summarized view of non performance related credit activity data. This tool simplifies the complex data into an easily understandable summary, ideal for quick assessments and initial screenings.<br><br> **3. Finance Performance Indicator** - A predictive tool that evaluates the likelihood of a company defaulting on payments within the next 90 days. This tool is crucial for risk assessment and mitigation, offering foresight and preparation for potential financial challenges.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.FinanceAgreementsApi(pycsapi.ApiClient(configuration))
company_id = 'company_id_example' # str | The connectId or safeNumber of the company

try:
    # Finance Agreements
    api_response = api_instance.finance_agreements(company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FinanceAgreementsApi->finance_agreements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| The connectId or safeNumber of the company | 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


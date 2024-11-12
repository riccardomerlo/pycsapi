# pycsapi.CompaniesApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**company_credit_report**](CompaniesApi.md#company_credit_report) | **GET** /companies/{connectId} | Company Credit Report
[**company_search**](CompaniesApi.md#company_search) | **GET** /companies | Company Search
[**company_search_criteria**](CompaniesApi.md#company_search_criteria) | **GET** /companies/searchcriteria | Company Search Criteria
[**confidence_match_search**](CompaniesApi.md#confidence_match_search) | **GET** /companies/match | Confidence Match Search

# **company_credit_report**
> CreditsafeGlobalDataReportsCompanyReportResponse company_credit_report(connect_id, accept=accept, language=language, template=template, include_indicators=include_indicators, custom_data=custom_data, call_ref=call_ref)

Company Credit Report

Orders a Company Credit Report by connectId.<br><br> To acquire a PDF version of the report use the optional request in 'Header'.<br><br> This request will provide a 'Base64-encoded' script to convert to a PDF, this will appear at the end of the JSON response.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.CompaniesApi(pycsapi.ApiClient(configuration))
connect_id = 'connect_id_example' # str | The connectId (optionally Safe Number where available) of the Company required to order their Credit Report. Obtained from `/companies` search results.
accept = 'accept_example' # str | Applies request for PDF link to Company Report. (optional)
language = 'en' # str | Report Language - The JSON structure of the Report is language invariant, but field content will return as the given language, where available. (optional) (default to en)
template = 'full' # str | Optional parameter to request a Templated Company Report. A Template adds/reduces sections of the Credit Report depending on your subscription. Do not include this parameter if you have not been given a template to use.<br> <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000063360-connect-report-templates-glossary-availability\" target=\"_blank\"> Connect Report Templates </a> (optional) (default to full)
include_indicators = false # bool | Optional parameter to include the indicator scores in to a company report -`fsi = Financial Strength` , `pbi = Payment Behaviour Indicator`, `eti = Estimated Turnover`, `pei = Payment Expectation Indicator`<br><br> Addition information on indicator acronyms can be found <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000084411-connect-report-indicator-definitions\" target=\"_blank\">HERE.</a><br><br> Addition information on understanding indicators can be found <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000078780-what-are-indicators-in-the-scores-and-indicators-tab-\" target=\"_blank\">HERE.</a> (optional) (default to false)
custom_data = 'custom_data_example' # str | Additional Report Parameters e.g.  German Report Reason Code value is `de_reason_code::1` . Use /reportcustomdata/{country} endpoint to see all values. (optional)
call_ref = 'call_ref_example' # str | This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions. (optional)

try:
    # Company Credit Report
    api_response = api_instance.company_credit_report(connect_id, accept=accept, language=language, template=template, include_indicators=include_indicators, custom_data=custom_data, call_ref=call_ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->company_credit_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connect_id** | **str**| The connectId (optionally Safe Number where available) of the Company required to order their Credit Report. Obtained from &#x60;/companies&#x60; search results. | 
 **accept** | **str**| Applies request for PDF link to Company Report. | [optional] 
 **language** | **str**| Report Language - The JSON structure of the Report is language invariant, but field content will return as the given language, where available. | [optional] [default to en]
 **template** | **str**| Optional parameter to request a Templated Company Report. A Template adds/reduces sections of the Credit Report depending on your subscription. Do not include this parameter if you have not been given a template to use.&lt;br&gt; &lt;a href&#x3D;\&quot;https://help.creditsafeuk.com/en/support/solutions/articles/7000063360-connect-report-templates-glossary-availability\&quot; target&#x3D;\&quot;_blank\&quot;&gt; Connect Report Templates &lt;/a&gt; | [optional] [default to full]
 **include_indicators** | **bool**| Optional parameter to include the indicator scores in to a company report -&#x60;fsi &#x3D; Financial Strength&#x60; , &#x60;pbi &#x3D; Payment Behaviour Indicator&#x60;, &#x60;eti &#x3D; Estimated Turnover&#x60;, &#x60;pei &#x3D; Payment Expectation Indicator&#x60;&lt;br&gt;&lt;br&gt; Addition information on indicator acronyms can be found &lt;a href&#x3D;\&quot;https://help.creditsafeuk.com/en/support/solutions/articles/7000084411-connect-report-indicator-definitions\&quot; target&#x3D;\&quot;_blank\&quot;&gt;HERE.&lt;/a&gt;&lt;br&gt;&lt;br&gt; Addition information on understanding indicators can be found &lt;a href&#x3D;\&quot;https://help.creditsafeuk.com/en/support/solutions/articles/7000078780-what-are-indicators-in-the-scores-and-indicators-tab-\&quot; target&#x3D;\&quot;_blank\&quot;&gt;HERE.&lt;/a&gt; | [optional] [default to false]
 **custom_data** | **str**| Additional Report Parameters e.g.  German Report Reason Code value is &#x60;de_reason_code::1&#x60; . Use /reportcustomdata/{country} endpoint to see all values. | [optional] 
 **call_ref** | **str**| This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions. | [optional] 

### Return type

[**CreditsafeGlobalDataReportsCompanyReportResponse**](CreditsafeGlobalDataReportsCompanyReportResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/json+pdf

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_search**
> InlineResponse200 company_search(countries, page=page, page_size=page_size, language=language, id=id, safe_no=safe_no, reg_no=reg_no, vat_no=vat_no, name=name, trade_name=trade_name, acronym=acronym, exact=exact, address=address, street=street, house_no=house_no, city=city, post_code=post_code, province=province, call_ref=call_ref, office_type=office_type, phone_no=phone_no, status=status, type=type, website=website, custom_data=custom_data)

Company Search

Endpoint to search for Companies according to the provided Search Criteria. To get the most relevant results, it is recommended to use a unique identifier such as `regNo` where available. If a unique identifier is not available, use a combination of the companies registered `postCode` and `name` for the next best hit rate.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.CompaniesApi(pycsapi.ApiClient(configuration))
countries = pycsapi.CreditsafeGlobalDataCountryCode() # CreditsafeGlobalDataCountryCode | comma-separated list of iso-2 country codes.<br>The code `PLC` can be used here to search for companies of this type across all countries.
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 56 # int | Number of items to return per Page. (optional)
language = 'language_example' # str | Only used for Countries where more than one Company Name exists for different languages e.g.  Japanese Kanji and English.<br>Country -  Languages Available<br>Japan [JP] - EN & JA  (optional)
id = 'id_example' # str | connectId - The primary Company identifier that is used to uniquely identify all companies across Creditsafe's Universe and Partner Network. This is returned on all Company Search Results. Use this field to use in other operations such as Ordering Company Credit Report by Id, and Adding Company to Monitoring Portfolio. (optional)
safe_no = 'safe_no_example' # str | Safe Number - Identifier for Companies in Creditsafe's Home Countries. (optional)
reg_no = 'reg_no_example' # str | Local Company Identifier - The Company identifier associated with it's Domestic Filing Agency. i.e. French SIREN/SIRET, United Kingdom Companies House CRN. (optional)
vat_no = 'vat_no_example' # str | Company VAT Number (optional)
name = 'name_example' # str | Company Name (optional)
trade_name = 'trade_name_example' # str | Trade Name of the Company, typically used in Countries where Name is not uniquely registered. (optional)
acronym = 'acronym_example' # str | A (non-unique) identifier to look for Companies by their more commonly known acronym rather than their lesser known full name. Acronym is predominantly available on French Companies. (optional)
exact = true # bool | Provide as `true` to find Companies matching a Name exactly.<br>A list of countries this is available at <a href=\"https://help.creditsafeuk.com/en/support/solutions/articles/7000083702-company-search-exact-parameter-availability\" target=\"_blank\">Here. (optional)
address = 'address_example' # str |  (optional)
street = 'street_example' # str | Address part identifier - Street of the Company (optional)
house_no = 'house_no_example' # str | Address part identifier - House/Building Number of the Company (optional)
city = 'city_example' # str | Address part identifier - City of the Company (optional)
post_code = 'post_code_example' # str | Address part identifier - Postcode/Zip Code of the Company. Can be provided partially to extend to a region with a * as a wildcard. I.e. CF* can represent all postcodes starting with CF. (optional)
province = 'province_example' # str | Address part identifier - Province/State of the Company (optional)
call_ref = 'call_ref_example' # str | This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions. (optional)
office_type = pycsapi.CreditsafeGlobalDataOfficeType() # CreditsafeGlobalDataOfficeType |  (optional)
phone_no = ['phone_no_example'] # list[str] | Provides Array of phone numbers or Null (optional)
status = pycsapi.CreditsafeGlobalDataCompanyStatus() # CreditsafeGlobalDataCompanyStatus |  (optional)
type = pycsapi.CreditsafeGlobalDataCompanyType() # CreditsafeGlobalDataCompanyType |  (optional)
website = 'website_example' # str |  (optional)
custom_data = 'custom_data_example' # str | Not currently used. (optional)

try:
    # Company Search
    api_response = api_instance.company_search(countries, page=page, page_size=page_size, language=language, id=id, safe_no=safe_no, reg_no=reg_no, vat_no=vat_no, name=name, trade_name=trade_name, acronym=acronym, exact=exact, address=address, street=street, house_no=house_no, city=city, post_code=post_code, province=province, call_ref=call_ref, office_type=office_type, phone_no=phone_no, status=status, type=type, website=website, custom_data=custom_data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->company_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countries** | [**CreditsafeGlobalDataCountryCode**](.md)| comma-separated list of iso-2 country codes.&lt;br&gt;The code &#x60;PLC&#x60; can be used here to search for companies of this type across all countries. | 
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Number of items to return per Page. | [optional] 
 **language** | **str**| Only used for Countries where more than one Company Name exists for different languages e.g.  Japanese Kanji and English.&lt;br&gt;Country -  Languages Available&lt;br&gt;Japan [JP] - EN &amp; JA  | [optional] 
 **id** | **str**| connectId - The primary Company identifier that is used to uniquely identify all companies across Creditsafe&#x27;s Universe and Partner Network. This is returned on all Company Search Results. Use this field to use in other operations such as Ordering Company Credit Report by Id, and Adding Company to Monitoring Portfolio. | [optional] 
 **safe_no** | **str**| Safe Number - Identifier for Companies in Creditsafe&#x27;s Home Countries. | [optional] 
 **reg_no** | **str**| Local Company Identifier - The Company identifier associated with it&#x27;s Domestic Filing Agency. i.e. French SIREN/SIRET, United Kingdom Companies House CRN. | [optional] 
 **vat_no** | **str**| Company VAT Number | [optional] 
 **name** | **str**| Company Name | [optional] 
 **trade_name** | **str**| Trade Name of the Company, typically used in Countries where Name is not uniquely registered. | [optional] 
 **acronym** | **str**| A (non-unique) identifier to look for Companies by their more commonly known acronym rather than their lesser known full name. Acronym is predominantly available on French Companies. | [optional] 
 **exact** | **bool**| Provide as &#x60;true&#x60; to find Companies matching a Name exactly.&lt;br&gt;A list of countries this is available at &lt;a href&#x3D;\&quot;https://help.creditsafeuk.com/en/support/solutions/articles/7000083702-company-search-exact-parameter-availability\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Here. | [optional] 
 **address** | **str**|  | [optional] 
 **street** | **str**| Address part identifier - Street of the Company | [optional] 
 **house_no** | **str**| Address part identifier - House/Building Number of the Company | [optional] 
 **city** | **str**| Address part identifier - City of the Company | [optional] 
 **post_code** | **str**| Address part identifier - Postcode/Zip Code of the Company. Can be provided partially to extend to a region with a * as a wildcard. I.e. CF* can represent all postcodes starting with CF. | [optional] 
 **province** | **str**| Address part identifier - Province/State of the Company | [optional] 
 **call_ref** | **str**| This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions. | [optional] 
 **office_type** | [**CreditsafeGlobalDataOfficeType**](.md)|  | [optional] 
 **phone_no** | [**list[str]**](str.md)| Provides Array of phone numbers or Null | [optional] 
 **status** | [**CreditsafeGlobalDataCompanyStatus**](.md)|  | [optional] 
 **type** | [**CreditsafeGlobalDataCompanyType**](.md)|  | [optional] 
 **website** | **str**|  | [optional] 
 **custom_data** | **str**| Not currently used. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_search_criteria**
> CreditsafeGlobalDataSearchCriteriaSchemaCountry company_search_criteria(countries)

Company Search Criteria

Returns the set of available Company Search parameters/fields for a provided list of countries.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.CompaniesApi(pycsapi.ApiClient(configuration))
countries = 'countries_example' # str | A comma separated list of ISO/Alpha 2 format country codes, or singular country Code. e.g. US,GB will return the common searchable Company fields in the United States and Great Britain.

try:
    # Company Search Criteria
    api_response = api_instance.company_search_criteria(countries)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->company_search_criteria: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countries** | **str**| A comma separated list of ISO/Alpha 2 format country codes, or singular country Code. e.g. US,GB will return the common searchable Company fields in the United States and Great Britain. | 

### Return type

[**CreditsafeGlobalDataSearchCriteriaSchemaCountry**](CreditsafeGlobalDataSearchCriteriaSchemaCountry.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confidence_match_search**
> InlineResponse2001 confidence_match_search(country, match_threshold, reg_no=reg_no, vat_no=vat_no, name=name, street=street, house_no=house_no, city=city, post_code=post_code, province=province, state=state, phone_no=phone_no, reference1=reference1, reference2=reference2, reference3=reference3, call_ref=call_ref)

Confidence Match Search

Supply all company search criteria to find potential company matches ranked by a `single score`.   - <a href=\"https://creditsafe.freshdesk.com/en/support/solutions/articles/7000059769-interpreting-confidence-match-scores\" target=\"_blank\">See here for more information</a>.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.CompaniesApi(pycsapi.ApiClient(configuration))
country = 'country_example' # str | Iso-2 country code
match_threshold = 56 # int | There are 3 main score bands to use for a successful response.<br> - Use score `898` for a 'good' match on 'name'.<br> - Use score `899` for a 'good' match on 'name' and 'ok' response on an address component.<br> - Use scores between `900 - 999` for use on the other searches adjusting for level of 'match' response.
reg_no = 'reg_no_example' # str | Local Company Identifier - The Company identifier associated with it's Domestic Filing Agency. i.e. French SIREN/SIRET, United Kingdom Companies House CRN. (optional)
vat_no = 'vat_no_example' # str | Company VAT Number (optional)
name = 'name_example' # str | Company Name (optional)
street = 'street_example' # str | Address part identifier - Street of the Company (optional)
house_no = 'house_no_example' # str | Address part identifier - House/Building Number of the Company (optional)
city = 'city_example' # str | Address part identifier - City of the Company (optional)
post_code = 'post_code_example' # str | Address part identifier - Postcode/Zip Code of the Company. (optional)
province = 'province_example' # str | Address part identifier - Province of the Company (optional)
state = 'state_example' # str | Address part identifier - State of the Company (optional)
phone_no = 'phone_no_example' # str |  (optional)
reference1 = 'reference1_example' # str | Customer supplied free text reference 1 of 3 (optional)
reference2 = 'reference2_example' # str | Customer supplied free text reference 2 of 3 (optional)
reference3 = 'reference3_example' # str | Customer supplied free text reference 3 of 3 (optional)
call_ref = 'call_ref_example' # str | This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions. (optional)

try:
    # Confidence Match Search
    api_response = api_instance.confidence_match_search(country, match_threshold, reg_no=reg_no, vat_no=vat_no, name=name, street=street, house_no=house_no, city=city, post_code=post_code, province=province, state=state, phone_no=phone_no, reference1=reference1, reference2=reference2, reference3=reference3, call_ref=call_ref)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompaniesApi->confidence_match_search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country** | **str**| Iso-2 country code | 
 **match_threshold** | **int**| There are 3 main score bands to use for a successful response.&lt;br&gt; - Use score &#x60;898&#x60; for a &#x27;good&#x27; match on &#x27;name&#x27;.&lt;br&gt; - Use score &#x60;899&#x60; for a &#x27;good&#x27; match on &#x27;name&#x27; and &#x27;ok&#x27; response on an address component.&lt;br&gt; - Use scores between &#x60;900 - 999&#x60; for use on the other searches adjusting for level of &#x27;match&#x27; response. | 
 **reg_no** | **str**| Local Company Identifier - The Company identifier associated with it&#x27;s Domestic Filing Agency. i.e. French SIREN/SIRET, United Kingdom Companies House CRN. | [optional] 
 **vat_no** | **str**| Company VAT Number | [optional] 
 **name** | **str**| Company Name | [optional] 
 **street** | **str**| Address part identifier - Street of the Company | [optional] 
 **house_no** | **str**| Address part identifier - House/Building Number of the Company | [optional] 
 **city** | **str**| Address part identifier - City of the Company | [optional] 
 **post_code** | **str**| Address part identifier - Postcode/Zip Code of the Company. | [optional] 
 **province** | **str**| Address part identifier - Province of the Company | [optional] 
 **state** | **str**| Address part identifier - State of the Company | [optional] 
 **phone_no** | **str**|  | [optional] 
 **reference1** | **str**| Customer supplied free text reference 1 of 3 | [optional] 
 **reference2** | **str**| Customer supplied free text reference 2 of 3 | [optional] 
 **reference3** | **str**| Customer supplied free text reference 3 of 3 | [optional] 
 **call_ref** | **str**| This parameter allows users to assign a unique identifier to their API queries. By using a callRef, it facilitates easier tracking and logging within Connect. If you provide a callRef, the Connect team can later retrieve and identify the specific requests associated with that identifier, enabling detailed tracing of interactions. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


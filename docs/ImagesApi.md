# pycsapi.ImagesApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**company_image**](ImagesApi.md#company_image) | **GET** /images/{imageId} | Company Image
[**company_image_documents**](ImagesApi.md#company_image_documents) | **GET** /images/companies | Company Image Documents
[**image_document_category_types**](ImagesApi.md#image_document_category_types) | **GET** /images/companies/types | Image Document Category Types

# **company_image**
> CreditsafeGlobalDataCoreAttachmentBinaryAttachment company_image(image_id)

Company Image

Endpoint to order an Image Document by Image ID.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ImagesApi(pycsapi.ApiClient(configuration))
image_id = 'image_id_example' # str | Image ID retrieved from `images/companies`

try:
    # Company Image
    api_response = api_instance.company_image(image_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->company_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| Image ID retrieved from &#x60;images/companies&#x60; | 

### Return type

[**CreditsafeGlobalDataCoreAttachmentBinaryAttachment**](CreditsafeGlobalDataCoreAttachmentBinaryAttachment.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_image_documents**
> ConnectImagesCompanyImages company_image_documents(page=page, page_size=page_size, id=id)

Company Image Documents

Returns the available Images for a given Company connectId.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ImagesApi(pycsapi.ApiClient(configuration))
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 56 # int | Number of items to return per Page. (optional)
id = 'id_example' # str | The company's connectId. (optional)

try:
    # Company Image Documents
    api_response = api_instance.company_image_documents(page=page, page_size=page_size, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->company_image_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Number of items to return per Page. | [optional] 
 **id** | **str**| The company&#x27;s connectId. | [optional] 

### Return type

[**ConnectImagesCompanyImages**](ConnectImagesCompanyImages.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_document_category_types**
> ConnectImagesCompanyImageTypes image_document_category_types(countries=countries)

Image Document Category Types

Lists available Image Document formats, types and languages per country.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.ImagesApi(pycsapi.ApiClient(configuration))
countries = 'countries_example' # str | Filter Images by country. (optional)

try:
    # Image Document Category Types
    api_response = api_instance.image_document_category_types(countries=countries)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ImagesApi->image_document_category_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **countries** | **str**| Filter Images by country. | [optional] 

### Return type

[**ConnectImagesCompanyImageTypes**](ConnectImagesCompanyImageTypes.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


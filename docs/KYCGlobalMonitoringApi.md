# pycsapi.KYCGlobalMonitoringApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compliance_delete_kyc_monitoring_profiles**](KYCGlobalMonitoringApi.md#compliance_delete_kyc_monitoring_profiles) | **DELETE** /compliance/kyc-protect/kycMonitoring/profiles | Delete Profiles From Monitoring
[**compliance_post_kyc_monitoring_profiles_bulk**](KYCGlobalMonitoringApi.md#compliance_post_kyc_monitoring_profiles_bulk) | **POST** /compliance/kyc-protect/kycMonitoring/profiles/bulk | Add Profiles To Monitoring
[**compliance_protect_get_lookup_monitoring_country_codes**](KYCGlobalMonitoringApi.md#compliance_protect_get_lookup_monitoring_country_codes) | **GET** /compliance/kyc-protect/lookup/kycMonitoring/countryCodes | Returns Available Country Codes
[**compliancegetkycmonitoringindividualprofilealertsbyalertid**](KYCGlobalMonitoringApi.md#compliancegetkycmonitoringindividualprofilealertsbyalertid) | **GET** /compliance/kyc-protect/kycMonitoring/profiles/{profileId}/alerts/{alertId} | Return Alert By Alert Id And ProfileId
[**compliancegetkycmonitoringprofilealertsbyprofileid**](KYCGlobalMonitoringApi.md#compliancegetkycmonitoringprofilealertsbyprofileid) | **GET** /compliance/kyc-protect/kycMonitoring/profiles/{profileId}/alerts | Return List Of Alerts By Profile
[**complianceputkycmonitoringindividualprofilealertsbyalertid**](KYCGlobalMonitoringApi.md#complianceputkycmonitoringindividualprofilealertsbyalertid) | **PUT** /compliance/kyc-protect/kycMonitoring/profiles/{profileId}/alerts/{alertId} | Update Status of Alert By Profile Id And Alert Id

# **compliance_delete_kyc_monitoring_profiles**
> DeleteKYCMonitoringProfilesResponse compliance_delete_kyc_monitoring_profiles(body=body)

Delete Profiles From Monitoring

Removes list of profiles from kyc monitoring

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCGlobalMonitoringApi(pycsapi.ApiClient(configuration))
body = pycsapi.DeleteKYCMonitoringProfilesResquest() # DeleteKYCMonitoringProfilesResquest |  (optional)

try:
    # Delete Profiles From Monitoring
    api_response = api_instance.compliance_delete_kyc_monitoring_profiles(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCGlobalMonitoringApi->compliance_delete_kyc_monitoring_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteKYCMonitoringProfilesResquest**](DeleteKYCMonitoringProfilesResquest.md)|  | [optional] 

### Return type

[**DeleteKYCMonitoringProfilesResponse**](DeleteKYCMonitoringProfilesResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliance_post_kyc_monitoring_profiles_bulk**
> PostKYCMonitoringProfilesBulkResponse compliance_post_kyc_monitoring_profiles_bulk(body=body)

Add Profiles To Monitoring

Adds a list of profile/s to monitoring.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCGlobalMonitoringApi(pycsapi.ApiClient(configuration))
body = pycsapi.PostKYCMonitoringProfilesBulkResquest() # PostKYCMonitoringProfilesBulkResquest |  (optional)

try:
    # Add Profiles To Monitoring
    api_response = api_instance.compliance_post_kyc_monitoring_profiles_bulk(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCGlobalMonitoringApi->compliance_post_kyc_monitoring_profiles_bulk: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PostKYCMonitoringProfilesBulkResquest**](PostKYCMonitoringProfilesBulkResquest.md)|  | [optional] 

### Return type

[**PostKYCMonitoringProfilesBulkResponse**](PostKYCMonitoringProfilesBulkResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliance_protect_get_lookup_monitoring_country_codes**
> list[str] compliance_protect_get_lookup_monitoring_country_codes()

Returns Available Country Codes

Gets the list of acceptable country codes for kyc monitoring.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCGlobalMonitoringApi(pycsapi.ApiClient(configuration))

try:
    # Returns Available Country Codes
    api_response = api_instance.compliance_protect_get_lookup_monitoring_country_codes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCGlobalMonitoringApi->compliance_protect_get_lookup_monitoring_country_codes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliancegetkycmonitoringindividualprofilealertsbyalertid**
> KycMonitoringKycAlertResponse compliancegetkycmonitoringindividualprofilealertsbyalertid(profile_id, alert_id)

Return Alert By Alert Id And ProfileId

Gets a kyc alert associated with a given profile.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCGlobalMonitoringApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile
alert_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the kyc alert

try:
    # Return Alert By Alert Id And ProfileId
    api_response = api_instance.compliancegetkycmonitoringindividualprofilealertsbyalertid(profile_id, alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCGlobalMonitoringApi->compliancegetkycmonitoringindividualprofilealertsbyalertid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| id of the profile | 
 **alert_id** | [**str**](.md)| id of the kyc alert | 

### Return type

[**KycMonitoringKycAlertResponse**](KycMonitoringKycAlertResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compliancegetkycmonitoringprofilealertsbyprofileid**
> InlineResponse20016 compliancegetkycmonitoringprofilealertsbyprofileid(profile_id, page=page, page_size=page_size, statuses=statuses)

Return List Of Alerts By Profile

Gets a list of kyc alerts by profile.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCGlobalMonitoringApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile
page = 1 # int | Starting page number. (optional) (default to 1)
page_size = 10 # int | Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. (optional) (default to 10)
statuses = ['statuses_example'] # list[str] | Statuses of kyc alert to filter. Allowed values are Open, ClosedProcessed and ClosedUnprocessed (optional)

try:
    # Return List Of Alerts By Profile
    api_response = api_instance.compliancegetkycmonitoringprofilealertsbyprofileid(profile_id, page=page, page_size=page_size, statuses=statuses)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCGlobalMonitoringApi->compliancegetkycmonitoringprofilealertsbyprofileid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| id of the profile | 
 **page** | **int**| Starting page number. | [optional] [default to 1]
 **page_size** | **int**| Specifies the number of items to be displayed per page. Allowed values are between 1 and 100. | [optional] [default to 10]
 **statuses** | [**list[str]**](str.md)| Statuses of kyc alert to filter. Allowed values are Open, ClosedProcessed and ClosedUnprocessed | [optional] 

### Return type

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complianceputkycmonitoringindividualprofilealertsbyalertid**
> KycMonitoringKycAlertResponse complianceputkycmonitoringindividualprofilealertsbyalertid(profile_id, alert_id, body=body)

Update Status of Alert By Profile Id And Alert Id

Updates a kyc alert associated with a given profile

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.KYCGlobalMonitoringApi(pycsapi.ApiClient(configuration))
profile_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the profile
alert_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | id of the kyc alert
body = pycsapi.UpdateKycAlertContract() # UpdateKycAlertContract |  (optional)

try:
    # Update Status of Alert By Profile Id And Alert Id
    api_response = api_instance.complianceputkycmonitoringindividualprofilealertsbyalertid(profile_id, alert_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KYCGlobalMonitoringApi->complianceputkycmonitoringindividualprofilealertsbyalertid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | [**str**](.md)| id of the profile | 
 **alert_id** | [**str**](.md)| id of the kyc alert | 
 **body** | [**UpdateKycAlertContract**](UpdateKycAlertContract.md)|  | [optional] 

### Return type

[**KycMonitoringKycAlertResponse**](KycMonitoringKycAlertResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


# pycsapi.GMEventRulesAndNotificationsApi

All URIs are relative to *https://connect.creditsafe.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**all_event_rules**](GMEventRulesAndNotificationsApi.md#all_event_rules) | **GET** /monitoring/eventRules | All EventRules
[**all_notification_events**](GMEventRulesAndNotificationsApi.md#all_notification_events) | **GET** /monitoring/notificationEvents | All Notification Events
[**filtered_event_rules**](GMEventRulesAndNotificationsApi.md#filtered_event_rules) | **GET** /monitoring/eventRules/{countryCode} | Filtered EventRules
[**list_company_events**](GMEventRulesAndNotificationsApi.md#list_company_events) | **GET** /monitoring/companies/{id}/events | List Company Events

# **all_event_rules**
> ConnectMonitoringEventRulesResponse all_event_rules()

All EventRules

Get all available notification event rules. Notification event rules allow you to control which events you wish to monitor for the `companies` contained within a given `portfolio`.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMEventRulesAndNotificationsApi(pycsapi.ApiClient(configuration))

try:
    # All EventRules
    api_response = api_instance.all_event_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMEventRulesAndNotificationsApi->all_event_rules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConnectMonitoringEventRulesResponse**](ConnectMonitoringEventRulesResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **all_notification_events**
> ConnectMonitoringAllNotificationsEvents all_notification_events(search_query=search_query, sort_by=sort_by, sort_dir=sort_dir, start_date=start_date, end_date=end_date, page=page, page_size=page_size, filter_by_created_date=filter_by_created_date)

All Notification Events

Get all notification events generated for companies monitored in your portfolios, based on the notification rules enabled. The notification events returned will be filtered based upon the supplied search criteria.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMEventRulesAndNotificationsApi(pycsapi.ApiClient(configuration))
search_query = 'search_query_example' # str | Return notificationEvents that match the given value (optional)
sort_by = 'companyName' # str | Sort results by this column. Null values of sort column are listed after non-nulls. (optional) (default to companyName)
sort_dir = 'asc' # str | The direction that you wish to sort results by. (optional) (default to asc)
start_date = '2013-10-20T19:20:30+01:00' # datetime | The start date on which results are filtered. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | The end date on which results are filtered. (optional)
page = 0 # int | Starting page number inGlobal Monitoring is `0`. If all items are displayed on one page this can also be left blank. (optional) (default to 0)
page_size = 56 # int | Number of items to return per Page. (optional)
filter_by_created_date = false # bool | Set to `true` to filter the Notification Events of the \"createdDate\" field when using `startDate` and `endDate` parameters. By default this is set to `false`, with the date parameters filtering using the \"eventDate\" field. (optional) (default to false)

try:
    # All Notification Events
    api_response = api_instance.all_notification_events(search_query=search_query, sort_by=sort_by, sort_dir=sort_dir, start_date=start_date, end_date=end_date, page=page, page_size=page_size, filter_by_created_date=filter_by_created_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMEventRulesAndNotificationsApi->all_notification_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_query** | **str**| Return notificationEvents that match the given value | [optional] 
 **sort_by** | **str**| Sort results by this column. Null values of sort column are listed after non-nulls. | [optional] [default to companyName]
 **sort_dir** | **str**| The direction that you wish to sort results by. | [optional] [default to asc]
 **start_date** | **datetime**| The start date on which results are filtered. | [optional] 
 **end_date** | **datetime**| The end date on which results are filtered. | [optional] 
 **page** | **int**| Starting page number inGlobal Monitoring is &#x60;0&#x60;. If all items are displayed on one page this can also be left blank. | [optional] [default to 0]
 **page_size** | **int**| Number of items to return per Page. | [optional] 
 **filter_by_created_date** | **bool**| Set to &#x60;true&#x60; to filter the Notification Events of the \&quot;createdDate\&quot; field when using &#x60;startDate&#x60; and &#x60;endDate&#x60; parameters. By default this is set to &#x60;false&#x60;, with the date parameters filtering using the \&quot;eventDate\&quot; field. | [optional] [default to false]

### Return type

[**ConnectMonitoringAllNotificationsEvents**](ConnectMonitoringAllNotificationsEvents.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **filtered_event_rules**
> ConnectMonitoringEventRulesResponse filtered_event_rules(country_code)

Filtered EventRules

Get all available notification event rules for the given `countryCode`. Notification event rules allow you to control which events you wish to monitor for the `companies` contained within a given `portfolio`.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMEventRulesAndNotificationsApi(pycsapi.ApiClient(configuration))
country_code = 'country_code_example' # str | ISO/Alpha 2 format country code for which notification event rules will be returned.

try:
    # Filtered EventRules
    api_response = api_instance.filtered_event_rules(country_code)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMEventRulesAndNotificationsApi->filtered_event_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_code** | **str**| ISO/Alpha 2 format country code for which notification event rules will be returned. | 

### Return type

[**ConnectMonitoringEventRulesResponse**](ConnectMonitoringEventRulesResponse.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_company_events**
> ConnectMonitoringCompanyEvents list_company_events(id, start_date=start_date, end_date=end_date, page=page, page_size=page_size)

List Company Events

Endpoint to return a collection of `events` for the given company, optionally filtered on the supplied search criteria. Event information will only be returned if the company exists in at least one of your `portfolios`.

### Example
```python
from __future__ import print_function
import time
import pycsapi
from pycsapi.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = pycsapi.GMEventRulesAndNotificationsApi(pycsapi.ApiClient(configuration))
id = 'id_example' # str | The connectId of the company that you wish to retrieve events for.
start_date = '2013-10-20T19:20:30+01:00' # datetime | The start date on which results are filtered. (optional)
end_date = '2013-10-20T19:20:30+01:00' # datetime | The end date on which results are filtered. (optional)
page = 0 # int | Starting page number inGlobal Monitoring is `0`. If all items are displayed on one page this can also be left blank. (optional) (default to 0)
page_size = 56 # int | Number of items to return per Page. (optional)

try:
    # List Company Events
    api_response = api_instance.list_company_events(id, start_date=start_date, end_date=end_date, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GMEventRulesAndNotificationsApi->list_company_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The connectId of the company that you wish to retrieve events for. | 
 **start_date** | **datetime**| The start date on which results are filtered. | [optional] 
 **end_date** | **datetime**| The end date on which results are filtered. | [optional] 
 **page** | **int**| Starting page number inGlobal Monitoring is &#x60;0&#x60;. If all items are displayed on one page this can also be left blank. | [optional] [default to 0]
 **page_size** | **int**| Number of items to return per Page. | [optional] 

### Return type

[**ConnectMonitoringCompanyEvents**](ConnectMonitoringCompanyEvents.md)

### Authorization

[bearerToken](../README.md#bearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


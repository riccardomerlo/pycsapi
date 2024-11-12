# GetAuditsResponseItems

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the Audit | [optional] 
**description** | **str** | Description of the Audit | [optional] 
**category** | **str** | Category of the audit | [optional] 
**subcategory** | **str** | Subcategory of the audit | [optional] 
**action** | **str** | Action of the audit | [optional] 
**created_at** | **datetime** | Audit created date and time | [optional] 
**created_by_id** | **int** | Id of the user who created the audit | [optional] 
**created_by** | **str** | Name of the user who created the audit | [optional] 
**payload** | **dict(str, object)** | The &#x60;payload&#x60; property represents the state of involved entities at the time of action taking place.&lt;br&gt;&lt;br&gt; This property contains dynamic data that varies depending on the request parameters and the context of the request. The response and can differ even with the same parameters under different conditions or contexts.&lt;br&gt;&lt;br&gt; This means the content of this property is not fixed and can include various data types such as GUIDs, strings, integers, and complex objects.&lt;br&gt;&lt;br&gt; Due to its dynamic nature, the &#x60;payload&#x60; can include any of the following potential structures, but is not limited to these examples &lt;li&gt; A single key-value pair where the value is a string or number. &lt;li&gt; A nested object containing detailed data structures. &lt;li&gt; An array of objects each with different attributes.&lt;br&gt;&lt;br&gt; Consumers of this API should handle the &#x60;payload&#x60; dynamically and be prepared to encounter different data types and structures.&lt;br&gt; Detailed processing logic based on the specific application needs and context checks is recommended when utilising this field. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


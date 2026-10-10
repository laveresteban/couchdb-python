# ExplainResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dbname** | **str** |  | [optional] 
**index** | [**ExplainResultIndex**](ExplainResultIndex.md) |  | [optional] 
**selector** | **Dict[str, object]** |  | [optional] 
**opts** | **Dict[str, object]** |  | [optional] 
**limit** | **int** |  | [optional] 
**skip** | **int** |  | [optional] 
**fields** | **object** | &#x60;\&quot;all_fields\&quot;&#x60; or a list of field names | [optional] 

## Example

```python
from couchdb_client.models.explain_result import ExplainResult

# TODO update the JSON string below
json = "{}"
# create an instance of ExplainResult from a JSON string
explain_result_instance = ExplainResult.from_json(json)
# print the JSON string representation of the object
print(ExplainResult.to_json())

# convert the object into a dict
explain_result_dict = explain_result_instance.to_dict()
# create an instance of ExplainResult from a dict
explain_result_from_dict = ExplainResult.from_dict(explain_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



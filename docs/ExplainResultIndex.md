# ExplainResultIndex


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ddoc** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**var_def** | **Dict[str, object]** |  | [optional] 

## Example

```python
from couchdb_client.models.explain_result_index import ExplainResultIndex

# TODO update the JSON string below
json = "{}"
# create an instance of ExplainResultIndex from a JSON string
explain_result_index_instance = ExplainResultIndex.from_json(json)
# print the JSON string representation of the object
print(ExplainResultIndex.to_json())

# convert the object into a dict
explain_result_index_dict = explain_result_index_instance.to_dict()
# create an instance of ExplainResultIndex from a dict
explain_result_index_from_dict = ExplainResultIndex.from_dict(explain_result_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



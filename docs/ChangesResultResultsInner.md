# ChangesResultResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**seq** | **str** |  | [optional] 
**deleted** | **bool** |  | [optional] 
**changes** | [**List[ChangesResultResultsInnerChangesInner]**](ChangesResultResultsInnerChangesInner.md) |  | [optional] 
**doc** | [**Document**](Document.md) |  | [optional] 

## Example

```python
from couchdb_client.models.changes_result_results_inner import ChangesResultResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChangesResultResultsInner from a JSON string
changes_result_results_inner_instance = ChangesResultResultsInner.from_json(json)
# print the JSON string representation of the object
print(ChangesResultResultsInner.to_json())

# convert the object into a dict
changes_result_results_inner_dict = changes_result_results_inner_instance.to_dict()
# create an instance of ChangesResultResultsInner from a dict
changes_result_results_inner_from_dict = ChangesResultResultsInner.from_dict(changes_result_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



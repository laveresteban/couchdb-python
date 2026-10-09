# ChangesResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_seq** | **str** |  | 
**pending** | **int** |  | [optional] 
**results** | [**List[ChangesResultResultsInner]**](ChangesResultResultsInner.md) |  | 

## Example

```python
from couchdb_client.models.changes_result import ChangesResult

# TODO update the JSON string below
json = "{}"
# create an instance of ChangesResult from a JSON string
changes_result_instance = ChangesResult.from_json(json)
# print the JSON string representation of the object
print(ChangesResult.to_json())

# convert the object into a dict
changes_result_dict = changes_result_instance.to_dict()
# create an instance of ChangesResult from a dict
changes_result_from_dict = ChangesResult.from_dict(changes_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



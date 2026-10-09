# IndexResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from couchdb_client.models.index_result import IndexResult

# TODO update the JSON string below
json = "{}"
# create an instance of IndexResult from a JSON string
index_result_instance = IndexResult.from_json(json)
# print the JSON string representation of the object
print(IndexResult.to_json())

# convert the object into a dict
index_result_dict = index_result_instance.to_dict()
# create an instance of IndexResult from a dict
index_result_from_dict = IndexResult.from_dict(index_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



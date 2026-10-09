# IndexesInformationIndexesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ddoc** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**partitioned** | **bool** |  | [optional] 
**var_def** | **Dict[str, object]** |  | [optional] 

## Example

```python
from couchdb_client.models.indexes_information_indexes_inner import IndexesInformationIndexesInner

# TODO update the JSON string below
json = "{}"
# create an instance of IndexesInformationIndexesInner from a JSON string
indexes_information_indexes_inner_instance = IndexesInformationIndexesInner.from_json(json)
# print the JSON string representation of the object
print(IndexesInformationIndexesInner.to_json())

# convert the object into a dict
indexes_information_indexes_inner_dict = indexes_information_indexes_inner_instance.to_dict()
# create an instance of IndexesInformationIndexesInner from a dict
indexes_information_indexes_inner_from_dict = IndexesInformationIndexesInner.from_dict(indexes_information_indexes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



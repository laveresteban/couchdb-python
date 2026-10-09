# IndexDefinitionRequestIndex


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | **List[str]** |  | 
**partial_filter_selector** | **Dict[str, object]** |  | [optional] 

## Example

```python
from couchdb_client.models.index_definition_request_index import IndexDefinitionRequestIndex

# TODO update the JSON string below
json = "{}"
# create an instance of IndexDefinitionRequestIndex from a JSON string
index_definition_request_index_instance = IndexDefinitionRequestIndex.from_json(json)
# print the JSON string representation of the object
print(IndexDefinitionRequestIndex.to_json())

# convert the object into a dict
index_definition_request_index_dict = index_definition_request_index_instance.to_dict()
# create an instance of IndexDefinitionRequestIndex from a dict
index_definition_request_index_from_dict = IndexDefinitionRequestIndex.from_dict(index_definition_request_index_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



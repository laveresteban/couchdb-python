# IndexDefinitionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | [**IndexDefinitionRequestIndex**](IndexDefinitionRequestIndex.md) |  | 
**ddoc** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] [default to 'json']
**partitioned** | **bool** |  | [optional] 

## Example

```python
from couchdb_client.models.index_definition_request import IndexDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IndexDefinitionRequest from a JSON string
index_definition_request_instance = IndexDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print(IndexDefinitionRequest.to_json())

# convert the object into a dict
index_definition_request_dict = index_definition_request_instance.to_dict()
# create an instance of IndexDefinitionRequest from a dict
index_definition_request_from_dict = IndexDefinitionRequest.from_dict(index_definition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ViewQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_docs** | **bool** |  | [optional] [default to False]
**reduce** | **bool** |  | [optional] 
**group** | **bool** |  | [optional] 
**group_level** | **int** |  | [optional] 
**keys** | **List[object]** |  | [optional] 
**key** | **object** |  | [optional] 
**start_key** | **object** |  | [optional] 
**end_key** | **object** |  | [optional] 
**startkey_docid** | **str** |  | [optional] 
**endkey_docid** | **str** |  | [optional] 
**inclusive_end** | **bool** |  | [optional] [default to True]
**limit** | **int** |  | [optional] 
**skip** | **int** |  | [optional] 
**descending** | **bool** |  | [optional] 
**conflicts** | **bool** |  | [optional] 
**attachments** | **bool** |  | [optional] 
**stable** | **bool** |  | [optional] 
**update_seq** | **bool** |  | [optional] 
**update** | **str** |  | [optional] 

## Example

```python
from couchdb_client.models.view_query import ViewQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ViewQuery from a JSON string
view_query_instance = ViewQuery.from_json(json)
# print the JSON string representation of the object
print(ViewQuery.to_json())

# convert the object into a dict
view_query_dict = view_query_instance.to_dict()
# create an instance of ViewQuery from a dict
view_query_from_dict = ViewQuery.from_dict(view_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



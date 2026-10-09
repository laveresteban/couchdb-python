# ChangesQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_ids** | **List[str]** |  | [optional] 
**selector** | **Dict[str, object]** |  | [optional] 

## Example

```python
from couchdb_client.models.changes_query import ChangesQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ChangesQuery from a JSON string
changes_query_instance = ChangesQuery.from_json(json)
# print the JSON string representation of the object
print(ChangesQuery.to_json())

# convert the object into a dict
changes_query_dict = changes_query_instance.to_dict()
# create an instance of ChangesQuery from a dict
changes_query_from_dict = ChangesQuery.from_dict(changes_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



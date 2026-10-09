# BulkDocs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**docs** | [**List[Document]**](Document.md) |  | 
**new_edits** | **bool** |  | [optional] [default to True]

## Example

```python
from couchdb_client.models.bulk_docs import BulkDocs

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDocs from a JSON string
bulk_docs_instance = BulkDocs.from_json(json)
# print the JSON string representation of the object
print(BulkDocs.to_json())

# convert the object into a dict
bulk_docs_dict = bulk_docs_instance.to_dict()
# create an instance of BulkDocs from a dict
bulk_docs_from_dict = BulkDocs.from_dict(bulk_docs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



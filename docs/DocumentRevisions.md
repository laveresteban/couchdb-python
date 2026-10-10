# DocumentRevisions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **int** |  | [optional] 
**ids** | **List[str]** |  | [optional] 

## Example

```python
from couchdb_client.models.document_revisions import DocumentRevisions

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentRevisions from a JSON string
document_revisions_instance = DocumentRevisions.from_json(json)
# print the JSON string representation of the object
print(DocumentRevisions.to_json())

# convert the object into a dict
document_revisions_dict = document_revisions_instance.to_dict()
# create an instance of DocumentRevisions from a dict
document_revisions_from_dict = DocumentRevisions.from_dict(document_revisions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



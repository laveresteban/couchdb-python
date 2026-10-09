# DocumentResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**rev** | **str** |  | [optional] 
**ok** | **bool** |  | [optional] 
**error** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 

## Example

```python
from couchdb_client.models.document_result import DocumentResult

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentResult from a JSON string
document_result_instance = DocumentResult.from_json(json)
# print the JSON string representation of the object
print(DocumentResult.to_json())

# convert the object into a dict
document_result_dict = document_result_instance.to_dict()
# create an instance of DocumentResult from a dict
document_result_from_dict = DocumentResult.from_dict(document_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



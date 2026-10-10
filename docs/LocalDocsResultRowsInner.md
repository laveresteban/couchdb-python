# LocalDocsResultRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**value** | [**ChangesResultResultsInnerChangesInner**](ChangesResultResultsInnerChangesInner.md) |  | [optional] 
**doc** | [**Document**](Document.md) |  | [optional] 

## Example

```python
from couchdb_client.models.local_docs_result_rows_inner import LocalDocsResultRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of LocalDocsResultRowsInner from a JSON string
local_docs_result_rows_inner_instance = LocalDocsResultRowsInner.from_json(json)
# print the JSON string representation of the object
print(LocalDocsResultRowsInner.to_json())

# convert the object into a dict
local_docs_result_rows_inner_dict = local_docs_result_rows_inner_instance.to_dict()
# create an instance of LocalDocsResultRowsInner from a dict
local_docs_result_rows_inner_from_dict = LocalDocsResultRowsInner.from_dict(local_docs_result_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



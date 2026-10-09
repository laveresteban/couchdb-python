# AllDocsResultRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**value** | [**AllDocsResultRowsInnerValue**](AllDocsResultRowsInnerValue.md) |  | [optional] 
**doc** | [**Document**](Document.md) |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from couchdb_client.models.all_docs_result_rows_inner import AllDocsResultRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AllDocsResultRowsInner from a JSON string
all_docs_result_rows_inner_instance = AllDocsResultRowsInner.from_json(json)
# print the JSON string representation of the object
print(AllDocsResultRowsInner.to_json())

# convert the object into a dict
all_docs_result_rows_inner_dict = all_docs_result_rows_inner_instance.to_dict()
# create an instance of AllDocsResultRowsInner from a dict
all_docs_result_rows_inner_from_dict = AllDocsResultRowsInner.from_dict(all_docs_result_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



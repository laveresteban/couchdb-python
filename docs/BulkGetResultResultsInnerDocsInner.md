# BulkGetResultResultsInnerDocsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | [**Document**](Document.md) |  | [optional] 
**error** | [**BulkGetResultResultsInnerDocsInnerError**](BulkGetResultResultsInnerDocsInnerError.md) |  | [optional] 

## Example

```python
from couchdb_client.models.bulk_get_result_results_inner_docs_inner import BulkGetResultResultsInnerDocsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkGetResultResultsInnerDocsInner from a JSON string
bulk_get_result_results_inner_docs_inner_instance = BulkGetResultResultsInnerDocsInner.from_json(json)
# print the JSON string representation of the object
print(BulkGetResultResultsInnerDocsInner.to_json())

# convert the object into a dict
bulk_get_result_results_inner_docs_inner_dict = bulk_get_result_results_inner_docs_inner_instance.to_dict()
# create an instance of BulkGetResultResultsInnerDocsInner from a dict
bulk_get_result_results_inner_docs_inner_from_dict = BulkGetResultResultsInnerDocsInner.from_dict(bulk_get_result_results_inner_docs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



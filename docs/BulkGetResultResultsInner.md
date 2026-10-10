# BulkGetResultResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**docs** | [**List[BulkGetResultResultsInnerDocsInner]**](BulkGetResultResultsInnerDocsInner.md) |  | [optional] 

## Example

```python
from couchdb_client.models.bulk_get_result_results_inner import BulkGetResultResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkGetResultResultsInner from a JSON string
bulk_get_result_results_inner_instance = BulkGetResultResultsInner.from_json(json)
# print the JSON string representation of the object
print(BulkGetResultResultsInner.to_json())

# convert the object into a dict
bulk_get_result_results_inner_dict = bulk_get_result_results_inner_instance.to_dict()
# create an instance of BulkGetResultResultsInner from a dict
bulk_get_result_results_inner_from_dict = BulkGetResultResultsInner.from_dict(bulk_get_result_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



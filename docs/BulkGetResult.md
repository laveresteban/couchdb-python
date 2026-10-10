# BulkGetResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[BulkGetResultResultsInner]**](BulkGetResultResultsInner.md) |  | 

## Example

```python
from couchdb_client.models.bulk_get_result import BulkGetResult

# TODO update the JSON string below
json = "{}"
# create an instance of BulkGetResult from a JSON string
bulk_get_result_instance = BulkGetResult.from_json(json)
# print the JSON string representation of the object
print(BulkGetResult.to_json())

# convert the object into a dict
bulk_get_result_dict = bulk_get_result_instance.to_dict()
# create an instance of BulkGetResult from a dict
bulk_get_result_from_dict = BulkGetResult.from_dict(bulk_get_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



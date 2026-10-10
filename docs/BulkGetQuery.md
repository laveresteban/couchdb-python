# BulkGetQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**docs** | [**List[BulkGetQueryDocsInner]**](BulkGetQueryDocsInner.md) |  | 

## Example

```python
from couchdb_client.models.bulk_get_query import BulkGetQuery

# TODO update the JSON string below
json = "{}"
# create an instance of BulkGetQuery from a JSON string
bulk_get_query_instance = BulkGetQuery.from_json(json)
# print the JSON string representation of the object
print(BulkGetQuery.to_json())

# convert the object into a dict
bulk_get_query_dict = bulk_get_query_instance.to_dict()
# create an instance of BulkGetQuery from a dict
bulk_get_query_from_dict = BulkGetQuery.from_dict(bulk_get_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



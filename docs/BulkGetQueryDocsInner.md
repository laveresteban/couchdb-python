# BulkGetQueryDocsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**rev** | **str** |  | [optional] 
**atts_since** | **List[str]** |  | [optional] 

## Example

```python
from couchdb_client.models.bulk_get_query_docs_inner import BulkGetQueryDocsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkGetQueryDocsInner from a JSON string
bulk_get_query_docs_inner_instance = BulkGetQueryDocsInner.from_json(json)
# print the JSON string representation of the object
print(BulkGetQueryDocsInner.to_json())

# convert the object into a dict
bulk_get_query_docs_inner_dict = bulk_get_query_docs_inner_instance.to_dict()
# create an instance of BulkGetQueryDocsInner from a dict
bulk_get_query_docs_inner_from_dict = BulkGetQueryDocsInner.from_dict(bulk_get_query_docs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



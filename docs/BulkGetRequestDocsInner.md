# BulkGetRequestDocsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**rev** | **str** |  | [optional] 
**atts_since** | **List[str]** |  | [optional] 

## Example

```python
from couchdb_client.models.bulk_get_request_docs_inner import BulkGetRequestDocsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkGetRequestDocsInner from a JSON string
bulk_get_request_docs_inner_instance = BulkGetRequestDocsInner.from_json(json)
# print the JSON string representation of the object
print(BulkGetRequestDocsInner.to_json())

# convert the object into a dict
bulk_get_request_docs_inner_dict = bulk_get_request_docs_inner_instance.to_dict()
# create an instance of BulkGetRequestDocsInner from a dict
bulk_get_request_docs_inner_from_dict = BulkGetRequestDocsInner.from_dict(bulk_get_request_docs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



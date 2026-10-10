# BulkGetRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**docs** | [**List[BulkGetRequestDocsInner]**](BulkGetRequestDocsInner.md) |  | 

## Example

```python
from couchdb_client.models.bulk_get_request import BulkGetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkGetRequest from a JSON string
bulk_get_request_instance = BulkGetRequest.from_json(json)
# print the JSON string representation of the object
print(BulkGetRequest.to_json())

# convert the object into a dict
bulk_get_request_dict = bulk_get_request_instance.to_dict()
# create an instance of BulkGetRequest from a dict
bulk_get_request_from_dict = BulkGetRequest.from_dict(bulk_get_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



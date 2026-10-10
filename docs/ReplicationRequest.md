# ReplicationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **object** | A database URL (string), or an object with &#x60;url&#x60; and optional &#x60;auth&#x60; (e.g. &#x60;{\&quot;basic\&quot;: {\&quot;username\&quot;: ..., \&quot;password\&quot;: ...}}&#x60;). Left untyped on purpose: &#x60;oneOf: [string, object]&#x60; breaks typescript-fetch.  | 
**target** | **object** | A database URL (string), or an object with &#x60;url&#x60; and optional &#x60;auth&#x60; (e.g. &#x60;{\&quot;basic\&quot;: {\&quot;username\&quot;: ..., \&quot;password\&quot;: ...}}&#x60;). Left untyped on purpose: &#x60;oneOf: [string, object]&#x60; breaks typescript-fetch.  | 
**create_target** | **bool** |  | [optional] 
**continuous** | **bool** |  | [optional] 
**cancel** | **bool** |  | [optional] 
**doc_ids** | **List[str]** |  | [optional] 
**selector** | **Dict[str, object]** |  | [optional] 

## Example

```python
from couchdb_client.models.replication_request import ReplicationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationRequest from a JSON string
replication_request_instance = ReplicationRequest.from_json(json)
# print the JSON string representation of the object
print(ReplicationRequest.to_json())

# convert the object into a dict
replication_request_dict = replication_request_instance.to_dict()
# create an instance of ReplicationRequest from a dict
replication_request_from_dict = ReplicationRequest.from_dict(replication_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ReplicationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | [**ReplicationRequestSource**](ReplicationRequestSource.md) |  | 
**target** | [**ReplicationRequestSource**](ReplicationRequestSource.md) |  | 
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



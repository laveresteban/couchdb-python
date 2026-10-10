# ReplicationResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | [optional] 
**session_id** | **str** |  | [optional] 
**source_last_seq** | **str** |  | [optional] 
**local_id** | **str** |  | [optional] 
**no_changes** | **bool** |  | [optional] 
**replication_id_version** | **int** |  | [optional] 
**history** | [**List[ReplicationResultHistoryInner]**](ReplicationResultHistoryInner.md) |  | [optional] 

## Example

```python
from couchdb_client.models.replication_result import ReplicationResult

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationResult from a JSON string
replication_result_instance = ReplicationResult.from_json(json)
# print the JSON string representation of the object
print(ReplicationResult.to_json())

# convert the object into a dict
replication_result_dict = replication_result_instance.to_dict()
# create an instance of ReplicationResult from a dict
replication_result_from_dict = ReplicationResult.from_dict(replication_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



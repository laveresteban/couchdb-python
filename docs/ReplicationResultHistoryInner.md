# ReplicationResultHistoryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_id** | **str** |  | [optional] 
**start_time** | **str** |  | [optional] 
**end_time** | **str** |  | [optional] 
**start_last_seq** | **object** | Sequence; a number or a string depending on server version | [optional] 
**end_last_seq** | **object** | Sequence; a number or a string depending on server version | [optional] 
**recorded_seq** | **object** | Sequence; a number or a string depending on server version | [optional] 
**missing_checked** | **int** |  | [optional] 
**missing_found** | **int** |  | [optional] 
**docs_read** | **int** |  | [optional] 
**docs_written** | **int** |  | [optional] 
**doc_write_failures** | **int** |  | [optional] 

## Example

```python
from couchdb_client.models.replication_result_history_inner import ReplicationResultHistoryInner

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationResultHistoryInner from a JSON string
replication_result_history_inner_instance = ReplicationResultHistoryInner.from_json(json)
# print the JSON string representation of the object
print(ReplicationResultHistoryInner.to_json())

# convert the object into a dict
replication_result_history_inner_dict = replication_result_history_inner_instance.to_dict()
# create an instance of ReplicationResultHistoryInner from a dict
replication_result_history_inner_from_dict = ReplicationResultHistoryInner.from_dict(replication_result_history_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



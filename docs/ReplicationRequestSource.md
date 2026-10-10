# ReplicationRequestSource

Database URL, or an endpoint object with url and auth

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**auth** | **Dict[str, object]** |  | [optional] 
**headers** | **Dict[str, str]** |  | [optional] 

## Example

```python
from couchdb_client.models.replication_request_source import ReplicationRequestSource

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationRequestSource from a JSON string
replication_request_source_instance = ReplicationRequestSource.from_json(json)
# print the JSON string representation of the object
print(ReplicationRequestSource.to_json())

# convert the object into a dict
replication_request_source_dict = replication_request_source_instance.to_dict()
# create an instance of ReplicationRequestSource from a dict
replication_request_source_from_dict = ReplicationRequestSource.from_dict(replication_request_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



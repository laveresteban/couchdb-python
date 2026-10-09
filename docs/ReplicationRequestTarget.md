# ReplicationRequestTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 

## Example

```python
from couchdb_client.models.replication_request_target import ReplicationRequestTarget

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationRequestTarget from a JSON string
replication_request_target_instance = ReplicationRequestTarget.from_json(json)
# print the JSON string representation of the object
print(ReplicationRequestTarget.to_json())

# convert the object into a dict
replication_request_target_dict = replication_request_target_instance.to_dict()
# create an instance of ReplicationRequestTarget from a dict
replication_request_target_from_dict = ReplicationRequestTarget.from_dict(replication_request_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



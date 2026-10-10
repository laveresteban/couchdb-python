# ReplicationEndpoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**auth** | **Dict[str, object]** |  | [optional] 
**headers** | **Dict[str, str]** |  | [optional] 

## Example

```python
from couchdb_client.models.replication_endpoint import ReplicationEndpoint

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicationEndpoint from a JSON string
replication_endpoint_instance = ReplicationEndpoint.from_json(json)
# print the JSON string representation of the object
print(ReplicationEndpoint.to_json())

# convert the object into a dict
replication_endpoint_dict = replication_endpoint_instance.to_dict()
# create an instance of ReplicationEndpoint from a dict
replication_endpoint_from_dict = ReplicationEndpoint.from_dict(replication_endpoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



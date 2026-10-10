# PurgeResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purge_seq** | **str** |  | [optional] 
**purged** | **Dict[str, List[str]]** |  | [optional] 

## Example

```python
from couchdb_client.models.purge_result import PurgeResult

# TODO update the JSON string below
json = "{}"
# create an instance of PurgeResult from a JSON string
purge_result_instance = PurgeResult.from_json(json)
# print the JSON string representation of the object
print(PurgeResult.to_json())

# convert the object into a dict
purge_result_dict = purge_result_instance.to_dict()
# create an instance of PurgeResult from a dict
purge_result_from_dict = PurgeResult.from_dict(purge_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



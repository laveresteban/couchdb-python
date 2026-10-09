# UuidsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuids** | **List[str]** |  | 

## Example

```python
from couchdb_client.models.uuids_result import UuidsResult

# TODO update the JSON string below
json = "{}"
# create an instance of UuidsResult from a JSON string
uuids_result_instance = UuidsResult.from_json(json)
# print the JSON string representation of the object
print(UuidsResult.to_json())

# convert the object into a dict
uuids_result_dict = uuids_result_instance.to_dict()
# create an instance of UuidsResult from a dict
uuids_result_from_dict = UuidsResult.from_dict(uuids_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



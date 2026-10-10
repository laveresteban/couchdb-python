# DbsInfoEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**info** | [**DatabaseInformation**](DatabaseInformation.md) |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from couchdb_client.models.dbs_info_entry import DbsInfoEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DbsInfoEntry from a JSON string
dbs_info_entry_instance = DbsInfoEntry.from_json(json)
# print the JSON string representation of the object
print(DbsInfoEntry.to_json())

# convert the object into a dict
dbs_info_entry_dict = dbs_info_entry_instance.to_dict()
# create an instance of DbsInfoEntry from a dict
dbs_info_entry_from_dict = DbsInfoEntry.from_dict(dbs_info_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



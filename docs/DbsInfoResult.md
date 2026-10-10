# DbsInfoResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**info** | [**DatabaseInformation**](DatabaseInformation.md) |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from couchdb_client.models.dbs_info_result import DbsInfoResult

# TODO update the JSON string below
json = "{}"
# create an instance of DbsInfoResult from a JSON string
dbs_info_result_instance = DbsInfoResult.from_json(json)
# print the JSON string representation of the object
print(DbsInfoResult.to_json())

# convert the object into a dict
dbs_info_result_dict = dbs_info_result_instance.to_dict()
# create an instance of DbsInfoResult from a dict
dbs_info_result_from_dict = DbsInfoResult.from_dict(dbs_info_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



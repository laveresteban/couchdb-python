# DbUpdatesResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_seq** | **str** |  | [optional] 
**results** | [**List[DbUpdatesResultResultsInner]**](DbUpdatesResultResultsInner.md) |  | 

## Example

```python
from couchdb_client.models.db_updates_result import DbUpdatesResult

# TODO update the JSON string below
json = "{}"
# create an instance of DbUpdatesResult from a JSON string
db_updates_result_instance = DbUpdatesResult.from_json(json)
# print the JSON string representation of the object
print(DbUpdatesResult.to_json())

# convert the object into a dict
db_updates_result_dict = db_updates_result_instance.to_dict()
# create an instance of DbUpdatesResult from a dict
db_updates_result_from_dict = DbUpdatesResult.from_dict(db_updates_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



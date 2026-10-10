# DbUpdatesResultResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_name** | **str** |  | [optional] 
**type** | **str** | &#x60;created&#x60;, &#x60;updated&#x60; or &#x60;deleted&#x60; | [optional] 
**seq** | **str** |  | [optional] 

## Example

```python
from couchdb_client.models.db_updates_result_results_inner import DbUpdatesResultResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DbUpdatesResultResultsInner from a JSON string
db_updates_result_results_inner_instance = DbUpdatesResultResultsInner.from_json(json)
# print the JSON string representation of the object
print(DbUpdatesResultResultsInner.to_json())

# convert the object into a dict
db_updates_result_results_inner_dict = db_updates_result_results_inner_instance.to_dict()
# create an instance of DbUpdatesResultResultsInner from a dict
db_updates_result_results_inner_from_dict = DbUpdatesResultResultsInner.from_dict(db_updates_result_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



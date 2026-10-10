# ActiveTask


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**pid** | **str** |  | [optional] 
**database** | **str** |  | [optional] 
**node** | **str** |  | [optional] 
**started_on** | **int** |  | [optional] 
**updated_on** | **int** |  | [optional] 
**progress** | **int** |  | [optional] 

## Example

```python
from couchdb_client.models.active_task import ActiveTask

# TODO update the JSON string below
json = "{}"
# create an instance of ActiveTask from a JSON string
active_task_instance = ActiveTask.from_json(json)
# print the JSON string representation of the object
print(ActiveTask.to_json())

# convert the object into a dict
active_task_dict = active_task_instance.to_dict()
# create an instance of ActiveTask from a dict
active_task_from_dict = ActiveTask.from_dict(active_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SchedulerJobs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_rows** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**jobs** | **List[Dict[str, object]]** |  | [optional] 

## Example

```python
from couchdb_client.models.scheduler_jobs import SchedulerJobs

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulerJobs from a JSON string
scheduler_jobs_instance = SchedulerJobs.from_json(json)
# print the JSON string representation of the object
print(SchedulerJobs.to_json())

# convert the object into a dict
scheduler_jobs_dict = scheduler_jobs_instance.to_dict()
# create an instance of SchedulerJobs from a dict
scheduler_jobs_from_dict = SchedulerJobs.from_dict(scheduler_jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



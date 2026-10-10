# SchedulerJobsJobsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**database** | **str** |  | [optional] 
**doc_id** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**user** | **str** |  | [optional] 
**node** | **str** |  | [optional] 
**pid** | **str** |  | [optional] 
**start_time** | **str** |  | [optional] 

## Example

```python
from couchdb_client.models.scheduler_jobs_jobs_inner import SchedulerJobsJobsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulerJobsJobsInner from a JSON string
scheduler_jobs_jobs_inner_instance = SchedulerJobsJobsInner.from_json(json)
# print the JSON string representation of the object
print(SchedulerJobsJobsInner.to_json())

# convert the object into a dict
scheduler_jobs_jobs_inner_dict = scheduler_jobs_jobs_inner_instance.to_dict()
# create an instance of SchedulerJobsJobsInner from a dict
scheduler_jobs_jobs_inner_from_dict = SchedulerJobsJobsInner.from_dict(scheduler_jobs_jobs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SchedulerDocsDocsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database** | **str** |  | [optional] 
**doc_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**target** | **str** |  | [optional] 
**error_count** | **int** |  | [optional] 
**last_updated** | **str** |  | [optional] 

## Example

```python
from couchdb_client.models.scheduler_docs_docs_inner import SchedulerDocsDocsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulerDocsDocsInner from a JSON string
scheduler_docs_docs_inner_instance = SchedulerDocsDocsInner.from_json(json)
# print the JSON string representation of the object
print(SchedulerDocsDocsInner.to_json())

# convert the object into a dict
scheduler_docs_docs_inner_dict = scheduler_docs_docs_inner_instance.to_dict()
# create an instance of SchedulerDocsDocsInner from a dict
scheduler_docs_docs_inner_from_dict = SchedulerDocsDocsInner.from_dict(scheduler_docs_docs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SchedulerDocs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_rows** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**docs** | [**List[SchedulerDocsDocsInner]**](SchedulerDocsDocsInner.md) |  | 

## Example

```python
from couchdb_client.models.scheduler_docs import SchedulerDocs

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulerDocs from a JSON string
scheduler_docs_instance = SchedulerDocs.from_json(json)
# print the JSON string representation of the object
print(SchedulerDocs.to_json())

# convert the object into a dict
scheduler_docs_dict = scheduler_docs_instance.to_dict()
# create an instance of SchedulerDocs from a dict
scheduler_docs_from_dict = SchedulerDocs.from_dict(scheduler_docs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



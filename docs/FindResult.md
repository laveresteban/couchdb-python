# FindResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**docs** | [**List[Document]**](Document.md) |  | 
**bookmark** | **str** |  | [optional] 
**warning** | **str** |  | [optional] 
**execution_stats** | **Dict[str, object]** |  | [optional] 

## Example

```python
from couchdb_client.models.find_result import FindResult

# TODO update the JSON string below
json = "{}"
# create an instance of FindResult from a JSON string
find_result_instance = FindResult.from_json(json)
# print the JSON string representation of the object
print(FindResult.to_json())

# convert the object into a dict
find_result_dict = find_result_instance.to_dict()
# create an instance of FindResult from a dict
find_result_from_dict = FindResult.from_dict(find_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



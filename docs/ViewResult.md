# ViewResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_rows** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**rows** | [**List[ViewResultRowsInner]**](ViewResultRowsInner.md) |  | 

## Example

```python
from couchdb_client.models.view_result import ViewResult

# TODO update the JSON string below
json = "{}"
# create an instance of ViewResult from a JSON string
view_result_instance = ViewResult.from_json(json)
# print the JSON string representation of the object
print(ViewResult.to_json())

# convert the object into a dict
view_result_dict = view_result_instance.to_dict()
# create an instance of ViewResult from a dict
view_result_from_dict = ViewResult.from_dict(view_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



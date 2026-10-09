# ViewResultRowsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**key** | **object** |  | [optional] 
**value** | **object** |  | [optional] 
**doc** | [**Document**](Document.md) |  | [optional] 

## Example

```python
from couchdb_client.models.view_result_rows_inner import ViewResultRowsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ViewResultRowsInner from a JSON string
view_result_rows_inner_instance = ViewResultRowsInner.from_json(json)
# print the JSON string representation of the object
print(ViewResultRowsInner.to_json())

# convert the object into a dict
view_result_rows_inner_dict = view_result_rows_inner_instance.to_dict()
# create an instance of ViewResultRowsInner from a dict
view_result_rows_inner_from_dict = ViewResultRowsInner.from_dict(view_result_rows_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



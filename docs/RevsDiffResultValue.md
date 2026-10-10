# RevsDiffResultValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**missing** | **List[str]** |  | [optional] 
**possible_ancestors** | **List[str]** |  | [optional] 

## Example

```python
from couchdb_client.models.revs_diff_result_value import RevsDiffResultValue

# TODO update the JSON string below
json = "{}"
# create an instance of RevsDiffResultValue from a JSON string
revs_diff_result_value_instance = RevsDiffResultValue.from_json(json)
# print the JSON string representation of the object
print(RevsDiffResultValue.to_json())

# convert the object into a dict
revs_diff_result_value_dict = revs_diff_result_value_instance.to_dict()
# create an instance of RevsDiffResultValue from a dict
revs_diff_result_value_from_dict = RevsDiffResultValue.from_dict(revs_diff_result_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



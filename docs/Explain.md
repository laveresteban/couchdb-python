# Explain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dbname** | **str** |  | [optional] 
**index** | **Dict[str, object]** |  | [optional] 
**selector** | **Dict[str, object]** |  | [optional] 
**opts** | **Dict[str, object]** |  | [optional] 
**limit** | **int** |  | [optional] 
**skip** | **int** |  | [optional] 
**fields** | **List[str]** |  | [optional] 
**range** | **Dict[str, object]** |  | [optional] 

## Example

```python
from couchdb_client.models.explain import Explain

# TODO update the JSON string below
json = "{}"
# create an instance of Explain from a JSON string
explain_instance = Explain.from_json(json)
# print the JSON string representation of the object
print(Explain.to_json())

# convert the object into a dict
explain_dict = explain_instance.to_dict()
# create an instance of Explain from a dict
explain_from_dict = Explain.from_dict(explain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



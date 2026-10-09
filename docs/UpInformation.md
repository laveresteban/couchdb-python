# UpInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**seeds** | **Dict[str, object]** |  | [optional] 

## Example

```python
from couchdb_client.models.up_information import UpInformation

# TODO update the JSON string below
json = "{}"
# create an instance of UpInformation from a JSON string
up_information_instance = UpInformation.from_json(json)
# print the JSON string representation of the object
print(UpInformation.to_json())

# convert the object into a dict
up_information_dict = up_information_instance.to_dict()
# create an instance of UpInformation from a dict
up_information_from_dict = UpInformation.from_dict(up_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



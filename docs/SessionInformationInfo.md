# SessionInformationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authenticated** | **str** |  | [optional] 
**authentication_db** | **str** |  | [optional] 
**authentication_handlers** | **List[str]** |  | [optional] 

## Example

```python
from couchdb_client.models.session_information_info import SessionInformationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SessionInformationInfo from a JSON string
session_information_info_instance = SessionInformationInfo.from_json(json)
# print the JSON string representation of the object
print(SessionInformationInfo.to_json())

# convert the object into a dict
session_information_info_dict = session_information_info_instance.to_dict()
# create an instance of SessionInformationInfo from a dict
session_information_info_from_dict = SessionInformationInfo.from_dict(session_information_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



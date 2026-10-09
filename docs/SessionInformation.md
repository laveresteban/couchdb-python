# SessionInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ok** | **bool** |  | 
**user_ctx** | [**SessionInformationUserCtx**](SessionInformationUserCtx.md) |  | 
**info** | [**SessionInformationInfo**](SessionInformationInfo.md) |  | [optional] 

## Example

```python
from couchdb_client.models.session_information import SessionInformation

# TODO update the JSON string below
json = "{}"
# create an instance of SessionInformation from a JSON string
session_information_instance = SessionInformation.from_json(json)
# print the JSON string representation of the object
print(SessionInformation.to_json())

# convert the object into a dict
session_information_dict = session_information_instance.to_dict()
# create an instance of SessionInformation from a dict
session_information_from_dict = SessionInformation.from_dict(session_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



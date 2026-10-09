# SessionInformationUserCtx


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**roles** | **List[str]** |  | [optional] 

## Example

```python
from couchdb_client.models.session_information_user_ctx import SessionInformationUserCtx

# TODO update the JSON string below
json = "{}"
# create an instance of SessionInformationUserCtx from a JSON string
session_information_user_ctx_instance = SessionInformationUserCtx.from_json(json)
# print the JSON string representation of the object
print(SessionInformationUserCtx.to_json())

# convert the object into a dict
session_information_user_ctx_dict = session_information_user_ctx_instance.to_dict()
# create an instance of SessionInformationUserCtx from a dict
session_information_user_ctx_from_dict = SessionInformationUserCtx.from_dict(session_information_user_ctx_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# ServerInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**couchdb** | **str** |  | 
**version** | **str** |  | 
**git_sha** | **str** |  | [optional] 
**uuid** | **str** |  | [optional] 
**features** | **List[str]** |  | [optional] 
**vendor** | [**ServerInformationVendor**](ServerInformationVendor.md) |  | [optional] 

## Example

```python
from couchdb_client.models.server_information import ServerInformation

# TODO update the JSON string below
json = "{}"
# create an instance of ServerInformation from a JSON string
server_information_instance = ServerInformation.from_json(json)
# print the JSON string representation of the object
print(ServerInformation.to_json())

# convert the object into a dict
server_information_dict = server_information_instance.to_dict()
# create an instance of ServerInformation from a dict
server_information_from_dict = ServerInformation.from_dict(server_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



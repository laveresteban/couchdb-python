# ServerInformationVendor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 

## Example

```python
from couchdb_client.models.server_information_vendor import ServerInformationVendor

# TODO update the JSON string below
json = "{}"
# create an instance of ServerInformationVendor from a JSON string
server_information_vendor_instance = ServerInformationVendor.from_json(json)
# print the JSON string representation of the object
print(ServerInformationVendor.to_json())

# convert the object into a dict
server_information_vendor_dict = server_information_vendor_instance.to_dict()
# create an instance of ServerInformationVendor from a dict
server_information_vendor_from_dict = ServerInformationVendor.from_dict(server_information_vendor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



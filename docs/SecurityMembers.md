# SecurityMembers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** |  | [optional] 
**roles** | **List[str]** |  | [optional] 

## Example

```python
from couchdb_client.models.security_members import SecurityMembers

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityMembers from a JSON string
security_members_instance = SecurityMembers.from_json(json)
# print the JSON string representation of the object
print(SecurityMembers.to_json())

# convert the object into a dict
security_members_dict = security_members_instance.to_dict()
# create an instance of SecurityMembers from a dict
security_members_from_dict = SecurityMembers.from_dict(security_members_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



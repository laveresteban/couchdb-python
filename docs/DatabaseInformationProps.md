# DatabaseInformationProps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partitioned** | **bool** |  | [optional] 

## Example

```python
from couchdb_client.models.database_information_props import DatabaseInformationProps

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseInformationProps from a JSON string
database_information_props_instance = DatabaseInformationProps.from_json(json)
# print the JSON string representation of the object
print(DatabaseInformationProps.to_json())

# convert the object into a dict
database_information_props_dict = database_information_props_instance.to_dict()
# create an instance of DatabaseInformationProps from a dict
database_information_props_from_dict = DatabaseInformationProps.from_dict(database_information_props_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



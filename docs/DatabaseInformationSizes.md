# DatabaseInformationSizes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **int** |  | [optional] 
**external** | **int** |  | [optional] 
**file** | **int** |  | [optional] 

## Example

```python
from couchdb_client.models.database_information_sizes import DatabaseInformationSizes

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseInformationSizes from a JSON string
database_information_sizes_instance = DatabaseInformationSizes.from_json(json)
# print the JSON string representation of the object
print(DatabaseInformationSizes.to_json())

# convert the object into a dict
database_information_sizes_dict = database_information_sizes_instance.to_dict()
# create an instance of DatabaseInformationSizes from a dict
database_information_sizes_from_dict = DatabaseInformationSizes.from_dict(database_information_sizes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



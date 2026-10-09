# DatabaseInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**db_name** | **str** |  | 
**update_seq** | **str** |  | [optional] 
**purge_seq** | **str** |  | [optional] 
**doc_count** | **int** |  | [optional] 
**doc_del_count** | **int** |  | [optional] 
**compact_running** | **bool** |  | [optional] 
**instance_start_time** | **str** |  | [optional] 
**sizes** | [**DatabaseInformationSizes**](DatabaseInformationSizes.md) |  | [optional] 
**props** | [**DatabaseInformationProps**](DatabaseInformationProps.md) |  | [optional] 

## Example

```python
from couchdb_client.models.database_information import DatabaseInformation

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseInformation from a JSON string
database_information_instance = DatabaseInformation.from_json(json)
# print the JSON string representation of the object
print(DatabaseInformation.to_json())

# convert the object into a dict
database_information_dict = database_information_instance.to_dict()
# create an instance of DatabaseInformation from a dict
database_information_from_dict = DatabaseInformation.from_dict(database_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



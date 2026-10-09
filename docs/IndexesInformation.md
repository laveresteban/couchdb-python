# IndexesInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_rows** | **int** |  | [optional] 
**indexes** | [**List[IndexesInformationIndexesInner]**](IndexesInformationIndexesInner.md) |  | 

## Example

```python
from couchdb_client.models.indexes_information import IndexesInformation

# TODO update the JSON string below
json = "{}"
# create an instance of IndexesInformation from a JSON string
indexes_information_instance = IndexesInformation.from_json(json)
# print the JSON string representation of the object
print(IndexesInformation.to_json())

# convert the object into a dict
indexes_information_dict = indexes_information_instance.to_dict()
# create an instance of IndexesInformation from a dict
indexes_information_from_dict = IndexesInformation.from_dict(indexes_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AllDocsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_rows** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**update_seq** | **str** |  | [optional] 
**rows** | [**List[AllDocsResultRowsInner]**](AllDocsResultRowsInner.md) |  | 

## Example

```python
from couchdb_client.models.all_docs_result import AllDocsResult

# TODO update the JSON string below
json = "{}"
# create an instance of AllDocsResult from a JSON string
all_docs_result_instance = AllDocsResult.from_json(json)
# print the JSON string representation of the object
print(AllDocsResult.to_json())

# convert the object into a dict
all_docs_result_dict = all_docs_result_instance.to_dict()
# create an instance of AllDocsResult from a dict
all_docs_result_from_dict = AllDocsResult.from_dict(all_docs_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



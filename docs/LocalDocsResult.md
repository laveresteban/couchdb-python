# LocalDocsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_rows** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**rows** | [**List[LocalDocsResultRowsInner]**](LocalDocsResultRowsInner.md) |  | 

## Example

```python
from couchdb_client.models.local_docs_result import LocalDocsResult

# TODO update the JSON string below
json = "{}"
# create an instance of LocalDocsResult from a JSON string
local_docs_result_instance = LocalDocsResult.from_json(json)
# print the JSON string representation of the object
print(LocalDocsResult.to_json())

# convert the object into a dict
local_docs_result_dict = local_docs_result_instance.to_dict()
# create an instance of LocalDocsResult from a dict
local_docs_result_from_dict = LocalDocsResult.from_dict(local_docs_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# AllDocsQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_docs** | **bool** |  | [optional] [default to False]
**keys** | **List[str]** |  | [optional] 
**start_key** | **str** |  | [optional] 
**end_key** | **str** |  | [optional] 
**limit** | **int** |  | [optional] 
**skip** | **int** |  | [optional] 
**descending** | **bool** |  | [optional] 

## Example

```python
from couchdb_client.models.all_docs_query import AllDocsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of AllDocsQuery from a JSON string
all_docs_query_instance = AllDocsQuery.from_json(json)
# print the JSON string representation of the object
print(AllDocsQuery.to_json())

# convert the object into a dict
all_docs_query_dict = all_docs_query_instance.to_dict()
# create an instance of AllDocsQuery from a dict
all_docs_query_from_dict = AllDocsQuery.from_dict(all_docs_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FindQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selector** | **Dict[str, object]** |  | 
**fields** | **List[str]** |  | [optional] 
**sort** | **List[Dict[str, str]]** | Field/direction pairs, e.g. &#x60;[{\&quot;age\&quot;: \&quot;desc\&quot;}]&#x60;. Direction is &#x60;asc&#x60; or &#x60;desc&#x60;. | [optional] 
**limit** | **int** |  | [optional] 
**skip** | **int** |  | [optional] 
**use_index** | **List[str]** |  | [optional] 
**bookmark** | **str** |  | [optional] 
**execution_stats** | **bool** |  | [optional] 

## Example

```python
from couchdb_client.models.find_query import FindQuery

# TODO update the JSON string below
json = "{}"
# create an instance of FindQuery from a JSON string
find_query_instance = FindQuery.from_json(json)
# print the JSON string representation of the object
print(FindQuery.to_json())

# convert the object into a dict
find_query_dict = find_query_instance.to_dict()
# create an instance of FindQuery from a dict
find_query_from_dict = FindQuery.from_dict(find_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



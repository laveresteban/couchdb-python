# Revisions

Revision history, newest first. Full rev ids are `{start - i}-{ids[i]}`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start** | **int** |  | 
**ids** | **List[str]** |  | 

## Example

```python
from couchdb_client.models.revisions import Revisions

# TODO update the JSON string below
json = "{}"
# create an instance of Revisions from a JSON string
revisions_instance = Revisions.from_json(json)
# print the JSON string representation of the object
print(Revisions.to_json())

# convert the object into a dict
revisions_dict = revisions_instance.to_dict()
# create an instance of Revisions from a dict
revisions_from_dict = Revisions.from_dict(revisions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



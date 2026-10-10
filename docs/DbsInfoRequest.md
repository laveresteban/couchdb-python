# DbsInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **List[str]** |  | 

## Example

```python
from couchdb_client.models.dbs_info_request import DbsInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DbsInfoRequest from a JSON string
dbs_info_request_instance = DbsInfoRequest.from_json(json)
# print the JSON string representation of the object
print(DbsInfoRequest.to_json())

# convert the object into a dict
dbs_info_request_dict = dbs_info_request_instance.to_dict()
# create an instance of DbsInfoRequest from a dict
dbs_info_request_from_dict = DbsInfoRequest.from_dict(dbs_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



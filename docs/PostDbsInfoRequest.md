# PostDbsInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keys** | **List[str]** |  | 

## Example

```python
from couchdb_client.models.post_dbs_info_request import PostDbsInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDbsInfoRequest from a JSON string
post_dbs_info_request_instance = PostDbsInfoRequest.from_json(json)
# print the JSON string representation of the object
print(PostDbsInfoRequest.to_json())

# convert the object into a dict
post_dbs_info_request_dict = post_dbs_info_request_instance.to_dict()
# create an instance of PostDbsInfoRequest from a dict
post_dbs_info_request_from_dict = PostDbsInfoRequest.from_dict(post_dbs_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



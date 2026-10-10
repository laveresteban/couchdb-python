# Attachment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  | [optional] 
**data** | **bytearray** | Base64 body (inline only) | [optional] 
**digest** | **str** |  | [optional] 
**length** | **int** |  | [optional] 
**revpos** | **int** |  | [optional] 
**stub** | **bool** |  | [optional] 
**follows** | **bool** |  | [optional] 
**encoding** | **str** |  | [optional] 
**encoded_length** | **int** |  | [optional] 

## Example

```python
from couchdb_client.models.attachment import Attachment

# TODO update the JSON string below
json = "{}"
# create an instance of Attachment from a JSON string
attachment_instance = Attachment.from_json(json)
# print the JSON string representation of the object
print(Attachment.to_json())

# convert the object into a dict
attachment_dict = attachment_instance.to_dict()
# create an instance of Attachment from a dict
attachment_from_dict = Attachment.from_dict(attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



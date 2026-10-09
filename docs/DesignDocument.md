# DesignDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**rev** | **str** |  | [optional] 
**language** | **str** |  | [optional] [default to 'javascript']
**views** | [**Dict[str, DesignDocumentViewsValue]**](DesignDocumentViewsValue.md) |  | [optional] 
**options** | **Dict[str, object]** |  | [optional] 

## Example

```python
from couchdb_client.models.design_document import DesignDocument

# TODO update the JSON string below
json = "{}"
# create an instance of DesignDocument from a JSON string
design_document_instance = DesignDocument.from_json(json)
# print the JSON string representation of the object
print(DesignDocument.to_json())

# convert the object into a dict
design_document_dict = design_document_instance.to_dict()
# create an instance of DesignDocument from a dict
design_document_from_dict = DesignDocument.from_dict(design_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DesignDocumentViewsValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**map** | **str** |  | [optional] 
**reduce** | **str** |  | [optional] 
**options** | **Dict[str, object]** |  | [optional] 

## Example

```python
from couchdb_client.models.design_document_views_value import DesignDocumentViewsValue

# TODO update the JSON string below
json = "{}"
# create an instance of DesignDocumentViewsValue from a JSON string
design_document_views_value_instance = DesignDocumentViewsValue.from_json(json)
# print the JSON string representation of the object
print(DesignDocumentViewsValue.to_json())

# convert the object into a dict
design_document_views_value_dict = design_document_views_value_instance.to_dict()
# create an instance of DesignDocumentViewsValue from a dict
design_document_views_value_from_dict = DesignDocumentViewsValue.from_dict(design_document_views_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# couchdb_client.DesignDocumentsApi

All URIs are relative to *http://localhost:5984*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_view**](DesignDocumentsApi.md#post_view) | **POST** /{db}/_design/{ddoc}/_view/{view} | Query a MapReduce view


# **post_view**
> ViewResult post_view(db, ddoc, view, view_query)

Query a MapReduce view

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.view_query import ViewQuery
from couchdb_client.models.view_result import ViewResult
from couchdb_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5984
# See configuration.py for a list of all supported configuration parameters.
configuration = couchdb_client.Configuration(
    host = "http://localhost:5984"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = couchdb_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with couchdb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = couchdb_client.DesignDocumentsApi(api_client)
    db = 'db_example' # str | Database name
    ddoc = 'ddoc_example' # str | Design document name without the `_design/` prefix
    view = 'view_example' # str | 
    view_query = couchdb_client.ViewQuery() # ViewQuery | 

    try:
        # Query a MapReduce view
        api_response = api_instance.post_view(db, ddoc, view, view_query)
        print("The response of DesignDocumentsApi->post_view:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DesignDocumentsApi->post_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name | 
 **ddoc** | **str**| Design document name without the &#x60;_design/&#x60; prefix | 
 **view** | **str**|  | 
 **view_query** | [**ViewQuery**](ViewQuery.md)|  | 

### Return type

[**ViewResult**](ViewResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | View rows |  -  |
**404** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


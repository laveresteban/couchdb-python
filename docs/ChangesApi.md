# couchdb_client.ChangesApi

All URIs are relative to *http://localhost:5984*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_changes**](ChangesApi.md#get_changes) | **GET** /{db}/_changes | Database changes feed (normal or longpoll)


# **get_changes**
> ChangesResult get_changes(db, feed=feed, since=since, include_docs=include_docs, limit=limit, timeout=timeout, descending=descending)

Database changes feed (normal or longpoll)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.changes_result import ChangesResult
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
    api_instance = couchdb_client.ChangesApi(api_client)
    db = 'db_example' # str | Database name
    feed = normal # str |  (optional) (default to normal)
    since = '0' # str |  (optional) (default to '0')
    include_docs = False # bool |  (optional) (default to False)
    limit = 56 # int |  (optional)
    timeout = 56 # int | Longpoll timeout in milliseconds (optional)
    descending = False # bool |  (optional) (default to False)

    try:
        # Database changes feed (normal or longpoll)
        api_response = api_instance.get_changes(db, feed=feed, since=since, include_docs=include_docs, limit=limit, timeout=timeout, descending=descending)
        print("The response of ChangesApi->get_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChangesApi->get_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name | 
 **feed** | **str**|  | [optional] [default to normal]
 **since** | **str**|  | [optional] [default to &#39;0&#39;]
 **include_docs** | **bool**|  | [optional] [default to False]
 **limit** | **int**|  | [optional] 
 **timeout** | **int**| Longpoll timeout in milliseconds | [optional] 
 **descending** | **bool**|  | [optional] [default to False]

### Return type

[**ChangesResult**](ChangesResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Changes |  -  |
**404** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


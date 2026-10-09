# couchdb_client.ReplicationApi

All URIs are relative to *http://localhost:5984*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_replicate**](ReplicationApi.md#post_replicate) | **POST** /_replicate | Run or cancel a one-off replication


# **post_replicate**
> ReplicationResult post_replicate(replication_request)

Run or cancel a one-off replication

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.replication_request import ReplicationRequest
from couchdb_client.models.replication_result import ReplicationResult
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
    api_instance = couchdb_client.ReplicationApi(api_client)
    replication_request = couchdb_client.ReplicationRequest() # ReplicationRequest | 

    try:
        # Run or cancel a one-off replication
        api_response = api_instance.post_replicate(replication_request)
        print("The response of ReplicationApi->post_replicate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReplicationApi->post_replicate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replication_request** | [**ReplicationRequest**](ReplicationRequest.md)|  | 

### Return type

[**ReplicationResult**](ReplicationResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Replication finished |  -  |
**202** | Continuous replication started |  -  |
**404** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


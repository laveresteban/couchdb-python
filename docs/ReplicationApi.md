# couchdb_client.ReplicationApi

All URIs are relative to *http://localhost:5984*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_bulk_get**](ReplicationApi.md#post_bulk_get) | **POST** /{db}/_bulk_get | Fetch many documents and revisions in one request
[**post_replicate**](ReplicationApi.md#post_replicate) | **POST** /_replicate | Run or cancel a one-off replication
[**post_revs_diff**](ReplicationApi.md#post_revs_diff) | **POST** /{db}/_revs_diff | Find which revisions the database does not have


# **post_bulk_get**
> BulkGetResult post_bulk_get(db, bulk_get_request, revs=revs, latest=latest, attachments=attachments)

Fetch many documents and revisions in one request

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.bulk_get_request import BulkGetRequest
from couchdb_client.models.bulk_get_result import BulkGetResult
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
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.
    bulk_get_request = couchdb_client.BulkGetRequest() # BulkGetRequest | 
    revs = False # bool | Include `_revisions` in each returned document (optional) (default to False)
    latest = False # bool |  (optional) (default to False)
    attachments = False # bool | Include attachment content as base64 `data`. With `atts_since`, only attachments newer than those revisions are sent; the rest come back as stubs. (optional) (default to False)

    try:
        # Fetch many documents and revisions in one request
        api_response = api_instance.post_bulk_get(db, bulk_get_request, revs=revs, latest=latest, attachments=attachments)
        print("The response of ReplicationApi->post_bulk_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReplicationApi->post_bulk_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 
 **bulk_get_request** | [**BulkGetRequest**](BulkGetRequest.md)|  | 
 **revs** | **bool**| Include &#x60;_revisions&#x60; in each returned document | [optional] [default to False]
 **latest** | **bool**|  | [optional] [default to False]
 **attachments** | **bool**| Include attachment content as base64 &#x60;data&#x60;. With &#x60;atts_since&#x60;, only attachments newer than those revisions are sent; the rest come back as stubs. | [optional] [default to False]

### Return type

[**BulkGetResult**](BulkGetResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One result per requested document |  -  |
**401** | CouchDB error |  -  |
**400** | CouchDB error |  -  |
**403** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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
**400** | CouchDB error |  -  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |
**500** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_revs_diff**
> Dict[str, RevsDiffResultValue] post_revs_diff(db, request_body)

Find which revisions the database does not have

Used by replicators to skip revisions the target already stores.

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.revs_diff_result_value import RevsDiffResultValue
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
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.
    request_body = None # Dict[str, List[str]] | 

    try:
        # Find which revisions the database does not have
        api_response = api_instance.post_revs_diff(db, request_body)
        print("The response of ReplicationApi->post_revs_diff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReplicationApi->post_revs_diff: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 
 **request_body** | [**Dict[str, List[str]]**](List.md)|  | 

### Return type

[**Dict[str, RevsDiffResultValue]**](RevsDiffResultValue.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Missing revisions, keyed by document id |  -  |
**401** | CouchDB error |  -  |
**400** | CouchDB error |  -  |
**403** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


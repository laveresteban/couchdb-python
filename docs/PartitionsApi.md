# couchdb_client.PartitionsApi

All URIs are relative to *http://localhost:5984*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_partition_all_docs**](PartitionsApi.md#post_partition_all_docs) | **POST** /{db}/_partition/{partition}/_all_docs | Query all documents in one partition
[**post_partition_find**](PartitionsApi.md#post_partition_find) | **POST** /{db}/_partition/{partition}/_find | Mango query within one partition


# **post_partition_all_docs**
> AllDocsResult post_partition_all_docs(db, partition, all_docs_query)

Query all documents in one partition

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.all_docs_query import AllDocsQuery
from couchdb_client.models.all_docs_result import AllDocsResult
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
    api_instance = couchdb_client.PartitionsApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.
    partition = 'partition_example' # str | 
    all_docs_query = couchdb_client.AllDocsQuery() # AllDocsQuery | 

    try:
        # Query all documents in one partition
        api_response = api_instance.post_partition_all_docs(db, partition, all_docs_query)
        print("The response of PartitionsApi->post_partition_all_docs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartitionsApi->post_partition_all_docs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 
 **partition** | **str**|  | 
 **all_docs_query** | [**AllDocsQuery**](AllDocsQuery.md)|  | 

### Return type

[**AllDocsResult**](AllDocsResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rows |  -  |
**401** | CouchDB error |  -  |
**400** | CouchDB error |  -  |
**403** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_partition_find**
> FindResult post_partition_find(db, partition, find_query)

Mango query within one partition

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.find_query import FindQuery
from couchdb_client.models.find_result import FindResult
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
    api_instance = couchdb_client.PartitionsApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.
    partition = 'partition_example' # str | 
    find_query = couchdb_client.FindQuery() # FindQuery | 

    try:
        # Mango query within one partition
        api_response = api_instance.post_partition_find(db, partition, find_query)
        print("The response of PartitionsApi->post_partition_find:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PartitionsApi->post_partition_find: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 
 **partition** | **str**|  | 
 **find_query** | [**FindQuery**](FindQuery.md)|  | 

### Return type

[**FindResult**](FindResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Matching documents |  -  |
**401** | CouchDB error |  -  |
**400** | CouchDB error |  -  |
**403** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


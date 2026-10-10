# couchdb_client.QueryApi

All URIs are relative to *http://localhost:5984*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_docs**](QueryApi.md#get_all_docs) | **GET** /{db}/_all_docs | Query all documents (key range in the query string)
[**get_design_docs**](QueryApi.md#get_design_docs) | **GET** /{db}/_design_docs | List design documents
[**get_indexes**](QueryApi.md#get_indexes) | **GET** /{db}/_index | List Mango indexes
[**get_local_docs**](QueryApi.md#get_local_docs) | **GET** /{db}/_local_docs | List local (non-replicated) documents
[**post_all_docs**](QueryApi.md#post_all_docs) | **POST** /{db}/_all_docs | Query all documents
[**post_explain**](QueryApi.md#post_explain) | **POST** /{db}/_explain | Show which index a Mango query would use
[**post_find**](QueryApi.md#post_find) | **POST** /{db}/_find | Mango query
[**post_index**](QueryApi.md#post_index) | **POST** /{db}/_index | Create a Mango index


# **get_all_docs**
> AllDocsResult get_all_docs(db, include_docs=include_docs, key=key, keys=keys, start_key=start_key, end_key=end_key, inclusive_end=inclusive_end, limit=limit, skip=skip, descending=descending, conflicts=conflicts, update_seq=update_seq)

Query all documents (key range in the query string)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import couchdb_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = couchdb_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with couchdb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = couchdb_client.QueryApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.
    include_docs = False # bool |  (optional) (default to False)
    key = 'key_example' # str | JSON-encoded key, e.g. `\"abc\"` (with quotes) or `[1,2]`. (optional)
    keys = 'keys_example' # str | JSON-encoded array of keys. (optional)
    start_key = 'start_key_example' # str | JSON-encoded key to start at. (optional)
    end_key = 'end_key_example' # str | JSON-encoded key to end at. (optional)
    inclusive_end = True # bool |  (optional) (default to True)
    limit = 56 # int |  (optional)
    skip = 0 # int |  (optional) (default to 0)
    descending = False # bool |  (optional) (default to False)
    conflicts = False # bool |  (optional) (default to False)
    update_seq = False # bool |  (optional) (default to False)

    try:
        # Query all documents (key range in the query string)
        api_response = api_instance.get_all_docs(db, include_docs=include_docs, key=key, keys=keys, start_key=start_key, end_key=end_key, inclusive_end=inclusive_end, limit=limit, skip=skip, descending=descending, conflicts=conflicts, update_seq=update_seq)
        print("The response of QueryApi->get_all_docs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryApi->get_all_docs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 
 **include_docs** | **bool**|  | [optional] [default to False]
 **key** | **str**| JSON-encoded key, e.g. &#x60;\&quot;abc\&quot;&#x60; (with quotes) or &#x60;[1,2]&#x60;. | [optional] 
 **keys** | **str**| JSON-encoded array of keys. | [optional] 
 **start_key** | **str**| JSON-encoded key to start at. | [optional] 
 **end_key** | **str**| JSON-encoded key to end at. | [optional] 
 **inclusive_end** | **bool**|  | [optional] [default to True]
 **limit** | **int**|  | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **descending** | **bool**|  | [optional] [default to False]
 **conflicts** | **bool**|  | [optional] [default to False]
 **update_seq** | **bool**|  | [optional] [default to False]

### Return type

[**AllDocsResult**](AllDocsResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rows |  -  |
**400** | CouchDB error |  -  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |
**404** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_design_docs**
> AllDocsResult get_design_docs(db, include_docs=include_docs, start_key=start_key, end_key=end_key, limit=limit, skip=skip, descending=descending)

List design documents

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import couchdb_client
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = couchdb_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with couchdb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = couchdb_client.QueryApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.
    include_docs = False # bool |  (optional) (default to False)
    start_key = 'start_key_example' # str | JSON-encoded key to start at. (optional)
    end_key = 'end_key_example' # str | JSON-encoded key to end at. (optional)
    limit = 56 # int |  (optional)
    skip = 0 # int |  (optional) (default to 0)
    descending = False # bool |  (optional) (default to False)

    try:
        # List design documents
        api_response = api_instance.get_design_docs(db, include_docs=include_docs, start_key=start_key, end_key=end_key, limit=limit, skip=skip, descending=descending)
        print("The response of QueryApi->get_design_docs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryApi->get_design_docs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 
 **include_docs** | **bool**|  | [optional] [default to False]
 **start_key** | **str**| JSON-encoded key to start at. | [optional] 
 **end_key** | **str**| JSON-encoded key to end at. | [optional] 
 **limit** | **int**|  | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **descending** | **bool**|  | [optional] [default to False]

### Return type

[**AllDocsResult**](AllDocsResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rows |  -  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |
**404** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indexes**
> IndexesInformation get_indexes(db)

List Mango indexes

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import couchdb_client
from couchdb_client.models.indexes_information import IndexesInformation
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = couchdb_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with couchdb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = couchdb_client.QueryApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.

    try:
        # List Mango indexes
        api_response = api_instance.get_indexes(db)
        print("The response of QueryApi->get_indexes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryApi->get_indexes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 

### Return type

[**IndexesInformation**](IndexesInformation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Indexes |  -  |
**401** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_local_docs**
> LocalDocsResult get_local_docs(db, include_docs=include_docs, start_key=start_key, end_key=end_key, limit=limit, skip=skip, descending=descending)

List local (non-replicated) documents

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import couchdb_client
from couchdb_client.models.local_docs_result import LocalDocsResult
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = couchdb_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with couchdb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = couchdb_client.QueryApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.
    include_docs = False # bool |  (optional) (default to False)
    start_key = 'start_key_example' # str | JSON-encoded key to start at. (optional)
    end_key = 'end_key_example' # str | JSON-encoded key to end at. (optional)
    limit = 56 # int |  (optional)
    skip = 0 # int |  (optional) (default to 0)
    descending = False # bool |  (optional) (default to False)

    try:
        # List local (non-replicated) documents
        api_response = api_instance.get_local_docs(db, include_docs=include_docs, start_key=start_key, end_key=end_key, limit=limit, skip=skip, descending=descending)
        print("The response of QueryApi->get_local_docs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryApi->get_local_docs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 
 **include_docs** | **bool**|  | [optional] [default to False]
 **start_key** | **str**| JSON-encoded key to start at. | [optional] 
 **end_key** | **str**| JSON-encoded key to end at. | [optional] 
 **limit** | **int**|  | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **descending** | **bool**|  | [optional] [default to False]

### Return type

[**LocalDocsResult**](LocalDocsResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rows (&#x60;total_rows&#x60; and &#x60;offset&#x60; are always null here) |  -  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |
**404** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_all_docs**
> AllDocsResult post_all_docs(db, all_docs_query)

Query all documents

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (bearerAuth):

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

# Configure Bearer authorization (JWT): bearerAuth
configuration = couchdb_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with couchdb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = couchdb_client.QueryApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.
    all_docs_query = couchdb_client.AllDocsQuery() # AllDocsQuery | 

    try:
        # Query all documents
        api_response = api_instance.post_all_docs(db, all_docs_query)
        print("The response of QueryApi->post_all_docs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryApi->post_all_docs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 
 **all_docs_query** | [**AllDocsQuery**](AllDocsQuery.md)|  | 

### Return type

[**AllDocsResult**](AllDocsResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

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

# **post_explain**
> ExplainResult post_explain(db, find_query)

Show which index a Mango query would use

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import couchdb_client
from couchdb_client.models.explain_result import ExplainResult
from couchdb_client.models.find_query import FindQuery
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = couchdb_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with couchdb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = couchdb_client.QueryApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.
    find_query = couchdb_client.FindQuery() # FindQuery | 

    try:
        # Show which index a Mango query would use
        api_response = api_instance.post_explain(db, find_query)
        print("The response of QueryApi->post_explain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryApi->post_explain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 
 **find_query** | [**FindQuery**](FindQuery.md)|  | 

### Return type

[**ExplainResult**](ExplainResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query plan |  -  |
**400** | CouchDB error |  -  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_find**
> FindResult post_find(db, find_query)

Mango query

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (bearerAuth):

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

# Configure Bearer authorization (JWT): bearerAuth
configuration = couchdb_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with couchdb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = couchdb_client.QueryApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.
    find_query = couchdb_client.FindQuery() # FindQuery | 

    try:
        # Mango query
        api_response = api_instance.post_find(db, find_query)
        print("The response of QueryApi->post_find:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryApi->post_find: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 
 **find_query** | [**FindQuery**](FindQuery.md)|  | 

### Return type

[**FindResult**](FindResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Matching documents |  -  |
**400** | CouchDB error |  -  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_index**
> IndexResult post_index(db, index_definition_request)

Create a Mango index

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import couchdb_client
from couchdb_client.models.index_definition_request import IndexDefinitionRequest
from couchdb_client.models.index_result import IndexResult
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

# Configure Bearer authorization (JWT): bearerAuth
configuration = couchdb_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with couchdb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = couchdb_client.QueryApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.
    index_definition_request = couchdb_client.IndexDefinitionRequest() # IndexDefinitionRequest | 

    try:
        # Create a Mango index
        api_response = api_instance.post_index(db, index_definition_request)
        print("The response of QueryApi->post_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryApi->post_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 
 **index_definition_request** | [**IndexDefinitionRequest**](IndexDefinitionRequest.md)|  | 

### Return type

[**IndexResult**](IndexResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Index created or already exists |  -  |
**401** | CouchDB error |  -  |
**400** | CouchDB error |  -  |
**403** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


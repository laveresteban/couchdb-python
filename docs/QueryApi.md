# couchdb_client.QueryApi

All URIs are relative to *http://localhost:5984*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_docs**](QueryApi.md#get_all_docs) | **GET** /{db}/_all_docs | Query all documents (GET form; keys are JSON-encoded)
[**get_indexes**](QueryApi.md#get_indexes) | **GET** /{db}/_index | List Mango indexes
[**post_all_docs**](QueryApi.md#post_all_docs) | **POST** /{db}/_all_docs | Query all documents
[**post_explain**](QueryApi.md#post_explain) | **POST** /{db}/_explain | Explain how a Mango query would run
[**post_find**](QueryApi.md#post_find) | **POST** /{db}/_find | Mango query
[**post_index**](QueryApi.md#post_index) | **POST** /{db}/_index | Create a Mango index


# **get_all_docs**
> AllDocsResult get_all_docs(db, include_docs=include_docs, descending=descending, limit=limit, skip=skip, key=key, startkey=startkey, endkey=endkey)

Query all documents (GET form; keys are JSON-encoded)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

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

# Enter a context with an instance of the API client
with couchdb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = couchdb_client.QueryApi(api_client)
    db = 'db_example' # str | Database name
    include_docs = False # bool |  (optional) (default to False)
    descending = False # bool |  (optional) (default to False)
    limit = 56 # int |  (optional)
    skip = 0 # int |  (optional) (default to 0)
    key = 'key_example' # str | JSON-encoded key to match exactly (optional)
    startkey = 'startkey_example' # str | JSON-encoded first key (optional)
    endkey = 'endkey_example' # str | JSON-encoded last key (optional)

    try:
        # Query all documents (GET form; keys are JSON-encoded)
        api_response = api_instance.get_all_docs(db, include_docs=include_docs, descending=descending, limit=limit, skip=skip, key=key, startkey=startkey, endkey=endkey)
        print("The response of QueryApi->get_all_docs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryApi->get_all_docs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name | 
 **include_docs** | **bool**|  | [optional] [default to False]
 **descending** | **bool**|  | [optional] [default to False]
 **limit** | **int**|  | [optional] 
 **skip** | **int**|  | [optional] [default to 0]
 **key** | **str**| JSON-encoded key to match exactly | [optional] 
 **startkey** | **str**| JSON-encoded first key | [optional] 
 **endkey** | **str**| JSON-encoded last key | [optional] 

### Return type

[**AllDocsResult**](AllDocsResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rows |  * X-Couch-Request-ID -  <br>  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_indexes**
> IndexesInformation get_indexes(db)

List Mango indexes

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

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

# Enter a context with an instance of the API client
with couchdb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = couchdb_client.QueryApi(api_client)
    db = 'db_example' # str | Database name

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
 **db** | **str**| Database name | 

### Return type

[**IndexesInformation**](IndexesInformation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Indexes |  * X-Couch-Request-ID -  <br>  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_all_docs**
> AllDocsResult post_all_docs(db, all_docs_query)

Query all documents

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
    api_instance = couchdb_client.QueryApi(api_client)
    db = 'db_example' # str | Database name
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
 **db** | **str**| Database name | 
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
**200** | Rows |  * X-Couch-Request-ID -  <br>  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |
**400** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_explain**
> Explain post_explain(db, find_query)

Explain how a Mango query would run

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.explain import Explain
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

# Enter a context with an instance of the API client
with couchdb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = couchdb_client.QueryApi(api_client)
    db = 'db_example' # str | Database name
    find_query = couchdb_client.FindQuery() # FindQuery | 

    try:
        # Explain how a Mango query would run
        api_response = api_instance.post_explain(db, find_query)
        print("The response of QueryApi->post_explain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QueryApi->post_explain: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name | 
 **find_query** | [**FindQuery**](FindQuery.md)|  | 

### Return type

[**Explain**](Explain.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query plan |  * X-Couch-Request-ID -  <br>  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |
**400** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_find**
> FindResult post_find(db, find_query)

Mango query

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
    api_instance = couchdb_client.QueryApi(api_client)
    db = 'db_example' # str | Database name
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
 **db** | **str**| Database name | 
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
**200** | Matching documents |  * X-Couch-Request-ID -  <br>  |
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

# Enter a context with an instance of the API client
with couchdb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = couchdb_client.QueryApi(api_client)
    db = 'db_example' # str | Database name
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
 **db** | **str**| Database name | 
 **index_definition_request** | [**IndexDefinitionRequest**](IndexDefinitionRequest.md)|  | 

### Return type

[**IndexResult**](IndexResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Index created or already exists |  * X-Couch-Request-ID -  <br>  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |
**400** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


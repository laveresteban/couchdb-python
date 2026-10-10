# couchdb_client.DocumentsApi

All URIs are relative to *http://localhost:5984*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_document**](DocumentsApi.md#delete_document) | **DELETE** /{db}/{docid} | Delete a document
[**delete_local_document**](DocumentsApi.md#delete_local_document) | **DELETE** /{db}/_local/{docid} | Delete a local document
[**get_document**](DocumentsApi.md#get_document) | **GET** /{db}/{docid} | Get a document
[**get_local_document**](DocumentsApi.md#get_local_document) | **GET** /{db}/_local/{docid} | Get a local (non-replicated) document
[**post_bulk_docs**](DocumentsApi.md#post_bulk_docs) | **POST** /{db}/_bulk_docs | Create, update or delete documents in bulk
[**post_document**](DocumentsApi.md#post_document) | **POST** /{db} | Create a document with a server-generated id
[**put_document**](DocumentsApi.md#put_document) | **PUT** /{db}/{docid} | Create or update a document
[**put_local_document**](DocumentsApi.md#put_local_document) | **PUT** /{db}/_local/{docid} | Create or update a local document


# **delete_document**
> DocumentResult delete_document(db, docid, if_match=if_match, rev=rev)

Delete a document

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.document_result import DocumentResult
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
    api_instance = couchdb_client.DocumentsApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.
    docid = 'docid_example' # str | 
    if_match = 'if_match_example' # str | Document revision (alternative to `rev`) (optional)
    rev = 'rev_example' # str |  (optional)

    try:
        # Delete a document
        api_response = api_instance.delete_document(db, docid, if_match=if_match, rev=rev)
        print("The response of DocumentsApi->delete_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->delete_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 
 **docid** | **str**|  | 
 **if_match** | **str**| Document revision (alternative to &#x60;rev&#x60;) | [optional] 
 **rev** | **str**|  | [optional] 

### Return type

[**DocumentResult**](DocumentResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document deleted |  -  |
**202** | Deletion accepted |  -  |
**404** | CouchDB error |  -  |
**409** | CouchDB error |  -  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_local_document**
> DocumentResult delete_local_document(db, docid, rev=rev)

Delete a local document

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.document_result import DocumentResult
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
    api_instance = couchdb_client.DocumentsApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.
    docid = 'docid_example' # str | 
    rev = 'rev_example' # str |  (optional)

    try:
        # Delete a local document
        api_response = api_instance.delete_local_document(db, docid, rev=rev)
        print("The response of DocumentsApi->delete_local_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->delete_local_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 
 **docid** | **str**|  | 
 **rev** | **str**|  | [optional] 

### Return type

[**DocumentResult**](DocumentResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document deleted |  -  |
**404** | CouchDB error |  -  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |
**409** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document**
> Document get_document(db, docid, rev=rev, revs_info=revs_info, conflicts=conflicts, revs=revs, latest=latest)

Get a document

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.document import Document
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
    api_instance = couchdb_client.DocumentsApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.
    docid = 'docid_example' # str | 
    rev = 'rev_example' # str |  (optional)
    revs_info = False # bool |  (optional) (default to False)
    conflicts = False # bool |  (optional) (default to False)
    revs = False # bool | Include the revision history as `_revisions` (optional) (default to False)
    latest = False # bool | With `rev`, return the latest leaf revision on that branch (optional) (default to False)

    try:
        # Get a document
        api_response = api_instance.get_document(db, docid, rev=rev, revs_info=revs_info, conflicts=conflicts, revs=revs, latest=latest)
        print("The response of DocumentsApi->get_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 
 **docid** | **str**|  | 
 **rev** | **str**|  | [optional] 
 **revs_info** | **bool**|  | [optional] [default to False]
 **conflicts** | **bool**|  | [optional] [default to False]
 **revs** | **bool**| Include the revision history as &#x60;_revisions&#x60; | [optional] [default to False]
 **latest** | **bool**| With &#x60;rev&#x60;, return the latest leaf revision on that branch | [optional] [default to False]

### Return type

[**Document**](Document.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The document |  -  |
**404** | CouchDB error |  -  |
**400** | CouchDB error |  -  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_local_document**
> Document get_local_document(db, docid)

Get a local (non-replicated) document

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.document import Document
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
    api_instance = couchdb_client.DocumentsApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.
    docid = 'docid_example' # str | 

    try:
        # Get a local (non-replicated) document
        api_response = api_instance.get_local_document(db, docid)
        print("The response of DocumentsApi->get_local_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->get_local_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 
 **docid** | **str**|  | 

### Return type

[**Document**](Document.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The document |  -  |
**404** | CouchDB error |  -  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_bulk_docs**
> List[DocumentResult] post_bulk_docs(db, bulk_docs)

Create, update or delete documents in bulk

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.bulk_docs import BulkDocs
from couchdb_client.models.document_result import DocumentResult
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
    api_instance = couchdb_client.DocumentsApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.
    bulk_docs = couchdb_client.BulkDocs() # BulkDocs | 

    try:
        # Create, update or delete documents in bulk
        api_response = api_instance.post_bulk_docs(db, bulk_docs)
        print("The response of DocumentsApi->post_bulk_docs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->post_bulk_docs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 
 **bulk_docs** | [**BulkDocs**](BulkDocs.md)|  | 

### Return type

[**List[DocumentResult]**](DocumentResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Per-document results |  -  |
**401** | CouchDB error |  -  |
**400** | CouchDB error |  -  |
**403** | CouchDB error |  -  |
**417** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_document**
> DocumentResult post_document(db, document)

Create a document with a server-generated id

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.document import Document
from couchdb_client.models.document_result import DocumentResult
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
    api_instance = couchdb_client.DocumentsApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.
    document = couchdb_client.Document() # Document | 

    try:
        # Create a document with a server-generated id
        api_response = api_instance.post_document(db, document)
        print("The response of DocumentsApi->post_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->post_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 
 **document** | [**Document**](Document.md)|  | 

### Return type

[**DocumentResult**](DocumentResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Document created |  -  |
**202** | Document accepted |  -  |
**409** | CouchDB error |  -  |
**400** | CouchDB error |  -  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_document**
> DocumentResult put_document(db, docid, document, if_match=if_match, rev=rev)

Create or update a document

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.document import Document
from couchdb_client.models.document_result import DocumentResult
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
    api_instance = couchdb_client.DocumentsApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.
    docid = 'docid_example' # str | 
    document = couchdb_client.Document() # Document | 
    if_match = 'if_match_example' # str | Document revision (alternative to `rev`) (optional)
    rev = 'rev_example' # str |  (optional)

    try:
        # Create or update a document
        api_response = api_instance.put_document(db, docid, document, if_match=if_match, rev=rev)
        print("The response of DocumentsApi->put_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->put_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 
 **docid** | **str**|  | 
 **document** | [**Document**](Document.md)|  | 
 **if_match** | **str**| Document revision (alternative to &#x60;rev&#x60;) | [optional] 
 **rev** | **str**|  | [optional] 

### Return type

[**DocumentResult**](DocumentResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Document written |  -  |
**202** | Document accepted |  -  |
**409** | CouchDB error |  -  |
**400** | CouchDB error |  -  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_local_document**
> DocumentResult put_local_document(db, docid, document)

Create or update a local document

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.document import Document
from couchdb_client.models.document_result import DocumentResult
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
    api_instance = couchdb_client.DocumentsApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.
    docid = 'docid_example' # str | 
    document = couchdb_client.Document() # Document | 

    try:
        # Create or update a local document
        api_response = api_instance.put_local_document(db, docid, document)
        print("The response of DocumentsApi->put_local_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->put_local_document: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 
 **docid** | **str**|  | 
 **document** | [**Document**](Document.md)|  | 

### Return type

[**DocumentResult**](DocumentResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Document written |  -  |
**409** | CouchDB error |  -  |
**400** | CouchDB error |  -  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


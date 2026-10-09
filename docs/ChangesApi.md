# couchdb_client.ChangesApi

All URIs are relative to *http://localhost:5984*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_changes**](ChangesApi.md#get_changes) | **GET** /{db}/_changes | Database changes feed (normal or longpoll)
[**post_changes**](ChangesApi.md#post_changes) | **POST** /{db}/_changes | Changes feed filtered by a body (&#x60;_doc_ids&#x60; or &#x60;_selector&#x60;)


# **get_changes**
> ChangesResult get_changes(db, feed=feed, since=since, include_docs=include_docs, conflicts=conflicts, attachments=attachments, style=style, filter=filter, view=view, doc_ids=doc_ids, limit=limit, timeout=timeout, heartbeat=heartbeat, seq_interval=seq_interval, descending=descending)

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
    feed = normal # str | `continuous` and `eventsource` stream; SDKs follow the feed with `longpoll`. (optional) (default to normal)
    since = '0' # str | Start after this sequence; `now` skips existing changes. (optional) (default to '0')
    include_docs = False # bool |  (optional) (default to False)
    conflicts = False # bool | Include `_conflicts` in docs; requires `include_docs`. (optional) (default to False)
    attachments = False # bool |  (optional) (default to False)
    style = main_only # str | `all_docs` returns all leaf revisions, not just the winner. (optional) (default to main_only)
    filter = 'filter_example' # str | `_doc_ids`, `_selector`, `_design`, `_view` or `ddoc/filter`. (optional)
    view = 'view_example' # str | `ddoc/view` used with `filter=_view`. (optional)
    doc_ids = 'doc_ids_example' # str | JSON array of ids, used with `filter=_doc_ids`. (optional)
    limit = 56 # int |  (optional)
    timeout = 56 # int | Longpoll timeout in milliseconds (optional)
    heartbeat = 56 # int | Milliseconds between keep-alive newlines. (optional)
    seq_interval = 56 # int | Only compute `seq` every N rows; others are null. Faster on clusters. (optional)
    descending = False # bool |  (optional) (default to False)

    try:
        # Database changes feed (normal or longpoll)
        api_response = api_instance.get_changes(db, feed=feed, since=since, include_docs=include_docs, conflicts=conflicts, attachments=attachments, style=style, filter=filter, view=view, doc_ids=doc_ids, limit=limit, timeout=timeout, heartbeat=heartbeat, seq_interval=seq_interval, descending=descending)
        print("The response of ChangesApi->get_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChangesApi->get_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name | 
 **feed** | **str**| &#x60;continuous&#x60; and &#x60;eventsource&#x60; stream; SDKs follow the feed with &#x60;longpoll&#x60;. | [optional] [default to normal]
 **since** | **str**| Start after this sequence; &#x60;now&#x60; skips existing changes. | [optional] [default to &#39;0&#39;]
 **include_docs** | **bool**|  | [optional] [default to False]
 **conflicts** | **bool**| Include &#x60;_conflicts&#x60; in docs; requires &#x60;include_docs&#x60;. | [optional] [default to False]
 **attachments** | **bool**|  | [optional] [default to False]
 **style** | **str**| &#x60;all_docs&#x60; returns all leaf revisions, not just the winner. | [optional] [default to main_only]
 **filter** | **str**| &#x60;_doc_ids&#x60;, &#x60;_selector&#x60;, &#x60;_design&#x60;, &#x60;_view&#x60; or &#x60;ddoc/filter&#x60;. | [optional] 
 **view** | **str**| &#x60;ddoc/view&#x60; used with &#x60;filter&#x3D;_view&#x60;. | [optional] 
 **doc_ids** | **str**| JSON array of ids, used with &#x60;filter&#x3D;_doc_ids&#x60;. | [optional] 
 **limit** | **int**|  | [optional] 
 **timeout** | **int**| Longpoll timeout in milliseconds | [optional] 
 **heartbeat** | **int**| Milliseconds between keep-alive newlines. | [optional] 
 **seq_interval** | **int**| Only compute &#x60;seq&#x60; every N rows; others are null. Faster on clusters. | [optional] 
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
**400** | CouchDB error |  -  |
**404** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_changes**
> ChangesResult post_changes(db, changes_query, feed=feed, since=since, include_docs=include_docs, conflicts=conflicts, attachments=attachments, style=style, filter=filter, view=view, doc_ids=doc_ids, limit=limit, timeout=timeout, heartbeat=heartbeat, seq_interval=seq_interval, descending=descending)

Changes feed filtered by a body (`_doc_ids` or `_selector`)

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.changes_query import ChangesQuery
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
    changes_query = couchdb_client.ChangesQuery() # ChangesQuery | 
    feed = normal # str | `continuous` and `eventsource` stream; SDKs follow the feed with `longpoll`. (optional) (default to normal)
    since = '0' # str | Start after this sequence; `now` skips existing changes. (optional) (default to '0')
    include_docs = False # bool |  (optional) (default to False)
    conflicts = False # bool | Include `_conflicts` in docs; requires `include_docs`. (optional) (default to False)
    attachments = False # bool |  (optional) (default to False)
    style = main_only # str | `all_docs` returns all leaf revisions, not just the winner. (optional) (default to main_only)
    filter = 'filter_example' # str | `_doc_ids`, `_selector`, `_design`, `_view` or `ddoc/filter`. (optional)
    view = 'view_example' # str | `ddoc/view` used with `filter=_view`. (optional)
    doc_ids = 'doc_ids_example' # str | JSON array of ids, used with `filter=_doc_ids`. (optional)
    limit = 56 # int |  (optional)
    timeout = 56 # int | Longpoll timeout in milliseconds (optional)
    heartbeat = 56 # int | Milliseconds between keep-alive newlines. (optional)
    seq_interval = 56 # int | Only compute `seq` every N rows; others are null. Faster on clusters. (optional)
    descending = False # bool |  (optional) (default to False)

    try:
        # Changes feed filtered by a body (`_doc_ids` or `_selector`)
        api_response = api_instance.post_changes(db, changes_query, feed=feed, since=since, include_docs=include_docs, conflicts=conflicts, attachments=attachments, style=style, filter=filter, view=view, doc_ids=doc_ids, limit=limit, timeout=timeout, heartbeat=heartbeat, seq_interval=seq_interval, descending=descending)
        print("The response of ChangesApi->post_changes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChangesApi->post_changes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name | 
 **changes_query** | [**ChangesQuery**](ChangesQuery.md)|  | 
 **feed** | **str**| &#x60;continuous&#x60; and &#x60;eventsource&#x60; stream; SDKs follow the feed with &#x60;longpoll&#x60;. | [optional] [default to normal]
 **since** | **str**| Start after this sequence; &#x60;now&#x60; skips existing changes. | [optional] [default to &#39;0&#39;]
 **include_docs** | **bool**|  | [optional] [default to False]
 **conflicts** | **bool**| Include &#x60;_conflicts&#x60; in docs; requires &#x60;include_docs&#x60;. | [optional] [default to False]
 **attachments** | **bool**|  | [optional] [default to False]
 **style** | **str**| &#x60;all_docs&#x60; returns all leaf revisions, not just the winner. | [optional] [default to main_only]
 **filter** | **str**| &#x60;_doc_ids&#x60;, &#x60;_selector&#x60;, &#x60;_design&#x60;, &#x60;_view&#x60; or &#x60;ddoc/filter&#x60;. | [optional] 
 **view** | **str**| &#x60;ddoc/view&#x60; used with &#x60;filter&#x3D;_view&#x60;. | [optional] 
 **doc_ids** | **str**| JSON array of ids, used with &#x60;filter&#x3D;_doc_ids&#x60;. | [optional] 
 **limit** | **int**|  | [optional] 
 **timeout** | **int**| Longpoll timeout in milliseconds | [optional] 
 **heartbeat** | **int**| Milliseconds between keep-alive newlines. | [optional] 
 **seq_interval** | **int**| Only compute &#x60;seq&#x60; every N rows; others are null. Faster on clusters. | [optional] 
 **descending** | **bool**|  | [optional] [default to False]

### Return type

[**ChangesResult**](ChangesResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Changes |  -  |
**400** | CouchDB error |  -  |
**404** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


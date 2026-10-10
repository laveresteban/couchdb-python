# couchdb_client.DatabasesApi

All URIs are relative to *http://localhost:5984*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_database**](DatabasesApi.md#delete_database) | **DELETE** /{db} | Delete a database
[**get_database_information**](DatabasesApi.md#get_database_information) | **GET** /{db} | Get database information
[**head_database**](DatabasesApi.md#head_database) | **HEAD** /{db} | Check database existence
[**put_database**](DatabasesApi.md#put_database) | **PUT** /{db} | Create a database


# **delete_database**
> Ok delete_database(db)

Delete a database

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.ok import Ok
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
    api_instance = couchdb_client.DatabasesApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.

    try:
        # Delete a database
        api_response = api_instance.delete_database(db)
        print("The response of DatabasesApi->delete_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->delete_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 

### Return type

[**Ok**](Ok.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Database deleted |  -  |
**202** | Database deleted, quorum not met |  -  |
**404** | CouchDB error |  -  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_information**
> DatabaseInformation get_database_information(db)

Get database information

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.database_information import DatabaseInformation
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
    api_instance = couchdb_client.DatabasesApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.

    try:
        # Get database information
        api_response = api_instance.get_database_information(db)
        print("The response of DatabasesApi->get_database_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 

### Return type

[**DatabaseInformation**](DatabaseInformation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Database information |  -  |
**404** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_database**
> head_database(db)

Check database existence

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
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
    api_instance = couchdb_client.DatabasesApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.

    try:
        # Check database existence
        api_instance.head_database(db)
    except Exception as e:
        print("Exception when calling DatabasesApi->head_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Database exists |  -  |
**404** | Database does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_database**
> Ok put_database(db, q=q, n=n, partitioned=partitioned)

Create a database

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.ok import Ok
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
    api_instance = couchdb_client.DatabasesApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.
    q = 56 # int | Number of shards (optional)
    n = 56 # int | Number of replicas (optional)
    partitioned = False # bool |  (optional) (default to False)

    try:
        # Create a database
        api_response = api_instance.put_database(db, q=q, n=n, partitioned=partitioned)
        print("The response of DatabasesApi->put_database:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->put_database: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 
 **q** | **int**| Number of shards | [optional] 
 **n** | **int**| Number of replicas | [optional] 
 **partitioned** | **bool**|  | [optional] [default to False]

### Return type

[**Ok**](Ok.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Database created |  -  |
**202** | Database created, quorum not met |  -  |
**400** | CouchDB error |  -  |
**401** | CouchDB error |  -  |
**412** | CouchDB error |  -  |
**403** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


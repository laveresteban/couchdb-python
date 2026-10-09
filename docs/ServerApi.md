# couchdb_client.ServerApi

All URIs are relative to *http://localhost:5984*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_dbs**](ServerApi.md#get_all_dbs) | **GET** /_all_dbs | List all databases
[**get_server_information**](ServerApi.md#get_server_information) | **GET** / | Server meta information
[**get_up**](ServerApi.md#get_up) | **GET** /_up | Health check
[**get_uuids**](ServerApi.md#get_uuids) | **GET** /_uuids | Request server-generated UUIDs


# **get_all_dbs**
> List[str] get_all_dbs(descending=descending, limit=limit, skip=skip)

List all databases

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
    api_instance = couchdb_client.ServerApi(api_client)
    descending = False # bool |  (optional) (default to False)
    limit = 56 # int |  (optional)
    skip = 0 # int |  (optional) (default to 0)

    try:
        # List all databases
        api_response = api_instance.get_all_dbs(descending=descending, limit=limit, skip=skip)
        print("The response of ServerApi->get_all_dbs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->get_all_dbs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **descending** | **bool**|  | [optional] [default to False]
 **limit** | **int**|  | [optional] 
 **skip** | **int**|  | [optional] [default to 0]

### Return type

**List[str]**

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Database names |  -  |
**401** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_information**
> ServerInformation get_server_information()

Server meta information

### Example


```python
import couchdb_client
from couchdb_client.models.server_information import ServerInformation
from couchdb_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5984
# See configuration.py for a list of all supported configuration parameters.
configuration = couchdb_client.Configuration(
    host = "http://localhost:5984"
)


# Enter a context with an instance of the API client
with couchdb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = couchdb_client.ServerApi(api_client)

    try:
        # Server meta information
        api_response = api_instance.get_server_information()
        print("The response of ServerApi->get_server_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->get_server_information: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ServerInformation**](ServerInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_up**
> UpInformation get_up()

Health check

### Example


```python
import couchdb_client
from couchdb_client.models.up_information import UpInformation
from couchdb_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5984
# See configuration.py for a list of all supported configuration parameters.
configuration = couchdb_client.Configuration(
    host = "http://localhost:5984"
)


# Enter a context with an instance of the API client
with couchdb_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = couchdb_client.ServerApi(api_client)

    try:
        # Health check
        api_response = api_instance.get_up()
        print("The response of ServerApi->get_up:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->get_up: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UpInformation**](UpInformation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server is up |  -  |
**404** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_uuids**
> UuidsResult get_uuids(count=count)

Request server-generated UUIDs

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.uuids_result import UuidsResult
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
    api_instance = couchdb_client.ServerApi(api_client)
    count = 1 # int |  (optional) (default to 1)

    try:
        # Request server-generated UUIDs
        api_response = api_instance.get_uuids(count=count)
        print("The response of ServerApi->get_uuids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServerApi->get_uuids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**|  | [optional] [default to 1]

### Return type

[**UuidsResult**](UuidsResult.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | UUIDs |  -  |
**401** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


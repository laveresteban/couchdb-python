# couchdb_client.AuthenticationApi

All URIs are relative to *http://localhost:5984*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_session**](AuthenticationApi.md#delete_session) | **DELETE** /_session | End the cookie session
[**get_session**](AuthenticationApi.md#get_session) | **GET** /_session | Get current session information
[**post_session**](AuthenticationApi.md#post_session) | **POST** /_session | Start a cookie session


# **delete_session**
> Ok delete_session()

End the cookie session

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
    api_instance = couchdb_client.AuthenticationApi(api_client)

    try:
        # End the cookie session
        api_response = api_instance.delete_session()
        print("The response of AuthenticationApi->delete_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->delete_session: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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
**200** | Session ended |  * X-Couch-Request-ID -  <br>  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_session**
> SessionInformation get_session()

Get current session information

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):

```python
import couchdb_client
from couchdb_client.models.session_information import SessionInformation
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
    api_instance = couchdb_client.AuthenticationApi(api_client)

    try:
        # Get current session information
        api_response = api_instance.get_session()
        print("The response of AuthenticationApi->get_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->get_session: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SessionInformation**](SessionInformation.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Session info |  * X-Couch-Request-ID -  <br>  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_session**
> SessionCreated post_session(session_request)

Start a cookie session

### Example


```python
import couchdb_client
from couchdb_client.models.session_created import SessionCreated
from couchdb_client.models.session_request import SessionRequest
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
    api_instance = couchdb_client.AuthenticationApi(api_client)
    session_request = couchdb_client.SessionRequest() # SessionRequest | 

    try:
        # Start a cookie session
        api_response = api_instance.post_session(session_request)
        print("The response of AuthenticationApi->post_session:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->post_session: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_request** | [**SessionRequest**](SessionRequest.md)|  | 

### Return type

[**SessionCreated**](SessionCreated.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Session created; AuthSession cookie is set |  * X-Couch-Request-ID -  <br>  |
**401** | CouchDB error |  -  |
**400** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


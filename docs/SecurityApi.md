# couchdb_client.SecurityApi

All URIs are relative to *http://localhost:5984*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_security**](SecurityApi.md#get_security) | **GET** /{db}/_security | Get the database security object
[**put_security**](SecurityApi.md#put_security) | **PUT** /{db}/_security | Replace the database security object


# **get_security**
> Security get_security(db)

Get the database security object

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import couchdb_client
from couchdb_client.models.security import Security
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
    api_instance = couchdb_client.SecurityApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.

    try:
        # Get the database security object
        api_response = api_instance.get_security(db)
        print("The response of SecurityApi->get_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->get_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 

### Return type

[**Security**](Security.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Security object |  -  |
**401** | CouchDB error |  -  |
**403** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_security**
> Ok put_security(db, security)

Replace the database security object

### Example

* Basic Authentication (basicAuth):
* Api Key Authentication (cookieAuth):
* Bearer (JWT) Authentication (bearerAuth):

```python
import couchdb_client
from couchdb_client.models.ok import Ok
from couchdb_client.models.security import Security
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
    api_instance = couchdb_client.SecurityApi(api_client)
    db = 'db_example' # str | Database name. System databases (`_users`, `_replicator`, ...) start with `_`.
    security = couchdb_client.Security() # Security | 

    try:
        # Replace the database security object
        api_response = api_instance.put_security(db, security)
        print("The response of SecurityApi->put_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->put_security: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db** | **str**| Database name. System databases (&#x60;_users&#x60;, &#x60;_replicator&#x60;, ...) start with &#x60;_&#x60;. | 
 **security** | [**Security**](Security.md)|  | 

### Return type

[**Ok**](Ok.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Security updated |  -  |
**401** | CouchDB error |  -  |
**400** | CouchDB error |  -  |
**403** | CouchDB error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


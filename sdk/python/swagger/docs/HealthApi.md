# swagger_client.HealthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_instance_metrics**](HealthApi.md#get_instance_metrics) | **GET** /health/metrics | Show instance metrics (experimental)
[**get_instance_status**](HealthApi.md#get_instance_status) | **GET** /health/status | Check health status of this instance


# **get_instance_metrics**
> get_instance_metrics()

Show instance metrics (experimental)

This endpoint returns an instance's metrics, such as average response time, status code distribution, hits per second and so on. The return values are currently not documented as this endpoint is still experimental.   The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:health:stats\"], \"actions\": [\"get\"], \"effect\": \"allow\" } ```

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.HealthApi()

try: 
    # Show instance metrics (experimental)
    api_instance.get_instance_metrics()
except ApiException as e:
    print("Exception when calling HealthApi->get_instance_metrics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_instance_status**
> InlineResponse200 get_instance_status()

Check health status of this instance

This endpoint returns `{ \"status\": \"ok\" }`. This status let's you know that the HTTP server is up and running. This status does currently not include checks whether the database connection is up and running. This endpoint does not require the `X-Forwarded-Proto` header when TLS termination is set.   Be aware that if you are running multiple nodes of ORY Hydra, the health status will never refer to the cluster state, only to a single instance.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HealthApi()

try: 
    # Check health status of this instance
    api_response = api_instance.get_instance_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HealthApi->get_instance_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


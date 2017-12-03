# swagger_client.PolicyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_policy**](PolicyApi.md#create_policy) | **POST** /policies | Create an Access Control Policy
[**delete_policy**](PolicyApi.md#delete_policy) | **DELETE** /policies/{id} | Delete an Access Control Policy
[**get_policy**](PolicyApi.md#get_policy) | **GET** /policies/{id} | Get an Access Control Policy
[**list_policies**](PolicyApi.md#list_policies) | **GET** /policies | List Access Control Policies
[**update_policy**](PolicyApi.md#update_policy) | **PUT** /policies/{id} | Update an Access Control Polic


# **create_policy**
> Policy create_policy(body=body)

Create an Access Control Policy

The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:policies\"], \"actions\": [\"create\"], \"effect\": \"allow\" } ```

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
api_instance = swagger_client.PolicyApi()
body = swagger_client.Policy() # Policy |  (optional)

try: 
    # Create an Access Control Policy
    api_response = api_instance.create_policy(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->create_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Policy**](Policy.md)|  | [optional] 

### Return type

[**Policy**](Policy.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_policy**
> delete_policy(id)

Delete an Access Control Policy

The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:policies:<id>\"], \"actions\": [\"delete\"], \"effect\": \"allow\" } ```

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
api_instance = swagger_client.PolicyApi()
id = 'id_example' # str | The id of the policy.

try: 
    # Delete an Access Control Policy
    api_instance.delete_policy(id)
except ApiException as e:
    print("Exception when calling PolicyApi->delete_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the policy. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_policy**
> Policy get_policy(id)

Get an Access Control Policy

The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:policies:<id>\"], \"actions\": [\"get\"], \"effect\": \"allow\" } ```

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
api_instance = swagger_client.PolicyApi()
id = 'id_example' # str | The id of the policy.

try: 
    # Get an Access Control Policy
    api_response = api_instance.get_policy(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->get_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the policy. | 

### Return type

[**Policy**](Policy.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_policies**
> list[Policy] list_policies(offset=offset, limit=limit)

List Access Control Policies

The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:policies\"], \"actions\": [\"list\"], \"effect\": \"allow\" } ```

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
api_instance = swagger_client.PolicyApi()
offset = 789 # int | The offset from where to start looking. (optional)
limit = 789 # int | The maximum amount of policies returned. (optional)

try: 
    # List Access Control Policies
    api_response = api_instance.list_policies(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->list_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The offset from where to start looking. | [optional] 
 **limit** | **int**| The maximum amount of policies returned. | [optional] 

### Return type

[**list[Policy]**](Policy.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_policy**
> Policy update_policy(id, body=body)

Update an Access Control Polic

The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:policies\"], \"actions\": [\"update\"], \"effect\": \"allow\" } ```

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
api_instance = swagger_client.PolicyApi()
id = 'id_example' # str | The id of the policy.
body = swagger_client.Policy() # Policy |  (optional)

try: 
    # Update an Access Control Polic
    api_response = api_instance.update_policy(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PolicyApi->update_policy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the policy. | 
 **body** | [**Policy**](Policy.md)|  | [optional] 

### Return type

[**Policy**](Policy.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


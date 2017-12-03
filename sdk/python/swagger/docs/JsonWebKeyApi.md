# swagger_client.JsonWebKeyApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_json_web_key_set**](JsonWebKeyApi.md#create_json_web_key_set) | **POST** /keys/{set} | Generate a new JSON Web Key
[**delete_json_web_key**](JsonWebKeyApi.md#delete_json_web_key) | **DELETE** /keys/{set}/{kid} | Delete a JSON Web Key
[**delete_json_web_key_set**](JsonWebKeyApi.md#delete_json_web_key_set) | **DELETE** /keys/{set} | Delete a JSON Web Key
[**get_json_web_key**](JsonWebKeyApi.md#get_json_web_key) | **GET** /keys/{set}/{kid} | Retrieve a JSON Web Key
[**get_json_web_key_set**](JsonWebKeyApi.md#get_json_web_key_set) | **GET** /keys/{set} | Retrieve a JSON Web Key Set
[**update_json_web_key**](JsonWebKeyApi.md#update_json_web_key) | **PUT** /keys/{set}/{kid} | Update a JSON Web Key
[**update_json_web_key_set**](JsonWebKeyApi.md#update_json_web_key_set) | **PUT** /keys/{set} | Update a JSON Web Key Set


# **create_json_web_key_set**
> JsonWebKeySet create_json_web_key_set(set, body=body)

Generate a new JSON Web Key

This endpoint is capable of generating JSON Web Key Sets for you. There a different strategies available, such as symmetric cryptographic keys (HS256, HS512) and asymetric cryptographic keys (RS256, ECDSA).   If the specified JSON Web Key Set does not exist, it will be created.   The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:keys:<set>:<kid>\"], \"actions\": [\"create\"], \"effect\": \"allow\" } ```

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
api_instance = swagger_client.JsonWebKeyApi()
set = 'set_example' # str | The set
body = swagger_client.JsonWebKeySetGeneratorRequest() # JsonWebKeySetGeneratorRequest |  (optional)

try: 
    # Generate a new JSON Web Key
    api_response = api_instance.create_json_web_key_set(set, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JsonWebKeyApi->create_json_web_key_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set** | **str**| The set | 
 **body** | [**JsonWebKeySetGeneratorRequest**](JsonWebKeySetGeneratorRequest.md)|  | [optional] 

### Return type

[**JsonWebKeySet**](JsonWebKeySet.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_json_web_key**
> delete_json_web_key(kid, set)

Delete a JSON Web Key

The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:keys:<set>:<kid>\"], \"actions\": [\"delete\"], \"effect\": \"allow\" } ```

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
api_instance = swagger_client.JsonWebKeyApi()
kid = 'kid_example' # str | The kid of the desired key
set = 'set_example' # str | The set

try: 
    # Delete a JSON Web Key
    api_instance.delete_json_web_key(kid, set)
except ApiException as e:
    print("Exception when calling JsonWebKeyApi->delete_json_web_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kid** | **str**| The kid of the desired key | 
 **set** | **str**| The set | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_json_web_key_set**
> delete_json_web_key_set(set)

Delete a JSON Web Key

The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:keys:<set>\"], \"actions\": [\"delete\"], \"effect\": \"allow\" } ```

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
api_instance = swagger_client.JsonWebKeyApi()
set = 'set_example' # str | The set

try: 
    # Delete a JSON Web Key
    api_instance.delete_json_web_key_set(set)
except ApiException as e:
    print("Exception when calling JsonWebKeyApi->delete_json_web_key_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set** | **str**| The set | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_json_web_key**
> JsonWebKeySet get_json_web_key(kid, set)

Retrieve a JSON Web Key

This endpoint can be used to retrieve JWKs stored in ORY Hydra.   The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:keys:<set>:<kid>\"], \"actions\": [\"get\"], \"effect\": \"allow\" } ```

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
api_instance = swagger_client.JsonWebKeyApi()
kid = 'kid_example' # str | The kid of the desired key
set = 'set_example' # str | The set

try: 
    # Retrieve a JSON Web Key
    api_response = api_instance.get_json_web_key(kid, set)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JsonWebKeyApi->get_json_web_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kid** | **str**| The kid of the desired key | 
 **set** | **str**| The set | 

### Return type

[**JsonWebKeySet**](JsonWebKeySet.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_json_web_key_set**
> JsonWebKeySet get_json_web_key_set(set)

Retrieve a JSON Web Key Set

This endpoint can be used to retrieve JWK Sets stored in ORY Hydra.   The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:keys:<set>:<kid>\"], \"actions\": [\"get\"], \"effect\": \"allow\" } ```

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
api_instance = swagger_client.JsonWebKeyApi()
set = 'set_example' # str | The set

try: 
    # Retrieve a JSON Web Key Set
    api_response = api_instance.get_json_web_key_set(set)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JsonWebKeyApi->get_json_web_key_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set** | **str**| The set | 

### Return type

[**JsonWebKeySet**](JsonWebKeySet.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_json_web_key**
> JsonWebKey update_json_web_key(kid, set, body=body)

Update a JSON Web Key

Use this method if you do not want to let Hydra generate the JWKs for you, but instead save your own.   The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:keys:<set>:<kid>\"], \"actions\": [\"update\"], \"effect\": \"allow\" } ```

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
api_instance = swagger_client.JsonWebKeyApi()
kid = 'kid_example' # str | The kid of the desired key
set = 'set_example' # str | The set
body = swagger_client.JsonWebKey() # JsonWebKey |  (optional)

try: 
    # Update a JSON Web Key
    api_response = api_instance.update_json_web_key(kid, set, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JsonWebKeyApi->update_json_web_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kid** | **str**| The kid of the desired key | 
 **set** | **str**| The set | 
 **body** | [**JsonWebKey**](JsonWebKey.md)|  | [optional] 

### Return type

[**JsonWebKey**](JsonWebKey.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_json_web_key_set**
> JsonWebKeySet update_json_web_key_set(set, body=body)

Update a JSON Web Key Set

Use this method if you do not want to let Hydra generate the JWKs for you, but instead save your own.   The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:keys:<set>\"], \"actions\": [\"update\"], \"effect\": \"allow\" } ```

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
api_instance = swagger_client.JsonWebKeyApi()
set = 'set_example' # str | The set
body = swagger_client.JsonWebKeySet() # JsonWebKeySet |  (optional)

try: 
    # Update a JSON Web Key Set
    api_response = api_instance.update_json_web_key_set(set, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JsonWebKeyApi->update_json_web_key_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set** | **str**| The set | 
 **body** | [**JsonWebKeySet**](JsonWebKeySet.md)|  | [optional] 

### Return type

[**JsonWebKeySet**](JsonWebKeySet.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


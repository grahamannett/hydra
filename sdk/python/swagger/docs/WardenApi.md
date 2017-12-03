# swagger_client.WardenApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_members_to_group**](WardenApi.md#add_members_to_group) | **POST** /warden/groups/{id}/members | Add members to a group
[**create_group**](WardenApi.md#create_group) | **POST** /warden/groups | Create a group
[**delete_group**](WardenApi.md#delete_group) | **DELETE** /warden/groups/{id} | Delete a group by id
[**does_warden_allow_access_request**](WardenApi.md#does_warden_allow_access_request) | **POST** /warden/allowed | Check if an access request is valid (without providing an access token)
[**does_warden_allow_token_access_request**](WardenApi.md#does_warden_allow_token_access_request) | **POST** /warden/token/allowed | Check if an access request is valid (providing an access token)
[**find_groups_by_member**](WardenApi.md#find_groups_by_member) | **GET** /warden/groups | Find groups by member
[**get_group**](WardenApi.md#get_group) | **GET** /warden/groups/{id} | Get a group by id
[**remove_members_from_group**](WardenApi.md#remove_members_from_group) | **DELETE** /warden/groups/{id}/members | Remove members from a group


# **add_members_to_group**
> add_members_to_group(id, body=body)

Add members to a group

The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:warden:groups:<id>\"], \"actions\": [\"members.add\"], \"effect\": \"allow\" } ```

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
api_instance = swagger_client.WardenApi()
id = 'id_example' # str | The id of the group to modify.
body = swagger_client.GroupMembers() # GroupMembers |  (optional)

try: 
    # Add members to a group
    api_instance.add_members_to_group(id, body=body)
except ApiException as e:
    print("Exception when calling WardenApi->add_members_to_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the group to modify. | 
 **body** | [**GroupMembers**](GroupMembers.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> Group create_group(body=body)

Create a group

The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:warden:groups\"], \"actions\": [\"create\"], \"effect\": \"allow\" } ```

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
api_instance = swagger_client.WardenApi()
body = swagger_client.Group() # Group |  (optional)

try: 
    # Create a group
    api_response = api_instance.create_group(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WardenApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Group**](Group.md)|  | [optional] 

### Return type

[**Group**](Group.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(id)

Delete a group by id

The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:warden:groups:<id>\"], \"actions\": [\"delete\"], \"effect\": \"allow\" } ```

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
api_instance = swagger_client.WardenApi()
id = 'id_example' # str | The id of the group to look up.

try: 
    # Delete a group by id
    api_instance.delete_group(id)
except ApiException as e:
    print("Exception when calling WardenApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the group to look up. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **does_warden_allow_access_request**
> WardenAccessRequestResponse does_warden_allow_access_request(body=body)

Check if an access request is valid (without providing an access token)

Checks if a subject (typically a user or a service) is allowed to perform an action on a resource. This endpoint requires a subject, a resource name, an action name and a context. If the subject is not allowed to perform the action on the resource, this endpoint returns a 200 response with `{ \"allowed\": false}`, otherwise `{ \"allowed\": true }` is returned.   The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:warden:allowed\"], \"actions\": [\"decide\"], \"effect\": \"allow\" } ```

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
api_instance = swagger_client.WardenApi()
body = swagger_client.WardenAccessRequest() # WardenAccessRequest |  (optional)

try: 
    # Check if an access request is valid (without providing an access token)
    api_response = api_instance.does_warden_allow_access_request(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WardenApi->does_warden_allow_access_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WardenAccessRequest**](WardenAccessRequest.md)|  | [optional] 

### Return type

[**WardenAccessRequestResponse**](WardenAccessRequestResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **does_warden_allow_token_access_request**
> WardenTokenAccessRequestResponse does_warden_allow_token_access_request(body=body)

Check if an access request is valid (providing an access token)

Checks if a token is valid and if the token subject is allowed to perform an action on a resource. This endpoint requires a token, a scope, a resource name, an action name and a context.   If a token is expired/invalid, has not been granted the requested scope or the subject is not allowed to perform the action on the resource, this endpoint returns a 200 response with `{ \"allowed\": false}`.   Extra data set through the `accessTokenExtra` field in the consent flow will be included in the response.   The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:warden:token:allowed\"], \"actions\": [\"decide\"], \"effect\": \"allow\" } ```

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
api_instance = swagger_client.WardenApi()
body = swagger_client.WardenTokenAccessRequest() # WardenTokenAccessRequest |  (optional)

try: 
    # Check if an access request is valid (providing an access token)
    api_response = api_instance.does_warden_allow_token_access_request(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WardenApi->does_warden_allow_token_access_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WardenTokenAccessRequest**](WardenTokenAccessRequest.md)|  | [optional] 

### Return type

[**WardenTokenAccessRequestResponse**](WardenTokenAccessRequestResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_groups_by_member**
> list[Group] find_groups_by_member(member)

Find groups by member

The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:warden:groups\"], \"actions\": [\"list\"], \"effect\": \"allow\" } ```

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
api_instance = swagger_client.WardenApi()
member = 'member_example' # str | The id of the member to look up.

try: 
    # Find groups by member
    api_response = api_instance.find_groups_by_member(member)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WardenApi->find_groups_by_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member** | **str**| The id of the member to look up. | 

### Return type

[**list[Group]**](Group.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> Group get_group(id)

Get a group by id

The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:warden:groups:<id>\"], \"actions\": [\"create\"], \"effect\": \"allow\" } ```

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
api_instance = swagger_client.WardenApi()
id = 'id_example' # str | The id of the group to look up.

try: 
    # Get a group by id
    api_response = api_instance.get_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WardenApi->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the group to look up. | 

### Return type

[**Group**](Group.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_members_from_group**
> remove_members_from_group(id, body=body)

Remove members from a group

The subject making the request needs to be assigned to a policy containing:  ``` { \"resources\": [\"rn:hydra:warden:groups:<id>\"], \"actions\": [\"members.remove\"], \"effect\": \"allow\" } ```

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
api_instance = swagger_client.WardenApi()
id = 'id_example' # str | The id of the group to modify.
body = swagger_client.GroupMembers() # GroupMembers |  (optional)

try: 
    # Remove members from a group
    api_instance.remove_members_from_group(id, body=body)
except ApiException as e:
    print("Exception when calling WardenApi->remove_members_from_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the group to modify. | 
 **body** | [**GroupMembers**](GroupMembers.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


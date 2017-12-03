# ConsentRequestAcceptance

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token_extra** | **dict(str, object)** | AccessTokenExtra represents arbitrary data that will be added to the access token and that will be returned on introspection and warden requests. | [optional] 
**grant_scopes** | **list[str]** | A list of scopes that the user agreed to grant. It should be a subset of requestedScopes from the consent request. | [optional] 
**id_token_extra** | **dict(str, object)** | IDTokenExtra represents arbitrary data that will be added to the ID token. The ID token will only be issued if the user agrees to it and if the client requested an ID token. | [optional] 
**subject** | **str** | Subject represents a unique identifier of the user (or service, or legal entity, ...) that accepted the OAuth2 request. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



import typing

import typing_extensions

_list = list

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListParameterVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    parameterVersions: _list[ParameterVersion]
    unreachable: _list[str]

@typing.type_check_only
class ListParametersResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    parameters: _list[Parameter]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Parameter(typing_extensions.TypedDict, total=False):
    createTime: str
    format: typing_extensions.Literal[
        "PARAMETER_FORMAT_UNSPECIFIED", "UNFORMATTED", "YAML", "JSON"
    ]
    kmsKey: str
    labels: dict[str, typing.Any]
    name: str
    policyMember: ResourcePolicyMember
    updateTime: str

@typing.type_check_only
class ParameterVersion(typing_extensions.TypedDict, total=False):
    createTime: str
    disabled: bool
    kmsKeyVersion: str
    name: str
    payload: ParameterVersionPayload
    updateTime: str

@typing.type_check_only
class ParameterVersionPayload(typing_extensions.TypedDict, total=False):
    data: str

@typing.type_check_only
class RenderParameterVersionResponse(typing_extensions.TypedDict, total=False):
    parameterVersion: str
    payload: ParameterVersionPayload
    renderedPayload: str

@typing.type_check_only
class ResourcePolicyMember(typing_extensions.TypedDict, total=False):
    iamPolicyNamePrincipal: str
    iamPolicyUidPrincipal: str

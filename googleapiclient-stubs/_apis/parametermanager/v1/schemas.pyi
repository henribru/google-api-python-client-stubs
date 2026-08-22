import typing

_list = list

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListParameterVersionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    parameterVersions: _list[ParameterVersion]
    unreachable: _list[str]

@typing.type_check_only
class ListParametersResponse(typing.TypedDict, total=False):
    nextPageToken: str
    parameters: _list[Parameter]
    unreachable: _list[str]

@typing.type_check_only
class ListTemplateVersionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    templateVersions: _list[TemplateVersion]
    unreachable: _list[str]

@typing.type_check_only
class ListTemplatesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    templates: _list[Template]
    unreachable: _list[str]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Parameter(typing.TypedDict, total=False):
    createTime: str
    format: typing.Literal[
        "PARAMETER_FORMAT_UNSPECIFIED", "UNFORMATTED", "YAML", "JSON"
    ]
    kmsKey: str
    labels: dict[str, typing.Any]
    name: str
    policyMember: ResourcePolicyMember
    updateTime: str

@typing.type_check_only
class ParameterVersion(typing.TypedDict, total=False):
    createTime: str
    disabled: bool
    kmsKeyVersion: str
    name: str
    payload: ParameterVersionPayload
    updateTime: str

@typing.type_check_only
class ParameterVersionPayload(typing.TypedDict, total=False):
    data: str

@typing.type_check_only
class RenderParameterVersionResponse(typing.TypedDict, total=False):
    parameterVersion: str
    payload: ParameterVersionPayload
    renderedPayload: str

@typing.type_check_only
class RenderTemplateVersionResponse(typing.TypedDict, total=False):
    parameterVersion: str
    payload: TemplateVersionPayload
    renderedPayload: str
    templateFormat: typing.Literal[
        "TEMPLATE_FORMAT_UNSPECIFIED", "TEMPLATE_FORMAT_YAML", "TEMPLATE_FORMAT_JSON"
    ]
    templateVersion: str

@typing.type_check_only
class ResourcePolicyMember(typing.TypedDict, total=False):
    iamPolicyNamePrincipal: str
    iamPolicyUidPrincipal: str

@typing.type_check_only
class Template(typing.TypedDict, total=False):
    createTime: str
    format: typing.Literal[
        "TEMPLATE_FORMAT_UNSPECIFIED", "TEMPLATE_FORMAT_YAML", "TEMPLATE_FORMAT_JSON"
    ]
    labels: dict[str, typing.Any]
    name: str
    updateTime: str

@typing.type_check_only
class TemplateVersion(typing.TypedDict, total=False):
    createTime: str
    disabled: bool
    name: str
    payload: TemplateVersionPayload
    updateTime: str

@typing.type_check_only
class TemplateVersionPayload(typing.TypedDict, total=False):
    data: str

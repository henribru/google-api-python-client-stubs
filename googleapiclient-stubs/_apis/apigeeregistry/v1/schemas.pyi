import typing

_list = list

@typing.type_check_only
class Api(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    availability: str
    createTime: str
    description: str
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    recommendedDeployment: str
    recommendedVersion: str
    updateTime: str

@typing.type_check_only
class ApiDeployment(typing.TypedDict, total=False):
    accessGuidance: str
    annotations: dict[str, typing.Any]
    apiSpecRevision: str
    createTime: str
    description: str
    displayName: str
    endpointUri: str
    externalChannelUri: str
    intendedAudience: str
    labels: dict[str, typing.Any]
    name: str
    revisionCreateTime: str
    revisionId: str
    revisionUpdateTime: str

@typing.type_check_only
class ApiSpec(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    contents: str
    createTime: str
    description: str
    filename: str
    hash: str
    labels: dict[str, typing.Any]
    mimeType: str
    name: str
    revisionCreateTime: str
    revisionId: str
    revisionUpdateTime: str
    sizeBytes: int
    sourceUri: str

@typing.type_check_only
class ApiVersion(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    description: str
    displayName: str
    labels: dict[str, typing.Any]
    name: str
    primarySpec: str
    state: str
    updateTime: str

@typing.type_check_only
class Artifact(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    contents: str
    createTime: str
    hash: str
    labels: dict[str, typing.Any]
    mimeType: str
    name: str
    sizeBytes: int
    updateTime: str

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Build(typing.TypedDict, total=False):
    commitId: str
    commitTime: str
    repo: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class Config(typing.TypedDict, total=False):
    cmekKeyName: str
    location: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class HttpBody(typing.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class Instance(typing.TypedDict, total=False):
    build: Build
    config: Config
    createTime: str
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "INACTIVE",
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "DELETING",
        "FAILED",
    ]
    stateMessage: str
    updateTime: str

@typing.type_check_only
class ListApiDeploymentRevisionsResponse(typing.TypedDict, total=False):
    apiDeployments: _list[ApiDeployment]
    nextPageToken: str

@typing.type_check_only
class ListApiDeploymentsResponse(typing.TypedDict, total=False):
    apiDeployments: _list[ApiDeployment]
    nextPageToken: str

@typing.type_check_only
class ListApiSpecRevisionsResponse(typing.TypedDict, total=False):
    apiSpecs: _list[ApiSpec]
    nextPageToken: str

@typing.type_check_only
class ListApiSpecsResponse(typing.TypedDict, total=False):
    apiSpecs: _list[ApiSpec]
    nextPageToken: str

@typing.type_check_only
class ListApiVersionsResponse(typing.TypedDict, total=False):
    apiVersions: _list[ApiVersion]
    nextPageToken: str

@typing.type_check_only
class ListApisResponse(typing.TypedDict, total=False):
    apis: _list[Api]
    nextPageToken: str

@typing.type_check_only
class ListArtifactsResponse(typing.TypedDict, total=False):
    artifacts: _list[Artifact]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiVersion: str
    cancellationRequested: bool
    createTime: str
    endTime: str
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class RollbackApiDeploymentRequest(typing.TypedDict, total=False):
    revisionId: str

@typing.type_check_only
class RollbackApiSpecRequest(typing.TypedDict, total=False):
    revisionId: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TagApiDeploymentRevisionRequest(typing.TypedDict, total=False):
    tag: str

@typing.type_check_only
class TagApiSpecRevisionRequest(typing.TypedDict, total=False):
    tag: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

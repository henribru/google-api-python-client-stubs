import typing

import typing_extensions

class ListFilesResponse(typing_extensions.TypedDict, total=False):
    files: typing.List[File]
    nextPageToken: str

class Tag(typing_extensions.TypedDict, total=False):
    name: str
    version: str

class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    bindingId: str
    members: typing.List[str]
    role: str

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class Package(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    updateTime: str
    createTime: str

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy

class Version(typing_extensions.TypedDict, total=False):
    description: str
    updateTime: str
    relatedTags: typing.List[Tag]
    name: str
    createTime: str

class GoogleDevtoolsArtifactregistryV1alpha1ImportArtifactsResponse(
    typing_extensions.TypedDict, total=False
):
    packages: typing.List[GoogleDevtoolsArtifactregistryV1alpha1Package]
    errors: typing.List[GoogleDevtoolsArtifactregistryV1alpha1ErrorInfo]

class ListPackagesResponse(typing_extensions.TypedDict, total=False):
    packages: typing.List[Package]
    nextPageToken: str

class GoogleDevtoolsArtifactregistryV1alpha1Package(
    typing_extensions.TypedDict, total=False
):
    updateTime: str
    displayName: str
    name: str
    createTime: str

class ListTagsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tags: typing.List[Tag]

class ListRepositoriesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    repositories: typing.List[Repository]

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class File(typing_extensions.TypedDict, total=False):
    hashes: typing.List[Hash]
    updateTime: str
    sizeBytes: str
    name: str
    owner: str
    createTime: str

class Empty(typing_extensions.TypedDict, total=False): ...

class GoogleDevtoolsArtifactregistryV1alpha1ErrorInfo(
    typing_extensions.TypedDict, total=False
):
    error: Status
    gcsSource: GoogleDevtoolsArtifactregistryV1alpha1GcsSource

class GoogleDevtoolsArtifactregistryV1alpha1GcsSource(
    typing_extensions.TypedDict, total=False
):
    uris: typing.List[str]

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

class Repository(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    updateTime: str
    description: str
    kmsKeyName: str
    createTime: str
    name: str
    format: typing_extensions.Literal[
        "FORMAT_UNSPECIFIED", "DOCKER", "MAVEN", "NPM", "APT"
    ]

class Status(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]

class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    name: str
    metadata: typing.Dict[str, typing.Any]
    locationId: str
    labels: typing.Dict[str, typing.Any]

class Hash(typing_extensions.TypedDict, total=False):
    value: str
    type: typing_extensions.Literal["HASH_TYPE_UNSPECIFIED", "SHA256"]

class Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[Binding]
    version: int
    etag: str

class Expr(typing_extensions.TypedDict, total=False):
    expression: str
    description: str
    location: str
    title: str

class ListVersionsResponse(typing_extensions.TypedDict, total=False):
    versions: typing.List[Version]
    nextPageToken: str

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

class Operation(typing_extensions.TypedDict, total=False):
    name: str
    metadata: typing.Dict[str, typing.Any]
    error: Status
    response: typing.Dict[str, typing.Any]
    done: bool

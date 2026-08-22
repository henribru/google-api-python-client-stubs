import typing

_list = list

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class File(typing.TypedDict, total=False):
    createTime: str
    hashes: _list[Hash]
    name: str
    owner: str
    sizeBytes: str
    updateTime: str

@typing.type_check_only
class Hash(typing.TypedDict, total=False):
    type: typing.Literal["HASH_TYPE_UNSPECIFIED", "SHA256", "MD5", "DIRSUM_SHA256"]
    value: str

@typing.type_check_only
class ListFilesResponse(typing.TypedDict, total=False):
    files: _list[File]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListPackagesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    packages: _list[Package]

@typing.type_check_only
class ListRepositoriesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    repositories: _list[Repository]

@typing.type_check_only
class ListTagsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tags: _list[Tag]

@typing.type_check_only
class ListVersionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    versions: _list[Version]

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
class Package(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    name: str
    updateTime: str

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class Repository(typing.TypedDict, total=False):
    createTime: str
    description: str
    format: typing.Literal[
        "FORMAT_UNSPECIFIED", "DOCKER", "MAVEN", "NPM", "APT", "YUM", "GOOGET", "PYTHON"
    ]
    kmsKeyName: str
    labels: dict[str, typing.Any]
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    sizeBytes: str
    updateTime: str

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class Tag(typing.TypedDict, total=False):
    name: str
    version: str

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class Version(typing.TypedDict, total=False):
    createTime: str
    description: str
    name: str
    relatedTags: _list[Tag]
    updateTime: str

import typing

import typing_extensions

_list = list

@typing.type_check_only
class AdvanceRelocateBucketOperationRequest(typing_extensions.TypedDict, total=False):
    expireTime: str
    ttl: str

@typing.type_check_only
class AnywhereCache(typing_extensions.TypedDict, total=False):
    admissionPolicy: str
    anywhereCacheId: str
    bucket: str
    createTime: str
    id: str
    kind: str
    pendingUpdate: bool
    selfLink: str
    state: str
    ttl: str
    updateTime: str
    zone: str

@typing.type_check_only
class AnywhereCaches(typing_extensions.TypedDict, total=False):
    items: _list[AnywhereCache]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Bucket(typing_extensions.TypedDict, total=False):
    acl: _list[BucketAccessControl]
    autoclass: dict[str, typing.Any]
    billing: dict[str, typing.Any]
    cors: _list[dict[str, typing.Any]]
    customPlacementConfig: dict[str, typing.Any]
    defaultEventBasedHold: bool
    defaultObjectAcl: _list[ObjectAccessControl]
    encryption: dict[str, typing.Any]
    etag: str
    generation: str
    hardDeleteTime: str
    hierarchicalNamespace: dict[str, typing.Any]
    iamConfiguration: dict[str, typing.Any]
    id: str
    ipFilter: dict[str, typing.Any]
    kind: str
    labels: dict[str, typing.Any]
    lifecycle: dict[str, typing.Any]
    location: str
    locationType: str
    logging: dict[str, typing.Any]
    metageneration: str
    name: str
    objectRetention: dict[str, typing.Any]
    owner: dict[str, typing.Any]
    projectNumber: str
    retentionPolicy: dict[str, typing.Any]
    rpo: str
    satisfiesPZI: bool
    satisfiesPZS: bool
    selfLink: str
    softDeletePolicy: dict[str, typing.Any]
    softDeleteTime: str
    storageClass: str
    timeCreated: str
    updated: str
    versioning: dict[str, typing.Any]
    website: dict[str, typing.Any]

@typing.type_check_only
class BucketAccessControl(typing_extensions.TypedDict, total=False):
    bucket: str
    domain: str
    email: str
    entity: str
    entityId: str
    etag: str
    id: str
    kind: str
    projectTeam: dict[str, typing.Any]
    role: str
    selfLink: str

@typing.type_check_only
class BucketAccessControls(typing_extensions.TypedDict, total=False):
    items: _list[BucketAccessControl]
    kind: str

@typing.type_check_only
class BucketStorageLayout(typing_extensions.TypedDict, total=False):
    bucket: str
    customPlacementConfig: dict[str, typing.Any]
    hierarchicalNamespace: dict[str, typing.Any]
    kind: str
    location: str
    locationType: str

@typing.type_check_only
class Buckets(typing_extensions.TypedDict, total=False):
    items: _list[Bucket]
    kind: str
    nextPageToken: str

@typing.type_check_only
class BulkRestoreObjectsRequest(typing_extensions.TypedDict, total=False):
    allowOverwrite: bool
    copySourceAcl: bool
    matchGlobs: _list[str]
    softDeletedAfterTime: str
    softDeletedBeforeTime: str

@typing.type_check_only
class Channel(typing_extensions.TypedDict, total=False):
    address: str
    expiration: str
    id: str
    kind: str
    params: dict[str, typing.Any]
    payload: bool
    resourceId: str
    resourceUri: str
    token: str
    type: str

@typing.type_check_only
class ComposeRequest(typing_extensions.TypedDict, total=False):
    destination: Object
    kind: str
    sourceObjects: _list[dict[str, typing.Any]]

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Folder(typing_extensions.TypedDict, total=False):
    bucket: str
    createTime: str
    id: str
    kind: str
    metageneration: str
    name: str
    pendingRenameInfo: dict[str, typing.Any]
    selfLink: str
    updateTime: str

@typing.type_check_only
class Folders(typing_extensions.TypedDict, total=False):
    items: _list[Folder]
    kind: str
    nextPageToken: str

@typing.type_check_only
class GoogleLongrunningListOperationsResponse(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    operations: _list[GoogleLongrunningOperation]

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: GoogleRpcStatus
    kind: str
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]
    selfLink: str

@typing.type_check_only
class GoogleRpcStatus(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class HmacKey(typing_extensions.TypedDict, total=False):
    kind: str
    metadata: HmacKeyMetadata
    secret: str

@typing.type_check_only
class HmacKeyMetadata(typing_extensions.TypedDict, total=False):
    accessId: str
    etag: str
    id: str
    kind: str
    projectId: str
    selfLink: str
    serviceAccountEmail: str
    state: str
    timeCreated: str
    updated: str

@typing.type_check_only
class HmacKeysMetadata(typing_extensions.TypedDict, total=False):
    items: _list[HmacKeyMetadata]
    kind: str
    nextPageToken: str

@typing.type_check_only
class ManagedFolder(typing_extensions.TypedDict, total=False):
    bucket: str
    createTime: str
    id: str
    kind: str
    metageneration: str
    name: str
    selfLink: str
    updateTime: str

@typing.type_check_only
class ManagedFolders(typing_extensions.TypedDict, total=False):
    items: _list[ManagedFolder]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Notification(typing_extensions.TypedDict, total=False):
    custom_attributes: dict[str, typing.Any]
    etag: str
    event_types: _list[str]
    id: str
    kind: str
    object_name_prefix: str
    payload_format: str
    selfLink: str
    topic: str

@typing.type_check_only
class Notifications(typing_extensions.TypedDict, total=False):
    items: _list[Notification]
    kind: str

@typing.type_check_only
class Object(typing_extensions.TypedDict, total=False):
    acl: _list[ObjectAccessControl]
    bucket: str
    cacheControl: str
    componentCount: int
    contentDisposition: str
    contentEncoding: str
    contentLanguage: str
    contentType: str
    crc32c: str
    customTime: str
    customerEncryption: dict[str, typing.Any]
    etag: str
    eventBasedHold: bool
    generation: str
    hardDeleteTime: str
    id: str
    kind: str
    kmsKeyName: str
    md5Hash: str
    mediaLink: str
    metadata: dict[str, typing.Any]
    metageneration: str
    name: str
    owner: dict[str, typing.Any]
    restoreToken: str
    retention: dict[str, typing.Any]
    retentionExpirationTime: str
    selfLink: str
    size: str
    softDeleteTime: str
    storageClass: str
    temporaryHold: bool
    timeCreated: str
    timeDeleted: str
    timeFinalized: str
    timeStorageClassUpdated: str
    updated: str

@typing.type_check_only
class ObjectAccessControl(typing_extensions.TypedDict, total=False):
    bucket: str
    domain: str
    email: str
    entity: str
    entityId: str
    etag: str
    generation: str
    id: str
    kind: str
    object: str
    projectTeam: dict[str, typing.Any]
    role: str
    selfLink: str

@typing.type_check_only
class ObjectAccessControls(typing_extensions.TypedDict, total=False):
    items: _list[ObjectAccessControl]
    kind: str

@typing.type_check_only
class Objects(typing_extensions.TypedDict, total=False):
    items: _list[Object]
    kind: str
    nextPageToken: str
    prefixes: _list[str]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: _list[dict[str, typing.Any]]
    etag: str
    kind: str
    resourceId: str
    version: int

@typing.type_check_only
class RelocateBucketRequest(typing_extensions.TypedDict, total=False):
    destinationCustomPlacementConfig: dict[str, typing.Any]
    destinationLocation: str
    validateOnly: bool

@typing.type_check_only
class RewriteResponse(typing_extensions.TypedDict, total=False):
    done: bool
    kind: str
    objectSize: str
    resource: Object
    rewriteToken: str
    totalBytesRewritten: str

@typing.type_check_only
class ServiceAccount(typing_extensions.TypedDict, total=False):
    email_address: str
    kind: str

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    kind: str
    permissions: _list[str]

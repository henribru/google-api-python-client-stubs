import typing

import typing_extensions
@typing.type_check_only
class Bucket(typing_extensions.TypedDict, total=False):
    acl: typing.List[BucketAccessControl]
    billing: typing.Dict[str, typing.Any]
    cors: typing.List[typing.Dict[str, typing.Any]]
    defaultEventBasedHold: bool
    defaultObjectAcl: typing.List[ObjectAccessControl]
    encryption: typing.Dict[str, typing.Any]
    etag: str
    iamConfiguration: typing.Dict[str, typing.Any]
    id: str
    kind: str
    labels: typing.Dict[str, typing.Any]
    lifecycle: typing.Dict[str, typing.Any]
    location: str
    locationType: str
    logging: typing.Dict[str, typing.Any]
    metageneration: str
    name: str
    owner: typing.Dict[str, typing.Any]
    projectNumber: str
    retentionPolicy: typing.Dict[str, typing.Any]
    satisfiesPZS: bool
    selfLink: str
    storageClass: str
    timeCreated: str
    updated: str
    versioning: typing.Dict[str, typing.Any]
    website: typing.Dict[str, typing.Any]
    zoneAffinity: typing.List[str]

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
    projectTeam: typing.Dict[str, typing.Any]
    role: str
    selfLink: str

@typing.type_check_only
class BucketAccessControls(typing_extensions.TypedDict, total=False):
    items: typing.List[BucketAccessControl]
    kind: str

@typing.type_check_only
class Buckets(typing_extensions.TypedDict, total=False):
    items: typing.List[Bucket]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Channel(typing_extensions.TypedDict, total=False):
    address: str
    expiration: str
    id: str
    kind: str
    params: typing.Dict[str, typing.Any]
    payload: bool
    resourceId: str
    resourceUri: str
    token: str
    type: str

@typing.type_check_only
class ComposeRequest(typing_extensions.TypedDict, total=False):
    destination: Object
    kind: str
    sourceObjects: typing.List[typing.Dict[str, typing.Any]]

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

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
    items: typing.List[HmacKeyMetadata]
    kind: str
    nextPageToken: str

@typing.type_check_only
class Notification(typing_extensions.TypedDict, total=False):
    custom_attributes: typing.Dict[str, typing.Any]
    etag: str
    event_types: typing.List[str]
    id: str
    kind: str
    object_name_prefix: str
    payload_format: str
    selfLink: str
    topic: str

@typing.type_check_only
class Notifications(typing_extensions.TypedDict, total=False):
    items: typing.List[Notification]
    kind: str

@typing.type_check_only
class Object(typing_extensions.TypedDict, total=False):
    acl: typing.List[ObjectAccessControl]
    bucket: str
    cacheControl: str
    componentCount: int
    contentDisposition: str
    contentEncoding: str
    contentLanguage: str
    contentType: str
    crc32c: str
    customTime: str
    customerEncryption: typing.Dict[str, typing.Any]
    etag: str
    eventBasedHold: bool
    generation: str
    id: str
    kind: str
    kmsKeyName: str
    md5Hash: str
    mediaLink: str
    metadata: typing.Dict[str, typing.Any]
    metageneration: str
    name: str
    owner: typing.Dict[str, typing.Any]
    retentionExpirationTime: str
    selfLink: str
    size: str
    storageClass: str
    temporaryHold: bool
    timeCreated: str
    timeDeleted: str
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
    projectTeam: typing.Dict[str, typing.Any]
    role: str
    selfLink: str

@typing.type_check_only
class ObjectAccessControls(typing_extensions.TypedDict, total=False):
    items: typing.List[ObjectAccessControl]
    kind: str

@typing.type_check_only
class Objects(typing_extensions.TypedDict, total=False):
    items: typing.List[Object]
    kind: str
    nextPageToken: str
    prefixes: typing.List[str]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    bindings: typing.List[typing.Dict[str, typing.Any]]
    etag: str
    kind: str
    resourceId: str
    version: int

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
    permissions: typing.List[str]

import typing

_list = list

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class V2AndroidApplication(typing.TypedDict, total=False):
    packageName: str
    sha1Fingerprint: str

@typing.type_check_only
class V2AndroidKeyRestrictions(typing.TypedDict, total=False):
    allowedApplications: _list[V2AndroidApplication]

@typing.type_check_only
class V2ApiTarget(typing.TypedDict, total=False):
    methods: _list[str]
    service: str

@typing.type_check_only
class V2BrowserKeyRestrictions(typing.TypedDict, total=False):
    allowedReferrers: _list[str]

@typing.type_check_only
class V2GetKeyStringResponse(typing.TypedDict, total=False):
    keyString: str

@typing.type_check_only
class V2IosKeyRestrictions(typing.TypedDict, total=False):
    allowedBundleIds: _list[str]

@typing.type_check_only
class V2Key(typing.TypedDict, total=False):
    annotations: dict[str, typing.Any]
    createTime: str
    deleteTime: str
    displayName: str
    etag: str
    keyString: str
    name: str
    restrictions: V2Restrictions
    serviceAccountEmail: str
    uid: str
    updateTime: str

@typing.type_check_only
class V2ListKeysResponse(typing.TypedDict, total=False):
    keys: _list[V2Key]
    nextPageToken: str

@typing.type_check_only
class V2LookupKeyResponse(typing.TypedDict, total=False):
    name: str
    parent: str

@typing.type_check_only
class V2Restrictions(typing.TypedDict, total=False):
    androidKeyRestrictions: V2AndroidKeyRestrictions
    apiTargets: _list[V2ApiTarget]
    browserKeyRestrictions: V2BrowserKeyRestrictions
    iosKeyRestrictions: V2IosKeyRestrictions
    serverKeyRestrictions: V2ServerKeyRestrictions

@typing.type_check_only
class V2ServerKeyRestrictions(typing.TypedDict, total=False):
    allowedIps: _list[str]

@typing.type_check_only
class V2UndeleteKeyRequest(typing.TypedDict, total=False): ...

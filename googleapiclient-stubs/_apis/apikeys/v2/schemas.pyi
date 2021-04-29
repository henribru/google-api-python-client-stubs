import typing

import typing_extensions

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class V2AndroidApplication(typing_extensions.TypedDict, total=False):
    packageName: str
    sha1Fingerprint: str

@typing.type_check_only
class V2AndroidKeyRestrictions(typing_extensions.TypedDict, total=False):
    allowedApplications: typing.List[V2AndroidApplication]

@typing.type_check_only
class V2ApiTarget(typing_extensions.TypedDict, total=False):
    methods: typing.List[str]
    service: str

@typing.type_check_only
class V2BrowserKeyRestrictions(typing_extensions.TypedDict, total=False):
    allowedReferrers: typing.List[str]

@typing.type_check_only
class V2CloneKeyRequest(typing_extensions.TypedDict, total=False):
    keyId: str

@typing.type_check_only
class V2GetKeyStringResponse(typing_extensions.TypedDict, total=False):
    keyString: str

@typing.type_check_only
class V2IosKeyRestrictions(typing_extensions.TypedDict, total=False):
    allowedBundleIds: typing.List[str]

@typing.type_check_only
class V2Key(typing_extensions.TypedDict, total=False):
    createTime: str
    deleteTime: str
    displayName: str
    etag: str
    keyString: str
    name: str
    restrictions: V2Restrictions
    uid: str
    updateTime: str

@typing.type_check_only
class V2ListKeysResponse(typing_extensions.TypedDict, total=False):
    keys: typing.List[V2Key]
    nextPageToken: str

@typing.type_check_only
class V2LookupKeyResponse(typing_extensions.TypedDict, total=False):
    name: str
    parent: str

@typing.type_check_only
class V2Restrictions(typing_extensions.TypedDict, total=False):
    androidKeyRestrictions: V2AndroidKeyRestrictions
    apiTargets: typing.List[V2ApiTarget]
    browserKeyRestrictions: V2BrowserKeyRestrictions
    iosKeyRestrictions: V2IosKeyRestrictions
    serverKeyRestrictions: V2ServerKeyRestrictions

@typing.type_check_only
class V2ServerKeyRestrictions(typing_extensions.TypedDict, total=False):
    allowedIps: typing.List[str]

@typing.type_check_only
class V2UndeleteKeyRequest(typing_extensions.TypedDict, total=False): ...

import typing

import typing_extensions

_list = list

@typing.type_check_only
class AdminUser(typing_extensions.TypedDict, total=False):
    familyName: str
    givenName: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ContactCenter(typing_extensions.TypedDict, total=False):
    adminUser: AdminUser
    ccaipManagedUsers: bool
    createTime: str
    customerDomainPrefix: str
    displayName: str
    instanceConfig: InstanceConfig
    kmsKey: str
    labels: dict[str, typing.Any]
    name: str
    samlParams: SAMLParams
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "STATE_DEPLOYING",
        "STATE_DEPLOYED",
        "STATE_TERMINATING",
        "STATE_FAILED",
        "STATE_TERMINATING_FAILED",
        "STATE_TERMINATED",
        "STATE_IN_GRACE_PERIOD",
    ]
    updateTime: str
    uris: URIs
    userEmail: str

@typing.type_check_only
class ContactCenterQuota(typing_extensions.TypedDict, total=False):
    contactCenterCountLimit: int
    contactCenterCountSum: int
    quotas: _list[Quota]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleCloudCommonOperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class InstanceConfig(typing_extensions.TypedDict, total=False):
    instanceSize: typing_extensions.Literal[
        "INSTANCE_SIZE_UNSPECIFIED",
        "STANDARD_SMALL",
        "STANDARD_MEDIUM",
        "STANDARD_LARGE",
        "STANDARD_XLARGE",
        "STANDARD_2XLARGE",
        "STANDARD_3XLARGE",
        "DEV_XSMALL",
    ]

@typing.type_check_only
class ListContactCentersResponse(typing_extensions.TypedDict, total=False):
    contactCenters: _list[ContactCenter]
    nextPageToken: str
    unreachable: _list[str]

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    contactCenter: ContactCenter
    createTime: str
    endTime: str
    requestedCancellation: bool
    statusMessage: str
    target: str
    verb: str

@typing.type_check_only
class Quota(typing_extensions.TypedDict, total=False):
    contactCenterCountLimit: int
    contactCenterCountSum: int
    contactCenterInstanceSize: typing_extensions.Literal[
        "INSTANCE_SIZE_UNSPECIFIED",
        "STANDARD_SMALL",
        "STANDARD_MEDIUM",
        "STANDARD_LARGE",
        "STANDARD_XLARGE",
        "STANDARD_2XLARGE",
        "STANDARD_3XLARGE",
        "DEV_XSMALL",
    ]

@typing.type_check_only
class SAMLParams(typing_extensions.TypedDict, total=False):
    certificate: str
    emailMapping: str
    entityId: str
    ssoUri: str
    userEmail: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class URIs(typing_extensions.TypedDict, total=False):
    chatBotUri: str
    mediaUri: str
    rootUri: str
    virtualAgentStreamingServiceUri: str

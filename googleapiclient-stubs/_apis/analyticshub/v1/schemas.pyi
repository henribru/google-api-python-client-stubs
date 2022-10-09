import typing

import typing_extensions

_list = list

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class BigQueryDatasetSource(typing_extensions.TypedDict, total=False):
    dataset: str

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class DataExchange(typing_extensions.TypedDict, total=False):
    description: str
    displayName: str
    documentation: str
    icon: str
    listingCount: int
    name: str
    primaryContact: str

@typing.type_check_only
class DataProvider(typing_extensions.TypedDict, total=False):
    name: str
    primaryContact: str

@typing.type_check_only
class DestinationDataset(typing_extensions.TypedDict, total=False):
    datasetReference: DestinationDatasetReference
    description: str
    friendlyName: str
    labels: dict[str, typing.Any]
    location: str

@typing.type_check_only
class DestinationDatasetReference(typing_extensions.TypedDict, total=False):
    datasetId: str
    projectId: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class GetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    options: GetPolicyOptions

@typing.type_check_only
class GetPolicyOptions(typing_extensions.TypedDict, total=False):
    requestedPolicyVersion: int

@typing.type_check_only
class ListDataExchangesResponse(typing_extensions.TypedDict, total=False):
    dataExchanges: _list[DataExchange]
    nextPageToken: str

@typing.type_check_only
class ListListingsResponse(typing_extensions.TypedDict, total=False):
    listings: _list[Listing]
    nextPageToken: str

@typing.type_check_only
class ListOrgDataExchangesResponse(typing_extensions.TypedDict, total=False):
    dataExchanges: _list[DataExchange]
    nextPageToken: str

@typing.type_check_only
class Listing(typing_extensions.TypedDict, total=False):
    bigqueryDataset: BigQueryDatasetSource
    categories: _list[str]
    dataProvider: DataProvider
    description: str
    displayName: str
    documentation: str
    icon: str
    name: str
    primaryContact: str
    publisher: Publisher
    requestAccess: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE"]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiVersion: str
    cancelRequested: bool
    createTime: str
    endTime: str
    statusDetail: str
    target: str
    verb: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class Publisher(typing_extensions.TypedDict, total=False):
    name: str
    primaryContact: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class SubscribeListingRequest(typing_extensions.TypedDict, total=False):
    destinationDataset: DestinationDataset

@typing.type_check_only
class SubscribeListingResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

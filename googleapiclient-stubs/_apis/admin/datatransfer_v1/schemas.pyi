import typing

_list = list

@typing.type_check_only
class Application(typing.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    name: str
    transferParams: _list[ApplicationTransferParam]

@typing.type_check_only
class ApplicationDataTransfer(typing.TypedDict, total=False):
    applicationId: str
    applicationTransferParams: _list[ApplicationTransferParam]
    applicationTransferStatus: str

@typing.type_check_only
class ApplicationTransferParam(typing.TypedDict, total=False):
    key: str
    value: _list[str]

@typing.type_check_only
class ApplicationsListResponse(typing.TypedDict, total=False):
    applications: _list[Application]
    etag: str
    kind: str
    nextPageToken: str

@typing.type_check_only
class DataTransfer(typing.TypedDict, total=False):
    applicationDataTransfers: _list[ApplicationDataTransfer]
    etag: str
    id: str
    kind: str
    newOwnerUserId: str
    oldOwnerUserId: str
    overallTransferStatusCode: str
    requestTime: str

@typing.type_check_only
class DataTransfersListResponse(typing.TypedDict, total=False):
    dataTransfers: _list[DataTransfer]
    etag: str
    kind: str
    nextPageToken: str

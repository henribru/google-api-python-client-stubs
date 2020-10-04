import typing

import typing_extensions
@typing.type_check_only
class Application(typing_extensions.TypedDict, total=False):
    etag: str
    id: str
    kind: str
    name: str
    transferParams: typing.List[ApplicationTransferParam]

@typing.type_check_only
class ApplicationDataTransfer(typing_extensions.TypedDict, total=False):
    applicationId: str
    applicationTransferParams: typing.List[ApplicationTransferParam]
    applicationTransferStatus: str

@typing.type_check_only
class ApplicationTransferParam(typing_extensions.TypedDict, total=False):
    key: str
    value: typing.List[str]

@typing.type_check_only
class ApplicationsListResponse(typing_extensions.TypedDict, total=False):
    applications: typing.List[Application]
    etag: str
    kind: str
    nextPageToken: str

@typing.type_check_only
class DataTransfer(typing_extensions.TypedDict, total=False):
    applicationDataTransfers: typing.List[ApplicationDataTransfer]
    etag: str
    id: str
    kind: str
    newOwnerUserId: str
    oldOwnerUserId: str
    overallTransferStatusCode: str
    requestTime: str

@typing.type_check_only
class DataTransfersListResponse(typing_extensions.TypedDict, total=False):
    dataTransfers: typing.List[DataTransfer]
    etag: str
    kind: str
    nextPageToken: str

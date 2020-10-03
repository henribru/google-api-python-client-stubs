import typing

import typing_extensions

class DataTransfersListResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    dataTransfers: typing.List[DataTransfer]
    etag: str
    kind: str

class ApplicationDataTransfer(typing_extensions.TypedDict, total=False):
    applicationId: str
    applicationTransferStatus: str
    applicationTransferParams: typing.List[ApplicationTransferParam]

class ApplicationTransferParam(typing_extensions.TypedDict, total=False):
    key: str
    value: typing.List[str]

class Application(typing_extensions.TypedDict, total=False):
    kind: str
    etag: str
    id: str
    transferParams: typing.List[ApplicationTransferParam]
    name: str

class ApplicationsListResponse(typing_extensions.TypedDict, total=False):
    etag: str
    nextPageToken: str
    applications: typing.List[Application]
    kind: str

class DataTransfer(typing_extensions.TypedDict, total=False):
    newOwnerUserId: str
    etag: str
    applicationDataTransfers: typing.List[ApplicationDataTransfer]
    overallTransferStatusCode: str
    kind: str
    id: str
    oldOwnerUserId: str
    requestTime: str

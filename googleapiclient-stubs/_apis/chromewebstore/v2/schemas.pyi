import typing

_list = list

@typing.type_check_only
class CancelSubmissionRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CancelSubmissionResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeployInfo(typing.TypedDict, total=False):
    deployPercentage: int

@typing.type_check_only
class DistributionChannel(typing.TypedDict, total=False):
    crxVersion: str
    deployPercentage: int

@typing.type_check_only
class FetchItemStatusResponse(typing.TypedDict, total=False):
    itemId: str
    lastAsyncUploadState: typing.Literal[
        "UPLOAD_STATE_UNSPECIFIED", "SUCCEEDED", "IN_PROGRESS", "FAILED", "NOT_FOUND"
    ]
    name: str
    publicKey: str
    publishedItemRevisionStatus: ItemRevisionStatus
    submittedItemRevisionStatus: ItemRevisionStatus
    takenDown: bool
    warned: bool

@typing.type_check_only
class ItemRevisionStatus(typing.TypedDict, total=False):
    distributionChannels: _list[DistributionChannel]
    state: typing.Literal[
        "ITEM_STATE_UNSPECIFIED",
        "PENDING_REVIEW",
        "STAGED",
        "PUBLISHED",
        "PUBLISHED_TO_TESTERS",
        "REJECTED",
        "CANCELLED",
    ]

@typing.type_check_only
class PublishItemRequest(typing.TypedDict, total=False):
    blockOnWarnings: bool
    deployInfos: _list[DeployInfo]
    publishType: typing.Literal[
        "PUBLISH_TYPE_UNSPECIFIED", "DEFAULT_PUBLISH", "STAGED_PUBLISH"
    ]
    skipReview: bool

@typing.type_check_only
class PublishItemResponse(typing.TypedDict, total=False):
    itemId: str
    name: str
    state: typing.Literal[
        "ITEM_STATE_UNSPECIFIED",
        "PENDING_REVIEW",
        "STAGED",
        "PUBLISHED",
        "PUBLISHED_TO_TESTERS",
        "REJECTED",
        "CANCELLED",
    ]
    warningInfo: WarningsInfo

@typing.type_check_only
class SetPublishedDeployPercentageRequest(typing.TypedDict, total=False):
    deployPercentage: int

@typing.type_check_only
class SetPublishedDeployPercentageResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class UploadItemPackageRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UploadItemPackageResponse(typing.TypedDict, total=False):
    crxVersion: str
    itemId: str
    name: str
    uploadState: typing.Literal[
        "UPLOAD_STATE_UNSPECIFIED", "SUCCEEDED", "IN_PROGRESS", "FAILED", "NOT_FOUND"
    ]

@typing.type_check_only
class Warning(typing.TypedDict, total=False):
    description: str
    reason: str

@typing.type_check_only
class WarningsInfo(typing.TypedDict, total=False):
    warnings: _list[Warning]

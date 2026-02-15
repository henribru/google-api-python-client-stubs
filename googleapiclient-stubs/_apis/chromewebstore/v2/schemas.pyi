import typing

import typing_extensions

_list = list

@typing.type_check_only
class CancelSubmissionRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CancelSubmissionResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeployInfo(typing_extensions.TypedDict, total=False):
    deployPercentage: int

@typing.type_check_only
class DistributionChannel(typing_extensions.TypedDict, total=False):
    crxVersion: str
    deployPercentage: int

@typing.type_check_only
class FetchItemStatusResponse(typing_extensions.TypedDict, total=False):
    itemId: str
    lastAsyncUploadState: typing_extensions.Literal[
        "UPLOAD_STATE_UNSPECIFIED", "SUCCEEDED", "IN_PROGRESS", "FAILED", "NOT_FOUND"
    ]
    name: str
    publicKey: str
    publishedItemRevisionStatus: ItemRevisionStatus
    submittedItemRevisionStatus: ItemRevisionStatus
    takenDown: bool
    warned: bool

@typing.type_check_only
class ItemRevisionStatus(typing_extensions.TypedDict, total=False):
    distributionChannels: _list[DistributionChannel]
    state: typing_extensions.Literal[
        "ITEM_STATE_UNSPECIFIED",
        "PENDING_REVIEW",
        "STAGED",
        "PUBLISHED",
        "PUBLISHED_TO_TESTERS",
        "REJECTED",
        "CANCELLED",
    ]

@typing.type_check_only
class PublishItemRequest(typing_extensions.TypedDict, total=False):
    deployInfos: _list[DeployInfo]
    publishType: typing_extensions.Literal[
        "PUBLISH_TYPE_UNSPECIFIED", "DEFAULT_PUBLISH", "STAGED_PUBLISH"
    ]
    skipReview: bool

@typing.type_check_only
class PublishItemResponse(typing_extensions.TypedDict, total=False):
    itemId: str
    name: str
    state: typing_extensions.Literal[
        "ITEM_STATE_UNSPECIFIED",
        "PENDING_REVIEW",
        "STAGED",
        "PUBLISHED",
        "PUBLISHED_TO_TESTERS",
        "REJECTED",
        "CANCELLED",
    ]

@typing.type_check_only
class SetPublishedDeployPercentageRequest(typing_extensions.TypedDict, total=False):
    deployPercentage: int

@typing.type_check_only
class SetPublishedDeployPercentageResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class UploadItemPackageRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UploadItemPackageResponse(typing_extensions.TypedDict, total=False):
    crxVersion: str
    itemId: str
    name: str
    uploadState: typing_extensions.Literal[
        "UPLOAD_STATE_UNSPECIFIED", "SUCCEEDED", "IN_PROGRESS", "FAILED", "NOT_FOUND"
    ]

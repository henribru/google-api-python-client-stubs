import typing

import typing_extensions

_list = list

@typing.type_check_only
class ClickTag(typing_extensions.TypedDict, total=False):
    clickThroughUrl: CreativeClickThroughUrl
    eventName: str
    name: str

@typing.type_check_only
class CreativeAssetId(typing_extensions.TypedDict, total=False):
    name: str
    type: typing_extensions.Literal[
        "IMAGE", "FLASH", "VIDEO", "HTML", "HTML_IMAGE", "AUDIO"
    ]

@typing.type_check_only
class CreativeAssetMetadata(typing_extensions.TypedDict, total=False):
    assetIdentifier: CreativeAssetId
    clickTags: _list[ClickTag]
    counterCustomEvents: _list[CreativeCustomEvent]
    detectedFeatures: _list[str]
    exitCustomEvents: _list[CreativeCustomEvent]
    id: str
    idDimensionValue: DimensionValue
    kind: str
    mediaRequestInfo: MediaRequestInfo
    mediaResponseInfo: MediaResponseInfo
    richMedia: bool
    timerCustomEvents: _list[CreativeCustomEvent]
    warnedValidationRules: _list[str]

@typing.type_check_only
class CreativeClickThroughUrl(typing_extensions.TypedDict, total=False):
    computedClickThroughUrl: str
    customClickThroughUrl: str
    landingPageId: str

@typing.type_check_only
class CreativeCustomEvent(typing_extensions.TypedDict, total=False):
    advertiserCustomEventId: str
    advertiserCustomEventName: str
    advertiserCustomEventType: typing_extensions.Literal[
        "ADVERTISER_EVENT_TIMER", "ADVERTISER_EVENT_EXIT", "ADVERTISER_EVENT_COUNTER"
    ]
    artworkLabel: str
    artworkType: typing_extensions.Literal[
        "ARTWORK_TYPE_FLASH",
        "ARTWORK_TYPE_HTML5",
        "ARTWORK_TYPE_MIXED",
        "ARTWORK_TYPE_IMAGE",
    ]
    exitClickThroughUrl: CreativeClickThroughUrl
    id: str
    popupWindowProperties: PopupWindowProperties
    targetType: typing_extensions.Literal[
        "TARGET_BLANK", "TARGET_TOP", "TARGET_SELF", "TARGET_PARENT", "TARGET_POPUP"
    ]
    videoReportingId: str

@typing.type_check_only
class DimensionValue(typing_extensions.TypedDict, total=False):
    dimensionName: str
    etag: str
    id: str
    kind: str
    matchType: typing_extensions.Literal[
        "EXACT", "BEGINS_WITH", "CONTAINS", "WILDCARD_EXPRESSION"
    ]
    value: str

@typing.type_check_only
class MediaRequestInfo(typing_extensions.TypedDict, total=False):
    currentBytes: str
    customData: str
    diffObjectVersion: str
    finalStatus: int
    notificationType: typing_extensions.Literal[
        "START", "PROGRESS", "END", "RESPONSE_SENT", "ERROR"
    ]
    requestId: str
    requestReceivedParamsServingInfo: str
    totalBytes: str
    totalBytesIsEstimated: bool

@typing.type_check_only
class MediaResponseInfo(typing_extensions.TypedDict, total=False):
    customData: str
    dataStorageTransform: str
    dynamicDropTarget: str
    dynamicDropzone: str
    requestClass: typing_extensions.Literal[
        "UNKNOWN_REQUEST_CLASS", "LATENCY_SENSITIVE", "PRODUCTION_BATCH", "BEST_EFFORT"
    ]
    scottyAgentUserId: str
    scottyCustomerLog: str
    trafficClassField: typing_extensions.Literal[
        "BE1", "AF1", "AF2", "AF3", "AF4", "NC1", "NC0", "BE0", "LLQ", "LLQ1", "LLQ2"
    ]
    verifyHashFromHeader: bool

@typing.type_check_only
class OffsetPosition(typing_extensions.TypedDict, total=False):
    left: int
    top: int

@typing.type_check_only
class PopupWindowProperties(typing_extensions.TypedDict, total=False):
    dimension: Size
    offset: OffsetPosition
    positionType: typing_extensions.Literal["CENTER", "COORDINATES"]
    showAddressBar: bool
    showMenuBar: bool
    showScrollBar: bool
    showStatusBar: bool
    showToolBar: bool
    title: str

@typing.type_check_only
class Size(typing_extensions.TypedDict, total=False):
    height: int
    iab: bool
    id: str
    kind: str
    width: int

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
    detectedFeatures: _list[
        typing_extensions.Literal[
            "CSS_FONT_FACE",
            "CSS_BACKGROUND_SIZE",
            "CSS_BORDER_IMAGE",
            "CSS_BORDER_RADIUS",
            "CSS_BOX_SHADOW",
            "CSS_FLEX_BOX",
            "CSS_HSLA",
            "CSS_MULTIPLE_BGS",
            "CSS_OPACITY",
            "CSS_RGBA",
            "CSS_TEXT_SHADOW",
            "CSS_ANIMATIONS",
            "CSS_COLUMNS",
            "CSS_GENERATED_CONTENT",
            "CSS_GRADIENTS",
            "CSS_REFLECTIONS",
            "CSS_TRANSFORMS",
            "CSS_TRANSFORMS3D",
            "CSS_TRANSITIONS",
            "APPLICATION_CACHE",
            "CANVAS",
            "CANVAS_TEXT",
            "DRAG_AND_DROP",
            "HASH_CHANGE",
            "HISTORY",
            "AUDIO",
            "VIDEO",
            "INDEXED_DB",
            "INPUT_ATTR_AUTOCOMPLETE",
            "INPUT_ATTR_AUTOFOCUS",
            "INPUT_ATTR_LIST",
            "INPUT_ATTR_PLACEHOLDER",
            "INPUT_ATTR_MAX",
            "INPUT_ATTR_MIN",
            "INPUT_ATTR_MULTIPLE",
            "INPUT_ATTR_PATTERN",
            "INPUT_ATTR_REQUIRED",
            "INPUT_ATTR_STEP",
            "INPUT_TYPE_SEARCH",
            "INPUT_TYPE_TEL",
            "INPUT_TYPE_URL",
            "INPUT_TYPE_EMAIL",
            "INPUT_TYPE_DATETIME",
            "INPUT_TYPE_DATE",
            "INPUT_TYPE_MONTH",
            "INPUT_TYPE_WEEK",
            "INPUT_TYPE_TIME",
            "INPUT_TYPE_DATETIME_LOCAL",
            "INPUT_TYPE_NUMBER",
            "INPUT_TYPE_RANGE",
            "INPUT_TYPE_COLOR",
            "LOCAL_STORAGE",
            "POST_MESSAGE",
            "SESSION_STORAGE",
            "WEB_SOCKETS",
            "WEB_SQL_DATABASE",
            "WEB_WORKERS",
            "GEO_LOCATION",
            "INLINE_SVG",
            "SMIL",
            "SVG_HREF",
            "SVG_CLIP_PATHS",
            "TOUCH",
            "WEBGL",
            "SVG_FILTERS",
            "SVG_FE_IMAGE",
        ]
    ]
    exitCustomEvents: _list[CreativeCustomEvent]
    id: str
    idDimensionValue: DimensionValue
    kind: str
    richMedia: bool
    timerCustomEvents: _list[CreativeCustomEvent]
    warnedValidationRules: _list[
        typing_extensions.Literal[
            "CLICK_TAG_NON_TOP_LEVEL",
            "CLICK_TAG_MISSING",
            "CLICK_TAG_MORE_THAN_ONE",
            "CLICK_TAG_INVALID",
            "ORPHANED_ASSET",
            "PRIMARY_HTML_MISSING",
            "EXTERNAL_FILE_REFERENCED",
            "MRAID_REFERENCED",
            "ADMOB_REFERENCED",
            "FILE_TYPE_INVALID",
            "ZIP_INVALID",
            "LINKED_FILE_NOT_FOUND",
            "MAX_FLASH_VERSION_11",
            "NOT_SSL_COMPLIANT",
            "FILE_DETAIL_EMPTY",
            "ASSET_INVALID",
            "GWD_PROPERTIES_INVALID",
            "ENABLER_UNSUPPORTED_METHOD_DCM",
            "ASSET_FORMAT_UNSUPPORTED_DCM",
            "COMPONENT_UNSUPPORTED_DCM",
            "HTML5_FEATURE_UNSUPPORTED",
            "CLICK_TAG_IN_GWD",
            "CLICK_TAG_HARD_CODED",
            "SVG_INVALID",
            "CLICK_TAG_IN_RICH_MEDIA",
            "MISSING_ENABLER_REFERENCE",
        ]
    ]

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

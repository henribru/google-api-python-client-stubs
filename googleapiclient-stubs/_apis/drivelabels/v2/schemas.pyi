import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleAppsDriveLabelsV2BadgeColors(typing_extensions.TypedDict, total=False):
    backgroundColor: GoogleTypeColor
    foregroundColor: GoogleTypeColor
    soloColor: GoogleTypeColor

@typing.type_check_only
class GoogleAppsDriveLabelsV2BadgeConfig(typing_extensions.TypedDict, total=False):
    color: GoogleTypeColor
    priorityOverride: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2Field(typing_extensions.TypedDict, total=False):
    appliedCapabilities: GoogleAppsDriveLabelsV2FieldAppliedCapabilities
    createTime: str
    creator: GoogleAppsDriveLabelsV2UserInfo
    dateOptions: GoogleAppsDriveLabelsV2FieldDateOptions
    disableTime: str
    disabler: GoogleAppsDriveLabelsV2UserInfo
    displayHints: GoogleAppsDriveLabelsV2FieldDisplayHints
    id: str
    integerOptions: GoogleAppsDriveLabelsV2FieldIntegerOptions
    lifecycle: GoogleAppsDriveLabelsV2Lifecycle
    lockStatus: GoogleAppsDriveLabelsV2LockStatus
    properties: GoogleAppsDriveLabelsV2FieldProperties
    publisher: GoogleAppsDriveLabelsV2UserInfo
    queryKey: str
    schemaCapabilities: GoogleAppsDriveLabelsV2FieldSchemaCapabilities
    selectionOptions: GoogleAppsDriveLabelsV2FieldSelectionOptions
    textOptions: GoogleAppsDriveLabelsV2FieldTextOptions
    updateTime: str
    updater: GoogleAppsDriveLabelsV2UserInfo
    userOptions: GoogleAppsDriveLabelsV2FieldUserOptions

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldAppliedCapabilities(
    typing_extensions.TypedDict, total=False
):
    canRead: bool
    canSearch: bool
    canWrite: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldDateOptions(typing_extensions.TypedDict, total=False):
    dateFormat: str
    dateFormatType: typing_extensions.Literal[
        "DATE_FORMAT_UNSPECIFIED", "LONG_DATE", "SHORT_DATE"
    ]
    maxValue: GoogleTypeDate
    minValue: GoogleTypeDate

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldDisplayHints(
    typing_extensions.TypedDict, total=False
):
    disabled: bool
    hiddenInSearch: bool
    required: bool
    shownInApply: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldIntegerOptions(
    typing_extensions.TypedDict, total=False
):
    maxValue: str
    minValue: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldListOptions(typing_extensions.TypedDict, total=False):
    maxEntries: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldProperties(typing_extensions.TypedDict, total=False):
    displayName: str
    insertBeforeField: str
    required: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldSchemaCapabilities(
    typing_extensions.TypedDict, total=False
):
    canDelete: bool
    canDisable: bool
    canEnable: bool
    canUpdate: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldSelectionOptions(
    typing_extensions.TypedDict, total=False
):
    choices: _list[GoogleAppsDriveLabelsV2FieldSelectionOptionsChoice]
    listOptions: GoogleAppsDriveLabelsV2FieldListOptions

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldSelectionOptionsChoice(
    typing_extensions.TypedDict, total=False
):
    appliedCapabilities: GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceAppliedCapabilities
    createTime: str
    creator: GoogleAppsDriveLabelsV2UserInfo
    disableTime: str
    disabler: GoogleAppsDriveLabelsV2UserInfo
    displayHints: GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHints
    id: str
    lifecycle: GoogleAppsDriveLabelsV2Lifecycle
    lockStatus: GoogleAppsDriveLabelsV2LockStatus
    properties: GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceProperties
    publishTime: str
    publisher: GoogleAppsDriveLabelsV2UserInfo
    schemaCapabilities: GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceSchemaCapabilities
    updateTime: str
    updater: GoogleAppsDriveLabelsV2UserInfo

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceAppliedCapabilities(
    typing_extensions.TypedDict, total=False
):
    canRead: bool
    canSearch: bool
    canSelect: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHints(
    typing_extensions.TypedDict, total=False
):
    badgeColors: GoogleAppsDriveLabelsV2BadgeColors
    badgePriority: str
    darkBadgeColors: GoogleAppsDriveLabelsV2BadgeColors
    disabled: bool
    hiddenInSearch: bool
    shownInApply: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceProperties(
    typing_extensions.TypedDict, total=False
):
    badgeConfig: GoogleAppsDriveLabelsV2BadgeConfig
    description: str
    displayName: str
    insertBeforeChoice: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceSchemaCapabilities(
    typing_extensions.TypedDict, total=False
):
    canDelete: bool
    canDisable: bool
    canEnable: bool
    canUpdate: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldTextOptions(typing_extensions.TypedDict, total=False):
    maxLength: int
    minLength: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldUserOptions(typing_extensions.TypedDict, total=False):
    listOptions: GoogleAppsDriveLabelsV2FieldListOptions

@typing.type_check_only
class GoogleAppsDriveLabelsV2Label(typing_extensions.TypedDict, total=False):
    appliedCapabilities: GoogleAppsDriveLabelsV2LabelAppliedCapabilities
    appliedLabelPolicy: GoogleAppsDriveLabelsV2LabelAppliedLabelPolicy
    createTime: str
    creator: GoogleAppsDriveLabelsV2UserInfo
    disableTime: str
    disabler: GoogleAppsDriveLabelsV2UserInfo
    displayHints: GoogleAppsDriveLabelsV2LabelDisplayHints
    fields: _list[GoogleAppsDriveLabelsV2Field]
    id: str
    labelType: typing_extensions.Literal["LABEL_TYPE_UNSPECIFIED", "SHARED", "ADMIN"]
    learnMoreUri: str
    lifecycle: GoogleAppsDriveLabelsV2Lifecycle
    lockStatus: GoogleAppsDriveLabelsV2LockStatus
    name: str
    properties: GoogleAppsDriveLabelsV2LabelProperties
    publishTime: str
    publisher: GoogleAppsDriveLabelsV2UserInfo
    revisionCreateTime: str
    revisionCreator: GoogleAppsDriveLabelsV2UserInfo
    revisionId: str
    schemaCapabilities: GoogleAppsDriveLabelsV2LabelSchemaCapabilities

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelAppliedCapabilities(
    typing_extensions.TypedDict, total=False
):
    canApply: bool
    canRead: bool
    canRemove: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelAppliedLabelPolicy(
    typing_extensions.TypedDict, total=False
):
    copyMode: typing_extensions.Literal[
        "COPY_MODE_UNSPECIFIED", "DO_NOT_COPY", "ALWAYS_COPY", "COPY_APPLIABLE"
    ]

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelDisplayHints(
    typing_extensions.TypedDict, total=False
):
    disabled: bool
    hiddenInSearch: bool
    priority: str
    shownInApply: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelProperties(typing_extensions.TypedDict, total=False):
    description: str
    title: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelSchemaCapabilities(
    typing_extensions.TypedDict, total=False
):
    canDelete: bool
    canDisable: bool
    canEnable: bool
    canUpdate: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2Lifecycle(typing_extensions.TypedDict, total=False):
    disabledPolicy: GoogleAppsDriveLabelsV2LifecycleDisabledPolicy
    hasUnpublishedChanges: bool
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "UNPUBLISHED_DRAFT", "PUBLISHED", "DISABLED", "DELETED"
    ]

@typing.type_check_only
class GoogleAppsDriveLabelsV2LifecycleDisabledPolicy(
    typing_extensions.TypedDict, total=False
):
    hideInSearch: bool
    showInApply: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2ListLabelsResponse(
    typing_extensions.TypedDict, total=False
):
    labels: _list[GoogleAppsDriveLabelsV2Label]
    nextPageToken: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2LockStatus(typing_extensions.TypedDict, total=False):
    locked: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2UserInfo(typing_extensions.TypedDict, total=False):
    person: str

@typing.type_check_only
class GoogleTypeColor(typing_extensions.TypedDict, total=False):
    alpha: float
    blue: float
    green: float
    red: float

@typing.type_check_only
class GoogleTypeDate(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

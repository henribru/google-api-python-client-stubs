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
class GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleAppsDriveLabelsV2DeleteLabelPermissionRequest]
    useAdminAccess: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequest(
    typing_extensions.TypedDict, total=False
):
    requests: _list[GoogleAppsDriveLabelsV2UpdateLabelPermissionRequest]
    useAdminAccess: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsResponse(
    typing_extensions.TypedDict, total=False
):
    permissions: _list[GoogleAppsDriveLabelsV2LabelPermission]

@typing.type_check_only
class GoogleAppsDriveLabelsV2DateLimits(typing_extensions.TypedDict, total=False):
    maxValue: GoogleTypeDate
    minValue: GoogleTypeDate

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeleteLabelPermissionRequest(
    typing_extensions.TypedDict, total=False
):
    name: str
    useAdminAccess: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequest(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    requests: _list[GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequest]
    useAdminAccess: bool
    view: typing_extensions.Literal["LABEL_VIEW_BASIC", "LABEL_VIEW_FULL"]
    writeControl: GoogleAppsDriveLabelsV2WriteControl

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateFieldRequest(
    typing_extensions.TypedDict, total=False
):
    field: GoogleAppsDriveLabelsV2Field

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateSelectionChoiceRequest(
    typing_extensions.TypedDict, total=False
):
    choice: GoogleAppsDriveLabelsV2FieldSelectionOptionsChoice
    fieldId: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteFieldRequest(
    typing_extensions.TypedDict, total=False
):
    id: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteSelectionChoiceRequest(
    typing_extensions.TypedDict, total=False
):
    fieldId: str
    id: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequest(
    typing_extensions.TypedDict, total=False
):
    disabledPolicy: GoogleAppsDriveLabelsV2LifecycleDisabledPolicy
    id: str
    updateMask: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableSelectionChoiceRequest(
    typing_extensions.TypedDict, total=False
):
    disabledPolicy: GoogleAppsDriveLabelsV2LifecycleDisabledPolicy
    fieldId: str
    id: str
    updateMask: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableFieldRequest(
    typing_extensions.TypedDict, total=False
):
    id: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableSelectionChoiceRequest(
    typing_extensions.TypedDict, total=False
):
    fieldId: str
    id: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequest(
    typing_extensions.TypedDict, total=False
):
    createField: GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateFieldRequest
    createSelectionChoice: (
        GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateSelectionChoiceRequest
    )
    deleteField: GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteFieldRequest
    deleteSelectionChoice: (
        GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteSelectionChoiceRequest
    )
    disableField: GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequest
    disableSelectionChoice: (
        GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableSelectionChoiceRequest
    )
    enableField: GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableFieldRequest
    enableSelectionChoice: (
        GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableSelectionChoiceRequest
    )
    updateField: (
        GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldPropertiesRequest
    )
    updateFieldType: (
        GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldTypeRequest
    )
    updateLabel: (
        GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateLabelPropertiesRequest
    )
    updateSelectionChoiceProperties: GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateSelectionChoicePropertiesRequest

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldPropertiesRequest(
    typing_extensions.TypedDict, total=False
):
    id: str
    properties: GoogleAppsDriveLabelsV2FieldProperties
    updateMask: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldTypeRequest(
    typing_extensions.TypedDict, total=False
):
    dateOptions: GoogleAppsDriveLabelsV2FieldDateOptions
    id: str
    integerOptions: GoogleAppsDriveLabelsV2FieldIntegerOptions
    selectionOptions: GoogleAppsDriveLabelsV2FieldSelectionOptions
    textOptions: GoogleAppsDriveLabelsV2FieldTextOptions
    updateMask: str
    userOptions: GoogleAppsDriveLabelsV2FieldUserOptions

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateLabelPropertiesRequest(
    typing_extensions.TypedDict, total=False
):
    properties: GoogleAppsDriveLabelsV2LabelProperties
    updateMask: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateSelectionChoicePropertiesRequest(
    typing_extensions.TypedDict, total=False
):
    fieldId: str
    id: str
    properties: GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceProperties
    updateMask: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponse(
    typing_extensions.TypedDict, total=False
):
    responses: _list[GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponse]
    updatedLabel: GoogleAppsDriveLabelsV2Label

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateFieldResponse(
    typing_extensions.TypedDict, total=False
):
    id: str
    priority: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponse(
    typing_extensions.TypedDict, total=False
):
    fieldId: str
    id: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteSelectionChoiceResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableFieldResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableSelectionChoiceResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableFieldResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableSelectionChoiceResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponse(
    typing_extensions.TypedDict, total=False
):
    createField: GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateFieldResponse
    createSelectionChoice: (
        GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponse
    )
    deleteField: GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponse
    deleteSelectionChoice: (
        GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteSelectionChoiceResponse
    )
    disableField: GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableFieldResponse
    disableSelectionChoice: (
        GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableSelectionChoiceResponse
    )
    enableField: GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableFieldResponse
    enableSelectionChoice: (
        GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableSelectionChoiceResponse
    )
    updateField: (
        GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldPropertiesResponse
    )
    updateFieldType: (
        GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldTypeResponse
    )
    updateLabel: (
        GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateLabelPropertiesResponse
    )
    updateSelectionChoiceProperties: GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateSelectionChoicePropertiesResponse

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldPropertiesResponse(
    typing_extensions.TypedDict, total=False
):
    priority: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldTypeResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateLabelPropertiesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateSelectionChoicePropertiesResponse(
    typing_extensions.TypedDict, total=False
):
    priority: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2DisableLabelRequest(
    typing_extensions.TypedDict, total=False
):
    disabledPolicy: GoogleAppsDriveLabelsV2LifecycleDisabledPolicy
    languageCode: str
    updateMask: str
    useAdminAccess: bool
    writeControl: GoogleAppsDriveLabelsV2WriteControl

@typing.type_check_only
class GoogleAppsDriveLabelsV2EnableLabelRequest(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    useAdminAccess: bool
    writeControl: GoogleAppsDriveLabelsV2WriteControl

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
class GoogleAppsDriveLabelsV2FieldLimits(typing_extensions.TypedDict, total=False):
    dateLimits: GoogleAppsDriveLabelsV2DateLimits
    integerLimits: GoogleAppsDriveLabelsV2IntegerLimits
    longTextLimits: GoogleAppsDriveLabelsV2LongTextLimits
    maxDescriptionLength: int
    maxDisplayNameLength: int
    maxIdLength: int
    selectionLimits: GoogleAppsDriveLabelsV2SelectionLimits
    textLimits: GoogleAppsDriveLabelsV2TextLimits
    userLimits: GoogleAppsDriveLabelsV2UserLimits

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
    appliedCapabilities: (
        GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceAppliedCapabilities
    )
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
    schemaCapabilities: (
        GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceSchemaCapabilities
    )
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
class GoogleAppsDriveLabelsV2IntegerLimits(typing_extensions.TypedDict, total=False):
    maxValue: str
    minValue: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2Label(typing_extensions.TypedDict, total=False):
    appliedCapabilities: GoogleAppsDriveLabelsV2LabelAppliedCapabilities
    appliedLabelPolicy: GoogleAppsDriveLabelsV2LabelAppliedLabelPolicy
    createTime: str
    creator: GoogleAppsDriveLabelsV2UserInfo
    customer: str
    disableTime: str
    disabler: GoogleAppsDriveLabelsV2UserInfo
    displayHints: GoogleAppsDriveLabelsV2LabelDisplayHints
    fields: _list[GoogleAppsDriveLabelsV2Field]
    id: str
    labelType: typing_extensions.Literal[
        "LABEL_TYPE_UNSPECIFIED", "SHARED", "ADMIN", "GOOGLE_APP"
    ]
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
class GoogleAppsDriveLabelsV2LabelLimits(typing_extensions.TypedDict, total=False):
    fieldLimits: GoogleAppsDriveLabelsV2FieldLimits
    maxDeletedFields: int
    maxDescriptionLength: int
    maxDraftRevisions: int
    maxFields: int
    maxTitleLength: int
    name: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelLock(typing_extensions.TypedDict, total=False):
    capabilities: GoogleAppsDriveLabelsV2LabelLockCapabilities
    choiceId: str
    createTime: str
    creator: GoogleAppsDriveLabelsV2UserInfo
    deleteTime: str
    fieldId: str
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETING"]

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelLockCapabilities(
    typing_extensions.TypedDict, total=False
):
    canViewPolicy: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelPermission(typing_extensions.TypedDict, total=False):
    audience: str
    email: str
    group: str
    name: str
    person: str
    role: typing_extensions.Literal[
        "LABEL_ROLE_UNSPECIFIED", "READER", "APPLIER", "ORGANIZER", "EDITOR"
    ]

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
class GoogleAppsDriveLabelsV2ListLabelLocksResponse(
    typing_extensions.TypedDict, total=False
):
    labelLocks: _list[GoogleAppsDriveLabelsV2LabelLock]
    nextPageToken: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2ListLabelPermissionsResponse(
    typing_extensions.TypedDict, total=False
):
    labelPermissions: _list[GoogleAppsDriveLabelsV2LabelPermission]
    nextPageToken: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2ListLabelsResponse(
    typing_extensions.TypedDict, total=False
):
    labels: _list[GoogleAppsDriveLabelsV2Label]
    nextPageToken: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2ListLimits(typing_extensions.TypedDict, total=False):
    maxEntries: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2LockStatus(typing_extensions.TypedDict, total=False):
    locked: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2LongTextLimits(typing_extensions.TypedDict, total=False):
    maxLength: int
    minLength: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2PublishLabelRequest(
    typing_extensions.TypedDict, total=False
):
    languageCode: str
    useAdminAccess: bool
    writeControl: GoogleAppsDriveLabelsV2WriteControl

@typing.type_check_only
class GoogleAppsDriveLabelsV2SelectionLimits(typing_extensions.TypedDict, total=False):
    listLimits: GoogleAppsDriveLabelsV2ListLimits
    maxChoices: int
    maxDeletedChoices: int
    maxDisplayNameLength: int
    maxIdLength: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2TextLimits(typing_extensions.TypedDict, total=False):
    maxLength: int
    minLength: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequest(
    typing_extensions.TypedDict, total=False
):
    copyMode: typing_extensions.Literal[
        "COPY_MODE_UNSPECIFIED", "DO_NOT_COPY", "ALWAYS_COPY", "COPY_APPLIABLE"
    ]
    languageCode: str
    useAdminAccess: bool
    view: typing_extensions.Literal["LABEL_VIEW_BASIC", "LABEL_VIEW_FULL"]

@typing.type_check_only
class GoogleAppsDriveLabelsV2UpdateLabelPermissionRequest(
    typing_extensions.TypedDict, total=False
):
    labelPermission: GoogleAppsDriveLabelsV2LabelPermission
    parent: str
    useAdminAccess: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2UserCapabilities(typing_extensions.TypedDict, total=False):
    canAccessLabelManager: bool
    canAdministrateLabels: bool
    canCreateAdminLabels: bool
    canCreateSharedLabels: bool
    name: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2UserInfo(typing_extensions.TypedDict, total=False):
    person: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2UserLimits(typing_extensions.TypedDict, total=False):
    listLimits: GoogleAppsDriveLabelsV2ListLimits

@typing.type_check_only
class GoogleAppsDriveLabelsV2WriteControl(typing_extensions.TypedDict, total=False):
    requiredRevisionId: str

@typing.type_check_only
class GoogleProtobufEmpty(typing_extensions.TypedDict, total=False): ...

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

import typing

_list = list

@typing.type_check_only
class GoogleAppsDriveLabelsV2BadgeColors(typing.TypedDict, total=False):
    backgroundColor: GoogleTypeColor
    foregroundColor: GoogleTypeColor
    soloColor: GoogleTypeColor

@typing.type_check_only
class GoogleAppsDriveLabelsV2BadgeConfig(typing.TypedDict, total=False):
    color: GoogleTypeColor
    priorityOverride: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2BatchDeleteLabelPermissionsRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleAppsDriveLabelsV2DeleteLabelPermissionRequest]
    useAdminAccess: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleAppsDriveLabelsV2UpdateLabelPermissionRequest]
    useAdminAccess: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2BatchUpdateLabelPermissionsResponse(
    typing.TypedDict, total=False
):
    permissions: _list[GoogleAppsDriveLabelsV2LabelPermission]

@typing.type_check_only
class GoogleAppsDriveLabelsV2DateLimits(typing.TypedDict, total=False):
    maxValue: GoogleTypeDate
    minValue: GoogleTypeDate

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeleteLabelPermissionRequest(
    typing.TypedDict, total=False
):
    name: str
    useAdminAccess: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequest(typing.TypedDict, total=False):
    languageCode: str
    requests: _list[GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequest]
    useAdminAccess: bool
    view: typing.Literal["LABEL_VIEW_BASIC", "LABEL_VIEW_FULL"]
    writeControl: GoogleAppsDriveLabelsV2WriteControl

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateFieldRequest(
    typing.TypedDict, total=False
):
    field: GoogleAppsDriveLabelsV2Field

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestCreateSelectionChoiceRequest(
    typing.TypedDict, total=False
):
    choice: GoogleAppsDriveLabelsV2FieldSelectionOptionsChoice
    fieldId: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteFieldRequest(
    typing.TypedDict, total=False
):
    id: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDeleteSelectionChoiceRequest(
    typing.TypedDict, total=False
):
    fieldId: str
    id: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableFieldRequest(
    typing.TypedDict, total=False
):
    disabledPolicy: GoogleAppsDriveLabelsV2LifecycleDisabledPolicy
    id: str
    updateMask: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestDisableSelectionChoiceRequest(
    typing.TypedDict, total=False
):
    disabledPolicy: GoogleAppsDriveLabelsV2LifecycleDisabledPolicy
    fieldId: str
    id: str
    updateMask: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableFieldRequest(
    typing.TypedDict, total=False
):
    id: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestEnableSelectionChoiceRequest(
    typing.TypedDict, total=False
):
    fieldId: str
    id: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestRequest(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    id: str
    properties: GoogleAppsDriveLabelsV2FieldProperties
    updateMask: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateFieldTypeRequest(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    properties: GoogleAppsDriveLabelsV2LabelProperties
    updateMask: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelRequestUpdateSelectionChoicePropertiesRequest(
    typing.TypedDict, total=False
):
    fieldId: str
    id: str
    properties: GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceProperties
    updateMask: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponse(typing.TypedDict, total=False):
    responses: _list[GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponse]
    updatedLabel: GoogleAppsDriveLabelsV2Label

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateFieldResponse(
    typing.TypedDict, total=False
):
    id: str
    priority: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseCreateSelectionChoiceResponse(
    typing.TypedDict, total=False
):
    fieldId: str
    id: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteFieldResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDeleteSelectionChoiceResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableFieldResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseDisableSelectionChoiceResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableFieldResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseEnableSelectionChoiceResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseResponse(
    typing.TypedDict, total=False
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
    typing.TypedDict, total=False
):
    priority: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateFieldTypeResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateLabelPropertiesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2DeltaUpdateLabelResponseUpdateSelectionChoicePropertiesResponse(
    typing.TypedDict, total=False
):
    priority: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2DisableLabelRequest(typing.TypedDict, total=False):
    disabledPolicy: GoogleAppsDriveLabelsV2LifecycleDisabledPolicy
    languageCode: str
    updateMask: str
    useAdminAccess: bool
    writeControl: GoogleAppsDriveLabelsV2WriteControl

@typing.type_check_only
class GoogleAppsDriveLabelsV2EnableLabelRequest(typing.TypedDict, total=False):
    languageCode: str
    useAdminAccess: bool
    writeControl: GoogleAppsDriveLabelsV2WriteControl

@typing.type_check_only
class GoogleAppsDriveLabelsV2Field(typing.TypedDict, total=False):
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
class GoogleAppsDriveLabelsV2FieldAppliedCapabilities(typing.TypedDict, total=False):
    canRead: bool
    canSearch: bool
    canWrite: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldDateOptions(typing.TypedDict, total=False):
    dateFormat: str
    dateFormatType: typing.Literal["DATE_FORMAT_UNSPECIFIED", "LONG_DATE", "SHORT_DATE"]
    maxValue: GoogleTypeDate
    minValue: GoogleTypeDate

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldDisplayHints(typing.TypedDict, total=False):
    disabled: bool
    hiddenInSearch: bool
    required: bool
    shownInApply: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldIntegerOptions(typing.TypedDict, total=False):
    maxValue: str
    minValue: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldLimits(typing.TypedDict, total=False):
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
class GoogleAppsDriveLabelsV2FieldListOptions(typing.TypedDict, total=False):
    maxEntries: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldProperties(typing.TypedDict, total=False):
    displayName: str
    insertBeforeField: str
    required: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldSchemaCapabilities(typing.TypedDict, total=False):
    canDelete: bool
    canDisable: bool
    canEnable: bool
    canUpdate: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldSelectionOptions(typing.TypedDict, total=False):
    choices: _list[GoogleAppsDriveLabelsV2FieldSelectionOptionsChoice]
    listOptions: GoogleAppsDriveLabelsV2FieldListOptions

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldSelectionOptionsChoice(typing.TypedDict, total=False):
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
    typing.TypedDict, total=False
):
    canRead: bool
    canSearch: bool
    canSelect: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceDisplayHints(
    typing.TypedDict, total=False
):
    badgeColors: GoogleAppsDriveLabelsV2BadgeColors
    badgePriority: str
    darkBadgeColors: GoogleAppsDriveLabelsV2BadgeColors
    disabled: bool
    hiddenInSearch: bool
    shownInApply: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceProperties(
    typing.TypedDict, total=False
):
    badgeConfig: GoogleAppsDriveLabelsV2BadgeConfig
    description: str
    displayName: str
    insertBeforeChoice: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldSelectionOptionsChoiceSchemaCapabilities(
    typing.TypedDict, total=False
):
    canDelete: bool
    canDisable: bool
    canEnable: bool
    canUpdate: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldTextOptions(typing.TypedDict, total=False):
    maxLength: int
    minLength: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2FieldUserOptions(typing.TypedDict, total=False):
    listOptions: GoogleAppsDriveLabelsV2FieldListOptions

@typing.type_check_only
class GoogleAppsDriveLabelsV2IntegerLimits(typing.TypedDict, total=False):
    maxValue: str
    minValue: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2Label(typing.TypedDict, total=False):
    appliedCapabilities: GoogleAppsDriveLabelsV2LabelAppliedCapabilities
    appliedLabelPolicy: GoogleAppsDriveLabelsV2LabelAppliedLabelPolicy
    createTime: str
    creator: GoogleAppsDriveLabelsV2UserInfo
    customer: str
    disableTime: str
    disabler: GoogleAppsDriveLabelsV2UserInfo
    displayHints: GoogleAppsDriveLabelsV2LabelDisplayHints
    enabledAppSettings: GoogleAppsDriveLabelsV2LabelEnabledAppSettings
    fields: _list[GoogleAppsDriveLabelsV2Field]
    id: str
    labelType: typing.Literal["LABEL_TYPE_UNSPECIFIED", "SHARED", "ADMIN", "GOOGLE_APP"]
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
class GoogleAppsDriveLabelsV2LabelAppliedCapabilities(typing.TypedDict, total=False):
    canApply: bool
    canRead: bool
    canRemove: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelAppliedLabelPolicy(typing.TypedDict, total=False):
    copyMode: typing.Literal[
        "COPY_MODE_UNSPECIFIED", "DO_NOT_COPY", "ALWAYS_COPY", "COPY_APPLIABLE"
    ]

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelDisplayHints(typing.TypedDict, total=False):
    disabled: bool
    hiddenInSearch: bool
    priority: str
    shownInApply: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelEnabledAppSettings(typing.TypedDict, total=False):
    enabledApps: _list[GoogleAppsDriveLabelsV2LabelEnabledAppSettingsEnabledApp]

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelEnabledAppSettingsEnabledApp(
    typing.TypedDict, total=False
):
    app: typing.Literal["APP_UNSPECIFIED", "DRIVE", "GMAIL"]

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelLimits(typing.TypedDict, total=False):
    fieldLimits: GoogleAppsDriveLabelsV2FieldLimits
    maxDeletedFields: int
    maxDescriptionLength: int
    maxDraftRevisions: int
    maxFields: int
    maxTitleLength: int
    name: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelLock(typing.TypedDict, total=False):
    capabilities: GoogleAppsDriveLabelsV2LabelLockCapabilities
    choiceId: str
    createTime: str
    creator: GoogleAppsDriveLabelsV2UserInfo
    deleteTime: str
    fieldId: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETING"]

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelLockCapabilities(typing.TypedDict, total=False):
    canViewPolicy: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelPermission(typing.TypedDict, total=False):
    audience: str
    email: str
    group: str
    name: str
    person: str
    role: typing.Literal[
        "LABEL_ROLE_UNSPECIFIED", "READER", "APPLIER", "ORGANIZER", "EDITOR"
    ]

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelProperties(typing.TypedDict, total=False):
    description: str
    title: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2LabelSchemaCapabilities(typing.TypedDict, total=False):
    canDelete: bool
    canDisable: bool
    canEnable: bool
    canUpdate: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2Lifecycle(typing.TypedDict, total=False):
    disabledPolicy: GoogleAppsDriveLabelsV2LifecycleDisabledPolicy
    hasUnpublishedChanges: bool
    state: typing.Literal[
        "STATE_UNSPECIFIED", "UNPUBLISHED_DRAFT", "PUBLISHED", "DISABLED", "DELETED"
    ]

@typing.type_check_only
class GoogleAppsDriveLabelsV2LifecycleDisabledPolicy(typing.TypedDict, total=False):
    hideInSearch: bool
    showInApply: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2ListLabelLocksResponse(typing.TypedDict, total=False):
    labelLocks: _list[GoogleAppsDriveLabelsV2LabelLock]
    nextPageToken: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2ListLabelPermissionsResponse(
    typing.TypedDict, total=False
):
    labelPermissions: _list[GoogleAppsDriveLabelsV2LabelPermission]
    nextPageToken: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2ListLabelsResponse(typing.TypedDict, total=False):
    labels: _list[GoogleAppsDriveLabelsV2Label]
    nextPageToken: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2ListLimits(typing.TypedDict, total=False):
    maxEntries: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2LockStatus(typing.TypedDict, total=False):
    locked: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2LongTextLimits(typing.TypedDict, total=False):
    maxLength: int
    minLength: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2PublishLabelRequest(typing.TypedDict, total=False):
    languageCode: str
    useAdminAccess: bool
    writeControl: GoogleAppsDriveLabelsV2WriteControl

@typing.type_check_only
class GoogleAppsDriveLabelsV2SelectionLimits(typing.TypedDict, total=False):
    listLimits: GoogleAppsDriveLabelsV2ListLimits
    maxChoices: int
    maxDeletedChoices: int
    maxDisplayNameLength: int
    maxIdLength: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2TextLimits(typing.TypedDict, total=False):
    maxLength: int
    minLength: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2UpdateLabelCopyModeRequest(typing.TypedDict, total=False):
    copyMode: typing.Literal[
        "COPY_MODE_UNSPECIFIED", "DO_NOT_COPY", "ALWAYS_COPY", "COPY_APPLIABLE"
    ]
    languageCode: str
    useAdminAccess: bool
    view: typing.Literal["LABEL_VIEW_BASIC", "LABEL_VIEW_FULL"]

@typing.type_check_only
class GoogleAppsDriveLabelsV2UpdateLabelEnabledAppSettingsRequest(
    typing.TypedDict, total=False
):
    enabledAppSettings: GoogleAppsDriveLabelsV2LabelEnabledAppSettings
    languageCode: str
    useAdminAccess: bool
    view: typing.Literal["LABEL_VIEW_BASIC", "LABEL_VIEW_FULL"]

@typing.type_check_only
class GoogleAppsDriveLabelsV2UpdateLabelPermissionRequest(
    typing.TypedDict, total=False
):
    labelPermission: GoogleAppsDriveLabelsV2LabelPermission
    parent: str
    useAdminAccess: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2UserCapabilities(typing.TypedDict, total=False):
    canAccessLabelManager: bool
    canAdministrateLabels: bool
    canCreateAdminLabels: bool
    canCreateSharedLabels: bool
    name: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2UserInfo(typing.TypedDict, total=False):
    person: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2UserLimits(typing.TypedDict, total=False):
    listLimits: GoogleAppsDriveLabelsV2ListLimits

@typing.type_check_only
class GoogleAppsDriveLabelsV2WriteControl(typing.TypedDict, total=False):
    requiredRevisionId: str

@typing.type_check_only
class GoogleProtobufEmpty(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleTypeColor(typing.TypedDict, total=False):
    alpha: float
    blue: float
    green: float
    red: float

@typing.type_check_only
class GoogleTypeDate(typing.TypedDict, total=False):
    day: int
    month: int
    year: int

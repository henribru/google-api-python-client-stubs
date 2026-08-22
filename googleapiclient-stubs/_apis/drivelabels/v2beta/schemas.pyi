import typing

_list = list

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaBadgeColors(typing.TypedDict, total=False):
    backgroundColor: GoogleTypeColor
    foregroundColor: GoogleTypeColor
    soloColor: GoogleTypeColor

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaBadgeConfig(typing.TypedDict, total=False):
    color: GoogleTypeColor
    priorityOverride: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaBatchDeleteLabelPermissionsRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleAppsDriveLabelsV2betaDeleteLabelPermissionRequest]
    useAdminAccess: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsRequest(
    typing.TypedDict, total=False
):
    requests: _list[GoogleAppsDriveLabelsV2betaUpdateLabelPermissionRequest]
    useAdminAccess: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaBatchUpdateLabelPermissionsResponse(
    typing.TypedDict, total=False
):
    permissions: _list[GoogleAppsDriveLabelsV2betaLabelPermission]

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDateLimits(typing.TypedDict, total=False):
    maxValue: GoogleTypeDate
    minValue: GoogleTypeDate

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeleteLabelPermissionRequest(
    typing.TypedDict, total=False
):
    name: str
    useAdminAccess: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequest(typing.TypedDict, total=False):
    languageCode: str
    requests: _list[GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestRequest]
    useAdminAccess: bool
    view: typing.Literal["LABEL_VIEW_BASIC", "LABEL_VIEW_FULL"]
    writeControl: GoogleAppsDriveLabelsV2betaWriteControl

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestCreateFieldRequest(
    typing.TypedDict, total=False
):
    field: GoogleAppsDriveLabelsV2betaField

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestCreateSelectionChoiceRequest(
    typing.TypedDict, total=False
):
    choice: GoogleAppsDriveLabelsV2betaFieldSelectionOptionsChoice
    fieldId: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestDeleteFieldRequest(
    typing.TypedDict, total=False
):
    id: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestDeleteSelectionChoiceRequest(
    typing.TypedDict, total=False
):
    fieldId: str
    id: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestDisableFieldRequest(
    typing.TypedDict, total=False
):
    disabledPolicy: GoogleAppsDriveLabelsV2betaLifecycleDisabledPolicy
    id: str
    updateMask: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestDisableSelectionChoiceRequest(
    typing.TypedDict, total=False
):
    disabledPolicy: GoogleAppsDriveLabelsV2betaLifecycleDisabledPolicy
    fieldId: str
    id: str
    updateMask: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestEnableFieldRequest(
    typing.TypedDict, total=False
):
    id: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestEnableSelectionChoiceRequest(
    typing.TypedDict, total=False
):
    fieldId: str
    id: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestRequest(
    typing.TypedDict, total=False
):
    createField: GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestCreateFieldRequest
    createSelectionChoice: (
        GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestCreateSelectionChoiceRequest
    )
    deleteField: GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestDeleteFieldRequest
    deleteSelectionChoice: (
        GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestDeleteSelectionChoiceRequest
    )
    disableField: GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestDisableFieldRequest
    disableSelectionChoice: (
        GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestDisableSelectionChoiceRequest
    )
    enableField: GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestEnableFieldRequest
    enableSelectionChoice: (
        GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestEnableSelectionChoiceRequest
    )
    updateField: (
        GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestUpdateFieldPropertiesRequest
    )
    updateFieldType: (
        GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestUpdateFieldTypeRequest
    )
    updateLabel: (
        GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestUpdateLabelPropertiesRequest
    )
    updateSelectionChoiceProperties: GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestUpdateSelectionChoicePropertiesRequest

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestUpdateFieldPropertiesRequest(
    typing.TypedDict, total=False
):
    id: str
    properties: GoogleAppsDriveLabelsV2betaFieldProperties
    updateMask: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestUpdateFieldTypeRequest(
    typing.TypedDict, total=False
):
    dateOptions: GoogleAppsDriveLabelsV2betaFieldDateOptions
    id: str
    integerOptions: GoogleAppsDriveLabelsV2betaFieldIntegerOptions
    selectionOptions: GoogleAppsDriveLabelsV2betaFieldSelectionOptions
    textOptions: GoogleAppsDriveLabelsV2betaFieldTextOptions
    updateMask: str
    userOptions: GoogleAppsDriveLabelsV2betaFieldUserOptions

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestUpdateLabelPropertiesRequest(
    typing.TypedDict, total=False
):
    properties: GoogleAppsDriveLabelsV2betaLabelProperties
    updateMask: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelRequestUpdateSelectionChoicePropertiesRequest(
    typing.TypedDict, total=False
):
    fieldId: str
    id: str
    properties: GoogleAppsDriveLabelsV2betaFieldSelectionOptionsChoiceProperties
    updateMask: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponse(
    typing.TypedDict, total=False
):
    responses: _list[GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseResponse]
    updatedLabel: GoogleAppsDriveLabelsV2betaLabel

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseCreateFieldResponse(
    typing.TypedDict, total=False
):
    id: str
    priority: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseCreateSelectionChoiceResponse(
    typing.TypedDict, total=False
):
    fieldId: str
    id: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseDeleteFieldResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseDeleteSelectionChoiceResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseDisableFieldResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseDisableSelectionChoiceResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseEnableFieldResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseEnableSelectionChoiceResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseResponse(
    typing.TypedDict, total=False
):
    createField: GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseCreateFieldResponse
    createSelectionChoice: (
        GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseCreateSelectionChoiceResponse
    )
    deleteField: GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseDeleteFieldResponse
    deleteSelectionChoice: (
        GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseDeleteSelectionChoiceResponse
    )
    disableField: (
        GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseDisableFieldResponse
    )
    disableSelectionChoice: GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseDisableSelectionChoiceResponse
    enableField: GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseEnableFieldResponse
    enableSelectionChoice: (
        GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseEnableSelectionChoiceResponse
    )
    updateField: (
        GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseUpdateFieldPropertiesResponse
    )
    updateFieldType: (
        GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseUpdateFieldTypeResponse
    )
    updateLabel: (
        GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseUpdateLabelPropertiesResponse
    )
    updateSelectionChoiceProperties: GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseUpdateSelectionChoicePropertiesResponse

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseUpdateFieldPropertiesResponse(
    typing.TypedDict, total=False
):
    priority: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseUpdateFieldTypeResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseUpdateLabelPropertiesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDeltaUpdateLabelResponseUpdateSelectionChoicePropertiesResponse(
    typing.TypedDict, total=False
):
    priority: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaDisableLabelRequest(typing.TypedDict, total=False):
    disabledPolicy: GoogleAppsDriveLabelsV2betaLifecycleDisabledPolicy
    languageCode: str
    updateMask: str
    useAdminAccess: bool
    writeControl: GoogleAppsDriveLabelsV2betaWriteControl

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaEnableLabelRequest(typing.TypedDict, total=False):
    languageCode: str
    useAdminAccess: bool
    writeControl: GoogleAppsDriveLabelsV2betaWriteControl

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaField(typing.TypedDict, total=False):
    appliedCapabilities: GoogleAppsDriveLabelsV2betaFieldAppliedCapabilities
    createTime: str
    creator: GoogleAppsDriveLabelsV2betaUserInfo
    dateOptions: GoogleAppsDriveLabelsV2betaFieldDateOptions
    disableTime: str
    disabler: GoogleAppsDriveLabelsV2betaUserInfo
    displayHints: GoogleAppsDriveLabelsV2betaFieldDisplayHints
    id: str
    integerOptions: GoogleAppsDriveLabelsV2betaFieldIntegerOptions
    lifecycle: GoogleAppsDriveLabelsV2betaLifecycle
    lockStatus: GoogleAppsDriveLabelsV2betaLockStatus
    properties: GoogleAppsDriveLabelsV2betaFieldProperties
    publisher: GoogleAppsDriveLabelsV2betaUserInfo
    queryKey: str
    schemaCapabilities: GoogleAppsDriveLabelsV2betaFieldSchemaCapabilities
    selectionOptions: GoogleAppsDriveLabelsV2betaFieldSelectionOptions
    textOptions: GoogleAppsDriveLabelsV2betaFieldTextOptions
    updateTime: str
    updater: GoogleAppsDriveLabelsV2betaUserInfo
    userOptions: GoogleAppsDriveLabelsV2betaFieldUserOptions

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaFieldAppliedCapabilities(
    typing.TypedDict, total=False
):
    canRead: bool
    canSearch: bool
    canWrite: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaFieldDateOptions(typing.TypedDict, total=False):
    dateFormat: str
    dateFormatType: typing.Literal["DATE_FORMAT_UNSPECIFIED", "LONG_DATE", "SHORT_DATE"]
    maxValue: GoogleTypeDate
    minValue: GoogleTypeDate

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaFieldDisplayHints(typing.TypedDict, total=False):
    disabled: bool
    hiddenInSearch: bool
    required: bool
    shownInApply: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaFieldIntegerOptions(typing.TypedDict, total=False):
    maxValue: str
    minValue: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaFieldLimits(typing.TypedDict, total=False):
    dateLimits: GoogleAppsDriveLabelsV2betaDateLimits
    integerLimits: GoogleAppsDriveLabelsV2betaIntegerLimits
    longTextLimits: GoogleAppsDriveLabelsV2betaLongTextLimits
    maxDescriptionLength: int
    maxDisplayNameLength: int
    maxIdLength: int
    selectionLimits: GoogleAppsDriveLabelsV2betaSelectionLimits
    textLimits: GoogleAppsDriveLabelsV2betaTextLimits
    userLimits: GoogleAppsDriveLabelsV2betaUserLimits

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaFieldListOptions(typing.TypedDict, total=False):
    maxEntries: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaFieldProperties(typing.TypedDict, total=False):
    displayName: str
    insertBeforeField: str
    required: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaFieldSchemaCapabilities(typing.TypedDict, total=False):
    canDelete: bool
    canDisable: bool
    canEnable: bool
    canUpdate: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaFieldSelectionOptions(typing.TypedDict, total=False):
    choices: _list[GoogleAppsDriveLabelsV2betaFieldSelectionOptionsChoice]
    listOptions: GoogleAppsDriveLabelsV2betaFieldListOptions

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaFieldSelectionOptionsChoice(
    typing.TypedDict, total=False
):
    appliedCapabilities: (
        GoogleAppsDriveLabelsV2betaFieldSelectionOptionsChoiceAppliedCapabilities
    )
    createTime: str
    creator: GoogleAppsDriveLabelsV2betaUserInfo
    disableTime: str
    disabler: GoogleAppsDriveLabelsV2betaUserInfo
    displayHints: GoogleAppsDriveLabelsV2betaFieldSelectionOptionsChoiceDisplayHints
    id: str
    lifecycle: GoogleAppsDriveLabelsV2betaLifecycle
    lockStatus: GoogleAppsDriveLabelsV2betaLockStatus
    properties: GoogleAppsDriveLabelsV2betaFieldSelectionOptionsChoiceProperties
    publishTime: str
    publisher: GoogleAppsDriveLabelsV2betaUserInfo
    schemaCapabilities: (
        GoogleAppsDriveLabelsV2betaFieldSelectionOptionsChoiceSchemaCapabilities
    )
    updateTime: str
    updater: GoogleAppsDriveLabelsV2betaUserInfo

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaFieldSelectionOptionsChoiceAppliedCapabilities(
    typing.TypedDict, total=False
):
    canRead: bool
    canSearch: bool
    canSelect: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaFieldSelectionOptionsChoiceDisplayHints(
    typing.TypedDict, total=False
):
    badgeColors: GoogleAppsDriveLabelsV2betaBadgeColors
    badgePriority: str
    darkBadgeColors: GoogleAppsDriveLabelsV2betaBadgeColors
    disabled: bool
    hiddenInSearch: bool
    shownInApply: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaFieldSelectionOptionsChoiceProperties(
    typing.TypedDict, total=False
):
    badgeConfig: GoogleAppsDriveLabelsV2betaBadgeConfig
    description: str
    displayName: str
    insertBeforeChoice: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaFieldSelectionOptionsChoiceSchemaCapabilities(
    typing.TypedDict, total=False
):
    canDelete: bool
    canDisable: bool
    canEnable: bool
    canUpdate: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaFieldTextOptions(typing.TypedDict, total=False):
    maxLength: int
    minLength: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaFieldUserOptions(typing.TypedDict, total=False):
    listOptions: GoogleAppsDriveLabelsV2betaFieldListOptions

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaIntegerLimits(typing.TypedDict, total=False):
    maxValue: str
    minValue: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaLabel(typing.TypedDict, total=False):
    appliedCapabilities: GoogleAppsDriveLabelsV2betaLabelAppliedCapabilities
    appliedLabelPolicy: GoogleAppsDriveLabelsV2betaLabelAppliedLabelPolicy
    createTime: str
    creator: GoogleAppsDriveLabelsV2betaUserInfo
    customer: str
    disableTime: str
    disabler: GoogleAppsDriveLabelsV2betaUserInfo
    displayHints: GoogleAppsDriveLabelsV2betaLabelDisplayHints
    enabledAppSettings: GoogleAppsDriveLabelsV2betaLabelEnabledAppSettings
    fields: _list[GoogleAppsDriveLabelsV2betaField]
    id: str
    labelType: typing.Literal["LABEL_TYPE_UNSPECIFIED", "SHARED", "ADMIN", "GOOGLE_APP"]
    learnMoreUri: str
    lifecycle: GoogleAppsDriveLabelsV2betaLifecycle
    lockStatus: GoogleAppsDriveLabelsV2betaLockStatus
    name: str
    properties: GoogleAppsDriveLabelsV2betaLabelProperties
    publishTime: str
    publisher: GoogleAppsDriveLabelsV2betaUserInfo
    revisionCreateTime: str
    revisionCreator: GoogleAppsDriveLabelsV2betaUserInfo
    revisionId: str
    schemaCapabilities: GoogleAppsDriveLabelsV2betaLabelSchemaCapabilities

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaLabelAppliedCapabilities(
    typing.TypedDict, total=False
):
    canApply: bool
    canRead: bool
    canRemove: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaLabelAppliedLabelPolicy(typing.TypedDict, total=False):
    copyMode: typing.Literal[
        "COPY_MODE_UNSPECIFIED", "DO_NOT_COPY", "ALWAYS_COPY", "COPY_APPLIABLE"
    ]

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaLabelDisplayHints(typing.TypedDict, total=False):
    disabled: bool
    hiddenInSearch: bool
    priority: str
    shownInApply: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaLabelEnabledAppSettings(typing.TypedDict, total=False):
    enabledApps: _list[GoogleAppsDriveLabelsV2betaLabelEnabledAppSettingsEnabledApp]

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaLabelEnabledAppSettingsEnabledApp(
    typing.TypedDict, total=False
):
    app: typing.Literal["APP_UNSPECIFIED", "DRIVE", "GMAIL"]

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaLabelLimits(typing.TypedDict, total=False):
    fieldLimits: GoogleAppsDriveLabelsV2betaFieldLimits
    maxDeletedFields: int
    maxDescriptionLength: int
    maxDraftRevisions: int
    maxFields: int
    maxTitleLength: int
    name: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaLabelLock(typing.TypedDict, total=False):
    capabilities: GoogleAppsDriveLabelsV2betaLabelLockCapabilities
    choiceId: str
    createTime: str
    creator: GoogleAppsDriveLabelsV2betaUserInfo
    deleteTime: str
    fieldId: str
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "ACTIVE", "DELETING"]

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaLabelLockCapabilities(typing.TypedDict, total=False):
    canViewPolicy: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaLabelPermission(typing.TypedDict, total=False):
    audience: str
    email: str
    group: str
    name: str
    person: str
    role: typing.Literal[
        "LABEL_ROLE_UNSPECIFIED", "READER", "APPLIER", "ORGANIZER", "EDITOR"
    ]

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaLabelProperties(typing.TypedDict, total=False):
    description: str
    title: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaLabelSchemaCapabilities(typing.TypedDict, total=False):
    canDelete: bool
    canDisable: bool
    canEnable: bool
    canUpdate: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaLifecycle(typing.TypedDict, total=False):
    disabledPolicy: GoogleAppsDriveLabelsV2betaLifecycleDisabledPolicy
    hasUnpublishedChanges: bool
    state: typing.Literal[
        "STATE_UNSPECIFIED", "UNPUBLISHED_DRAFT", "PUBLISHED", "DISABLED", "DELETED"
    ]

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaLifecycleDisabledPolicy(typing.TypedDict, total=False):
    hideInSearch: bool
    showInApply: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaListLabelLocksResponse(typing.TypedDict, total=False):
    labelLocks: _list[GoogleAppsDriveLabelsV2betaLabelLock]
    nextPageToken: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaListLabelPermissionsResponse(
    typing.TypedDict, total=False
):
    labelPermissions: _list[GoogleAppsDriveLabelsV2betaLabelPermission]
    nextPageToken: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaListLabelsResponse(typing.TypedDict, total=False):
    labels: _list[GoogleAppsDriveLabelsV2betaLabel]
    nextPageToken: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaListLimits(typing.TypedDict, total=False):
    maxEntries: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaLockStatus(typing.TypedDict, total=False):
    locked: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaLongTextLimits(typing.TypedDict, total=False):
    maxLength: int
    minLength: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaPublishLabelRequest(typing.TypedDict, total=False):
    languageCode: str
    useAdminAccess: bool
    writeControl: GoogleAppsDriveLabelsV2betaWriteControl

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaSelectionLimits(typing.TypedDict, total=False):
    listLimits: GoogleAppsDriveLabelsV2betaListLimits
    maxChoices: int
    maxDeletedChoices: int
    maxDisplayNameLength: int
    maxIdLength: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaTextLimits(typing.TypedDict, total=False):
    maxLength: int
    minLength: int

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaUpdateLabelCopyModeRequest(
    typing.TypedDict, total=False
):
    copyMode: typing.Literal[
        "COPY_MODE_UNSPECIFIED", "DO_NOT_COPY", "ALWAYS_COPY", "COPY_APPLIABLE"
    ]
    languageCode: str
    useAdminAccess: bool
    view: typing.Literal["LABEL_VIEW_BASIC", "LABEL_VIEW_FULL"]

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaUpdateLabelEnabledAppSettingsRequest(
    typing.TypedDict, total=False
):
    enabledAppSettings: GoogleAppsDriveLabelsV2betaLabelEnabledAppSettings
    languageCode: str
    useAdminAccess: bool
    view: typing.Literal["LABEL_VIEW_BASIC", "LABEL_VIEW_FULL"]

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaUpdateLabelPermissionRequest(
    typing.TypedDict, total=False
):
    labelPermission: GoogleAppsDriveLabelsV2betaLabelPermission
    parent: str
    useAdminAccess: bool

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaUserCapabilities(typing.TypedDict, total=False):
    canAccessLabelManager: bool
    canAdministrateLabels: bool
    canCreateAdminLabels: bool
    canCreateSharedLabels: bool
    name: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaUserInfo(typing.TypedDict, total=False):
    person: str

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaUserLimits(typing.TypedDict, total=False):
    listLimits: GoogleAppsDriveLabelsV2betaListLimits

@typing.type_check_only
class GoogleAppsDriveLabelsV2betaWriteControl(typing.TypedDict, total=False):
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

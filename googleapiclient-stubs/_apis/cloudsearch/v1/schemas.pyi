import typing

import typing_extensions

_list = list

@typing.type_check_only
class AbuseReportingConfig(typing_extensions.TypedDict, total=False):
    recordingAllowed: bool
    writtenUgcAllowed: bool

@typing.type_check_only
class AckInfo(typing_extensions.TypedDict, total=False):
    unackedDeviceCount: int
    unackedDeviceIds: _list[str]

@typing.type_check_only
class AclFixRequest(typing_extensions.TypedDict, total=False):
    recipientEmails: _list[str]
    role: typing_extensions.Literal["UNKNOWN", "READER", "COMMENTER", "WRITER"]
    shouldFix: bool

@typing.type_check_only
class AclFixStatus(typing_extensions.TypedDict, total=False):
    fixability: typing_extensions.Literal[
        "UNKNOWN", "ALREADY_ACCESSIBLE", "CAN_FIX", "CANNOT_FIX", "ACL_FIXER_ERROR"
    ]
    fixableEmailAddress: _list[str]
    outOfDomainWarningEmailAddress: _list[str]

@typing.type_check_only
class AclInfo(typing_extensions.TypedDict, total=False):
    groupsCount: int
    scope: typing_extensions.Literal[
        "LIMITED",
        "DASHER_DOMAIN_WITH_LINK",
        "DASHER_DOMAIN",
        "PUBLIC_WITH_LINK",
        "PUBLIC",
        "TEAM_DRIVE",
    ]
    usersCount: int

@typing.type_check_only
class ActionParameter(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class AffectedMembership(typing_extensions.TypedDict, total=False):
    affectedMember: MemberId
    priorMembershipRole: typing_extensions.Literal[
        "ROLE_UNKNOWN", "ROLE_NONE", "ROLE_INVITEE", "ROLE_MEMBER", "ROLE_OWNER"
    ]
    priorMembershipState: typing_extensions.Literal[
        "MEMBER_UNKNOWN",
        "MEMBER_INVITED",
        "MEMBER_JOINED",
        "MEMBER_NOT_A_MEMBER",
        "MEMBER_FAILED",
    ]
    targetMembershipRole: typing_extensions.Literal[
        "ROLE_UNKNOWN", "ROLE_NONE", "ROLE_INVITEE", "ROLE_MEMBER", "ROLE_OWNER"
    ]

@typing.type_check_only
class AllAuthenticatedUsersProto(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Annotation(typing_extensions.TypedDict, total=False):
    babelPlaceholderMetadata: BabelPlaceholderMetadata
    cardCapabilityMetadata: CardCapabilityMetadata
    chipRenderType: typing_extensions.Literal[
        "CHIP_RENDER_TYPE_UNSPECIFIED", "RENDER", "RENDER_IF_POSSIBLE", "DO_NOT_RENDER"
    ]
    consentedAppUnfurlMetadata: ConsentedAppUnfurlMetadata
    customEmojiMetadata: CustomEmojiMetadata
    dataLossPreventionMetadata: DataLossPreventionMetadata
    driveMetadata: DriveMetadata
    formatMetadata: FormatMetadata
    groupRetentionSettingsUpdated: GroupRetentionSettingsUpdatedMetaData
    gsuiteIntegrationMetadata: GsuiteIntegrationMetadata
    incomingWebhookChangedMetadata: IncomingWebhookChangedMetadata
    integrationConfigUpdated: IntegrationConfigUpdatedMetadata
    length: int
    localId: str
    membershipChanged: MembershipChangedMetadata
    readReceiptsSettingsMetadata: ReadReceiptsSettingsUpdatedMetadata
    requiredMessageFeaturesMetadata: RequiredMessageFeaturesMetadata
    roomUpdated: RoomUpdatedMetadata
    serverInvalidated: bool
    slashCommandMetadata: SlashCommandMetadata
    startIndex: int
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "URL",
        "DRIVE_FILE",
        "DRIVE_DOC",
        "DRIVE_SHEET",
        "DRIVE_SLIDE",
        "DRIVE_FORM",
        "USER_MENTION",
        "SLASH_COMMAND",
        "CONSENTED_APP_UNFURL",
        "VIDEO",
        "FORMAT_DATA",
        "IMAGE",
        "PDF",
        "VIDEO_CALL",
        "UPLOAD_METADATA",
        "GSUITE_INTEGRATION",
        "CUSTOM_EMOJI",
        "CARD_CAPABILITY",
        "DATA_LOSS_PREVENTION",
        "REQUIRED_MESSAGE_FEATURES_METADATA",
        "MEMBERSHIP_CHANGED",
        "ROOM_UPDATED",
        "GROUP_RETENTION_SETTINGS_UPDATED",
        "BABEL_PLACEHOLDER",
        "READ_RECEIPTS_SETTINGS_UPDATED",
        "INCOMING_WEBHOOK_CHANGED",
        "INTEGRATION_CONFIG_UPDATED",
        "INVITATION",
    ]
    uniqueId: str
    uploadMetadata: UploadMetadata
    urlMetadata: UrlMetadata
    userMentionMetadata: UserMentionMetadata
    videoCallMetadata: VideoCallMetadata
    youtubeMetadata: YoutubeMetadata

@typing.type_check_only
class AppId(typing_extensions.TypedDict, total=False):
    appType: typing_extensions.Literal[
        "APP_TYPE_UNSPECIFIED", "APP", "GSUITE_APP", "INCOMING_WEBHOOK"
    ]
    gsuiteAppType: typing_extensions.Literal[
        "GSUITE_APP_TYPE_UNSPECIFIED",
        "TASKS_APP",
        "CALENDAR_APP",
        "DOCS_APP",
        "SHEETS_APP",
        "SLIDES_APP",
        "MEET_APP",
        "ASSISTIVE_SUGGESTION_APP",
        "CONTACTS_APP",
        "ACTIVITY_FEED_APP",
        "DRIVE_APP",
        "CHAT_IN_MEET_APP",
    ]
    id: str

@typing.type_check_only
class AppsDynamiteSharedAction(typing_extensions.TypedDict, total=False):
    function: str
    interaction: typing_extensions.Literal["INTERACTION_UNSPECIFIED", "OPEN_DIALOG"]
    loadIndicator: typing_extensions.Literal["SPINNER", "NONE"]
    parameters: _list[AppsDynamiteSharedActionActionParameter]

@typing.type_check_only
class AppsDynamiteSharedActionActionParameter(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class AppsDynamiteSharedActivityFeedAnnotationData(
    typing_extensions.TypedDict, total=False
):
    activityFeedMessageCreateTime: str
    activityFeedMessageId: MessageId
    chatItem: AppsDynamiteSharedChatItem
    sharedUserInfo: UserInfo
    userInfo: AppsDynamiteSharedActivityFeedAnnotationDataUserInfo

@typing.type_check_only
class AppsDynamiteSharedActivityFeedAnnotationDataUserInfo(
    typing_extensions.TypedDict, total=False
):
    updaterCountDisplayType: typing_extensions.Literal[
        "UPDATER_COUNT_DISPLAY_TYPE_UNSPECIFIED", "EXACT_COUNT", "NONZERO_COUNT"
    ]
    updaterCountToShow: int
    updaterToShow: UserId

@typing.type_check_only
class AppsDynamiteSharedAppProfile(typing_extensions.TypedDict, total=False):
    avatarEmoji: str
    avatarUrl: str
    name: str

@typing.type_check_only
class AppsDynamiteSharedAssistantAnnotationData(
    typing_extensions.TypedDict, total=False
):
    suggestion: AppsDynamiteSharedAssistantSuggestion
    unfulfillable: AppsDynamiteSharedAssistantUnfulfillableRequest

@typing.type_check_only
class AppsDynamiteSharedAssistantDebugContext(typing_extensions.TypedDict, total=False):
    query: str

@typing.type_check_only
class AppsDynamiteSharedAssistantFeedbackContext(
    typing_extensions.TypedDict, total=False
):
    feedbackChips: _list[AppsDynamiteSharedAssistantFeedbackContextFeedbackChip]
    thumbsFeedback: typing_extensions.Literal[
        "THUMBS_FEEDBACK_UNSPECIFIED", "NONE_SELECTED", "UP", "DOWN"
    ]

@typing.type_check_only
class AppsDynamiteSharedAssistantFeedbackContextFeedbackChip(
    typing_extensions.TypedDict, total=False
):
    feedbackChipType: typing_extensions.Literal[
        "FEEDBACK_CHIP_TYPE_UNSPECIFIED",
        "WRONG_TRIGGER",
        "WRONG_FILE",
        "CORRECT_TRIGGER",
        "CORRECT_FILE",
        "DISRUPTIVE",
        "OTHER",
    ]
    state: typing_extensions.Literal[
        "FEEDBACK_CHIP_STATE_UNSPECIFIED", "SELECTED", "UNSELECTED"
    ]

@typing.type_check_only
class AppsDynamiteSharedAssistantSessionContext(
    typing_extensions.TypedDict, total=False
):
    contextualSessionId: str

@typing.type_check_only
class AppsDynamiteSharedAssistantSuggestion(typing_extensions.TypedDict, total=False):
    debugContext: AppsDynamiteSharedAssistantDebugContext
    feedbackContext: AppsDynamiteSharedAssistantFeedbackContext
    findDocumentSuggestion: AppsDynamiteSharedFindDocumentSuggestion
    serializedSuggestions: str
    sessionContext: AppsDynamiteSharedAssistantSessionContext

@typing.type_check_only
class AppsDynamiteSharedAssistantUnfulfillableRequest(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class AppsDynamiteSharedAvatarInfo(typing_extensions.TypedDict, total=False):
    emoji: AppsDynamiteSharedEmoji

@typing.type_check_only
class AppsDynamiteSharedBackendUploadMetadata(typing_extensions.TypedDict, total=False):
    blobPath: str
    contentName: str
    contentSize: str
    contentType: str
    dlpScanOutcome: typing_extensions.Literal[
        "SCAN_UNKNOWN_OUTCOME",
        "SCAN_SUCCEEDED_NO_VIOLATION",
        "SCAN_SUCCEEDED_BLOCK",
        "SCAN_SUCCEEDED_WARN",
        "SCAN_SUCCEEDED_AUDIT_ONLY",
        "SCAN_FAILURE_EXCEPTION",
        "SCAN_FAILURE_TIMEOUT",
        "SCAN_FAILURE_ALL_RULES_FAILED",
        "SCAN_FAILURE_ILLEGAL_STATE_FOR_ATTACHMENTS",
        "SCAN_SKIPPED_EXPERIMENT_DISABLED",
        "SCAN_SKIPPED_CONSUMER",
        "SCAN_SKIPPED_NON_HUMAN_USER",
        "SCAN_SKIPPED_NO_MESSAGE",
        "SCAN_SKIPPED_USER_ACKNOWLEDGED_WARNING",
        "SCAN_SKIPPED_MESSAGE_FROM_UNSUPPORTED_ORIGIN",
        "SCAN_RULE_EVALUATION_SKIPPED_NO_RULES_FOUND",
        "SCAN_RULE_EVALUATION_SKIPPED_NO_APPLICABLE_RULES_FOR_ACTION_PARAMS",
        "SCAN_RULE_EVALUATION_SKIPPED_NO_APPLICABLE_RULES_FOR_TRIGGER",
        "SCAN_RULE_EVALUATION_SKIPPED_CHANGELING_PERMANENT_ERROR",
        "SCAN_RULE_EVALUATION_SKIPPED_CHANGELING_EMPTY_RESPONSE",
        "SCAN_SUCCEEDED_WITH_FAILURES_NO_VIOLATION",
        "SCAN_SUCCEEDED_WITH_FAILURES_BLOCK",
        "SCAN_SUCCEEDED_WITH_FAILURES_WARN",
        "SCAN_SUCCEEDED_WITH_FAILURES_AUDIT_ONLY",
    ]
    dlpScanSummary: DlpScanSummary
    groupId: GroupId
    originalDimension: AppsDynamiteSharedDimension
    quoteReplyMessageId: MessageId
    sha256: str
    uploadIp: str
    uploadTimestampUsec: str
    videoId: str
    videoThumbnailBlobId: str
    virusScanResult: typing_extensions.Literal[
        "UNKNOWN_VIRUS_SCAN_RESULT", "CLEAN", "INFECTED", "ERROR", "POLICY_VIOLATION"
    ]

@typing.type_check_only
class AppsDynamiteSharedBorderStyle(typing_extensions.TypedDict, total=False):
    cornerRadius: int
    strokeColor: Color
    type: typing_extensions.Literal["BORDER_TYPE_UNSPECIFIED", "NO_BORDER", "STROKE"]

@typing.type_check_only
class AppsDynamiteSharedButton(typing_extensions.TypedDict, total=False):
    altText: str
    color: Color
    disabled: bool
    icon: AppsDynamiteSharedIcon
    onClick: AppsDynamiteSharedOnClick
    text: str

@typing.type_check_only
class AppsDynamiteSharedButtonList(typing_extensions.TypedDict, total=False):
    buttons: _list[AppsDynamiteSharedButton]

@typing.type_check_only
class AppsDynamiteSharedCalendarEventAnnotationData(
    typing_extensions.TypedDict, total=False
):
    calendarEvent: AppsDynamiteSharedCalendarEventAnnotationDataCalendarEvent
    eventCreation: AppsDynamiteSharedCalendarEventAnnotationDataEventCreation

@typing.type_check_only
class AppsDynamiteSharedCalendarEventAnnotationDataCalendarEvent(
    typing_extensions.TypedDict, total=False
):
    endTime: AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTime
    eventId: str
    startTime: AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTime
    title: str

@typing.type_check_only
class AppsDynamiteSharedCalendarEventAnnotationDataCalendarEventTime(
    typing_extensions.TypedDict, total=False
):
    allDay: Date
    timed: str

@typing.type_check_only
class AppsDynamiteSharedCalendarEventAnnotationDataEventCreation(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class AppsDynamiteSharedCallAnnotationData(typing_extensions.TypedDict, total=False):
    callEndedTimestamp: str
    callMetadata: AppsDynamiteSharedCallMetadata
    callStatus: typing_extensions.Literal[
        "CALL_STATUS_UNSPECIFIED", "CALL_STARTED", "CALL_MISSED", "CALL_ENDED"
    ]

@typing.type_check_only
class AppsDynamiteSharedCallMetadata(typing_extensions.TypedDict, total=False):
    meetMetadata: AppsDynamiteSharedMeetMetadata

@typing.type_check_only
class AppsDynamiteSharedCard(typing_extensions.TypedDict, total=False):
    cardActions: _list[AppsDynamiteSharedCardCardAction]
    header: AppsDynamiteSharedCardCardHeader
    name: str
    sections: _list[AppsDynamiteSharedCardSection]

@typing.type_check_only
class AppsDynamiteSharedCardCardAction(typing_extensions.TypedDict, total=False):
    actionLabel: str
    onClick: AppsDynamiteSharedOnClick

@typing.type_check_only
class AppsDynamiteSharedCardCardHeader(typing_extensions.TypedDict, total=False):
    imageAltText: str
    imageType: typing_extensions.Literal["SQUARE", "CIRCLE"]
    imageUrl: str
    subtitle: str
    title: str

@typing.type_check_only
class AppsDynamiteSharedCardClickSuggestion(typing_extensions.TypedDict, total=False):
    actionId: str
    suggestionMessageId: MessageId

@typing.type_check_only
class AppsDynamiteSharedCardSection(typing_extensions.TypedDict, total=False):
    collapsible: bool
    header: str
    uncollapsibleWidgetsCount: int
    widgets: _list[AppsDynamiteSharedWidget]

@typing.type_check_only
class AppsDynamiteSharedChatItem(typing_extensions.TypedDict, total=False):
    activityInfo: _list[AppsDynamiteSharedChatItemActivityInfo]
    groupInfo: AppsDynamiteSharedChatItemGroupInfo
    messageInfo: AppsDynamiteSharedMessageInfo

@typing.type_check_only
class AppsDynamiteSharedChatItemActivityInfo(typing_extensions.TypedDict, total=False):
    feedItemNudge: AppsDynamiteSharedChatItemActivityInfoFeedItemNudge
    feedItemReactions: AppsDynamiteSharedChatItemActivityInfoFeedItemReactions
    feedItemThreadReply: AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReply
    feedItemUserMention: AppsDynamiteSharedChatItemActivityInfoFeedItemUserMention

@typing.type_check_only
class AppsDynamiteSharedChatItemActivityInfoFeedItemNudge(
    typing_extensions.TypedDict, total=False
):
    nudgeType: typing_extensions.Literal["UNDEFINED", "REPLY", "FOLLOW_UP"]

@typing.type_check_only
class AppsDynamiteSharedChatItemActivityInfoFeedItemReactions(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class AppsDynamiteSharedChatItemActivityInfoFeedItemThreadReply(
    typing_extensions.TypedDict, total=False
):
    replyType: typing_extensions.Literal["UNSPECIFIED", "ROOT", "FOLLOWER"]

@typing.type_check_only
class AppsDynamiteSharedChatItemActivityInfoFeedItemUserMention(
    typing_extensions.TypedDict, total=False
):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "DIRECT", "ALL"]

@typing.type_check_only
class AppsDynamiteSharedChatItemGroupInfo(typing_extensions.TypedDict, total=False):
    attributeCheckerGroupType: typing_extensions.Literal[
        "ATTRIBUTE_CHECKER_GROUP_TYPE_UNSPECIFIED",
        "ONE_TO_ONE_HUMAN_DM",
        "ONE_TO_ONE_BOT_DM",
        "IMMUTABLE_MEMBERSHIP_GROUP_DM",
        "FLAT_ROOM",
        "THREADED_ROOM",
        "IMMUTABLE_MEMBERSHIP_HUMAN_DM",
        "POST_ROOM",
        "ACTIVITY_FEED",
    ]
    groupName: str
    groupReadTimeUsec: str
    inlineThreadingEnabled: bool

@typing.type_check_only
class AppsDynamiteSharedColumns(typing_extensions.TypedDict, total=False):
    columnItems: _list[AppsDynamiteSharedColumnsColumn]
    wrapStyle: typing_extensions.Literal["WRAP_STYLE_UNSPECIFIED", "NOWRAP", "WRAP"]

@typing.type_check_only
class AppsDynamiteSharedColumnsColumn(typing_extensions.TypedDict, total=False):
    horizontalAlignment: typing_extensions.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END"
    ]
    horizontalSizeStyle: typing_extensions.Literal[
        "HORIZONTAL_SIZE_STYLE_UNSPECIFIED",
        "FILL_AVAILABLE_SPACE",
        "FILL_MINIMUM_SPACE",
    ]
    verticalAlignment: typing_extensions.Literal[
        "VERTICAL_ALIGNMENT_UNSPECIFIED", "CENTER", "TOP", "BOTTOM"
    ]
    widgets: _list[AppsDynamiteSharedColumnsColumnWidgets]

@typing.type_check_only
class AppsDynamiteSharedColumnsColumnWidgets(typing_extensions.TypedDict, total=False):
    buttonList: AppsDynamiteSharedButtonList
    dateTimePicker: AppsDynamiteSharedDateTimePicker
    decoratedText: AppsDynamiteSharedDecoratedText
    image: AppsDynamiteSharedImage
    selectionInput: AppsDynamiteSharedSelectionInput
    textInput: AppsDynamiteSharedTextInput
    textParagraph: AppsDynamiteSharedTextParagraph

@typing.type_check_only
class AppsDynamiteSharedContentReportType(typing_extensions.TypedDict, total=False):
    systemViolation: typing_extensions.Literal[
        "VIOLATION_UNSPECIFIED",
        "HARASSMENT",
        "DISCRIMINATION",
        "EXPLICIT_CONTENT",
        "SPAM",
        "CONFIDENTIAL_INFORMATION",
        "SENSITIVE_INFORMATION",
        "FRAUD",
        "MALWARE",
        "ILLEGAL_ACTIVITIES",
        "OTHER",
    ]

@typing.type_check_only
class AppsDynamiteSharedCustomEmoji(typing_extensions.TypedDict, total=False):
    blobId: str
    contentType: str
    createTimeMicros: str
    creatorUserId: UserId
    deleteTimeMicros: str
    ephemeralUrl: str
    ownerCustomerId: CustomerId
    readToken: str
    shortcode: str
    state: typing_extensions.Literal[
        "EMOJI_STATE_UNSPECIFIED",
        "EMOJI_ENABLED",
        "EMOJI_SYSTEM_DISABLED",
        "EMOJI_HIDDEN",
        "EMOJI_DELETED",
    ]
    updateTimeMicros: str
    uuid: str

@typing.type_check_only
class AppsDynamiteSharedDateTimePicker(typing_extensions.TypedDict, total=False):
    label: str
    name: str
    onChangeAction: AppsDynamiteSharedAction
    timezoneOffsetDate: int
    type: typing_extensions.Literal["DATE_AND_TIME", "DATE_ONLY", "TIME_ONLY"]
    valueMsEpoch: str

@typing.type_check_only
class AppsDynamiteSharedDecoratedText(typing_extensions.TypedDict, total=False):
    bottomLabel: str
    button: AppsDynamiteSharedButton
    endIcon: AppsDynamiteSharedIcon
    icon: AppsDynamiteSharedIcon
    onClick: AppsDynamiteSharedOnClick
    startIcon: AppsDynamiteSharedIcon
    switchControl: AppsDynamiteSharedDecoratedTextSwitchControl
    text: str
    topLabel: str
    wrapText: bool

@typing.type_check_only
class AppsDynamiteSharedDecoratedTextSwitchControl(
    typing_extensions.TypedDict, total=False
):
    controlType: typing_extensions.Literal["SWITCH", "CHECKBOX", "CHECK_BOX"]
    name: str
    onChangeAction: AppsDynamiteSharedAction
    selected: bool
    value: str

@typing.type_check_only
class AppsDynamiteSharedDimension(typing_extensions.TypedDict, total=False):
    height: int
    width: int

@typing.type_check_only
class AppsDynamiteSharedDivider(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class AppsDynamiteSharedDlpMetricsMetadata(typing_extensions.TypedDict, total=False):
    dlpStatus: typing_extensions.Literal[
        "DLP_STATUS_UNKNOWN",
        "DLP_DISABLED",
        "DLP_ENABLED_NO_RULE_FETCH",
        "DLP_ENABLED_RULES_FETCHED_NO_RULES",
        "DLP_ENABLED_RULES_FETCHED_NO_APPLICABLE_RULES",
        "DLP_ENABLED_RULES_FETCHED_AND_EVALUATED",
        "DLP_ENABLED_SCAN_TIMEOUT",
        "DLP_ENABLED_SCAN_FAILED",
    ]

@typing.type_check_only
class AppsDynamiteSharedDocument(typing_extensions.TypedDict, total=False):
    fileId: str
    justification: AppsDynamiteSharedJustification
    lastModifiedTime: str
    mimeType: str
    title: str
    url: str

@typing.type_check_only
class AppsDynamiteSharedEmoji(typing_extensions.TypedDict, total=False):
    customEmoji: AppsDynamiteSharedCustomEmoji
    unicode: str

@typing.type_check_only
class AppsDynamiteSharedFindDocumentSuggestion(
    typing_extensions.TypedDict, total=False
):
    documentSuggestions: _list[AppsDynamiteSharedDocument]
    showActionButtons: bool

@typing.type_check_only
class AppsDynamiteSharedGrid(typing_extensions.TypedDict, total=False):
    borderStyle: AppsDynamiteSharedBorderStyle
    columnCount: int
    items: _list[AppsDynamiteSharedGridGridItem]
    onClick: AppsDynamiteSharedOnClick
    title: str

@typing.type_check_only
class AppsDynamiteSharedGridGridItem(typing_extensions.TypedDict, total=False):
    id: str
    image: AppsDynamiteSharedImageComponent
    layout: typing_extensions.Literal[
        "GRID_ITEM_LAYOUT_UNSPECIFIED", "TEXT_BELOW", "TEXT_ABOVE"
    ]
    subtitle: str
    textAlignment: typing_extensions.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END"
    ]
    title: str

@typing.type_check_only
class AppsDynamiteSharedGroupDetails(typing_extensions.TypedDict, total=False):
    description: str
    guidelines: str

@typing.type_check_only
class AppsDynamiteSharedGroupVisibility(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal["UNKNOWN", "PRIVATE", "PUBLIC"]

@typing.type_check_only
class AppsDynamiteSharedIcon(typing_extensions.TypedDict, total=False):
    altText: str
    iconUrl: str
    imageType: typing_extensions.Literal["SQUARE", "CIRCLE"]
    knownIcon: str

@typing.type_check_only
class AppsDynamiteSharedImage(typing_extensions.TypedDict, total=False):
    altText: str
    imageUrl: str
    onClick: AppsDynamiteSharedOnClick

@typing.type_check_only
class AppsDynamiteSharedImageComponent(typing_extensions.TypedDict, total=False):
    altText: str
    borderStyle: AppsDynamiteSharedBorderStyle
    cropStyle: AppsDynamiteSharedImageCropStyle
    imageUri: str

@typing.type_check_only
class AppsDynamiteSharedImageCropStyle(typing_extensions.TypedDict, total=False):
    aspectRatio: float
    type: typing_extensions.Literal[
        "IMAGE_CROP_TYPE_UNSPECIFIED",
        "SQUARE",
        "CIRCLE",
        "RECTANGLE_CUSTOM",
        "RECTANGLE_4_3",
    ]

@typing.type_check_only
class AppsDynamiteSharedJustification(typing_extensions.TypedDict, total=False):
    actionTime: str
    actionType: typing_extensions.Literal[
        "ACTION_TYPE_UNSPECIFIED",
        "COMMENTED",
        "CREATED",
        "EDITED",
        "PRESENTED",
        "SHARED",
        "VIEWED",
        "COMMENT_RESOLVED",
        "SENT",
    ]
    documentOwner: AppsDynamiteSharedJustificationPerson
    topics: _list[str]

@typing.type_check_only
class AppsDynamiteSharedJustificationPerson(typing_extensions.TypedDict, total=False):
    isRecipient: bool
    user: UserId

@typing.type_check_only
class AppsDynamiteSharedMeetMetadata(typing_extensions.TypedDict, total=False):
    meetingCode: str
    meetingUrl: str

@typing.type_check_only
class AppsDynamiteSharedMessageInfo(typing_extensions.TypedDict, total=False):
    messageId: MessageId
    messageType: typing_extensions.Literal["MESSAGE_TYPE_UNSPECIFIED", "INLINE_REPLY"]
    topicReadTimeUsec: str

@typing.type_check_only
class AppsDynamiteSharedMessageIntegrationPayload(
    typing_extensions.TypedDict, total=False
):
    projectNumber: str
    tasksMessageIntegrationPayload: AppsDynamiteSharedTasksMessageIntegrationPayload
    type: typing_extensions.Literal["PAYLOAD_TYPE_UNSPECIFIED", "TASKS"]

@typing.type_check_only
class AppsDynamiteSharedOnClick(typing_extensions.TypedDict, total=False):
    action: AppsDynamiteSharedAction
    openDynamicLinkAction: AppsDynamiteSharedAction
    openLink: AppsDynamiteSharedOpenLink

@typing.type_check_only
class AppsDynamiteSharedOpenLink(typing_extensions.TypedDict, total=False):
    appUri: AppsDynamiteSharedOpenLinkAppUri
    onClose: typing_extensions.Literal["NOTHING", "RELOAD"]
    openAs: typing_extensions.Literal["FULL_SIZE", "OVERLAY"]
    url: str

@typing.type_check_only
class AppsDynamiteSharedOpenLinkAppUri(typing_extensions.TypedDict, total=False):
    androidIntent: AppsDynamiteSharedOpenLinkAppUriIntent
    companionUri: str
    iosUri: str

@typing.type_check_only
class AppsDynamiteSharedOpenLinkAppUriIntent(typing_extensions.TypedDict, total=False):
    extraData: _list[AppsDynamiteSharedOpenLinkAppUriIntentExtraData]
    intentAction: str

@typing.type_check_only
class AppsDynamiteSharedOpenLinkAppUriIntentExtraData(
    typing_extensions.TypedDict, total=False
):
    key: str
    value: str

@typing.type_check_only
class AppsDynamiteSharedOrganizationInfo(typing_extensions.TypedDict, total=False):
    consumerInfo: AppsDynamiteSharedOrganizationInfoConsumerInfo
    customerInfo: AppsDynamiteSharedOrganizationInfoCustomerInfo

@typing.type_check_only
class AppsDynamiteSharedOrganizationInfoConsumerInfo(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class AppsDynamiteSharedOrganizationInfoCustomerInfo(
    typing_extensions.TypedDict, total=False
):
    customerId: CustomerId

@typing.type_check_only
class AppsDynamiteSharedOriginAppSuggestion(typing_extensions.TypedDict, total=False):
    appId: AppId
    cardClickSuggestion: AppsDynamiteSharedCardClickSuggestion

@typing.type_check_only
class AppsDynamiteSharedPhoneNumber(typing_extensions.TypedDict, total=False):
    type: str
    value: str

@typing.type_check_only
class AppsDynamiteSharedReaction(typing_extensions.TypedDict, total=False):
    count: int
    createTimestamp: str
    currentUserParticipated: bool
    emoji: AppsDynamiteSharedEmoji

@typing.type_check_only
class AppsDynamiteSharedRetentionSettings(typing_extensions.TypedDict, total=False):
    expiryTimestamp: str
    state: typing_extensions.Literal[
        "UNKNOWN_RETENTION_STATE", "PERMANENT", "EPHEMERAL_ONE_DAY"
    ]

@typing.type_check_only
class AppsDynamiteSharedSegmentedMembershipCount(
    typing_extensions.TypedDict, total=False
):
    memberType: typing_extensions.Literal[
        "MEMBER_TYPE_UNSPECIFIED", "HUMAN_USER", "ROSTER_MEMBER"
    ]
    membershipCount: int
    membershipState: typing_extensions.Literal[
        "MEMBER_UNKNOWN",
        "MEMBER_INVITED",
        "MEMBER_JOINED",
        "MEMBER_NOT_A_MEMBER",
        "MEMBER_FAILED",
    ]

@typing.type_check_only
class AppsDynamiteSharedSegmentedMembershipCounts(
    typing_extensions.TypedDict, total=False
):
    value: _list[AppsDynamiteSharedSegmentedMembershipCount]

@typing.type_check_only
class AppsDynamiteSharedSelectionInput(typing_extensions.TypedDict, total=False):
    items: _list[AppsDynamiteSharedSelectionInputSelectionItem]
    label: str
    name: str
    onChangeAction: AppsDynamiteSharedAction
    type: typing_extensions.Literal["CHECK_BOX", "RADIO_BUTTON", "SWITCH", "DROPDOWN"]

@typing.type_check_only
class AppsDynamiteSharedSelectionInputSelectionItem(
    typing_extensions.TypedDict, total=False
):
    selected: bool
    text: str
    value: str

@typing.type_check_only
class AppsDynamiteSharedSpaceInfo(typing_extensions.TypedDict, total=False):
    avatarInfo: AppsDynamiteSharedAvatarInfo
    avatarUrl: str
    description: str
    groupId: GroupId
    inviterEmail: str
    isExternal: bool
    name: str
    numMembers: int
    userMembershipState: typing_extensions.Literal[
        "MEMBER_UNKNOWN",
        "MEMBER_INVITED",
        "MEMBER_JOINED",
        "MEMBER_NOT_A_MEMBER",
        "MEMBER_FAILED",
    ]

@typing.type_check_only
class AppsDynamiteSharedSuggestions(typing_extensions.TypedDict, total=False):
    items: _list[AppsDynamiteSharedSuggestionsSuggestionItem]

@typing.type_check_only
class AppsDynamiteSharedSuggestionsSuggestionItem(
    typing_extensions.TypedDict, total=False
):
    text: str

@typing.type_check_only
class AppsDynamiteSharedTasksAnnotationData(typing_extensions.TypedDict, total=False):
    assigneeChange: AppsDynamiteSharedTasksAnnotationDataAssigneeChange
    completionChange: AppsDynamiteSharedTasksAnnotationDataCompletionChange
    creation: AppsDynamiteSharedTasksAnnotationDataCreation
    deletionChange: AppsDynamiteSharedTasksAnnotationDataDeletionChange
    taskId: str
    taskProperties: AppsDynamiteSharedTasksAnnotationDataTaskProperties
    userDefinedMessage: AppsDynamiteSharedTasksAnnotationDataUserDefinedMessage

@typing.type_check_only
class AppsDynamiteSharedTasksAnnotationDataAssigneeChange(
    typing_extensions.TypedDict, total=False
):
    oldAssignee: UserId

@typing.type_check_only
class AppsDynamiteSharedTasksAnnotationDataCompletionChange(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class AppsDynamiteSharedTasksAnnotationDataCreation(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class AppsDynamiteSharedTasksAnnotationDataDeletionChange(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class AppsDynamiteSharedTasksAnnotationDataTaskProperties(
    typing_extensions.TypedDict, total=False
):
    assignee: UserId
    completed: bool
    deleted: bool
    description: str
    startDate: Date
    startTime: str
    title: str

@typing.type_check_only
class AppsDynamiteSharedTasksAnnotationDataUserDefinedMessage(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class AppsDynamiteSharedTasksMessageIntegrationPayload(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class AppsDynamiteSharedTextInput(typing_extensions.TypedDict, total=False):
    autoCompleteAction: AppsDynamiteSharedAction
    hintText: str
    initialSuggestions: AppsDynamiteSharedSuggestions
    label: str
    name: str
    onChangeAction: AppsDynamiteSharedAction
    type: typing_extensions.Literal["SINGLE_LINE", "MULTIPLE_LINE"]
    value: str

@typing.type_check_only
class AppsDynamiteSharedTextParagraph(typing_extensions.TypedDict, total=False):
    text: str

@typing.type_check_only
class AppsDynamiteSharedUserBlockRelationship(typing_extensions.TypedDict, total=False):
    hasBlockedRequester: bool
    isBlockedByRequester: bool

@typing.type_check_only
class AppsDynamiteSharedVideoReference(typing_extensions.TypedDict, total=False):
    format: _list[int]
    status: typing_extensions.Literal[
        "UNKNOWN_STATUS",
        "SUCCESS",
        "ERROR",
        "NOT_APPLICABLE",
        "THUMBNAIL_SUCCESS",
        "GO_LIVE_SUCCESS",
    ]

@typing.type_check_only
class AppsDynamiteSharedWidget(typing_extensions.TypedDict, total=False):
    buttonList: AppsDynamiteSharedButtonList
    columns: AppsDynamiteSharedColumns
    dateTimePicker: AppsDynamiteSharedDateTimePicker
    decoratedText: AppsDynamiteSharedDecoratedText
    divider: AppsDynamiteSharedDivider
    grid: AppsDynamiteSharedGrid
    horizontalAlignment: typing_extensions.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END"
    ]
    image: AppsDynamiteSharedImage
    selectionInput: AppsDynamiteSharedSelectionInput
    textInput: AppsDynamiteSharedTextInput
    textParagraph: AppsDynamiteSharedTextParagraph

@typing.type_check_only
class AppsDynamiteV1ApiCompatV1Action(typing_extensions.TypedDict, total=False):
    confirm: AppsDynamiteV1ApiCompatV1ActionConfirm
    name: str
    style: str
    text: str
    type: str
    value: str

@typing.type_check_only
class AppsDynamiteV1ApiCompatV1ActionConfirm(typing_extensions.TypedDict, total=False):
    dismiss_text: str
    ok_text: str
    text: str
    title: str

@typing.type_check_only
class AppsDynamiteV1ApiCompatV1Attachment(typing_extensions.TypedDict, total=False):
    actions: _list[AppsDynamiteV1ApiCompatV1Action]
    attachment_type: str
    author_icon: str
    author_link: str
    author_name: str
    callback_id: str
    color: str
    fallback: str
    fields: _list[AppsDynamiteV1ApiCompatV1Field]
    footer: str
    footer_icon: str
    image_url: str
    mrkdwn_in: _list[str]
    pretext: str
    text: str
    thumb_url: str
    title: str
    title_link: str
    ts: int

@typing.type_check_only
class AppsDynamiteV1ApiCompatV1Field(typing_extensions.TypedDict, total=False):
    short: bool
    title: str
    value: str

@typing.type_check_only
class Attachment(typing_extensions.TypedDict, total=False):
    addOnData: GoogleChatV1ContextualAddOnMarkup
    appId: UserId
    attachmentId: str
    cardAddOnData: AppsDynamiteSharedCard
    deprecatedAddOnData: ContextualAddOnMarkup
    slackData: AppsDynamiteV1ApiCompatV1Attachment
    slackDataImageUrlHeight: int

@typing.type_check_only
class AuditLoggingSettings(typing_extensions.TypedDict, total=False):
    logAdminReadActions: bool
    logDataReadActions: bool
    logDataWriteActions: bool
    project: str

@typing.type_check_only
class AuthorizedItemId(typing_extensions.TypedDict, total=False):
    id: str
    resourceKey: str

@typing.type_check_only
class AutoComplete(typing_extensions.TypedDict, total=False):
    items: _list[AutoCompleteItem]

@typing.type_check_only
class AutoCompleteItem(typing_extensions.TypedDict, total=False):
    text: str

@typing.type_check_only
class BabelMessageProps(typing_extensions.TypedDict, total=False):
    clientGeneratedId: str
    contentExtension: ChatContentExtension
    deliveryMedium: DeliveryMedium
    eventId: str
    messageContent: ChatConserverMessageContent
    wasUpdatedByBackfill: bool

@typing.type_check_only
class BabelPlaceholderMetadata(typing_extensions.TypedDict, total=False):
    deleteMetadata: DeleteMetadata
    editMetadata: EditMetadata
    hangoutVideoMetadata: HangoutVideoEventMetadata

@typing.type_check_only
class BooleanOperatorOptions(typing_extensions.TypedDict, total=False):
    operatorName: str

@typing.type_check_only
class BooleanPropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: BooleanOperatorOptions

@typing.type_check_only
class BorderStyle(typing_extensions.TypedDict, total=False):
    cornerRadius: int
    strokeColor: str
    type: typing_extensions.Literal["BORDER_TYPE_NOT_SET", "NO_BORDER", "STROKE"]

@typing.type_check_only
class BotInfo(typing_extensions.TypedDict, total=False):
    appAllowlistStatus: typing_extensions.Literal[
        "UNSPECIFIED_STATUS",
        "ALLOWED",
        "ALL_APPS_DISABLED_BY_ADMIN",
        "APP_NOT_ALLOWLISTED_BY_ADMIN",
    ]
    appId: AppId
    botAvatarUrl: str
    botName: str
    description: str
    developerName: str
    marketPlaceBannerUrl: str
    status: typing_extensions.Literal[
        "UNKNOWN_STATUS", "ENABLED", "DISABLED_BY_DEVELOPER"
    ]
    supportHomeScreen: bool
    supportUrls: SupportUrls
    supportedUses: _list[str]

@typing.type_check_only
class BotResponse(typing_extensions.TypedDict, total=False):
    botId: UserId
    requiredAction: typing_extensions.Literal[
        "UNKNOWN_SETUP_TYPE", "CONFIGURATION", "AUTHENTICATION"
    ]
    responseType: typing_extensions.Literal[
        "UNKNOWN_RESPONSE_TYPE",
        "ERROR",
        "SETUP_REQUIRED",
        "DISABLED_BY_ADMIN",
        "DISABLED_BY_DEVELOPER",
        "PRIVATE",
    ]
    setupUrl: str

@typing.type_check_only
class BroadcastAccess(typing_extensions.TypedDict, total=False):
    accessPolicy: typing_extensions.Literal[
        "BROADCASTING_ACCESS_POLICY_UNSPECIFIED", "ORGANIZATION", "PUBLIC"
    ]
    viewUrl: str

@typing.type_check_only
class BroadcastSessionInfo(typing_extensions.TypedDict, total=False):
    broadcastSessionId: str
    broadcastStats: BroadcastStats
    ingestionId: str
    sessionStateInfo: SessionStateInfo

@typing.type_check_only
class BroadcastStats(typing_extensions.TypedDict, total=False):
    estimatedViewerCount: str

@typing.type_check_only
class Button(typing_extensions.TypedDict, total=False):
    imageButton: ImageButton
    textButton: TextButton

@typing.type_check_only
class CallInfo(typing_extensions.TypedDict, total=False):
    abuseReportingConfig: AbuseReportingConfig
    artifactOwner: UserDisplayInfo
    attachedDocuments: _list[DocumentInfo]
    availableReactions: _list[ReactionInfo]
    broadcastSessionInfo: BroadcastSessionInfo
    calendarEventId: str
    chatConfig: ChatConfig
    coActivity: CoActivity
    collaboration: Collaboration
    cseInfo: CseInfo
    maxJoinedDevices: int
    mediaBackendInfo: str
    organizationName: str
    paygateInfo: PaygateInfo
    presenter: Presenter
    recordingInfo: RecordingInfo
    recordingSessionInfo: RecordingSessionInfo
    settings: CallSettings
    streamingSessions: _list[StreamingSessionInfo]
    transcriptionSessionInfo: TranscriptionSessionInfo
    viewerCount: int
    youTubeBroadcastSessionInfos: _list[YouTubeBroadcastSessionInfo]

@typing.type_check_only
class CallSettings(typing_extensions.TypedDict, total=False):
    accessLock: bool
    attendanceReportEnabled: bool
    audioLock: bool
    chatLock: bool
    cseEnabled: bool
    moderationEnabled: bool
    presentLock: bool
    projectDinoEnabled: bool
    reactionsLock: bool
    videoLock: bool

@typing.type_check_only
class CapTokenHolderProto(typing_extensions.TypedDict, total=False):
    tokenHmacSha1Prefix: str

@typing.type_check_only
class Card(typing_extensions.TypedDict, total=False):
    cardActions: _list[CardAction]
    displayStyle: typing_extensions.Literal[
        "DISPLAY_STYLE_UNSPECIFIED", "PEEK", "REPLACE"
    ]
    fixedFooter: FixedFooter
    header: CardHeader
    name: str
    peekCardHeader: CardHeader
    sections: _list[Section]

@typing.type_check_only
class CardAction(typing_extensions.TypedDict, total=False):
    actionLabel: str
    onClick: OnClick

@typing.type_check_only
class CardCapabilityMetadata(typing_extensions.TypedDict, total=False):
    requiredCapabilities: _list[str]

@typing.type_check_only
class CardHeader(typing_extensions.TypedDict, total=False):
    imageAltText: str
    imageStyle: typing_extensions.Literal[
        "CROP_TYPE_NOT_SET", "SQUARE", "CIRCLE", "RECTANGLE_CUSTOM", "RECTANGLE_4_3"
    ]
    imageUrl: str
    subtitle: str
    title: str

@typing.type_check_only
class ChatConfig(typing_extensions.TypedDict, total=False):
    chatType: typing_extensions.Literal[
        "CHAT_TYPE_UNSPECIFIED", "MEET_CHAT", "GOOGLE_CHAT"
    ]
    googleChatConfig: GoogleChatConfig

@typing.type_check_only
class ChatConserverDynamitePlaceholderMetadata(
    typing_extensions.TypedDict, total=False
):
    attachmentMetadata: ChatConserverDynamitePlaceholderMetadataAttachmentMetadata
    botMessageMetadata: ChatConserverDynamitePlaceholderMetadataBotMessageMetadata
    calendarEventMetadata: ChatConserverDynamitePlaceholderMetadataCalendarEventMetadata
    deleteMetadata: ChatConserverDynamitePlaceholderMetadataDeleteMetadata
    editMetadata: ChatConserverDynamitePlaceholderMetadataEditMetadata
    spaceUrl: str
    tasksMetadata: ChatConserverDynamitePlaceholderMetadataTasksMetadata
    videoCallMetadata: ChatConserverDynamitePlaceholderMetadataVideoCallMetadata

@typing.type_check_only
class ChatConserverDynamitePlaceholderMetadataAttachmentMetadata(
    typing_extensions.TypedDict, total=False
):
    filename: str

@typing.type_check_only
class ChatConserverDynamitePlaceholderMetadataBotMessageMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class ChatConserverDynamitePlaceholderMetadataCalendarEventMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class ChatConserverDynamitePlaceholderMetadataDeleteMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class ChatConserverDynamitePlaceholderMetadataEditMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class ChatConserverDynamitePlaceholderMetadataTasksMetadata(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class ChatConserverDynamitePlaceholderMetadataVideoCallMetadata(
    typing_extensions.TypedDict, total=False
):
    meetingUrl: str

@typing.type_check_only
class ChatConserverMessageContent(typing_extensions.TypedDict, total=False):
    attachment: _list[SocialCommonAttachmentAttachment]
    segment: _list[Segment]

@typing.type_check_only
class ChatContentExtension(typing_extensions.TypedDict, total=False):
    annotation: _list[EventAnnotation]
    dynamitePlaceholderMetadata: ChatConserverDynamitePlaceholderMetadata
    eventOtrStatus: typing_extensions.Literal["OFF_THE_RECORD", "ON_THE_RECORD"]
    groupLinkSharingModificationEvent: GroupLinkSharingModificationEvent
    hangoutEvent: HangoutEvent
    inviteAcceptedEvent: InviteAcceptedEvent
    membershipChangeEvent: MembershipChangeEvent
    otrChatMessageEvent: OtrChatMessageEvent
    otrModificationEvent: OtrModificationEvent
    renameEvent: RenameEvent

@typing.type_check_only
class ChatProto(typing_extensions.TypedDict, total=False):
    chatId: str
    memberType: int

@typing.type_check_only
class CheckAccessResponse(typing_extensions.TypedDict, total=False):
    hasAccess: bool

@typing.type_check_only
class CircleProto(typing_extensions.TypedDict, total=False):
    circleId: str
    ownerGaiaId: str
    requiredConsistencyTimestampUsec: str

@typing.type_check_only
class CloudPrincipalProto(typing_extensions.TypedDict, total=False):
    id: str

@typing.type_check_only
class CoActivity(typing_extensions.TypedDict, total=False):
    activityTitle: str
    coActivityApp: typing_extensions.Literal[
        "CO_ACTIVITY_APP_UNSPECIFIED",
        "CO_ACTIVITY_APP_YOU_TUBE_MAIN",
        "CO_ACTIVITY_APP_SPOTIFY",
        "CO_ACTIVITY_APP_UNO",
        "CO_ACTIVITY_APP_HEADSUP",
        "CO_ACTIVITY_APP_KAHOOT",
        "CO_ACTIVITY_APP_GQUEUES",
    ]

@typing.type_check_only
class Collaboration(typing_extensions.TypedDict, total=False):
    attachmentId: str
    initiator: UserDisplayInfo
    uri: str

@typing.type_check_only
class Color(typing_extensions.TypedDict, total=False):
    alpha: float
    blue: float
    green: float
    red: float

@typing.type_check_only
class CommunalLabelTag(typing_extensions.TypedDict, total=False):
    creatorUserId: str
    labelId: str

@typing.type_check_only
class CompositeFilter(typing_extensions.TypedDict, total=False):
    logicOperator: typing_extensions.Literal["AND", "OR", "NOT"]
    subFilters: _list[Filter]

@typing.type_check_only
class ConsentedAppUnfurlMetadata(typing_extensions.TypedDict, total=False):
    clientSpecifiedAppId: UserId

@typing.type_check_only
class ContactGroupProto(typing_extensions.TypedDict, total=False):
    groupId: str
    ownerGaiaId: str
    requiredConsistencyTimestampUsec: str

@typing.type_check_only
class ContentReport(typing_extensions.TypedDict, total=False):
    reportCreateTimestamp: str
    reportJustification: ContentReportJustification
    reportType: AppsDynamiteSharedContentReportType
    reporterUserId: UserId
    revisionCreateTimestamp: str

@typing.type_check_only
class ContentReportJustification(typing_extensions.TypedDict, total=False):
    userJustification: str

@typing.type_check_only
class ContentReportSummary(typing_extensions.TypedDict, total=False):
    numberReports: int
    numberReportsAllRevisions: int

@typing.type_check_only
class ContextAttribute(typing_extensions.TypedDict, total=False):
    name: str
    values: _list[str]

@typing.type_check_only
class ContextualAddOnMarkup(typing_extensions.TypedDict, total=False):
    cards: _list[Card]
    toolbar: Toolbar

@typing.type_check_only
class CseInfo(typing_extensions.TypedDict, total=False):
    cseDomain: str
    wrappedKey: str

@typing.type_check_only
class CustomEmojiMetadata(typing_extensions.TypedDict, total=False):
    customEmoji: AppsDynamiteSharedCustomEmoji

@typing.type_check_only
class CustomerId(typing_extensions.TypedDict, total=False):
    customerId: str

@typing.type_check_only
class CustomerIndexStats(typing_extensions.TypedDict, total=False):
    date: Date
    itemCountByStatus: _list[ItemCountByStatus]

@typing.type_check_only
class CustomerQueryStats(typing_extensions.TypedDict, total=False):
    date: Date
    queryCountByStatus: _list[QueryCountByStatus]

@typing.type_check_only
class CustomerSearchApplicationStats(typing_extensions.TypedDict, total=False):
    count: str
    date: Date

@typing.type_check_only
class CustomerSessionStats(typing_extensions.TypedDict, total=False):
    date: Date
    searchSessionsCount: str

@typing.type_check_only
class CustomerSettings(typing_extensions.TypedDict, total=False):
    auditLoggingSettings: AuditLoggingSettings
    vpcSettings: VPCSettings

@typing.type_check_only
class CustomerUserStats(typing_extensions.TypedDict, total=False):
    date: Date
    oneDayActiveUsersCount: str
    sevenDaysActiveUsersCount: str
    thirtyDaysActiveUsersCount: str

@typing.type_check_only
class DataLossPreventionMetadata(typing_extensions.TypedDict, total=False):
    dlpScanSummary: DlpScanSummary
    warnAcknowledged: bool

@typing.type_check_only
class DataSource(typing_extensions.TypedDict, total=False):
    disableModifications: bool
    disableServing: bool
    displayName: str
    indexingServiceAccounts: _list[str]
    itemsVisibility: _list[GSuitePrincipal]
    name: str
    operationIds: _list[str]
    returnThumbnailUrls: bool
    shortName: str

@typing.type_check_only
class DataSourceIndexStats(typing_extensions.TypedDict, total=False):
    date: Date
    itemCountByStatus: _list[ItemCountByStatus]

@typing.type_check_only
class DataSourceRestriction(typing_extensions.TypedDict, total=False):
    filterOptions: _list[FilterOptions]
    source: Source

@typing.type_check_only
class Date(typing_extensions.TypedDict, total=False):
    day: int
    month: int
    year: int

@typing.type_check_only
class DateOperatorOptions(typing_extensions.TypedDict, total=False):
    greaterThanOperatorName: str
    lessThanOperatorName: str
    operatorName: str

@typing.type_check_only
class DatePropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: DateOperatorOptions

@typing.type_check_only
class DateTimePicker(typing_extensions.TypedDict, total=False):
    label: str
    name: str
    onChange: FormAction
    timezoneOffsetDate: int
    type: typing_extensions.Literal[
        "UNSPECIFIED_TYPE", "DATE_AND_TIME", "DATE_ONLY", "TIME_ONLY"
    ]
    valueMsEpoch: str

@typing.type_check_only
class DateValues(typing_extensions.TypedDict, total=False):
    values: _list[Date]

@typing.type_check_only
class DebugOptions(typing_extensions.TypedDict, total=False):
    enableDebugging: bool

@typing.type_check_only
class DeepLinkData(typing_extensions.TypedDict, total=False):
    appId: str
    client: _list[PackagingServiceClient]
    deepLinkId: str
    url: str

@typing.type_check_only
class DeleteMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeleteQueueItemsRequest(typing_extensions.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions
    queue: str

@typing.type_check_only
class DeliveryMedium(typing_extensions.TypedDict, total=False):
    mediumType: typing_extensions.Literal[
        "UNKNOWN_MEDIUM", "BABEL_MEDIUM", "GOOGLE_VOICE_MEDIUM", "LOCAL_SMS_MEDIUM"
    ]
    selfPhone: VoicePhoneNumber

@typing.type_check_only
class DisplayedProperty(typing_extensions.TypedDict, total=False):
    propertyName: str

@typing.type_check_only
class Divider(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DlpScanSummary(typing_extensions.TypedDict, total=False):
    scanId: str
    scanNotApplicableForContext: bool
    scanOutcome: typing_extensions.Literal[
        "SCAN_UNKNOWN_OUTCOME",
        "SCAN_SUCCEEDED_NO_VIOLATION",
        "SCAN_SUCCEEDED_BLOCK",
        "SCAN_SUCCEEDED_WARN",
        "SCAN_SUCCEEDED_AUDIT_ONLY",
        "SCAN_FAILURE_EXCEPTION",
        "SCAN_FAILURE_TIMEOUT",
        "SCAN_FAILURE_ALL_RULES_FAILED",
        "SCAN_FAILURE_ILLEGAL_STATE_FOR_ATTACHMENTS",
        "SCAN_SKIPPED_EXPERIMENT_DISABLED",
        "SCAN_SKIPPED_CONSUMER",
        "SCAN_SKIPPED_NON_HUMAN_USER",
        "SCAN_SKIPPED_NO_MESSAGE",
        "SCAN_SKIPPED_USER_ACKNOWLEDGED_WARNING",
        "SCAN_SKIPPED_MESSAGE_FROM_UNSUPPORTED_ORIGIN",
        "SCAN_RULE_EVALUATION_SKIPPED_NO_RULES_FOUND",
        "SCAN_RULE_EVALUATION_SKIPPED_NO_APPLICABLE_RULES_FOR_ACTION_PARAMS",
        "SCAN_RULE_EVALUATION_SKIPPED_NO_APPLICABLE_RULES_FOR_TRIGGER",
        "SCAN_RULE_EVALUATION_SKIPPED_CHANGELING_PERMANENT_ERROR",
        "SCAN_RULE_EVALUATION_SKIPPED_CHANGELING_EMPTY_RESPONSE",
        "SCAN_SUCCEEDED_WITH_FAILURES_NO_VIOLATION",
        "SCAN_SUCCEEDED_WITH_FAILURES_BLOCK",
        "SCAN_SUCCEEDED_WITH_FAILURES_WARN",
        "SCAN_SUCCEEDED_WITH_FAILURES_AUDIT_ONLY",
    ]

@typing.type_check_only
class DmId(typing_extensions.TypedDict, total=False):
    dmId: str

@typing.type_check_only
class DocumentInfo(typing_extensions.TypedDict, total=False):
    whiteboardInfo: WhiteboardInfo

@typing.type_check_only
class DoubleOperatorOptions(typing_extensions.TypedDict, total=False):
    operatorName: str

@typing.type_check_only
class DoublePropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: DoubleOperatorOptions

@typing.type_check_only
class DoubleValues(typing_extensions.TypedDict, total=False):
    values: _list[float]

@typing.type_check_only
class DriveFollowUpRestrict(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "UNSPECIFIED", "FOLLOWUP_SUGGESTIONS", "FOLLOWUP_ACTION_ITEMS"
    ]

@typing.type_check_only
class DriveLocationRestrict(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["UNSPECIFIED", "TRASHED", "STARRED"]

@typing.type_check_only
class DriveMetadata(typing_extensions.TypedDict, total=False):
    aclFixRequest: AclFixRequest
    aclFixStatus: AclFixStatus
    canEdit: bool
    canShare: bool
    canView: bool
    driveAction: typing_extensions.Literal[
        "DRIVE_ACTION_UNSPECIFIED",
        "ADD_TO_DRIVE",
        "ORGANIZE",
        "ADD_SHORTCUT",
        "ADD_ANOTHER_SHORTCUT",
    ]
    driveState: typing_extensions.Literal[
        "DRIVE_STATE_UNSPECIFIED",
        "IN_MY_DRIVE",
        "IN_TEAM_DRIVE",
        "SHARED_IN_DRIVE",
        "NOT_IN_DRIVE",
    ]
    embedUrl: TrustedResourceUrlProto
    encryptedDocId: bool
    encryptedResourceKey: str
    externalMimetype: str
    id: str
    isDownloadRestricted: bool
    isOwner: bool
    legacyUploadMetadata: LegacyUploadMetadata
    mimetype: str
    organizationDisplayName: str
    shortcutAuthorizedItemId: AuthorizedItemId
    shouldNotRender: bool
    thumbnailHeight: int
    thumbnailUrl: str
    thumbnailWidth: int
    title: str
    urlFragment: str
    wrappedResourceKey: WrappedResourceKey

@typing.type_check_only
class DriveMimeTypeRestrict(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "UNSPECIFIED",
        "PDF",
        "DOCUMENT",
        "PRESENTATION",
        "SPREADSHEET",
        "FORM",
        "DRAWING",
        "SCRIPT",
        "MAP",
        "IMAGE",
        "AUDIO",
        "VIDEO",
        "FOLDER",
        "ARCHIVE",
        "SITE",
    ]

@typing.type_check_only
class DriveTimeSpanRestrict(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "UNSPECIFIED",
        "TODAY",
        "YESTERDAY",
        "LAST_7_DAYS",
        "LAST_30_DAYS",
        "LAST_90_DAYS",
    ]

@typing.type_check_only
class DynamiteSpacesScoringInfo(typing_extensions.TypedDict, total=False):
    affinityScore: float
    commonContactCountAffinityScore: float
    contactsIntersectionCount: float
    finalScore: float
    freshnessScore: float
    joinedSpacesAffinityScore: float
    lastMessagePostedTimestampSecs: str
    lastReadTimestampSecs: str
    memberMetadataCount: float
    messageScore: float
    numAucContacts: str
    smallContactListAffinityScore: float
    smallUnjoinedSpacesAffinityScore: float
    spaceAgeInDays: float
    spaceCreationTimestampSecs: str
    topicalityScore: float

@typing.type_check_only
class EditMetadata(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EmailAddress(typing_extensions.TypedDict, total=False):
    customType: str
    emailAddress: str
    emailUrl: str
    primary: bool
    type: str

@typing.type_check_only
class EmailOwnerProto(typing_extensions.TypedDict, total=False):
    email: str

@typing.type_check_only
class EmbedClientItem(typing_extensions.TypedDict, total=False):
    canonicalId: str
    deepLinkData: DeepLinkData
    id: str
    provenance: Provenance
    renderId: str
    signature: str
    transientData: TransientData
    type: _list[str]

@typing.type_check_only
class EnumOperatorOptions(typing_extensions.TypedDict, total=False):
    operatorName: str

@typing.type_check_only
class EnumPropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: EnumOperatorOptions
    orderedRanking: typing_extensions.Literal["NO_ORDER", "ASCENDING", "DESCENDING"]
    possibleValues: _list[EnumValuePair]

@typing.type_check_only
class EnumValuePair(typing_extensions.TypedDict, total=False):
    integerValue: int
    stringValue: str

@typing.type_check_only
class EnumValues(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class ErrorInfo(typing_extensions.TypedDict, total=False):
    errorMessages: _list[ErrorMessage]

@typing.type_check_only
class ErrorMessage(typing_extensions.TypedDict, total=False):
    errorMessage: str
    source: Source

@typing.type_check_only
class EventAnnotation(typing_extensions.TypedDict, total=False):
    type: int
    value: str

@typing.type_check_only
class EventProto(typing_extensions.TypedDict, total=False):
    eventId: str
    memberType: int

@typing.type_check_only
class FacetBucket(typing_extensions.TypedDict, total=False):
    count: int
    percentage: int
    value: Value

@typing.type_check_only
class FacetOptions(typing_extensions.TypedDict, total=False):
    numFacetBuckets: int
    objectType: str
    operatorName: str
    sourceName: str

@typing.type_check_only
class FacetResult(typing_extensions.TypedDict, total=False):
    buckets: _list[FacetBucket]
    objectType: str
    operatorName: str
    sourceName: str

@typing.type_check_only
class FieldViolation(typing_extensions.TypedDict, total=False):
    description: str
    field: str

@typing.type_check_only
class Filter(dict[str, typing.Any]): ...

@typing.type_check_only
class FilterOptions(dict[str, typing.Any]): ...

@typing.type_check_only
class FixedFooter(typing_extensions.TypedDict, total=False):
    buttons: _list[Button]
    primaryButton: TextButton
    secondaryButton: TextButton

@typing.type_check_only
class FormAction(typing_extensions.TypedDict, total=False):
    actionMethodName: str
    loadIndicator: typing_extensions.Literal["SPINNER", "NONE"]
    parameters: _list[ActionParameter]
    persistValues: bool

@typing.type_check_only
class FormatMetadata(typing_extensions.TypedDict, total=False):
    fontColor: int
    formatType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "BOLD",
        "ITALIC",
        "STRIKE",
        "SOURCE_CODE",
        "MONOSPACE",
        "HIDDEN",
        "MONOSPACE_BLOCK",
        "UNDERLINE",
        "FONT_COLOR",
        "BULLETED_LIST",
        "BULLETED_LIST_ITEM",
        "CLIENT_HIDDEN",
    ]

@typing.type_check_only
class Formatting(typing_extensions.TypedDict, total=False):
    bold: bool
    highlight: bool
    italics: bool
    strikethrough: bool
    style: typing_extensions.Literal[
        "UNKNOWN_STYLE", "HEADING_1", "HEADING_2", "HEADING_3", "HEADING_4"
    ]
    underline: bool

@typing.type_check_only
class FreshnessOptions(typing_extensions.TypedDict, total=False):
    freshnessDuration: str
    freshnessProperty: str

@typing.type_check_only
class GSuitePrincipal(typing_extensions.TypedDict, total=False):
    gsuiteDomain: bool
    gsuiteGroupEmail: str
    gsuiteUserEmail: str

@typing.type_check_only
class GaiaGroupProto(typing_extensions.TypedDict, total=False):
    groupId: str

@typing.type_check_only
class GaiaUserProto(typing_extensions.TypedDict, total=False):
    userId: str

@typing.type_check_only
class GatewayAccess(typing_extensions.TypedDict, total=False):
    enabled: bool

@typing.type_check_only
class GatewaySipAccess(typing_extensions.TypedDict, total=False):
    sipAccessCode: str
    uri: str

@typing.type_check_only
class GetCustomerIndexStatsResponse(typing_extensions.TypedDict, total=False):
    averageIndexedItemCount: str
    stats: _list[CustomerIndexStats]

@typing.type_check_only
class GetCustomerQueryStatsResponse(typing_extensions.TypedDict, total=False):
    stats: _list[CustomerQueryStats]
    totalQueryCount: str

@typing.type_check_only
class GetCustomerSearchApplicationStatsResponse(
    typing_extensions.TypedDict, total=False
):
    averageSearchApplicationCount: str
    stats: _list[CustomerSearchApplicationStats]

@typing.type_check_only
class GetCustomerSessionStatsResponse(typing_extensions.TypedDict, total=False):
    stats: _list[CustomerSessionStats]

@typing.type_check_only
class GetCustomerUserStatsResponse(typing_extensions.TypedDict, total=False):
    stats: _list[CustomerUserStats]

@typing.type_check_only
class GetDataSourceIndexStatsResponse(typing_extensions.TypedDict, total=False):
    averageIndexedItemCount: str
    stats: _list[DataSourceIndexStats]

@typing.type_check_only
class GetSearchApplicationQueryStatsResponse(typing_extensions.TypedDict, total=False):
    stats: _list[SearchApplicationQueryStats]
    totalQueryCount: str

@typing.type_check_only
class GetSearchApplicationSessionStatsResponse(
    typing_extensions.TypedDict, total=False
):
    stats: _list[SearchApplicationSessionStats]

@typing.type_check_only
class GetSearchApplicationUserStatsResponse(typing_extensions.TypedDict, total=False):
    stats: _list[SearchApplicationUserStats]

@typing.type_check_only
class GoogleChatConfig(typing_extensions.TypedDict, total=False):
    chatGroupId: str

@typing.type_check_only
class GoogleChatV1ContextualAddOnMarkup(typing_extensions.TypedDict, total=False):
    cards: _list[GoogleChatV1ContextualAddOnMarkupCard]

@typing.type_check_only
class GoogleChatV1ContextualAddOnMarkupCard(typing_extensions.TypedDict, total=False):
    cardActions: _list[GoogleChatV1ContextualAddOnMarkupCardCardAction]
    header: GoogleChatV1ContextualAddOnMarkupCardCardHeader
    name: str
    sections: _list[GoogleChatV1ContextualAddOnMarkupCardSection]

@typing.type_check_only
class GoogleChatV1ContextualAddOnMarkupCardCardAction(
    typing_extensions.TypedDict, total=False
):
    actionLabel: str
    onClick: GoogleChatV1WidgetMarkupOnClick

@typing.type_check_only
class GoogleChatV1ContextualAddOnMarkupCardCardHeader(
    typing_extensions.TypedDict, total=False
):
    imageStyle: typing_extensions.Literal["IMAGE_STYLE_UNSPECIFIED", "IMAGE", "AVATAR"]
    imageUrl: str
    subtitle: str
    title: str

@typing.type_check_only
class GoogleChatV1ContextualAddOnMarkupCardSection(
    typing_extensions.TypedDict, total=False
):
    header: str
    widgets: _list[GoogleChatV1WidgetMarkup]

@typing.type_check_only
class GoogleChatV1WidgetMarkup(typing_extensions.TypedDict, total=False):
    buttons: _list[GoogleChatV1WidgetMarkupButton]
    image: GoogleChatV1WidgetMarkupImage
    keyValue: GoogleChatV1WidgetMarkupKeyValue
    textParagraph: GoogleChatV1WidgetMarkupTextParagraph

@typing.type_check_only
class GoogleChatV1WidgetMarkupButton(typing_extensions.TypedDict, total=False):
    imageButton: GoogleChatV1WidgetMarkupImageButton
    textButton: GoogleChatV1WidgetMarkupTextButton

@typing.type_check_only
class GoogleChatV1WidgetMarkupFormAction(typing_extensions.TypedDict, total=False):
    actionMethodName: str
    parameters: _list[GoogleChatV1WidgetMarkupFormActionActionParameter]

@typing.type_check_only
class GoogleChatV1WidgetMarkupFormActionActionParameter(
    typing_extensions.TypedDict, total=False
):
    key: str
    value: str

@typing.type_check_only
class GoogleChatV1WidgetMarkupImage(typing_extensions.TypedDict, total=False):
    aspectRatio: float
    imageUrl: str
    onClick: GoogleChatV1WidgetMarkupOnClick

@typing.type_check_only
class GoogleChatV1WidgetMarkupImageButton(typing_extensions.TypedDict, total=False):
    icon: typing_extensions.Literal[
        "ICON_UNSPECIFIED",
        "AIRPLANE",
        "BOOKMARK",
        "BUS",
        "CAR",
        "CLOCK",
        "CONFIRMATION_NUMBER_ICON",
        "DOLLAR",
        "DESCRIPTION",
        "EMAIL",
        "EVENT_PERFORMER",
        "EVENT_SEAT",
        "FLIGHT_ARRIVAL",
        "FLIGHT_DEPARTURE",
        "HOTEL",
        "HOTEL_ROOM_TYPE",
        "INVITE",
        "MAP_PIN",
        "MEMBERSHIP",
        "MULTIPLE_PEOPLE",
        "OFFER",
        "PERSON",
        "PHONE",
        "RESTAURANT_ICON",
        "SHOPPING_CART",
        "STAR",
        "STORE",
        "TICKET",
        "TRAIN",
        "VIDEO_CAMERA",
        "VIDEO_PLAY",
    ]
    iconUrl: str
    name: str
    onClick: GoogleChatV1WidgetMarkupOnClick

@typing.type_check_only
class GoogleChatV1WidgetMarkupKeyValue(typing_extensions.TypedDict, total=False):
    bottomLabel: str
    button: GoogleChatV1WidgetMarkupButton
    content: str
    contentMultiline: bool
    icon: typing_extensions.Literal[
        "ICON_UNSPECIFIED",
        "AIRPLANE",
        "BOOKMARK",
        "BUS",
        "CAR",
        "CLOCK",
        "CONFIRMATION_NUMBER_ICON",
        "DOLLAR",
        "DESCRIPTION",
        "EMAIL",
        "EVENT_PERFORMER",
        "EVENT_SEAT",
        "FLIGHT_ARRIVAL",
        "FLIGHT_DEPARTURE",
        "HOTEL",
        "HOTEL_ROOM_TYPE",
        "INVITE",
        "MAP_PIN",
        "MEMBERSHIP",
        "MULTIPLE_PEOPLE",
        "OFFER",
        "PERSON",
        "PHONE",
        "RESTAURANT_ICON",
        "SHOPPING_CART",
        "STAR",
        "STORE",
        "TICKET",
        "TRAIN",
        "VIDEO_CAMERA",
        "VIDEO_PLAY",
    ]
    iconUrl: str
    onClick: GoogleChatV1WidgetMarkupOnClick
    topLabel: str

@typing.type_check_only
class GoogleChatV1WidgetMarkupOnClick(typing_extensions.TypedDict, total=False):
    action: GoogleChatV1WidgetMarkupFormAction
    openLink: GoogleChatV1WidgetMarkupOpenLink

@typing.type_check_only
class GoogleChatV1WidgetMarkupOpenLink(typing_extensions.TypedDict, total=False):
    url: str

@typing.type_check_only
class GoogleChatV1WidgetMarkupTextButton(typing_extensions.TypedDict, total=False):
    onClick: GoogleChatV1WidgetMarkupOnClick
    text: str

@typing.type_check_only
class GoogleChatV1WidgetMarkupTextParagraph(typing_extensions.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleDocsMetadata(typing_extensions.TypedDict, total=False):
    aclInfo: AclInfo
    documentType: typing_extensions.Literal[
        "UNKNOWN",
        "DOCUMENT",
        "PRESENTATION",
        "SPREADSHEET",
        "PDF",
        "IMAGE",
        "BINARY_BLOB",
        "FUSION_TABLE",
        "FOLDER",
        "DRAWING",
        "VIDEO",
        "FORM",
        "DRAFT_SITE",
        "DRAFT_SITE_PAGE",
        "JAM",
        "SHORTCUT",
        "SCRIPT",
    ]
    fileExtension: str
    lastContentModifiedTimestamp: str
    numSubscribers: int
    numViewers: int
    resultInfo: GoogleDocsResultInfo
    typeInfo: TypeInfo

@typing.type_check_only
class GoogleDocsResultInfo(typing_extensions.TypedDict, total=False):
    attachmentSha1: str
    cosmoId: Id
    cosmoNameSpace: int
    encryptedId: str
    mimeType: str
    shareScope: ShareScope

@typing.type_check_only
class Grid(typing_extensions.TypedDict, total=False):
    borderStyle: BorderStyle
    items: _list[GridItem]
    numColumns: int
    onClick: OnClick
    title: str

@typing.type_check_only
class GridItem(typing_extensions.TypedDict, total=False):
    identifier: str
    image: ImageComponent
    layout: typing_extensions.Literal["NOT_SET", "TEXT_BELOW", "TEXT_ABOVE"]
    subtitle: str
    textAlignment: typing_extensions.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END"
    ]
    title: str

@typing.type_check_only
class GroupDetailsUpdatedMetadata(typing_extensions.TypedDict, total=False):
    newGroupDetails: AppsDynamiteSharedGroupDetails
    prevGroupDetails: AppsDynamiteSharedGroupDetails

@typing.type_check_only
class GroupId(typing_extensions.TypedDict, total=False):
    dmId: DmId
    spaceId: SpaceId

@typing.type_check_only
class GroupLinkSharingModificationEvent(typing_extensions.TypedDict, total=False):
    newStatus: typing_extensions.Literal[
        "UNKNOWN_LINK_SHARING_STATUS",
        "LINK_SHARING_ON",
        "LINK_SHARING_OFF",
        "NOT_AVAILABLE",
    ]

@typing.type_check_only
class GroupRetentionSettingsUpdatedMetaData(typing_extensions.TypedDict, total=False):
    initiator: UserId
    retentionSettings: AppsDynamiteSharedRetentionSettings

@typing.type_check_only
class GsuiteIntegrationMetadata(typing_extensions.TypedDict, total=False):
    activityFeedData: AppsDynamiteSharedActivityFeedAnnotationData
    assistantData: AppsDynamiteSharedAssistantAnnotationData
    calendarEventData: AppsDynamiteSharedCalendarEventAnnotationData
    callData: AppsDynamiteSharedCallAnnotationData
    clientType: typing_extensions.Literal[
        "UNKNOWN_CLIENT_TYPE",
        "MEET",
        "TASKS",
        "CALENDAR_EVENT",
        "ASSISTANT",
        "ACTIVITY_FEED_SERVICE",
    ]
    indexableTexts: _list[str]
    tasksData: AppsDynamiteSharedTasksAnnotationData

@typing.type_check_only
class HangoutEvent(typing_extensions.TypedDict, total=False):
    hangoutDurationSecs: str
    mediaType: typing_extensions.Literal["AUDIO_VIDEO", "AUDIO_ONLY", "PUSH_TO_TALK"]
    participantId: _list[StoredParticipantId]
    type: typing_extensions.Literal[
        "START_HANGOUT",
        "JOIN_HANGOUT",
        "LEAVE_HANGOUT",
        "END_HANGOUT",
        "HANGOUT_COMING_SOON",
        "ONGOING_HANGOUT",
    ]

@typing.type_check_only
class HangoutVideoEventMetadata(typing_extensions.TypedDict, total=False):
    hangoutVideoType: typing_extensions.Literal[
        "UNKNOWN_HANGOUT_VIDEO_EVENT_TYPE", "VIDEO_START", "VIDEO_END"
    ]

@typing.type_check_only
class HashtagData(typing_extensions.TypedDict, total=False):
    searchText: str

@typing.type_check_only
class HostProto(typing_extensions.TypedDict, total=False):
    hostName: str
    hostOwner: str

@typing.type_check_only
class HtmlOperatorOptions(typing_extensions.TypedDict, total=False):
    operatorName: str

@typing.type_check_only
class HtmlPropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: HtmlOperatorOptions
    retrievalImportance: RetrievalImportance

@typing.type_check_only
class HtmlValues(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class IconImage(typing_extensions.TypedDict, total=False):
    altText: str
    icon: typing_extensions.Literal[
        "NONE",
        "AIRPLANE",
        "BOOKMARK",
        "BUS",
        "CAR",
        "CLOCK",
        "CONFIRMATION_NUMBER_ICON",
        "DOLLAR",
        "DESCRIPTION",
        "EDIT",
        "EDIT_NOTE",
        "EMAIL",
        "EVENT_PERFORMER",
        "EVENT_SEAT",
        "FLIGHT_ARRIVAL",
        "FLIGHT_DEPARTURE",
        "HOTEL",
        "HOTEL_ROOM_TYPE",
        "INVITE",
        "MAP_PIN",
        "MEMBERSHIP",
        "MULTIPLE_PEOPLE",
        "OFFER",
        "OPEN_IN_NEW",
        "PERSON",
        "PHONE",
        "RESTAURANT_ICON",
        "SHOPPING_CART",
        "STAR",
        "STORE",
        "TICKET",
        "TRAIN",
        "VIDEO_CAMERA",
        "VIDEO_PLAY",
    ]
    iconUrl: str
    imageStyle: typing_extensions.Literal[
        "CROP_TYPE_NOT_SET", "SQUARE", "CIRCLE", "RECTANGLE_CUSTOM", "RECTANGLE_4_3"
    ]

@typing.type_check_only
class Id(typing_extensions.TypedDict, total=False):
    creatorUserId: str
    localId: str
    nameSpace: int

@typing.type_check_only
class Image(typing_extensions.TypedDict, total=False):
    altText: str
    aspectRatio: float
    imageUrl: str
    onClick: OnClick

@typing.type_check_only
class ImageButton(typing_extensions.TypedDict, total=False):
    icon: typing_extensions.Literal[
        "NONE",
        "AIRPLANE",
        "BOOKMARK",
        "BUS",
        "CAR",
        "CLOCK",
        "CONFIRMATION_NUMBER_ICON",
        "DOLLAR",
        "DESCRIPTION",
        "EDIT",
        "EDIT_NOTE",
        "EMAIL",
        "EVENT_PERFORMER",
        "EVENT_SEAT",
        "FLIGHT_ARRIVAL",
        "FLIGHT_DEPARTURE",
        "HOTEL",
        "HOTEL_ROOM_TYPE",
        "INVITE",
        "MAP_PIN",
        "MEMBERSHIP",
        "MULTIPLE_PEOPLE",
        "OFFER",
        "OPEN_IN_NEW",
        "PERSON",
        "PHONE",
        "RESTAURANT_ICON",
        "SHOPPING_CART",
        "STAR",
        "STORE",
        "TICKET",
        "TRAIN",
        "VIDEO_CAMERA",
        "VIDEO_PLAY",
    ]
    iconUrl: str
    name: str
    onClick: OnClick

@typing.type_check_only
class ImageComponent(typing_extensions.TypedDict, total=False):
    altText: str
    borderStyle: BorderStyle
    cropStyle: ImageCropStyle
    imageUrl: str

@typing.type_check_only
class ImageCropStyle(typing_extensions.TypedDict, total=False):
    aspectRatio: float
    type: typing_extensions.Literal[
        "CROP_TYPE_NOT_SET", "SQUARE", "CIRCLE", "RECTANGLE_CUSTOM", "RECTANGLE_4_3"
    ]

@typing.type_check_only
class ImageKeyValue(typing_extensions.TypedDict, total=False):
    icon: typing_extensions.Literal[
        "NONE",
        "AIRPLANE",
        "BOOKMARK",
        "BUS",
        "CAR",
        "CLOCK",
        "CONFIRMATION_NUMBER_ICON",
        "DOLLAR",
        "DESCRIPTION",
        "EDIT",
        "EDIT_NOTE",
        "EMAIL",
        "EVENT_PERFORMER",
        "EVENT_SEAT",
        "FLIGHT_ARRIVAL",
        "FLIGHT_DEPARTURE",
        "HOTEL",
        "HOTEL_ROOM_TYPE",
        "INVITE",
        "MAP_PIN",
        "MEMBERSHIP",
        "MULTIPLE_PEOPLE",
        "OFFER",
        "OPEN_IN_NEW",
        "PERSON",
        "PHONE",
        "RESTAURANT_ICON",
        "SHOPPING_CART",
        "STAR",
        "STORE",
        "TICKET",
        "TRAIN",
        "VIDEO_CAMERA",
        "VIDEO_PLAY",
    ]
    iconUrl: str
    onClick: OnClick
    text: str

@typing.type_check_only
class IncomingWebhookChangedMetadata(typing_extensions.TypedDict, total=False):
    incomingWebhookName: str
    initiatorId: UserId
    initiatorProfile: User
    obfuscatedIncomingWebhookId: str
    oldIncomingWebhookName: str
    type: typing_extensions.Literal[
        "UNSPECIFIED",
        "ADDED",
        "UPDATED",
        "REMOVED",
        "UPDATED_NAME",
        "UPDATED_AVATAR",
        "UPDATED_NAME_AND_AVATAR",
    ]

@typing.type_check_only
class IndexItemOptions(typing_extensions.TypedDict, total=False):
    allowUnknownGsuitePrincipals: bool

@typing.type_check_only
class IndexItemRequest(typing_extensions.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions
    indexItemOptions: IndexItemOptions
    item: Item
    mode: typing_extensions.Literal["UNSPECIFIED", "SYNCHRONOUS", "ASYNCHRONOUS"]

@typing.type_check_only
class InitializeCustomerRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class IntegerOperatorOptions(typing_extensions.TypedDict, total=False):
    greaterThanOperatorName: str
    lessThanOperatorName: str
    operatorName: str

@typing.type_check_only
class IntegerPropertyOptions(typing_extensions.TypedDict, total=False):
    maximumValue: str
    minimumValue: str
    operatorOptions: IntegerOperatorOptions
    orderedRanking: typing_extensions.Literal["NO_ORDER", "ASCENDING", "DESCENDING"]

@typing.type_check_only
class IntegerValues(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class IntegrationConfigMutation(typing_extensions.TypedDict, total=False):
    addApp: AppId
    addPinnedItem: PinnedItemId
    removeApp: AppId
    removePinnedItem: PinnedItemId

@typing.type_check_only
class IntegrationConfigUpdatedMetadata(typing_extensions.TypedDict, total=False):
    initiatorId: UserId
    mutations: _list[IntegrationConfigMutation]

@typing.type_check_only
class Interaction(typing_extensions.TypedDict, total=False):
    interactionTime: str
    principal: Principal
    type: typing_extensions.Literal["UNSPECIFIED", "VIEW", "EDIT"]

@typing.type_check_only
class InviteAcceptedEvent(typing_extensions.TypedDict, total=False):
    participantId: _list[StoredParticipantId]

@typing.type_check_only
class InviteeInfo(typing_extensions.TypedDict, total=False):
    email: str
    userId: UserId

@typing.type_check_only
class Item(dict[str, typing.Any]): ...

@typing.type_check_only
class ItemAcl(typing_extensions.TypedDict, total=False):
    aclInheritanceType: typing_extensions.Literal[
        "NOT_APPLICABLE", "CHILD_OVERRIDE", "PARENT_OVERRIDE", "BOTH_PERMIT"
    ]
    deniedReaders: _list[Principal]
    inheritAclFrom: str
    owners: _list[Principal]
    readers: _list[Principal]

@typing.type_check_only
class ItemContent(typing_extensions.TypedDict, total=False):
    contentDataRef: UploadItemRef
    contentFormat: typing_extensions.Literal["UNSPECIFIED", "HTML", "TEXT", "RAW"]
    hash: str
    inlineContent: str

@typing.type_check_only
class ItemCountByStatus(typing_extensions.TypedDict, total=False):
    count: str
    indexedItemsCount: str
    statusCode: typing_extensions.Literal[
        "CODE_UNSPECIFIED", "ERROR", "MODIFIED", "NEW_ITEM", "ACCEPTED"
    ]

@typing.type_check_only
class ItemMetadata(typing_extensions.TypedDict, total=False):
    containerName: str
    contentLanguage: str
    contextAttributes: _list[ContextAttribute]
    createTime: str
    hash: str
    interactions: _list[Interaction]
    keywords: _list[str]
    mimeType: str
    objectType: str
    searchQualityMetadata: SearchQualityMetadata
    sourceRepositoryUrl: str
    title: str
    updateTime: str

@typing.type_check_only
class ItemStatus(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "CODE_UNSPECIFIED", "ERROR", "MODIFIED", "NEW_ITEM", "ACCEPTED"
    ]
    processingErrors: _list[ProcessingError]
    repositoryErrors: _list[RepositoryError]

@typing.type_check_only
class ItemStructuredData(dict[str, typing.Any]): ...

@typing.type_check_only
class KeyValue(typing_extensions.TypedDict, total=False):
    bottomLabel: str
    button: Button
    content: str
    contentMultiline: bool
    endIcon: IconImage
    icon: typing_extensions.Literal[
        "NONE",
        "AIRPLANE",
        "BOOKMARK",
        "BUS",
        "CAR",
        "CLOCK",
        "CONFIRMATION_NUMBER_ICON",
        "DOLLAR",
        "DESCRIPTION",
        "EDIT",
        "EDIT_NOTE",
        "EMAIL",
        "EVENT_PERFORMER",
        "EVENT_SEAT",
        "FLIGHT_ARRIVAL",
        "FLIGHT_DEPARTURE",
        "HOTEL",
        "HOTEL_ROOM_TYPE",
        "INVITE",
        "MAP_PIN",
        "MEMBERSHIP",
        "MULTIPLE_PEOPLE",
        "OFFER",
        "OPEN_IN_NEW",
        "PERSON",
        "PHONE",
        "RESTAURANT_ICON",
        "SHOPPING_CART",
        "STAR",
        "STORE",
        "TICKET",
        "TRAIN",
        "VIDEO_CAMERA",
        "VIDEO_PLAY",
    ]
    iconAltText: str
    iconUrl: str
    imageStyle: typing_extensions.Literal[
        "CROP_TYPE_NOT_SET", "SQUARE", "CIRCLE", "RECTANGLE_CUSTOM", "RECTANGLE_4_3"
    ]
    onClick: OnClick
    startIcon: IconImage
    switchWidget: SwitchWidget
    topLabel: str

@typing.type_check_only
class LanguageConfig(typing_extensions.TypedDict, total=False):
    spokenLanguages: _list[str]

@typing.type_check_only
class LdapGroupProto(typing_extensions.TypedDict, total=False):
    groupName: str

@typing.type_check_only
class LdapUserProto(typing_extensions.TypedDict, total=False):
    userName: str

@typing.type_check_only
class LegacyUploadMetadata(typing_extensions.TypedDict, total=False):
    legacyUniqueId: str
    uploadMetadata: UploadMetadata

@typing.type_check_only
class LinkData(typing_extensions.TypedDict, total=False):
    attachment: SocialCommonAttachmentAttachment
    attachmentRenderHint: typing_extensions.Literal[
        "ATTACHMENT_RENDER_HINT_UNKNOWN",
        "ATTACHMENT_RENDER_HINT_AFTER",
        "ATTACHMENT_RENDER_HINT_INTERLEAVED",
    ]
    displayUrl: str
    linkTarget: str
    linkType: typing_extensions.Literal["UNKNOWN_LINK_TYPE", "SELF_LINK"]
    title: str

@typing.type_check_only
class ListDataSourceResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sources: _list[DataSource]

@typing.type_check_only
class ListItemNamesForUnmappedIdentityResponse(
    typing_extensions.TypedDict, total=False
):
    itemNames: _list[str]
    nextPageToken: str

@typing.type_check_only
class ListItemsResponse(typing_extensions.TypedDict, total=False):
    items: _list[Item]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListQuerySourcesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sources: _list[QuerySource]

@typing.type_check_only
class ListSearchApplicationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    searchApplications: _list[SearchApplication]

@typing.type_check_only
class ListUnmappedIdentitiesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    unmappedIdentities: _list[UnmappedIdentity]

@typing.type_check_only
class MatchRange(typing_extensions.TypedDict, total=False):
    end: int
    start: int

@typing.type_check_only
class MdbGroupProto(typing_extensions.TypedDict, total=False):
    groupName: str

@typing.type_check_only
class MdbUserProto(typing_extensions.TypedDict, total=False):
    gaiaId: str
    userName: str

@typing.type_check_only
class Media(typing_extensions.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class MeetingSpace(typing_extensions.TypedDict, total=False):
    acceptedNumberClass: _list[str]
    broadcastAccess: BroadcastAccess
    callInfo: CallInfo
    gatewayAccess: GatewayAccess
    gatewaySipAccess: _list[GatewaySipAccess]
    meetingAlias: str
    meetingCode: str
    meetingSpaceId: str
    meetingUrl: str
    moreJoinUrl: str
    phoneAccess: _list[PhoneAccess]
    settings: Settings
    universalPhoneAccess: UniversalPhoneAccess

@typing.type_check_only
class Member(typing_extensions.TypedDict, total=False):
    roster: Roster
    user: User

@typing.type_check_only
class MemberId(typing_extensions.TypedDict, total=False):
    rosterId: RosterId
    userId: UserId

@typing.type_check_only
class MembershipChangeEvent(typing_extensions.TypedDict, total=False):
    leaveReason: typing_extensions.Literal[
        "LEAVE_REASON_UNKNOWN", "FORCE_HISTORY_POLICY_CHANGE", "USER_INITIATED"
    ]
    participantId: _list[StoredParticipantId]
    type: typing_extensions.Literal["JOIN", "LEAVE"]

@typing.type_check_only
class MembershipChangedMetadata(typing_extensions.TypedDict, total=False):
    affectedMemberProfiles: _list[Member]
    affectedMembers: _list[MemberId]
    affectedMemberships: _list[AffectedMembership]
    initiator: UserId
    initiatorProfile: User
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "INVITED",
        "JOINED",
        "ADDED",
        "REMOVED",
        "LEFT",
        "BOT_ADDED",
        "BOT_REMOVED",
        "KICKED_DUE_TO_OTR_CONFLICT",
        "ROLE_UPDATED",
        "ROLE_TARGET_AUDIENCE_UPDATED",
    ]

@typing.type_check_only
class Menu(typing_extensions.TypedDict, total=False):
    items: _list[MenuItem]
    label: str
    name: str
    onChange: FormAction

@typing.type_check_only
class MenuItem(typing_extensions.TypedDict, total=False):
    selected: bool
    text: str
    value: str

@typing.type_check_only
class Message(typing_extensions.TypedDict, total=False):
    annotations: _list[Annotation]
    appProfile: AppsDynamiteSharedAppProfile
    attachments: _list[Attachment]
    attributes: MessageAttributes
    botResponses: _list[BotResponse]
    communalLabels: _list[CommunalLabelTag]
    contentReportSummary: ContentReportSummary
    createTime: str
    creatorId: UserId
    deletableBy: typing_extensions.Literal[
        "PERMISSION_UNSPECIFIED",
        "PERMISSION_NO_ONE",
        "PERMISSION_CREATOR",
        "PERMISSION_MEMBER",
    ]
    deleteTime: str
    deleteTimeForRequester: str
    deletedByVault: bool
    dlpScanOutcome: typing_extensions.Literal[
        "SCAN_UNKNOWN_OUTCOME",
        "SCAN_SUCCEEDED_NO_VIOLATION",
        "SCAN_SUCCEEDED_BLOCK",
        "SCAN_SUCCEEDED_WARN",
        "SCAN_SUCCEEDED_AUDIT_ONLY",
        "SCAN_FAILURE_EXCEPTION",
        "SCAN_FAILURE_TIMEOUT",
        "SCAN_FAILURE_ALL_RULES_FAILED",
        "SCAN_FAILURE_ILLEGAL_STATE_FOR_ATTACHMENTS",
        "SCAN_SKIPPED_EXPERIMENT_DISABLED",
        "SCAN_SKIPPED_CONSUMER",
        "SCAN_SKIPPED_NON_HUMAN_USER",
        "SCAN_SKIPPED_NO_MESSAGE",
        "SCAN_SKIPPED_USER_ACKNOWLEDGED_WARNING",
        "SCAN_SKIPPED_MESSAGE_FROM_UNSUPPORTED_ORIGIN",
        "SCAN_RULE_EVALUATION_SKIPPED_NO_RULES_FOUND",
        "SCAN_RULE_EVALUATION_SKIPPED_NO_APPLICABLE_RULES_FOR_ACTION_PARAMS",
        "SCAN_RULE_EVALUATION_SKIPPED_NO_APPLICABLE_RULES_FOR_TRIGGER",
        "SCAN_RULE_EVALUATION_SKIPPED_CHANGELING_PERMANENT_ERROR",
        "SCAN_RULE_EVALUATION_SKIPPED_CHANGELING_EMPTY_RESPONSE",
        "SCAN_SUCCEEDED_WITH_FAILURES_NO_VIOLATION",
        "SCAN_SUCCEEDED_WITH_FAILURES_BLOCK",
        "SCAN_SUCCEEDED_WITH_FAILURES_WARN",
        "SCAN_SUCCEEDED_WITH_FAILURES_AUDIT_ONLY",
    ]
    dlpScanSummary: DlpScanSummary
    editableBy: typing_extensions.Literal[
        "PERMISSION_UNSPECIFIED",
        "PERMISSION_NO_ONE",
        "PERMISSION_CREATOR",
        "PERMISSION_MEMBER",
    ]
    fallbackText: str
    id: MessageId
    isContentPurged: bool
    isInlineReply: bool
    lastEditTime: str
    lastUpdateTime: str
    localId: str
    messageIntegrationPayload: AppsDynamiteSharedMessageIntegrationPayload
    messageOrigin: typing_extensions.Literal[
        "ORIGIN_NOT_SET",
        "ORIGIN_DYNAMITE",
        "ORIGIN_BABEL_INTEROP_LIVE",
        "ORIGIN_BABEL_INTEROP_RETRY",
        "ORIGIN_BABEL",
        "ORIGIN_BABEL_DUAL_WRITE",
        "ORIGIN_BABEL_DUAL_WRITE_RETRY",
        "ORIGIN_BACKFILL_FROM_PAPYRUS",
        "ORIGIN_BACKFILL_FROM_GMAIL_ARCHIVE",
    ]
    messageState: typing_extensions.Literal["PUBLIC", "PRIVATE"]
    originAppSuggestions: _list[AppsDynamiteSharedOriginAppSuggestion]
    personalLabels: _list[PersonalLabelTag]
    privateMessageInfos: _list[PrivateMessageInfo]
    privateMessageViewer: UserId
    props: MessageProps
    quotedByState: typing_extensions.Literal[
        "QUOTED_BY_STATE_UNSPECIFIED",
        "QUOTED_BY_STATE_HAS_BEEN_QUOTED",
        "QUOTED_BY_STATE_HAS_NOT_BEEN_QUOTED",
    ]
    quotedMessageMetadata: QuotedMessageMetadata
    reactions: _list[AppsDynamiteSharedReaction]
    reports: _list[ContentReport]
    retentionSettings: AppsDynamiteSharedRetentionSettings
    secondaryMessageKey: str
    textBody: str
    tombstoneMetadata: TombstoneMetadata
    updaterId: UserId
    uploadMetadata: _list[UploadMetadata]

@typing.type_check_only
class MessageAttributes(typing_extensions.TypedDict, total=False):
    isTombstone: bool

@typing.type_check_only
class MessageId(typing_extensions.TypedDict, total=False):
    messageId: str
    parentId: MessageParentId

@typing.type_check_only
class MessageInfo(typing_extensions.TypedDict, total=False):
    message: Message
    searcherMembershipState: typing_extensions.Literal[
        "MEMBER_UNKNOWN",
        "MEMBER_INVITED",
        "MEMBER_JOINED",
        "MEMBER_NOT_A_MEMBER",
        "MEMBER_FAILED",
    ]

@typing.type_check_only
class MessageParentId(typing_extensions.TypedDict, total=False):
    topicId: TopicId

@typing.type_check_only
class MessageProps(typing_extensions.TypedDict, total=False):
    babelProps: BabelMessageProps

@typing.type_check_only
class Metadata(typing_extensions.TypedDict, total=False):
    createTime: str
    displayOptions: ResultDisplayMetadata
    fields: _list[NamedProperty]
    mimeType: str
    objectType: str
    owner: Person
    source: Source
    thumbnailUrl: str
    updateTime: str

@typing.type_check_only
class Metaline(typing_extensions.TypedDict, total=False):
    properties: _list[DisplayedProperty]

@typing.type_check_only
class Name(typing_extensions.TypedDict, total=False):
    displayName: str

@typing.type_check_only
class NamedProperty(dict[str, typing.Any]): ...

@typing.type_check_only
class OAuthConsumerProto(typing_extensions.TypedDict, total=False):
    domain: str

@typing.type_check_only
class ObjectDefinition(typing_extensions.TypedDict, total=False):
    name: str
    options: ObjectOptions
    propertyDefinitions: _list[PropertyDefinition]

@typing.type_check_only
class ObjectDisplayOptions(typing_extensions.TypedDict, total=False):
    metalines: _list[Metaline]
    objectDisplayLabel: str

@typing.type_check_only
class ObjectOptions(typing_extensions.TypedDict, total=False):
    displayOptions: ObjectDisplayOptions
    freshnessOptions: FreshnessOptions
    suggestionFilteringOperators: _list[str]

@typing.type_check_only
class ObjectPropertyOptions(typing_extensions.TypedDict, total=False):
    subobjectProperties: _list[PropertyDefinition]

@typing.type_check_only
class ObjectValues(dict[str, typing.Any]): ...

@typing.type_check_only
class OnClick(typing_extensions.TypedDict, total=False):
    action: FormAction
    link: str
    openLink: OpenLink
    openLinkAction: FormAction

@typing.type_check_only
class OpenLink(typing_extensions.TypedDict, total=False):
    loadIndicator: typing_extensions.Literal["NONE", "SPINNER"]
    onClose: typing_extensions.Literal["NOTHING", "RELOAD_ADD_ON"]
    openAs: typing_extensions.Literal["FULL_SIZE", "OVERLAY"]
    url: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OtrChatMessageEvent(typing_extensions.TypedDict, total=False):
    expirationTimestampUsec: str
    kansasRowId: str
    kansasVersionInfo: str
    messageOtrStatus: typing_extensions.Literal["OFF_THE_RECORD", "ON_THE_RECORD"]

@typing.type_check_only
class OtrModificationEvent(typing_extensions.TypedDict, total=False):
    newOtrStatus: typing_extensions.Literal["OFF_THE_RECORD", "ON_THE_RECORD"]
    newOtrToggle: typing_extensions.Literal["ENABLED", "DISABLED"]
    oldOtrStatus: typing_extensions.Literal["OFF_THE_RECORD", "ON_THE_RECORD"]
    oldOtrToggle: typing_extensions.Literal["ENABLED", "DISABLED"]

@typing.type_check_only
class PackagingServiceClient(typing_extensions.TypedDict, total=False):
    androidPackageName: str
    iosAppStoreId: str
    iosBundleId: str
    type: typing_extensions.Literal["ANDROID", "IOS"]

@typing.type_check_only
class PaygateInfo(typing_extensions.TypedDict, total=False):
    callEndingSoonWarningTime: str
    callEndingTime: str
    showUpgradePromos: bool

@typing.type_check_only
class PeopleSuggestion(typing_extensions.TypedDict, total=False):
    person: Person

@typing.type_check_only
class Person(typing_extensions.TypedDict, total=False):
    emailAddresses: _list[EmailAddress]
    name: str
    obfuscatedId: str
    personNames: _list[Name]
    phoneNumbers: _list[PhoneNumber]
    photos: _list[Photo]

@typing.type_check_only
class PersonalLabelTag(typing_extensions.TypedDict, total=False):
    labelId: str

@typing.type_check_only
class PhoneAccess(typing_extensions.TypedDict, total=False):
    formattedPhoneNumber: str
    languageCode: str
    phoneNumber: str
    pin: str
    regionCode: str

@typing.type_check_only
class PhoneNumber(typing_extensions.TypedDict, total=False):
    phoneNumber: str
    type: typing_extensions.Literal["OTHER", "MOBILE", "OFFICE"]

@typing.type_check_only
class Photo(typing_extensions.TypedDict, total=False):
    url: str

@typing.type_check_only
class PinnedItemId(typing_extensions.TypedDict, total=False):
    driveId: str

@typing.type_check_only
class PollItemsRequest(typing_extensions.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions
    limit: int
    queue: str
    statusCodes: _list[str]

@typing.type_check_only
class PollItemsResponse(typing_extensions.TypedDict, total=False):
    items: _list[Item]

@typing.type_check_only
class PostiniUserProto(typing_extensions.TypedDict, total=False):
    postiniUserId: str

@typing.type_check_only
class Presenter(typing_extensions.TypedDict, total=False):
    byDeviceId: str
    copresenterDeviceIds: _list[str]
    presenterDeviceId: str

@typing.type_check_only
class Principal(typing_extensions.TypedDict, total=False):
    groupResourceName: str
    gsuitePrincipal: GSuitePrincipal
    userResourceName: str

@typing.type_check_only
class PrincipalProto(typing_extensions.TypedDict, total=False):
    allAuthenticatedUsers: AllAuthenticatedUsersProto
    capTokenHolder: CapTokenHolderProto
    chat: ChatProto
    circle: CircleProto
    cloudPrincipal: CloudPrincipalProto
    contactGroup: ContactGroupProto
    emailOwner: EmailOwnerProto
    event: EventProto
    gaiaGroup: GaiaGroupProto
    gaiaUser: GaiaUserProto
    host: HostProto
    ldapGroup: LdapGroupProto
    ldapUser: LdapUserProto
    mdbGroup: MdbGroupProto
    mdbUser: MdbUserProto
    oauthConsumer: OAuthConsumerProto
    postiniUser: PostiniUserProto
    rbacRole: RbacRoleProto
    rbacSubject: RbacSubjectProto
    resourceRole: ResourceRoleProto
    scope: typing_extensions.Literal[
        "INVALID",
        "GAIA_USER",
        "GAIA_GROUP",
        "LDAP_USER",
        "LDAP_GROUP",
        "MDB_USER",
        "MDB_GROUP",
        "POSTINI_USER",
        "CONTACT_GROUP",
        "SIMPLE_SECRET_HOLDER",
        "SIGNING_KEY_POSSESSOR",
        "ALL_AUTHENTICATED_USERS",
        "OAUTH_CONSUMER",
        "HOST",
        "SOCIAL_GRAPH_NODE",
        "EMAIL_OWNER",
        "CAP_TOKEN_HOLDER",
        "CIRCLE",
        "SQUARE",
        "EVENT",
        "RESOURCE_ROLE",
        "CHAT",
        "YOUTUBE_USER",
        "UNUSED_ZWIEBACK_SESSION",
        "ZWIEBACK_SESSION",
        "RBAC_ROLE",
        "RBAC_SUBJECT",
        "CLOUD_PRINCIPAL",
    ]
    signingKeyPossessor: SigningKeyPossessorProto
    simpleSecretHolder: SimpleSecretHolderProto
    socialGraphNode: SocialGraphNodeProto
    square: SquareProto
    youtubeUser: YoutubeUserProto
    zwiebackSession: ZwiebackSessionProto

@typing.type_check_only
class PrivateMessageInfo(typing_extensions.TypedDict, total=False):
    annotations: _list[Annotation]
    attachments: _list[Attachment]
    contextualAddOnMarkup: _list[GoogleChatV1ContextualAddOnMarkup]
    gsuiteIntegrationMetadata: _list[GsuiteIntegrationMetadata]
    text: str
    userId: UserId

@typing.type_check_only
class ProcessingError(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "PROCESSING_ERROR_CODE_UNSPECIFIED",
        "MALFORMED_REQUEST",
        "UNSUPPORTED_CONTENT_FORMAT",
        "INDIRECT_BROKEN_ACL",
        "ACL_CYCLE",
    ]
    errorMessage: str
    fieldViolations: _list[FieldViolation]

@typing.type_check_only
class PropertyDefinition(dict[str, typing.Any]): ...

@typing.type_check_only
class PropertyDisplayOptions(typing_extensions.TypedDict, total=False):
    displayLabel: str

@typing.type_check_only
class Provenance(typing_extensions.TypedDict, total=False):
    annotationBlob: str
    canonicalUrl: str
    inputUrl: str
    itemtype: _list[str]
    retrievedTimestampMsec: str
    retrievedUrl: str

@typing.type_check_only
class PushItem(typing_extensions.TypedDict, total=False):
    contentHash: str
    metadataHash: str
    payload: str
    queue: str
    repositoryError: RepositoryError
    structuredDataHash: str
    type: typing_extensions.Literal[
        "UNSPECIFIED", "MODIFIED", "NOT_MODIFIED", "REPOSITORY_ERROR", "REQUEUE"
    ]

@typing.type_check_only
class PushItemRequest(typing_extensions.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions
    item: PushItem

@typing.type_check_only
class QueryCountByStatus(typing_extensions.TypedDict, total=False):
    count: str
    statusCode: int

@typing.type_check_only
class QueryInterpretation(typing_extensions.TypedDict, total=False):
    interpretationType: typing_extensions.Literal["NONE", "BLEND", "REPLACE"]
    interpretedQuery: str
    reason: typing_extensions.Literal[
        "UNSPECIFIED",
        "QUERY_HAS_NATURAL_LANGUAGE_INTENT",
        "NOT_ENOUGH_RESULTS_FOUND_FOR_USER_QUERY",
    ]

@typing.type_check_only
class QueryInterpretationConfig(typing_extensions.TypedDict, total=False):
    forceDisableSupplementalResults: bool
    forceVerbatimMode: bool

@typing.type_check_only
class QueryInterpretationOptions(typing_extensions.TypedDict, total=False):
    disableNlInterpretation: bool
    disableSupplementalResults: bool
    enableVerbatimMode: bool

@typing.type_check_only
class QueryItem(typing_extensions.TypedDict, total=False):
    isSynthetic: bool

@typing.type_check_only
class QueryOperator(typing_extensions.TypedDict, total=False):
    displayName: str
    enumValues: _list[str]
    greaterThanOperatorName: str
    isFacetable: bool
    isRepeatable: bool
    isReturnable: bool
    isSortable: bool
    isSuggestable: bool
    lessThanOperatorName: str
    objectType: str
    operatorName: str
    type: typing_extensions.Literal[
        "UNKNOWN",
        "INTEGER",
        "DOUBLE",
        "TIMESTAMP",
        "BOOLEAN",
        "ENUM",
        "DATE",
        "TEXT",
        "HTML",
    ]

@typing.type_check_only
class QuerySource(typing_extensions.TypedDict, total=False):
    displayName: str
    operators: _list[QueryOperator]
    shortName: str
    source: Source

@typing.type_check_only
class QuerySuggestion(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class QuotedMessageMetadata(typing_extensions.TypedDict, total=False):
    annotations: _list[Annotation]
    appProfile: AppsDynamiteSharedAppProfile
    botAttachmentState: typing_extensions.Literal[
        "BOT_ATTACHMENT_STATE_UNSPECIFIED",
        "BOT_ATTACHMENT_STATE_HAS_BOT_ATTACHMENT",
        "BOT_ATTACHMENT_STATE_NO_BOT_ATTACHMENT",
    ]
    creatorId: UserId
    lastUpdateTimeWhenQuotedMicros: str
    messageId: MessageId
    messageState: typing_extensions.Literal[
        "MESSAGE_STATE_UNSPECIFIED",
        "MESSAGE_STATE_ACTIVE",
        "MESSAGE_STATE_DELETED",
        "MESSAGE_STATE_OTR_EDITED",
    ]
    retentionSettings: AppsDynamiteSharedRetentionSettings
    textBody: str
    uploadMetadata: _list[UploadMetadata]

@typing.type_check_only
class RbacRoleProto(typing_extensions.TypedDict, total=False):
    name: str
    objectId: str
    rbacNamespace: str
    rbacRoleName: str

@typing.type_check_only
class RbacSubjectProto(typing_extensions.TypedDict, total=False):
    username: str

@typing.type_check_only
class ReactionInfo(typing_extensions.TypedDict, total=False):
    emoji: str

@typing.type_check_only
class ReadReceiptsSettingsUpdatedMetadata(typing_extensions.TypedDict, total=False):
    readReceiptsEnabled: bool

@typing.type_check_only
class RecordingEvent(typing_extensions.TypedDict, total=False):
    deviceId: str
    type: typing_extensions.Literal[
        "RECORDING_EVENT_UNSPECIFIED",
        "USER_ACTION",
        "STARTED_BY_USER",
        "STOPPED_BY_USER",
        "CANCELLED_BY_USER",
        "CANCELLED_INITIALIZATION_FAILED",
        "CANCELLED_INITIATOR_LEFT",
        "ACTIVE_ABOUT_TO_STOP_TOO_LONG",
        "STOPPED_TOO_LONG",
        "STOPPED_ALL_DEVICES_LEFT",
        "STOPPED_INTERNAL_FAILURES",
    ]

@typing.type_check_only
class RecordingInfo(typing_extensions.TypedDict, total=False):
    latestRecordingEvent: RecordingEvent
    ownerDisplayName: str
    producerDeviceId: str
    recordingApplicationType: typing_extensions.Literal[
        "RECORDING_APPLICATION_TYPE_UNSPECIFIED",
        "RECORDING",
        "GLIVE_STREAM",
        "BROADCAST",
    ]
    recordingId: str
    recordingStatus: typing_extensions.Literal[
        "RECORDING_UNSPECIFIED",
        "RECORDING_INACTIVE",
        "RECORDING_STARTING",
        "RECORDING_STARTED",
    ]

@typing.type_check_only
class RecordingSessionInfo(typing_extensions.TypedDict, total=False):
    ownerEmail: str
    recordingSessionId: str
    sessionStateInfo: SessionStateInfo

@typing.type_check_only
class RenameEvent(typing_extensions.TypedDict, total=False):
    newName: str
    originalName: str

@typing.type_check_only
class RepositoryError(typing_extensions.TypedDict, total=False):
    errorMessage: str
    httpStatusCode: int
    type: typing_extensions.Literal[
        "UNKNOWN",
        "NETWORK_ERROR",
        "DNS_ERROR",
        "CONNECTION_ERROR",
        "AUTHENTICATION_ERROR",
        "AUTHORIZATION_ERROR",
        "SERVER_ERROR",
        "QUOTA_EXCEEDED",
        "SERVICE_UNAVAILABLE",
        "CLIENT_ERROR",
    ]

@typing.type_check_only
class RequestOptions(typing_extensions.TypedDict, total=False):
    debugOptions: DebugOptions
    languageCode: str
    searchApplicationId: str
    timeZone: str

@typing.type_check_only
class RequiredMessageFeaturesMetadata(typing_extensions.TypedDict, total=False):
    requiredFeatures: _list[str]

@typing.type_check_only
class ResetSearchApplicationRequest(typing_extensions.TypedDict, total=False):
    debugOptions: DebugOptions

@typing.type_check_only
class ResourceRoleProto(typing_extensions.TypedDict, total=False):
    applicationId: str
    objectId: str
    objectPart: str
    roleId: int

@typing.type_check_only
class ResponseDebugInfo(typing_extensions.TypedDict, total=False):
    enabledExperiments: _list[int]
    formattedDebugInfo: str

@typing.type_check_only
class RestrictItem(typing_extensions.TypedDict, total=False):
    driveFollowUpRestrict: DriveFollowUpRestrict
    driveLocationRestrict: DriveLocationRestrict
    driveMimeTypeRestrict: DriveMimeTypeRestrict
    driveTimeSpanRestrict: DriveTimeSpanRestrict
    searchOperator: str

@typing.type_check_only
class ResultCounts(typing_extensions.TypedDict, total=False):
    sourceResultCounts: _list[SourceResultCount]

@typing.type_check_only
class ResultDebugInfo(typing_extensions.TypedDict, total=False):
    formattedDebugInfo: str

@typing.type_check_only
class ResultDisplayField(typing_extensions.TypedDict, total=False):
    label: str
    operatorName: str
    property: NamedProperty

@typing.type_check_only
class ResultDisplayLine(typing_extensions.TypedDict, total=False):
    fields: _list[ResultDisplayField]

@typing.type_check_only
class ResultDisplayMetadata(dict[str, typing.Any]): ...

@typing.type_check_only
class RetrievalImportance(typing_extensions.TypedDict, total=False):
    importance: typing_extensions.Literal["DEFAULT", "HIGHEST", "HIGH", "LOW", "NONE"]

@typing.type_check_only
class RoomRenameMetadata(typing_extensions.TypedDict, total=False):
    newName: str
    prevName: str

@typing.type_check_only
class RoomUpdatedMetadata(typing_extensions.TypedDict, total=False):
    groupDetailsMetadata: GroupDetailsUpdatedMetadata
    groupLinkSharingEnabled: bool
    initiator: User
    initiatorType: typing_extensions.Literal[
        "INITIATOR_TYPE_UNSPECIFIED", "INITIATOR_TYPE_END_USER", "INITIATOR_TYPE_ADMIN"
    ]
    name: str
    renameMetadata: RoomRenameMetadata
    visibility: AppsDynamiteSharedGroupVisibility

@typing.type_check_only
class Roster(typing_extensions.TypedDict, total=False):
    avatarUrl: str
    id: RosterId
    membershipCount: int
    name: str
    rosterGaiaKey: str
    rosterState: typing_extensions.Literal[
        "ROSTER_STATE_UNKNOWN", "ROSTER_ACTIVE", "ROSTER_DELETED"
    ]
    segmentedMembershipCounts: AppsDynamiteSharedSegmentedMembershipCounts

@typing.type_check_only
class RosterId(typing_extensions.TypedDict, total=False):
    id: str

@typing.type_check_only
class SafeUrlProto(typing_extensions.TypedDict, total=False):
    privateDoNotAccessOrElseSafeUrlWrappedValue: str

@typing.type_check_only
class Schema(typing_extensions.TypedDict, total=False):
    objectDefinitions: _list[ObjectDefinition]
    operationIds: _list[str]

@typing.type_check_only
class ScoringConfig(typing_extensions.TypedDict, total=False):
    disableFreshness: bool
    disablePersonalization: bool

@typing.type_check_only
class SearchApplication(dict[str, typing.Any]): ...

@typing.type_check_only
class SearchApplicationQueryStats(typing_extensions.TypedDict, total=False):
    date: Date
    queryCountByStatus: _list[QueryCountByStatus]

@typing.type_check_only
class SearchApplicationSessionStats(typing_extensions.TypedDict, total=False):
    date: Date
    searchSessionsCount: str

@typing.type_check_only
class SearchApplicationUserStats(typing_extensions.TypedDict, total=False):
    date: Date
    oneDayActiveUsersCount: str
    sevenDaysActiveUsersCount: str
    thirtyDaysActiveUsersCount: str

@typing.type_check_only
class SearchItemsByViewUrlRequest(typing_extensions.TypedDict, total=False):
    debugOptions: DebugOptions
    pageToken: str
    viewUrl: str

@typing.type_check_only
class SearchItemsByViewUrlResponse(typing_extensions.TypedDict, total=False):
    items: _list[Item]
    nextPageToken: str

@typing.type_check_only
class SearchQualityMetadata(typing_extensions.TypedDict, total=False):
    quality: float

@typing.type_check_only
class SearchRequest(typing_extensions.TypedDict, total=False):
    contextAttributes: _list[ContextAttribute]
    dataSourceRestrictions: _list[DataSourceRestriction]
    facetOptions: _list[FacetOptions]
    pageSize: int
    query: str
    queryInterpretationOptions: QueryInterpretationOptions
    requestOptions: RequestOptions
    sortOptions: SortOptions
    start: int

@typing.type_check_only
class SearchResponse(typing_extensions.TypedDict, total=False):
    debugInfo: ResponseDebugInfo
    errorInfo: ErrorInfo
    facetResults: _list[FacetResult]
    hasMoreResults: bool
    queryInterpretation: QueryInterpretation
    resultCountEstimate: str
    resultCountExact: str
    resultCounts: ResultCounts
    results: _list[SearchResult]
    spellResults: _list[SpellResult]
    structuredResults: _list[StructuredResult]

@typing.type_check_only
class SearchResult(dict[str, typing.Any]): ...

@typing.type_check_only
class Section(typing_extensions.TypedDict, total=False):
    collapsable: bool
    description: str
    numUncollapsableWidgets: int
    widgets: _list[WidgetMarkup]

@typing.type_check_only
class Segment(typing_extensions.TypedDict, total=False):
    formatting: Formatting
    hashtagData: HashtagData
    linkData: LinkData
    text: str
    type: typing_extensions.Literal[
        "TEXT", "LINE_BREAK", "LINK", "USER_MENTION", "ALL_USER_MENTION", "HASHTAG"
    ]
    userMentionData: UserMentionData

@typing.type_check_only
class SelectionControl(typing_extensions.TypedDict, total=False):
    items: _list[SelectionItem]
    label: str
    name: str
    onChange: FormAction
    type: typing_extensions.Literal["CHECK_BOX", "RADIO_BUTTON", "SWITCH", "DROPDOWN"]

@typing.type_check_only
class SelectionItem(typing_extensions.TypedDict, total=False):
    selected: bool
    text: str
    value: str

@typing.type_check_only
class SessionEvent(typing_extensions.TypedDict, total=False):
    deviceId: str
    type: typing_extensions.Literal[
        "EVENT_UNSPECIFIED",
        "STARTED_BY_USER",
        "STOPPED_BY_USER",
        "CANCELLED_BY_USER",
        "CANCELLED_INITIALIZATION_FAILED",
        "CANCELLED_INITIATOR_LEFT",
        "ACTIVE_ABOUT_TO_STOP_TOO_LONG",
        "STOPPED_TOO_LONG",
        "STOPPED_ALL_DEVICES_LEFT",
        "STOPPED_INTERNAL_FAILURES",
    ]

@typing.type_check_only
class SessionStateInfo(typing_extensions.TypedDict, total=False):
    ackInfo: AckInfo
    languageConfig: LanguageConfig
    lastActorDeviceId: str
    maxEndTime: str
    sessionState: typing_extensions.Literal[
        "SESSION_STATE_UNSPECIFIED", "STARTING", "ACTIVE", "STOPPED"
    ]
    sessionStopReason: typing_extensions.Literal[
        "SESSION_STOP_REASON_UNSPECIFIED",
        "USER_ACTION",
        "STOPPED_INITIALIZATION_FAILED",
        "STOPPED_TOO_LONG",
        "STOPPED_ALL_DEVICES_LEFT",
        "STOPPED_INTERNAL_FAILURES",
        "STOPPED_YOU_TUBE_LIVE_EVENT_ENDED",
    ]

@typing.type_check_only
class Settings(typing_extensions.TypedDict, total=False):
    accessLock: bool
    attendanceReportEnabled: bool
    chatLock: bool
    cohostArtifactSharingEnabled: bool
    cseEnabled: bool
    defaultAsViewer: bool
    moderationEnabled: bool
    presentLock: bool
    reactionsLock: bool

@typing.type_check_only
class ShareScope(typing_extensions.TypedDict, total=False):
    domain: str
    scope: typing_extensions.Literal[
        "UNKNOWN", "PRIVATE", "LIMITED", "EXTENDED", "DASHER_DOMAIN", "PUBLIC"
    ]

@typing.type_check_only
class SigningKeyPossessorProto(typing_extensions.TypedDict, total=False):
    keymasterKeyType: int
    serializedVerificationKey: str
    serializedVerificationKeyset: str

@typing.type_check_only
class SimpleSecretHolderProto(typing_extensions.TypedDict, total=False):
    label: SimpleSecretLabelProto

@typing.type_check_only
class SimpleSecretLabelProto(typing_extensions.TypedDict, total=False):
    capabilityId: int
    genericLabel: str
    inviteId: str
    type: typing_extensions.Literal[
        "INVALID", "AUTH_KEY", "INVITE", "GENERIC_SECRET", "CAP_TOKEN", "REKE"
    ]

@typing.type_check_only
class SlashCommandMetadata(typing_extensions.TypedDict, total=False):
    argumentsHint: str
    commandId: str
    commandName: str
    id: UserId
    triggersDialog: bool
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "ADD", "INVOKE", "FAILED_TO_ADD"
    ]

@typing.type_check_only
class Snippet(typing_extensions.TypedDict, total=False):
    matchRanges: _list[MatchRange]
    snippet: str

@typing.type_check_only
class SocialCommonAttachmentAttachment(typing_extensions.TypedDict, total=False):
    embedItem: EmbedClientItem
    id: str

@typing.type_check_only
class SocialGraphNodeProto(typing_extensions.TypedDict, total=False):
    sgnDomain: str
    sgnPk: str

@typing.type_check_only
class SortOptions(typing_extensions.TypedDict, total=False):
    operatorName: str
    sortOrder: typing_extensions.Literal["ASCENDING", "DESCENDING"]

@typing.type_check_only
class Source(typing_extensions.TypedDict, total=False):
    name: str
    predefinedSource: typing_extensions.Literal[
        "NONE",
        "QUERY_HISTORY",
        "PERSON",
        "GOOGLE_DRIVE",
        "GOOGLE_GMAIL",
        "GOOGLE_SITES",
        "GOOGLE_GROUPS",
        "GOOGLE_CALENDAR",
        "GOOGLE_KEEP",
    ]

@typing.type_check_only
class SourceConfig(typing_extensions.TypedDict, total=False):
    crowdingConfig: SourceCrowdingConfig
    scoringConfig: SourceScoringConfig
    source: Source

@typing.type_check_only
class SourceCrowdingConfig(typing_extensions.TypedDict, total=False):
    numResults: int
    numSuggestions: int

@typing.type_check_only
class SourceResultCount(typing_extensions.TypedDict, total=False):
    hasMoreResults: bool
    resultCountEstimate: str
    resultCountExact: str
    source: Source

@typing.type_check_only
class SourceScoringConfig(typing_extensions.TypedDict, total=False):
    sourceImportance: typing_extensions.Literal["DEFAULT", "LOW", "HIGH"]

@typing.type_check_only
class SpaceId(typing_extensions.TypedDict, total=False):
    spaceId: str

@typing.type_check_only
class SpellResult(typing_extensions.TypedDict, total=False):
    suggestedQuery: str

@typing.type_check_only
class SquareProto(typing_extensions.TypedDict, total=False):
    memberType: int
    squareId: str

@typing.type_check_only
class StartUploadItemRequest(typing_extensions.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StoredParticipantId(typing_extensions.TypedDict, total=False):
    gaiaId: str

@typing.type_check_only
class StreamViewerStats(typing_extensions.TypedDict, total=False):
    estimatedViewerCount: str

@typing.type_check_only
class StreamingSessionInfo(typing_extensions.TypedDict, total=False):
    applicationType: typing_extensions.Literal[
        "RECORDING_APPLICATION_TYPE_UNSPECIFIED",
        "RECORDING",
        "GLIVE_STREAM",
        "BROADCAST",
    ]
    latestSessionEvent: SessionEvent
    ownerDisplayName: str
    sessionId: str
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED", "INACTIVE", "STARTING", "LIVE"
    ]
    trainingEnabled: bool
    viewerAccessPolicy: typing_extensions.Literal[
        "BROADCASTING_ACCESS_POLICY_UNSPECIFIED", "ORGANIZATION", "PUBLIC"
    ]
    viewerStats: StreamViewerStats

@typing.type_check_only
class StructuredDataObject(dict[str, typing.Any]): ...

@typing.type_check_only
class StructuredResult(typing_extensions.TypedDict, total=False):
    person: Person

@typing.type_check_only
class SuggestRequest(typing_extensions.TypedDict, total=False):
    dataSourceRestrictions: _list[DataSourceRestriction]
    query: str
    requestOptions: RequestOptions

@typing.type_check_only
class SuggestResponse(typing_extensions.TypedDict, total=False):
    suggestResults: _list[SuggestResult]

@typing.type_check_only
class SuggestResult(typing_extensions.TypedDict, total=False):
    peopleSuggestion: PeopleSuggestion
    querySuggestion: QuerySuggestion
    source: Source
    suggestedQuery: str

@typing.type_check_only
class SupportUrls(typing_extensions.TypedDict, total=False):
    adminConfigUrl: str
    deletionPolicyUrl: str
    privacyPolicyUrl: str
    setupUrl: str
    supportUrl: str
    tosUrl: str

@typing.type_check_only
class SwitchWidget(typing_extensions.TypedDict, total=False):
    controlType: typing_extensions.Literal["UNSPECIFIED", "SWITCH", "CHECKBOX"]
    name: str
    onChange: FormAction
    selected: bool
    value: str

@typing.type_check_only
class TextButton(typing_extensions.TypedDict, total=False):
    altText: str
    backgroundColor: str
    disabled: bool
    onClick: OnClick
    style: typing_extensions.Literal["UNSPECIFIED", "TEXT", "FILLED"]
    text: str

@typing.type_check_only
class TextField(typing_extensions.TypedDict, total=False):
    autoComplete: AutoComplete
    autoCompleteCallback: FormAction
    autoCompleteMultipleSelections: bool
    hintText: str
    label: str
    maxLines: int
    name: str
    onChange: FormAction
    type: typing_extensions.Literal["SINGLE_LINE", "MULTIPLE_LINE"]
    value: str

@typing.type_check_only
class TextKeyValue(typing_extensions.TypedDict, total=False):
    key: str
    onClick: OnClick
    text: str

@typing.type_check_only
class TextOperatorOptions(typing_extensions.TypedDict, total=False):
    exactMatchWithOperator: bool
    operatorName: str

@typing.type_check_only
class TextParagraph(typing_extensions.TypedDict, total=False):
    text: str

@typing.type_check_only
class TextPropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: TextOperatorOptions
    retrievalImportance: RetrievalImportance

@typing.type_check_only
class TextValues(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class TimestampOperatorOptions(typing_extensions.TypedDict, total=False):
    greaterThanOperatorName: str
    lessThanOperatorName: str
    operatorName: str

@typing.type_check_only
class TimestampPropertyOptions(typing_extensions.TypedDict, total=False):
    operatorOptions: TimestampOperatorOptions

@typing.type_check_only
class TimestampValues(typing_extensions.TypedDict, total=False):
    values: _list[str]

@typing.type_check_only
class TombstoneMetadata(typing_extensions.TypedDict, total=False):
    tombstoneType: typing_extensions.Literal[
        "TOMBSTONE_UNSPECIFIED",
        "CREATOR",
        "ROOM_OWNER",
        "ADMIN",
        "APP_MESSAGE_EXPIRY",
        "CREATOR_VIA_APP",
        "ROOM_OWNER_VIA_APP",
    ]

@typing.type_check_only
class Toolbar(typing_extensions.TypedDict, total=False):
    color: str
    iconUrl: str
    name: str

@typing.type_check_only
class TopicId(typing_extensions.TypedDict, total=False):
    groupId: GroupId
    topicId: str

@typing.type_check_only
class TranscriptionSessionInfo(typing_extensions.TypedDict, total=False):
    sessionStateInfo: SessionStateInfo
    transcriptionSessionId: str

@typing.type_check_only
class TransientData(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class TrustedResourceUrlProto(typing_extensions.TypedDict, total=False):
    privateDoNotAccessOrElseTrustedResourceUrlWrappedValue: str

@typing.type_check_only
class TypeInfo(typing_extensions.TypedDict, total=False):
    videoInfo: VideoInfo

@typing.type_check_only
class UniversalPhoneAccess(typing_extensions.TypedDict, total=False):
    pin: str
    pstnInfoUrl: str

@typing.type_check_only
class UnmappedIdentity(typing_extensions.TypedDict, total=False):
    externalIdentity: Principal
    resolutionStatusCode: typing_extensions.Literal[
        "CODE_UNSPECIFIED",
        "NOT_FOUND",
        "IDENTITY_SOURCE_NOT_FOUND",
        "IDENTITY_SOURCE_MISCONFIGURED",
        "TOO_MANY_MAPPINGS_FOUND",
        "INTERNAL_ERROR",
    ]

@typing.type_check_only
class UnreserveItemsRequest(typing_extensions.TypedDict, total=False):
    connectorName: str
    debugOptions: DebugOptions
    queue: str

@typing.type_check_only
class UpdateDataSourceRequest(typing_extensions.TypedDict, total=False):
    debugOptions: DebugOptions
    source: DataSource

@typing.type_check_only
class UpdateSchemaRequest(typing_extensions.TypedDict, total=False):
    debugOptions: DebugOptions
    schema: Schema
    validateOnly: bool

@typing.type_check_only
class UploadItemRef(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class UploadMetadata(typing_extensions.TypedDict, total=False):
    attachmentToken: str
    backendUploadMetadata: AppsDynamiteSharedBackendUploadMetadata
    clonedAuthorizedItemId: AuthorizedItemId
    clonedDriveAction: typing_extensions.Literal[
        "DRIVE_ACTION_UNSPECIFIED",
        "ADD_TO_DRIVE",
        "ORGANIZE",
        "ADD_SHORTCUT",
        "ADD_ANOTHER_SHORTCUT",
    ]
    clonedDriveId: str
    contentName: str
    contentType: str
    dlpMetricsMetadata: AppsDynamiteSharedDlpMetricsMetadata
    localId: str
    originalDimension: AppsDynamiteSharedDimension
    videoReference: AppsDynamiteSharedVideoReference
    virusScanResult: typing_extensions.Literal[
        "UNKNOWN_VIRUS_SCAN_RESULT", "CLEAN", "INFECTED", "ERROR", "POLICY_VIOLATION"
    ]

@typing.type_check_only
class UrlMetadata(typing_extensions.TypedDict, total=False):
    domain: str
    gwsUrl: SafeUrlProto
    gwsUrlExpirationTimestamp: str
    imageHeight: str
    imageUrl: str
    imageWidth: str
    intImageHeight: int
    intImageWidth: int
    mimeType: str
    redirectUrl: SafeUrlProto
    shouldNotRender: bool
    snippet: str
    title: str
    url: SafeUrlProto
    urlSource: typing_extensions.Literal[
        "URL_SOURCE_UNKNOWN", "USER_SUPPLIED_URL", "SERVER_SUPPLIED_POLICY_VIOLATION"
    ]

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    avatarUrl: str
    blockRelationship: AppsDynamiteSharedUserBlockRelationship
    botInfo: BotInfo
    deleted: bool
    email: str
    firstName: str
    gender: str
    id: UserId
    isAnonymous: bool
    lastName: str
    name: str
    organizationInfo: AppsDynamiteSharedOrganizationInfo
    phoneNumber: _list[AppsDynamiteSharedPhoneNumber]
    userAccountState: typing_extensions.Literal[
        "UNKNOWN_USER_ACCOUNT_STATE",
        "ENABLED",
        "DISABLED",
        "DELETED",
        "TEMPORARY_UNAVAILABLE",
    ]
    userProfileVisibility: typing_extensions.Literal[
        "UNKNOWN_USER_PROFILE_VISIBILITY",
        "FULL_PROFILE",
        "PRIMARY_MAIL",
        "INVITEE_EMAIL",
        "DELETED_USER",
        "UNKNOWN_USER",
        "FAILURE",
    ]

@typing.type_check_only
class UserDisplayInfo(typing_extensions.TypedDict, total=False):
    avatarUrl: str
    displayName: str

@typing.type_check_only
class UserId(typing_extensions.TypedDict, total=False):
    actingUserId: str
    id: str
    originAppId: AppId
    type: typing_extensions.Literal["HUMAN", "BOT"]

@typing.type_check_only
class UserInfo(typing_extensions.TypedDict, total=False):
    driveNotificationAvatarUrl: str
    updaterCountDisplayType: typing_extensions.Literal[
        "UPDATER_COUNT_DISPLAY_TYPE_UNSPECIFIED",
        "NO_DISPLAY_COUNT",
        "EXACT_COUNT",
        "NONZERO_COUNT",
    ]
    updaterCountToShow: int
    updaterToShowEmail: str
    updaterToShowGaiaId: str
    updaterToShowName: str
    updaterToShowUserId: UserId

@typing.type_check_only
class UserMentionData(typing_extensions.TypedDict, total=False):
    email: str
    user: PrincipalProto
    userGaiaId: str
    userId: str

@typing.type_check_only
class UserMentionMetadata(typing_extensions.TypedDict, total=False):
    displayName: str
    gender: str
    id: UserId
    inviteeInfo: InviteeInfo
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "INVITE",
        "UNINVITE",
        "MENTION",
        "MENTION_ALL",
        "FAILED_TO_ADD",
    ]

@typing.type_check_only
class VPCSettings(typing_extensions.TypedDict, total=False):
    project: str

@typing.type_check_only
class Value(typing_extensions.TypedDict, total=False):
    booleanValue: bool
    dateValue: Date
    doubleValue: float
    integerValue: str
    stringValue: str
    timestampValue: str

@typing.type_check_only
class ValueFilter(typing_extensions.TypedDict, total=False):
    operatorName: str
    value: Value

@typing.type_check_only
class VideoCallMetadata(typing_extensions.TypedDict, total=False):
    meetingSpace: MeetingSpace
    shouldNotRender: bool
    wasCreatedInCurrentGroup: bool

@typing.type_check_only
class VideoInfo(typing_extensions.TypedDict, total=False):
    duration: int

@typing.type_check_only
class VoicePhoneNumber(typing_extensions.TypedDict, total=False):
    e164: str
    i18nData: VoicePhoneNumberI18nData

@typing.type_check_only
class VoicePhoneNumberI18nData(typing_extensions.TypedDict, total=False):
    countryCode: int
    internationalNumber: str
    isValid: bool
    nationalNumber: str
    regionCode: str
    validationResult: typing_extensions.Literal[
        "UNKNOWN",
        "IS_POSSIBLE",
        "INVALID_COUNTRY_CODE",
        "TOO_SHORT",
        "TOO_LONG",
        "IS_POSSIBLE_LOCAL_ONLY",
        "INVALID_LENGTH",
    ]

@typing.type_check_only
class WhiteboardInfo(typing_extensions.TypedDict, total=False):
    id: str
    title: str
    uri: str

@typing.type_check_only
class WidgetMarkup(typing_extensions.TypedDict, total=False):
    buttons: _list[Button]
    dateTimePicker: DateTimePicker
    divider: Divider
    grid: Grid
    horizontalAlignment: typing_extensions.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END"
    ]
    image: Image
    imageKeyValue: ImageKeyValue
    keyValue: KeyValue
    menu: Menu
    selectionControl: SelectionControl
    textField: TextField
    textKeyValue: TextKeyValue
    textParagraph: TextParagraph

@typing.type_check_only
class WrappedResourceKey(typing_extensions.TypedDict, total=False):
    resourceKey: str

@typing.type_check_only
class YouTubeBroadcastSessionInfo(typing_extensions.TypedDict, total=False):
    broadcastStats: YouTubeBroadcastStats
    sessionStateInfo: SessionStateInfo
    youTubeBroadcastSessionId: str
    youTubeLiveBroadcastEvent: YouTubeLiveBroadcastEvent

@typing.type_check_only
class YouTubeBroadcastStats(typing_extensions.TypedDict, total=False):
    estimatedViewerCount: str

@typing.type_check_only
class YouTubeLiveBroadcastEvent(typing_extensions.TypedDict, total=False):
    broadcastId: str
    channelId: str
    viewUrl: str

@typing.type_check_only
class YoutubeMetadata(typing_extensions.TypedDict, total=False):
    id: str
    shouldNotRender: bool
    startTime: int

@typing.type_check_only
class YoutubeUserProto(typing_extensions.TypedDict, total=False):
    youtubeUserId: str

@typing.type_check_only
class ZwiebackSessionProto(typing_extensions.TypedDict, total=False):
    zwiebackSessionId: str

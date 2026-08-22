import typing

_list = list

@typing.type_check_only
class AccessPermissionSetting(typing.TypedDict, total=False):
    principals: _list[Principal]

@typing.type_check_only
class AccessPermissionSettings(typing.TypedDict, total=False):
    discoverSpaceSetting: AccessPermissionSetting
    joinSpaceSetting: AccessPermissionSetting

@typing.type_check_only
class AccessSettings(typing.TypedDict, total=False):
    accessPermissionSettings: AccessPermissionSettings
    accessState: typing.Literal["ACCESS_STATE_UNSPECIFIED", "PRIVATE", "DISCOVERABLE"]
    audience: str

@typing.type_check_only
class AccessoryWidget(typing.TypedDict, total=False):
    buttonList: GoogleAppsCardV1ButtonList

@typing.type_check_only
class ActionParameter(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class ActionResponse(typing.TypedDict, total=False):
    dialogAction: DialogAction
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "NEW_MESSAGE",
        "UPDATE_MESSAGE",
        "UPDATE_USER_MESSAGE_CARDS",
        "REQUEST_CONFIG",
        "DIALOG",
        "UPDATE_WIDGET",
    ]
    updatedWidget: UpdatedWidget
    url: str

@typing.type_check_only
class ActionStatus(typing.TypedDict, total=False):
    statusCode: typing.Literal[
        "OK",
        "CANCELLED",
        "UNKNOWN",
        "INVALID_ARGUMENT",
        "DEADLINE_EXCEEDED",
        "NOT_FOUND",
        "ALREADY_EXISTS",
        "PERMISSION_DENIED",
        "UNAUTHENTICATED",
        "RESOURCE_EXHAUSTED",
        "FAILED_PRECONDITION",
        "ABORTED",
        "OUT_OF_RANGE",
        "UNIMPLEMENTED",
        "INTERNAL",
        "UNAVAILABLE",
        "DATA_LOSS",
    ]
    userFacingMessage: str

@typing.type_check_only
class Annotation(typing.TypedDict, total=False):
    customEmojiMetadata: CustomEmojiMetadata
    length: int
    richLinkMetadata: RichLinkMetadata
    slashCommand: SlashCommandMetadata
    startIndex: int
    type: typing.Literal[
        "ANNOTATION_TYPE_UNSPECIFIED",
        "USER_MENTION",
        "SLASH_COMMAND",
        "RICH_LINK",
        "CUSTOM_EMOJI",
    ]
    userMention: UserMentionMetadata

@typing.type_check_only
class AppCommandMetadata(typing.TypedDict, total=False):
    appCommandId: int
    appCommandType: typing.Literal[
        "APP_COMMAND_TYPE_UNSPECIFIED",
        "SLASH_COMMAND",
        "QUICK_COMMAND",
        "MESSAGE_ACTION",
    ]

@typing.type_check_only
class AttachedGif(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class Attachment(typing.TypedDict, total=False):
    attachmentDataRef: AttachmentDataRef
    contentName: str
    contentType: str
    downloadUri: str
    driveDataRef: DriveDataRef
    name: str
    source: typing.Literal["SOURCE_UNSPECIFIED", "DRIVE_FILE", "UPLOADED_CONTENT"]
    thumbnailUri: str

@typing.type_check_only
class AttachmentDataRef(typing.TypedDict, total=False):
    attachmentUploadToken: str
    resourceName: str

@typing.type_check_only
class Audience(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class Availability(typing.TypedDict, total=False):
    customStatus: CustomStatus
    doNotDisturbMetadata: DoNotDisturbMetadata
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "IDLE", "AWAY", "DO_NOT_DISTURB"
    ]

@typing.type_check_only
class Button(typing.TypedDict, total=False):
    imageButton: ImageButton
    textButton: TextButton

@typing.type_check_only
class CalendarEventLinkData(typing.TypedDict, total=False):
    calendarId: str
    eventId: str

@typing.type_check_only
class Card(typing.TypedDict, total=False):
    cardActions: _list[CardAction]
    header: CardHeader
    name: str
    sections: _list[Section]

@typing.type_check_only
class CardAction(typing.TypedDict, total=False):
    actionLabel: str
    onClick: OnClick

@typing.type_check_only
class CardHeader(typing.TypedDict, total=False):
    imageStyle: typing.Literal["IMAGE_STYLE_UNSPECIFIED", "IMAGE", "AVATAR"]
    imageUrl: str
    subtitle: str
    title: str

@typing.type_check_only
class CardWithId(typing.TypedDict, total=False):
    card: GoogleAppsCardV1Card
    cardId: str

@typing.type_check_only
class ChatAppLogEntry(typing.TypedDict, total=False):
    deployment: str
    deploymentFunction: str
    error: Status

@typing.type_check_only
class ChatClientDataSourceMarkup(typing.TypedDict, total=False):
    spaceDataSource: SpaceDataSource

@typing.type_check_only
class ChatSpaceLinkData(typing.TypedDict, total=False):
    message: str
    space: str
    thread: str

@typing.type_check_only
class Color(typing.TypedDict, total=False):
    alpha: float
    blue: float
    green: float
    red: float

@typing.type_check_only
class CommonEventObject(typing.TypedDict, total=False):
    formInputs: dict[str, typing.Any]
    hostApp: typing.Literal[
        "UNSPECIFIED_HOST_APP",
        "GMAIL",
        "CALENDAR",
        "DRIVE",
        "DEMO",
        "DOCS",
        "MEET",
        "SHEETS",
        "SLIDES",
        "DRAWINGS",
        "CHAT",
    ]
    invokedFunction: str
    parameters: dict[str, typing.Any]
    platform: typing.Literal["UNKNOWN_PLATFORM", "WEB", "IOS", "ANDROID"]
    timeZone: TimeZone
    userLocale: str

@typing.type_check_only
class CompleteImportSpaceRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CompleteImportSpaceResponse(typing.TypedDict, total=False):
    space: Space

@typing.type_check_only
class CustomEmoji(typing.TypedDict, total=False):
    emojiName: str
    name: str
    payload: CustomEmojiPayload
    temporaryImageUri: str
    uid: str

@typing.type_check_only
class CustomEmojiMetadata(typing.TypedDict, total=False):
    customEmoji: CustomEmoji

@typing.type_check_only
class CustomEmojiPayload(typing.TypedDict, total=False):
    fileContent: str
    filename: str

@typing.type_check_only
class CustomStatus(typing.TypedDict, total=False):
    emoji: Emoji
    expireTime: str
    text: str
    ttl: str

@typing.type_check_only
class DateInput(typing.TypedDict, total=False):
    msSinceEpoch: str

@typing.type_check_only
class DateTimeInput(typing.TypedDict, total=False):
    hasDate: bool
    hasTime: bool
    msSinceEpoch: str

@typing.type_check_only
class DeletionMetadata(typing.TypedDict, total=False):
    deletionType: typing.Literal[
        "DELETION_TYPE_UNSPECIFIED",
        "CREATOR",
        "SPACE_OWNER",
        "ADMIN",
        "APP_MESSAGE_EXPIRY",
        "CREATOR_VIA_APP",
        "SPACE_OWNER_VIA_APP",
        "SPACE_MEMBER",
    ]

@typing.type_check_only
class DeprecatedEvent(typing.TypedDict, total=False):
    action: FormAction
    appCommandMetadata: AppCommandMetadata
    common: CommonEventObject
    configCompleteRedirectUrl: str
    dialogEventType: typing.Literal[
        "TYPE_UNSPECIFIED", "REQUEST_DIALOG", "SUBMIT_DIALOG", "CANCEL_DIALOG"
    ]
    eventTime: str
    isDialogEvent: bool
    message: Message
    space: Space
    thread: Thread
    threadKey: str
    token: str
    type: typing.Literal[
        "UNSPECIFIED",
        "MESSAGE",
        "ADDED_TO_SPACE",
        "REMOVED_FROM_SPACE",
        "CARD_CLICKED",
        "WIDGET_UPDATED",
        "APP_COMMAND",
    ]
    user: User

@typing.type_check_only
class Dialog(typing.TypedDict, total=False):
    body: GoogleAppsCardV1Card

@typing.type_check_only
class DialogAction(typing.TypedDict, total=False):
    actionStatus: ActionStatus
    dialog: Dialog

@typing.type_check_only
class DoNotDisturbMetadata(typing.TypedDict, total=False):
    expirationTime: str

@typing.type_check_only
class DriveDataRef(typing.TypedDict, total=False):
    driveFileId: str

@typing.type_check_only
class DriveLinkData(typing.TypedDict, total=False):
    driveDataRef: DriveDataRef
    mimeType: str

@typing.type_check_only
class Emoji(typing.TypedDict, total=False):
    customEmoji: CustomEmoji
    unicode: str

@typing.type_check_only
class EmojiReactionSummary(typing.TypedDict, total=False):
    emoji: Emoji
    reactionCount: int

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class FindGroupChatsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    spaces: _list[Space]

@typing.type_check_only
class FormAction(typing.TypedDict, total=False):
    actionMethodName: str
    parameters: _list[ActionParameter]

@typing.type_check_only
class ForwardedMetadata(typing.TypedDict, total=False):
    space: str
    spaceDisplayName: str

@typing.type_check_only
class GoogleAppsCardV1Action(typing.TypedDict, total=False):
    allWidgetsAreRequired: bool
    function: str
    interaction: typing.Literal["INTERACTION_UNSPECIFIED", "OPEN_DIALOG"]
    loadIndicator: typing.Literal["SPINNER", "NONE"]
    parameters: _list[GoogleAppsCardV1ActionParameter]
    persistValues: bool
    requiredWidgets: _list[str]

@typing.type_check_only
class GoogleAppsCardV1ActionParameter(typing.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class GoogleAppsCardV1BorderStyle(typing.TypedDict, total=False):
    cornerRadius: int
    strokeColor: Color
    type: typing.Literal["BORDER_TYPE_UNSPECIFIED", "NO_BORDER", "STROKE"]

@typing.type_check_only
class GoogleAppsCardV1Button(typing.TypedDict, total=False):
    altText: str
    color: Color
    disabled: bool
    icon: GoogleAppsCardV1Icon
    onClick: GoogleAppsCardV1OnClick
    text: str
    type: typing.Literal[
        "TYPE_UNSPECIFIED", "OUTLINED", "FILLED", "FILLED_TONAL", "BORDERLESS"
    ]

@typing.type_check_only
class GoogleAppsCardV1ButtonList(typing.TypedDict, total=False):
    buttons: _list[GoogleAppsCardV1Button]

@typing.type_check_only
class GoogleAppsCardV1Card(typing.TypedDict, total=False):
    cardActions: _list[GoogleAppsCardV1CardAction]
    displayStyle: typing.Literal["DISPLAY_STYLE_UNSPECIFIED", "PEEK", "REPLACE"]
    expressionData: _list[GoogleAppsCardV1ExpressionData]
    fixedFooter: GoogleAppsCardV1CardFixedFooter
    header: GoogleAppsCardV1CardHeader
    name: str
    peekCardHeader: GoogleAppsCardV1CardHeader
    sectionDividerStyle: typing.Literal[
        "DIVIDER_STYLE_UNSPECIFIED", "SOLID_DIVIDER", "NO_DIVIDER"
    ]
    sections: _list[GoogleAppsCardV1Section]

@typing.type_check_only
class GoogleAppsCardV1CardAction(typing.TypedDict, total=False):
    actionLabel: str
    onClick: GoogleAppsCardV1OnClick

@typing.type_check_only
class GoogleAppsCardV1CardFixedFooter(typing.TypedDict, total=False):
    primaryButton: GoogleAppsCardV1Button
    secondaryButton: GoogleAppsCardV1Button

@typing.type_check_only
class GoogleAppsCardV1CardHeader(typing.TypedDict, total=False):
    imageAltText: str
    imageType: typing.Literal["SQUARE", "CIRCLE"]
    imageUrl: str
    subtitle: str
    title: str

@typing.type_check_only
class GoogleAppsCardV1Carousel(typing.TypedDict, total=False):
    carouselCards: _list[GoogleAppsCardV1CarouselCard]

@typing.type_check_only
class GoogleAppsCardV1CarouselCard(typing.TypedDict, total=False):
    footerWidgets: _list[GoogleAppsCardV1NestedWidget]
    widgets: _list[GoogleAppsCardV1NestedWidget]

@typing.type_check_only
class GoogleAppsCardV1Chip(typing.TypedDict, total=False):
    altText: str
    disabled: bool
    enabled: bool
    icon: GoogleAppsCardV1Icon
    label: str
    onClick: GoogleAppsCardV1OnClick

@typing.type_check_only
class GoogleAppsCardV1ChipList(typing.TypedDict, total=False):
    chips: _list[GoogleAppsCardV1Chip]
    layout: typing.Literal["LAYOUT_UNSPECIFIED", "WRAPPED", "HORIZONTAL_SCROLLABLE"]

@typing.type_check_only
class GoogleAppsCardV1CollapseControl(typing.TypedDict, total=False):
    collapseButton: GoogleAppsCardV1Button
    expandButton: GoogleAppsCardV1Button
    horizontalAlignment: typing.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END"
    ]

@typing.type_check_only
class GoogleAppsCardV1Column(typing.TypedDict, total=False):
    horizontalAlignment: typing.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END"
    ]
    horizontalSizeStyle: typing.Literal[
        "HORIZONTAL_SIZE_STYLE_UNSPECIFIED",
        "FILL_AVAILABLE_SPACE",
        "FILL_MINIMUM_SPACE",
    ]
    verticalAlignment: typing.Literal[
        "VERTICAL_ALIGNMENT_UNSPECIFIED", "CENTER", "TOP", "BOTTOM"
    ]
    widgets: _list[GoogleAppsCardV1Widgets]

@typing.type_check_only
class GoogleAppsCardV1Columns(typing.TypedDict, total=False):
    columnItems: _list[GoogleAppsCardV1Column]

@typing.type_check_only
class GoogleAppsCardV1CommonWidgetAction(typing.TypedDict, total=False):
    updateVisibilityAction: GoogleAppsCardV1UpdateVisibilityAction

@typing.type_check_only
class GoogleAppsCardV1Condition(typing.TypedDict, total=False):
    actionRuleId: str
    expressionDataCondition: GoogleAppsCardV1ExpressionDataCondition

@typing.type_check_only
class GoogleAppsCardV1DataSourceConfig(typing.TypedDict, total=False):
    minCharactersTrigger: int
    platformDataSource: GoogleAppsCardV1PlatformDataSource
    remoteDataSource: GoogleAppsCardV1Action

@typing.type_check_only
class GoogleAppsCardV1DateTimePicker(typing.TypedDict, total=False):
    hostAppDataSource: HostAppDataSourceMarkup
    label: str
    name: str
    onChangeAction: GoogleAppsCardV1Action
    timezoneOffsetDate: int
    type: typing.Literal["DATE_AND_TIME", "DATE_ONLY", "TIME_ONLY"]
    valueMsEpoch: str

@typing.type_check_only
class GoogleAppsCardV1DecoratedText(typing.TypedDict, total=False):
    bottomLabel: str
    bottomLabelText: GoogleAppsCardV1TextParagraph
    button: GoogleAppsCardV1Button
    contentText: GoogleAppsCardV1TextParagraph
    endIcon: GoogleAppsCardV1Icon
    icon: GoogleAppsCardV1Icon
    onClick: GoogleAppsCardV1OnClick
    startIcon: GoogleAppsCardV1Icon
    startIconVerticalAlignment: typing.Literal[
        "VERTICAL_ALIGNMENT_UNSPECIFIED", "TOP", "MIDDLE", "BOTTOM"
    ]
    switchControl: GoogleAppsCardV1SwitchControl
    text: str
    topLabel: str
    topLabelText: GoogleAppsCardV1TextParagraph
    wrapText: bool

@typing.type_check_only
class GoogleAppsCardV1Divider(typing.TypedDict, total=False): ...

@typing.type_check_only
class GoogleAppsCardV1EventAction(typing.TypedDict, total=False):
    actionRuleId: str
    commonWidgetAction: GoogleAppsCardV1CommonWidgetAction
    postEventTriggers: _list[GoogleAppsCardV1Trigger]

@typing.type_check_only
class GoogleAppsCardV1ExpressionData(typing.TypedDict, total=False):
    conditions: _list[GoogleAppsCardV1Condition]
    eventActions: _list[GoogleAppsCardV1EventAction]
    expression: str
    id: str

@typing.type_check_only
class GoogleAppsCardV1ExpressionDataCondition(typing.TypedDict, total=False):
    conditionType: typing.Literal[
        "CONDITION_TYPE_UNSPECIFIED",
        "EXPRESSION_EVALUATION_SUCCESS",
        "EXPRESSION_EVALUATION_FAILURE",
    ]

@typing.type_check_only
class GoogleAppsCardV1Grid(typing.TypedDict, total=False):
    borderStyle: GoogleAppsCardV1BorderStyle
    columnCount: int
    items: _list[GoogleAppsCardV1GridItem]
    onClick: GoogleAppsCardV1OnClick
    title: str

@typing.type_check_only
class GoogleAppsCardV1GridItem(typing.TypedDict, total=False):
    id: str
    image: GoogleAppsCardV1ImageComponent
    layout: typing.Literal["GRID_ITEM_LAYOUT_UNSPECIFIED", "TEXT_BELOW", "TEXT_ABOVE"]
    subtitle: str
    title: str

@typing.type_check_only
class GoogleAppsCardV1Icon(typing.TypedDict, total=False):
    altText: str
    iconUrl: str
    imageType: typing.Literal["SQUARE", "CIRCLE"]
    knownIcon: str
    materialIcon: GoogleAppsCardV1MaterialIcon

@typing.type_check_only
class GoogleAppsCardV1Image(typing.TypedDict, total=False):
    altText: str
    imageUrl: str
    onClick: GoogleAppsCardV1OnClick

@typing.type_check_only
class GoogleAppsCardV1ImageComponent(typing.TypedDict, total=False):
    altText: str
    borderStyle: GoogleAppsCardV1BorderStyle
    cropStyle: GoogleAppsCardV1ImageCropStyle
    imageUri: str

@typing.type_check_only
class GoogleAppsCardV1ImageCropStyle(typing.TypedDict, total=False):
    aspectRatio: float
    type: typing.Literal[
        "IMAGE_CROP_TYPE_UNSPECIFIED",
        "SQUARE",
        "CIRCLE",
        "RECTANGLE_CUSTOM",
        "RECTANGLE_4_3",
    ]

@typing.type_check_only
class GoogleAppsCardV1MaterialIcon(typing.TypedDict, total=False):
    fill: bool
    grade: int
    name: str
    weight: int

@typing.type_check_only
class GoogleAppsCardV1NestedWidget(typing.TypedDict, total=False):
    buttonList: GoogleAppsCardV1ButtonList
    image: GoogleAppsCardV1Image
    textParagraph: GoogleAppsCardV1TextParagraph

@typing.type_check_only
class GoogleAppsCardV1OnClick(typing.TypedDict, total=False):
    action: GoogleAppsCardV1Action
    card: GoogleAppsCardV1Card
    openDynamicLinkAction: GoogleAppsCardV1Action
    openLink: GoogleAppsCardV1OpenLink
    overflowMenu: GoogleAppsCardV1OverflowMenu

@typing.type_check_only
class GoogleAppsCardV1OpenLink(typing.TypedDict, total=False):
    onClose: typing.Literal["NOTHING", "RELOAD"]
    openAs: typing.Literal["FULL_SIZE", "OVERLAY"]
    url: str

@typing.type_check_only
class GoogleAppsCardV1OverflowMenu(typing.TypedDict, total=False):
    items: _list[GoogleAppsCardV1OverflowMenuItem]

@typing.type_check_only
class GoogleAppsCardV1OverflowMenuItem(typing.TypedDict, total=False):
    disabled: bool
    onClick: GoogleAppsCardV1OnClick
    startIcon: GoogleAppsCardV1Icon
    text: str

@typing.type_check_only
class GoogleAppsCardV1PlatformDataSource(typing.TypedDict, total=False):
    commonDataSource: typing.Literal["UNKNOWN", "USER"]
    hostAppDataSource: HostAppDataSourceMarkup

@typing.type_check_only
class GoogleAppsCardV1Section(typing.TypedDict, total=False):
    collapseControl: GoogleAppsCardV1CollapseControl
    collapsible: bool
    header: str
    id: str
    uncollapsibleWidgetsCount: int
    widgets: _list[GoogleAppsCardV1Widget]

@typing.type_check_only
class GoogleAppsCardV1SelectionInput(typing.TypedDict, total=False):
    dataSourceConfigs: _list[GoogleAppsCardV1DataSourceConfig]
    externalDataSource: GoogleAppsCardV1Action
    hintText: str
    items: _list[GoogleAppsCardV1SelectionItem]
    label: str
    multiSelectMaxSelectedItems: int
    multiSelectMinQueryLength: int
    name: str
    onChangeAction: GoogleAppsCardV1Action
    platformDataSource: GoogleAppsCardV1PlatformDataSource
    type: typing.Literal[
        "CHECK_BOX", "RADIO_BUTTON", "SWITCH", "DROPDOWN", "MULTI_SELECT"
    ]

@typing.type_check_only
class GoogleAppsCardV1SelectionItem(typing.TypedDict, total=False):
    bottomText: str
    selected: bool
    startIconUri: str
    text: str
    value: str

@typing.type_check_only
class GoogleAppsCardV1SuggestionItem(typing.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleAppsCardV1Suggestions(typing.TypedDict, total=False):
    items: _list[GoogleAppsCardV1SuggestionItem]

@typing.type_check_only
class GoogleAppsCardV1SwitchControl(typing.TypedDict, total=False):
    controlType: typing.Literal["SWITCH", "CHECKBOX", "CHECK_BOX"]
    name: str
    onChangeAction: GoogleAppsCardV1Action
    selected: bool
    value: str

@typing.type_check_only
class GoogleAppsCardV1TextInput(typing.TypedDict, total=False):
    autoCompleteAction: GoogleAppsCardV1Action
    hintText: str
    hostAppDataSource: HostAppDataSourceMarkup
    initialSuggestions: GoogleAppsCardV1Suggestions
    label: str
    name: str
    onChangeAction: GoogleAppsCardV1Action
    placeholderText: str
    type: typing.Literal["SINGLE_LINE", "MULTIPLE_LINE"]
    validation: GoogleAppsCardV1Validation
    value: str

@typing.type_check_only
class GoogleAppsCardV1TextParagraph(typing.TypedDict, total=False):
    maxLines: int
    text: str
    textSyntax: typing.Literal["TEXT_SYNTAX_UNSPECIFIED", "HTML", "MARKDOWN"]

@typing.type_check_only
class GoogleAppsCardV1Trigger(typing.TypedDict, total=False):
    actionRuleId: str

@typing.type_check_only
class GoogleAppsCardV1UpdateVisibilityAction(typing.TypedDict, total=False):
    visibility: typing.Literal["VISIBILITY_UNSPECIFIED", "VISIBLE", "HIDDEN"]

@typing.type_check_only
class GoogleAppsCardV1Validation(typing.TypedDict, total=False):
    characterLimit: int
    inputType: typing.Literal[
        "INPUT_TYPE_UNSPECIFIED", "TEXT", "INTEGER", "FLOAT", "EMAIL", "EMOJI_PICKER"
    ]

@typing.type_check_only
class GoogleAppsCardV1Widget(typing.TypedDict, total=False):
    buttonList: GoogleAppsCardV1ButtonList
    carousel: GoogleAppsCardV1Carousel
    chipList: GoogleAppsCardV1ChipList
    columns: GoogleAppsCardV1Columns
    dateTimePicker: GoogleAppsCardV1DateTimePicker
    decoratedText: GoogleAppsCardV1DecoratedText
    divider: GoogleAppsCardV1Divider
    eventActions: _list[GoogleAppsCardV1EventAction]
    grid: GoogleAppsCardV1Grid
    horizontalAlignment: typing.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END"
    ]
    id: str
    image: GoogleAppsCardV1Image
    selectionInput: GoogleAppsCardV1SelectionInput
    textInput: GoogleAppsCardV1TextInput
    textParagraph: GoogleAppsCardV1TextParagraph
    visibility: typing.Literal["VISIBILITY_UNSPECIFIED", "VISIBLE", "HIDDEN"]

@typing.type_check_only
class GoogleAppsCardV1Widgets(typing.TypedDict, total=False):
    buttonList: GoogleAppsCardV1ButtonList
    chipList: GoogleAppsCardV1ChipList
    dateTimePicker: GoogleAppsCardV1DateTimePicker
    decoratedText: GoogleAppsCardV1DecoratedText
    image: GoogleAppsCardV1Image
    selectionInput: GoogleAppsCardV1SelectionInput
    textInput: GoogleAppsCardV1TextInput
    textParagraph: GoogleAppsCardV1TextParagraph

@typing.type_check_only
class GoogleChatV1Section(typing.TypedDict, total=False):
    displayName: str
    name: str
    sortOrder: int
    type: typing.Literal[
        "SECTION_TYPE_UNSPECIFIED",
        "CUSTOM_SECTION",
        "DEFAULT_DIRECT_MESSAGES",
        "DEFAULT_SPACES",
        "DEFAULT_APPS",
    ]

@typing.type_check_only
class Group(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class HostAppDataSourceMarkup(typing.TypedDict, total=False):
    chatDataSource: ChatClientDataSourceMarkup
    workflowDataSource: WorkflowDataSourceMarkup

@typing.type_check_only
class Image(typing.TypedDict, total=False):
    aspectRatio: float
    imageUrl: str
    onClick: OnClick

@typing.type_check_only
class ImageButton(typing.TypedDict, total=False):
    icon: typing.Literal[
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
    onClick: OnClick

@typing.type_check_only
class Inputs(typing.TypedDict, total=False):
    dateInput: DateInput
    dateTimeInput: DateTimeInput
    stringInputs: StringInputs
    timeInput: TimeInput

@typing.type_check_only
class KeyValue(typing.TypedDict, total=False):
    bottomLabel: str
    button: Button
    content: str
    contentMultiline: bool
    icon: typing.Literal[
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
    onClick: OnClick
    topLabel: str

@typing.type_check_only
class ListCustomEmojisResponse(typing.TypedDict, total=False):
    customEmojis: _list[CustomEmoji]
    nextPageToken: str

@typing.type_check_only
class ListMembershipsResponse(typing.TypedDict, total=False):
    memberships: _list[Membership]
    nextPageToken: str

@typing.type_check_only
class ListMessagesResponse(typing.TypedDict, total=False):
    messages: _list[Message]
    nextPageToken: str

@typing.type_check_only
class ListReactionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    reactions: _list[Reaction]

@typing.type_check_only
class ListSectionItemsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sectionItems: _list[SectionItem]

@typing.type_check_only
class ListSectionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sections: _list[GoogleChatV1Section]

@typing.type_check_only
class ListSpaceEventsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    spaceEvents: _list[SpaceEvent]

@typing.type_check_only
class ListSpacesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    spaces: _list[Space]

@typing.type_check_only
class MarkAsActiveRequest(typing.TypedDict, total=False):
    expireTime: str
    ttl: str

@typing.type_check_only
class MarkAsAwayRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class MarkAsDoNotDisturbRequest(typing.TypedDict, total=False):
    expireTime: str
    ttl: str

@typing.type_check_only
class MatchedUrl(typing.TypedDict, total=False):
    url: str

@typing.type_check_only
class Media(typing.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class MeetSpaceLinkData(typing.TypedDict, total=False):
    huddleStatus: typing.Literal[
        "HUDDLE_STATUS_UNSPECIFIED", "STARTED", "ENDED", "MISSED"
    ]
    meetingCode: str
    type: typing.Literal["TYPE_UNSPECIFIED", "MEETING", "HUDDLE"]

@typing.type_check_only
class Membership(typing.TypedDict, total=False):
    affiliation: typing.Literal[
        "AFFILIATION_UNSPECIFIED", "INTERNAL", "EXTERNAL", "MANAGED_EXTERNAL"
    ]
    createTime: str
    deleteTime: str
    groupMember: Group
    member: User
    name: str
    role: typing.Literal[
        "MEMBERSHIP_ROLE_UNSPECIFIED",
        "ROLE_MEMBER",
        "ROLE_MANAGER",
        "ROLE_ASSISTANT_MANAGER",
    ]
    state: typing.Literal[
        "MEMBERSHIP_STATE_UNSPECIFIED", "JOINED", "INVITED", "NOT_A_MEMBER"
    ]

@typing.type_check_only
class MembershipBatchCreatedEventData(typing.TypedDict, total=False):
    memberships: _list[MembershipCreatedEventData]

@typing.type_check_only
class MembershipBatchDeletedEventData(typing.TypedDict, total=False):
    memberships: _list[MembershipDeletedEventData]

@typing.type_check_only
class MembershipBatchUpdatedEventData(typing.TypedDict, total=False):
    memberships: _list[MembershipUpdatedEventData]

@typing.type_check_only
class MembershipCount(typing.TypedDict, total=False):
    joinedDirectHumanUserCount: int
    joinedGroupCount: int

@typing.type_check_only
class MembershipCreatedEventData(typing.TypedDict, total=False):
    membership: Membership

@typing.type_check_only
class MembershipDeletedEventData(typing.TypedDict, total=False):
    membership: Membership

@typing.type_check_only
class MembershipUpdatedEventData(typing.TypedDict, total=False):
    membership: Membership

@typing.type_check_only
class Message(typing.TypedDict, total=False):
    accessoryWidgets: _list[AccessoryWidget]
    actionResponse: ActionResponse
    annotations: _list[Annotation]
    argumentText: str
    attachedGifs: _list[AttachedGif]
    attachment: _list[Attachment]
    cards: _list[Card]
    cardsV2: _list[CardWithId]
    clientAssignedMessageId: str
    createTime: str
    deleteTime: str
    deletionMetadata: DeletionMetadata
    emojiReactionSummaries: _list[EmojiReactionSummary]
    fallbackText: str
    formattedText: str
    lastUpdateTime: str
    markupSyntax: typing.Literal[
        "MARKUP_SYNTAX_UNSPECIFIED", "MARKUP_SYNTAX_CHAT", "MARKUP_SYNTAX_MARKDOWN"
    ]
    matchedUrl: MatchedUrl
    name: str
    privateMessageViewer: User
    quotedMessageMetadata: QuotedMessageMetadata
    sender: User
    silent: bool
    slashCommand: SlashCommand
    space: Space
    text: str
    thread: Thread
    threadReply: bool

@typing.type_check_only
class MessageBatchCreatedEventData(typing.TypedDict, total=False):
    messages: _list[MessageCreatedEventData]

@typing.type_check_only
class MessageBatchDeletedEventData(typing.TypedDict, total=False):
    messages: _list[MessageDeletedEventData]

@typing.type_check_only
class MessageBatchUpdatedEventData(typing.TypedDict, total=False):
    messages: _list[MessageUpdatedEventData]

@typing.type_check_only
class MessageCreatedEventData(typing.TypedDict, total=False):
    message: Message

@typing.type_check_only
class MessageDeletedEventData(typing.TypedDict, total=False):
    message: Message

@typing.type_check_only
class MessageUpdatedEventData(typing.TypedDict, total=False):
    message: Message

@typing.type_check_only
class MoveSectionItemRequest(typing.TypedDict, total=False):
    targetSection: str

@typing.type_check_only
class MoveSectionItemResponse(typing.TypedDict, total=False):
    sectionItem: SectionItem

@typing.type_check_only
class OnClick(typing.TypedDict, total=False):
    action: FormAction
    openLink: OpenLink

@typing.type_check_only
class OpenLink(typing.TypedDict, total=False):
    url: str

@typing.type_check_only
class PermissionSetting(typing.TypedDict, total=False):
    assistantManagersAllowed: bool
    managersAllowed: bool
    membersAllowed: bool

@typing.type_check_only
class PermissionSettings(typing.TypedDict, total=False):
    manageApps: PermissionSetting
    manageMembersAndGroups: PermissionSetting
    manageWebhooks: PermissionSetting
    modifySpaceDetails: PermissionSetting
    postMessages: PermissionSetting
    replyMessages: PermissionSetting
    toggleHistory: PermissionSetting
    useAtMentionAll: PermissionSetting

@typing.type_check_only
class PositionSectionRequest(typing.TypedDict, total=False):
    relativePosition: typing.Literal["POSITION_UNSPECIFIED", "START", "END"]
    sortOrder: int

@typing.type_check_only
class PositionSectionResponse(typing.TypedDict, total=False):
    section: GoogleChatV1Section

@typing.type_check_only
class Principal(typing.TypedDict, total=False):
    audience: Audience

@typing.type_check_only
class QuotedMessageMetadata(typing.TypedDict, total=False):
    forwardedMetadata: ForwardedMetadata
    lastUpdateTime: str
    name: str
    quoteType: typing.Literal["QUOTE_TYPE_UNSPECIFIED", "REPLY", "FORWARD"]
    quotedMessageSnapshot: QuotedMessageSnapshot

@typing.type_check_only
class QuotedMessageSnapshot(typing.TypedDict, total=False):
    annotations: _list[Annotation]
    attachments: _list[Attachment]
    formattedText: str
    sender: str
    text: str

@typing.type_check_only
class Reaction(typing.TypedDict, total=False):
    emoji: Emoji
    name: str
    user: User

@typing.type_check_only
class ReactionBatchCreatedEventData(typing.TypedDict, total=False):
    reactions: _list[ReactionCreatedEventData]

@typing.type_check_only
class ReactionBatchDeletedEventData(typing.TypedDict, total=False):
    reactions: _list[ReactionDeletedEventData]

@typing.type_check_only
class ReactionCreatedEventData(typing.TypedDict, total=False):
    reaction: Reaction

@typing.type_check_only
class ReactionDeletedEventData(typing.TypedDict, total=False):
    reaction: Reaction

@typing.type_check_only
class RichLinkMetadata(typing.TypedDict, total=False):
    calendarEventLinkData: CalendarEventLinkData
    chatSpaceLinkData: ChatSpaceLinkData
    driveLinkData: DriveLinkData
    meetSpaceLinkData: MeetSpaceLinkData
    richLinkType: typing.Literal[
        "RICH_LINK_TYPE_UNSPECIFIED",
        "DRIVE_FILE",
        "CHAT_SPACE",
        "GMAIL_MESSAGE",
        "MEET_SPACE",
        "CALENDAR_EVENT",
    ]
    uri: str

@typing.type_check_only
class SearchMessageResult(typing.TypedDict, total=False):
    message: Message
    read: bool
    spaceMuteSetting: typing.Literal["MUTE_SETTING_UNSPECIFIED", "UNMUTED", "MUTED"]

@typing.type_check_only
class SearchMessagesRequest(typing.TypedDict, total=False):
    filter: str
    markupSyntax: typing.Literal[
        "MARKUP_SYNTAX_UNSPECIFIED", "MARKUP_SYNTAX_CHAT", "MARKUP_SYNTAX_MARKDOWN"
    ]
    orderBy: str
    pageSize: int
    pageToken: str
    view: typing.Literal[
        "SEARCH_MESSAGES_VIEW_UNSPECIFIED",
        "SEARCH_MESSAGES_VIEW_BASIC",
        "SEARCH_MESSAGES_VIEW_FULL",
    ]

@typing.type_check_only
class SearchMessagesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    results: _list[SearchMessageResult]

@typing.type_check_only
class SearchSpaceResult(typing.TypedDict, total=False):
    space: Space

@typing.type_check_only
class SearchSpacesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    results: _list[SearchSpaceResult]
    spaces: _list[Space]
    totalSize: int

@typing.type_check_only
class Section(typing.TypedDict, total=False):
    header: str
    widgets: _list[WidgetMarkup]

@typing.type_check_only
class SectionItem(typing.TypedDict, total=False):
    name: str
    space: str

@typing.type_check_only
class SelectionItems(typing.TypedDict, total=False):
    items: _list[GoogleAppsCardV1SelectionItem]

@typing.type_check_only
class SetUpSpaceRequest(typing.TypedDict, total=False):
    memberships: _list[Membership]
    requestId: str
    space: Space

@typing.type_check_only
class SlashCommand(typing.TypedDict, total=False):
    commandId: str

@typing.type_check_only
class SlashCommandMetadata(typing.TypedDict, total=False):
    bot: User
    commandId: str
    commandName: str
    triggersDialog: bool
    type: typing.Literal["TYPE_UNSPECIFIED", "ADD", "INVOKE"]

@typing.type_check_only
class Space(typing.TypedDict, total=False):
    accessSettings: AccessSettings
    adminInstalled: bool
    createTime: str
    customer: str
    displayName: str
    externalUserAllowed: bool
    importMode: bool
    importModeExpireTime: str
    lastActiveTime: str
    membershipCount: MembershipCount
    name: str
    permissionSettings: PermissionSettings
    predefinedPermissionSettings: typing.Literal[
        "PREDEFINED_PERMISSION_SETTINGS_UNSPECIFIED",
        "COLLABORATION_SPACE",
        "ANNOUNCEMENT_SPACE",
    ]
    singleUserBotDm: bool
    spaceDetails: SpaceDetails
    spaceHistoryState: typing.Literal[
        "HISTORY_STATE_UNSPECIFIED", "HISTORY_OFF", "HISTORY_ON"
    ]
    spaceThreadingState: typing.Literal[
        "SPACE_THREADING_STATE_UNSPECIFIED",
        "THREADED_MESSAGES",
        "GROUPED_MESSAGES",
        "UNTHREADED_MESSAGES",
    ]
    spaceType: typing.Literal[
        "SPACE_TYPE_UNSPECIFIED", "SPACE", "GROUP_CHAT", "DIRECT_MESSAGE"
    ]
    spaceUri: str
    threaded: bool
    type: typing.Literal["TYPE_UNSPECIFIED", "ROOM", "DM"]

@typing.type_check_only
class SpaceBatchUpdatedEventData(typing.TypedDict, total=False):
    spaces: _list[SpaceUpdatedEventData]

@typing.type_check_only
class SpaceDataSource(typing.TypedDict, total=False):
    defaultToCurrentSpace: bool

@typing.type_check_only
class SpaceDetails(typing.TypedDict, total=False):
    description: str
    guidelines: str

@typing.type_check_only
class SpaceEvent(typing.TypedDict, total=False):
    eventTime: str
    eventType: str
    membershipBatchCreatedEventData: MembershipBatchCreatedEventData
    membershipBatchDeletedEventData: MembershipBatchDeletedEventData
    membershipBatchUpdatedEventData: MembershipBatchUpdatedEventData
    membershipCreatedEventData: MembershipCreatedEventData
    membershipDeletedEventData: MembershipDeletedEventData
    membershipUpdatedEventData: MembershipUpdatedEventData
    messageBatchCreatedEventData: MessageBatchCreatedEventData
    messageBatchDeletedEventData: MessageBatchDeletedEventData
    messageBatchUpdatedEventData: MessageBatchUpdatedEventData
    messageCreatedEventData: MessageCreatedEventData
    messageDeletedEventData: MessageDeletedEventData
    messageUpdatedEventData: MessageUpdatedEventData
    name: str
    reactionBatchCreatedEventData: ReactionBatchCreatedEventData
    reactionBatchDeletedEventData: ReactionBatchDeletedEventData
    reactionCreatedEventData: ReactionCreatedEventData
    reactionDeletedEventData: ReactionDeletedEventData
    spaceBatchUpdatedEventData: SpaceBatchUpdatedEventData
    spaceUpdatedEventData: SpaceUpdatedEventData

@typing.type_check_only
class SpaceNotificationSetting(typing.TypedDict, total=False):
    muteSetting: typing.Literal["MUTE_SETTING_UNSPECIFIED", "UNMUTED", "MUTED"]
    name: str
    notificationSetting: typing.Literal[
        "NOTIFICATION_SETTING_UNSPECIFIED",
        "ALL",
        "MAIN_CONVERSATIONS",
        "FOR_YOU",
        "OFF",
    ]

@typing.type_check_only
class SpaceReadState(typing.TypedDict, total=False):
    lastReadTime: str
    name: str

@typing.type_check_only
class SpaceUpdatedEventData(typing.TypedDict, total=False):
    space: Space

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StringInputs(typing.TypedDict, total=False):
    value: _list[str]

@typing.type_check_only
class TextButton(typing.TypedDict, total=False):
    onClick: OnClick
    text: str

@typing.type_check_only
class TextParagraph(typing.TypedDict, total=False):
    text: str

@typing.type_check_only
class Thread(typing.TypedDict, total=False):
    name: str
    threadKey: str

@typing.type_check_only
class ThreadReadState(typing.TypedDict, total=False):
    lastReadTime: str
    name: str

@typing.type_check_only
class TimeInput(typing.TypedDict, total=False):
    hours: int
    minutes: int

@typing.type_check_only
class TimeZone(typing.TypedDict, total=False):
    id: str
    offset: int

@typing.type_check_only
class UpdatedWidget(typing.TypedDict, total=False):
    suggestions: SelectionItems
    widget: str

@typing.type_check_only
class UploadAttachmentRequest(typing.TypedDict, total=False):
    filename: str

@typing.type_check_only
class UploadAttachmentResponse(typing.TypedDict, total=False):
    attachmentDataRef: AttachmentDataRef

@typing.type_check_only
class User(typing.TypedDict, total=False):
    displayName: str
    domainId: str
    isAnonymous: bool
    name: str
    type: typing.Literal["TYPE_UNSPECIFIED", "HUMAN", "BOT"]

@typing.type_check_only
class UserMentionMetadata(typing.TypedDict, total=False):
    type: typing.Literal["TYPE_UNSPECIFIED", "ADD", "MENTION"]
    user: User

@typing.type_check_only
class WidgetMarkup(typing.TypedDict, total=False):
    buttons: _list[Button]
    image: Image
    keyValue: KeyValue
    textParagraph: TextParagraph

@typing.type_check_only
class WorkflowDataSourceMarkup(typing.TypedDict, total=False):
    includeVariables: bool
    type: typing.Literal["UNKNOWN", "USER", "SPACE", "USER_WITH_FREE_FORM"]

import typing

import typing_extensions

_list = list

@typing.type_check_only
class AccessSettings(typing_extensions.TypedDict, total=False):
    accessState: typing_extensions.Literal[
        "ACCESS_STATE_UNSPECIFIED", "PRIVATE", "DISCOVERABLE"
    ]
    audience: str

@typing.type_check_only
class AccessoryWidget(typing_extensions.TypedDict, total=False):
    buttonList: GoogleAppsCardV1ButtonList

@typing.type_check_only
class ActionParameter(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class ActionResponse(typing_extensions.TypedDict, total=False):
    dialogAction: DialogAction
    type: typing_extensions.Literal[
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
class ActionStatus(typing_extensions.TypedDict, total=False):
    statusCode: typing_extensions.Literal[
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
class Annotation(typing_extensions.TypedDict, total=False):
    length: int
    richLinkMetadata: RichLinkMetadata
    slashCommand: SlashCommandMetadata
    startIndex: int
    type: typing_extensions.Literal[
        "ANNOTATION_TYPE_UNSPECIFIED", "USER_MENTION", "SLASH_COMMAND", "RICH_LINK"
    ]
    userMention: UserMentionMetadata

@typing.type_check_only
class AttachedGif(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class Attachment(typing_extensions.TypedDict, total=False):
    attachmentDataRef: AttachmentDataRef
    contentName: str
    contentType: str
    downloadUri: str
    driveDataRef: DriveDataRef
    name: str
    source: typing_extensions.Literal[
        "SOURCE_UNSPECIFIED", "DRIVE_FILE", "UPLOADED_CONTENT"
    ]
    thumbnailUri: str

@typing.type_check_only
class AttachmentDataRef(typing_extensions.TypedDict, total=False):
    attachmentUploadToken: str
    resourceName: str

@typing.type_check_only
class Button(typing_extensions.TypedDict, total=False):
    imageButton: ImageButton
    textButton: TextButton

@typing.type_check_only
class Card(typing_extensions.TypedDict, total=False):
    cardActions: _list[CardAction]
    header: CardHeader
    name: str
    sections: _list[Section]

@typing.type_check_only
class CardAction(typing_extensions.TypedDict, total=False):
    actionLabel: str
    onClick: OnClick

@typing.type_check_only
class CardHeader(typing_extensions.TypedDict, total=False):
    imageStyle: typing_extensions.Literal["IMAGE_STYLE_UNSPECIFIED", "IMAGE", "AVATAR"]
    imageUrl: str
    subtitle: str
    title: str

@typing.type_check_only
class CardWithId(typing_extensions.TypedDict, total=False):
    card: GoogleAppsCardV1Card
    cardId: str

@typing.type_check_only
class ChatAppLogEntry(typing_extensions.TypedDict, total=False):
    deployment: str
    deploymentFunction: str
    error: Status

@typing.type_check_only
class ChatClientDataSourceMarkup(typing_extensions.TypedDict, total=False):
    spaceDataSource: SpaceDataSource

@typing.type_check_only
class ChatSpaceLinkData(typing_extensions.TypedDict, total=False):
    message: str
    space: str
    thread: str

@typing.type_check_only
class Color(typing_extensions.TypedDict, total=False):
    alpha: float
    blue: float
    green: float
    red: float

@typing.type_check_only
class CommonEventObject(typing_extensions.TypedDict, total=False):
    formInputs: dict[str, typing.Any]
    hostApp: typing_extensions.Literal[
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
    platform: typing_extensions.Literal["UNKNOWN_PLATFORM", "WEB", "IOS", "ANDROID"]
    timeZone: TimeZone
    userLocale: str

@typing.type_check_only
class CompleteImportSpaceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CompleteImportSpaceResponse(typing_extensions.TypedDict, total=False):
    space: Space

@typing.type_check_only
class CustomEmoji(typing_extensions.TypedDict, total=False):
    uid: str

@typing.type_check_only
class DateInput(typing_extensions.TypedDict, total=False):
    msSinceEpoch: str

@typing.type_check_only
class DateTimeInput(typing_extensions.TypedDict, total=False):
    hasDate: bool
    hasTime: bool
    msSinceEpoch: str

@typing.type_check_only
class DeletionMetadata(typing_extensions.TypedDict, total=False):
    deletionType: typing_extensions.Literal[
        "DELETION_TYPE_UNSPECIFIED",
        "CREATOR",
        "SPACE_OWNER",
        "ADMIN",
        "APP_MESSAGE_EXPIRY",
        "CREATOR_VIA_APP",
        "SPACE_OWNER_VIA_APP",
    ]

@typing.type_check_only
class DeprecatedEvent(typing_extensions.TypedDict, total=False):
    action: FormAction
    common: CommonEventObject
    configCompleteRedirectUrl: str
    dialogEventType: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "REQUEST_DIALOG", "SUBMIT_DIALOG", "CANCEL_DIALOG"
    ]
    eventTime: str
    isDialogEvent: bool
    message: Message
    space: Space
    threadKey: str
    token: str
    type: typing_extensions.Literal[
        "UNSPECIFIED",
        "MESSAGE",
        "ADDED_TO_SPACE",
        "REMOVED_FROM_SPACE",
        "CARD_CLICKED",
        "WIDGET_UPDATED",
    ]
    user: User

@typing.type_check_only
class Dialog(typing_extensions.TypedDict, total=False):
    body: GoogleAppsCardV1Card

@typing.type_check_only
class DialogAction(typing_extensions.TypedDict, total=False):
    actionStatus: ActionStatus
    dialog: Dialog

@typing.type_check_only
class DriveDataRef(typing_extensions.TypedDict, total=False):
    driveFileId: str

@typing.type_check_only
class DriveLinkData(typing_extensions.TypedDict, total=False):
    driveDataRef: DriveDataRef
    mimeType: str

@typing.type_check_only
class Emoji(typing_extensions.TypedDict, total=False):
    customEmoji: CustomEmoji
    unicode: str

@typing.type_check_only
class EmojiReactionSummary(typing_extensions.TypedDict, total=False):
    emoji: Emoji
    reactionCount: int

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FormAction(typing_extensions.TypedDict, total=False):
    actionMethodName: str
    parameters: _list[ActionParameter]

@typing.type_check_only
class GoogleAppsCardV1Action(typing_extensions.TypedDict, total=False):
    allWidgetsAreRequired: bool
    function: str
    interaction: typing_extensions.Literal["INTERACTION_UNSPECIFIED", "OPEN_DIALOG"]
    loadIndicator: typing_extensions.Literal["SPINNER", "NONE"]
    parameters: _list[GoogleAppsCardV1ActionParameter]
    persistValues: bool
    requiredWidgets: _list[str]

@typing.type_check_only
class GoogleAppsCardV1ActionParameter(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class GoogleAppsCardV1BorderStyle(typing_extensions.TypedDict, total=False):
    cornerRadius: int
    strokeColor: Color
    type: typing_extensions.Literal["BORDER_TYPE_UNSPECIFIED", "NO_BORDER", "STROKE"]

@typing.type_check_only
class GoogleAppsCardV1Button(typing_extensions.TypedDict, total=False):
    altText: str
    color: Color
    disabled: bool
    icon: GoogleAppsCardV1Icon
    onClick: GoogleAppsCardV1OnClick
    text: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "OUTLINED", "FILLED", "FILLED_TONAL", "BORDERLESS"
    ]

@typing.type_check_only
class GoogleAppsCardV1ButtonList(typing_extensions.TypedDict, total=False):
    buttons: _list[GoogleAppsCardV1Button]

@typing.type_check_only
class GoogleAppsCardV1Card(typing_extensions.TypedDict, total=False):
    cardActions: _list[GoogleAppsCardV1CardAction]
    displayStyle: typing_extensions.Literal[
        "DISPLAY_STYLE_UNSPECIFIED", "PEEK", "REPLACE"
    ]
    fixedFooter: GoogleAppsCardV1CardFixedFooter
    header: GoogleAppsCardV1CardHeader
    name: str
    peekCardHeader: GoogleAppsCardV1CardHeader
    sectionDividerStyle: typing_extensions.Literal[
        "DIVIDER_STYLE_UNSPECIFIED", "SOLID_DIVIDER", "NO_DIVIDER"
    ]
    sections: _list[GoogleAppsCardV1Section]

@typing.type_check_only
class GoogleAppsCardV1CardAction(typing_extensions.TypedDict, total=False):
    actionLabel: str
    onClick: GoogleAppsCardV1OnClick

@typing.type_check_only
class GoogleAppsCardV1CardFixedFooter(typing_extensions.TypedDict, total=False):
    primaryButton: GoogleAppsCardV1Button
    secondaryButton: GoogleAppsCardV1Button

@typing.type_check_only
class GoogleAppsCardV1CardHeader(typing_extensions.TypedDict, total=False):
    imageAltText: str
    imageType: typing_extensions.Literal["SQUARE", "CIRCLE"]
    imageUrl: str
    subtitle: str
    title: str

@typing.type_check_only
class GoogleAppsCardV1Carousel(typing_extensions.TypedDict, total=False):
    carouselCards: _list[GoogleAppsCardV1CarouselCard]

@typing.type_check_only
class GoogleAppsCardV1CarouselCard(typing_extensions.TypedDict, total=False):
    footerWidgets: _list[GoogleAppsCardV1NestedWidget]
    widgets: _list[GoogleAppsCardV1NestedWidget]

@typing.type_check_only
class GoogleAppsCardV1Chip(typing_extensions.TypedDict, total=False):
    altText: str
    disabled: bool
    enabled: bool
    icon: GoogleAppsCardV1Icon
    label: str
    onClick: GoogleAppsCardV1OnClick

@typing.type_check_only
class GoogleAppsCardV1ChipList(typing_extensions.TypedDict, total=False):
    chips: _list[GoogleAppsCardV1Chip]
    layout: typing_extensions.Literal[
        "LAYOUT_UNSPECIFIED", "WRAPPED", "HORIZONTAL_SCROLLABLE"
    ]

@typing.type_check_only
class GoogleAppsCardV1CollapseControl(typing_extensions.TypedDict, total=False):
    collapseButton: GoogleAppsCardV1Button
    expandButton: GoogleAppsCardV1Button
    horizontalAlignment: typing_extensions.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END"
    ]

@typing.type_check_only
class GoogleAppsCardV1Column(typing_extensions.TypedDict, total=False):
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
    widgets: _list[GoogleAppsCardV1Widgets]

@typing.type_check_only
class GoogleAppsCardV1Columns(typing_extensions.TypedDict, total=False):
    columnItems: _list[GoogleAppsCardV1Column]

@typing.type_check_only
class GoogleAppsCardV1DateTimePicker(typing_extensions.TypedDict, total=False):
    label: str
    name: str
    onChangeAction: GoogleAppsCardV1Action
    timezoneOffsetDate: int
    type: typing_extensions.Literal["DATE_AND_TIME", "DATE_ONLY", "TIME_ONLY"]
    valueMsEpoch: str

@typing.type_check_only
class GoogleAppsCardV1DecoratedText(typing_extensions.TypedDict, total=False):
    bottomLabel: str
    button: GoogleAppsCardV1Button
    endIcon: GoogleAppsCardV1Icon
    icon: GoogleAppsCardV1Icon
    onClick: GoogleAppsCardV1OnClick
    startIcon: GoogleAppsCardV1Icon
    switchControl: GoogleAppsCardV1SwitchControl
    text: str
    topLabel: str
    wrapText: bool

@typing.type_check_only
class GoogleAppsCardV1Divider(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleAppsCardV1Grid(typing_extensions.TypedDict, total=False):
    borderStyle: GoogleAppsCardV1BorderStyle
    columnCount: int
    items: _list[GoogleAppsCardV1GridItem]
    onClick: GoogleAppsCardV1OnClick
    title: str

@typing.type_check_only
class GoogleAppsCardV1GridItem(typing_extensions.TypedDict, total=False):
    id: str
    image: GoogleAppsCardV1ImageComponent
    layout: typing_extensions.Literal[
        "GRID_ITEM_LAYOUT_UNSPECIFIED", "TEXT_BELOW", "TEXT_ABOVE"
    ]
    subtitle: str
    title: str

@typing.type_check_only
class GoogleAppsCardV1Icon(typing_extensions.TypedDict, total=False):
    altText: str
    iconUrl: str
    imageType: typing_extensions.Literal["SQUARE", "CIRCLE"]
    knownIcon: str
    materialIcon: GoogleAppsCardV1MaterialIcon

@typing.type_check_only
class GoogleAppsCardV1Image(typing_extensions.TypedDict, total=False):
    altText: str
    imageUrl: str
    onClick: GoogleAppsCardV1OnClick

@typing.type_check_only
class GoogleAppsCardV1ImageComponent(typing_extensions.TypedDict, total=False):
    altText: str
    borderStyle: GoogleAppsCardV1BorderStyle
    cropStyle: GoogleAppsCardV1ImageCropStyle
    imageUri: str

@typing.type_check_only
class GoogleAppsCardV1ImageCropStyle(typing_extensions.TypedDict, total=False):
    aspectRatio: float
    type: typing_extensions.Literal[
        "IMAGE_CROP_TYPE_UNSPECIFIED",
        "SQUARE",
        "CIRCLE",
        "RECTANGLE_CUSTOM",
        "RECTANGLE_4_3",
    ]

@typing.type_check_only
class GoogleAppsCardV1MaterialIcon(typing_extensions.TypedDict, total=False):
    fill: bool
    grade: int
    name: str
    weight: int

@typing.type_check_only
class GoogleAppsCardV1NestedWidget(typing_extensions.TypedDict, total=False):
    buttonList: GoogleAppsCardV1ButtonList
    image: GoogleAppsCardV1Image
    textParagraph: GoogleAppsCardV1TextParagraph

@typing.type_check_only
class GoogleAppsCardV1OnClick(typing_extensions.TypedDict, total=False):
    action: GoogleAppsCardV1Action
    card: GoogleAppsCardV1Card
    openDynamicLinkAction: GoogleAppsCardV1Action
    openLink: GoogleAppsCardV1OpenLink
    overflowMenu: GoogleAppsCardV1OverflowMenu

@typing.type_check_only
class GoogleAppsCardV1OpenLink(typing_extensions.TypedDict, total=False):
    onClose: typing_extensions.Literal["NOTHING", "RELOAD"]
    openAs: typing_extensions.Literal["FULL_SIZE", "OVERLAY"]
    url: str

@typing.type_check_only
class GoogleAppsCardV1OverflowMenu(typing_extensions.TypedDict, total=False):
    items: _list[GoogleAppsCardV1OverflowMenuItem]

@typing.type_check_only
class GoogleAppsCardV1OverflowMenuItem(typing_extensions.TypedDict, total=False):
    disabled: bool
    onClick: GoogleAppsCardV1OnClick
    startIcon: GoogleAppsCardV1Icon
    text: str

@typing.type_check_only
class GoogleAppsCardV1PlatformDataSource(typing_extensions.TypedDict, total=False):
    commonDataSource: typing_extensions.Literal["UNKNOWN", "USER"]
    hostAppDataSource: HostAppDataSourceMarkup

@typing.type_check_only
class GoogleAppsCardV1Section(typing_extensions.TypedDict, total=False):
    collapseControl: GoogleAppsCardV1CollapseControl
    collapsible: bool
    header: str
    uncollapsibleWidgetsCount: int
    widgets: _list[GoogleAppsCardV1Widget]

@typing.type_check_only
class GoogleAppsCardV1SelectionInput(typing_extensions.TypedDict, total=False):
    externalDataSource: GoogleAppsCardV1Action
    items: _list[GoogleAppsCardV1SelectionItem]
    label: str
    multiSelectMaxSelectedItems: int
    multiSelectMinQueryLength: int
    name: str
    onChangeAction: GoogleAppsCardV1Action
    platformDataSource: GoogleAppsCardV1PlatformDataSource
    type: typing_extensions.Literal[
        "CHECK_BOX", "RADIO_BUTTON", "SWITCH", "DROPDOWN", "MULTI_SELECT"
    ]

@typing.type_check_only
class GoogleAppsCardV1SelectionItem(typing_extensions.TypedDict, total=False):
    bottomText: str
    selected: bool
    startIconUri: str
    text: str
    value: str

@typing.type_check_only
class GoogleAppsCardV1SuggestionItem(typing_extensions.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleAppsCardV1Suggestions(typing_extensions.TypedDict, total=False):
    items: _list[GoogleAppsCardV1SuggestionItem]

@typing.type_check_only
class GoogleAppsCardV1SwitchControl(typing_extensions.TypedDict, total=False):
    controlType: typing_extensions.Literal["SWITCH", "CHECKBOX", "CHECK_BOX"]
    name: str
    onChangeAction: GoogleAppsCardV1Action
    selected: bool
    value: str

@typing.type_check_only
class GoogleAppsCardV1TextInput(typing_extensions.TypedDict, total=False):
    autoCompleteAction: GoogleAppsCardV1Action
    hintText: str
    initialSuggestions: GoogleAppsCardV1Suggestions
    label: str
    name: str
    onChangeAction: GoogleAppsCardV1Action
    placeholderText: str
    type: typing_extensions.Literal["SINGLE_LINE", "MULTIPLE_LINE"]
    validation: GoogleAppsCardV1Validation
    value: str

@typing.type_check_only
class GoogleAppsCardV1TextParagraph(typing_extensions.TypedDict, total=False):
    maxLines: int
    text: str

@typing.type_check_only
class GoogleAppsCardV1Validation(typing_extensions.TypedDict, total=False):
    characterLimit: int
    inputType: typing_extensions.Literal[
        "INPUT_TYPE_UNSPECIFIED", "TEXT", "INTEGER", "FLOAT", "EMAIL", "EMOJI_PICKER"
    ]

@typing.type_check_only
class GoogleAppsCardV1Widget(typing_extensions.TypedDict, total=False):
    buttonList: GoogleAppsCardV1ButtonList
    carousel: GoogleAppsCardV1Carousel
    chipList: GoogleAppsCardV1ChipList
    columns: GoogleAppsCardV1Columns
    dateTimePicker: GoogleAppsCardV1DateTimePicker
    decoratedText: GoogleAppsCardV1DecoratedText
    divider: GoogleAppsCardV1Divider
    grid: GoogleAppsCardV1Grid
    horizontalAlignment: typing_extensions.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END"
    ]
    image: GoogleAppsCardV1Image
    selectionInput: GoogleAppsCardV1SelectionInput
    textInput: GoogleAppsCardV1TextInput
    textParagraph: GoogleAppsCardV1TextParagraph

@typing.type_check_only
class GoogleAppsCardV1Widgets(typing_extensions.TypedDict, total=False):
    buttonList: GoogleAppsCardV1ButtonList
    chipList: GoogleAppsCardV1ChipList
    dateTimePicker: GoogleAppsCardV1DateTimePicker
    decoratedText: GoogleAppsCardV1DecoratedText
    image: GoogleAppsCardV1Image
    selectionInput: GoogleAppsCardV1SelectionInput
    textInput: GoogleAppsCardV1TextInput
    textParagraph: GoogleAppsCardV1TextParagraph

@typing.type_check_only
class Group(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class HostAppDataSourceMarkup(typing_extensions.TypedDict, total=False):
    chatDataSource: ChatClientDataSourceMarkup

@typing.type_check_only
class Image(typing_extensions.TypedDict, total=False):
    aspectRatio: float
    imageUrl: str
    onClick: OnClick

@typing.type_check_only
class ImageButton(typing_extensions.TypedDict, total=False):
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
    onClick: OnClick

@typing.type_check_only
class Inputs(typing_extensions.TypedDict, total=False):
    dateInput: DateInput
    dateTimeInput: DateTimeInput
    stringInputs: StringInputs
    timeInput: TimeInput

@typing.type_check_only
class KeyValue(typing_extensions.TypedDict, total=False):
    bottomLabel: str
    button: Button
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
    onClick: OnClick
    topLabel: str

@typing.type_check_only
class ListMembershipsResponse(typing_extensions.TypedDict, total=False):
    memberships: _list[Membership]
    nextPageToken: str

@typing.type_check_only
class ListMessagesResponse(typing_extensions.TypedDict, total=False):
    messages: _list[Message]
    nextPageToken: str

@typing.type_check_only
class ListReactionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    reactions: _list[Reaction]

@typing.type_check_only
class ListSpaceEventsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    spaceEvents: _list[SpaceEvent]

@typing.type_check_only
class ListSpacesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    spaces: _list[Space]

@typing.type_check_only
class MatchedUrl(typing_extensions.TypedDict, total=False):
    url: str

@typing.type_check_only
class Media(typing_extensions.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class Membership(typing_extensions.TypedDict, total=False):
    createTime: str
    deleteTime: str
    groupMember: Group
    member: User
    name: str
    role: typing_extensions.Literal[
        "MEMBERSHIP_ROLE_UNSPECIFIED", "ROLE_MEMBER", "ROLE_MANAGER"
    ]
    state: typing_extensions.Literal[
        "MEMBERSHIP_STATE_UNSPECIFIED", "JOINED", "INVITED", "NOT_A_MEMBER"
    ]

@typing.type_check_only
class MembershipBatchCreatedEventData(typing_extensions.TypedDict, total=False):
    memberships: _list[MembershipCreatedEventData]

@typing.type_check_only
class MembershipBatchDeletedEventData(typing_extensions.TypedDict, total=False):
    memberships: _list[MembershipDeletedEventData]

@typing.type_check_only
class MembershipBatchUpdatedEventData(typing_extensions.TypedDict, total=False):
    memberships: _list[MembershipUpdatedEventData]

@typing.type_check_only
class MembershipCount(typing_extensions.TypedDict, total=False):
    joinedDirectHumanUserCount: int
    joinedGroupCount: int

@typing.type_check_only
class MembershipCreatedEventData(typing_extensions.TypedDict, total=False):
    membership: Membership

@typing.type_check_only
class MembershipDeletedEventData(typing_extensions.TypedDict, total=False):
    membership: Membership

@typing.type_check_only
class MembershipUpdatedEventData(typing_extensions.TypedDict, total=False):
    membership: Membership

@typing.type_check_only
class Message(typing_extensions.TypedDict, total=False):
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
    matchedUrl: MatchedUrl
    name: str
    privateMessageViewer: User
    quotedMessageMetadata: QuotedMessageMetadata
    sender: User
    slashCommand: SlashCommand
    space: Space
    text: str
    thread: Thread
    threadReply: bool

@typing.type_check_only
class MessageBatchCreatedEventData(typing_extensions.TypedDict, total=False):
    messages: _list[MessageCreatedEventData]

@typing.type_check_only
class MessageBatchDeletedEventData(typing_extensions.TypedDict, total=False):
    messages: _list[MessageDeletedEventData]

@typing.type_check_only
class MessageBatchUpdatedEventData(typing_extensions.TypedDict, total=False):
    messages: _list[MessageUpdatedEventData]

@typing.type_check_only
class MessageCreatedEventData(typing_extensions.TypedDict, total=False):
    message: Message

@typing.type_check_only
class MessageDeletedEventData(typing_extensions.TypedDict, total=False):
    message: Message

@typing.type_check_only
class MessageUpdatedEventData(typing_extensions.TypedDict, total=False):
    message: Message

@typing.type_check_only
class OnClick(typing_extensions.TypedDict, total=False):
    action: FormAction
    openLink: OpenLink

@typing.type_check_only
class OpenLink(typing_extensions.TypedDict, total=False):
    url: str

@typing.type_check_only
class PermissionSetting(typing_extensions.TypedDict, total=False):
    managersAllowed: bool
    membersAllowed: bool

@typing.type_check_only
class PermissionSettings(typing_extensions.TypedDict, total=False):
    manageApps: PermissionSetting
    manageMembersAndGroups: PermissionSetting
    manageWebhooks: PermissionSetting
    modifySpaceDetails: PermissionSetting
    postMessages: PermissionSetting
    replyMessages: PermissionSetting
    toggleHistory: PermissionSetting
    useAtMentionAll: PermissionSetting

@typing.type_check_only
class QuotedMessageMetadata(typing_extensions.TypedDict, total=False):
    lastUpdateTime: str
    name: str

@typing.type_check_only
class Reaction(typing_extensions.TypedDict, total=False):
    emoji: Emoji
    name: str
    user: User

@typing.type_check_only
class ReactionBatchCreatedEventData(typing_extensions.TypedDict, total=False):
    reactions: _list[ReactionCreatedEventData]

@typing.type_check_only
class ReactionBatchDeletedEventData(typing_extensions.TypedDict, total=False):
    reactions: _list[ReactionDeletedEventData]

@typing.type_check_only
class ReactionCreatedEventData(typing_extensions.TypedDict, total=False):
    reaction: Reaction

@typing.type_check_only
class ReactionDeletedEventData(typing_extensions.TypedDict, total=False):
    reaction: Reaction

@typing.type_check_only
class RichLinkMetadata(typing_extensions.TypedDict, total=False):
    chatSpaceLinkData: ChatSpaceLinkData
    driveLinkData: DriveLinkData
    richLinkType: typing_extensions.Literal[
        "RICH_LINK_TYPE_UNSPECIFIED", "DRIVE_FILE", "CHAT_SPACE"
    ]
    uri: str

@typing.type_check_only
class SearchSpacesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    spaces: _list[Space]
    totalSize: int

@typing.type_check_only
class Section(typing_extensions.TypedDict, total=False):
    header: str
    widgets: _list[WidgetMarkup]

@typing.type_check_only
class SelectionItems(typing_extensions.TypedDict, total=False):
    items: _list[GoogleAppsCardV1SelectionItem]

@typing.type_check_only
class SetUpSpaceRequest(typing_extensions.TypedDict, total=False):
    memberships: _list[Membership]
    requestId: str
    space: Space

@typing.type_check_only
class SlashCommand(typing_extensions.TypedDict, total=False):
    commandId: str

@typing.type_check_only
class SlashCommandMetadata(typing_extensions.TypedDict, total=False):
    bot: User
    commandId: str
    commandName: str
    triggersDialog: bool
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "ADD", "INVOKE"]

@typing.type_check_only
class Space(typing_extensions.TypedDict, total=False):
    accessSettings: AccessSettings
    adminInstalled: bool
    createTime: str
    displayName: str
    externalUserAllowed: bool
    importMode: bool
    importModeExpireTime: str
    lastActiveTime: str
    membershipCount: MembershipCount
    name: str
    permissionSettings: PermissionSettings
    predefinedPermissionSettings: typing_extensions.Literal[
        "PREDEFINED_PERMISSION_SETTINGS_UNSPECIFIED",
        "COLLABORATION_SPACE",
        "ANNOUNCEMENT_SPACE",
    ]
    singleUserBotDm: bool
    spaceDetails: SpaceDetails
    spaceHistoryState: typing_extensions.Literal[
        "HISTORY_STATE_UNSPECIFIED", "HISTORY_OFF", "HISTORY_ON"
    ]
    spaceThreadingState: typing_extensions.Literal[
        "SPACE_THREADING_STATE_UNSPECIFIED",
        "THREADED_MESSAGES",
        "GROUPED_MESSAGES",
        "UNTHREADED_MESSAGES",
    ]
    spaceType: typing_extensions.Literal[
        "SPACE_TYPE_UNSPECIFIED", "SPACE", "GROUP_CHAT", "DIRECT_MESSAGE"
    ]
    spaceUri: str
    threaded: bool
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "ROOM", "DM"]

@typing.type_check_only
class SpaceBatchUpdatedEventData(typing_extensions.TypedDict, total=False):
    spaces: _list[SpaceUpdatedEventData]

@typing.type_check_only
class SpaceDataSource(typing_extensions.TypedDict, total=False):
    defaultToCurrentSpace: bool

@typing.type_check_only
class SpaceDetails(typing_extensions.TypedDict, total=False):
    description: str
    guidelines: str

@typing.type_check_only
class SpaceEvent(typing_extensions.TypedDict, total=False):
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
class SpaceReadState(typing_extensions.TypedDict, total=False):
    lastReadTime: str
    name: str

@typing.type_check_only
class SpaceUpdatedEventData(typing_extensions.TypedDict, total=False):
    space: Space

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StringInputs(typing_extensions.TypedDict, total=False):
    value: _list[str]

@typing.type_check_only
class TextButton(typing_extensions.TypedDict, total=False):
    onClick: OnClick
    text: str

@typing.type_check_only
class TextParagraph(typing_extensions.TypedDict, total=False):
    text: str

@typing.type_check_only
class Thread(typing_extensions.TypedDict, total=False):
    name: str
    threadKey: str

@typing.type_check_only
class ThreadReadState(typing_extensions.TypedDict, total=False):
    lastReadTime: str
    name: str

@typing.type_check_only
class TimeInput(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int

@typing.type_check_only
class TimeZone(typing_extensions.TypedDict, total=False):
    id: str
    offset: int

@typing.type_check_only
class UpdatedWidget(typing_extensions.TypedDict, total=False):
    suggestions: SelectionItems
    widget: str

@typing.type_check_only
class UploadAttachmentRequest(typing_extensions.TypedDict, total=False):
    filename: str

@typing.type_check_only
class UploadAttachmentResponse(typing_extensions.TypedDict, total=False):
    attachmentDataRef: AttachmentDataRef

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    displayName: str
    domainId: str
    isAnonymous: bool
    name: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "HUMAN", "BOT"]

@typing.type_check_only
class UserMentionMetadata(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "ADD", "MENTION"]
    user: User

@typing.type_check_only
class WidgetMarkup(typing_extensions.TypedDict, total=False):
    buttons: _list[Button]
    image: Image
    keyValue: KeyValue
    textParagraph: TextParagraph

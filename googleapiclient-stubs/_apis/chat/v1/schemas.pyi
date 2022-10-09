import typing

import typing_extensions

_list = list

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
    ]
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
    slashCommand: SlashCommandMetadata
    startIndex: int
    type: typing_extensions.Literal[
        "ANNOTATION_TYPE_UNSPECIFIED", "USER_MENTION", "SLASH_COMMAND"
    ]
    userMention: UserMentionMetadata

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
class DateInput(typing_extensions.TypedDict, total=False):
    msSinceEpoch: str

@typing.type_check_only
class DateTimeInput(typing_extensions.TypedDict, total=False):
    hasDate: bool
    hasTime: bool
    msSinceEpoch: str

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
        "UNSPECIFIED", "MESSAGE", "ADDED_TO_SPACE", "REMOVED_FROM_SPACE", "CARD_CLICKED"
    ]
    user: User

@typing.type_check_only
class Dialog(typing_extensions.TypedDict, total=False):
    body: GoogleAppsCardV1Card

@typing.type_check_only
class DialogAction(dict[str, typing.Any]): ...

@typing.type_check_only
class DriveDataRef(typing_extensions.TypedDict, total=False):
    driveFileId: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FormAction(typing_extensions.TypedDict, total=False):
    actionMethodName: str
    parameters: _list[ActionParameter]

@typing.type_check_only
class GoogleAppsCardV1Action(typing_extensions.TypedDict, total=False):
    function: str
    loadIndicator: typing_extensions.Literal["SPINNER", "NONE"]
    parameters: _list[GoogleAppsCardV1ActionParameter]
    persistValues: bool

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

@typing.type_check_only
class GoogleAppsCardV1ButtonList(typing_extensions.TypedDict, total=False):
    buttons: _list[GoogleAppsCardV1Button]

@typing.type_check_only
class GoogleAppsCardV1Card(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleAppsCardV1CardAction(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleAppsCardV1CardFixedFooter(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleAppsCardV1CardHeader(typing_extensions.TypedDict, total=False):
    imageAltText: str
    imageType: typing_extensions.Literal["SQUARE", "CIRCLE"]
    imageUrl: str
    subtitle: str
    title: str

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
    textAlignment: typing_extensions.Literal[
        "HORIZONTAL_ALIGNMENT_UNSPECIFIED", "START", "CENTER", "END"
    ]
    title: str

@typing.type_check_only
class GoogleAppsCardV1Icon(typing_extensions.TypedDict, total=False):
    altText: str
    iconUrl: str
    imageType: typing_extensions.Literal["SQUARE", "CIRCLE"]
    knownIcon: str

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
class GoogleAppsCardV1OnClick(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleAppsCardV1OpenLink(typing_extensions.TypedDict, total=False):
    onClose: typing_extensions.Literal["NOTHING", "RELOAD"]
    openAs: typing_extensions.Literal["FULL_SIZE", "OVERLAY"]
    url: str

@typing.type_check_only
class GoogleAppsCardV1Section(dict[str, typing.Any]): ...

@typing.type_check_only
class GoogleAppsCardV1SelectionInput(typing_extensions.TypedDict, total=False):
    items: _list[GoogleAppsCardV1SelectionItem]
    label: str
    name: str
    onChangeAction: GoogleAppsCardV1Action
    type: typing_extensions.Literal["CHECK_BOX", "RADIO_BUTTON", "SWITCH", "DROPDOWN"]

@typing.type_check_only
class GoogleAppsCardV1SelectionItem(typing_extensions.TypedDict, total=False):
    selected: bool
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
    type: typing_extensions.Literal["SINGLE_LINE", "MULTIPLE_LINE"]
    value: str

@typing.type_check_only
class GoogleAppsCardV1TextParagraph(typing_extensions.TypedDict, total=False):
    text: str

@typing.type_check_only
class GoogleAppsCardV1Widget(dict[str, typing.Any]): ...

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
    member: User
    name: str
    role: typing_extensions.Literal[
        "MEMBERSHIP_ROLE_UNSPECIFIED", "ROLE_MEMBER", "ROLE_MANAGER"
    ]
    state: typing_extensions.Literal[
        "MEMBERSHIP_STATE_UNSPECIFIED", "JOINED", "INVITED", "NOT_A_MEMBER"
    ]

@typing.type_check_only
class Message(dict[str, typing.Any]): ...

@typing.type_check_only
class OnClick(typing_extensions.TypedDict, total=False):
    action: FormAction
    openLink: OpenLink

@typing.type_check_only
class OpenLink(typing_extensions.TypedDict, total=False):
    url: str

@typing.type_check_only
class Section(typing_extensions.TypedDict, total=False):
    header: str
    widgets: _list[WidgetMarkup]

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
    displayName: str
    name: str
    singleUserBotDm: bool
    spaceDetails: SpaceDetails
    threaded: bool
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "ROOM", "DM"]

@typing.type_check_only
class SpaceDetails(typing_extensions.TypedDict, total=False):
    description: str
    guidelines: str

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

@typing.type_check_only
class TimeInput(typing_extensions.TypedDict, total=False):
    hours: int
    minutes: int

@typing.type_check_only
class TimeZone(typing_extensions.TypedDict, total=False):
    id: str
    offset: int

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

import typing

import typing_extensions

class OnClick(typing_extensions.TypedDict, total=False):
    action: FormAction
    openLink: OpenLink

class CardHeader(typing_extensions.TypedDict, total=False):
    subtitle: str
    title: str
    imageStyle: typing_extensions.Literal["IMAGE_STYLE_UNSPECIFIED", "IMAGE", "AVATAR"]
    imageUrl: str

class UserMentionMetadata(typing_extensions.TypedDict, total=False):
    user: User
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "ADD", "MENTION"]

class Image(typing_extensions.TypedDict, total=False):
    aspectRatio: float
    imageUrl: str
    onClick: OnClick

class Button(typing_extensions.TypedDict, total=False):
    textButton: TextButton
    imageButton: ImageButton

class AttachmentDataRef(typing_extensions.TypedDict, total=False):
    resourceName: str

class TextButton(typing_extensions.TypedDict, total=False):
    onClick: OnClick
    text: str

class WidgetMarkup(typing_extensions.TypedDict, total=False):
    keyValue: KeyValue
    textParagraph: TextParagraph
    image: Image
    buttons: typing.List[Button]

class Card(typing_extensions.TypedDict, total=False):
    header: CardHeader
    name: str
    cardActions: typing.List[CardAction]
    sections: typing.List[Section]

class TextParagraph(typing_extensions.TypedDict, total=False):
    text: str

class ImageButton(typing_extensions.TypedDict, total=False):
    iconUrl: str
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
    name: str
    onClick: OnClick

class ListSpacesResponse(typing_extensions.TypedDict, total=False):
    spaces: typing.List[Space]
    nextPageToken: str

class Section(typing_extensions.TypedDict, total=False):
    widgets: typing.List[WidgetMarkup]
    header: str

class Message(typing_extensions.TypedDict, total=False):
    createTime: str
    attachment: typing.List[Attachment]
    cards: typing.List[Card]
    fallbackText: str
    previewText: str
    thread: Thread
    annotations: typing.List[Annotation]
    argumentText: str
    space: Space
    sender: User
    text: str
    name: str
    slashCommand: SlashCommand
    actionResponse: ActionResponse

class SlashCommandMetadata(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "ADD", "INVOKE"]
    triggersDialog: bool
    commandName: str
    bot: User
    commandId: str

class Space(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "ROOM", "DM"]
    singleUserBotDm: bool
    name: str
    displayName: str
    threaded: bool

class ActionResponse(typing_extensions.TypedDict, total=False):
    url: str
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "NEW_MESSAGE", "UPDATE_MESSAGE", "REQUEST_CONFIG"
    ]

class FormAction(typing_extensions.TypedDict, total=False):
    actionMethodName: str
    parameters: typing.List[ActionParameter]

class ListMembershipsResponse(typing_extensions.TypedDict, total=False):
    memberships: typing.List[Membership]
    nextPageToken: str

class KeyValue(typing_extensions.TypedDict, total=False):
    content: str
    onClick: OnClick
    bottomLabel: str
    contentMultiline: bool
    topLabel: str
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
    button: Button
    iconUrl: str

class Membership(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    state: typing_extensions.Literal[
        "MEMBERSHIP_STATE_UNSPECIFIED", "JOINED", "INVITED", "NOT_A_MEMBER"
    ]
    member: User

class User(typing_extensions.TypedDict, total=False):
    domainId: str
    displayName: str
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "HUMAN", "BOT"]
    name: str

class Thread(typing_extensions.TypedDict, total=False):
    name: str

class CardAction(typing_extensions.TypedDict, total=False):
    onClick: OnClick
    actionLabel: str

class DriveDataRef(typing_extensions.TypedDict, total=False):
    driveFileId: str

class DeprecatedEvent(typing_extensions.TypedDict, total=False):
    token: str
    threadKey: str
    user: User
    eventTime: str
    configCompleteRedirectUrl: str
    message: Message
    space: Space
    type: typing_extensions.Literal[
        "UNSPECIFIED", "MESSAGE", "ADDED_TO_SPACE", "REMOVED_FROM_SPACE", "CARD_CLICKED"
    ]
    action: FormAction

class Attachment(typing_extensions.TypedDict, total=False):
    attachmentDataRef: AttachmentDataRef
    driveDataRef: DriveDataRef
    contentType: str
    downloadUri: str
    contentName: str
    name: str
    thumbnailUri: str
    source: typing_extensions.Literal[
        "SOURCE_UNSPECIFIED", "DRIVE_FILE", "UPLOADED_CONTENT"
    ]

class Media(typing_extensions.TypedDict, total=False):
    resourceName: str

class Empty(typing_extensions.TypedDict, total=False): ...

class SlashCommand(typing_extensions.TypedDict, total=False):
    commandId: str

class ActionParameter(typing_extensions.TypedDict, total=False):
    key: str
    value: str

class OpenLink(typing_extensions.TypedDict, total=False):
    url: str

class Annotation(typing_extensions.TypedDict, total=False):
    length: int
    type: typing_extensions.Literal[
        "ANNOTATION_TYPE_UNSPECIFIED", "USER_MENTION", "SLASH_COMMAND"
    ]
    startIndex: int
    userMention: UserMentionMetadata
    slashCommand: SlashCommandMetadata

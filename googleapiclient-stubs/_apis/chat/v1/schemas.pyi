import typing

import typing_extensions
@typing.type_check_only
class ActionParameter(typing_extensions.TypedDict, total=False):
    key: str
    value: str

@typing.type_check_only
class ActionResponse(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "NEW_MESSAGE", "UPDATE_MESSAGE", "REQUEST_CONFIG"
    ]
    url: str

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
    cardActions: typing.List[CardAction]
    header: CardHeader
    name: str
    sections: typing.List[Section]

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
class DeprecatedEvent(typing_extensions.TypedDict, total=False):
    action: FormAction
    configCompleteRedirectUrl: str
    eventTime: str
    message: Message
    space: Space
    threadKey: str
    token: str
    type: typing_extensions.Literal[
        "UNSPECIFIED", "MESSAGE", "ADDED_TO_SPACE", "REMOVED_FROM_SPACE", "CARD_CLICKED"
    ]
    user: User

@typing.type_check_only
class DriveDataRef(typing_extensions.TypedDict, total=False):
    driveFileId: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class FormAction(typing_extensions.TypedDict, total=False):
    actionMethodName: str
    parameters: typing.List[ActionParameter]

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
    memberships: typing.List[Membership]
    nextPageToken: str

@typing.type_check_only
class ListSpacesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    spaces: typing.List[Space]

@typing.type_check_only
class Media(typing_extensions.TypedDict, total=False):
    resourceName: str

@typing.type_check_only
class Membership(typing_extensions.TypedDict, total=False):
    createTime: str
    member: User
    name: str
    state: typing_extensions.Literal[
        "MEMBERSHIP_STATE_UNSPECIFIED", "JOINED", "INVITED", "NOT_A_MEMBER"
    ]

@typing.type_check_only
class Message(typing_extensions.TypedDict, total=False):
    actionResponse: ActionResponse
    annotations: typing.List[Annotation]
    argumentText: str
    attachment: typing.List[Attachment]
    cards: typing.List[Card]
    createTime: str
    fallbackText: str
    name: str
    previewText: str
    sender: User
    slashCommand: SlashCommand
    space: Space
    text: str
    thread: Thread

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
    widgets: typing.List[WidgetMarkup]

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
    threaded: bool
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "ROOM", "DM"]

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
    buttons: typing.List[Button]
    image: Image
    keyValue: KeyValue
    textParagraph: TextParagraph

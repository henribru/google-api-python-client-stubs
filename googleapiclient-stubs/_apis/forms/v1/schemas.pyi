import typing

import typing_extensions

_list = list

@typing.type_check_only
class Answer(typing_extensions.TypedDict, total=False):
    fileUploadAnswers: FileUploadAnswers
    grade: Grade
    questionId: str
    textAnswers: TextAnswers

@typing.type_check_only
class BatchUpdateFormRequest(typing_extensions.TypedDict, total=False):
    includeFormInResponse: bool
    requests: _list[Request]
    writeControl: WriteControl

@typing.type_check_only
class BatchUpdateFormResponse(typing_extensions.TypedDict, total=False):
    form: Form
    replies: _list[Response]
    writeControl: WriteControl

@typing.type_check_only
class ChoiceQuestion(typing_extensions.TypedDict, total=False):
    options: _list[Option]
    shuffle: bool
    type: typing_extensions.Literal[
        "CHOICE_TYPE_UNSPECIFIED", "RADIO", "CHECKBOX", "DROP_DOWN"
    ]

@typing.type_check_only
class CloudPubsubTopic(typing_extensions.TypedDict, total=False):
    topicName: str

@typing.type_check_only
class CorrectAnswer(typing_extensions.TypedDict, total=False):
    value: str

@typing.type_check_only
class CorrectAnswers(typing_extensions.TypedDict, total=False):
    answers: _list[CorrectAnswer]

@typing.type_check_only
class CreateItemRequest(typing_extensions.TypedDict, total=False):
    item: Item
    location: Location

@typing.type_check_only
class CreateItemResponse(typing_extensions.TypedDict, total=False):
    itemId: str
    questionId: _list[str]

@typing.type_check_only
class CreateWatchRequest(typing_extensions.TypedDict, total=False):
    watch: Watch
    watchId: str

@typing.type_check_only
class DateQuestion(typing_extensions.TypedDict, total=False):
    includeTime: bool
    includeYear: bool

@typing.type_check_only
class DeleteItemRequest(typing_extensions.TypedDict, total=False):
    location: Location

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExtraMaterial(typing_extensions.TypedDict, total=False):
    link: TextLink
    video: VideoLink

@typing.type_check_only
class Feedback(typing_extensions.TypedDict, total=False):
    material: _list[ExtraMaterial]
    text: str

@typing.type_check_only
class FileUploadAnswer(typing_extensions.TypedDict, total=False):
    fileId: str
    fileName: str
    mimeType: str

@typing.type_check_only
class FileUploadAnswers(typing_extensions.TypedDict, total=False):
    answers: _list[FileUploadAnswer]

@typing.type_check_only
class FileUploadQuestion(typing_extensions.TypedDict, total=False):
    folderId: str
    maxFileSize: str
    maxFiles: int
    types: _list[str]

@typing.type_check_only
class Form(typing_extensions.TypedDict, total=False):
    formId: str
    info: Info
    items: _list[Item]
    linkedSheetId: str
    responderUri: str
    revisionId: str
    settings: FormSettings

@typing.type_check_only
class FormResponse(typing_extensions.TypedDict, total=False):
    answers: dict[str, typing.Any]
    createTime: str
    formId: str
    lastSubmittedTime: str
    respondentEmail: str
    responseId: str
    totalScore: float

@typing.type_check_only
class FormSettings(typing_extensions.TypedDict, total=False):
    quizSettings: QuizSettings

@typing.type_check_only
class Grade(typing_extensions.TypedDict, total=False):
    correct: bool
    feedback: Feedback
    score: float

@typing.type_check_only
class Grading(typing_extensions.TypedDict, total=False):
    correctAnswers: CorrectAnswers
    generalFeedback: Feedback
    pointValue: int
    whenRight: Feedback
    whenWrong: Feedback

@typing.type_check_only
class Grid(typing_extensions.TypedDict, total=False):
    columns: ChoiceQuestion
    shuffleQuestions: bool

@typing.type_check_only
class Image(typing_extensions.TypedDict, total=False):
    altText: str
    contentUri: str
    properties: MediaProperties
    sourceUri: str

@typing.type_check_only
class ImageItem(typing_extensions.TypedDict, total=False):
    image: Image

@typing.type_check_only
class Info(typing_extensions.TypedDict, total=False):
    description: str
    documentTitle: str
    title: str

@typing.type_check_only
class Item(typing_extensions.TypedDict, total=False):
    description: str
    imageItem: ImageItem
    itemId: str
    pageBreakItem: PageBreakItem
    questionGroupItem: QuestionGroupItem
    questionItem: QuestionItem
    textItem: TextItem
    title: str
    videoItem: VideoItem

@typing.type_check_only
class ListFormResponsesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    responses: _list[FormResponse]

@typing.type_check_only
class ListWatchesResponse(typing_extensions.TypedDict, total=False):
    watches: _list[Watch]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    index: int

@typing.type_check_only
class MediaProperties(typing_extensions.TypedDict, total=False):
    alignment: typing_extensions.Literal[
        "ALIGNMENT_UNSPECIFIED", "LEFT", "RIGHT", "CENTER"
    ]
    width: int

@typing.type_check_only
class MoveItemRequest(typing_extensions.TypedDict, total=False):
    newLocation: Location
    originalLocation: Location

@typing.type_check_only
class Option(typing_extensions.TypedDict, total=False):
    goToAction: typing_extensions.Literal[
        "GO_TO_ACTION_UNSPECIFIED", "NEXT_SECTION", "RESTART_FORM", "SUBMIT_FORM"
    ]
    goToSectionId: str
    image: Image
    isOther: bool
    value: str

@typing.type_check_only
class PageBreakItem(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Question(typing_extensions.TypedDict, total=False):
    choiceQuestion: ChoiceQuestion
    dateQuestion: DateQuestion
    fileUploadQuestion: FileUploadQuestion
    grading: Grading
    questionId: str
    required: bool
    rowQuestion: RowQuestion
    scaleQuestion: ScaleQuestion
    textQuestion: TextQuestion
    timeQuestion: TimeQuestion

@typing.type_check_only
class QuestionGroupItem(typing_extensions.TypedDict, total=False):
    grid: Grid
    image: Image
    questions: _list[Question]

@typing.type_check_only
class QuestionItem(typing_extensions.TypedDict, total=False):
    image: Image
    question: Question

@typing.type_check_only
class QuizSettings(typing_extensions.TypedDict, total=False):
    isQuiz: bool

@typing.type_check_only
class RenewWatchRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Request(typing_extensions.TypedDict, total=False):
    createItem: CreateItemRequest
    deleteItem: DeleteItemRequest
    moveItem: MoveItemRequest
    updateFormInfo: UpdateFormInfoRequest
    updateItem: UpdateItemRequest
    updateSettings: UpdateSettingsRequest

@typing.type_check_only
class Response(typing_extensions.TypedDict, total=False):
    createItem: CreateItemResponse

@typing.type_check_only
class RowQuestion(typing_extensions.TypedDict, total=False):
    title: str

@typing.type_check_only
class ScaleQuestion(typing_extensions.TypedDict, total=False):
    high: int
    highLabel: str
    low: int
    lowLabel: str

@typing.type_check_only
class TextAnswer(typing_extensions.TypedDict, total=False):
    value: str

@typing.type_check_only
class TextAnswers(typing_extensions.TypedDict, total=False):
    answers: _list[TextAnswer]

@typing.type_check_only
class TextItem(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class TextLink(typing_extensions.TypedDict, total=False):
    displayText: str
    uri: str

@typing.type_check_only
class TextQuestion(typing_extensions.TypedDict, total=False):
    paragraph: bool

@typing.type_check_only
class TimeQuestion(typing_extensions.TypedDict, total=False):
    duration: bool

@typing.type_check_only
class UpdateFormInfoRequest(typing_extensions.TypedDict, total=False):
    info: Info
    updateMask: str

@typing.type_check_only
class UpdateItemRequest(typing_extensions.TypedDict, total=False):
    item: Item
    location: Location
    updateMask: str

@typing.type_check_only
class UpdateSettingsRequest(typing_extensions.TypedDict, total=False):
    settings: FormSettings
    updateMask: str

@typing.type_check_only
class Video(typing_extensions.TypedDict, total=False):
    properties: MediaProperties
    youtubeUri: str

@typing.type_check_only
class VideoItem(typing_extensions.TypedDict, total=False):
    caption: str
    video: Video

@typing.type_check_only
class VideoLink(typing_extensions.TypedDict, total=False):
    displayText: str
    youtubeUri: str

@typing.type_check_only
class Watch(typing_extensions.TypedDict, total=False):
    createTime: str
    errorType: typing_extensions.Literal[
        "ERROR_TYPE_UNSPECIFIED",
        "PROJECT_NOT_AUTHORIZED",
        "NO_USER_ACCESS",
        "OTHER_ERRORS",
    ]
    eventType: typing_extensions.Literal[
        "EVENT_TYPE_UNSPECIFIED", "SCHEMA", "RESPONSES"
    ]
    expireTime: str
    id: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "ACTIVE", "SUSPENDED"]
    target: WatchTarget

@typing.type_check_only
class WatchTarget(typing_extensions.TypedDict, total=False):
    topic: CloudPubsubTopic

@typing.type_check_only
class WriteControl(typing_extensions.TypedDict, total=False):
    requiredRevisionId: str
    targetRevisionId: str

import typing

_list = list

@typing.type_check_only
class Answer(typing.TypedDict, total=False):
    author: Author
    createTime: str
    name: str
    text: str
    updateTime: str
    upvoteCount: int

@typing.type_check_only
class Author(typing.TypedDict, total=False):
    displayName: str
    profilePhotoUri: str
    type: typing.Literal[
        "AUTHOR_TYPE_UNSPECIFIED", "REGULAR_USER", "LOCAL_GUIDE", "MERCHANT"
    ]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class ListAnswersResponse(typing.TypedDict, total=False):
    answers: _list[Answer]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListQuestionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    questions: _list[Question]
    totalSize: int

@typing.type_check_only
class Question(typing.TypedDict, total=False):
    author: Author
    createTime: str
    name: str
    text: str
    topAnswers: _list[Answer]
    totalAnswerCount: int
    updateTime: str
    upvoteCount: int

@typing.type_check_only
class UpsertAnswerRequest(typing.TypedDict, total=False):
    answer: Answer

import typing

import typing_extensions

_list = list

@typing.type_check_only
class Answer(typing_extensions.TypedDict, total=False):
    author: Author
    createTime: str
    name: str
    text: str
    updateTime: str
    upvoteCount: int

@typing.type_check_only
class Author(typing_extensions.TypedDict, total=False):
    displayName: str
    profilePhotoUri: str
    type: typing_extensions.Literal[
        "AUTHOR_TYPE_UNSPECIFIED", "REGULAR_USER", "LOCAL_GUIDE", "MERCHANT"
    ]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListAnswersResponse(typing_extensions.TypedDict, total=False):
    answers: _list[Answer]
    nextPageToken: str
    totalSize: int

@typing.type_check_only
class ListQuestionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    questions: _list[Question]
    totalSize: int

@typing.type_check_only
class Question(typing_extensions.TypedDict, total=False):
    author: Author
    createTime: str
    name: str
    text: str
    topAnswers: _list[Answer]
    totalAnswerCount: int
    updateTime: str
    upvoteCount: int

@typing.type_check_only
class UpsertAnswerRequest(typing_extensions.TypedDict, total=False):
    answer: Answer

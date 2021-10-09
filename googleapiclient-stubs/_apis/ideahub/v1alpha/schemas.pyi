import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleSearchIdeahubV1alphaAvailableLocale(
    typing_extensions.TypedDict, total=False
):
    locale: str
    name: str

@typing.type_check_only
class GoogleSearchIdeahubV1alphaIdea(typing_extensions.TypedDict, total=False):
    name: str
    text: str
    topics: _list[GoogleSearchIdeahubV1alphaTopic]

@typing.type_check_only
class GoogleSearchIdeahubV1alphaIdeaActivity(typing_extensions.TypedDict, total=False):
    ideas: _list[str]
    name: str
    topics: _list[str]
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED",
        "POST_DRAFTED",
        "POST_PUBLISHED",
        "POST_DELETED",
        "POST_UNPUBLISHED",
    ]
    uri: str

@typing.type_check_only
class GoogleSearchIdeahubV1alphaIdeaState(typing_extensions.TypedDict, total=False):
    dismissed: bool
    name: str
    saved: bool

@typing.type_check_only
class GoogleSearchIdeahubV1alphaListAvailableLocalesResponse(
    typing_extensions.TypedDict, total=False
):
    availableLocales: _list[GoogleSearchIdeahubV1alphaAvailableLocale]
    nextPageToken: str

@typing.type_check_only
class GoogleSearchIdeahubV1alphaListIdeasResponse(
    typing_extensions.TypedDict, total=False
):
    ideas: _list[GoogleSearchIdeahubV1alphaIdea]
    nextPageToken: str

@typing.type_check_only
class GoogleSearchIdeahubV1alphaTopic(typing_extensions.TypedDict, total=False):
    displayName: str
    mid: str
    name: str

@typing.type_check_only
class GoogleSearchIdeahubV1alphaTopicState(typing_extensions.TypedDict, total=False):
    dismissed: bool
    name: str
    saved: bool

import typing

_list = list

@typing.type_check_only
class GoogleSearchIdeahubV1alphaAvailableLocale(typing.TypedDict, total=False):
    locale: str
    name: str

@typing.type_check_only
class GoogleSearchIdeahubV1alphaIdea(typing.TypedDict, total=False):
    name: str
    text: str
    topics: _list[GoogleSearchIdeahubV1alphaTopic]

@typing.type_check_only
class GoogleSearchIdeahubV1alphaIdeaActivity(typing.TypedDict, total=False):
    ideas: _list[str]
    name: str
    topics: _list[str]
    type: typing.Literal[
        "TYPE_UNSPECIFIED",
        "POST_DRAFTED",
        "POST_PUBLISHED",
        "POST_DELETED",
        "POST_UNPUBLISHED",
    ]
    uri: str

@typing.type_check_only
class GoogleSearchIdeahubV1alphaIdeaState(typing.TypedDict, total=False):
    dismissed: bool
    name: str
    saved: bool

@typing.type_check_only
class GoogleSearchIdeahubV1alphaListAvailableLocalesResponse(
    typing.TypedDict, total=False
):
    availableLocales: _list[GoogleSearchIdeahubV1alphaAvailableLocale]
    nextPageToken: str

@typing.type_check_only
class GoogleSearchIdeahubV1alphaListIdeasResponse(typing.TypedDict, total=False):
    ideas: _list[GoogleSearchIdeahubV1alphaIdea]
    nextPageToken: str

@typing.type_check_only
class GoogleSearchIdeahubV1alphaTopic(typing.TypedDict, total=False):
    displayName: str
    mid: str
    name: str

@typing.type_check_only
class GoogleSearchIdeahubV1alphaTopicState(typing.TypedDict, total=False):
    dismissed: bool
    name: str
    saved: bool

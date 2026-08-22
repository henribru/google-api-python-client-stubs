import typing

_list = list

@typing.type_check_only
class GoogleSearchIdeahubV1betaAvailableLocale(typing.TypedDict, total=False):
    locale: str
    name: str

@typing.type_check_only
class GoogleSearchIdeahubV1betaIdea(typing.TypedDict, total=False):
    name: str
    text: str
    topics: _list[GoogleSearchIdeahubV1betaTopic]

@typing.type_check_only
class GoogleSearchIdeahubV1betaIdeaActivity(typing.TypedDict, total=False):
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
class GoogleSearchIdeahubV1betaIdeaState(typing.TypedDict, total=False):
    dismissed: bool
    name: str
    saved: bool

@typing.type_check_only
class GoogleSearchIdeahubV1betaListAvailableLocalesResponse(
    typing.TypedDict, total=False
):
    availableLocales: _list[GoogleSearchIdeahubV1betaAvailableLocale]
    nextPageToken: str

@typing.type_check_only
class GoogleSearchIdeahubV1betaListIdeasResponse(typing.TypedDict, total=False):
    ideas: _list[GoogleSearchIdeahubV1betaIdea]
    nextPageToken: str

@typing.type_check_only
class GoogleSearchIdeahubV1betaTopic(typing.TypedDict, total=False):
    displayName: str
    mid: str
    name: str

@typing.type_check_only
class GoogleSearchIdeahubV1betaTopicState(typing.TypedDict, total=False):
    dismissed: bool
    name: str
    saved: bool

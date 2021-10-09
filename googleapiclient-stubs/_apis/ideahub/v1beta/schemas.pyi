import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleSearchIdeahubV1betaAvailableLocale(
    typing_extensions.TypedDict, total=False
):
    locale: str
    name: str

@typing.type_check_only
class GoogleSearchIdeahubV1betaIdea(typing_extensions.TypedDict, total=False):
    name: str
    text: str
    topics: _list[GoogleSearchIdeahubV1betaTopic]

@typing.type_check_only
class GoogleSearchIdeahubV1betaIdeaActivity(typing_extensions.TypedDict, total=False):
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
class GoogleSearchIdeahubV1betaIdeaState(typing_extensions.TypedDict, total=False):
    dismissed: bool
    name: str
    saved: bool

@typing.type_check_only
class GoogleSearchIdeahubV1betaListAvailableLocalesResponse(
    typing_extensions.TypedDict, total=False
):
    availableLocales: _list[GoogleSearchIdeahubV1betaAvailableLocale]
    nextPageToken: str

@typing.type_check_only
class GoogleSearchIdeahubV1betaListIdeasResponse(
    typing_extensions.TypedDict, total=False
):
    ideas: _list[GoogleSearchIdeahubV1betaIdea]
    nextPageToken: str

@typing.type_check_only
class GoogleSearchIdeahubV1betaTopic(typing_extensions.TypedDict, total=False):
    displayName: str
    mid: str
    name: str

@typing.type_check_only
class GoogleSearchIdeahubV1betaTopicState(typing_extensions.TypedDict, total=False):
    dismissed: bool
    name: str
    saved: bool

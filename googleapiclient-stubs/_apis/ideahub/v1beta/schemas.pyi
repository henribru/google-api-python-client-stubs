import typing

import typing_extensions

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
    topics: typing.List[GoogleSearchIdeahubV1betaTopic]

@typing.type_check_only
class GoogleSearchIdeahubV1betaIdeaActivity(typing_extensions.TypedDict, total=False):
    ideas: typing.List[str]
    name: str
    topics: typing.List[str]
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
    availableLocales: typing.List[GoogleSearchIdeahubV1betaAvailableLocale]
    nextPageToken: str

@typing.type_check_only
class GoogleSearchIdeahubV1betaListIdeasResponse(
    typing_extensions.TypedDict, total=False
):
    ideas: typing.List[GoogleSearchIdeahubV1betaIdea]
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

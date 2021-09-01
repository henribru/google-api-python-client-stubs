import typing

import typing_extensions

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
    topics: typing.List[GoogleSearchIdeahubV1alphaTopic]

@typing.type_check_only
class GoogleSearchIdeahubV1alphaIdeaActivity(typing_extensions.TypedDict, total=False):
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
class GoogleSearchIdeahubV1alphaIdeaState(typing_extensions.TypedDict, total=False):
    dismissed: bool
    name: str
    saved: bool

@typing.type_check_only
class GoogleSearchIdeahubV1alphaListAvailableLocalesResponse(
    typing_extensions.TypedDict, total=False
):
    availableLocales: typing.List[GoogleSearchIdeahubV1alphaAvailableLocale]
    nextPageToken: str

@typing.type_check_only
class GoogleSearchIdeahubV1alphaListIdeasResponse(
    typing_extensions.TypedDict, total=False
):
    ideas: typing.List[GoogleSearchIdeahubV1alphaIdea]
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

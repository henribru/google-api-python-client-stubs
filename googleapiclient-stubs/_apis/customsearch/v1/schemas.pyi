import typing

import typing_extensions

_list = list

@typing.type_check_only
class Promotion(typing_extensions.TypedDict, total=False):
    bodyLines: _list[dict[str, typing.Any]]
    displayLink: str
    htmlTitle: str
    image: dict[str, typing.Any]
    link: str
    title: str

@typing.type_check_only
class Result(typing_extensions.TypedDict, total=False):
    cacheId: str
    displayLink: str
    fileFormat: str
    formattedUrl: str
    htmlFormattedUrl: str
    htmlSnippet: str
    htmlTitle: str
    image: dict[str, typing.Any]
    kind: str
    labels: _list[dict[str, typing.Any]]
    link: str
    mime: str
    pagemap: dict[str, typing.Any]
    snippet: str
    title: str

@typing.type_check_only
class Search(typing_extensions.TypedDict, total=False):
    context: dict[str, typing.Any]
    items: _list[Result]
    kind: str
    promotions: _list[Promotion]
    queries: dict[str, typing.Any]
    searchInformation: dict[str, typing.Any]
    spelling: dict[str, typing.Any]
    url: dict[str, typing.Any]

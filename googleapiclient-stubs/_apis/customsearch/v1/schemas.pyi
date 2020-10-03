import typing

import typing_extensions

class Search(typing_extensions.TypedDict, total=False):
    url: typing.Dict[str, typing.Any]
    searchInformation: typing.Dict[str, typing.Any]
    items: typing.List[Result]
    spelling: typing.Dict[str, typing.Any]
    context: typing.Dict[str, typing.Any]
    promotions: typing.List[Promotion]
    queries: typing.Dict[str, typing.Any]
    kind: str

class Result(typing_extensions.TypedDict, total=False):
    link: str
    image: typing.Dict[str, typing.Any]
    displayLink: str
    cacheId: str
    formattedUrl: str
    htmlFormattedUrl: str
    htmlSnippet: str
    mime: str
    htmlTitle: str
    title: str
    labels: typing.List[typing.Dict[str, typing.Any]]
    kind: str
    fileFormat: str
    pagemap: typing.Dict[str, typing.Any]
    snippet: str

class Promotion(typing_extensions.TypedDict, total=False):
    title: str
    htmlTitle: str
    bodyLines: typing.List[typing.Dict[str, typing.Any]]
    displayLink: str
    image: typing.Dict[str, typing.Any]
    link: str

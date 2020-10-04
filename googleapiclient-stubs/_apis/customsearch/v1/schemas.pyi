import typing

import typing_extensions
@typing.type_check_only
class Promotion(typing_extensions.TypedDict, total=False):
    bodyLines: typing.List[typing.Dict[str, typing.Any]]
    displayLink: str
    htmlTitle: str
    image: typing.Dict[str, typing.Any]
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
    image: typing.Dict[str, typing.Any]
    kind: str
    labels: typing.List[typing.Dict[str, typing.Any]]
    link: str
    mime: str
    pagemap: typing.Dict[str, typing.Any]
    snippet: str
    title: str

@typing.type_check_only
class Search(typing_extensions.TypedDict, total=False):
    context: typing.Dict[str, typing.Any]
    items: typing.List[Result]
    kind: str
    promotions: typing.List[Promotion]
    queries: typing.Dict[str, typing.Any]
    searchInformation: typing.Dict[str, typing.Any]
    spelling: typing.Dict[str, typing.Any]
    url: typing.Dict[str, typing.Any]

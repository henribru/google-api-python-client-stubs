import typing

import typing_extensions

class RdapResponse(typing_extensions.TypedDict, total=False):
    notices: typing.List[Notice]
    title: str
    jsonResponse: HttpBody
    rdapConformance: typing.List[str]
    description: typing.List[str]
    lang: str
    errorCode: int

class Link(typing_extensions.TypedDict, total=False):
    title: str
    type: str
    hreflang: str
    value: str
    rel: str
    href: str
    media: str

class Notice(typing_extensions.TypedDict, total=False):
    type: str
    title: str
    description: typing.List[str]
    links: typing.List[Link]

class HttpBody(typing_extensions.TypedDict, total=False):
    data: str
    extensions: typing.List[typing.Dict[str, typing.Any]]
    contentType: str

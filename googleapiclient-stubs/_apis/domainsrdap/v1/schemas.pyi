import typing

import typing_extensions
@typing.type_check_only
class HttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: typing.List[typing.Dict[str, typing.Any]]

@typing.type_check_only
class Link(typing_extensions.TypedDict, total=False):
    href: str
    hreflang: str
    media: str
    rel: str
    title: str
    type: str
    value: str

@typing.type_check_only
class Notice(typing_extensions.TypedDict, total=False):
    description: typing.List[str]
    links: typing.List[Link]
    title: str
    type: str

@typing.type_check_only
class RdapResponse(typing_extensions.TypedDict, total=False):
    description: typing.List[str]
    errorCode: int
    jsonResponse: HttpBody
    lang: str
    notices: typing.List[Notice]
    rdapConformance: typing.List[str]
    title: str

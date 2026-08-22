import typing

_list = list

@typing.type_check_only
class HttpBody(typing.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class Link(typing.TypedDict, total=False):
    href: str
    hreflang: str
    media: str
    rel: str
    title: str
    type: str
    value: str

@typing.type_check_only
class Notice(typing.TypedDict, total=False):
    description: _list[str]
    links: _list[Link]
    title: str
    type: str

@typing.type_check_only
class RdapResponse(typing.TypedDict, total=False):
    description: _list[str]
    errorCode: int
    jsonResponse: HttpBody
    lang: str
    notices: _list[Notice]
    rdapConformance: _list[str]
    title: str

import typing

import typing_extensions

class GroupItemResource(typing_extensions.TypedDict, total=False):
    id: str
    kind: str

class GroupItem(typing_extensions.TypedDict, total=False):
    etag: str
    resource: GroupItemResource
    id: str
    errors: Errors
    kind: str
    groupId: str

class GroupContentDetails(typing_extensions.TypedDict, total=False):
    itemType: str
    itemCount: str

class ErrorProto(typing_extensions.TypedDict, total=False):
    argument: typing.List[str]
    code: str
    domain: str
    externalErrorMessage: str
    locationType: typing_extensions.Literal["PATH", "OTHER", "PARAMETER"]
    location: str
    debugInfo: str

class ListGroupsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    errors: Errors
    etag: str
    kind: str
    items: typing.List[Group]

class ListGroupItemsResponse(typing_extensions.TypedDict, total=False):
    etag: str
    errors: Errors
    items: typing.List[GroupItem]
    kind: str

class Group(typing_extensions.TypedDict, total=False):
    contentDetails: GroupContentDetails
    etag: str
    errors: Errors
    kind: str
    id: str
    snippet: GroupSnippet

class Errors(typing_extensions.TypedDict, total=False):
    code: typing_extensions.Literal[
        "BAD_REQUEST",
        "FORBIDDEN",
        "NOT_FOUND",
        "CONFLICT",
        "GONE",
        "PRECONDITION_FAILED",
        "INTERNAL_ERROR",
        "SERVICE_UNAVAILABLE",
    ]
    error: typing.List[ErrorProto]
    requestId: str

class EmptyResponse(typing_extensions.TypedDict, total=False):
    errors: Errors

class QueryResponse(typing_extensions.TypedDict, total=False):
    rows: typing.List[list]
    kind: str
    columnHeaders: typing.List[ResultTableColumnHeader]
    errors: Errors

class ResultTableColumnHeader(typing_extensions.TypedDict, total=False):
    dataType: str
    name: str
    columnType: str

class GroupSnippet(typing_extensions.TypedDict, total=False):
    title: str
    publishedAt: str

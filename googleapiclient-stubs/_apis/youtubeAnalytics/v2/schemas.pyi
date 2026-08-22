import typing

_list = list

@typing.type_check_only
class EmptyResponse(typing.TypedDict, total=False):
    errors: Errors

@typing.type_check_only
class ErrorProto(typing.TypedDict, total=False):
    argument: _list[str]
    code: str
    debugInfo: str
    domain: str
    externalErrorMessage: str
    location: str
    locationType: typing.Literal["PATH", "OTHER", "PARAMETER"]

@typing.type_check_only
class Errors(typing.TypedDict, total=False):
    code: typing.Literal[
        "BAD_REQUEST",
        "FORBIDDEN",
        "NOT_FOUND",
        "CONFLICT",
        "GONE",
        "PRECONDITION_FAILED",
        "INTERNAL_ERROR",
        "SERVICE_UNAVAILABLE",
    ]
    error: _list[ErrorProto]
    requestId: str

@typing.type_check_only
class Group(typing.TypedDict, total=False):
    contentDetails: GroupContentDetails
    errors: Errors
    etag: str
    id: str
    kind: str
    snippet: GroupSnippet

@typing.type_check_only
class GroupContentDetails(typing.TypedDict, total=False):
    itemCount: str
    itemType: str

@typing.type_check_only
class GroupItem(typing.TypedDict, total=False):
    errors: Errors
    etag: str
    groupId: str
    id: str
    kind: str
    resource: GroupItemResource

@typing.type_check_only
class GroupItemResource(typing.TypedDict, total=False):
    id: str
    kind: str

@typing.type_check_only
class GroupSnippet(typing.TypedDict, total=False):
    publishedAt: str
    title: str

@typing.type_check_only
class ListGroupItemsResponse(typing.TypedDict, total=False):
    errors: Errors
    etag: str
    items: _list[GroupItem]
    kind: str

@typing.type_check_only
class ListGroupsResponse(typing.TypedDict, total=False):
    errors: Errors
    etag: str
    items: _list[Group]
    kind: str
    nextPageToken: str

@typing.type_check_only
class QueryResponse(typing.TypedDict, total=False):
    columnHeaders: _list[ResultTableColumnHeader]
    errors: Errors
    kind: str
    rows: _list[_list[typing.Any]]

@typing.type_check_only
class ResultTableColumnHeader(typing.TypedDict, total=False):
    columnType: str
    dataType: str
    name: str

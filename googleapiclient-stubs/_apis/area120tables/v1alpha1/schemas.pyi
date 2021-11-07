import typing

import typing_extensions

_list = list

@typing.type_check_only
class BatchCreateRowsRequest(typing_extensions.TypedDict, total=False):
    requests: _list[CreateRowRequest]

@typing.type_check_only
class BatchCreateRowsResponse(typing_extensions.TypedDict, total=False):
    rows: _list[Row]

@typing.type_check_only
class BatchDeleteRowsRequest(typing_extensions.TypedDict, total=False):
    names: _list[str]

@typing.type_check_only
class BatchUpdateRowsRequest(typing_extensions.TypedDict, total=False):
    requests: _list[UpdateRowRequest]

@typing.type_check_only
class BatchUpdateRowsResponse(typing_extensions.TypedDict, total=False):
    rows: _list[Row]

@typing.type_check_only
class ColumnDescription(typing_extensions.TypedDict, total=False):
    dataType: str
    dateDetails: DateDetails
    id: str
    labels: _list[LabeledItem]
    lookupDetails: LookupDetails
    multipleValuesDisallowed: bool
    name: str
    readonly: bool
    relationshipDetails: RelationshipDetails

@typing.type_check_only
class CreateRowRequest(typing_extensions.TypedDict, total=False):
    parent: str
    row: Row
    view: typing_extensions.Literal["VIEW_UNSPECIFIED", "COLUMN_ID_VIEW"]

@typing.type_check_only
class DateDetails(typing_extensions.TypedDict, total=False):
    hasTime: bool

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class LabeledItem(typing_extensions.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class ListRowsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    rows: _list[Row]

@typing.type_check_only
class ListTablesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    tables: _list[Table]

@typing.type_check_only
class ListWorkspacesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    workspaces: _list[Workspace]

@typing.type_check_only
class LookupDetails(typing_extensions.TypedDict, total=False):
    relationshipColumn: str
    relationshipColumnId: str

@typing.type_check_only
class RelationshipDetails(typing_extensions.TypedDict, total=False):
    linkedTable: str

@typing.type_check_only
class Row(typing_extensions.TypedDict, total=False):
    createTime: str
    name: str
    updateTime: str
    values: dict[str, typing.Any]

@typing.type_check_only
class SavedView(typing_extensions.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class Table(typing_extensions.TypedDict, total=False):
    columns: _list[ColumnDescription]
    createTime: str
    displayName: str
    name: str
    savedViews: _list[SavedView]
    timeZone: str
    updateTime: str

@typing.type_check_only
class UpdateRowRequest(typing_extensions.TypedDict, total=False):
    row: Row
    updateMask: str
    view: typing_extensions.Literal["VIEW_UNSPECIFIED", "COLUMN_ID_VIEW"]

@typing.type_check_only
class Workspace(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    name: str
    tables: _list[Table]
    updateTime: str

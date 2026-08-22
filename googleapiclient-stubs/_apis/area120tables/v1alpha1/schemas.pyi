import typing

_list = list

@typing.type_check_only
class BatchCreateRowsRequest(typing.TypedDict, total=False):
    requests: _list[CreateRowRequest]

@typing.type_check_only
class BatchCreateRowsResponse(typing.TypedDict, total=False):
    rows: _list[Row]

@typing.type_check_only
class BatchDeleteRowsRequest(typing.TypedDict, total=False):
    names: _list[str]

@typing.type_check_only
class BatchUpdateRowsRequest(typing.TypedDict, total=False):
    requests: _list[UpdateRowRequest]

@typing.type_check_only
class BatchUpdateRowsResponse(typing.TypedDict, total=False):
    rows: _list[Row]

@typing.type_check_only
class ColumnDescription(typing.TypedDict, total=False):
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
class CreateRowRequest(typing.TypedDict, total=False):
    parent: str
    row: Row
    view: typing.Literal["VIEW_UNSPECIFIED", "COLUMN_ID_VIEW"]

@typing.type_check_only
class DateDetails(typing.TypedDict, total=False):
    hasTime: bool

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class LabeledItem(typing.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class ListRowsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    rows: _list[Row]

@typing.type_check_only
class ListTablesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    tables: _list[Table]

@typing.type_check_only
class ListWorkspacesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    workspaces: _list[Workspace]

@typing.type_check_only
class LookupDetails(typing.TypedDict, total=False):
    relationshipColumn: str
    relationshipColumnId: str

@typing.type_check_only
class RelationshipDetails(typing.TypedDict, total=False):
    linkedTable: str

@typing.type_check_only
class Row(typing.TypedDict, total=False):
    createTime: str
    name: str
    updateTime: str
    values: dict[str, typing.Any]

@typing.type_check_only
class SavedView(typing.TypedDict, total=False):
    id: str
    name: str

@typing.type_check_only
class Table(typing.TypedDict, total=False):
    columns: _list[ColumnDescription]
    createTime: str
    displayName: str
    name: str
    savedViews: _list[SavedView]
    timeZone: str
    updateTime: str

@typing.type_check_only
class UpdateRowRequest(typing.TypedDict, total=False):
    row: Row
    updateMask: str
    view: typing.Literal["VIEW_UNSPECIFIED", "COLUMN_ID_VIEW"]

@typing.type_check_only
class Workspace(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    name: str
    tables: _list[Table]
    updateTime: str

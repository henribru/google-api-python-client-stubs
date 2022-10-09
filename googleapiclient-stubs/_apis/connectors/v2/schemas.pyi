import typing

import typing_extensions

_list = list

@typing.type_check_only
class Action(typing_extensions.TypedDict, total=False):
    inputParameters: _list[InputParameter]
    name: str
    resultMetadata: _list[ResultMetadata]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Entity(typing_extensions.TypedDict, total=False):
    fields: dict[str, typing.Any]
    name: str

@typing.type_check_only
class EntityType(typing_extensions.TypedDict, total=False):
    fields: _list[Field]
    name: str

@typing.type_check_only
class ExecuteActionRequest(typing_extensions.TypedDict, total=False):
    parameters: dict[str, typing.Any]

@typing.type_check_only
class ExecuteActionResponse(typing_extensions.TypedDict, total=False):
    results: _list[dict[str, typing.Any]]

@typing.type_check_only
class ExecuteSqlQueryRequest(typing_extensions.TypedDict, total=False):
    query: Query

@typing.type_check_only
class ExecuteSqlQueryResponse(typing_extensions.TypedDict, total=False):
    results: _list[dict[str, typing.Any]]

@typing.type_check_only
class Field(typing_extensions.TypedDict, total=False):
    additionalDetails: dict[str, typing.Any]
    dataType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "INT",
        "SMALLINT",
        "DOUBLE",
        "DATE",
        "DATETIME",
        "TIME",
        "STRING",
        "LONG",
        "BOOLEAN",
        "DECIMAL",
        "UUID",
        "BLOB",
        "BIT",
        "TINYINT",
        "INTEGER",
        "BIGINT",
        "FLOAT",
        "REAL",
        "NUMERIC",
        "CHAR",
        "VARCHAR",
        "LONGVARCHAR",
        "TIMESTAMP",
        "NCHAR",
        "NVARCHAR",
        "LONGNVARCHAR",
        "NULL",
        "OTHER",
        "JAVA_OBJECT",
        "DISTINCT",
        "STRUCT",
        "ARRAY",
        "CLOB",
        "REF",
        "DATALINK",
        "ROWID",
        "BINARY",
        "VARBINARY",
        "LONGVARBINARY",
        "NCLOB",
        "SQLXML",
        "REF_CURSOR",
        "TIME_WITH_TIMEZONE",
        "TIMESTAMP_WITH_TIMEZONE",
    ]
    defaultValue: typing.Any
    description: str
    key: bool
    name: str
    nullable: bool
    reference: Reference

@typing.type_check_only
class InputParameter(typing_extensions.TypedDict, total=False):
    dataType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "INT",
        "SMALLINT",
        "DOUBLE",
        "DATE",
        "DATETIME",
        "TIME",
        "STRING",
        "LONG",
        "BOOLEAN",
        "DECIMAL",
        "UUID",
        "BLOB",
        "BIT",
        "TINYINT",
        "INTEGER",
        "BIGINT",
        "FLOAT",
        "REAL",
        "NUMERIC",
        "CHAR",
        "VARCHAR",
        "LONGVARCHAR",
        "TIMESTAMP",
        "NCHAR",
        "NVARCHAR",
        "LONGNVARCHAR",
        "NULL",
        "OTHER",
        "JAVA_OBJECT",
        "DISTINCT",
        "STRUCT",
        "ARRAY",
        "CLOB",
        "REF",
        "DATALINK",
        "ROWID",
        "BINARY",
        "VARBINARY",
        "LONGVARBINARY",
        "NCLOB",
        "SQLXML",
        "REF_CURSOR",
        "TIME_WITH_TIMEZONE",
        "TIMESTAMP_WITH_TIMEZONE",
    ]
    defaultValue: typing.Any
    description: str
    name: str
    nullable: bool

@typing.type_check_only
class ListActionsResponse(typing_extensions.TypedDict, total=False):
    actions: _list[Action]
    nextPageToken: str
    unsupportedActionNames: _list[str]

@typing.type_check_only
class ListEntitiesResponse(typing_extensions.TypedDict, total=False):
    entities: _list[Entity]
    nextPageToken: str

@typing.type_check_only
class ListEntityTypesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    types: _list[EntityType]
    unsupportedTypeNames: _list[str]

@typing.type_check_only
class Query(typing_extensions.TypedDict, total=False):
    query: str

@typing.type_check_only
class Reference(typing_extensions.TypedDict, total=False):
    name: str
    type: str

@typing.type_check_only
class ResultMetadata(typing_extensions.TypedDict, total=False):
    dataType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "INT",
        "SMALLINT",
        "DOUBLE",
        "DATE",
        "DATETIME",
        "TIME",
        "STRING",
        "LONG",
        "BOOLEAN",
        "DECIMAL",
        "UUID",
        "BLOB",
        "BIT",
        "TINYINT",
        "INTEGER",
        "BIGINT",
        "FLOAT",
        "REAL",
        "NUMERIC",
        "CHAR",
        "VARCHAR",
        "LONGVARCHAR",
        "TIMESTAMP",
        "NCHAR",
        "NVARCHAR",
        "LONGNVARCHAR",
        "NULL",
        "OTHER",
        "JAVA_OBJECT",
        "DISTINCT",
        "STRUCT",
        "ARRAY",
        "CLOB",
        "REF",
        "DATALINK",
        "ROWID",
        "BINARY",
        "VARBINARY",
        "LONGVARBINARY",
        "NCLOB",
        "SQLXML",
        "REF_CURSOR",
        "TIME_WITH_TIMEZONE",
        "TIMESTAMP_WITH_TIMEZONE",
    ]
    description: str
    name: str

@typing.type_check_only
class UpdateEntitiesWithConditionsResponse(typing_extensions.TypedDict, total=False):
    response: dict[str, typing.Any]

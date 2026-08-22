import typing

_list = list

@typing.type_check_only
class DatabaseInstance(typing.TypedDict, total=False):
    databaseUrl: str
    name: str
    project: str
    state: typing.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED", "ACTIVE", "DISABLED", "DELETED"
    ]
    type: typing.Literal[
        "DATABASE_INSTANCE_TYPE_UNSPECIFIED", "DEFAULT_DATABASE", "USER_DATABASE"
    ]

@typing.type_check_only
class DisableDatabaseInstanceRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ListDatabaseInstancesResponse(typing.TypedDict, total=False):
    instances: _list[DatabaseInstance]
    nextPageToken: str

@typing.type_check_only
class ReenableDatabaseInstanceRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteDatabaseInstanceRequest(typing.TypedDict, total=False): ...

import typing

import typing_extensions

_list = list

@typing.type_check_only
class DatabaseInstance(typing_extensions.TypedDict, total=False):
    databaseUrl: str
    name: str
    project: str
    state: typing_extensions.Literal[
        "LIFECYCLE_STATE_UNSPECIFIED", "ACTIVE", "DISABLED", "DELETED"
    ]
    type: typing_extensions.Literal[
        "DATABASE_INSTANCE_TYPE_UNSPECIFIED", "DEFAULT_DATABASE", "USER_DATABASE"
    ]

@typing.type_check_only
class DisableDatabaseInstanceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ListDatabaseInstancesResponse(typing_extensions.TypedDict, total=False):
    instances: _list[DatabaseInstance]
    nextPageToken: str

@typing.type_check_only
class ReenableDatabaseInstanceRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UndeleteDatabaseInstanceRequest(typing_extensions.TypedDict, total=False): ...

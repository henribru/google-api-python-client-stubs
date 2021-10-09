import typing

import typing_extensions

_list = list

@typing.type_check_only
class GoogleDatastoreAdminV1CommonMetadata(typing_extensions.TypedDict, total=False):
    endTime: str
    labels: dict[str, typing.Any]
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "EXPORT_ENTITIES",
        "IMPORT_ENTITIES",
        "CREATE_INDEX",
        "DELETE_INDEX",
    ]
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "INITIALIZING",
        "PROCESSING",
        "CANCELLING",
        "FINALIZING",
        "SUCCESSFUL",
        "FAILED",
        "CANCELLED",
    ]

@typing.type_check_only
class GoogleDatastoreAdminV1EntityFilter(typing_extensions.TypedDict, total=False):
    kinds: _list[str]
    namespaceIds: _list[str]

@typing.type_check_only
class GoogleDatastoreAdminV1ExportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    common: GoogleDatastoreAdminV1CommonMetadata
    entityFilter: GoogleDatastoreAdminV1EntityFilter
    outputUrlPrefix: str
    progressBytes: GoogleDatastoreAdminV1Progress
    progressEntities: GoogleDatastoreAdminV1Progress

@typing.type_check_only
class GoogleDatastoreAdminV1ExportEntitiesResponse(
    typing_extensions.TypedDict, total=False
):
    outputUrl: str

@typing.type_check_only
class GoogleDatastoreAdminV1ImportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    common: GoogleDatastoreAdminV1CommonMetadata
    entityFilter: GoogleDatastoreAdminV1EntityFilter
    inputUrl: str
    progressBytes: GoogleDatastoreAdminV1Progress
    progressEntities: GoogleDatastoreAdminV1Progress

@typing.type_check_only
class GoogleDatastoreAdminV1IndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    common: GoogleDatastoreAdminV1CommonMetadata
    indexId: str
    progressEntities: GoogleDatastoreAdminV1Progress

@typing.type_check_only
class GoogleDatastoreAdminV1Progress(typing_extensions.TypedDict, total=False):
    workCompleted: str
    workEstimated: str

@typing.type_check_only
class GoogleDatastoreAdminV1beta1CommonMetadata(
    typing_extensions.TypedDict, total=False
):
    endTime: str
    labels: dict[str, typing.Any]
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "EXPORT_ENTITIES", "IMPORT_ENTITIES"
    ]
    startTime: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "INITIALIZING",
        "PROCESSING",
        "CANCELLING",
        "FINALIZING",
        "SUCCESSFUL",
        "FAILED",
        "CANCELLED",
    ]

@typing.type_check_only
class GoogleDatastoreAdminV1beta1EntityFilter(typing_extensions.TypedDict, total=False):
    kinds: _list[str]
    namespaceIds: _list[str]

@typing.type_check_only
class GoogleDatastoreAdminV1beta1ExportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    common: GoogleDatastoreAdminV1beta1CommonMetadata
    entityFilter: GoogleDatastoreAdminV1beta1EntityFilter
    outputUrlPrefix: str
    progressBytes: GoogleDatastoreAdminV1beta1Progress
    progressEntities: GoogleDatastoreAdminV1beta1Progress

@typing.type_check_only
class GoogleDatastoreAdminV1beta1ExportEntitiesRequest(
    typing_extensions.TypedDict, total=False
):
    entityFilter: GoogleDatastoreAdminV1beta1EntityFilter
    labels: dict[str, typing.Any]
    outputUrlPrefix: str

@typing.type_check_only
class GoogleDatastoreAdminV1beta1ExportEntitiesResponse(
    typing_extensions.TypedDict, total=False
):
    outputUrl: str

@typing.type_check_only
class GoogleDatastoreAdminV1beta1ImportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    common: GoogleDatastoreAdminV1beta1CommonMetadata
    entityFilter: GoogleDatastoreAdminV1beta1EntityFilter
    inputUrl: str
    progressBytes: GoogleDatastoreAdminV1beta1Progress
    progressEntities: GoogleDatastoreAdminV1beta1Progress

@typing.type_check_only
class GoogleDatastoreAdminV1beta1ImportEntitiesRequest(
    typing_extensions.TypedDict, total=False
):
    entityFilter: GoogleDatastoreAdminV1beta1EntityFilter
    inputUrl: str
    labels: dict[str, typing.Any]

@typing.type_check_only
class GoogleDatastoreAdminV1beta1Progress(typing_extensions.TypedDict, total=False):
    workCompleted: str
    workEstimated: str

@typing.type_check_only
class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

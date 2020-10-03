import typing

import typing_extensions

class GoogleDatastoreAdminV1beta1ImportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    entityFilter: GoogleDatastoreAdminV1beta1EntityFilter
    common: GoogleDatastoreAdminV1beta1CommonMetadata
    inputUrl: str
    progressEntities: GoogleDatastoreAdminV1beta1Progress
    progressBytes: GoogleDatastoreAdminV1beta1Progress

class GoogleDatastoreAdminV1Progress(typing_extensions.TypedDict, total=False):
    workCompleted: str
    workEstimated: str

class GoogleDatastoreAdminV1beta1ExportEntitiesResponse(
    typing_extensions.TypedDict, total=False
):
    outputUrl: str

class GoogleDatastoreAdminV1beta1ExportEntitiesRequest(
    typing_extensions.TypedDict, total=False
):
    labels: typing.Dict[str, typing.Any]
    entityFilter: GoogleDatastoreAdminV1beta1EntityFilter
    outputUrlPrefix: str

class GoogleDatastoreAdminV1beta1ExportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    progressEntities: GoogleDatastoreAdminV1beta1Progress
    outputUrlPrefix: str
    common: GoogleDatastoreAdminV1beta1CommonMetadata
    progressBytes: GoogleDatastoreAdminV1beta1Progress
    entityFilter: GoogleDatastoreAdminV1beta1EntityFilter

class GoogleDatastoreAdminV1ImportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    progressEntities: GoogleDatastoreAdminV1Progress
    progressBytes: GoogleDatastoreAdminV1Progress
    entityFilter: GoogleDatastoreAdminV1EntityFilter
    inputUrl: str
    common: GoogleDatastoreAdminV1CommonMetadata

class GoogleDatastoreAdminV1IndexOperationMetadata(
    typing_extensions.TypedDict, total=False
):
    progressEntities: GoogleDatastoreAdminV1Progress
    common: GoogleDatastoreAdminV1CommonMetadata
    indexId: str

class GoogleDatastoreAdminV1CommonMetadata(typing_extensions.TypedDict, total=False):
    startTime: str
    endTime: str
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
    labels: typing.Dict[str, typing.Any]
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED",
        "EXPORT_ENTITIES",
        "IMPORT_ENTITIES",
        "CREATE_INDEX",
        "DELETE_INDEX",
    ]

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class GoogleLongrunningOperation(typing_extensions.TypedDict, total=False):
    name: str
    response: typing.Dict[str, typing.Any]
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]

class GoogleDatastoreAdminV1beta1EntityFilter(typing_extensions.TypedDict, total=False):
    kinds: typing.List[str]
    namespaceIds: typing.List[str]

class GoogleDatastoreAdminV1beta1CommonMetadata(
    typing_extensions.TypedDict, total=False
):
    startTime: str
    operationType: typing_extensions.Literal[
        "OPERATION_TYPE_UNSPECIFIED", "EXPORT_ENTITIES", "IMPORT_ENTITIES"
    ]
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
    endTime: str
    labels: typing.Dict[str, typing.Any]

class GoogleDatastoreAdminV1EntityFilter(typing_extensions.TypedDict, total=False):
    namespaceIds: typing.List[str]
    kinds: typing.List[str]

class GoogleDatastoreAdminV1ExportEntitiesResponse(
    typing_extensions.TypedDict, total=False
):
    outputUrl: str

class GoogleDatastoreAdminV1beta1Progress(typing_extensions.TypedDict, total=False):
    workEstimated: str
    workCompleted: str

class GoogleDatastoreAdminV1beta1ImportEntitiesRequest(
    typing_extensions.TypedDict, total=False
):
    inputUrl: str
    entityFilter: GoogleDatastoreAdminV1beta1EntityFilter
    labels: typing.Dict[str, typing.Any]

class GoogleDatastoreAdminV1ExportEntitiesMetadata(
    typing_extensions.TypedDict, total=False
):
    entityFilter: GoogleDatastoreAdminV1EntityFilter
    common: GoogleDatastoreAdminV1CommonMetadata
    progressEntities: GoogleDatastoreAdminV1Progress
    progressBytes: GoogleDatastoreAdminV1Progress
    outputUrlPrefix: str

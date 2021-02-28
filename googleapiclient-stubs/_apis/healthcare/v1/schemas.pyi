import typing

import typing_extensions
@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: typing.List[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CharacterMaskConfig(typing_extensions.TypedDict, total=False):
    maskingCharacter: str

@typing.type_check_only
class CreateMessageRequest(typing_extensions.TypedDict, total=False):
    message: Message

@typing.type_check_only
class CryptoHashConfig(typing_extensions.TypedDict, total=False):
    cryptoKey: str

@typing.type_check_only
class Dataset(typing_extensions.TypedDict, total=False):
    name: str
    timeZone: str

@typing.type_check_only
class DateShiftConfig(typing_extensions.TypedDict, total=False):
    cryptoKey: str

@typing.type_check_only
class DeidentifyConfig(typing_extensions.TypedDict, total=False):
    dicom: DicomConfig
    fhir: FhirConfig
    image: ImageConfig
    text: TextConfig

@typing.type_check_only
class DeidentifyDatasetRequest(typing_extensions.TypedDict, total=False):
    config: DeidentifyConfig
    destinationDataset: str

@typing.type_check_only
class DeidentifyDicomStoreRequest(typing_extensions.TypedDict, total=False):
    config: DeidentifyConfig
    destinationStore: str
    filterConfig: DicomFilterConfig

@typing.type_check_only
class DeidentifyFhirStoreRequest(typing_extensions.TypedDict, total=False):
    config: DeidentifyConfig
    destinationStore: str
    resourceFilter: FhirFilter

@typing.type_check_only
class DeidentifySummary(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DicomConfig(typing_extensions.TypedDict, total=False):
    filterProfile: typing_extensions.Literal[
        "TAG_FILTER_PROFILE_UNSPECIFIED",
        "MINIMAL_KEEP_LIST_PROFILE",
        "ATTRIBUTE_CONFIDENTIALITY_BASIC_PROFILE",
        "KEEP_ALL_PROFILE",
        "DEIDENTIFY_TAG_CONTENTS",
    ]
    keepList: TagFilterList
    removeList: TagFilterList
    skipIdRedaction: bool

@typing.type_check_only
class DicomFilterConfig(typing_extensions.TypedDict, total=False):
    resourcePathsGcsUri: str

@typing.type_check_only
class DicomStore(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    name: str
    notificationConfig: NotificationConfig

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExportDicomDataRequest(typing_extensions.TypedDict, total=False):
    bigqueryDestination: GoogleCloudHealthcareV1DicomBigQueryDestination
    gcsDestination: GoogleCloudHealthcareV1DicomGcsDestination

@typing.type_check_only
class ExportDicomDataResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExportResourcesRequest(typing_extensions.TypedDict, total=False):
    bigqueryDestination: GoogleCloudHealthcareV1FhirBigQueryDestination
    gcsDestination: GoogleCloudHealthcareV1FhirGcsDestination

@typing.type_check_only
class ExportResourcesResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class FhirConfig(typing_extensions.TypedDict, total=False):
    fieldMetadataList: typing.List[FieldMetadata]

@typing.type_check_only
class FhirFilter(typing_extensions.TypedDict, total=False):
    resources: Resources

@typing.type_check_only
class FhirStore(typing_extensions.TypedDict, total=False):
    disableReferentialIntegrity: bool
    disableResourceVersioning: bool
    enableUpdateCreate: bool
    labels: typing.Dict[str, typing.Any]
    name: str
    notificationConfig: NotificationConfig
    streamConfigs: typing.List[StreamConfig]
    version: typing_extensions.Literal["VERSION_UNSPECIFIED", "DSTU2", "STU3", "R4"]

@typing.type_check_only
class FieldMetadata(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal[
        "ACTION_UNSPECIFIED", "TRANSFORM", "INSPECT_AND_TRANSFORM", "DO_NOT_TRANSFORM"
    ]
    paths: typing.List[str]

@typing.type_check_only
class GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummary(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummary(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudHealthcareV1DicomBigQueryDestination(
    typing_extensions.TypedDict, total=False
):
    force: bool
    tableUri: str

@typing.type_check_only
class GoogleCloudHealthcareV1DicomGcsDestination(
    typing_extensions.TypedDict, total=False
):
    mimeType: str
    uriPrefix: str

@typing.type_check_only
class GoogleCloudHealthcareV1DicomGcsSource(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudHealthcareV1FhirBigQueryDestination(
    typing_extensions.TypedDict, total=False
):
    datasetUri: str
    force: bool
    schemaConfig: SchemaConfig
    writeDisposition: typing_extensions.Literal[
        "WRITE_DISPOSITION_UNSPECIFIED", "WRITE_EMPTY", "WRITE_TRUNCATE", "WRITE_APPEND"
    ]

@typing.type_check_only
class GoogleCloudHealthcareV1FhirGcsDestination(
    typing_extensions.TypedDict, total=False
):
    uriPrefix: str

@typing.type_check_only
class GoogleCloudHealthcareV1FhirGcsSource(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class Hl7V2NotificationConfig(typing_extensions.TypedDict, total=False):
    filter: str
    pubsubTopic: str

@typing.type_check_only
class Hl7V2Store(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    name: str
    notificationConfigs: typing.List[Hl7V2NotificationConfig]
    parserConfig: ParserConfig
    rejectDuplicateMessage: bool

@typing.type_check_only
class HttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: typing.List[typing.Dict[str, typing.Any]]

@typing.type_check_only
class ImageConfig(typing_extensions.TypedDict, total=False):
    textRedactionMode: typing_extensions.Literal[
        "TEXT_REDACTION_MODE_UNSPECIFIED",
        "REDACT_ALL_TEXT",
        "REDACT_SENSITIVE_TEXT",
        "REDACT_NO_TEXT",
    ]

@typing.type_check_only
class ImportDicomDataRequest(typing_extensions.TypedDict, total=False):
    gcsSource: GoogleCloudHealthcareV1DicomGcsSource

@typing.type_check_only
class ImportDicomDataResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ImportResourcesRequest(typing_extensions.TypedDict, total=False):
    contentStructure: typing_extensions.Literal[
        "CONTENT_STRUCTURE_UNSPECIFIED",
        "BUNDLE",
        "RESOURCE",
        "BUNDLE_PRETTY",
        "RESOURCE_PRETTY",
    ]
    gcsSource: GoogleCloudHealthcareV1FhirGcsSource

@typing.type_check_only
class ImportResourcesResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class InfoTypeTransformation(typing_extensions.TypedDict, total=False):
    characterMaskConfig: CharacterMaskConfig
    cryptoHashConfig: CryptoHashConfig
    dateShiftConfig: DateShiftConfig
    infoTypes: typing.List[str]
    redactConfig: RedactConfig
    replaceWithInfoTypeConfig: ReplaceWithInfoTypeConfig

@typing.type_check_only
class IngestMessageRequest(typing_extensions.TypedDict, total=False):
    message: Message

@typing.type_check_only
class IngestMessageResponse(typing_extensions.TypedDict, total=False):
    hl7Ack: str
    message: Message

@typing.type_check_only
class ListDatasetsResponse(typing_extensions.TypedDict, total=False):
    datasets: typing.List[Dataset]
    nextPageToken: str

@typing.type_check_only
class ListDicomStoresResponse(typing_extensions.TypedDict, total=False):
    dicomStores: typing.List[DicomStore]
    nextPageToken: str

@typing.type_check_only
class ListFhirStoresResponse(typing_extensions.TypedDict, total=False):
    fhirStores: typing.List[FhirStore]
    nextPageToken: str

@typing.type_check_only
class ListHl7V2StoresResponse(typing_extensions.TypedDict, total=False):
    hl7V2Stores: typing.List[Hl7V2Store]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: typing.List[Location]
    nextPageToken: str

@typing.type_check_only
class ListMessagesResponse(typing_extensions.TypedDict, total=False):
    hl7V2Messages: typing.List[Message]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: typing.List[Operation]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: typing.Dict[str, typing.Any]
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class Message(typing_extensions.TypedDict, total=False):
    createTime: str
    data: str
    labels: typing.Dict[str, typing.Any]
    messageType: str
    name: str
    parsedData: ParsedData
    patientIds: typing.List[PatientId]
    sendFacility: str
    sendTime: str

@typing.type_check_only
class NotificationConfig(typing_extensions.TypedDict, total=False):
    pubsubTopic: str

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: typing.Dict[str, typing.Any]
    name: str
    response: typing.Dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiMethodName: str
    cancelRequested: bool
    counter: ProgressCounter
    createTime: str
    endTime: str
    logsUrl: str

@typing.type_check_only
class ParsedData(typing_extensions.TypedDict, total=False):
    segments: typing.List[Segment]

@typing.type_check_only
class ParserConfig(typing_extensions.TypedDict, total=False):
    allowNullHeader: bool
    segmentTerminator: str

@typing.type_check_only
class PatientId(typing_extensions.TypedDict, total=False):
    type: str
    value: str

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    etag: str
    version: int

@typing.type_check_only
class ProgressCounter(typing_extensions.TypedDict, total=False):
    failure: str
    pending: str
    success: str

@typing.type_check_only
class RedactConfig(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ReplaceWithInfoTypeConfig(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Resources(typing_extensions.TypedDict, total=False):
    resources: typing.List[str]

@typing.type_check_only
class SchemaConfig(typing_extensions.TypedDict, total=False):
    recursiveStructureDepth: str
    schemaType: typing_extensions.Literal["SCHEMA_TYPE_UNSPECIFIED", "ANALYTICS"]

@typing.type_check_only
class SearchResourcesRequest(typing_extensions.TypedDict, total=False):
    resourceType: str

@typing.type_check_only
class Segment(typing_extensions.TypedDict, total=False):
    fields: typing.Dict[str, typing.Any]
    segmentId: str
    setId: str

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StreamConfig(typing_extensions.TypedDict, total=False):
    bigqueryDestination: GoogleCloudHealthcareV1FhirBigQueryDestination
    resourceTypes: typing.List[str]

@typing.type_check_only
class TagFilterList(typing_extensions.TypedDict, total=False):
    tags: typing.List[str]

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

@typing.type_check_only
class TextConfig(typing_extensions.TypedDict, total=False):
    transformations: typing.List[InfoTypeTransformation]

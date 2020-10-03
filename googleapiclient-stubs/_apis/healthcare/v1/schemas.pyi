import typing

import typing_extensions

class CreateMessageRequest(typing_extensions.TypedDict, total=False):
    message: Message

class Hl7V2NotificationConfig(typing_extensions.TypedDict, total=False):
    filter: str
    pubsubTopic: str

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class ParsedData(typing_extensions.TypedDict, total=False):
    segments: typing.List[Segment]

class Policy(typing_extensions.TypedDict, total=False):
    version: int
    auditConfigs: typing.List[AuditConfig]
    etag: str
    bindings: typing.List[Binding]

class Status(typing_extensions.TypedDict, total=False):
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str
    code: int

class Location(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    displayName: str
    name: str
    metadata: typing.Dict[str, typing.Any]
    locationId: str

class ListMessagesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    hl7V2Messages: typing.List[Message]

class ExportDicomDataRequest(typing_extensions.TypedDict, total=False):
    bigqueryDestination: GoogleCloudHealthcareV1DicomBigQueryDestination
    gcsDestination: GoogleCloudHealthcareV1DicomGcsDestination

class GoogleCloudHealthcareV1DicomGcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class DateShiftConfig(typing_extensions.TypedDict, total=False):
    cryptoKey: str

class FhirFilter(typing_extensions.TypedDict, total=False):
    resources: Resources

class ParserConfig(typing_extensions.TypedDict, total=False):
    allowNullHeader: bool
    segmentTerminator: str

class FieldMetadata(typing_extensions.TypedDict, total=False):
    paths: typing.List[str]
    action: typing_extensions.Literal[
        "ACTION_UNSPECIFIED", "TRANSFORM", "INSPECT_AND_TRANSFORM", "DO_NOT_TRANSFORM"
    ]

class ExportDicomDataResponse(typing_extensions.TypedDict, total=False): ...

class SearchResourcesRequest(typing_extensions.TypedDict, total=False):
    resourceType: str

class TagFilterList(typing_extensions.TypedDict, total=False):
    tags: typing.List[str]

class CharacterMaskConfig(typing_extensions.TypedDict, total=False):
    maskingCharacter: str

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class DicomStore(typing_extensions.TypedDict, total=False):
    notificationConfig: NotificationConfig
    labels: typing.Dict[str, typing.Any]
    name: str

class Expr(typing_extensions.TypedDict, total=False):
    title: str
    description: str
    expression: str
    location: str

class Binding(typing_extensions.TypedDict, total=False):
    members: typing.List[str]
    role: str
    condition: Expr

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

class ImportResourcesRequest(typing_extensions.TypedDict, total=False):
    contentStructure: typing_extensions.Literal[
        "CONTENT_STRUCTURE_UNSPECIFIED",
        "BUNDLE",
        "RESOURCE",
        "BUNDLE_PRETTY",
        "RESOURCE_PRETTY",
    ]
    gcsSource: GoogleCloudHealthcareV1FhirGcsSource

class FhirConfig(typing_extensions.TypedDict, total=False):
    fieldMetadataList: typing.List[FieldMetadata]

class Operation(typing_extensions.TypedDict, total=False):
    error: Status
    response: typing.Dict[str, typing.Any]
    name: str
    metadata: typing.Dict[str, typing.Any]
    done: bool

class InfoTypeTransformation(typing_extensions.TypedDict, total=False):
    replaceWithInfoTypeConfig: ReplaceWithInfoTypeConfig
    characterMaskConfig: CharacterMaskConfig
    dateShiftConfig: DateShiftConfig
    infoTypes: typing.List[str]
    redactConfig: RedactConfig
    cryptoHashConfig: CryptoHashConfig

class PatientId(typing_extensions.TypedDict, total=False):
    value: str
    type: str

class DicomFilterConfig(typing_extensions.TypedDict, total=False):
    resourcePathsGcsUri: str

class ListDicomStoresResponse(typing_extensions.TypedDict, total=False):
    dicomStores: typing.List[DicomStore]
    nextPageToken: str

class ImageConfig(typing_extensions.TypedDict, total=False):
    textRedactionMode: typing_extensions.Literal[
        "TEXT_REDACTION_MODE_UNSPECIFIED",
        "REDACT_ALL_TEXT",
        "REDACT_SENSITIVE_TEXT",
        "REDACT_NO_TEXT",
    ]

class IngestMessageRequest(typing_extensions.TypedDict, total=False):
    message: Message

class DicomConfig(typing_extensions.TypedDict, total=False):
    skipIdRedaction: bool
    removeList: TagFilterList
    filterProfile: typing_extensions.Literal[
        "TAG_FILTER_PROFILE_UNSPECIFIED",
        "MINIMAL_KEEP_LIST_PROFILE",
        "ATTRIBUTE_CONFIDENTIALITY_BASIC_PROFILE",
        "KEEP_ALL_PROFILE",
        "DEIDENTIFY_TAG_CONTENTS",
    ]
    keepList: TagFilterList

class SchemaConfig(typing_extensions.TypedDict, total=False):
    recursiveStructureDepth: str
    schemaType: typing_extensions.Literal["SCHEMA_TYPE_UNSPECIFIED", "ANALYTICS"]

class ReplaceWithInfoTypeConfig(typing_extensions.TypedDict, total=False): ...

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class CryptoHashConfig(typing_extensions.TypedDict, total=False):
    cryptoKey: str

class Message(typing_extensions.TypedDict, total=False):
    messageType: str
    parsedData: ParsedData
    data: str
    labels: typing.Dict[str, typing.Any]
    sendFacility: str
    patientIds: typing.List[PatientId]
    sendTime: str
    name: str
    createTime: str

class DeidentifyDicomStoreRequest(typing_extensions.TypedDict, total=False):
    filterConfig: DicomFilterConfig
    config: DeidentifyConfig
    destinationStore: str

class Resources(typing_extensions.TypedDict, total=False):
    resources: typing.List[str]

class GoogleCloudHealthcareV1FhirGcsDestination(
    typing_extensions.TypedDict, total=False
):
    uriPrefix: str

class FhirStore(typing_extensions.TypedDict, total=False):
    enableUpdateCreate: bool
    disableResourceVersioning: bool
    streamConfigs: typing.List[StreamConfig]
    notificationConfig: NotificationConfig
    labels: typing.Dict[str, typing.Any]
    version: typing_extensions.Literal["VERSION_UNSPECIFIED", "DSTU2", "STU3", "R4"]
    disableReferentialIntegrity: bool
    name: str

class ExportResourcesResponse(typing_extensions.TypedDict, total=False): ...

class DeidentifyDatasetRequest(typing_extensions.TypedDict, total=False):
    destinationDataset: str
    config: DeidentifyConfig

class Segment(typing_extensions.TypedDict, total=False):
    setId: str
    segmentId: str
    fields: typing.Dict[str, typing.Any]

class TextConfig(typing_extensions.TypedDict, total=False):
    transformations: typing.List[InfoTypeTransformation]

class Empty(typing_extensions.TypedDict, total=False): ...

class StreamConfig(typing_extensions.TypedDict, total=False):
    bigqueryDestination: GoogleCloudHealthcareV1FhirBigQueryDestination
    resourceTypes: typing.List[str]

class DeidentifyFhirStoreRequest(typing_extensions.TypedDict, total=False):
    destinationStore: str
    config: DeidentifyConfig
    resourceFilter: FhirFilter

class GoogleCloudHealthcareV1DeidentifyDeidentifyDicomStoreSummary(
    typing_extensions.TypedDict, total=False
): ...

class ImportDicomDataRequest(typing_extensions.TypedDict, total=False):
    gcsSource: GoogleCloudHealthcareV1DicomGcsSource

class IngestMessageResponse(typing_extensions.TypedDict, total=False):
    message: Message
    hl7Ack: str

class Hl7V2Store(typing_extensions.TypedDict, total=False):
    rejectDuplicateMessage: bool
    labels: typing.Dict[str, typing.Any]
    name: str
    notificationConfigs: typing.List[Hl7V2NotificationConfig]
    parserConfig: ParserConfig

class ImportResourcesResponse(typing_extensions.TypedDict, total=False): ...

class ListHl7V2StoresResponse(typing_extensions.TypedDict, total=False):
    hl7V2Stores: typing.List[Hl7V2Store]
    nextPageToken: str

class GoogleCloudHealthcareV1DicomBigQueryDestination(
    typing_extensions.TypedDict, total=False
):
    tableUri: str
    force: bool

class HttpBody(typing_extensions.TypedDict, total=False):
    extensions: typing.List[typing.Dict[str, typing.Any]]
    contentType: str
    data: str

class DeidentifyConfig(typing_extensions.TypedDict, total=False):
    fhir: FhirConfig
    dicom: DicomConfig
    image: ImageConfig
    text: TextConfig

class GoogleCloudHealthcareV1DeidentifyDeidentifyFhirStoreSummary(
    typing_extensions.TypedDict, total=False
): ...

class GoogleCloudHealthcareV1FhirBigQueryDestination(
    typing_extensions.TypedDict, total=False
):
    force: bool
    datasetUri: str
    schemaConfig: SchemaConfig

class Dataset(typing_extensions.TypedDict, total=False):
    timeZone: str
    name: str

class ProgressCounter(typing_extensions.TypedDict, total=False):
    success: str
    failure: str
    pending: str

class ListFhirStoresResponse(typing_extensions.TypedDict, total=False):
    fhirStores: typing.List[FhirStore]
    nextPageToken: str

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class AuditConfig(typing_extensions.TypedDict, total=False):
    service: str
    auditLogConfigs: typing.List[AuditLogConfig]

class RedactConfig(typing_extensions.TypedDict, total=False): ...
class ImportDicomDataResponse(typing_extensions.TypedDict, total=False): ...

class GoogleCloudHealthcareV1DicomGcsDestination(
    typing_extensions.TypedDict, total=False
):
    uriPrefix: str
    mimeType: str

class ExportResourcesRequest(typing_extensions.TypedDict, total=False):
    bigqueryDestination: GoogleCloudHealthcareV1FhirBigQueryDestination
    gcsDestination: GoogleCloudHealthcareV1FhirGcsDestination

class GoogleCloudHealthcareV1FhirGcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class OperationMetadata(typing_extensions.TypedDict, total=False):
    endTime: str
    cancelRequested: bool
    counter: ProgressCounter
    logsUrl: str
    createTime: str
    apiMethodName: str

class DeidentifySummary(typing_extensions.TypedDict, total=False): ...

class ListDatasetsResponse(typing_extensions.TypedDict, total=False):
    datasets: typing.List[Dataset]
    nextPageToken: str

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[Location]

class NotificationConfig(typing_extensions.TypedDict, total=False):
    pubsubTopic: str

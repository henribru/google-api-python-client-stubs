import typing

import typing_extensions

class GoogleCloudHealthcareV1beta1FhirRestExportResourcesResponse(
    typing_extensions.TypedDict, total=False
):
    resourceCount: str
    fhirStore: str

class GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

class Field(typing_extensions.TypedDict, total=False):
    name: str
    table: str
    type: str
    minOccurs: int
    maxOccurs: int

class Signature(typing_extensions.TypedDict, total=False):
    signatureTime: str
    userId: str
    image: Image
    metadata: typing.Dict[str, typing.Any]

class EvaluateUserConsentsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    results: typing.List[Result]

class GoogleCloudHealthcareV1beta1AnnotationGcsSource(
    typing_extensions.TypedDict, total=False
):
    uri: str

class DeidentifyConfig(typing_extensions.TypedDict, total=False):
    fhir: FhirConfig
    annotation: AnnotationConfig
    dicom: DicomConfig
    image: ImageConfig
    text: TextConfig

class GoogleCloudHealthcareV1beta1FhirRestExportResourcesErrorDetails(
    typing_extensions.TypedDict, total=False
):
    successCount: str
    resourceCount: str
    fhirStore: str
    errorCount: str

class ImportDicomDataRequest(typing_extensions.TypedDict, total=False):
    gcsSource: GoogleCloudHealthcareV1beta1DicomGcsSource

class RevokeConsentRequest(typing_extensions.TypedDict, total=False):
    consentArtifact: str

class ImportMessagesRequest(typing_extensions.TypedDict, total=False):
    gcsSource: GcsSource

class ListAnnotationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    annotations: typing.List[Annotation]

class ArchiveUserDataMappingResponse(typing_extensions.TypedDict, total=False): ...

class Segment(typing_extensions.TypedDict, total=False):
    fields: typing.Dict[str, typing.Any]
    segmentId: str
    setId: str

class GoogleCloudHealthcareV1beta1DicomStreamConfig(
    typing_extensions.TypedDict, total=False
):
    bigqueryDestination: GoogleCloudHealthcareV1beta1DicomBigQueryDestination

class Resources(typing_extensions.TypedDict, total=False):
    resources: typing.List[str]

class ListConsentArtifactsResponse(typing_extensions.TypedDict, total=False):
    consentArtifacts: typing.List[ConsentArtifact]
    nextPageToken: str

class AnnotationStore(typing_extensions.TypedDict, total=False):
    name: str
    labels: typing.Dict[str, typing.Any]

class Hl7V2NotificationConfig(typing_extensions.TypedDict, total=False):
    pubsubTopic: str
    filter: str

class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiMethodName: str
    cancelRequested: bool
    createTime: str
    endTime: str
    logsUrl: str
    counter: ProgressCounter

class CheckDataAccessRequest(typing_extensions.TypedDict, total=False):
    dataId: str
    consentList: ConsentList
    requestAttributes: typing.Dict[str, typing.Any]
    responseView: typing_extensions.Literal[
        "RESPONSE_VIEW_UNSPECIFIED", "BASIC", "FULL"
    ]

class SchemaGroup(typing_extensions.TypedDict, total=False):
    minOccurs: int
    members: typing.List[GroupOrSegment]
    choice: bool
    maxOccurs: int
    name: str

class GoogleCloudHealthcareV1beta1FhirRestImportResourcesErrorDetails(
    typing_extensions.TypedDict, total=False
):
    inputSize: str
    fhirStore: str
    successCount: str
    errorCount: str

class ImportAnnotationsRequest(typing_extensions.TypedDict, total=False):
    gcsSource: GoogleCloudHealthcareV1beta1AnnotationGcsSource
    name: str

class StreamConfig(typing_extensions.TypedDict, total=False):
    resourceTypes: typing.List[str]
    bigqueryDestination: GoogleCloudHealthcareV1beta1FhirBigQueryDestination

class UserDataMapping(typing_extensions.TypedDict, total=False):
    userId: str
    resourceAttributes: typing.List[Attribute]
    archived: bool
    name: str
    archiveTime: str
    dataId: str

class SchemaPackage(typing_extensions.TypedDict, total=False):
    types: typing.List[Hl7TypesConfig]
    unexpectedSegmentHandling: typing_extensions.Literal[
        "UNEXPECTED_SEGMENT_HANDLING_MODE_UNSPECIFIED", "FAIL", "SKIP", "PARSE"
    ]
    schematizedParsingType: typing_extensions.Literal[
        "SCHEMATIZED_PARSING_TYPE_UNSPECIFIED", "SOFT_FAIL", "HARD_FAIL"
    ]
    ignoreMinOccurs: bool
    schemas: typing.List[Hl7SchemaConfig]

class DicomConfig(typing_extensions.TypedDict, total=False):
    keepList: TagFilterList
    skipIdRedaction: bool
    filterProfile: typing_extensions.Literal[
        "TAG_FILTER_PROFILE_UNSPECIFIED",
        "MINIMAL_KEEP_LIST_PROFILE",
        "ATTRIBUTE_CONFIDENTIALITY_BASIC_PROFILE",
        "KEEP_ALL_PROFILE",
        "DEIDENTIFY_TAG_CONTENTS",
    ]
    removeList: TagFilterList

class HttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    extensions: typing.List[typing.Dict[str, typing.Any]]
    data: str

class RedactConfig(typing_extensions.TypedDict, total=False): ...

class IngestMessageRequest(typing_extensions.TypedDict, total=False):
    message: Message

class VersionSource(typing_extensions.TypedDict, total=False):
    value: str
    mshField: str

class ImageAnnotation(typing_extensions.TypedDict, total=False):
    frameIndex: int
    boundingPolys: typing.List[BoundingPoly]

class SchemaSegment(typing_extensions.TypedDict, total=False):
    minOccurs: int
    type: str
    maxOccurs: int

class DicomStore(typing_extensions.TypedDict, total=False):
    name: str
    streamConfigs: typing.List[GoogleCloudHealthcareV1beta1DicomStreamConfig]
    notificationConfig: NotificationConfig
    labels: typing.Dict[str, typing.Any]

class Message(typing_extensions.TypedDict, total=False):
    sendFacility: str
    data: str
    createTime: str
    schematizedData: SchematizedData
    labels: typing.Dict[str, typing.Any]
    messageType: str
    sendTime: str
    name: str
    patientIds: typing.List[PatientId]
    parsedData: ParsedData

class Hl7TypesConfig(typing_extensions.TypedDict, total=False):
    type: typing.List[Type]
    version: typing.List[VersionSource]

class ResourceAnnotation(typing_extensions.TypedDict, total=False):
    label: str

class FieldMetadata(typing_extensions.TypedDict, total=False):
    paths: typing.List[str]
    action: typing_extensions.Literal[
        "ACTION_UNSPECIFIED", "TRANSFORM", "INSPECT_AND_TRANSFORM", "DO_NOT_TRANSFORM"
    ]

class AttributeDefinition(typing_extensions.TypedDict, total=False):
    consentDefaultValues: typing.List[str]
    description: str
    category: typing_extensions.Literal["CATEGORY_UNSPECIFIED", "RESOURCE", "REQUEST"]
    allowedValues: typing.List[str]
    dataMappingDefaultValue: str
    name: str

class EvaluateAnnotationStoreResponse(typing_extensions.TypedDict, total=False):
    evalStore: str
    goldenStore: str
    goldenCount: str
    matchedCount: str

class AuditConfig(typing_extensions.TypedDict, total=False):
    service: str
    auditLogConfigs: typing.List[AuditLogConfig]

class Result(typing_extensions.TypedDict, total=False):
    dataId: str
    consented: bool
    consentDetails: typing.Dict[str, typing.Any]

class QueryAccessibleDataRequest(typing_extensions.TypedDict, total=False):
    gcsDestination: GoogleCloudHealthcareV1beta1ConsentGcsDestination
    resourceAttributes: typing.Dict[str, typing.Any]
    requestAttributes: typing.Dict[str, typing.Any]

class ExportDicomDataRequest(typing_extensions.TypedDict, total=False):
    gcsDestination: GoogleCloudHealthcareV1beta1DicomGcsDestination
    bigqueryDestination: GoogleCloudHealthcareV1beta1DicomBigQueryDestination

class GoogleCloudHealthcareV1beta1FhirRestGcsSource(
    typing_extensions.TypedDict, total=False
):
    uri: str

class TagFilterList(typing_extensions.TypedDict, total=False):
    tags: typing.List[str]

class ExportAnnotationsRequest(typing_extensions.TypedDict, total=False):
    bigqueryDestination: GoogleCloudHealthcareV1beta1AnnotationBigQueryDestination
    gcsDestination: GoogleCloudHealthcareV1beta1AnnotationGcsDestination
    name: str

class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class CreateMessageRequest(typing_extensions.TypedDict, total=False):
    message: Message

class ProgressCounter(typing_extensions.TypedDict, total=False):
    pending: str
    success: str
    failure: str

class DateShiftConfig(typing_extensions.TypedDict, total=False):
    cryptoKey: str

class ListAttributeDefinitionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    attributeDefinitions: typing.List[AttributeDefinition]

class Status(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]

class Dataset(typing_extensions.TypedDict, total=False):
    timeZone: str
    name: str

class PatientId(typing_extensions.TypedDict, total=False):
    type: str
    value: str

class InfoTypeTransformation(typing_extensions.TypedDict, total=False):
    redactConfig: RedactConfig
    replaceWithInfoTypeConfig: ReplaceWithInfoTypeConfig
    dateShiftConfig: DateShiftConfig
    characterMaskConfig: CharacterMaskConfig
    infoTypes: typing.List[str]
    cryptoHashConfig: CryptoHashConfig

class ParsedData(typing_extensions.TypedDict, total=False):
    segments: typing.List[Segment]

class Empty(typing_extensions.TypedDict, total=False): ...

class ConsentStore(typing_extensions.TypedDict, total=False):
    name: str
    enableConsentCreateOnUpdate: bool
    defaultConsentTtl: str
    labels: typing.Dict[str, typing.Any]

class GoogleCloudHealthcareV1beta1FhirBigQueryDestination(
    typing_extensions.TypedDict, total=False
):
    force: bool
    schemaConfig: SchemaConfig
    datasetUri: str

class CryptoHashConfig(typing_extensions.TypedDict, total=False):
    cryptoKey: str

class GoogleCloudHealthcareV1beta1AnnotationGcsDestination(
    typing_extensions.TypedDict, total=False
):
    uriPrefix: str

class GoogleCloudHealthcareV1beta1FhirRestImportResourcesResponse(
    typing_extensions.TypedDict, total=False
):
    fhirStore: str
    inputSize: str

class RejectConsentRequest(typing_extensions.TypedDict, total=False):
    consentArtifact: str

class GoogleCloudHealthcareV1beta1DicomGcsDestination(
    typing_extensions.TypedDict, total=False
):
    mimeType: str
    uriPrefix: str

class SchematizedData(typing_extensions.TypedDict, total=False):
    error: str
    data: str

class GoogleCloudHealthcareV1beta1ConsentPolicy(
    typing_extensions.TypedDict, total=False
):
    resourceAttributes: typing.List[Attribute]
    authorizationRule: Expr

class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    updateMask: str
    policy: Policy

class Attribute(typing_extensions.TypedDict, total=False):
    attributeDefinitionId: str
    values: typing.List[str]

class IngestMessageResponse(typing_extensions.TypedDict, total=False):
    message: Message
    hl7Ack: str

class ListDatasetsResponse(typing_extensions.TypedDict, total=False):
    datasets: typing.List[Dataset]
    nextPageToken: str

class ListUserDataMappingsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    userDataMappings: typing.List[UserDataMapping]

class FilterList(typing_extensions.TypedDict, total=False):
    infoTypes: typing.List[str]

class ImageConfig(typing_extensions.TypedDict, total=False):
    textRedactionMode: typing_extensions.Literal[
        "TEXT_REDACTION_MODE_UNSPECIFIED",
        "REDACT_ALL_TEXT",
        "REDACT_SENSITIVE_TEXT",
        "REDACT_NO_TEXT",
    ]

class CheckDataAccessResponse(typing_extensions.TypedDict, total=False):
    consented: bool
    consentDetails: typing.Dict[str, typing.Any]

class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    operations: typing.List[Operation]
    nextPageToken: str

class GoogleCloudHealthcareV1beta1DicomBigQueryDestination(
    typing_extensions.TypedDict, total=False
):
    tableUri: str
    force: bool

class ListConsentRevisionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    consents: typing.List[Consent]

class ListDicomStoresResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    dicomStores: typing.List[DicomStore]

class GoogleCloudHealthcareV1beta1ConsentGcsDestination(
    typing_extensions.TypedDict, total=False
):
    uriPrefix: str

class ListFhirStoresResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    fhirStores: typing.List[FhirStore]

class SensitiveTextAnnotation(typing_extensions.TypedDict, total=False):
    details: typing.Dict[str, typing.Any]

class Policy(typing_extensions.TypedDict, total=False):
    etag: str
    auditConfigs: typing.List[AuditConfig]
    bindings: typing.List[Binding]
    version: int

class ImportAnnotationsErrorDetails(typing_extensions.TypedDict, total=False):
    successCount: str
    errorCount: str
    annotationStore: str

class ImportDicomDataResponse(typing_extensions.TypedDict, total=False): ...

class DeidentifyFhirStoreRequest(typing_extensions.TypedDict, total=False):
    config: DeidentifyConfig
    destinationStore: str
    resourceFilter: FhirFilter

class AnnotationSource(typing_extensions.TypedDict, total=False):
    cloudHealthcareSource: CloudHealthcareSource

class Binding(typing_extensions.TypedDict, total=False):
    members: typing.List[str]
    condition: Expr
    role: str

class GoogleCloudHealthcareV1beta1FhirRestGcsDestination(
    typing_extensions.TypedDict, total=False
):
    uriPrefix: str

class FhirConfig(typing_extensions.TypedDict, total=False):
    fieldMetadataList: typing.List[FieldMetadata]

class NotificationConfig(typing_extensions.TypedDict, total=False):
    pubsubTopic: str

class Image(typing_extensions.TypedDict, total=False):
    rawBytes: str
    gcsUri: str

class DeidentifyDatasetRequest(typing_extensions.TypedDict, total=False):
    destinationDataset: str
    config: DeidentifyConfig

class ListHl7V2StoresResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    hl7V2Stores: typing.List[Hl7V2Store]

class Expr(typing_extensions.TypedDict, total=False):
    location: str
    title: str
    description: str
    expression: str

class CloudHealthcareSource(typing_extensions.TypedDict, total=False):
    name: str

class SearchResourcesRequest(typing_extensions.TypedDict, total=False):
    resourceType: str

class Hl7SchemaConfig(typing_extensions.TypedDict, total=False):
    version: typing.List[VersionSource]
    messageSchemaConfigs: typing.Dict[str, typing.Any]

class InfoTypeConfig(typing_extensions.TypedDict, total=False):
    ignoreList: FilterList
    strictMatching: bool
    evaluateList: FilterList

class EvaluateAnnotationStoreRequest(typing_extensions.TypedDict, total=False):
    goldenStore: str
    evalInfoTypeMapping: typing.Dict[str, typing.Any]
    name: str
    goldenInfoTypeMapping: typing.Dict[str, typing.Any]
    bigqueryDestination: GoogleCloudHealthcareV1beta1AnnotationBigQueryDestination
    infoTypeConfig: InfoTypeConfig

class Consent(typing_extensions.TypedDict, total=False):
    consentArtifact: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "ARCHIVED", "REVOKED", "DRAFT", "REJECTED"
    ]
    revisionId: str
    ttl: str
    expireTime: str
    userId: str
    name: str
    revisionCreateTime: str
    policies: typing.List[GoogleCloudHealthcareV1beta1ConsentPolicy]

class ReplaceWithInfoTypeConfig(typing_extensions.TypedDict, total=False): ...

class ParserConfig(typing_extensions.TypedDict, total=False):
    segmentTerminator: str
    version: typing_extensions.Literal["PARSER_VERSION_UNSPECIFIED", "V1", "V2"]
    schema: SchemaPackage
    allowNullHeader: bool

class ActivateConsentRequest(typing_extensions.TypedDict, total=False):
    ttl: str
    expireTime: str
    consentArtifact: str

class BoundingPoly(typing_extensions.TypedDict, total=False):
    label: str
    vertices: typing.List[Vertex]

class CharacterMaskConfig(typing_extensions.TypedDict, total=False):
    maskingCharacter: str

class ListMessagesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    hl7V2Messages: typing.List[Message]

class ArchiveUserDataMappingRequest(typing_extensions.TypedDict, total=False): ...

class FhirStore(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    name: str
    notificationConfig: NotificationConfig
    enableUpdateCreate: bool
    version: typing_extensions.Literal["VERSION_UNSPECIFIED", "DSTU2", "STU3", "R4"]
    disableReferentialIntegrity: bool
    disableResourceVersioning: bool
    defaultSearchHandlingStrict: bool
    streamConfigs: typing.List[StreamConfig]

class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: typing.List[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

class Operation(typing_extensions.TypedDict, total=False):
    metadata: typing.Dict[str, typing.Any]
    done: bool
    response: typing.Dict[str, typing.Any]
    error: Status
    name: str

class ImportResourcesRequest(typing_extensions.TypedDict, total=False):
    gcsSource: GoogleCloudHealthcareV1beta1FhirRestGcsSource
    contentStructure: typing_extensions.Literal[
        "CONTENT_STRUCTURE_UNSPECIFIED",
        "BUNDLE",
        "RESOURCE",
        "BUNDLE_PRETTY",
        "RESOURCE_PRETTY",
    ]

class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

class ExportAnnotationsResponse(typing_extensions.TypedDict, total=False):
    annotationStore: str
    successCount: str

class Finding(typing_extensions.TypedDict, total=False):
    end: str
    quote: str
    start: str
    infoType: str

class GoogleCloudHealthcareV1beta1DeidentifyDeidentifyFhirStoreSummary(
    typing_extensions.TypedDict, total=False
):
    successResourceCount: str

class ExportResourcesRequest(typing_extensions.TypedDict, total=False):
    gcsDestination: GoogleCloudHealthcareV1beta1FhirRestGcsDestination
    bigqueryDestination: GoogleCloudHealthcareV1beta1FhirBigQueryDestination

class ImportAnnotationsResponse(typing_extensions.TypedDict, total=False):
    successCount: str
    annotationStore: str

class GoogleCloudHealthcareV1beta1AnnotationBigQueryDestination(
    typing_extensions.TypedDict, total=False
):
    tableUri: str
    force: bool
    schemaType: typing_extensions.Literal["SCHEMA_TYPE_UNSPECIFIED", "SIMPLE"]

class ErrorDetail(typing_extensions.TypedDict, total=False):
    error: Status
    resource: str

class ExportAnnotationsErrorDetails(typing_extensions.TypedDict, total=False):
    errorCount: str
    annotationStore: str
    successCount: str

class ImportMessagesResponse(typing_extensions.TypedDict, total=False): ...

class Hl7V2Store(typing_extensions.TypedDict, total=False):
    rejectDuplicateMessage: bool
    notificationConfig: NotificationConfig
    notificationConfigs: typing.List[Hl7V2NotificationConfig]
    labels: typing.Dict[str, typing.Any]
    name: str
    parserConfig: ParserConfig

class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    locations: typing.List[Location]

class DeidentifySummary(typing_extensions.TypedDict, total=False):
    successStoreCount: str
    successResourceCount: str
    failureResourceCount: str

class ConsentList(typing_extensions.TypedDict, total=False):
    consents: typing.List[str]

class Location(typing_extensions.TypedDict, total=False):
    name: str
    displayName: str
    locationId: str
    metadata: typing.Dict[str, typing.Any]
    labels: typing.Dict[str, typing.Any]

class GroupOrSegment(typing.Dict[str, typing.Any]): ...

class ConsentArtifact(typing_extensions.TypedDict, total=False):
    name: str
    userId: str
    consentContentScreenshots: typing.List[Image]
    userSignature: Signature
    consentContentVersion: str
    witnessSignature: Signature
    guardianSignature: Signature
    metadata: typing.Dict[str, typing.Any]

class Type(typing_extensions.TypedDict, total=False):
    primitive: typing_extensions.Literal[
        "PRIMITIVE_UNSPECIFIED", "STRING", "VARIES", "UNESCAPED_STRING"
    ]
    fields: typing.List[Field]
    name: str

class ListConsentsResponse(typing_extensions.TypedDict, total=False):
    consents: typing.List[Consent]
    nextPageToken: str

class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: typing.List[str]

class ListConsentStoresResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    consentStores: typing.List[ConsentStore]

class ListAnnotationStoresResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    annotationStores: typing.List[AnnotationStore]

class Detail(typing_extensions.TypedDict, total=False):
    findings: typing.List[Finding]

class Vertex(typing_extensions.TypedDict, total=False):
    x: float
    y: float

class TextConfig(typing_extensions.TypedDict, total=False):
    transformations: typing.List[InfoTypeTransformation]

class Annotation(typing_extensions.TypedDict, total=False):
    imageAnnotation: ImageAnnotation
    resourceAnnotation: ResourceAnnotation
    textAnnotation: SensitiveTextAnnotation
    name: str
    customData: typing.Dict[str, typing.Any]
    annotationSource: AnnotationSource

class AnnotationConfig(typing_extensions.TypedDict, total=False):
    storeQuote: bool
    annotationStoreName: str

class ConsentEvaluation(typing_extensions.TypedDict, total=False):
    evaluationResult: typing_extensions.Literal[
        "EVALUATION_RESULT_UNSPECIFIED",
        "NOT_APPLICABLE",
        "NO_MATCHING_POLICY",
        "NO_SATISFIED_POLICY",
        "HAS_SATISFIED_POLICY",
    ]

class GoogleCloudHealthcareV1beta1DeidentifyDeidentifyDicomStoreSummary(
    typing_extensions.TypedDict, total=False
):
    failureResourceCount: str
    successResourceCount: str

class SchemaConfig(typing_extensions.TypedDict, total=False):
    schemaType: typing_extensions.Literal[
        "SCHEMA_TYPE_UNSPECIFIED", "LOSSLESS", "ANALYTICS"
    ]
    recursiveStructureDepth: str

class DicomFilterConfig(typing_extensions.TypedDict, total=False):
    resourcePathsGcsUri: str

class EvaluateUserConsentsRequest(typing_extensions.TypedDict, total=False):
    requestAttributes: typing.Dict[str, typing.Any]
    consentList: ConsentList
    resourceAttributes: typing.Dict[str, typing.Any]
    pageToken: str
    pageSize: int
    responseView: typing_extensions.Literal[
        "RESPONSE_VIEW_UNSPECIFIED", "BASIC", "FULL"
    ]
    userId: str

class ImportDicomDataErrorDetails(typing_extensions.TypedDict, total=False):
    sampleErrors: typing.List[ErrorDetail]

class DeidentifyErrorDetails(typing_extensions.TypedDict, total=False):
    successResourceCount: str
    failureResourceCount: str
    successStoreCount: str
    failureStoreCount: str

class ExportDicomDataResponse(typing_extensions.TypedDict, total=False): ...

class FhirFilter(typing_extensions.TypedDict, total=False):
    resources: Resources

class GoogleCloudHealthcareV1beta1DicomGcsSource(
    typing_extensions.TypedDict, total=False
):
    uri: str

class DeidentifyDicomStoreRequest(typing_extensions.TypedDict, total=False):
    config: DeidentifyConfig
    filterConfig: DicomFilterConfig
    destinationStore: str

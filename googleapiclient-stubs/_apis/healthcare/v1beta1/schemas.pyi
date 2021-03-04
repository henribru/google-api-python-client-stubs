import typing

import typing_extensions
@typing.type_check_only
class ActivateConsentRequest(typing_extensions.TypedDict, total=False):
    consentArtifact: str
    expireTime: str
    ttl: str

@typing.type_check_only
class AnalyzeEntitiesRequest(typing_extensions.TypedDict, total=False):
    documentContent: str

@typing.type_check_only
class AnalyzeEntitiesResponse(typing_extensions.TypedDict, total=False):
    entities: typing.List[Entity]
    entityMentions: typing.List[EntityMention]
    relationships: typing.List[EntityMentionRelationship]

@typing.type_check_only
class Annotation(typing_extensions.TypedDict, total=False):
    annotationSource: AnnotationSource
    customData: typing.Dict[str, typing.Any]
    imageAnnotation: ImageAnnotation
    name: str
    resourceAnnotation: ResourceAnnotation
    textAnnotation: SensitiveTextAnnotation

@typing.type_check_only
class AnnotationConfig(typing_extensions.TypedDict, total=False):
    annotationStoreName: str
    storeQuote: bool

@typing.type_check_only
class AnnotationSource(typing_extensions.TypedDict, total=False):
    cloudHealthcareSource: CloudHealthcareSource

@typing.type_check_only
class AnnotationStore(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    name: str

@typing.type_check_only
class ArchiveUserDataMappingRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ArchiveUserDataMappingResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Attribute(typing_extensions.TypedDict, total=False):
    attributeDefinitionId: str
    values: typing.List[str]

@typing.type_check_only
class AttributeDefinition(typing_extensions.TypedDict, total=False):
    allowedValues: typing.List[str]
    category: typing_extensions.Literal["CATEGORY_UNSPECIFIED", "RESOURCE", "REQUEST"]
    consentDefaultValues: typing.List[str]
    dataMappingDefaultValue: str
    description: str
    name: str

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
class BatchGetMessagesResponse(typing_extensions.TypedDict, total=False):
    messages: typing.List[Message]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: typing.List[str]
    role: str

@typing.type_check_only
class BoundingPoly(typing_extensions.TypedDict, total=False):
    label: str
    vertices: typing.List[Vertex]

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CharacterMaskConfig(typing_extensions.TypedDict, total=False):
    maskingCharacter: str

@typing.type_check_only
class CheckDataAccessRequest(typing_extensions.TypedDict, total=False):
    consentList: ConsentList
    dataId: str
    requestAttributes: typing.Dict[str, typing.Any]
    responseView: typing_extensions.Literal[
        "RESPONSE_VIEW_UNSPECIFIED", "BASIC", "FULL"
    ]

@typing.type_check_only
class CheckDataAccessResponse(typing_extensions.TypedDict, total=False):
    consentDetails: typing.Dict[str, typing.Any]
    consented: bool

@typing.type_check_only
class CloudHealthcareSource(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class Consent(typing_extensions.TypedDict, total=False):
    consentArtifact: str
    expireTime: str
    metadata: typing.Dict[str, typing.Any]
    name: str
    policies: typing.List[GoogleCloudHealthcareV1beta1ConsentPolicy]
    revisionCreateTime: str
    revisionId: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "ARCHIVED", "REVOKED", "DRAFT", "REJECTED"
    ]
    ttl: str
    userId: str

@typing.type_check_only
class ConsentArtifact(typing_extensions.TypedDict, total=False):
    consentContentScreenshots: typing.List[Image]
    consentContentVersion: str
    guardianSignature: Signature
    metadata: typing.Dict[str, typing.Any]
    name: str
    userId: str
    userSignature: Signature
    witnessSignature: Signature

@typing.type_check_only
class ConsentEvaluation(typing_extensions.TypedDict, total=False):
    evaluationResult: typing_extensions.Literal[
        "EVALUATION_RESULT_UNSPECIFIED",
        "NOT_APPLICABLE",
        "NO_MATCHING_POLICY",
        "NO_SATISFIED_POLICY",
        "HAS_SATISFIED_POLICY",
    ]

@typing.type_check_only
class ConsentList(typing_extensions.TypedDict, total=False):
    consents: typing.List[str]

@typing.type_check_only
class ConsentStore(typing_extensions.TypedDict, total=False):
    defaultConsentTtl: str
    enableConsentCreateOnUpdate: bool
    labels: typing.Dict[str, typing.Any]
    name: str

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
    annotation: AnnotationConfig
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
class Detail(typing_extensions.TypedDict, total=False):
    findings: typing.List[Finding]

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
    streamConfigs: typing.List[GoogleCloudHealthcareV1beta1DicomStreamConfig]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Entity(typing_extensions.TypedDict, total=False):
    entityId: str
    preferredTerm: str
    vocabularyCodes: typing.List[str]

@typing.type_check_only
class EntityMention(typing_extensions.TypedDict, total=False):
    certaintyAssessment: Feature
    confidence: float
    linkedEntities: typing.List[LinkedEntity]
    mentionId: str
    subject: Feature
    temporalAssessment: Feature
    text: TextSpan
    type: str

@typing.type_check_only
class EntityMentionRelationship(typing_extensions.TypedDict, total=False):
    confidence: float
    objectId: str
    subjectId: str

@typing.type_check_only
class EvaluateAnnotationStoreRequest(typing_extensions.TypedDict, total=False):
    bigqueryDestination: GoogleCloudHealthcareV1beta1AnnotationBigQueryDestination
    evalInfoTypeMapping: typing.Dict[str, typing.Any]
    goldenInfoTypeMapping: typing.Dict[str, typing.Any]
    goldenStore: str
    infoTypeConfig: InfoTypeConfig

@typing.type_check_only
class EvaluateAnnotationStoreResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EvaluateUserConsentsRequest(typing_extensions.TypedDict, total=False):
    consentList: ConsentList
    pageSize: int
    pageToken: str
    requestAttributes: typing.Dict[str, typing.Any]
    resourceAttributes: typing.Dict[str, typing.Any]
    responseView: typing_extensions.Literal[
        "RESPONSE_VIEW_UNSPECIFIED", "BASIC", "FULL"
    ]
    userId: str

@typing.type_check_only
class EvaluateUserConsentsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    results: typing.List[Result]

@typing.type_check_only
class ExportAnnotationsRequest(typing_extensions.TypedDict, total=False):
    bigqueryDestination: GoogleCloudHealthcareV1beta1AnnotationBigQueryDestination
    gcsDestination: GoogleCloudHealthcareV1beta1AnnotationGcsDestination

@typing.type_check_only
class ExportAnnotationsResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExportDicomDataRequest(typing_extensions.TypedDict, total=False):
    bigqueryDestination: GoogleCloudHealthcareV1beta1DicomBigQueryDestination
    filterConfig: DicomFilterConfig
    gcsDestination: GoogleCloudHealthcareV1beta1DicomGcsDestination

@typing.type_check_only
class ExportDicomDataResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExportMessagesRequest(typing_extensions.TypedDict, total=False):
    endTime: str
    gcsDestination: GcsDestination
    startTime: str

@typing.type_check_only
class ExportResourcesRequest(typing_extensions.TypedDict, total=False):
    _since: str
    _type: str
    bigqueryDestination: GoogleCloudHealthcareV1beta1FhirBigQueryDestination
    gcsDestination: GoogleCloudHealthcareV1beta1FhirGcsDestination

@typing.type_check_only
class Expr(typing_extensions.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Feature(typing_extensions.TypedDict, total=False):
    confidence: float
    value: str

@typing.type_check_only
class FhirConfig(typing_extensions.TypedDict, total=False):
    fieldMetadataList: typing.List[FieldMetadata]

@typing.type_check_only
class FhirFilter(typing_extensions.TypedDict, total=False):
    resources: Resources

@typing.type_check_only
class FhirStore(typing_extensions.TypedDict, total=False):
    defaultSearchHandlingStrict: bool
    disableReferentialIntegrity: bool
    disableResourceVersioning: bool
    enableUpdateCreate: bool
    labels: typing.Dict[str, typing.Any]
    name: str
    notificationConfig: NotificationConfig
    streamConfigs: typing.List[StreamConfig]
    validationConfig: ValidationConfig
    version: typing_extensions.Literal["VERSION_UNSPECIFIED", "DSTU2", "STU3", "R4"]

@typing.type_check_only
class Field(typing_extensions.TypedDict, total=False):
    maxOccurs: int
    minOccurs: int
    name: str
    table: str
    type: str

@typing.type_check_only
class FieldMetadata(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal[
        "ACTION_UNSPECIFIED", "TRANSFORM", "INSPECT_AND_TRANSFORM", "DO_NOT_TRANSFORM"
    ]
    paths: typing.List[str]

@typing.type_check_only
class FilterList(typing_extensions.TypedDict, total=False):
    infoTypes: typing.List[str]

@typing.type_check_only
class Finding(typing_extensions.TypedDict, total=False):
    end: str
    infoType: str
    quote: str
    start: str

@typing.type_check_only
class GcsDestination(typing_extensions.TypedDict, total=False):
    contentStructure: typing_extensions.Literal[
        "CONTENT_STRUCTURE_UNSPECIFIED", "MESSAGE_JSON"
    ]
    messageView: typing_extensions.Literal[
        "MESSAGE_VIEW_UNSPECIFIED",
        "RAW_ONLY",
        "PARSED_ONLY",
        "FULL",
        "SCHEMATIZED_ONLY",
        "BASIC",
    ]
    uriPrefix: str

@typing.type_check_only
class GcsSource(typing_extensions.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudHealthcareV1beta1AnnotationBigQueryDestination(
    typing_extensions.TypedDict, total=False
):
    force: bool
    schemaType: typing_extensions.Literal["SCHEMA_TYPE_UNSPECIFIED", "SIMPLE"]
    tableUri: str
    writeDisposition: typing_extensions.Literal[
        "WRITE_DISPOSITION_UNSPECIFIED", "WRITE_EMPTY", "WRITE_TRUNCATE", "WRITE_APPEND"
    ]

@typing.type_check_only
class GoogleCloudHealthcareV1beta1AnnotationGcsDestination(
    typing_extensions.TypedDict, total=False
):
    uriPrefix: str

@typing.type_check_only
class GoogleCloudHealthcareV1beta1AnnotationGcsSource(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudHealthcareV1beta1ConsentGcsDestination(
    typing_extensions.TypedDict, total=False
):
    uriPrefix: str

@typing.type_check_only
class GoogleCloudHealthcareV1beta1ConsentPolicy(
    typing_extensions.TypedDict, total=False
):
    authorizationRule: Expr
    resourceAttributes: typing.List[Attribute]

@typing.type_check_only
class GoogleCloudHealthcareV1beta1DeidentifyDeidentifyDicomStoreSummary(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudHealthcareV1beta1DeidentifyDeidentifyFhirStoreSummary(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudHealthcareV1beta1DicomBigQueryDestination(
    typing_extensions.TypedDict, total=False
):
    force: bool
    tableUri: str
    writeDisposition: typing_extensions.Literal[
        "WRITE_DISPOSITION_UNSPECIFIED", "WRITE_EMPTY", "WRITE_TRUNCATE", "WRITE_APPEND"
    ]

@typing.type_check_only
class GoogleCloudHealthcareV1beta1DicomGcsDestination(
    typing_extensions.TypedDict, total=False
):
    mimeType: str
    uriPrefix: str

@typing.type_check_only
class GoogleCloudHealthcareV1beta1DicomGcsSource(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudHealthcareV1beta1DicomStreamConfig(
    typing_extensions.TypedDict, total=False
):
    bigqueryDestination: GoogleCloudHealthcareV1beta1DicomBigQueryDestination

@typing.type_check_only
class GoogleCloudHealthcareV1beta1FhirBigQueryDestination(
    typing_extensions.TypedDict, total=False
):
    datasetUri: str
    force: bool
    schemaConfig: SchemaConfig
    writeDisposition: typing_extensions.Literal[
        "WRITE_DISPOSITION_UNSPECIFIED", "WRITE_EMPTY", "WRITE_TRUNCATE", "WRITE_APPEND"
    ]

@typing.type_check_only
class GoogleCloudHealthcareV1beta1FhirExportResourcesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudHealthcareV1beta1FhirGcsDestination(
    typing_extensions.TypedDict, total=False
):
    uriPrefix: str

@typing.type_check_only
class GoogleCloudHealthcareV1beta1FhirGcsSource(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleCloudHealthcareV1beta1FhirImportResourcesResponse(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GroupOrSegment(typing_extensions.TypedDict, total=False):
    group: SchemaGroup
    segment: SchemaSegment

@typing.type_check_only
class Hl7SchemaConfig(typing_extensions.TypedDict, total=False):
    messageSchemaConfigs: typing.Dict[str, typing.Any]
    version: typing.List[VersionSource]

@typing.type_check_only
class Hl7TypesConfig(typing_extensions.TypedDict, total=False):
    type: typing.List[Type]
    version: typing.List[VersionSource]

@typing.type_check_only
class Hl7V2NotificationConfig(typing_extensions.TypedDict, total=False):
    filter: str
    pubsubTopic: str

@typing.type_check_only
class Hl7V2Store(typing_extensions.TypedDict, total=False):
    labels: typing.Dict[str, typing.Any]
    name: str
    notificationConfig: NotificationConfig
    notificationConfigs: typing.List[Hl7V2NotificationConfig]
    parserConfig: ParserConfig
    rejectDuplicateMessage: bool

@typing.type_check_only
class HttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: typing.List[typing.Dict[str, typing.Any]]

@typing.type_check_only
class Image(typing_extensions.TypedDict, total=False):
    gcsUri: str
    rawBytes: str

@typing.type_check_only
class ImageAnnotation(typing_extensions.TypedDict, total=False):
    boundingPolys: typing.List[BoundingPoly]
    frameIndex: int

@typing.type_check_only
class ImageConfig(typing_extensions.TypedDict, total=False):
    textRedactionMode: typing_extensions.Literal[
        "TEXT_REDACTION_MODE_UNSPECIFIED",
        "REDACT_ALL_TEXT",
        "REDACT_SENSITIVE_TEXT",
        "REDACT_NO_TEXT",
    ]

@typing.type_check_only
class ImportAnnotationsRequest(typing_extensions.TypedDict, total=False):
    gcsSource: GoogleCloudHealthcareV1beta1AnnotationGcsSource

@typing.type_check_only
class ImportAnnotationsResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ImportDicomDataRequest(typing_extensions.TypedDict, total=False):
    gcsSource: GoogleCloudHealthcareV1beta1DicomGcsSource

@typing.type_check_only
class ImportDicomDataResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ImportMessagesRequest(typing_extensions.TypedDict, total=False):
    gcsSource: GcsSource

@typing.type_check_only
class ImportMessagesResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ImportResourcesRequest(typing_extensions.TypedDict, total=False):
    contentStructure: typing_extensions.Literal[
        "CONTENT_STRUCTURE_UNSPECIFIED",
        "BUNDLE",
        "RESOURCE",
        "BUNDLE_PRETTY",
        "RESOURCE_PRETTY",
    ]
    gcsSource: GoogleCloudHealthcareV1beta1FhirGcsSource

@typing.type_check_only
class InfoTypeConfig(typing_extensions.TypedDict, total=False):
    evaluateList: FilterList
    ignoreList: FilterList
    strictMatching: bool

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
class LinkedEntity(typing_extensions.TypedDict, total=False):
    entityId: str

@typing.type_check_only
class ListAnnotationStoresResponse(typing_extensions.TypedDict, total=False):
    annotationStores: typing.List[AnnotationStore]
    nextPageToken: str

@typing.type_check_only
class ListAnnotationsResponse(typing_extensions.TypedDict, total=False):
    annotations: typing.List[Annotation]
    nextPageToken: str

@typing.type_check_only
class ListAttributeDefinitionsResponse(typing_extensions.TypedDict, total=False):
    attributeDefinitions: typing.List[AttributeDefinition]
    nextPageToken: str

@typing.type_check_only
class ListConsentArtifactsResponse(typing_extensions.TypedDict, total=False):
    consentArtifacts: typing.List[ConsentArtifact]
    nextPageToken: str

@typing.type_check_only
class ListConsentRevisionsResponse(typing_extensions.TypedDict, total=False):
    consents: typing.List[Consent]
    nextPageToken: str

@typing.type_check_only
class ListConsentStoresResponse(typing_extensions.TypedDict, total=False):
    consentStores: typing.List[ConsentStore]
    nextPageToken: str

@typing.type_check_only
class ListConsentsResponse(typing_extensions.TypedDict, total=False):
    consents: typing.List[Consent]
    nextPageToken: str

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
class ListUserDataMappingsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    userDataMappings: typing.List[UserDataMapping]

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
    schematizedData: SchematizedData
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
    schema: SchemaPackage
    segmentTerminator: str
    version: typing_extensions.Literal["PARSER_VERSION_UNSPECIFIED", "V1", "V2"]

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
class QueryAccessibleDataRequest(typing_extensions.TypedDict, total=False):
    gcsDestination: GoogleCloudHealthcareV1beta1ConsentGcsDestination
    requestAttributes: typing.Dict[str, typing.Any]
    resourceAttributes: typing.Dict[str, typing.Any]

@typing.type_check_only
class RedactConfig(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RejectConsentRequest(typing_extensions.TypedDict, total=False):
    consentArtifact: str

@typing.type_check_only
class ReplaceWithInfoTypeConfig(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ResourceAnnotation(typing_extensions.TypedDict, total=False):
    label: str

@typing.type_check_only
class Resources(typing_extensions.TypedDict, total=False):
    resources: typing.List[str]

@typing.type_check_only
class Result(typing_extensions.TypedDict, total=False):
    consentDetails: typing.Dict[str, typing.Any]
    consented: bool
    dataId: str

@typing.type_check_only
class RevokeConsentRequest(typing_extensions.TypedDict, total=False):
    consentArtifact: str

@typing.type_check_only
class SchemaConfig(typing_extensions.TypedDict, total=False):
    recursiveStructureDepth: str
    schemaType: typing_extensions.Literal[
        "SCHEMA_TYPE_UNSPECIFIED", "LOSSLESS", "ANALYTICS"
    ]

@typing.type_check_only
class SchemaGroup(typing.Dict[str, typing.Any]): ...

@typing.type_check_only
class SchemaPackage(typing_extensions.TypedDict, total=False):
    ignoreMinOccurs: bool
    schemas: typing.List[Hl7SchemaConfig]
    schematizedParsingType: typing_extensions.Literal[
        "SCHEMATIZED_PARSING_TYPE_UNSPECIFIED", "SOFT_FAIL", "HARD_FAIL"
    ]
    types: typing.List[Hl7TypesConfig]
    unexpectedSegmentHandling: typing_extensions.Literal[
        "UNEXPECTED_SEGMENT_HANDLING_MODE_UNSPECIFIED", "FAIL", "SKIP", "PARSE"
    ]

@typing.type_check_only
class SchemaSegment(typing_extensions.TypedDict, total=False):
    maxOccurs: int
    minOccurs: int
    type: str

@typing.type_check_only
class SchematizedData(typing_extensions.TypedDict, total=False):
    data: str
    error: str

@typing.type_check_only
class SearchResourcesRequest(typing_extensions.TypedDict, total=False):
    resourceType: str

@typing.type_check_only
class Segment(typing_extensions.TypedDict, total=False):
    fields: typing.Dict[str, typing.Any]
    segmentId: str
    setId: str

@typing.type_check_only
class SensitiveTextAnnotation(typing_extensions.TypedDict, total=False):
    details: typing.Dict[str, typing.Any]

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Signature(typing_extensions.TypedDict, total=False):
    image: Image
    metadata: typing.Dict[str, typing.Any]
    signatureTime: str
    userId: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StreamConfig(typing_extensions.TypedDict, total=False):
    bigqueryDestination: GoogleCloudHealthcareV1beta1FhirBigQueryDestination
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

@typing.type_check_only
class TextSpan(typing_extensions.TypedDict, total=False):
    beginOffset: int
    content: str

@typing.type_check_only
class Type(typing_extensions.TypedDict, total=False):
    fields: typing.List[Field]
    name: str
    primitive: typing_extensions.Literal[
        "PRIMITIVE_UNSPECIFIED", "STRING", "VARIES", "UNESCAPED_STRING"
    ]

@typing.type_check_only
class UserDataMapping(typing_extensions.TypedDict, total=False):
    archiveTime: str
    archived: bool
    dataId: str
    name: str
    resourceAttributes: typing.List[Attribute]
    userId: str

@typing.type_check_only
class ValidationConfig(typing_extensions.TypedDict, total=False):
    disableProfileValidation: bool
    enabledImplementationGuides: typing.List[str]

@typing.type_check_only
class VersionSource(typing_extensions.TypedDict, total=False):
    mshField: str
    value: str

@typing.type_check_only
class Vertex(typing_extensions.TypedDict, total=False):
    x: float
    y: float

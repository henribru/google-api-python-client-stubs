import typing

import typing_extensions

_list = list

@typing.type_check_only
class AccessDeterminationLogConfig(typing_extensions.TypedDict, total=False):
    logLevel: typing_extensions.Literal[
        "LOG_LEVEL_UNSPECIFIED", "DISABLED", "MINIMUM", "VERBOSE"
    ]

@typing.type_check_only
class Action(typing_extensions.TypedDict, total=False):
    cleanImageTag: ImageConfig
    cleanTextTag: CleanTextTag
    deleteTag: DeleteTag
    keepTag: KeepTag
    queries: _list[str]
    recurseTag: RecurseTag
    regenUidTag: RegenUidTag
    removeTag: RemoveTag
    resetTag: ResetTag

@typing.type_check_only
class ActivateConsentRequest(typing_extensions.TypedDict, total=False):
    consentArtifact: str
    expireTime: str
    ttl: str

@typing.type_check_only
class AdminConsents(typing_extensions.TypedDict, total=False):
    names: _list[str]

@typing.type_check_only
class AnalyzeEntitiesRequest(typing_extensions.TypedDict, total=False):
    alternativeOutputFormat: typing_extensions.Literal[
        "ALTERNATIVE_OUTPUT_FORMAT_UNSPECIFIED", "FHIR_BUNDLE"
    ]
    documentContent: str
    licensedVocabularies: _list[
        typing_extensions.Literal[
            "LICENSED_VOCABULARY_UNSPECIFIED", "ICD10CM", "SNOMEDCT_US"
        ]
    ]

@typing.type_check_only
class AnalyzeEntitiesResponse(typing_extensions.TypedDict, total=False):
    entities: _list[Entity]
    entityMentions: _list[EntityMention]
    fhirBundle: str
    relationships: _list[EntityMentionRelationship]

@typing.type_check_only
class ApplyAdminConsentsErrorDetail(typing_extensions.TypedDict, total=False):
    consentErrors: _list[ConsentErrors]
    existingOperationId: str

@typing.type_check_only
class ApplyAdminConsentsRequest(typing_extensions.TypedDict, total=False):
    newConsentsList: AdminConsents
    validateOnly: bool

@typing.type_check_only
class ApplyAdminConsentsResponse(typing_extensions.TypedDict, total=False):
    affectedResources: str
    consentApplySuccess: str
    failedResources: str

@typing.type_check_only
class ApplyConsentsRequest(typing_extensions.TypedDict, total=False):
    patientScope: PatientScope
    timeRange: TimeRange
    validateOnly: bool

@typing.type_check_only
class ApplyConsentsResponse(typing_extensions.TypedDict, total=False):
    affectedResources: str
    consentApplyFailure: str
    consentApplySuccess: str
    failedResources: str

@typing.type_check_only
class ArchiveUserDataMappingRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ArchiveUserDataMappingResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Attribute(typing_extensions.TypedDict, total=False):
    attributeDefinitionId: str
    values: _list[str]

@typing.type_check_only
class AttributeDefinition(typing_extensions.TypedDict, total=False):
    allowedValues: _list[str]
    category: typing_extensions.Literal["CATEGORY_UNSPECIFIED", "RESOURCE", "REQUEST"]
    consentDefaultValues: _list[str]
    dataMappingDefaultValue: str
    description: str
    name: str

@typing.type_check_only
class AuditConfig(typing_extensions.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing_extensions.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing_extensions.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class BatchGetMessagesResponse(typing_extensions.TypedDict, total=False):
    messages: _list[Message]

@typing.type_check_only
class Binding(typing_extensions.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BlobStorageInfo(typing_extensions.TypedDict, total=False):
    sizeBytes: str
    storageClass: typing_extensions.Literal[
        "BLOB_STORAGE_CLASS_UNSPECIFIED", "STANDARD", "NEARLINE", "COLDLINE", "ARCHIVE"
    ]
    storageClassUpdateTime: str

@typing.type_check_only
class BlobStorageSettings(typing_extensions.TypedDict, total=False):
    blobStorageClass: typing_extensions.Literal[
        "BLOB_STORAGE_CLASS_UNSPECIFIED", "STANDARD", "NEARLINE", "COLDLINE", "ARCHIVE"
    ]

@typing.type_check_only
class BulkExportGcsDestination(typing_extensions.TypedDict, total=False):
    uriPrefix: str

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CharacterMaskConfig(typing_extensions.TypedDict, total=False):
    maskingCharacter: str

@typing.type_check_only
class CharacterMaskField(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CheckDataAccessRequest(typing_extensions.TypedDict, total=False):
    consentList: ConsentList
    dataId: str
    requestAttributes: dict[str, typing.Any]
    responseView: typing_extensions.Literal[
        "RESPONSE_VIEW_UNSPECIFIED", "BASIC", "FULL"
    ]

@typing.type_check_only
class CheckDataAccessResponse(typing_extensions.TypedDict, total=False):
    consentDetails: dict[str, typing.Any]
    consented: bool

@typing.type_check_only
class CleanDescriptorsOption(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CleanTextField(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CleanTextTag(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ConfigureSearchRequest(typing_extensions.TypedDict, total=False):
    canonicalUrls: _list[str]
    validateOnly: bool

@typing.type_check_only
class Consent(typing_extensions.TypedDict, total=False):
    consentArtifact: str
    expireTime: str
    metadata: dict[str, typing.Any]
    name: str
    policies: _list[GoogleCloudHealthcareV1beta1ConsentPolicy]
    revisionCreateTime: str
    revisionId: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "ARCHIVED", "REVOKED", "DRAFT", "REJECTED"
    ]
    ttl: str
    userId: str

@typing.type_check_only
class ConsentAccessorScope(typing_extensions.TypedDict, total=False):
    actor: str
    environment: str
    purpose: str

@typing.type_check_only
class ConsentArtifact(typing_extensions.TypedDict, total=False):
    consentContentScreenshots: _list[Image]
    consentContentVersion: str
    guardianSignature: Signature
    metadata: dict[str, typing.Any]
    name: str
    userId: str
    userSignature: Signature
    witnessSignature: Signature

@typing.type_check_only
class ConsentConfig(typing_extensions.TypedDict, total=False):
    accessDeterminationLogConfig: AccessDeterminationLogConfig
    accessEnforced: bool
    consentHeaderHandling: ConsentHeaderHandling
    enforcedAdminConsents: _list[str]
    version: typing_extensions.Literal["CONSENT_ENFORCEMENT_VERSION_UNSPECIFIED", "V1"]

@typing.type_check_only
class ConsentErrors(typing_extensions.TypedDict, total=False):
    error: Status
    name: str

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
class ConsentHeaderHandling(typing_extensions.TypedDict, total=False):
    profile: typing_extensions.Literal[
        "SCOPE_PROFILE_UNSPECIFIED", "PERMIT_EMPTY_SCOPE", "REQUIRED_ON_READ"
    ]

@typing.type_check_only
class ConsentList(typing_extensions.TypedDict, total=False):
    consents: _list[str]

@typing.type_check_only
class ConsentStore(typing_extensions.TypedDict, total=False):
    defaultConsentTtl: str
    enableConsentCreateOnUpdate: bool
    labels: dict[str, typing.Any]
    name: str

@typing.type_check_only
class ContextualDeidConfig(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CreateMessageRequest(typing_extensions.TypedDict, total=False):
    message: Message

@typing.type_check_only
class CryptoHashConfig(typing_extensions.TypedDict, total=False):
    cryptoKey: str
    kmsWrapped: KmsWrappedCryptoKey

@typing.type_check_only
class CryptoHashField(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Dataset(typing_extensions.TypedDict, total=False):
    encryptionSpec: EncryptionSpec
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    timeZone: str

@typing.type_check_only
class DateShiftConfig(typing_extensions.TypedDict, total=False):
    cryptoKey: str
    kmsWrapped: KmsWrappedCryptoKey

@typing.type_check_only
class DateShiftField(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeidentifiedStoreDestination(typing_extensions.TypedDict, total=False):
    config: DeidentifyConfig
    store: str

@typing.type_check_only
class DeidentifyConfig(typing_extensions.TypedDict, total=False):
    dicom: DicomConfig
    dicomTagConfig: DicomTagConfig
    fhir: FhirConfig
    fhirFieldConfig: FhirFieldConfig
    image: ImageConfig
    operationMetadata: DeidentifyOperationMetadata
    text: TextConfig
    useRegionalDataProcessing: bool

@typing.type_check_only
class DeidentifyDatasetRequest(typing_extensions.TypedDict, total=False):
    config: DeidentifyConfig
    destinationDataset: str
    gcsConfigUri: str

@typing.type_check_only
class DeidentifyDicomStoreRequest(typing_extensions.TypedDict, total=False):
    config: DeidentifyConfig
    destinationStore: str
    filterConfig: DicomFilterConfig
    gcsConfigUri: str

@typing.type_check_only
class DeidentifyFhirStoreRequest(typing_extensions.TypedDict, total=False):
    config: DeidentifyConfig
    destinationStore: str
    gcsConfigUri: str
    resourceFilter: FhirFilter
    skipModifiedResources: bool

@typing.type_check_only
class DeidentifyOperationMetadata(typing_extensions.TypedDict, total=False):
    fhirOutput: FhirOutput

@typing.type_check_only
class DeidentifySummary(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class DeleteTag(typing_extensions.TypedDict, total=False): ...

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
    labels: dict[str, typing.Any]
    name: str
    notificationConfig: NotificationConfig
    streamConfigs: _list[GoogleCloudHealthcareV1beta1DicomStreamConfig]

@typing.type_check_only
class DicomStoreMetrics(typing_extensions.TypedDict, total=False):
    blobStorageSizeBytes: str
    instanceCount: str
    name: str
    seriesCount: str
    structuredStorageSizeBytes: str
    studyCount: str

@typing.type_check_only
class DicomTagConfig(typing_extensions.TypedDict, total=False):
    actions: _list[Action]
    options: Options
    profileType: typing_extensions.Literal[
        "PROFILE_TYPE_UNSPECIFIED",
        "MINIMAL_KEEP_LIST_PROFILE",
        "ATTRIBUTE_CONFIDENTIALITY_BASIC_PROFILE",
        "KEEP_ALL_PROFILE",
        "DEIDENTIFY_TAG_CONTENTS",
    ]

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionSpec(typing_extensions.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class Entity(typing_extensions.TypedDict, total=False):
    entityId: str
    preferredTerm: str
    vocabularyCodes: _list[str]

@typing.type_check_only
class EntityMention(typing_extensions.TypedDict, total=False):
    additionalInfo: _list[Feature]
    certaintyAssessment: Feature
    confidence: float
    linkedEntities: _list[LinkedEntity]
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
class EvaluateUserConsentsRequest(typing_extensions.TypedDict, total=False):
    consentList: ConsentList
    pageSize: int
    pageToken: str
    requestAttributes: dict[str, typing.Any]
    resourceAttributes: dict[str, typing.Any]
    responseView: typing_extensions.Literal[
        "RESPONSE_VIEW_UNSPECIFIED", "BASIC", "FULL"
    ]
    userId: str

@typing.type_check_only
class EvaluateUserConsentsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    results: _list[Result]

@typing.type_check_only
class ExplainDataAccessConsentInfo(typing_extensions.TypedDict, total=False):
    cascadeOrigins: _list[str]
    consentResource: str
    enforcementTime: str
    matchingAccessorScopes: _list[ConsentAccessorScope]
    patientConsentOwner: str
    type: typing_extensions.Literal[
        "CONSENT_POLICY_TYPE_UNSPECIFIED",
        "CONSENT_POLICY_TYPE_PATIENT",
        "CONSENT_POLICY_TYPE_ADMIN",
    ]
    variants: _list[
        typing_extensions.Literal[
            "CONSENT_VARIANT_UNSPECIFIED",
            "CONSENT_VARIANT_STANDARD",
            "CONSENT_VARIANT_CASCADE",
        ]
    ]

@typing.type_check_only
class ExplainDataAccessConsentScope(typing_extensions.TypedDict, total=False):
    accessorScope: ConsentAccessorScope
    decision: typing_extensions.Literal[
        "CONSENT_DECISION_TYPE_UNSPECIFIED",
        "CONSENT_DECISION_TYPE_PERMIT",
        "CONSENT_DECISION_TYPE_DENY",
    ]
    enforcingConsents: _list[ExplainDataAccessConsentInfo]
    exceptions: _list[ExplainDataAccessConsentScope]

@typing.type_check_only
class ExplainDataAccessResponse(typing_extensions.TypedDict, total=False):
    consentScopes: _list[ExplainDataAccessConsentScope]
    warning: str

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
    filter: str
    gcsDestination: GcsDestination
    pubsubDestination: PubsubDestination
    startTime: str

@typing.type_check_only
class ExportMessagesResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ExportResourcesHistoryRequest(typing_extensions.TypedDict, total=False):
    _since: str
    _type: str
    gcsDestination: GoogleCloudHealthcareV1beta1FhirGcsDestination
    maxResourceVersions: str

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
    defaultKeepExtensions: bool
    fieldMetadataList: _list[FieldMetadata]

@typing.type_check_only
class FhirFieldConfig(typing_extensions.TypedDict, total=False):
    fieldMetadataList: _list[GoogleCloudHealthcareV1beta1DeidentifyFieldMetadata]
    options: GoogleCloudHealthcareV1beta1DeidentifyOptions
    profileType: typing_extensions.Literal[
        "PROFILE_TYPE_UNSPECIFIED", "KEEP_ALL", "BASIC", "CLEAN_ALL"
    ]

@typing.type_check_only
class FhirFilter(typing_extensions.TypedDict, total=False):
    resources: Resources

@typing.type_check_only
class FhirNotificationConfig(typing_extensions.TypedDict, total=False):
    pubsubTopic: str
    sendFullResource: bool
    sendPreviousResourceOnDelete: bool

@typing.type_check_only
class FhirOutput(typing_extensions.TypedDict, total=False):
    fhirStore: str

@typing.type_check_only
class FhirStore(typing_extensions.TypedDict, total=False):
    bulkExportGcsDestination: BulkExportGcsDestination
    complexDataTypeReferenceParsing: typing_extensions.Literal[
        "COMPLEX_DATA_TYPE_REFERENCE_PARSING_UNSPECIFIED", "DISABLED", "ENABLED"
    ]
    consentConfig: ConsentConfig
    defaultSearchHandlingStrict: bool
    disableReferentialIntegrity: bool
    disableResourceVersioning: bool
    enableHistoryModifications: bool
    enableUpdateCreate: bool
    labels: dict[str, typing.Any]
    name: str
    notificationConfig: NotificationConfig
    notificationConfigs: _list[FhirNotificationConfig]
    searchConfig: SearchConfig
    streamConfigs: _list[StreamConfig]
    validationConfig: ValidationConfig
    version: typing_extensions.Literal[
        "VERSION_UNSPECIFIED", "DSTU2", "STU3", "R4", "R5"
    ]

@typing.type_check_only
class FhirStoreMetric(typing_extensions.TypedDict, total=False):
    count: str
    resourceType: str
    structuredStorageSizeBytes: str

@typing.type_check_only
class FhirStoreMetrics(typing_extensions.TypedDict, total=False):
    metrics: _list[FhirStoreMetric]
    name: str

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
    paths: _list[str]

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
class GoogleCloudHealthcareV1beta1ConsentGcsDestination(
    typing_extensions.TypedDict, total=False
):
    uriPrefix: str

@typing.type_check_only
class GoogleCloudHealthcareV1beta1ConsentPolicy(
    typing_extensions.TypedDict, total=False
):
    authorizationRule: Expr
    resourceAttributes: _list[Attribute]

@typing.type_check_only
class GoogleCloudHealthcareV1beta1DeidentifyDeidentifyDicomStoreSummary(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudHealthcareV1beta1DeidentifyDeidentifyFhirStoreSummary(
    typing_extensions.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudHealthcareV1beta1DeidentifyFieldMetadata(
    typing_extensions.TypedDict, total=False
):
    characterMaskField: CharacterMaskField
    cleanTextField: CleanTextField
    cryptoHashField: CryptoHashField
    dateShiftField: DateShiftField
    keepField: KeepField
    paths: _list[str]
    removeField: RemoveField

@typing.type_check_only
class GoogleCloudHealthcareV1beta1DeidentifyOptions(
    typing_extensions.TypedDict, total=False
):
    characterMaskConfig: CharacterMaskConfig
    contextualDeid: ContextualDeidConfig
    cryptoHashConfig: CryptoHashConfig
    dateShiftConfig: DateShiftConfig
    keepExtensions: KeepExtensionsConfig

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
    changeDataCaptureConfig: GoogleCloudHealthcareV1beta1FhirChangeDataCaptureConfig
    datasetUri: str
    force: bool
    schemaConfig: SchemaConfig
    writeDisposition: typing_extensions.Literal[
        "WRITE_DISPOSITION_UNSPECIFIED", "WRITE_EMPTY", "WRITE_TRUNCATE", "WRITE_APPEND"
    ]

@typing.type_check_only
class GoogleCloudHealthcareV1beta1FhirChangeDataCaptureConfig(
    typing_extensions.TypedDict, total=False
):
    historyMode: typing_extensions.Literal[
        "HISTORY_MODE_UNSPECIFIED", "KEEP_LATEST_VERSION", "KEEP_ALL_VERSIONS"
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
    messageSchemaConfigs: dict[str, typing.Any]
    version: _list[VersionSource]

@typing.type_check_only
class Hl7TypesConfig(typing_extensions.TypedDict, total=False):
    type: _list[Type]
    version: _list[VersionSource]

@typing.type_check_only
class Hl7V2NotificationConfig(typing_extensions.TypedDict, total=False):
    filter: str
    pubsubTopic: str

@typing.type_check_only
class Hl7V2Store(typing_extensions.TypedDict, total=False):
    labels: dict[str, typing.Any]
    name: str
    notificationConfig: NotificationConfig
    notificationConfigs: _list[Hl7V2NotificationConfig]
    parserConfig: ParserConfig
    rejectDuplicateMessage: bool

@typing.type_check_only
class Hl7V2StoreMetric(typing_extensions.TypedDict, total=False):
    count: str
    messageType: str
    structuredStorageSizeBytes: str

@typing.type_check_only
class Hl7V2StoreMetrics(typing_extensions.TypedDict, total=False):
    metrics: _list[Hl7V2StoreMetric]
    name: str

@typing.type_check_only
class HttpBody(typing_extensions.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class Image(typing_extensions.TypedDict, total=False):
    gcsUri: str
    rawBytes: str

@typing.type_check_only
class ImageConfig(typing_extensions.TypedDict, total=False):
    additionalInfoTypes: _list[str]
    excludeInfoTypes: _list[str]
    textRedactionMode: typing_extensions.Literal[
        "TEXT_REDACTION_MODE_UNSPECIFIED",
        "REDACT_ALL_TEXT",
        "REDACT_SENSITIVE_TEXT",
        "REDACT_NO_TEXT",
        "REDACT_SENSITIVE_TEXT_CLEAN_DESCRIPTORS",
    ]

@typing.type_check_only
class ImportDicomDataRequest(typing_extensions.TypedDict, total=False):
    blobStorageSettings: BlobStorageSettings
    gcsSource: GoogleCloudHealthcareV1beta1DicomGcsSource

@typing.type_check_only
class ImportDicomDataResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ImportMessagesRequest(typing_extensions.TypedDict, total=False):
    gcsSource: GcsSource

@typing.type_check_only
class ImportMessagesResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ImportResourcesHistoryRequest(typing_extensions.TypedDict, total=False):
    contentStructure: typing_extensions.Literal[
        "CONTENT_STRUCTURE_UNSPECIFIED",
        "BUNDLE",
        "RESOURCE",
        "BUNDLE_PRETTY",
        "RESOURCE_PRETTY",
    ]
    gcsSource: GoogleCloudHealthcareV1beta1FhirGcsSource
    maxErrorCount: str

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
class InfoTypeTransformation(typing_extensions.TypedDict, total=False):
    characterMaskConfig: CharacterMaskConfig
    cryptoHashConfig: CryptoHashConfig
    dateShiftConfig: DateShiftConfig
    infoTypes: _list[str]
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
class KeepExtensionsConfig(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class KeepField(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class KeepTag(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class KmsWrappedCryptoKey(typing_extensions.TypedDict, total=False):
    cryptoKey: str
    wrappedKey: str

@typing.type_check_only
class LinkedEntity(typing_extensions.TypedDict, total=False):
    entityId: str

@typing.type_check_only
class ListAttributeDefinitionsResponse(typing_extensions.TypedDict, total=False):
    attributeDefinitions: _list[AttributeDefinition]
    nextPageToken: str

@typing.type_check_only
class ListConsentArtifactsResponse(typing_extensions.TypedDict, total=False):
    consentArtifacts: _list[ConsentArtifact]
    nextPageToken: str

@typing.type_check_only
class ListConsentRevisionsResponse(typing_extensions.TypedDict, total=False):
    consents: _list[Consent]
    nextPageToken: str

@typing.type_check_only
class ListConsentStoresResponse(typing_extensions.TypedDict, total=False):
    consentStores: _list[ConsentStore]
    nextPageToken: str

@typing.type_check_only
class ListConsentsResponse(typing_extensions.TypedDict, total=False):
    consents: _list[Consent]
    nextPageToken: str

@typing.type_check_only
class ListDatasetsResponse(typing_extensions.TypedDict, total=False):
    datasets: _list[Dataset]
    nextPageToken: str

@typing.type_check_only
class ListDicomStoresResponse(typing_extensions.TypedDict, total=False):
    dicomStores: _list[DicomStore]
    nextPageToken: str

@typing.type_check_only
class ListFhirStoresResponse(typing_extensions.TypedDict, total=False):
    fhirStores: _list[FhirStore]
    nextPageToken: str

@typing.type_check_only
class ListHl7V2StoresResponse(typing_extensions.TypedDict, total=False):
    hl7V2Stores: _list[Hl7V2Store]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing_extensions.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMessagesResponse(typing_extensions.TypedDict, total=False):
    hl7V2Messages: _list[Message]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListUserDataMappingsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    userDataMappings: _list[UserDataMapping]

@typing.type_check_only
class Location(typing_extensions.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Message(typing_extensions.TypedDict, total=False):
    createTime: str
    data: str
    labels: dict[str, typing.Any]
    messageType: str
    name: str
    parsedData: ParsedData
    patientIds: _list[PatientId]
    schematizedData: SchematizedData
    sendFacility: str
    sendTime: str

@typing.type_check_only
class NotificationConfig(typing_extensions.TypedDict, total=False):
    pubsubTopic: str
    sendForBulkImport: bool

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing_extensions.TypedDict, total=False):
    apiMethodName: str
    cancelRequested: bool
    counter: ProgressCounter
    createTime: str
    endTime: str
    logsUrl: str

@typing.type_check_only
class Options(typing_extensions.TypedDict, total=False):
    cleanDescriptors: CleanDescriptorsOption
    cleanImage: ImageConfig
    primaryIds: typing_extensions.Literal[
        "PRIMARY_IDS_OPTION_UNSPECIFIED", "KEEP", "REGEN"
    ]

@typing.type_check_only
class ParsedData(typing_extensions.TypedDict, total=False):
    segments: _list[Segment]

@typing.type_check_only
class ParserConfig(typing_extensions.TypedDict, total=False):
    allowNullHeader: bool
    schema: SchemaPackage
    segmentTerminator: str
    version: typing_extensions.Literal["PARSER_VERSION_UNSPECIFIED", "V1", "V2", "V3"]

@typing.type_check_only
class PatientId(typing_extensions.TypedDict, total=False):
    type: str
    value: str

@typing.type_check_only
class PatientScope(typing_extensions.TypedDict, total=False):
    patientIds: _list[str]

@typing.type_check_only
class Policy(typing_extensions.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ProgressCounter(typing_extensions.TypedDict, total=False):
    failure: str
    pending: str
    secondaryFailure: str
    secondarySuccess: str
    success: str

@typing.type_check_only
class PubsubDestination(typing_extensions.TypedDict, total=False):
    pubsubTopic: str

@typing.type_check_only
class QueryAccessibleDataRequest(typing_extensions.TypedDict, total=False):
    gcsDestination: GoogleCloudHealthcareV1beta1ConsentGcsDestination
    requestAttributes: dict[str, typing.Any]
    resourceAttributes: dict[str, typing.Any]

@typing.type_check_only
class QueryAccessibleDataResponse(typing_extensions.TypedDict, total=False):
    gcsUris: _list[str]

@typing.type_check_only
class RecurseTag(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RedactConfig(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RegenUidTag(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RejectConsentRequest(typing_extensions.TypedDict, total=False):
    consentArtifact: str

@typing.type_check_only
class RemoveField(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class RemoveTag(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ReplaceWithInfoTypeConfig(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ResetTag(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Resources(typing_extensions.TypedDict, total=False):
    resources: _list[str]

@typing.type_check_only
class Result(typing_extensions.TypedDict, total=False):
    consentDetails: dict[str, typing.Any]
    consented: bool
    dataId: str

@typing.type_check_only
class RevokeConsentRequest(typing_extensions.TypedDict, total=False):
    consentArtifact: str

@typing.type_check_only
class RollbackFhirResourceFilteringFields(typing_extensions.TypedDict, total=False):
    metadataFilter: str
    operationIds: _list[str]

@typing.type_check_only
class RollbackFhirResourcesRequest(typing_extensions.TypedDict, total=False):
    changeType: typing_extensions.Literal[
        "CHANGE_TYPE_UNSPECIFIED", "ALL", "CREATE", "UPDATE", "DELETE"
    ]
    excludeRollbacks: bool
    filteringFields: RollbackFhirResourceFilteringFields
    force: bool
    inputGcsObject: str
    resultGcsBucket: str
    rollbackTime: str
    type: _list[str]

@typing.type_check_only
class RollbackFhirResourcesResponse(typing_extensions.TypedDict, total=False):
    fhirStore: str

@typing.type_check_only
class RollbackHL7MessagesFilteringFields(typing_extensions.TypedDict, total=False):
    operationIds: _list[str]

@typing.type_check_only
class RollbackHl7V2MessagesRequest(typing_extensions.TypedDict, total=False):
    changeType: typing_extensions.Literal[
        "CHANGE_TYPE_UNSPECIFIED", "ALL", "CREATE", "UPDATE", "DELETE"
    ]
    excludeRollbacks: bool
    filteringFields: RollbackHL7MessagesFilteringFields
    force: bool
    inputGcsObject: str
    resultGcsBucket: str
    rollbackTime: str

@typing.type_check_only
class RollbackHl7V2MessagesResponse(typing_extensions.TypedDict, total=False):
    hl7v2Store: str

@typing.type_check_only
class SchemaConfig(typing_extensions.TypedDict, total=False):
    lastUpdatedPartitionConfig: TimePartitioning
    recursiveStructureDepth: str
    schemaType: typing_extensions.Literal[
        "SCHEMA_TYPE_UNSPECIFIED", "LOSSLESS", "ANALYTICS", "ANALYTICS_V2"
    ]

@typing.type_check_only
class SchemaGroup(typing_extensions.TypedDict, total=False):
    choice: bool
    maxOccurs: int
    members: _list[GroupOrSegment]
    minOccurs: int
    name: str

@typing.type_check_only
class SchemaPackage(typing_extensions.TypedDict, total=False):
    ignoreMinOccurs: bool
    schemas: _list[Hl7SchemaConfig]
    schematizedParsingType: typing_extensions.Literal[
        "SCHEMATIZED_PARSING_TYPE_UNSPECIFIED", "SOFT_FAIL", "HARD_FAIL"
    ]
    types: _list[Hl7TypesConfig]
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
class SearchConfig(typing_extensions.TypedDict, total=False):
    searchParameters: _list[SearchParameter]

@typing.type_check_only
class SearchParameter(typing_extensions.TypedDict, total=False):
    canonicalUrl: str
    parameter: str

@typing.type_check_only
class SearchResourcesRequest(typing_extensions.TypedDict, total=False):
    resourceType: str

@typing.type_check_only
class Segment(typing_extensions.TypedDict, total=False):
    fields: dict[str, typing.Any]
    segmentId: str
    setId: str

@typing.type_check_only
class SeriesMetrics(typing_extensions.TypedDict, total=False):
    blobStorageSizeBytes: str
    instanceCount: str
    series: str
    structuredStorageSizeBytes: str

@typing.type_check_only
class SetBlobStorageSettingsRequest(typing_extensions.TypedDict, total=False):
    blobStorageSettings: BlobStorageSettings
    filterConfig: DicomFilterConfig

@typing.type_check_only
class SetBlobStorageSettingsResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class SetIamPolicyRequest(typing_extensions.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Signature(typing_extensions.TypedDict, total=False):
    image: Image
    metadata: dict[str, typing.Any]
    signatureTime: str
    userId: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StorageInfo(typing_extensions.TypedDict, total=False):
    blobStorageInfo: BlobStorageInfo
    referencedResource: str
    structuredStorageInfo: StructuredStorageInfo

@typing.type_check_only
class StreamConfig(typing_extensions.TypedDict, total=False):
    bigqueryDestination: GoogleCloudHealthcareV1beta1FhirBigQueryDestination
    deidentifiedStoreDestination: DeidentifiedStoreDestination
    resourceTypes: _list[str]

@typing.type_check_only
class StructuredStorageInfo(typing_extensions.TypedDict, total=False):
    sizeBytes: str

@typing.type_check_only
class StudyMetrics(typing_extensions.TypedDict, total=False):
    blobStorageSizeBytes: str
    instanceCount: str
    seriesCount: str
    structuredStorageSizeBytes: str
    study: str

@typing.type_check_only
class TagFilterList(typing_extensions.TypedDict, total=False):
    tags: _list[str]

@typing.type_check_only
class TestIamPermissionsRequest(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing_extensions.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TextConfig(typing_extensions.TypedDict, total=False):
    additionalTransformations: _list[InfoTypeTransformation]
    excludeInfoTypes: _list[str]
    profileType: typing_extensions.Literal["PROFILE_TYPE_UNSPECIFIED", "EMPTY", "BASIC"]
    transformations: _list[InfoTypeTransformation]

@typing.type_check_only
class TextSpan(typing_extensions.TypedDict, total=False):
    beginOffset: int
    content: str

@typing.type_check_only
class TimePartitioning(typing_extensions.TypedDict, total=False):
    expirationMs: str
    type: typing_extensions.Literal[
        "PARTITION_TYPE_UNSPECIFIED", "HOUR", "DAY", "MONTH", "YEAR"
    ]

@typing.type_check_only
class TimeRange(typing_extensions.TypedDict, total=False):
    end: str
    start: str

@typing.type_check_only
class Type(typing_extensions.TypedDict, total=False):
    fields: _list[Field]
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
    resourceAttributes: _list[Attribute]
    userId: str

@typing.type_check_only
class ValidationConfig(typing_extensions.TypedDict, total=False):
    disableFhirpathValidation: bool
    disableProfileValidation: bool
    disableReferenceTypeValidation: bool
    disableRequiredFieldValidation: bool
    enabledImplementationGuides: _list[str]

@typing.type_check_only
class VersionSource(typing_extensions.TypedDict, total=False):
    mshField: str
    value: str

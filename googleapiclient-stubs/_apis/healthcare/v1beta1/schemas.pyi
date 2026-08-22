import typing

_list = list

@typing.type_check_only
class AccessDeterminationLogConfig(typing.TypedDict, total=False):
    logLevel: typing.Literal["LOG_LEVEL_UNSPECIFIED", "DISABLED", "MINIMUM", "VERBOSE"]

@typing.type_check_only
class Action(typing.TypedDict, total=False):
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
class ActivateConsentRequest(typing.TypedDict, total=False):
    consentArtifact: str
    expireTime: str
    ttl: str

@typing.type_check_only
class AdminConsents(typing.TypedDict, total=False):
    names: _list[str]

@typing.type_check_only
class AnalyzeEntitiesRequest(typing.TypedDict, total=False):
    alternativeOutputFormat: typing.Literal[
        "ALTERNATIVE_OUTPUT_FORMAT_UNSPECIFIED", "FHIR_BUNDLE"
    ]
    documentContent: str
    licensedVocabularies: _list[
        typing.Literal["LICENSED_VOCABULARY_UNSPECIFIED", "ICD10CM", "SNOMEDCT_US"]
    ]

@typing.type_check_only
class AnalyzeEntitiesResponse(typing.TypedDict, total=False):
    entities: _list[Entity]
    entityMentions: _list[EntityMention]
    fhirBundle: str
    relationships: _list[EntityMentionRelationship]

@typing.type_check_only
class ApplyAdminConsentsErrorDetail(typing.TypedDict, total=False):
    consentErrors: _list[ConsentErrors]
    existingOperationId: str

@typing.type_check_only
class ApplyAdminConsentsRequest(typing.TypedDict, total=False):
    newConsentsList: AdminConsents
    validateOnly: bool

@typing.type_check_only
class ApplyAdminConsentsResponse(typing.TypedDict, total=False):
    affectedResources: str
    consentApplySuccess: str
    failedResources: str

@typing.type_check_only
class ApplyConsentsRequest(typing.TypedDict, total=False):
    patientScope: PatientScope
    timeRange: TimeRange
    validateOnly: bool

@typing.type_check_only
class ApplyConsentsResponse(typing.TypedDict, total=False):
    affectedResources: str
    consentApplyFailure: str
    consentApplySuccess: str
    failedResources: str

@typing.type_check_only
class ArchiveUserDataMappingRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ArchiveUserDataMappingResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class Attribute(typing.TypedDict, total=False):
    attributeDefinitionId: str
    values: _list[str]

@typing.type_check_only
class AttributeDefinition(typing.TypedDict, total=False):
    allowedValues: _list[str]
    category: typing.Literal["CATEGORY_UNSPECIFIED", "RESOURCE", "REQUEST"]
    consentDefaultValues: _list[str]
    dataMappingDefaultValue: str
    description: str
    name: str

@typing.type_check_only
class AuditConfig(typing.TypedDict, total=False):
    auditLogConfigs: _list[AuditLogConfig]
    service: str

@typing.type_check_only
class AuditLogConfig(typing.TypedDict, total=False):
    exemptedMembers: _list[str]
    logType: typing.Literal[
        "LOG_TYPE_UNSPECIFIED", "ADMIN_READ", "DATA_WRITE", "DATA_READ"
    ]

@typing.type_check_only
class BatchGetMessagesResponse(typing.TypedDict, total=False):
    messages: _list[Message]

@typing.type_check_only
class Binding(typing.TypedDict, total=False):
    condition: Expr
    members: _list[str]
    role: str

@typing.type_check_only
class BlobStorageInfo(typing.TypedDict, total=False):
    sizeBytes: str
    storageClass: typing.Literal[
        "BLOB_STORAGE_CLASS_UNSPECIFIED", "STANDARD", "NEARLINE", "COLDLINE", "ARCHIVE"
    ]
    storageClassUpdateTime: str

@typing.type_check_only
class BlobStorageSettings(typing.TypedDict, total=False):
    blobStorageClass: typing.Literal[
        "BLOB_STORAGE_CLASS_UNSPECIFIED", "STANDARD", "NEARLINE", "COLDLINE", "ARCHIVE"
    ]

@typing.type_check_only
class BulkDeleteResourcesRequest(typing.TypedDict, total=False):
    gcsDestination: GoogleCloudHealthcareV1beta1FhirGcsDestination
    type: str
    until: str
    validateOnly: bool
    versionConfig: typing.Literal[
        "VERSION_CONFIG_UNSPECIFIED", "ALL", "CURRENT_ONLY", "HISTORY_ONLY"
    ]

@typing.type_check_only
class BulkExportGcsDestination(typing.TypedDict, total=False):
    uriPrefix: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CharacterMaskConfig(typing.TypedDict, total=False):
    maskingCharacter: str

@typing.type_check_only
class CharacterMaskField(typing.TypedDict, total=False): ...

@typing.type_check_only
class CheckDataAccessRequest(typing.TypedDict, total=False):
    consentList: ConsentList
    dataId: str
    requestAttributes: dict[str, typing.Any]
    responseView: typing.Literal["RESPONSE_VIEW_UNSPECIFIED", "BASIC", "FULL"]

@typing.type_check_only
class CheckDataAccessResponse(typing.TypedDict, total=False):
    consentDetails: dict[str, typing.Any]
    consented: bool

@typing.type_check_only
class CleanDescriptorsOption(typing.TypedDict, total=False): ...

@typing.type_check_only
class CleanTextField(typing.TypedDict, total=False): ...

@typing.type_check_only
class CleanTextTag(typing.TypedDict, total=False): ...

@typing.type_check_only
class ConfigureSearchRequest(typing.TypedDict, total=False):
    canonicalUrls: _list[str]
    validateOnly: bool

@typing.type_check_only
class Consent(typing.TypedDict, total=False):
    consentArtifact: str
    expireTime: str
    metadata: dict[str, typing.Any]
    name: str
    policies: _list[GoogleCloudHealthcareV1beta1ConsentPolicy]
    revisionCreateTime: str
    revisionId: str
    state: typing.Literal[
        "STATE_UNSPECIFIED", "ACTIVE", "ARCHIVED", "REVOKED", "DRAFT", "REJECTED"
    ]
    ttl: str
    userId: str

@typing.type_check_only
class ConsentAccessorScope(typing.TypedDict, total=False):
    actor: str
    environment: str
    purpose: str

@typing.type_check_only
class ConsentArtifact(typing.TypedDict, total=False):
    consentContentScreenshots: _list[Image]
    consentContentVersion: str
    guardianSignature: Signature
    metadata: dict[str, typing.Any]
    name: str
    userId: str
    userSignature: Signature
    witnessSignature: Signature

@typing.type_check_only
class ConsentConfig(typing.TypedDict, total=False):
    accessDeterminationLogConfig: AccessDeterminationLogConfig
    accessEnforced: bool
    consentHeaderHandling: ConsentHeaderHandling
    enforcedAdminConsents: _list[str]
    version: typing.Literal["CONSENT_ENFORCEMENT_VERSION_UNSPECIFIED", "V1"]

@typing.type_check_only
class ConsentErrors(typing.TypedDict, total=False):
    error: Status
    name: str

@typing.type_check_only
class ConsentEvaluation(typing.TypedDict, total=False):
    evaluationResult: typing.Literal[
        "EVALUATION_RESULT_UNSPECIFIED",
        "NOT_APPLICABLE",
        "NO_MATCHING_POLICY",
        "NO_SATISFIED_POLICY",
        "HAS_SATISFIED_POLICY",
    ]

@typing.type_check_only
class ConsentHeaderHandling(typing.TypedDict, total=False):
    profile: typing.Literal[
        "SCOPE_PROFILE_UNSPECIFIED", "PERMIT_EMPTY_SCOPE", "REQUIRED_ON_READ"
    ]

@typing.type_check_only
class ConsentList(typing.TypedDict, total=False):
    consents: _list[str]

@typing.type_check_only
class ConsentStore(typing.TypedDict, total=False):
    defaultConsentTtl: str
    enableConsentCreateOnUpdate: bool
    labels: dict[str, typing.Any]
    name: str

@typing.type_check_only
class ContextualDeidConfig(typing.TypedDict, total=False): ...

@typing.type_check_only
class CreateMessageRequest(typing.TypedDict, total=False):
    message: Message

@typing.type_check_only
class CryptoHashConfig(typing.TypedDict, total=False):
    cryptoKey: str
    kmsWrapped: KmsWrappedCryptoKey

@typing.type_check_only
class CryptoHashField(typing.TypedDict, total=False): ...

@typing.type_check_only
class CustomRegex(typing.TypedDict, total=False):
    groupIndexes: _list[int]
    pattern: str

@typing.type_check_only
class Dataset(typing.TypedDict, total=False):
    encryptionSpec: EncryptionSpec
    name: str
    satisfiesPzi: bool
    satisfiesPzs: bool
    timeZone: str

@typing.type_check_only
class DateShiftConfig(typing.TypedDict, total=False):
    cryptoKey: str
    kmsWrapped: KmsWrappedCryptoKey

@typing.type_check_only
class DateShiftField(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeidentifiedStoreDestination(typing.TypedDict, total=False):
    config: DeidentifyConfig
    store: str

@typing.type_check_only
class DeidentifyConfig(typing.TypedDict, total=False):
    dicom: DicomConfig
    dicomTagConfig: DicomTagConfig
    fhir: FhirConfig
    fhirFieldConfig: FhirFieldConfig
    image: ImageConfig
    operationMetadata: DeidentifyOperationMetadata
    text: TextConfig
    useRegionalDataProcessing: bool

@typing.type_check_only
class DeidentifyDatasetRequest(typing.TypedDict, total=False):
    config: DeidentifyConfig
    destinationDataset: str
    gcsConfigUri: str

@typing.type_check_only
class DeidentifyDicomStoreRequest(typing.TypedDict, total=False):
    config: DeidentifyConfig
    destinationStore: str
    filterConfig: DicomFilterConfig
    gcsConfigUri: str

@typing.type_check_only
class DeidentifyFhirStoreRequest(typing.TypedDict, total=False):
    config: DeidentifyConfig
    destinationStore: str
    gcsConfigUri: str
    resourceFilter: FhirFilter
    skipModifiedResources: bool

@typing.type_check_only
class DeidentifyOperationMetadata(typing.TypedDict, total=False):
    fhirOutput: FhirOutput

@typing.type_check_only
class DeidentifySummary(typing.TypedDict, total=False): ...

@typing.type_check_only
class DeleteTag(typing.TypedDict, total=False): ...

@typing.type_check_only
class DicomConfig(typing.TypedDict, total=False):
    filterProfile: typing.Literal[
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
class DicomFilterConfig(typing.TypedDict, total=False):
    resourcePathsGcsUri: str

@typing.type_check_only
class DicomNotificationConfig(typing.TypedDict, total=False):
    pubsubTopic: str

@typing.type_check_only
class DicomStore(typing.TypedDict, total=False):
    labels: dict[str, typing.Any]
    name: str
    notificationConfig: NotificationConfig
    notificationConfigs: _list[DicomNotificationConfig]
    streamConfigs: _list[GoogleCloudHealthcareV1beta1DicomStreamConfig]

@typing.type_check_only
class DicomStoreMetrics(typing.TypedDict, total=False):
    blobStorageSizeBytes: str
    instanceCount: str
    name: str
    seriesCount: str
    structuredStorageSizeBytes: str
    studyCount: str

@typing.type_check_only
class DicomTagConfig(typing.TypedDict, total=False):
    actions: _list[Action]
    options: Options
    profileType: typing.Literal[
        "PROFILE_TYPE_UNSPECIFIED",
        "MINIMAL_KEEP_LIST_PROFILE",
        "ATTRIBUTE_CONFIDENTIALITY_BASIC_PROFILE",
        "KEEP_ALL_PROFILE",
        "DEIDENTIFY_TAG_CONTENTS",
    ]

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class EncryptionSpec(typing.TypedDict, total=False):
    kmsKeyName: str

@typing.type_check_only
class Entity(typing.TypedDict, total=False):
    entityId: str
    preferredTerm: str
    vocabularyCodes: _list[str]

@typing.type_check_only
class EntityMention(typing.TypedDict, total=False):
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
class EntityMentionRelationship(typing.TypedDict, total=False):
    confidence: float
    objectId: str
    subjectId: str

@typing.type_check_only
class EvaluateUserConsentsRequest(typing.TypedDict, total=False):
    consentList: ConsentList
    pageSize: int
    pageToken: str
    requestAttributes: dict[str, typing.Any]
    resourceAttributes: dict[str, typing.Any]
    responseView: typing.Literal["RESPONSE_VIEW_UNSPECIFIED", "BASIC", "FULL"]
    userId: str

@typing.type_check_only
class EvaluateUserConsentsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    results: _list[Result]

@typing.type_check_only
class ExplainDataAccessConsentInfo(typing.TypedDict, total=False):
    cascadeOrigins: _list[str]
    consentResource: str
    enforcementTime: str
    matchingAccessorScopes: _list[ConsentAccessorScope]
    patientConsentOwner: str
    type: typing.Literal[
        "CONSENT_POLICY_TYPE_UNSPECIFIED",
        "CONSENT_POLICY_TYPE_PATIENT",
        "CONSENT_POLICY_TYPE_ADMIN",
    ]
    variants: _list[
        typing.Literal[
            "CONSENT_VARIANT_UNSPECIFIED",
            "CONSENT_VARIANT_STANDARD",
            "CONSENT_VARIANT_CASCADE",
        ]
    ]

@typing.type_check_only
class ExplainDataAccessConsentScope(typing.TypedDict, total=False):
    accessorScope: ConsentAccessorScope
    decision: typing.Literal[
        "CONSENT_DECISION_TYPE_UNSPECIFIED",
        "CONSENT_DECISION_TYPE_PERMIT",
        "CONSENT_DECISION_TYPE_DENY",
    ]
    enforcingConsents: _list[ExplainDataAccessConsentInfo]
    exceptions: _list[ExplainDataAccessConsentScope]

@typing.type_check_only
class ExplainDataAccessResponse(typing.TypedDict, total=False):
    consentScopes: _list[ExplainDataAccessConsentScope]
    warning: str

@typing.type_check_only
class ExportDicomDataRequest(typing.TypedDict, total=False):
    bigqueryDestination: GoogleCloudHealthcareV1beta1DicomBigQueryDestination
    filterConfig: DicomFilterConfig
    gcsDestination: GoogleCloudHealthcareV1beta1DicomGcsDestination

@typing.type_check_only
class ExportDicomDataResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class ExportMessagesRequest(typing.TypedDict, total=False):
    endTime: str
    filter: str
    gcsDestination: GcsDestination
    pubsubDestination: PubsubDestination
    startTime: str

@typing.type_check_only
class ExportMessagesResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class ExportResourcesHistoryRequest(typing.TypedDict, total=False):
    _since: str
    _type: str
    gcsDestination: GoogleCloudHealthcareV1beta1FhirGcsDestination
    maxResourceVersions: str

@typing.type_check_only
class ExportResourcesRequest(typing.TypedDict, total=False):
    _since: str
    _type: str
    bigqueryDestination: GoogleCloudHealthcareV1beta1FhirBigQueryDestination
    gcsDestination: GoogleCloudHealthcareV1beta1FhirGcsDestination

@typing.type_check_only
class Expr(typing.TypedDict, total=False):
    description: str
    expression: str
    location: str
    title: str

@typing.type_check_only
class Feature(typing.TypedDict, total=False):
    confidence: float
    value: str

@typing.type_check_only
class FhirConfig(typing.TypedDict, total=False):
    defaultKeepExtensions: bool
    fieldMetadataList: _list[FieldMetadata]

@typing.type_check_only
class FhirFieldConfig(typing.TypedDict, total=False):
    fieldMetadataList: _list[GoogleCloudHealthcareV1beta1DeidentifyFieldMetadata]
    options: GoogleCloudHealthcareV1beta1DeidentifyOptions
    profileType: typing.Literal[
        "PROFILE_TYPE_UNSPECIFIED", "KEEP_ALL", "BASIC", "CLEAN_ALL"
    ]

@typing.type_check_only
class FhirFilter(typing.TypedDict, total=False):
    resources: Resources

@typing.type_check_only
class FhirNotificationConfig(typing.TypedDict, total=False):
    pubsubTopic: str
    sendFullResource: bool
    sendPreviousResourceOnDelete: bool

@typing.type_check_only
class FhirOutput(typing.TypedDict, total=False):
    fhirStore: str

@typing.type_check_only
class FhirStore(typing.TypedDict, total=False):
    bulkExportGcsDestination: BulkExportGcsDestination
    complexDataTypeReferenceParsing: typing.Literal[
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
    version: typing.Literal["VERSION_UNSPECIFIED", "DSTU2", "STU3", "R4", "R5"]

@typing.type_check_only
class FhirStoreMetric(typing.TypedDict, total=False):
    count: str
    resourceType: str
    structuredStorageSizeBytes: str
    versionedStorageSizeBytes: str

@typing.type_check_only
class FhirStoreMetrics(typing.TypedDict, total=False):
    metrics: _list[FhirStoreMetric]
    name: str

@typing.type_check_only
class Field(typing.TypedDict, total=False):
    maxOccurs: int
    minOccurs: int
    name: str
    table: str
    type: str

@typing.type_check_only
class FieldMetadata(typing.TypedDict, total=False):
    action: typing.Literal[
        "ACTION_UNSPECIFIED", "TRANSFORM", "INSPECT_AND_TRANSFORM", "DO_NOT_TRANSFORM"
    ]
    paths: _list[str]

@typing.type_check_only
class GcsDestination(typing.TypedDict, total=False):
    contentStructure: typing.Literal["CONTENT_STRUCTURE_UNSPECIFIED", "MESSAGE_JSON"]
    messageView: typing.Literal[
        "MESSAGE_VIEW_UNSPECIFIED",
        "RAW_ONLY",
        "PARSED_ONLY",
        "FULL",
        "SCHEMATIZED_ONLY",
        "BASIC",
    ]
    uriPrefix: str

@typing.type_check_only
class GcsSource(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudHealthcareV1beta1ConsentGcsDestination(typing.TypedDict, total=False):
    uriPrefix: str

@typing.type_check_only
class GoogleCloudHealthcareV1beta1ConsentPolicy(typing.TypedDict, total=False):
    authorizationRule: Expr
    resourceAttributes: _list[Attribute]

@typing.type_check_only
class GoogleCloudHealthcareV1beta1DeidentifyDeidentifyDicomStoreSummary(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudHealthcareV1beta1DeidentifyDeidentifyFhirStoreSummary(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudHealthcareV1beta1DeidentifyFieldMetadata(
    typing.TypedDict, total=False
):
    characterMaskField: CharacterMaskField
    cleanTextField: CleanTextField
    cryptoHashField: CryptoHashField
    dateShiftField: DateShiftField
    keepField: KeepField
    paths: _list[str]
    removeField: RemoveField

@typing.type_check_only
class GoogleCloudHealthcareV1beta1DeidentifyOptions(typing.TypedDict, total=False):
    characterMaskConfig: CharacterMaskConfig
    contextualDeid: ContextualDeidConfig
    cryptoHashConfig: CryptoHashConfig
    dateShiftConfig: DateShiftConfig
    keepExtensions: KeepExtensionsConfig

@typing.type_check_only
class GoogleCloudHealthcareV1beta1DicomBigQueryDestination(
    typing.TypedDict, total=False
):
    changeDataCaptureConfig: GoogleCloudHealthcareV1beta1DicomChangeDataCaptureConfig
    force: bool
    includeSourceStore: bool
    schemaFlattened: SchemaFlattened
    schemaJson: SchemaJSON
    tableUri: str
    writeDisposition: typing.Literal[
        "WRITE_DISPOSITION_UNSPECIFIED", "WRITE_EMPTY", "WRITE_TRUNCATE", "WRITE_APPEND"
    ]

@typing.type_check_only
class GoogleCloudHealthcareV1beta1DicomChangeDataCaptureConfig(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudHealthcareV1beta1DicomGcsDestination(typing.TypedDict, total=False):
    mimeType: str
    uriPrefix: str

@typing.type_check_only
class GoogleCloudHealthcareV1beta1DicomGcsSource(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudHealthcareV1beta1DicomStreamConfig(typing.TypedDict, total=False):
    bigqueryDestination: GoogleCloudHealthcareV1beta1DicomBigQueryDestination

@typing.type_check_only
class GoogleCloudHealthcareV1beta1FhirBigQueryDestination(
    typing.TypedDict, total=False
):
    changeDataCaptureConfig: GoogleCloudHealthcareV1beta1FhirChangeDataCaptureConfig
    datasetUri: str
    force: bool
    schemaConfig: SchemaConfig
    writeDisposition: typing.Literal[
        "WRITE_DISPOSITION_UNSPECIFIED", "WRITE_EMPTY", "WRITE_TRUNCATE", "WRITE_APPEND"
    ]

@typing.type_check_only
class GoogleCloudHealthcareV1beta1FhirChangeDataCaptureConfig(
    typing.TypedDict, total=False
):
    historyMode: typing.Literal[
        "HISTORY_MODE_UNSPECIFIED", "KEEP_LATEST_VERSION", "KEEP_ALL_VERSIONS"
    ]

@typing.type_check_only
class GoogleCloudHealthcareV1beta1FhirExportResourcesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GoogleCloudHealthcareV1beta1FhirGcsDestination(typing.TypedDict, total=False):
    uriPrefix: str

@typing.type_check_only
class GoogleCloudHealthcareV1beta1FhirGcsSource(typing.TypedDict, total=False):
    uri: str

@typing.type_check_only
class GoogleCloudHealthcareV1beta1FhirImportResourcesResponse(
    typing.TypedDict, total=False
): ...

@typing.type_check_only
class GroupOrSegment(typing.TypedDict, total=False):
    group: SchemaGroup
    segment: SchemaSegment

@typing.type_check_only
class Hl7SchemaConfig(typing.TypedDict, total=False):
    messageSchemaConfigs: dict[str, typing.Any]
    version: _list[VersionSource]

@typing.type_check_only
class Hl7TypesConfig(typing.TypedDict, total=False):
    type: _list[Type]
    version: _list[VersionSource]

@typing.type_check_only
class Hl7V2NotificationConfig(typing.TypedDict, total=False):
    filter: str
    pubsubTopic: str

@typing.type_check_only
class Hl7V2Store(typing.TypedDict, total=False):
    labels: dict[str, typing.Any]
    name: str
    notificationConfig: NotificationConfig
    notificationConfigs: _list[Hl7V2NotificationConfig]
    parserConfig: ParserConfig
    rejectDuplicateMessage: bool

@typing.type_check_only
class Hl7V2StoreMetric(typing.TypedDict, total=False):
    count: str
    messageType: str
    structuredStorageSizeBytes: str

@typing.type_check_only
class Hl7V2StoreMetrics(typing.TypedDict, total=False):
    metrics: _list[Hl7V2StoreMetric]
    name: str

@typing.type_check_only
class HttpBody(typing.TypedDict, total=False):
    contentType: str
    data: str
    extensions: _list[dict[str, typing.Any]]

@typing.type_check_only
class Image(typing.TypedDict, total=False):
    gcsUri: str
    rawBytes: str

@typing.type_check_only
class ImageConfig(typing.TypedDict, total=False):
    additionalInfoTypes: _list[str]
    customRegexes: _list[CustomRegex]
    excludeInfoTypes: _list[str]
    textRedactionMode: typing.Literal[
        "TEXT_REDACTION_MODE_UNSPECIFIED",
        "REDACT_ALL_TEXT",
        "REDACT_SENSITIVE_TEXT",
        "REDACT_NO_TEXT",
        "REDACT_SENSITIVE_TEXT_CLEAN_DESCRIPTORS",
    ]

@typing.type_check_only
class ImportDicomDataRequest(typing.TypedDict, total=False):
    blobStorageSettings: BlobStorageSettings
    gcsSource: GoogleCloudHealthcareV1beta1DicomGcsSource

@typing.type_check_only
class ImportDicomDataResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class ImportMessagesRequest(typing.TypedDict, total=False):
    gcsSource: GcsSource

@typing.type_check_only
class ImportMessagesResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class ImportResourcesHistoryRequest(typing.TypedDict, total=False):
    contentStructure: typing.Literal[
        "CONTENT_STRUCTURE_UNSPECIFIED",
        "BUNDLE",
        "RESOURCE",
        "BUNDLE_PRETTY",
        "RESOURCE_PRETTY",
    ]
    gcsSource: GoogleCloudHealthcareV1beta1FhirGcsSource
    maxErrorCount: str

@typing.type_check_only
class ImportResourcesRequest(typing.TypedDict, total=False):
    contentStructure: typing.Literal[
        "CONTENT_STRUCTURE_UNSPECIFIED",
        "BUNDLE",
        "RESOURCE",
        "BUNDLE_PRETTY",
        "RESOURCE_PRETTY",
    ]
    gcsSource: GoogleCloudHealthcareV1beta1FhirGcsSource

@typing.type_check_only
class InfoTypeTransformation(typing.TypedDict, total=False):
    characterMaskConfig: CharacterMaskConfig
    cryptoHashConfig: CryptoHashConfig
    dateShiftConfig: DateShiftConfig
    infoTypes: _list[str]
    redactConfig: RedactConfig
    replaceWithInfoTypeConfig: ReplaceWithInfoTypeConfig

@typing.type_check_only
class IngestMessageRequest(typing.TypedDict, total=False):
    message: Message

@typing.type_check_only
class IngestMessageResponse(typing.TypedDict, total=False):
    hl7Ack: str
    message: Message

@typing.type_check_only
class KeepExtensionsConfig(typing.TypedDict, total=False): ...

@typing.type_check_only
class KeepField(typing.TypedDict, total=False): ...

@typing.type_check_only
class KeepTag(typing.TypedDict, total=False): ...

@typing.type_check_only
class KmsWrappedCryptoKey(typing.TypedDict, total=False):
    cryptoKey: str
    wrappedKey: str

@typing.type_check_only
class LinkedEntity(typing.TypedDict, total=False):
    entityId: str

@typing.type_check_only
class ListAttributeDefinitionsResponse(typing.TypedDict, total=False):
    attributeDefinitions: _list[AttributeDefinition]
    nextPageToken: str

@typing.type_check_only
class ListConsentArtifactsResponse(typing.TypedDict, total=False):
    consentArtifacts: _list[ConsentArtifact]
    nextPageToken: str

@typing.type_check_only
class ListConsentRevisionsResponse(typing.TypedDict, total=False):
    consents: _list[Consent]
    nextPageToken: str

@typing.type_check_only
class ListConsentStoresResponse(typing.TypedDict, total=False):
    consentStores: _list[ConsentStore]
    nextPageToken: str

@typing.type_check_only
class ListConsentsResponse(typing.TypedDict, total=False):
    consents: _list[Consent]
    nextPageToken: str

@typing.type_check_only
class ListDatasetsResponse(typing.TypedDict, total=False):
    datasets: _list[Dataset]
    nextPageToken: str

@typing.type_check_only
class ListDicomStoresResponse(typing.TypedDict, total=False):
    dicomStores: _list[DicomStore]
    nextPageToken: str

@typing.type_check_only
class ListFhirStoresResponse(typing.TypedDict, total=False):
    fhirStores: _list[FhirStore]
    nextPageToken: str

@typing.type_check_only
class ListHl7V2StoresResponse(typing.TypedDict, total=False):
    hl7V2Stores: _list[Hl7V2Store]
    nextPageToken: str

@typing.type_check_only
class ListLocationsResponse(typing.TypedDict, total=False):
    locations: _list[Location]
    nextPageToken: str

@typing.type_check_only
class ListMessagesResponse(typing.TypedDict, total=False):
    hl7V2Messages: _list[Message]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListUserDataMappingsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    userDataMappings: _list[UserDataMapping]

@typing.type_check_only
class Location(typing.TypedDict, total=False):
    displayName: str
    labels: dict[str, typing.Any]
    locationId: str
    metadata: dict[str, typing.Any]
    name: str

@typing.type_check_only
class Message(typing.TypedDict, total=False):
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
class NotificationConfig(typing.TypedDict, total=False):
    pubsubTopic: str
    sendForBulkImport: bool

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OperationMetadata(typing.TypedDict, total=False):
    apiMethodName: str
    cancelRequested: bool
    counter: ProgressCounter
    createTime: str
    endTime: str
    logsUrl: str

@typing.type_check_only
class Options(typing.TypedDict, total=False):
    cleanDescriptors: CleanDescriptorsOption
    cleanImage: ImageConfig
    primaryIds: typing.Literal["PRIMARY_IDS_OPTION_UNSPECIFIED", "KEEP", "REGEN"]

@typing.type_check_only
class ParsedData(typing.TypedDict, total=False):
    segments: _list[Segment]

@typing.type_check_only
class ParserConfig(typing.TypedDict, total=False):
    allowNullHeader: bool
    schema: SchemaPackage
    segmentTerminator: str
    version: typing.Literal["PARSER_VERSION_UNSPECIFIED", "V1", "V2", "V3"]

@typing.type_check_only
class PatientId(typing.TypedDict, total=False):
    type: str
    value: str

@typing.type_check_only
class PatientScope(typing.TypedDict, total=False):
    patientIds: _list[str]

@typing.type_check_only
class Policy(typing.TypedDict, total=False):
    auditConfigs: _list[AuditConfig]
    bindings: _list[Binding]
    etag: str
    version: int

@typing.type_check_only
class ProgressCounter(typing.TypedDict, total=False):
    failure: str
    pending: str
    secondaryFailure: str
    secondarySuccess: str
    success: str

@typing.type_check_only
class PubsubDestination(typing.TypedDict, total=False):
    pubsubTopic: str

@typing.type_check_only
class QueryAccessibleDataRequest(typing.TypedDict, total=False):
    gcsDestination: GoogleCloudHealthcareV1beta1ConsentGcsDestination
    requestAttributes: dict[str, typing.Any]
    resourceAttributes: dict[str, typing.Any]

@typing.type_check_only
class QueryAccessibleDataResponse(typing.TypedDict, total=False):
    gcsUris: _list[str]

@typing.type_check_only
class RecurseTag(typing.TypedDict, total=False): ...

@typing.type_check_only
class RedactConfig(typing.TypedDict, total=False): ...

@typing.type_check_only
class RegenUidTag(typing.TypedDict, total=False): ...

@typing.type_check_only
class RejectConsentRequest(typing.TypedDict, total=False):
    consentArtifact: str

@typing.type_check_only
class RemoveField(typing.TypedDict, total=False): ...

@typing.type_check_only
class RemoveTag(typing.TypedDict, total=False): ...

@typing.type_check_only
class ReplaceWithInfoTypeConfig(typing.TypedDict, total=False): ...

@typing.type_check_only
class ResetTag(typing.TypedDict, total=False): ...

@typing.type_check_only
class Resources(typing.TypedDict, total=False):
    resources: _list[str]

@typing.type_check_only
class Result(typing.TypedDict, total=False):
    consentDetails: dict[str, typing.Any]
    consented: bool
    dataId: str

@typing.type_check_only
class RevokeConsentRequest(typing.TypedDict, total=False):
    consentArtifact: str

@typing.type_check_only
class RollbackFhirResourceFilteringFields(typing.TypedDict, total=False):
    metadataFilter: str
    operationIds: _list[str]

@typing.type_check_only
class RollbackFhirResourcesRequest(typing.TypedDict, total=False):
    changeType: typing.Literal[
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
class RollbackFhirResourcesResponse(typing.TypedDict, total=False):
    fhirStore: str

@typing.type_check_only
class RollbackHL7MessagesFilteringFields(typing.TypedDict, total=False):
    operationIds: _list[str]

@typing.type_check_only
class RollbackHl7V2MessagesRequest(typing.TypedDict, total=False):
    changeType: typing.Literal[
        "CHANGE_TYPE_UNSPECIFIED", "ALL", "CREATE", "UPDATE", "DELETE"
    ]
    excludeRollbacks: bool
    filteringFields: RollbackHL7MessagesFilteringFields
    force: bool
    inputGcsObject: str
    resultGcsBucket: str
    rollbackTime: str

@typing.type_check_only
class RollbackHl7V2MessagesResponse(typing.TypedDict, total=False):
    hl7v2Store: str

@typing.type_check_only
class SchemaConfig(typing.TypedDict, total=False):
    lastUpdatedPartitionConfig: TimePartitioning
    recursiveStructureDepth: str
    schemaType: typing.Literal[
        "SCHEMA_TYPE_UNSPECIFIED", "LOSSLESS", "ANALYTICS", "ANALYTICS_V2"
    ]

@typing.type_check_only
class SchemaFlattened(typing.TypedDict, total=False): ...

@typing.type_check_only
class SchemaGroup(typing.TypedDict, total=False):
    choice: bool
    maxOccurs: int
    members: _list[GroupOrSegment]
    minOccurs: int
    name: str

@typing.type_check_only
class SchemaJSON(typing.TypedDict, total=False): ...

@typing.type_check_only
class SchemaPackage(typing.TypedDict, total=False):
    ignoreMinOccurs: bool
    schemas: _list[Hl7SchemaConfig]
    schematizedParsingType: typing.Literal[
        "SCHEMATIZED_PARSING_TYPE_UNSPECIFIED", "SOFT_FAIL", "HARD_FAIL"
    ]
    types: _list[Hl7TypesConfig]
    unexpectedSegmentHandling: typing.Literal[
        "UNEXPECTED_SEGMENT_HANDLING_MODE_UNSPECIFIED", "FAIL", "SKIP", "PARSE"
    ]

@typing.type_check_only
class SchemaSegment(typing.TypedDict, total=False):
    maxOccurs: int
    minOccurs: int
    type: str

@typing.type_check_only
class SchematizedData(typing.TypedDict, total=False):
    data: str
    error: str

@typing.type_check_only
class SearchConfig(typing.TypedDict, total=False):
    searchParameters: _list[SearchParameter]

@typing.type_check_only
class SearchParameter(typing.TypedDict, total=False):
    canonicalUrl: str
    parameter: str

@typing.type_check_only
class Segment(typing.TypedDict, total=False):
    fields: dict[str, typing.Any]
    segmentId: str
    setId: str

@typing.type_check_only
class SeriesMetrics(typing.TypedDict, total=False):
    blobStorageSizeBytes: str
    instanceCount: str
    series: str
    structuredStorageSizeBytes: str

@typing.type_check_only
class SetBlobStorageSettingsRequest(typing.TypedDict, total=False):
    blobStorageSettings: BlobStorageSettings
    filterConfig: DicomFilterConfig

@typing.type_check_only
class SetBlobStorageSettingsResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class SetIamPolicyRequest(typing.TypedDict, total=False):
    policy: Policy
    updateMask: str

@typing.type_check_only
class Signature(typing.TypedDict, total=False):
    image: Image
    metadata: dict[str, typing.Any]
    signatureTime: str
    userId: str

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class StorageInfo(typing.TypedDict, total=False):
    blobStorageInfo: BlobStorageInfo
    referencedResource: str
    structuredStorageInfo: StructuredStorageInfo

@typing.type_check_only
class StreamConfig(typing.TypedDict, total=False):
    bigqueryDestination: GoogleCloudHealthcareV1beta1FhirBigQueryDestination
    deidentifiedStoreDestination: DeidentifiedStoreDestination
    resourceTypes: _list[str]

@typing.type_check_only
class StructuredStorageInfo(typing.TypedDict, total=False):
    sizeBytes: str

@typing.type_check_only
class StudyMetrics(typing.TypedDict, total=False):
    blobStorageSizeBytes: str
    instanceCount: str
    seriesCount: str
    structuredStorageSizeBytes: str
    study: str

@typing.type_check_only
class TagFilterList(typing.TypedDict, total=False):
    tags: _list[str]

@typing.type_check_only
class TestIamPermissionsRequest(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TestIamPermissionsResponse(typing.TypedDict, total=False):
    permissions: _list[str]

@typing.type_check_only
class TextConfig(typing.TypedDict, total=False):
    additionalTransformations: _list[InfoTypeTransformation]
    excludeInfoTypes: _list[str]
    profileType: typing.Literal["PROFILE_TYPE_UNSPECIFIED", "EMPTY", "BASIC"]
    transformations: _list[InfoTypeTransformation]

@typing.type_check_only
class TextSpan(typing.TypedDict, total=False):
    beginOffset: int
    content: str

@typing.type_check_only
class TimePartitioning(typing.TypedDict, total=False):
    expirationMs: str
    type: typing.Literal["PARTITION_TYPE_UNSPECIFIED", "HOUR", "DAY", "MONTH", "YEAR"]

@typing.type_check_only
class TimeRange(typing.TypedDict, total=False):
    end: str
    start: str

@typing.type_check_only
class Type(typing.TypedDict, total=False):
    fields: _list[Field]
    name: str
    primitive: typing.Literal[
        "PRIMITIVE_UNSPECIFIED", "STRING", "VARIES", "UNESCAPED_STRING"
    ]

@typing.type_check_only
class UpdateSeriesMetadataResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class UpdateStudyMetadataResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class UserDataMapping(typing.TypedDict, total=False):
    archiveTime: str
    archived: bool
    dataId: str
    name: str
    resourceAttributes: _list[Attribute]
    userId: str

@typing.type_check_only
class ValidationConfig(typing.TypedDict, total=False):
    disableFhirpathValidation: bool
    disableProfileValidation: bool
    disableReferenceTypeValidation: bool
    disableRequiredFieldValidation: bool
    enableFhirpathProfileValidation: bool
    enabledImplementationGuides: _list[str]

@typing.type_check_only
class VersionSource(typing.TypedDict, total=False):
    mshField: str
    value: str

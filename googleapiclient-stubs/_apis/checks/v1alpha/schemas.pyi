import typing

import typing_extensions

_list = list

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class GoogleChecksAccountV1alphaApp(typing_extensions.TypedDict, total=False):
    name: str
    title: str

@typing.type_check_only
class GoogleChecksAccountV1alphaListAppsResponse(
    typing_extensions.TypedDict, total=False
):
    apps: _list[GoogleChecksAccountV1alphaApp]
    nextPageToken: str

@typing.type_check_only
class GoogleChecksAisafetyV1alphaClassifyContentRequest(
    typing_extensions.TypedDict, total=False
):
    classifierVersion: typing_extensions.Literal[
        "CLASSIFIER_VERSION_UNSPECIFIED", "STABLE", "LATEST"
    ]
    context: GoogleChecksAisafetyV1alphaClassifyContentRequestContext
    input: GoogleChecksAisafetyV1alphaClassifyContentRequestInputContent
    policies: _list[GoogleChecksAisafetyV1alphaClassifyContentRequestPolicyConfig]

@typing.type_check_only
class GoogleChecksAisafetyV1alphaClassifyContentRequestContext(
    typing_extensions.TypedDict, total=False
):
    prompt: str

@typing.type_check_only
class GoogleChecksAisafetyV1alphaClassifyContentRequestInputContent(
    typing_extensions.TypedDict, total=False
):
    textInput: GoogleChecksAisafetyV1alphaTextInput

@typing.type_check_only
class GoogleChecksAisafetyV1alphaClassifyContentRequestPolicyConfig(
    typing_extensions.TypedDict, total=False
):
    policyType: typing_extensions.Literal[
        "POLICY_TYPE_UNSPECIFIED",
        "DANGEROUS_CONTENT",
        "PII_SOLICITING_RECITING",
        "HARASSMENT",
        "SEXUALLY_EXPLICIT",
        "HATE_SPEECH",
        "MEDICAL_INFO",
        "VIOLENCE_AND_GORE",
        "OBSCENITY_AND_PROFANITY",
    ]
    threshold: float

@typing.type_check_only
class GoogleChecksAisafetyV1alphaClassifyContentResponse(
    typing_extensions.TypedDict, total=False
):
    policyResults: _list[GoogleChecksAisafetyV1alphaClassifyContentResponsePolicyResult]

@typing.type_check_only
class GoogleChecksAisafetyV1alphaClassifyContentResponsePolicyResult(
    typing_extensions.TypedDict, total=False
):
    policyType: typing_extensions.Literal[
        "POLICY_TYPE_UNSPECIFIED",
        "DANGEROUS_CONTENT",
        "PII_SOLICITING_RECITING",
        "HARASSMENT",
        "SEXUALLY_EXPLICIT",
        "HATE_SPEECH",
        "MEDICAL_INFO",
        "VIOLENCE_AND_GORE",
        "OBSCENITY_AND_PROFANITY",
    ]
    score: float
    violationResult: typing_extensions.Literal[
        "VIOLATION_RESULT_UNSPECIFIED",
        "VIOLATIVE",
        "NON_VIOLATIVE",
        "CLASSIFICATION_ERROR",
    ]

@typing.type_check_only
class GoogleChecksAisafetyV1alphaTextInput(typing_extensions.TypedDict, total=False):
    content: str
    languageCode: str

@typing.type_check_only
class GoogleChecksRepoScanV1alphaCliAnalysis(typing_extensions.TypedDict, total=False):
    codeScans: _list[GoogleChecksRepoScanV1alphaCodeScan]
    sources: _list[GoogleChecksRepoScanV1alphaSource]

@typing.type_check_only
class GoogleChecksRepoScanV1alphaCodeAttribution(
    typing_extensions.TypedDict, total=False
):
    codeExcerpt: str
    lineNumber: int
    path: str
    startLineNumber: int

@typing.type_check_only
class GoogleChecksRepoScanV1alphaCodeScan(typing_extensions.TypedDict, total=False):
    dataTypeClassifications: _list[
        GoogleChecksRepoScanV1alphaCodeScanDataTypeClassification
    ]
    sourceCode: GoogleChecksRepoScanV1alphaSourceCode

@typing.type_check_only
class GoogleChecksRepoScanV1alphaCodeScanDataTypeClassification(
    typing_extensions.TypedDict, total=False
):
    dataType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "DATA_TYPE_APPROXIMATE_LOCATION",
        "DATA_TYPE_PRECISE_LOCATION",
        "DATA_TYPE_PERSONAL_NAME",
        "DATA_TYPE_EMAIL_ADDRESS",
        "DATA_TYPE_USER_IDS",
        "DATA_TYPE_PHYSICAL_ADDRESS",
        "DATA_TYPE_PHONE_NUMBER",
        "DATA_TYPE_RACE_AND_ETHNICITY",
        "DATA_TYPE_POLITICAL_OR_RELIGIOUS_BELIEFS",
        "DATA_TYPE_SEXUAL_ORIENTATION",
        "DATA_TYPE_OTHER_PERSONAL_INFO",
        "DATA_TYPE_PAYMENT_INFO",
        "DATA_TYPE_PURCHASE_HISTORY",
        "DATA_TYPE_CREDIT_SCORE",
        "DATA_TYPE_OTHER_FINANCIAL_INFO",
        "DATA_TYPE_HEALTH_INFO",
        "DATA_TYPE_FITNESS_INFO",
        "DATA_TYPE_EMAILS",
        "DATA_TYPE_TEXT_MESSAGES",
        "DATA_TYPE_OTHER_IN_APP_MESSAGES",
        "DATA_TYPE_PHOTOS",
        "DATA_TYPE_VIDEOS",
        "DATA_TYPE_VOICE_OR_SOUND_RECORDINGS",
        "DATA_TYPE_MUSIC_FILES",
        "DATA_TYPE_OTHER_AUDIO_FILES",
        "DATA_TYPE_FILES_AND_DOCS",
        "DATA_TYPE_CALENDAR_EVENTS",
        "DATA_TYPE_CONTACTS",
        "DATA_TYPE_APP_INTERACTIONS",
        "DATA_TYPE_IN_APP_SEARCH_HISTORY",
        "DATA_TYPE_INSTALLED_APPS",
        "DATA_TYPE_OTHER_USER_GENERATED_CONTENT",
        "DATA_TYPE_OTHER_ACTIONS",
        "DATA_TYPE_WEB_BROWSING_HISTORY",
        "DATA_TYPE_CRASH_LOGS",
        "DATA_TYPE_PERFORMANCE_DIAGNOSTICS",
        "DATA_TYPE_OTHER_APP_PERFORMANCE_DATA",
        "DATA_TYPE_DEVICE_OR_OTHER_IDS",
    ]
    lineNumber: int

@typing.type_check_only
class GoogleChecksRepoScanV1alphaGenerateScanRequest(
    typing_extensions.TypedDict, total=False
):
    cliAnalysis: GoogleChecksRepoScanV1alphaCliAnalysis
    cliVersion: str
    localScanPath: str
    scmMetadata: GoogleChecksRepoScanV1alphaScmMetadata

@typing.type_check_only
class GoogleChecksRepoScanV1alphaListRepoScansResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    repoScans: _list[GoogleChecksRepoScanV1alphaRepoScan]

@typing.type_check_only
class GoogleChecksRepoScanV1alphaPullRequest(typing_extensions.TypedDict, total=False):
    baseBranch: str
    prNumber: str

@typing.type_check_only
class GoogleChecksRepoScanV1alphaRepoScan(typing_extensions.TypedDict, total=False):
    cliVersion: str
    localScanPath: str
    name: str
    resultsUri: str
    scmMetadata: GoogleChecksRepoScanV1alphaScmMetadata
    sources: _list[GoogleChecksRepoScanV1alphaSource]

@typing.type_check_only
class GoogleChecksRepoScanV1alphaScmMetadata(typing_extensions.TypedDict, total=False):
    branch: str
    pullRequest: GoogleChecksRepoScanV1alphaPullRequest
    remoteUri: str
    revisionId: str

@typing.type_check_only
class GoogleChecksRepoScanV1alphaSource(typing_extensions.TypedDict, total=False):
    codeAttribution: GoogleChecksRepoScanV1alphaCodeAttribution
    dataType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "DATA_TYPE_APPROXIMATE_LOCATION",
        "DATA_TYPE_PRECISE_LOCATION",
        "DATA_TYPE_PERSONAL_NAME",
        "DATA_TYPE_EMAIL_ADDRESS",
        "DATA_TYPE_USER_IDS",
        "DATA_TYPE_PHYSICAL_ADDRESS",
        "DATA_TYPE_PHONE_NUMBER",
        "DATA_TYPE_RACE_AND_ETHNICITY",
        "DATA_TYPE_POLITICAL_OR_RELIGIOUS_BELIEFS",
        "DATA_TYPE_SEXUAL_ORIENTATION",
        "DATA_TYPE_OTHER_PERSONAL_INFO",
        "DATA_TYPE_PAYMENT_INFO",
        "DATA_TYPE_PURCHASE_HISTORY",
        "DATA_TYPE_CREDIT_SCORE",
        "DATA_TYPE_OTHER_FINANCIAL_INFO",
        "DATA_TYPE_HEALTH_INFO",
        "DATA_TYPE_FITNESS_INFO",
        "DATA_TYPE_EMAILS",
        "DATA_TYPE_TEXT_MESSAGES",
        "DATA_TYPE_OTHER_IN_APP_MESSAGES",
        "DATA_TYPE_PHOTOS",
        "DATA_TYPE_VIDEOS",
        "DATA_TYPE_VOICE_OR_SOUND_RECORDINGS",
        "DATA_TYPE_MUSIC_FILES",
        "DATA_TYPE_OTHER_AUDIO_FILES",
        "DATA_TYPE_FILES_AND_DOCS",
        "DATA_TYPE_CALENDAR_EVENTS",
        "DATA_TYPE_CONTACTS",
        "DATA_TYPE_APP_INTERACTIONS",
        "DATA_TYPE_IN_APP_SEARCH_HISTORY",
        "DATA_TYPE_INSTALLED_APPS",
        "DATA_TYPE_OTHER_USER_GENERATED_CONTENT",
        "DATA_TYPE_OTHER_ACTIONS",
        "DATA_TYPE_WEB_BROWSING_HISTORY",
        "DATA_TYPE_CRASH_LOGS",
        "DATA_TYPE_PERFORMANCE_DIAGNOSTICS",
        "DATA_TYPE_OTHER_APP_PERFORMANCE_DATA",
        "DATA_TYPE_DEVICE_OR_OTHER_IDS",
    ]
    falsePositive: bool

@typing.type_check_only
class GoogleChecksRepoScanV1alphaSourceCode(typing_extensions.TypedDict, total=False):
    code: str
    endLine: int
    path: str
    startLine: int

@typing.type_check_only
class GoogleChecksReportV1alphaAnalyzeUploadRequest(
    typing_extensions.TypedDict, total=False
):
    appBinaryFileType: typing_extensions.Literal[
        "APP_BINARY_FILE_TYPE_UNSPECIFIED", "ANDROID_APK", "ANDROID_AAB", "IOS_IPA"
    ]
    codeReferenceId: str

@typing.type_check_only
class GoogleChecksReportV1alphaAppBundle(typing_extensions.TypedDict, total=False):
    bundleId: str
    codeReferenceId: str
    releaseType: typing_extensions.Literal[
        "APP_BUNDLE_RELEASE_TYPE_UNSPECIFIED", "PUBLIC", "PRE_RELEASE"
    ]
    version: str
    versionId: str

@typing.type_check_only
class GoogleChecksReportV1alphaCheck(typing_extensions.TypedDict, total=False):
    citations: _list[GoogleChecksReportV1alphaCheckCitation]
    evidence: GoogleChecksReportV1alphaCheckEvidence
    regionCodes: _list[str]
    severity: typing_extensions.Literal[
        "CHECK_SEVERITY_UNSPECIFIED", "PRIORITY", "POTENTIAL", "OPPORTUNITY"
    ]
    state: typing_extensions.Literal[
        "CHECK_STATE_UNSPECIFIED", "PASSED", "FAILED", "UNCHECKED"
    ]
    stateMetadata: GoogleChecksReportV1alphaCheckStateMetadata
    type: typing_extensions.Literal[
        "CHECK_TYPE_UNSPECIFIED",
        "STORE_LISTING_PRIVACY_POLICY_LINK_PRESENT",
        "PRIVACY_POLICY_UPDATE_DATE_RECENT",
        "PRIVACY_POLICY_GDPR_GENERAL_RULES",
        "PRIVACY_POLICY_CCPA_GENERAL_RULES",
        "PRIVACY_POLICY_COLLECTION_CATEGORIES_DATA_NOTICE",
        "PRIVACY_POLICY_PROCESSING_PURPOSE_DATA_NOTICE",
        "PRIVACY_POLICY_SHARING_CATEGORIES_DATA_NOTICE",
        "PRIVACY_POLICY_DATA_RETENTION_NOTICE",
        "PRIVACY_POLICY_CONTACT_DETAILS_NOTICE",
        "PRIVACY_POLICY_CHILDREN_GENERAL_RULES",
        "PRIVACY_POLICY_DATA_TYPE_PHONE_NUMBER",
        "PRIVACY_POLICY_DATA_TYPE_USER_ACCOUNT_INFO",
        "PRIVACY_POLICY_DATA_TYPE_PRECISE_LOCATION",
        "PRIVACY_POLICY_DATA_TYPE_DEVICE_ID",
        "PRIVACY_POLICY_DATA_TYPE_APPS_ON_DEVICE",
        "PRIVACY_POLICY_DATA_TYPE_CONTACTS",
        "PRIVACY_POLICY_DATA_TYPE_TEXT_MESSAGES",
        "PRIVACY_POLICY_DATA_TYPE_PII",
        "PRIVACY_POLICY_DATA_TYPE_PII_CATEGORIES",
        "PRIVACY_POLICY_DATA_TYPE_HEALTH_AND_BIOMETRIC",
        "PRIVACY_POLICY_BRAZIL_LGPD_GENERAL_RULES",
        "PRIVACY_POLICY_VIRGINIA_VCDPA_GENERAL_RULES",
        "PRIVACY_POLICY_AFFILIATION_MENTION",
        "PRIVACY_POLICY_RIGHT_TO_DELETE_NOTICE",
        "PRIVACY_POLICY_RIGHT_TO_ACCESS_NOTICE",
        "PRIVACY_POLICY_RIGHT_TO_RECTIFICATION_NOTICE",
        "PRIVACY_POLICY_RIGHT_TO_KNOW_ABOUT_SELLING_NOTICE",
        "PRIVACY_POLICY_RIGHT_TO_KNOW_ABOUT_SHARING_NOTICE",
        "PRIVACY_POLICY_RIGHT_TO_OPT_OUT_FROM_SELLING_NOTICE",
        "PRIVACY_POLICY_METHOD_TO_OPT_OUT_FROM_SELLING_OR_SHARING_NOTICE",
        "PRIVACY_POLICY_DATA_CONTROLLER_IDENTITY",
        "PRIVACY_POLICY_DPO_CONTACT_DETAILS",
        "PRIVACY_POLICY_RIGHT_TO_LODGE_A_COMPLAINT",
        "PRIVACY_POLICY_LEGAL_BASIS",
        "PRIVACY_POLICY_CHILDREN_INFO_COLLECTION",
        "PRIVACY_POLICY_CHILDREN_INFO_USAGE_PURPOSES",
        "PRIVACY_POLICY_CHILDREN_INFO_DISCLOSURE_PRACTICES",
        "PRIVACY_POLICY_CHILDREN_INFO_PUBLICITY",
        "PRIVACY_POLICY_PARENTS_METHOD_OF_INFO_DELETION",
        "PRIVACY_POLICY_PARENTS_METHOD_TO_INFO_REVIEW",
        "PRIVACY_POLICY_PARENTS_METHOD_TO_STOP_FURTHER_INFO_COLLECTION_USE",
        "PRIVACY_POLICY_PARENTS_RIGHT_TO_INFO_DELETION",
        "PRIVACY_POLICY_PARENTS_RIGHT_TO_INFO_REVIEW",
        "PRIVACY_POLICY_PARENTS_RIGHT_TO_STOP_FURTHER_INFO_COLLECTION_USE",
        "PRIVACY_POLICY_PSL_APPROXIMATE_LOCATION",
        "PRIVACY_POLICY_PSL_PRECISE_LOCATION",
        "PRIVACY_POLICY_PSL_NAME",
        "PRIVACY_POLICY_PSL_EMAIL_ADDRESS",
        "PRIVACY_POLICY_PSL_USER_IDENTIFIERS",
        "PRIVACY_POLICY_PSL_ADDRESS",
        "PRIVACY_POLICY_PSL_PHONE_NUMBER",
        "PRIVACY_POLICY_PSL_RACE_AND_ETHNICITY",
        "PRIVACY_POLICY_PSL_CREDIT_SCORE",
        "PRIVACY_POLICY_PSL_PURCHASE_HISTORY",
        "PRIVACY_POLICY_PSL_HEALTH_INFO",
        "PRIVACY_POLICY_PSL_FITNESS_INFO",
        "PRIVACY_POLICY_PSL_EMAIL_MESSAGES",
        "PRIVACY_POLICY_PSL_TEXT_MESSAGES",
        "PRIVACY_POLICY_PSL_PHOTOS",
        "PRIVACY_POLICY_PSL_VIDEOS",
        "PRIVACY_POLICY_PSL_MUSIC_FILES",
        "PRIVACY_POLICY_PSL_VOICE_OR_SOUND_RECORDINGS",
        "PRIVACY_POLICY_PSL_FILES_AND_DOCS",
        "PRIVACY_POLICY_PSL_CALENDAR_EVENTS",
        "PRIVACY_POLICY_PSL_CONTACTS",
        "PRIVACY_POLICY_PSL_APP_INTERACTIONS",
        "PRIVACY_POLICY_PSL_IN_APP_SEARCH_HISTORY",
        "PRIVACY_POLICY_PSL_WEB_BROWSING_HISTORY",
        "PRIVACY_POLICY_PSL_INSTALLED_APPS",
        "PRIVACY_POLICY_PSL_CRASH_LOGS",
        "PRIVACY_POLICY_PSL_DIAGNOSTICS",
        "PRIVACY_POLICY_PSL_DEVICE_OR_OTHER_IDS",
        "DATA_MONITORING_NEW_ENDPOINT",
        "DATA_MONITORING_NEW_PERMISSION",
        "DATA_MONITORING_NEW_DATA_TYPE",
        "DATA_MONITORING_NEW_SDK",
        "DATA_MONITORING_ENCRYPTION",
        "DATA_MONITORING_NEW_DATA_TYPE_VERSION_DIFF",
        "DATA_MONITORING_NEW_ENDPOINT_VERSION_DIFF",
        "DATA_MONITORING_NEW_PERMISSION_VERSION_DIFF",
        "DATA_MONITORING_NEW_SDK_VERSION_DIFF",
        "DATA_MONITORING_SDKS_DENYLIST_VIOLATION",
        "DATA_MONITORING_PERMISSIONS_DENYLIST_VIOLATION",
        "DATA_MONITORING_ENDPOINTS_DENYLIST_VIOLATION",
        "DATA_MONITORING_OUTDATED_SDK_VERSION",
        "DATA_MONITORING_CRITICAL_SDK_ISSUE",
        "PRIVACY_POLICY_DATA_TYPE_SENSITIVE_INFO",
        "DATA_MONITORING_PII_LOGCAT_LEAK",
        "DATA_MONITORING_MINIMIZE_PERMISSION_MEDIA",
        "DATA_MONITORING_MINIMIZE_PERMISSION_CAMERA",
        "DATA_MONITORING_MINIMIZE_PERMISSION_DOCUMENTS",
    ]

@typing.type_check_only
class GoogleChecksReportV1alphaCheckCitation(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "CITATION_TYPE_UNSPECIFIED",
        "COPPA",
        "GDPR",
        "FERPA",
        "CAL_OPPA",
        "CCPA",
        "SOPIPA",
        "LGPD",
        "CPRA",
        "VCDPA",
        "GOOGLE_PLAY_POLICY",
        "APP_STORE_POLICY",
        "CPA",
        "CTDPA",
        "UCPA",
        "PIPEDA",
        "ALBERTA_PIPA",
        "QUEBEC_ACT",
        "QUEBEC_BILL_64",
        "CHINA_PIPL",
        "SOUTH_KOREA_PIPA",
        "SOUTH_AFRICA_POPIA",
        "JAPAN_APPI",
        "INDIA_DPDPA",
        "OCPA",
        "TDPSA",
        "MCDPA",
    ]

@typing.type_check_only
class GoogleChecksReportV1alphaCheckDataSecurityEvidence(
    typing_extensions.TypedDict, total=False
):
    dataInTransitInfo: _list[
        GoogleChecksReportV1alphaCheckDataSecurityEvidenceDataInTransitInfo
    ]

@typing.type_check_only
class GoogleChecksReportV1alphaCheckDataSecurityEvidenceDataInTransitInfo(
    typing_extensions.TypedDict, total=False
):
    uri: str

@typing.type_check_only
class GoogleChecksReportV1alphaCheckDataTypeEvidence(
    typing_extensions.TypedDict, total=False
):
    dataType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "DATA_TYPE_APPROXIMATE_LOCATION",
        "DATA_TYPE_PRECISE_LOCATION",
        "DATA_TYPE_PERSONAL_NAME",
        "DATA_TYPE_EMAIL_ADDRESS",
        "DATA_TYPE_USER_IDS",
        "DATA_TYPE_PHYSICAL_ADDRESS",
        "DATA_TYPE_PHONE_NUMBER",
        "DATA_TYPE_RACE_AND_ETHNICITY",
        "DATA_TYPE_POLITICAL_OR_RELIGIOUS_BELIEFS",
        "DATA_TYPE_SEXUAL_ORIENTATION",
        "DATA_TYPE_OTHER_PERSONAL_INFO",
        "DATA_TYPE_PAYMENT_INFO",
        "DATA_TYPE_PURCHASE_HISTORY",
        "DATA_TYPE_CREDIT_SCORE",
        "DATA_TYPE_OTHER_FINANCIAL_INFO",
        "DATA_TYPE_HEALTH_INFO",
        "DATA_TYPE_FITNESS_INFO",
        "DATA_TYPE_EMAILS",
        "DATA_TYPE_TEXT_MESSAGES",
        "DATA_TYPE_OTHER_IN_APP_MESSAGES",
        "DATA_TYPE_PHOTOS",
        "DATA_TYPE_VIDEOS",
        "DATA_TYPE_VOICE_OR_SOUND_RECORDINGS",
        "DATA_TYPE_MUSIC_FILES",
        "DATA_TYPE_OTHER_AUDIO_FILES",
        "DATA_TYPE_FILES_AND_DOCS",
        "DATA_TYPE_CALENDAR_EVENTS",
        "DATA_TYPE_CONTACTS",
        "DATA_TYPE_APP_INTERACTIONS",
        "DATA_TYPE_IN_APP_SEARCH_HISTORY",
        "DATA_TYPE_INSTALLED_APPS",
        "DATA_TYPE_OTHER_USER_GENERATED_CONTENT",
        "DATA_TYPE_OTHER_ACTIONS",
        "DATA_TYPE_WEB_BROWSING_HISTORY",
        "DATA_TYPE_CRASH_LOGS",
        "DATA_TYPE_PERFORMANCE_DIAGNOSTICS",
        "DATA_TYPE_OTHER_APP_PERFORMANCE_DATA",
        "DATA_TYPE_DEVICE_OR_OTHER_IDS",
    ]
    dataTypeEvidence: GoogleChecksReportV1alphaDataTypeEvidence

@typing.type_check_only
class GoogleChecksReportV1alphaCheckEndpointEvidence(
    typing_extensions.TypedDict, total=False
):
    endpoint: GoogleChecksReportV1alphaEndpoint

@typing.type_check_only
class GoogleChecksReportV1alphaCheckEndpointRestrictionViolationEvidence(
    typing_extensions.TypedDict, total=False
):
    endpointDetails: _list[
        GoogleChecksReportV1alphaCheckEndpointRestrictionViolationEvidenceEndpointDetails
    ]

@typing.type_check_only
class GoogleChecksReportV1alphaCheckEndpointRestrictionViolationEvidenceEndpointDetails(
    typing_extensions.TypedDict, total=False
):
    endpoint: GoogleChecksReportV1alphaEndpoint

@typing.type_check_only
class GoogleChecksReportV1alphaCheckEvidence(typing_extensions.TypedDict, total=False):
    dataSecurity: GoogleChecksReportV1alphaCheckDataSecurityEvidence
    dataTypes: _list[GoogleChecksReportV1alphaCheckDataTypeEvidence]
    endpointRestrictionViolations: _list[
        GoogleChecksReportV1alphaCheckEndpointRestrictionViolationEvidence
    ]
    endpoints: _list[GoogleChecksReportV1alphaCheckEndpointEvidence]
    permissionRestrictionViolations: _list[
        GoogleChecksReportV1alphaCheckPermissionRestrictionViolationEvidence
    ]
    permissions: _list[GoogleChecksReportV1alphaCheckPermissionEvidence]
    privacyPolicyTexts: _list[GoogleChecksReportV1alphaCheckPrivacyPolicyTextEvidence]
    sdkIssues: _list[GoogleChecksReportV1alphaCheckSdkIssueEvidence]
    sdkRestrictionViolations: _list[
        GoogleChecksReportV1alphaCheckSdkRestrictionViolationEvidence
    ]
    sdks: _list[GoogleChecksReportV1alphaCheckSdkEvidence]

@typing.type_check_only
class GoogleChecksReportV1alphaCheckPermissionEvidence(
    typing_extensions.TypedDict, total=False
):
    permission: GoogleChecksReportV1alphaPermission

@typing.type_check_only
class GoogleChecksReportV1alphaCheckPermissionRestrictionViolationEvidence(
    typing_extensions.TypedDict, total=False
):
    permissionDetails: _list[
        GoogleChecksReportV1alphaCheckPermissionRestrictionViolationEvidencePermissionDetails
    ]

@typing.type_check_only
class GoogleChecksReportV1alphaCheckPermissionRestrictionViolationEvidencePermissionDetails(
    typing_extensions.TypedDict, total=False
):
    permission: GoogleChecksReportV1alphaPermission

@typing.type_check_only
class GoogleChecksReportV1alphaCheckPrivacyPolicyTextEvidence(
    typing_extensions.TypedDict, total=False
):
    policyFragment: GoogleChecksReportV1alphaPolicyFragment

@typing.type_check_only
class GoogleChecksReportV1alphaCheckSdkEvidence(
    typing_extensions.TypedDict, total=False
):
    sdk: GoogleChecksReportV1alphaSdk

@typing.type_check_only
class GoogleChecksReportV1alphaCheckSdkIssueEvidence(
    typing_extensions.TypedDict, total=False
):
    sdk: GoogleChecksReportV1alphaSdk
    sdkVersion: str

@typing.type_check_only
class GoogleChecksReportV1alphaCheckSdkRestrictionViolationEvidence(
    typing_extensions.TypedDict, total=False
):
    sdkDetails: _list[
        GoogleChecksReportV1alphaCheckSdkRestrictionViolationEvidenceSdkDetails
    ]

@typing.type_check_only
class GoogleChecksReportV1alphaCheckSdkRestrictionViolationEvidenceSdkDetails(
    typing_extensions.TypedDict, total=False
):
    sdk: GoogleChecksReportV1alphaSdk

@typing.type_check_only
class GoogleChecksReportV1alphaCheckStateMetadata(
    typing_extensions.TypedDict, total=False
):
    badges: _list[
        typing_extensions.Literal[
            "CHECK_STATE_BADGE_UNSPECIFIED",
            "NEWLY_FAILING",
            "RECENTLY_FAILING",
            "RESOLVED",
        ]
    ]
    firstFailingTime: str
    lastFailingTime: str

@typing.type_check_only
class GoogleChecksReportV1alphaDataMonitoring(typing_extensions.TypedDict, total=False):
    dataTypes: _list[GoogleChecksReportV1alphaDataMonitoringDataTypeResult]
    endpoints: _list[GoogleChecksReportV1alphaDataMonitoringEndpointResult]
    permissions: _list[GoogleChecksReportV1alphaDataMonitoringPermissionResult]
    sdks: _list[GoogleChecksReportV1alphaDataMonitoringSdkResult]

@typing.type_check_only
class GoogleChecksReportV1alphaDataMonitoringDataTypeResult(
    typing_extensions.TypedDict, total=False
):
    dataType: typing_extensions.Literal[
        "DATA_TYPE_UNSPECIFIED",
        "DATA_TYPE_APPROXIMATE_LOCATION",
        "DATA_TYPE_PRECISE_LOCATION",
        "DATA_TYPE_PERSONAL_NAME",
        "DATA_TYPE_EMAIL_ADDRESS",
        "DATA_TYPE_USER_IDS",
        "DATA_TYPE_PHYSICAL_ADDRESS",
        "DATA_TYPE_PHONE_NUMBER",
        "DATA_TYPE_RACE_AND_ETHNICITY",
        "DATA_TYPE_POLITICAL_OR_RELIGIOUS_BELIEFS",
        "DATA_TYPE_SEXUAL_ORIENTATION",
        "DATA_TYPE_OTHER_PERSONAL_INFO",
        "DATA_TYPE_PAYMENT_INFO",
        "DATA_TYPE_PURCHASE_HISTORY",
        "DATA_TYPE_CREDIT_SCORE",
        "DATA_TYPE_OTHER_FINANCIAL_INFO",
        "DATA_TYPE_HEALTH_INFO",
        "DATA_TYPE_FITNESS_INFO",
        "DATA_TYPE_EMAILS",
        "DATA_TYPE_TEXT_MESSAGES",
        "DATA_TYPE_OTHER_IN_APP_MESSAGES",
        "DATA_TYPE_PHOTOS",
        "DATA_TYPE_VIDEOS",
        "DATA_TYPE_VOICE_OR_SOUND_RECORDINGS",
        "DATA_TYPE_MUSIC_FILES",
        "DATA_TYPE_OTHER_AUDIO_FILES",
        "DATA_TYPE_FILES_AND_DOCS",
        "DATA_TYPE_CALENDAR_EVENTS",
        "DATA_TYPE_CONTACTS",
        "DATA_TYPE_APP_INTERACTIONS",
        "DATA_TYPE_IN_APP_SEARCH_HISTORY",
        "DATA_TYPE_INSTALLED_APPS",
        "DATA_TYPE_OTHER_USER_GENERATED_CONTENT",
        "DATA_TYPE_OTHER_ACTIONS",
        "DATA_TYPE_WEB_BROWSING_HISTORY",
        "DATA_TYPE_CRASH_LOGS",
        "DATA_TYPE_PERFORMANCE_DIAGNOSTICS",
        "DATA_TYPE_OTHER_APP_PERFORMANCE_DATA",
        "DATA_TYPE_DEVICE_OR_OTHER_IDS",
    ]
    dataTypeEvidence: GoogleChecksReportV1alphaDataTypeEvidence
    metadata: GoogleChecksReportV1alphaDataMonitoringResultMetadata

@typing.type_check_only
class GoogleChecksReportV1alphaDataMonitoringEndpointResult(
    typing_extensions.TypedDict, total=False
):
    endpoint: GoogleChecksReportV1alphaEndpoint
    hitCount: int
    metadata: GoogleChecksReportV1alphaDataMonitoringResultMetadata

@typing.type_check_only
class GoogleChecksReportV1alphaDataMonitoringPermissionResult(
    typing_extensions.TypedDict, total=False
):
    metadata: GoogleChecksReportV1alphaDataMonitoringResultMetadata
    permission: GoogleChecksReportV1alphaPermission

@typing.type_check_only
class GoogleChecksReportV1alphaDataMonitoringResultMetadata(
    typing_extensions.TypedDict, total=False
):
    badges: _list[
        typing_extensions.Literal["DATA_MONITORING_RESULT_BADGE_UNSPECIFIED", "NEW"]
    ]
    firstDetectedTime: str
    lastDetectedAppVersion: str
    lastDetectedTime: str

@typing.type_check_only
class GoogleChecksReportV1alphaDataMonitoringSdkResult(
    typing_extensions.TypedDict, total=False
):
    metadata: GoogleChecksReportV1alphaDataMonitoringResultMetadata
    sdk: GoogleChecksReportV1alphaSdk

@typing.type_check_only
class GoogleChecksReportV1alphaDataTypeEndpointEvidence(
    typing_extensions.TypedDict, total=False
):
    attributedSdks: _list[
        GoogleChecksReportV1alphaDataTypeEndpointEvidenceAttributedSdk
    ]
    endpointDetails: _list[
        GoogleChecksReportV1alphaDataTypeEndpointEvidenceEndpointDetails
    ]
    exfiltratedDataType: typing_extensions.Literal[
        "EXFILTRATED_DATA_TYPE_UNSPECIFIED",
        "EXFILTRATED_DATA_TYPE_PHONE_NUMBER",
        "EXFILTRATED_DATA_TYPE_PRECISE_LOCATION",
        "EXFILTRATED_DATA_TYPE_CONTACT_NAME",
        "EXFILTRATED_DATA_TYPE_CONTACT_EMAIL",
        "EXFILTRATED_DATA_TYPE_CONTACT_PHONE_NUMBER",
        "EXFILTRATED_DATA_TYPE_INCOMING_TEXT_NUMBER",
        "EXFILTRATED_DATA_TYPE_INCOMING_TEXT_MESSAGE",
        "EXFILTRATED_DATA_TYPE_OUTGOING_TEXT_NUMBER",
        "EXFILTRATED_DATA_TYPE_OUTGOING_TEXT_MESSAGE",
        "EXFILTRATED_DATA_TYPE_ADVERTISING_ID",
        "EXFILTRATED_DATA_TYPE_ANDROID_ID",
        "EXFILTRATED_DATA_TYPE_IMEI",
        "EXFILTRATED_DATA_TYPE_IMSI",
        "EXFILTRATED_DATA_TYPE_SIM_SERIAL_NUMBER",
        "EXFILTRATED_DATA_TYPE_SSID",
        "EXFILTRATED_DATA_TYPE_ACCOUNT",
        "EXFILTRATED_DATA_TYPE_EXTERNAL_ACCOUNT",
        "EXFILTRATED_DATA_TYPE_INSTALLED_PACKAGES",
    ]

@typing.type_check_only
class GoogleChecksReportV1alphaDataTypeEndpointEvidenceAttributedSdk(
    typing_extensions.TypedDict, total=False
):
    sdk: GoogleChecksReportV1alphaSdk

@typing.type_check_only
class GoogleChecksReportV1alphaDataTypeEndpointEvidenceEndpointDetails(
    typing_extensions.TypedDict, total=False
):
    endpoint: GoogleChecksReportV1alphaEndpoint

@typing.type_check_only
class GoogleChecksReportV1alphaDataTypeEvidence(
    typing_extensions.TypedDict, total=False
):
    endpoints: _list[GoogleChecksReportV1alphaDataTypeEndpointEvidence]
    permissions: _list[GoogleChecksReportV1alphaDataTypePermissionEvidence]
    privacyPolicyTexts: _list[
        GoogleChecksReportV1alphaDataTypePrivacyPolicyTextEvidence
    ]

@typing.type_check_only
class GoogleChecksReportV1alphaDataTypePermissionEvidence(
    typing_extensions.TypedDict, total=False
):
    permission: GoogleChecksReportV1alphaPermission

@typing.type_check_only
class GoogleChecksReportV1alphaDataTypePrivacyPolicyTextEvidence(
    typing_extensions.TypedDict, total=False
):
    policyFragment: GoogleChecksReportV1alphaPolicyFragment

@typing.type_check_only
class GoogleChecksReportV1alphaEndpoint(typing_extensions.TypedDict, total=False):
    domain: str

@typing.type_check_only
class GoogleChecksReportV1alphaListReportsResponse(
    typing_extensions.TypedDict, total=False
):
    nextPageToken: str
    reports: _list[GoogleChecksReportV1alphaReport]

@typing.type_check_only
class GoogleChecksReportV1alphaPermission(typing_extensions.TypedDict, total=False):
    id: str

@typing.type_check_only
class GoogleChecksReportV1alphaPolicyFragment(typing_extensions.TypedDict, total=False):
    htmlContent: str
    sourceUri: str

@typing.type_check_only
class GoogleChecksReportV1alphaReport(typing_extensions.TypedDict, total=False):
    appBundle: GoogleChecksReportV1alphaAppBundle
    checks: _list[GoogleChecksReportV1alphaCheck]
    dataMonitoring: GoogleChecksReportV1alphaDataMonitoring
    name: str
    resultsUri: str

@typing.type_check_only
class GoogleChecksReportV1alphaSdk(typing_extensions.TypedDict, total=False):
    id: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
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

@typing.type_check_only
class WaitOperationRequest(typing_extensions.TypedDict, total=False):
    timeout: str

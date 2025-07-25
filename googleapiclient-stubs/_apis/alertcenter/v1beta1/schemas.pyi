import typing

import typing_extensions

_list = list

@typing.type_check_only
class AbuseDetected(typing_extensions.TypedDict, total=False):
    additionalDetails: EntityList
    product: str
    subAlertId: str
    variationType: typing_extensions.Literal[
        "ABUSE_DETECTED_VARIATION_TYPE_UNSPECIFIED",
        "DRIVE_ABUSIVE_CONTENT",
        "LIMITED_DISABLE",
    ]

@typing.type_check_only
class AccessApproval(typing_extensions.TypedDict, total=False):
    justificationReason: _list[
        typing_extensions.Literal[
            "JUSTIFICATION_UNSPECIFIED",
            "CUSTOMER_INITIATED_SUPPORT",
            "GOOGLE_INITIATED_REVIEW",
            "GOOGLE_INITIATED_SERVICE",
            "THIRD_PARTY_DATA_REQUEST",
            "GOOGLE_RESPONSE_TO_PRODUCTION_ALERT",
        ]
    ]
    officeLocation: str
    products: _list[str]
    requestId: str
    scope: str
    tickets: _list[SupportTicket]

@typing.type_check_only
class AccountSuspensionDetails(typing_extensions.TypedDict, total=False):
    abuseReason: typing_extensions.Literal[
        "ACCOUNT_SUSPENSION_ABUSE_REASON_UNSPECIFIED",
        "TOS_VIOLATION",
        "SPAM",
        "PHISHING",
        "TRAFFIC_PUMPING",
        "FRAUD",
        "NUMBER_HARVESTING",
        "PAYMENTS_FRAUD",
        "UNWANTED_CONTENT",
    ]
    productName: str

@typing.type_check_only
class AccountSuspensionWarning(typing_extensions.TypedDict, total=False):
    appealWindow: str
    state: typing_extensions.Literal[
        "ACCOUNT_SUSPENSION_WARNING_STATE_UNSPECIFIED",
        "WARNING",
        "SUSPENDED",
        "APPEAL_APPROVED",
        "APPEAL_SUBMITTED",
    ]
    suspensionDetails: _list[AccountSuspensionDetails]

@typing.type_check_only
class AccountWarning(typing_extensions.TypedDict, total=False):
    email: str
    loginDetails: LoginDetails

@typing.type_check_only
class ActionInfo(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ActivityRule(typing_extensions.TypedDict, total=False):
    actionNames: _list[str]
    createTime: str
    description: str
    displayName: str
    name: str
    query: str
    supersededAlerts: _list[str]
    supersedingAlert: str
    threshold: str
    triggerSource: str
    updateTime: str
    windowSize: str

@typing.type_check_only
class Alert(typing_extensions.TypedDict, total=False):
    alertId: str
    createTime: str
    customerId: str
    data: dict[str, typing.Any]
    deleted: bool
    endTime: str
    etag: str
    metadata: AlertMetadata
    securityInvestigationToolLink: str
    source: str
    startTime: str
    type: str
    updateTime: str

@typing.type_check_only
class AlertFeedback(typing_extensions.TypedDict, total=False):
    alertId: str
    createTime: str
    customerId: str
    email: str
    feedbackId: str
    type: typing_extensions.Literal[
        "ALERT_FEEDBACK_TYPE_UNSPECIFIED",
        "NOT_USEFUL",
        "SOMEWHAT_USEFUL",
        "VERY_USEFUL",
    ]

@typing.type_check_only
class AlertMetadata(typing_extensions.TypedDict, total=False):
    alertId: str
    assignee: str
    customerId: str
    etag: str
    severity: str
    status: str
    updateTime: str

@typing.type_check_only
class ApnsCertificateExpirationInfo(typing_extensions.TypedDict, total=False):
    appleId: str
    expirationTime: str
    uid: str

@typing.type_check_only
class AppMakerSqlSetupNotification(typing_extensions.TypedDict, total=False):
    requestInfo: _list[RequestInfo]

@typing.type_check_only
class AppSettingsChanged(typing_extensions.TypedDict, total=False):
    alertDetails: str
    name: str

@typing.type_check_only
class AppsOutage(typing_extensions.TypedDict, total=False):
    dashboardUri: str
    incidentTrackingId: str
    mergeInfo: MergeInfo
    nextUpdateTime: str
    products: _list[str]
    resolutionTime: str
    status: typing_extensions.Literal[
        "STATUS_UNSPECIFIED",
        "NEW",
        "ONGOING",
        "RESOLVED",
        "FALSE_POSITIVE",
        "PARTIALLY_RESOLVED",
        "MERGED",
        "DOWNGRADED",
    ]

@typing.type_check_only
class Attachment(typing_extensions.TypedDict, total=False):
    csv: Csv

@typing.type_check_only
class BadWhitelist(typing_extensions.TypedDict, total=False):
    domainId: DomainId
    maliciousEntity: MaliciousEntity
    messages: _list[GmailMessageInfo]
    sourceIp: str

@typing.type_check_only
class BatchDeleteAlertsRequest(typing_extensions.TypedDict, total=False):
    alertId: _list[str]
    customerId: str

@typing.type_check_only
class BatchDeleteAlertsResponse(typing_extensions.TypedDict, total=False):
    failedAlertStatus: dict[str, typing.Any]
    successAlertIds: _list[str]

@typing.type_check_only
class BatchUndeleteAlertsRequest(typing_extensions.TypedDict, total=False):
    alertId: _list[str]
    customerId: str

@typing.type_check_only
class BatchUndeleteAlertsResponse(typing_extensions.TypedDict, total=False):
    failedAlertStatus: dict[str, typing.Any]
    successAlertIds: _list[str]

@typing.type_check_only
class CloudPubsubTopic(typing_extensions.TypedDict, total=False):
    payloadFormat: typing_extensions.Literal["PAYLOAD_FORMAT_UNSPECIFIED", "JSON"]
    topicName: str

@typing.type_check_only
class Csv(typing_extensions.TypedDict, total=False):
    dataRows: _list[CsvRow]
    headers: _list[str]

@typing.type_check_only
class CsvRow(typing_extensions.TypedDict, total=False):
    entries: _list[str]

@typing.type_check_only
class DeviceCompromised(typing_extensions.TypedDict, total=False):
    email: str
    events: _list[DeviceCompromisedSecurityDetail]

@typing.type_check_only
class DeviceCompromisedSecurityDetail(typing_extensions.TypedDict, total=False):
    deviceCompromisedState: str
    deviceId: str
    deviceModel: str
    deviceType: str
    iosVendorId: str
    resourceId: str
    serialNumber: str

@typing.type_check_only
class DeviceManagementRule(typing_extensions.TypedDict, total=False):
    deviceId: str
    deviceModel: str
    deviceType: str
    email: str
    id: str
    iosVendorId: str
    ownerId: str
    resourceId: str
    ruleAction: str
    serialNumber: str

@typing.type_check_only
class DlpRuleViolation(typing_extensions.TypedDict, total=False):
    ruleViolationInfo: RuleViolationInfo

@typing.type_check_only
class DomainId(typing_extensions.TypedDict, total=False):
    customerPrimaryDomain: str

@typing.type_check_only
class DomainWideTakeoutInitiated(typing_extensions.TypedDict, total=False):
    email: str
    takeoutRequestId: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Entity(typing_extensions.TypedDict, total=False):
    link: str
    name: str
    values: _list[str]

@typing.type_check_only
class EntityList(typing_extensions.TypedDict, total=False):
    entities: _list[Entity]
    headers: _list[str]
    name: str

@typing.type_check_only
class GmailMessageInfo(typing_extensions.TypedDict, total=False):
    attachmentsSha256Hash: _list[str]
    date: str
    md5HashMessageBody: str
    md5HashSubject: str
    messageBodySnippet: str
    messageId: str
    recipient: str
    sentTime: str
    subjectText: str

@typing.type_check_only
class GoogleOperations(typing_extensions.TypedDict, total=False):
    affectedUserEmails: _list[str]
    attachmentData: Attachment
    description: str
    domain: str
    header: str
    title: str

@typing.type_check_only
class ListAlertFeedbackResponse(typing_extensions.TypedDict, total=False):
    feedback: _list[AlertFeedback]

@typing.type_check_only
class ListAlertsResponse(typing_extensions.TypedDict, total=False):
    alerts: _list[Alert]
    nextPageToken: str

@typing.type_check_only
class LoginDetails(typing_extensions.TypedDict, total=False):
    ipAddress: str
    loginTime: str

@typing.type_check_only
class MailPhishing(typing_extensions.TypedDict, total=False):
    domainId: DomainId
    isInternal: bool
    maliciousEntity: MaliciousEntity
    messages: _list[GmailMessageInfo]
    systemActionType: typing_extensions.Literal[
        "SYSTEM_ACTION_TYPE_UNSPECIFIED", "NO_OPERATION", "REMOVED_FROM_INBOX"
    ]

@typing.type_check_only
class MaliciousEntity(typing_extensions.TypedDict, total=False):
    displayName: str
    entity: User
    fromHeader: str

@typing.type_check_only
class MandatoryServiceAnnouncement(typing_extensions.TypedDict, total=False):
    description: str
    title: str

@typing.type_check_only
class MatchInfo(typing_extensions.TypedDict, total=False):
    predefinedDetector: PredefinedDetectorInfo
    userDefinedDetector: UserDefinedDetectorInfo

@typing.type_check_only
class MergeInfo(typing_extensions.TypedDict, total=False):
    newAlertId: str
    newIncidentTrackingId: str

@typing.type_check_only
class Notification(typing_extensions.TypedDict, total=False):
    cloudPubsubTopic: CloudPubsubTopic

@typing.type_check_only
class PhishingSpike(typing_extensions.TypedDict, total=False):
    domainId: DomainId
    isInternal: bool
    maliciousEntity: MaliciousEntity
    messages: _list[GmailMessageInfo]

@typing.type_check_only
class PredefinedDetectorInfo(typing_extensions.TypedDict, total=False):
    detectorName: str

@typing.type_check_only
class PrimaryAdminChangedEvent(typing_extensions.TypedDict, total=False):
    domain: str
    previousAdminEmail: str
    updatedAdminEmail: str

@typing.type_check_only
class ReportingRule(typing_extensions.TypedDict, total=False):
    alertDetails: str
    name: str
    query: str

@typing.type_check_only
class RequestInfo(typing_extensions.TypedDict, total=False):
    appDeveloperEmail: _list[str]
    appKey: str
    numberOfRequests: str

@typing.type_check_only
class ResourceInfo(typing_extensions.TypedDict, total=False):
    chatAttachmentId: str
    chatMessageId: str
    deviceId: str
    documentId: str
    resourceTitle: str

@typing.type_check_only
class RuleInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    resourceName: str

@typing.type_check_only
class RuleViolationInfo(typing_extensions.TypedDict, total=False):
    dataSource: typing_extensions.Literal[
        "DATA_SOURCE_UNSPECIFIED", "DRIVE", "CHROME", "CHAT"
    ]
    eventType: typing_extensions.Literal[
        "EVENT_TYPE_UNSPECIFIED", "ACCESS_BLOCKED", "SHARING_BLOCKED"
    ]
    matchInfo: _list[MatchInfo]
    recipients: _list[str]
    resourceInfo: ResourceInfo
    ruleInfo: RuleInfo
    suppressedActionTypes: _list[
        typing_extensions.Literal[
            "ACTION_TYPE_UNSPECIFIED",
            "DRIVE_BLOCK_EXTERNAL_SHARING",
            "DRIVE_WARN_ON_EXTERNAL_SHARING",
            "DRIVE_RESTRICT_DOWNLOAD_PRINT_COPY",
            "DRIVE_APPLY_DRIVE_LABELS",
            "CHROME_BLOCK_FILE_DOWNLOAD",
            "CHROME_WARN_FILE_DOWNLOAD",
            "CHROME_BLOCK_FILE_UPLOAD",
            "CHROME_WARN_FILE_UPLOAD",
            "CHROME_BLOCK_WEB_CONTENT_UPLOAD",
            "CHROME_WARN_WEB_CONTENT_UPLOAD",
            "CHROME_BLOCK_PAGE_PRINT",
            "CHROME_WARN_PAGE_PRINT",
            "CHROME_BLOCK_URL_VISITED",
            "CHROME_WARN_URL_VISITED",
            "CHROME_BLOCK_SCREENSHOT",
            "CHROME_STORE_CONTENT",
            "DELETE_WEBPROTECT_EVIDENCE",
            "CHAT_BLOCK_CONTENT",
            "CHAT_WARN_USER",
            "ALERT",
            "RULE_ACTIVATE",
            "RULE_DEACTIVATE",
        ]
    ]
    trigger: typing_extensions.Literal[
        "TRIGGER_UNSPECIFIED",
        "DRIVE_SHARE",
        "CHROME_FILE_DOWNLOAD",
        "CHROME_FILE_UPLOAD",
        "CHROME_WEB_CONTENT_UPLOAD",
        "CHAT_MESSAGE_SENT",
        "CHAT_ATTACHMENT_UPLOADED",
        "CHROME_PAGE_PRINT",
        "CHROME_URL_VISITED",
    ]
    triggeredActionInfo: _list[ActionInfo]
    triggeredActionTypes: _list[
        typing_extensions.Literal[
            "ACTION_TYPE_UNSPECIFIED",
            "DRIVE_BLOCK_EXTERNAL_SHARING",
            "DRIVE_WARN_ON_EXTERNAL_SHARING",
            "DRIVE_RESTRICT_DOWNLOAD_PRINT_COPY",
            "DRIVE_APPLY_DRIVE_LABELS",
            "CHROME_BLOCK_FILE_DOWNLOAD",
            "CHROME_WARN_FILE_DOWNLOAD",
            "CHROME_BLOCK_FILE_UPLOAD",
            "CHROME_WARN_FILE_UPLOAD",
            "CHROME_BLOCK_WEB_CONTENT_UPLOAD",
            "CHROME_WARN_WEB_CONTENT_UPLOAD",
            "CHROME_BLOCK_PAGE_PRINT",
            "CHROME_WARN_PAGE_PRINT",
            "CHROME_BLOCK_URL_VISITED",
            "CHROME_WARN_URL_VISITED",
            "CHROME_BLOCK_SCREENSHOT",
            "CHROME_STORE_CONTENT",
            "DELETE_WEBPROTECT_EVIDENCE",
            "CHAT_BLOCK_CONTENT",
            "CHAT_WARN_USER",
            "ALERT",
            "RULE_ACTIVATE",
            "RULE_DEACTIVATE",
        ]
    ]
    triggeringUserEmail: str

@typing.type_check_only
class SSOProfileCreatedEvent(typing_extensions.TypedDict, total=False):
    inboundSsoProfileName: str

@typing.type_check_only
class SSOProfileDeletedEvent(typing_extensions.TypedDict, total=False):
    inboundSsoProfileName: str

@typing.type_check_only
class SSOProfileUpdatedEvent(typing_extensions.TypedDict, total=False):
    inboundSsoProfileChanges: str
    inboundSsoProfileName: str

@typing.type_check_only
class SensitiveAdminAction(typing_extensions.TypedDict, total=False):
    actorEmail: str
    eventTime: str
    primaryAdminChangedEvent: PrimaryAdminChangedEvent
    ssoProfileCreatedEvent: SSOProfileCreatedEvent
    ssoProfileDeletedEvent: SSOProfileDeletedEvent
    ssoProfileUpdatedEvent: SSOProfileUpdatedEvent
    superAdminPasswordResetEvent: SuperAdminPasswordResetEvent

@typing.type_check_only
class Settings(typing_extensions.TypedDict, total=False):
    notifications: _list[Notification]

@typing.type_check_only
class StateSponsoredAttack(typing_extensions.TypedDict, total=False):
    email: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SuperAdminPasswordResetEvent(typing_extensions.TypedDict, total=False):
    userEmail: str

@typing.type_check_only
class SupportTicket(typing_extensions.TypedDict, total=False):
    ticketId: str
    ticketUrl: str

@typing.type_check_only
class SuspiciousActivity(typing_extensions.TypedDict, total=False):
    email: str
    events: _list[SuspiciousActivitySecurityDetail]

@typing.type_check_only
class SuspiciousActivitySecurityDetail(typing_extensions.TypedDict, total=False):
    deviceId: str
    deviceModel: str
    deviceProperty: str
    deviceType: str
    iosVendorId: str
    newValue: str
    oldValue: str
    resourceId: str
    serialNumber: str

@typing.type_check_only
class TransferError(typing_extensions.TypedDict, total=False):
    email: str
    entityType: typing_extensions.Literal[
        "TRANSFER_ENTITY_TYPE_UNSPECIFIED",
        "TRANSFER_AUTO_ATTENDANT",
        "TRANSFER_RING_GROUP",
        "TRANSFER_USER",
    ]
    id: str
    invalidReason: typing_extensions.Literal[
        "TRANSFER_INVALID_REASON_UNSPECIFIED",
        "TRANSFER_TARGET_DELETED",
        "UNLICENSED",
        "SUSPENDED",
        "NO_PHONE_NUMBER",
    ]
    name: str

@typing.type_check_only
class TransferMisconfiguration(typing_extensions.TypedDict, total=False):
    errors: _list[TransferError]

@typing.type_check_only
class UndeleteAlertRequest(typing_extensions.TypedDict, total=False):
    customerId: str

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    displayName: str
    emailAddress: str

@typing.type_check_only
class UserChanges(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class UserDefinedDetectorInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    resourceName: str

@typing.type_check_only
class VaultAcceleratedDeletion(typing_extensions.TypedDict, total=False):
    actionType: typing_extensions.Literal[
        "VAULT_ACCELERATED_DELETION_ACTION_TYPE_UNSPECIFIED",
        "VAULT_ACCELERATED_DELETION_ACTION_TYPE_CREATE",
        "VAULT_ACCELERATED_DELETION_ACTION_TYPE_CANCEL",
    ]
    appType: typing_extensions.Literal[
        "VAULT_ACCELERATED_DELETION_APP_TYPE_UNSPECIFIED",
        "VAULT_ACCELERATED_DELETION_APP_TYPE_GMAIL",
    ]
    createTime: str
    deletionRequestId: str
    matterId: str

@typing.type_check_only
class VoiceMisconfiguration(typing_extensions.TypedDict, total=False):
    entityName: str
    entityType: typing_extensions.Literal[
        "ENTITY_TYPE_UNSPECIFIED", "AUTO_ATTENDANT", "RING_GROUP"
    ]
    fixUri: str
    membersMisconfiguration: TransferMisconfiguration
    transferMisconfiguration: TransferMisconfiguration
    voicemailMisconfiguration: VoicemailMisconfiguration

@typing.type_check_only
class VoicemailMisconfiguration(typing_extensions.TypedDict, total=False):
    errors: _list[VoicemailRecipientError]

@typing.type_check_only
class VoicemailRecipientError(typing_extensions.TypedDict, total=False):
    email: str
    invalidReason: typing_extensions.Literal[
        "EMAIL_INVALID_REASON_UNSPECIFIED", "OUT_OF_QUOTA", "RECIPIENT_DELETED"
    ]

import typing

import typing_extensions
@typing.type_check_only
class AccountWarning(typing_extensions.TypedDict, total=False):
    email: str
    loginDetails: LoginDetails

@typing.type_check_only
class ActivityRule(typing_extensions.TypedDict, total=False):
    actionNames: typing.List[str]
    createTime: str
    description: str
    displayName: str
    name: str
    query: str
    supersededAlerts: typing.List[str]
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
    data: typing.Dict[str, typing.Any]
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
class AppMakerSqlSetupNotification(typing_extensions.TypedDict, total=False):
    requestInfo: typing.List[RequestInfo]

@typing.type_check_only
class Attachment(typing_extensions.TypedDict, total=False):
    csv: Csv

@typing.type_check_only
class BadWhitelist(typing_extensions.TypedDict, total=False):
    domainId: DomainId
    maliciousEntity: MaliciousEntity
    messages: typing.List[GmailMessageInfo]
    sourceIp: str

@typing.type_check_only
class BatchDeleteAlertsRequest(typing_extensions.TypedDict, total=False):
    alertId: typing.List[str]
    customerId: str

@typing.type_check_only
class BatchDeleteAlertsResponse(typing_extensions.TypedDict, total=False):
    failedAlertStatus: typing.Dict[str, typing.Any]
    successAlertIds: typing.List[str]

@typing.type_check_only
class BatchUndeleteAlertsRequest(typing_extensions.TypedDict, total=False):
    alertId: typing.List[str]
    customerId: str

@typing.type_check_only
class BatchUndeleteAlertsResponse(typing_extensions.TypedDict, total=False):
    failedAlertStatus: typing.Dict[str, typing.Any]
    successAlertIds: typing.List[str]

@typing.type_check_only
class CloudPubsubTopic(typing_extensions.TypedDict, total=False):
    payloadFormat: typing_extensions.Literal["PAYLOAD_FORMAT_UNSPECIFIED", "JSON"]
    topicName: str

@typing.type_check_only
class Csv(typing_extensions.TypedDict, total=False):
    dataRows: typing.List[CsvRow]
    headers: typing.List[str]

@typing.type_check_only
class CsvRow(typing_extensions.TypedDict, total=False):
    entries: typing.List[str]

@typing.type_check_only
class DeviceCompromised(typing_extensions.TypedDict, total=False):
    email: str
    events: typing.List[DeviceCompromisedSecurityDetail]

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
class GmailMessageInfo(typing_extensions.TypedDict, total=False):
    attachmentsSha256Hash: typing.List[str]
    date: str
    md5HashMessageBody: str
    md5HashSubject: str
    messageBodySnippet: str
    messageId: str
    recipient: str
    subjectText: str

@typing.type_check_only
class GoogleOperations(typing_extensions.TypedDict, total=False):
    affectedUserEmails: typing.List[str]
    attachmentData: Attachment
    description: str
    header: str
    title: str

@typing.type_check_only
class ListAlertFeedbackResponse(typing_extensions.TypedDict, total=False):
    feedback: typing.List[AlertFeedback]

@typing.type_check_only
class ListAlertsResponse(typing_extensions.TypedDict, total=False):
    alerts: typing.List[Alert]
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
    messages: typing.List[GmailMessageInfo]
    systemActionType: typing_extensions.Literal[
        "SYSTEM_ACTION_TYPE_UNSPECIFIED", "NO_OPERATION", "REMOVED_FROM_INBOX"
    ]

@typing.type_check_only
class MaliciousEntity(typing_extensions.TypedDict, total=False):
    displayName: str
    entity: User
    fromHeader: str

@typing.type_check_only
class MatchInfo(typing_extensions.TypedDict, total=False):
    predefinedDetector: PredefinedDetectorInfo
    userDefinedDetector: UserDefinedDetectorInfo

@typing.type_check_only
class Notification(typing_extensions.TypedDict, total=False):
    cloudPubsubTopic: CloudPubsubTopic

@typing.type_check_only
class PhishingSpike(typing_extensions.TypedDict, total=False):
    domainId: DomainId
    isInternal: bool
    maliciousEntity: MaliciousEntity
    messages: typing.List[GmailMessageInfo]

@typing.type_check_only
class PredefinedDetectorInfo(typing_extensions.TypedDict, total=False):
    detectorName: str

@typing.type_check_only
class RequestInfo(typing_extensions.TypedDict, total=False):
    appDeveloperEmail: typing.List[str]
    appKey: str
    numberOfRequests: str

@typing.type_check_only
class ResourceInfo(typing_extensions.TypedDict, total=False):
    documentId: str
    resourceTitle: str

@typing.type_check_only
class RuleInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    resourceName: str

@typing.type_check_only
class RuleViolationInfo(typing_extensions.TypedDict, total=False):
    dataSource: typing_extensions.Literal["DATA_SOURCE_UNSPECIFIED", "DRIVE"]
    matchInfo: typing.List[MatchInfo]
    recipients: typing.List[str]
    resourceInfo: ResourceInfo
    ruleInfo: RuleInfo
    suppressedActionTypes: typing.List[str]
    trigger: typing_extensions.Literal["TRIGGER_UNSPECIFIED", "DRIVE_SHARE"]
    triggeredActionTypes: typing.List[str]
    triggeringUserEmail: str

@typing.type_check_only
class Settings(typing_extensions.TypedDict, total=False):
    notifications: typing.List[Notification]

@typing.type_check_only
class StateSponsoredAttack(typing_extensions.TypedDict, total=False):
    email: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

@typing.type_check_only
class SuspiciousActivity(typing_extensions.TypedDict, total=False):
    email: str
    events: typing.List[SuspiciousActivitySecurityDetail]

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
class UndeleteAlertRequest(typing_extensions.TypedDict, total=False):
    customerId: str

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    displayName: str
    emailAddress: str

@typing.type_check_only
class UserDefinedDetectorInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    resourceName: str

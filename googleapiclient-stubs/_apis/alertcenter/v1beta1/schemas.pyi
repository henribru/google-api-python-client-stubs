import typing

import typing_extensions

class PredefinedDetectorInfo(typing_extensions.TypedDict, total=False):
    detectorName: str

class LoginDetails(typing_extensions.TypedDict, total=False):
    ipAddress: str
    loginTime: str

class BatchUndeleteAlertsResponse(typing_extensions.TypedDict, total=False):
    failedAlertStatus: typing.Dict[str, typing.Any]
    successAlertIds: typing.List[str]

class ResourceInfo(typing_extensions.TypedDict, total=False):
    documentId: str
    resourceTitle: str

class RuleViolationInfo(typing_extensions.TypedDict, total=False):
    suppressedActionTypes: typing.List[str]
    dataSource: typing_extensions.Literal["DATA_SOURCE_UNSPECIFIED", "DRIVE"]
    trigger: typing_extensions.Literal["TRIGGER_UNSPECIFIED", "DRIVE_SHARE"]
    triggeringUserEmail: str
    recipients: typing.List[str]
    triggeredActionTypes: typing.List[str]
    resourceInfo: ResourceInfo
    matchInfo: typing.List[MatchInfo]
    ruleInfo: RuleInfo

class StateSponsoredAttack(typing_extensions.TypedDict, total=False):
    email: str

class BatchDeleteAlertsResponse(typing_extensions.TypedDict, total=False):
    failedAlertStatus: typing.Dict[str, typing.Any]
    successAlertIds: typing.List[str]

class ListAlertsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    alerts: typing.List[Alert]

class BadWhitelist(typing_extensions.TypedDict, total=False):
    messages: typing.List[GmailMessageInfo]
    sourceIp: str
    domainId: DomainId
    maliciousEntity: MaliciousEntity

class PhishingSpike(typing_extensions.TypedDict, total=False):
    messages: typing.List[GmailMessageInfo]
    domainId: DomainId
    isInternal: bool
    maliciousEntity: MaliciousEntity

class GmailMessageInfo(typing_extensions.TypedDict, total=False):
    date: str
    md5HashMessageBody: str
    messageBodySnippet: str
    messageId: str
    md5HashSubject: str
    recipient: str
    subjectText: str
    attachmentsSha256Hash: typing.List[str]

class AppMakerSqlSetupNotification(typing_extensions.TypedDict, total=False):
    requestInfo: typing.List[RequestInfo]

class User(typing_extensions.TypedDict, total=False):
    emailAddress: str
    displayName: str

class RuleInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    resourceName: str

class Csv(typing_extensions.TypedDict, total=False):
    dataRows: typing.List[CsvRow]
    headers: typing.List[str]

class MaliciousEntity(typing_extensions.TypedDict, total=False):
    fromHeader: str
    entity: User
    displayName: str

class Empty(typing_extensions.TypedDict, total=False): ...

class Settings(typing_extensions.TypedDict, total=False):
    notifications: typing.List[Notification]

class MailPhishing(typing_extensions.TypedDict, total=False):
    messages: typing.List[GmailMessageInfo]
    maliciousEntity: MaliciousEntity
    domainId: DomainId
    systemActionType: typing_extensions.Literal[
        "SYSTEM_ACTION_TYPE_UNSPECIFIED", "NO_OPERATION", "REMOVED_FROM_INBOX"
    ]
    isInternal: bool

class Notification(typing_extensions.TypedDict, total=False):
    cloudPubsubTopic: CloudPubsubTopic

class GoogleOperations(typing_extensions.TypedDict, total=False):
    affectedUserEmails: typing.List[str]
    title: str
    description: str
    attachmentData: Attachment

class AccountWarning(typing_extensions.TypedDict, total=False):
    loginDetails: LoginDetails
    email: str

class AlertMetadata(typing_extensions.TypedDict, total=False):
    assignee: str
    alertId: str
    etag: str
    customerId: str
    updateTime: str
    severity: str
    status: str

class SuspiciousActivity(typing_extensions.TypedDict, total=False):
    email: str
    events: typing.List[SuspiciousActivitySecurityDetail]

class DeviceCompromised(typing_extensions.TypedDict, total=False):
    email: str
    events: typing.List[DeviceCompromisedSecurityDetail]

class Attachment(typing_extensions.TypedDict, total=False):
    csv: Csv

class SuspiciousActivitySecurityDetail(typing_extensions.TypedDict, total=False):
    serialNumber: str
    resourceId: str
    deviceProperty: str
    newValue: str
    iosVendorId: str
    oldValue: str
    deviceType: str
    deviceModel: str
    deviceId: str

class DlpRuleViolation(typing_extensions.TypedDict, total=False):
    ruleViolationInfo: RuleViolationInfo

class DomainId(typing_extensions.TypedDict, total=False):
    customerPrimaryDomain: str

class ActivityRule(typing_extensions.TypedDict, total=False):
    actionNames: typing.List[str]
    name: str
    threshold: str
    supersedingAlert: str
    description: str
    updateTime: str
    supersededAlerts: typing.List[str]
    triggerSource: str
    createTime: str
    query: str
    displayName: str
    windowSize: str

class CloudPubsubTopic(typing_extensions.TypedDict, total=False):
    payloadFormat: typing_extensions.Literal["PAYLOAD_FORMAT_UNSPECIFIED", "JSON"]
    topicName: str

class DomainWideTakeoutInitiated(typing_extensions.TypedDict, total=False):
    takeoutRequestId: str
    email: str

class BatchUndeleteAlertsRequest(typing_extensions.TypedDict, total=False):
    alertId: typing.List[str]
    customerId: str

class AlertFeedback(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "ALERT_FEEDBACK_TYPE_UNSPECIFIED",
        "NOT_USEFUL",
        "SOMEWHAT_USEFUL",
        "VERY_USEFUL",
    ]
    createTime: str
    email: str
    alertId: str
    customerId: str
    feedbackId: str

class CsvRow(typing_extensions.TypedDict, total=False):
    entries: typing.List[str]

class MatchInfo(typing_extensions.TypedDict, total=False):
    predefinedDetector: PredefinedDetectorInfo
    userDefinedDetector: UserDefinedDetectorInfo

class UndeleteAlertRequest(typing_extensions.TypedDict, total=False):
    customerId: str

class UserDefinedDetectorInfo(typing_extensions.TypedDict, total=False):
    resourceName: str
    displayName: str

class DeviceCompromisedSecurityDetail(typing_extensions.TypedDict, total=False):
    iosVendorId: str
    deviceCompromisedState: str
    resourceId: str
    serialNumber: str
    deviceType: str
    deviceId: str
    deviceModel: str

class RequestInfo(typing_extensions.TypedDict, total=False):
    appDeveloperEmail: typing.List[str]
    appKey: str
    numberOfRequests: str

class ListAlertFeedbackResponse(typing_extensions.TypedDict, total=False):
    feedback: typing.List[AlertFeedback]

class BatchDeleteAlertsRequest(typing_extensions.TypedDict, total=False):
    alertId: typing.List[str]
    customerId: str

class Status(typing_extensions.TypedDict, total=False):
    code: int
    message: str
    details: typing.List[typing.Dict[str, typing.Any]]

class Alert(typing_extensions.TypedDict, total=False):
    updateTime: str
    metadata: AlertMetadata
    endTime: str
    customerId: str
    startTime: str
    securityInvestigationToolLink: str
    alertId: str
    etag: str
    data: typing.Dict[str, typing.Any]
    deleted: bool
    createTime: str
    type: str
    source: str

import typing

_list = list

@typing.type_check_only
class AccountCount(typing.TypedDict, total=False):
    account: UserInfo
    count: str

@typing.type_check_only
class AccountCountError(typing.TypedDict, total=False):
    account: UserInfo
    errorType: typing.Literal[
        "ERROR_TYPE_UNSPECIFIED",
        "WILDCARD_TOO_BROAD",
        "TOO_MANY_TERMS",
        "LOCATION_UNAVAILABLE",
        "UNKNOWN",
        "DEADLINE_EXCEEDED",
    ]

@typing.type_check_only
class AccountInfo(typing.TypedDict, total=False):
    emails: _list[str]

@typing.type_check_only
class AddHeldAccountResult(typing.TypedDict, total=False):
    account: HeldAccount
    status: Status

@typing.type_check_only
class AddHeldAccountsRequest(typing.TypedDict, total=False):
    accountIds: _list[str]
    emails: _list[str]

@typing.type_check_only
class AddHeldAccountsResponse(typing.TypedDict, total=False):
    responses: _list[AddHeldAccountResult]

@typing.type_check_only
class AddMatterPermissionsRequest(typing.TypedDict, total=False):
    ccMe: bool
    matterPermission: MatterPermission
    sendEmails: bool

@typing.type_check_only
class CalendarExportOptions(typing.TypedDict, total=False):
    exportFormat: typing.Literal[
        "EXPORT_FORMAT_UNSPECIFIED", "MBOX", "PST", "ICS", "XML", "JSON"
    ]

@typing.type_check_only
class CalendarOptions(typing.TypedDict, total=False):
    locationQuery: _list[str]
    minusWords: _list[str]
    peopleQuery: _list[str]
    responseStatuses: _list[
        typing.Literal[
            "ATTENDEE_RESPONSE_UNSPECIFIED",
            "ATTENDEE_RESPONSE_NEEDS_ACTION",
            "ATTENDEE_RESPONSE_ACCEPTED",
            "ATTENDEE_RESPONSE_DECLINED",
            "ATTENDEE_RESPONSE_TENTATIVE",
        ]
    ]
    versionDate: str

@typing.type_check_only
class CancelOperationRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CloseMatterRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CloseMatterResponse(typing.TypedDict, total=False):
    matter: Matter

@typing.type_check_only
class CloudStorageFile(typing.TypedDict, total=False):
    bucketName: str
    md5Hash: str
    objectName: str
    size: str

@typing.type_check_only
class CloudStorageSink(typing.TypedDict, total=False):
    files: _list[CloudStorageFile]

@typing.type_check_only
class CorpusQuery(typing.TypedDict, total=False):
    calendarQuery: HeldCalendarQuery
    driveQuery: HeldDriveQuery
    geminiQuery: HeldGeminiQuery
    groupsQuery: HeldGroupsQuery
    hangoutsChatQuery: HeldHangoutsChatQuery
    mailQuery: HeldMailQuery
    voiceQuery: HeldVoiceQuery

@typing.type_check_only
class CountArtifactsMetadata(typing.TypedDict, total=False):
    endTime: str
    matterId: str
    query: Query
    startTime: str

@typing.type_check_only
class CountArtifactsRequest(typing.TypedDict, total=False):
    query: Query
    view: typing.Literal["COUNT_RESULT_VIEW_UNSPECIFIED", "TOTAL_COUNT", "ALL"]

@typing.type_check_only
class CountArtifactsResponse(typing.TypedDict, total=False):
    groupsCountResult: GroupsCountResult
    mailCountResult: MailCountResult
    totalCount: str

@typing.type_check_only
class DriveDocumentIds(typing.TypedDict, total=False):
    ids: _list[str]

@typing.type_check_only
class DriveDocumentInfo(typing.TypedDict, total=False):
    documentIds: DriveDocumentIds

@typing.type_check_only
class DriveExportOptions(typing.TypedDict, total=False):
    includeAccessInfo: bool

@typing.type_check_only
class DriveOptions(typing.TypedDict, total=False):
    clientSideEncryptedOption: typing.Literal[
        "CLIENT_SIDE_ENCRYPTED_OPTION_UNSPECIFIED",
        "CLIENT_SIDE_ENCRYPTED_OPTION_ANY",
        "CLIENT_SIDE_ENCRYPTED_OPTION_ENCRYPTED",
        "CLIENT_SIDE_ENCRYPTED_OPTION_UNENCRYPTED",
    ]
    includeSharedDrives: bool
    includeTeamDrives: bool
    sharedDrivesOption: typing.Literal[
        "SHARED_DRIVES_OPTION_UNSPECIFIED",
        "NOT_INCLUDED",
        "INCLUDED_IF_ACCOUNT_IS_NOT_A_MEMBER",
        "INCLUDED",
    ]
    versionDate: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Export(typing.TypedDict, total=False):
    cloudStorageSink: CloudStorageSink
    createTime: str
    exportOptions: ExportOptions
    id: str
    matterId: str
    name: str
    parentExportId: str
    query: Query
    requester: UserInfo
    stats: ExportStats
    status: typing.Literal[
        "EXPORT_STATUS_UNSPECIFIED", "COMPLETED", "FAILED", "IN_PROGRESS"
    ]

@typing.type_check_only
class ExportOptions(typing.TypedDict, total=False):
    calendarOptions: CalendarExportOptions
    driveOptions: DriveExportOptions
    geminiOptions: GeminiExportOptions
    groupsOptions: GroupsExportOptions
    hangoutsChatOptions: HangoutsChatExportOptions
    mailOptions: MailExportOptions
    region: typing.Literal["EXPORT_REGION_UNSPECIFIED", "ANY", "US", "EUROPE"]
    voiceOptions: VoiceExportOptions

@typing.type_check_only
class ExportStats(typing.TypedDict, total=False):
    exportedArtifactCount: str
    sizeInBytes: str
    totalArtifactCount: str

@typing.type_check_only
class GeminiExportOptions(typing.TypedDict, total=False):
    exportFormat: typing.Literal[
        "EXPORT_FORMAT_UNSPECIFIED", "MBOX", "PST", "ICS", "XML", "JSON"
    ]

@typing.type_check_only
class GeminiOptions(typing.TypedDict, total=False): ...

@typing.type_check_only
class GroupsCountResult(typing.TypedDict, total=False):
    accountCountErrors: _list[AccountCountError]
    accountCounts: _list[AccountCount]
    matchingAccountsCount: str
    nonQueryableAccounts: _list[str]
    queriedAccountsCount: str

@typing.type_check_only
class GroupsExportOptions(typing.TypedDict, total=False):
    exportFormat: typing.Literal[
        "EXPORT_FORMAT_UNSPECIFIED", "MBOX", "PST", "ICS", "XML", "JSON"
    ]

@typing.type_check_only
class HangoutsChatExportOptions(typing.TypedDict, total=False):
    exportFormat: typing.Literal[
        "EXPORT_FORMAT_UNSPECIFIED", "MBOX", "PST", "ICS", "XML", "JSON"
    ]

@typing.type_check_only
class HangoutsChatInfo(typing.TypedDict, total=False):
    roomId: _list[str]

@typing.type_check_only
class HangoutsChatOptions(typing.TypedDict, total=False):
    includeRooms: bool

@typing.type_check_only
class HeldAccount(typing.TypedDict, total=False):
    accountId: str
    email: str
    firstName: str
    holdTime: str
    lastName: str

@typing.type_check_only
class HeldCalendarQuery(typing.TypedDict, total=False): ...

@typing.type_check_only
class HeldDriveQuery(typing.TypedDict, total=False):
    includeSharedDriveFiles: bool
    includeTeamDriveFiles: bool

@typing.type_check_only
class HeldGeminiQuery(typing.TypedDict, total=False): ...

@typing.type_check_only
class HeldGroupsQuery(typing.TypedDict, total=False):
    endTime: str
    startTime: str
    terms: str

@typing.type_check_only
class HeldHangoutsChatQuery(typing.TypedDict, total=False):
    includeRooms: bool

@typing.type_check_only
class HeldMailQuery(typing.TypedDict, total=False):
    endTime: str
    startTime: str
    terms: str

@typing.type_check_only
class HeldOrgUnit(typing.TypedDict, total=False):
    holdTime: str
    orgUnitId: str

@typing.type_check_only
class HeldVoiceQuery(typing.TypedDict, total=False):
    coveredData: _list[
        typing.Literal[
            "COVERED_DATA_UNSPECIFIED", "TEXT_MESSAGES", "VOICEMAILS", "CALL_LOGS"
        ]
    ]

@typing.type_check_only
class Hold(typing.TypedDict, total=False):
    accounts: _list[HeldAccount]
    corpus: typing.Literal[
        "CORPUS_TYPE_UNSPECIFIED",
        "DRIVE",
        "MAIL",
        "GROUPS",
        "HANGOUTS_CHAT",
        "VOICE",
        "CALENDAR",
        "GEMINI",
    ]
    holdId: str
    name: str
    orgUnit: HeldOrgUnit
    query: CorpusQuery
    updateTime: str

@typing.type_check_only
class ListExportsResponse(typing.TypedDict, total=False):
    exports: _list[Export]
    nextPageToken: str

@typing.type_check_only
class ListHeldAccountsResponse(typing.TypedDict, total=False):
    accounts: _list[HeldAccount]

@typing.type_check_only
class ListHoldsResponse(typing.TypedDict, total=False):
    holds: _list[Hold]
    nextPageToken: str

@typing.type_check_only
class ListMattersResponse(typing.TypedDict, total=False):
    matters: _list[Matter]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]
    unreachable: _list[str]

@typing.type_check_only
class ListSavedQueriesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    savedQueries: _list[SavedQuery]

@typing.type_check_only
class MailCountResult(typing.TypedDict, total=False):
    accountCountErrors: _list[AccountCountError]
    accountCounts: _list[AccountCount]
    matchingAccountsCount: str
    nonQueryableAccounts: _list[str]
    queriedAccountsCount: str

@typing.type_check_only
class MailExportOptions(typing.TypedDict, total=False):
    exportFormat: typing.Literal[
        "EXPORT_FORMAT_UNSPECIFIED", "MBOX", "PST", "ICS", "XML", "JSON"
    ]
    exportLinkedDriveFiles: bool
    showConfidentialModeContent: bool
    useNewExport: bool

@typing.type_check_only
class MailOptions(typing.TypedDict, total=False):
    clientSideEncryptedOption: typing.Literal[
        "CLIENT_SIDE_ENCRYPTED_OPTION_UNSPECIFIED",
        "CLIENT_SIDE_ENCRYPTED_OPTION_ANY",
        "CLIENT_SIDE_ENCRYPTED_OPTION_ENCRYPTED",
        "CLIENT_SIDE_ENCRYPTED_OPTION_UNENCRYPTED",
    ]
    excludeDrafts: bool

@typing.type_check_only
class Matter(typing.TypedDict, total=False):
    description: str
    matterId: str
    matterPermissions: _list[MatterPermission]
    matterRegion: typing.Literal["MATTER_REGION_UNSPECIFIED", "ANY", "US", "EUROPE"]
    name: str
    state: typing.Literal["STATE_UNSPECIFIED", "OPEN", "CLOSED", "DELETED"]

@typing.type_check_only
class MatterPermission(typing.TypedDict, total=False):
    accountId: str
    role: typing.Literal["ROLE_UNSPECIFIED", "COLLABORATOR", "OWNER"]

@typing.type_check_only
class Operation(typing.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OrgUnitInfo(typing.TypedDict, total=False):
    orgUnitId: str

@typing.type_check_only
class Query(typing.TypedDict, total=False):
    accountInfo: AccountInfo
    calendarOptions: CalendarOptions
    corpus: typing.Literal[
        "CORPUS_TYPE_UNSPECIFIED",
        "DRIVE",
        "MAIL",
        "GROUPS",
        "HANGOUTS_CHAT",
        "VOICE",
        "CALENDAR",
        "GEMINI",
    ]
    dataScope: typing.Literal[
        "DATA_SCOPE_UNSPECIFIED", "ALL_DATA", "HELD_DATA", "UNPROCESSED_DATA"
    ]
    driveDocumentInfo: DriveDocumentInfo
    driveOptions: DriveOptions
    endTime: str
    geminiOptions: GeminiOptions
    hangoutsChatInfo: HangoutsChatInfo
    hangoutsChatOptions: HangoutsChatOptions
    mailOptions: MailOptions
    method: typing.Literal[
        "SEARCH_METHOD_UNSPECIFIED",
        "ACCOUNT",
        "ORG_UNIT",
        "TEAM_DRIVE",
        "ENTIRE_ORG",
        "ROOM",
        "SITES_URL",
        "SHARED_DRIVE",
        "DRIVE_DOCUMENT",
    ]
    orgUnitInfo: OrgUnitInfo
    searchMethod: typing.Literal[
        "SEARCH_METHOD_UNSPECIFIED",
        "ACCOUNT",
        "ORG_UNIT",
        "TEAM_DRIVE",
        "ENTIRE_ORG",
        "ROOM",
        "SITES_URL",
        "SHARED_DRIVE",
        "DRIVE_DOCUMENT",
    ]
    sharedDriveInfo: SharedDriveInfo
    sitesUrlInfo: SitesUrlInfo
    startTime: str
    teamDriveInfo: TeamDriveInfo
    terms: str
    timeZone: str
    voiceOptions: VoiceOptions

@typing.type_check_only
class RemoveHeldAccountsRequest(typing.TypedDict, total=False):
    accountIds: _list[str]

@typing.type_check_only
class RemoveHeldAccountsResponse(typing.TypedDict, total=False):
    statuses: _list[Status]

@typing.type_check_only
class RemoveMatterPermissionsRequest(typing.TypedDict, total=False):
    accountId: str

@typing.type_check_only
class ReopenMatterRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class ReopenMatterResponse(typing.TypedDict, total=False):
    matter: Matter

@typing.type_check_only
class SavedQuery(typing.TypedDict, total=False):
    createTime: str
    displayName: str
    matterId: str
    query: Query
    savedQueryId: str

@typing.type_check_only
class SharedDriveInfo(typing.TypedDict, total=False):
    sharedDriveIds: _list[str]

@typing.type_check_only
class SitesUrlInfo(typing.TypedDict, total=False):
    urls: _list[str]

@typing.type_check_only
class Status(typing.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TeamDriveInfo(typing.TypedDict, total=False):
    teamDriveIds: _list[str]

@typing.type_check_only
class UndeleteMatterRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class UserInfo(typing.TypedDict, total=False):
    displayName: str
    email: str

@typing.type_check_only
class VoiceExportOptions(typing.TypedDict, total=False):
    exportFormat: typing.Literal[
        "EXPORT_FORMAT_UNSPECIFIED", "MBOX", "PST", "ICS", "XML", "JSON"
    ]

@typing.type_check_only
class VoiceOptions(typing.TypedDict, total=False):
    coveredData: _list[
        typing.Literal[
            "COVERED_DATA_UNSPECIFIED", "TEXT_MESSAGES", "VOICEMAILS", "CALL_LOGS"
        ]
    ]

import typing

import typing_extensions

_list = list

@typing.type_check_only
class AccountCount(typing_extensions.TypedDict, total=False):
    account: UserInfo
    count: str

@typing.type_check_only
class AccountCountError(typing_extensions.TypedDict, total=False):
    account: UserInfo
    errorType: typing_extensions.Literal[
        "ERROR_TYPE_UNSPECIFIED",
        "WILDCARD_TOO_BROAD",
        "TOO_MANY_TERMS",
        "LOCATION_UNAVAILABLE",
        "UNKNOWN",
        "DEADLINE_EXCEEDED",
    ]

@typing.type_check_only
class AccountInfo(typing_extensions.TypedDict, total=False):
    emails: _list[str]

@typing.type_check_only
class AddHeldAccountResult(typing_extensions.TypedDict, total=False):
    account: HeldAccount
    status: Status

@typing.type_check_only
class AddHeldAccountsRequest(typing_extensions.TypedDict, total=False):
    accountIds: _list[str]
    emails: _list[str]

@typing.type_check_only
class AddHeldAccountsResponse(typing_extensions.TypedDict, total=False):
    responses: _list[AddHeldAccountResult]

@typing.type_check_only
class AddMatterPermissionsRequest(typing_extensions.TypedDict, total=False):
    ccMe: bool
    matterPermission: MatterPermission
    sendEmails: bool

@typing.type_check_only
class CancelOperationRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CloseMatterRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CloseMatterResponse(typing_extensions.TypedDict, total=False):
    matter: Matter

@typing.type_check_only
class CloudStorageFile(typing_extensions.TypedDict, total=False):
    bucketName: str
    md5Hash: str
    objectName: str
    size: str

@typing.type_check_only
class CloudStorageSink(typing_extensions.TypedDict, total=False):
    files: _list[CloudStorageFile]

@typing.type_check_only
class CorpusQuery(typing_extensions.TypedDict, total=False):
    driveQuery: HeldDriveQuery
    groupsQuery: HeldGroupsQuery
    hangoutsChatQuery: HeldHangoutsChatQuery
    mailQuery: HeldMailQuery
    voiceQuery: HeldVoiceQuery

@typing.type_check_only
class CountArtifactsMetadata(typing_extensions.TypedDict, total=False):
    endTime: str
    matterId: str
    query: Query
    startTime: str

@typing.type_check_only
class CountArtifactsRequest(typing_extensions.TypedDict, total=False):
    query: Query
    view: typing_extensions.Literal[
        "COUNT_RESULT_VIEW_UNSPECIFIED", "TOTAL_COUNT", "ALL"
    ]

@typing.type_check_only
class CountArtifactsResponse(typing_extensions.TypedDict, total=False):
    groupsCountResult: GroupsCountResult
    mailCountResult: MailCountResult
    totalCount: str

@typing.type_check_only
class DriveExportOptions(typing_extensions.TypedDict, total=False):
    includeAccessInfo: bool

@typing.type_check_only
class DriveOptions(typing_extensions.TypedDict, total=False):
    clientSideEncryptedOption: typing_extensions.Literal[
        "CLIENT_SIDE_ENCRYPTED_OPTION_UNSPECIFIED",
        "CLIENT_SIDE_ENCRYPTED_OPTION_ANY",
        "CLIENT_SIDE_ENCRYPTED_OPTION_ENCRYPTED",
        "CLIENT_SIDE_ENCRYPTED_OPTION_UNENCRYPTED",
    ]
    includeSharedDrives: bool
    includeTeamDrives: bool
    versionDate: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Export(typing_extensions.TypedDict, total=False):
    cloudStorageSink: CloudStorageSink
    createTime: str
    exportOptions: ExportOptions
    id: str
    matterId: str
    name: str
    query: Query
    requester: UserInfo
    stats: ExportStats
    status: typing_extensions.Literal[
        "EXPORT_STATUS_UNSPECIFIED", "COMPLETED", "FAILED", "IN_PROGRESS"
    ]

@typing.type_check_only
class ExportOptions(typing_extensions.TypedDict, total=False):
    driveOptions: DriveExportOptions
    groupsOptions: GroupsExportOptions
    hangoutsChatOptions: HangoutsChatExportOptions
    mailOptions: MailExportOptions
    region: typing_extensions.Literal[
        "EXPORT_REGION_UNSPECIFIED", "ANY", "US", "EUROPE"
    ]
    voiceOptions: VoiceExportOptions

@typing.type_check_only
class ExportStats(typing_extensions.TypedDict, total=False):
    exportedArtifactCount: str
    sizeInBytes: str
    totalArtifactCount: str

@typing.type_check_only
class GroupsCountResult(typing_extensions.TypedDict, total=False):
    accountCountErrors: _list[AccountCountError]
    accountCounts: _list[AccountCount]
    matchingAccountsCount: str
    nonQueryableAccounts: _list[str]
    queriedAccountsCount: str

@typing.type_check_only
class GroupsExportOptions(typing_extensions.TypedDict, total=False):
    exportFormat: typing_extensions.Literal["EXPORT_FORMAT_UNSPECIFIED", "MBOX", "PST"]

@typing.type_check_only
class HangoutsChatExportOptions(typing_extensions.TypedDict, total=False):
    exportFormat: typing_extensions.Literal["EXPORT_FORMAT_UNSPECIFIED", "MBOX", "PST"]

@typing.type_check_only
class HangoutsChatInfo(typing_extensions.TypedDict, total=False):
    roomId: _list[str]

@typing.type_check_only
class HangoutsChatOptions(typing_extensions.TypedDict, total=False):
    includeRooms: bool

@typing.type_check_only
class HeldAccount(typing_extensions.TypedDict, total=False):
    accountId: str
    email: str
    firstName: str
    holdTime: str
    lastName: str

@typing.type_check_only
class HeldDriveQuery(typing_extensions.TypedDict, total=False):
    includeSharedDriveFiles: bool
    includeTeamDriveFiles: bool

@typing.type_check_only
class HeldGroupsQuery(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str
    terms: str

@typing.type_check_only
class HeldHangoutsChatQuery(typing_extensions.TypedDict, total=False):
    includeRooms: bool

@typing.type_check_only
class HeldMailQuery(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str
    terms: str

@typing.type_check_only
class HeldOrgUnit(typing_extensions.TypedDict, total=False):
    holdTime: str
    orgUnitId: str

@typing.type_check_only
class HeldVoiceQuery(typing_extensions.TypedDict, total=False):
    coveredData: _list[str]

@typing.type_check_only
class Hold(typing_extensions.TypedDict, total=False):
    accounts: _list[HeldAccount]
    corpus: typing_extensions.Literal[
        "CORPUS_TYPE_UNSPECIFIED", "DRIVE", "MAIL", "GROUPS", "HANGOUTS_CHAT", "VOICE"
    ]
    holdId: str
    name: str
    orgUnit: HeldOrgUnit
    query: CorpusQuery
    updateTime: str

@typing.type_check_only
class ListExportsResponse(typing_extensions.TypedDict, total=False):
    exports: _list[Export]
    nextPageToken: str

@typing.type_check_only
class ListHeldAccountsResponse(typing_extensions.TypedDict, total=False):
    accounts: _list[HeldAccount]

@typing.type_check_only
class ListHoldsResponse(typing_extensions.TypedDict, total=False):
    holds: _list[Hold]
    nextPageToken: str

@typing.type_check_only
class ListMattersResponse(typing_extensions.TypedDict, total=False):
    matters: _list[Matter]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ListSavedQueriesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    savedQueries: _list[SavedQuery]

@typing.type_check_only
class MailCountResult(typing_extensions.TypedDict, total=False):
    accountCountErrors: _list[AccountCountError]
    accountCounts: _list[AccountCount]
    matchingAccountsCount: str
    nonQueryableAccounts: _list[str]
    queriedAccountsCount: str

@typing.type_check_only
class MailExportOptions(typing_extensions.TypedDict, total=False):
    exportFormat: typing_extensions.Literal["EXPORT_FORMAT_UNSPECIFIED", "MBOX", "PST"]
    showConfidentialModeContent: bool
    useNewExport: bool

@typing.type_check_only
class MailOptions(typing_extensions.TypedDict, total=False):
    excludeDrafts: bool

@typing.type_check_only
class Matter(typing_extensions.TypedDict, total=False):
    description: str
    matterId: str
    matterPermissions: _list[MatterPermission]
    name: str
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "OPEN", "CLOSED", "DELETED"]

@typing.type_check_only
class MatterPermission(typing_extensions.TypedDict, total=False):
    accountId: str
    role: typing_extensions.Literal["ROLE_UNSPECIFIED", "COLLABORATOR", "OWNER"]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class OrgUnitInfo(typing_extensions.TypedDict, total=False):
    orgUnitId: str

@typing.type_check_only
class Query(typing_extensions.TypedDict, total=False):
    accountInfo: AccountInfo
    corpus: typing_extensions.Literal[
        "CORPUS_TYPE_UNSPECIFIED", "DRIVE", "MAIL", "GROUPS", "HANGOUTS_CHAT", "VOICE"
    ]
    dataScope: typing_extensions.Literal[
        "DATA_SCOPE_UNSPECIFIED", "ALL_DATA", "HELD_DATA", "UNPROCESSED_DATA"
    ]
    driveOptions: DriveOptions
    endTime: str
    hangoutsChatInfo: HangoutsChatInfo
    hangoutsChatOptions: HangoutsChatOptions
    mailOptions: MailOptions
    method: typing_extensions.Literal[
        "SEARCH_METHOD_UNSPECIFIED",
        "ACCOUNT",
        "ORG_UNIT",
        "TEAM_DRIVE",
        "ENTIRE_ORG",
        "ROOM",
        "SITES_URL",
        "SHARED_DRIVE",
    ]
    orgUnitInfo: OrgUnitInfo
    searchMethod: typing_extensions.Literal[
        "SEARCH_METHOD_UNSPECIFIED",
        "ACCOUNT",
        "ORG_UNIT",
        "TEAM_DRIVE",
        "ENTIRE_ORG",
        "ROOM",
        "SITES_URL",
        "SHARED_DRIVE",
    ]
    sharedDriveInfo: SharedDriveInfo
    sitesUrlInfo: SitesUrlInfo
    startTime: str
    teamDriveInfo: TeamDriveInfo
    terms: str
    timeZone: str
    voiceOptions: VoiceOptions

@typing.type_check_only
class RemoveHeldAccountsRequest(typing_extensions.TypedDict, total=False):
    accountIds: _list[str]

@typing.type_check_only
class RemoveHeldAccountsResponse(typing_extensions.TypedDict, total=False):
    statuses: _list[Status]

@typing.type_check_only
class RemoveMatterPermissionsRequest(typing_extensions.TypedDict, total=False):
    accountId: str

@typing.type_check_only
class ReopenMatterRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class ReopenMatterResponse(typing_extensions.TypedDict, total=False):
    matter: Matter

@typing.type_check_only
class SavedQuery(typing_extensions.TypedDict, total=False):
    createTime: str
    displayName: str
    matterId: str
    query: Query
    savedQueryId: str

@typing.type_check_only
class SharedDriveInfo(typing_extensions.TypedDict, total=False):
    sharedDriveIds: _list[str]

@typing.type_check_only
class SitesUrlInfo(typing_extensions.TypedDict, total=False):
    urls: _list[str]

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TeamDriveInfo(typing_extensions.TypedDict, total=False):
    teamDriveIds: _list[str]

@typing.type_check_only
class UndeleteMatterRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class UserInfo(typing_extensions.TypedDict, total=False):
    displayName: str
    email: str

@typing.type_check_only
class VoiceExportOptions(typing_extensions.TypedDict, total=False):
    exportFormat: typing_extensions.Literal["EXPORT_FORMAT_UNSPECIFIED", "MBOX", "PST"]

@typing.type_check_only
class VoiceOptions(typing_extensions.TypedDict, total=False):
    coveredData: _list[str]

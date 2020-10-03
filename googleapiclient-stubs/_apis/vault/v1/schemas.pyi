import typing

import typing_extensions

class MatterPermission(typing_extensions.TypedDict, total=False):
    accountId: str
    role: typing_extensions.Literal["ROLE_UNSPECIFIED", "COLLABORATOR", "OWNER"]

class ExportOptions(typing_extensions.TypedDict, total=False):
    driveOptions: DriveExportOptions
    groupsOptions: GroupsExportOptions
    mailOptions: MailExportOptions
    region: typing_extensions.Literal[
        "EXPORT_REGION_UNSPECIFIED", "ANY", "US", "EUROPE"
    ]
    hangoutsChatOptions: HangoutsChatExportOptions

class Query(typing_extensions.TypedDict, total=False):
    endTime: str
    searchMethod: typing_extensions.Literal[
        "SEARCH_METHOD_UNSPECIFIED",
        "ACCOUNT",
        "ORG_UNIT",
        "TEAM_DRIVE",
        "ENTIRE_ORG",
        "ROOM",
        "SHARED_DRIVE",
    ]
    mailOptions: MailOptions
    hangoutsChatInfo: HangoutsChatInfo
    terms: str
    accountInfo: AccountInfo
    corpus: typing_extensions.Literal[
        "CORPUS_TYPE_UNSPECIFIED", "DRIVE", "MAIL", "GROUPS", "HANGOUTS_CHAT"
    ]
    timeZone: str
    driveOptions: DriveOptions
    method: typing_extensions.Literal[
        "SEARCH_METHOD_UNSPECIFIED",
        "ACCOUNT",
        "ORG_UNIT",
        "TEAM_DRIVE",
        "ENTIRE_ORG",
        "ROOM",
        "SHARED_DRIVE",
    ]
    startTime: str
    teamDriveInfo: TeamDriveInfo
    hangoutsChatOptions: HangoutsChatOptions
    dataScope: typing_extensions.Literal[
        "DATA_SCOPE_UNSPECIFIED", "ALL_DATA", "HELD_DATA", "UNPROCESSED_DATA"
    ]
    orgUnitInfo: OrgUnitInfo
    sharedDriveInfo: SharedDriveInfo

class HeldAccount(typing_extensions.TypedDict, total=False):
    email: str
    firstName: str
    accountId: str
    holdTime: str
    lastName: str

class DriveExportOptions(typing_extensions.TypedDict, total=False):
    includeAccessInfo: bool

class RemoveMatterPermissionsRequest(typing_extensions.TypedDict, total=False):
    accountId: str

class CloudStorageSink(typing_extensions.TypedDict, total=False):
    files: typing.List[CloudStorageFile]

class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: typing.List[typing.Dict[str, typing.Any]]
    message: str

class UserInfo(typing_extensions.TypedDict, total=False):
    email: str
    displayName: str

class ListMattersResponse(typing_extensions.TypedDict, total=False):
    matters: typing.List[Matter]
    nextPageToken: str

class ListHeldAccountsResponse(typing_extensions.TypedDict, total=False):
    accounts: typing.List[HeldAccount]

class HangoutsChatExportOptions(typing_extensions.TypedDict, total=False):
    exportFormat: typing_extensions.Literal["EXPORT_FORMAT_UNSPECIFIED", "MBOX", "PST"]

class ListExportsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    exports: typing.List[Export]

class OrgUnitInfo(typing_extensions.TypedDict, total=False):
    orgUnitId: str

class CloseMatterRequest(typing_extensions.TypedDict, total=False): ...

class CloudStorageFile(typing_extensions.TypedDict, total=False):
    bucketName: str
    size: str
    md5Hash: str
    objectName: str

class HeldOrgUnit(typing_extensions.TypedDict, total=False):
    holdTime: str
    orgUnitId: str

class AddHeldAccountsRequest(typing_extensions.TypedDict, total=False):
    accountIds: typing.List[str]
    emails: typing.List[str]

class HeldMailQuery(typing_extensions.TypedDict, total=False):
    terms: str
    startTime: str
    endTime: str

class HeldHangoutsChatQuery(typing_extensions.TypedDict, total=False):
    includeRooms: bool

class Matter(typing_extensions.TypedDict, total=False):
    state: typing_extensions.Literal["STATE_UNSPECIFIED", "OPEN", "CLOSED", "DELETED"]
    name: str
    matterId: str
    description: str
    matterPermissions: typing.List[MatterPermission]

class HeldGroupsQuery(typing_extensions.TypedDict, total=False):
    endTime: str
    terms: str
    startTime: str

class ReopenMatterRequest(typing_extensions.TypedDict, total=False): ...
class UndeleteMatterRequest(typing_extensions.TypedDict, total=False): ...
class Empty(typing_extensions.TypedDict, total=False): ...

class ListSavedQueriesResponse(typing_extensions.TypedDict, total=False):
    savedQueries: typing.List[SavedQuery]
    nextPageToken: str

class CloseMatterResponse(typing_extensions.TypedDict, total=False):
    matter: Matter

class Export(typing_extensions.TypedDict, total=False):
    name: str
    exportOptions: ExportOptions
    status: typing_extensions.Literal[
        "EXPORT_STATUS_UNSPECIFIED", "COMPLETED", "FAILED", "IN_PROGRESS"
    ]
    requester: UserInfo
    createTime: str
    cloudStorageSink: CloudStorageSink
    id: str
    stats: ExportStats
    matterId: str
    query: Query

class RemoveHeldAccountsRequest(typing_extensions.TypedDict, total=False):
    accountIds: typing.List[str]

class Hold(typing_extensions.TypedDict, total=False):
    updateTime: str
    corpus: typing_extensions.Literal[
        "CORPUS_TYPE_UNSPECIFIED", "DRIVE", "MAIL", "GROUPS", "HANGOUTS_CHAT"
    ]
    accounts: typing.List[HeldAccount]
    orgUnit: HeldOrgUnit
    holdId: str
    query: CorpusQuery
    name: str

class AddHeldAccountResult(typing_extensions.TypedDict, total=False):
    status: Status
    account: HeldAccount

class ExportStats(typing_extensions.TypedDict, total=False):
    sizeInBytes: str
    exportedArtifactCount: str
    totalArtifactCount: str

class AccountInfo(typing_extensions.TypedDict, total=False):
    emails: typing.List[str]

class MailExportOptions(typing_extensions.TypedDict, total=False):
    showConfidentialModeContent: bool
    exportFormat: typing_extensions.Literal["EXPORT_FORMAT_UNSPECIFIED", "MBOX", "PST"]

class MailOptions(typing_extensions.TypedDict, total=False):
    excludeDrafts: bool

class ListHoldsResponse(typing_extensions.TypedDict, total=False):
    holds: typing.List[Hold]
    nextPageToken: str

class SharedDriveInfo(typing_extensions.TypedDict, total=False):
    sharedDriveIds: typing.List[str]

class HangoutsChatOptions(typing_extensions.TypedDict, total=False):
    includeRooms: bool

class HangoutsChatInfo(typing_extensions.TypedDict, total=False):
    roomId: typing.List[str]

class RemoveHeldAccountsResponse(typing_extensions.TypedDict, total=False):
    statuses: typing.List[Status]

class CorpusQuery(typing_extensions.TypedDict, total=False):
    groupsQuery: HeldGroupsQuery
    mailQuery: HeldMailQuery
    hangoutsChatQuery: HeldHangoutsChatQuery
    driveQuery: HeldDriveQuery

class DriveOptions(typing_extensions.TypedDict, total=False):
    includeSharedDrives: bool
    includeTeamDrives: bool
    versionDate: str

class SavedQuery(typing_extensions.TypedDict, total=False):
    matterId: str
    displayName: str
    savedQueryId: str
    createTime: str
    query: Query

class AddMatterPermissionsRequest(typing_extensions.TypedDict, total=False):
    ccMe: bool
    sendEmails: bool
    matterPermission: MatterPermission

class GroupsExportOptions(typing_extensions.TypedDict, total=False):
    exportFormat: typing_extensions.Literal["EXPORT_FORMAT_UNSPECIFIED", "MBOX", "PST"]

class HeldDriveQuery(typing_extensions.TypedDict, total=False):
    includeSharedDriveFiles: bool
    includeTeamDriveFiles: bool

class TeamDriveInfo(typing_extensions.TypedDict, total=False):
    teamDriveIds: typing.List[str]

class ReopenMatterResponse(typing_extensions.TypedDict, total=False):
    matter: Matter

class AddHeldAccountsResponse(typing_extensions.TypedDict, total=False):
    responses: typing.List[AddHeldAccountResult]

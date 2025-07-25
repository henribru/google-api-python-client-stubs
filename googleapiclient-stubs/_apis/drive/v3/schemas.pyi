import typing

import typing_extensions

_list = list

@typing.type_check_only
class About(typing_extensions.TypedDict, total=False):
    appInstalled: bool
    canCreateDrives: bool
    canCreateTeamDrives: bool
    driveThemes: _list[dict[str, typing.Any]]
    exportFormats: dict[str, typing.Any]
    folderColorPalette: _list[str]
    importFormats: dict[str, typing.Any]
    kind: str
    maxImportSizes: dict[str, typing.Any]
    maxUploadSize: str
    storageQuota: dict[str, typing.Any]
    teamDriveThemes: _list[dict[str, typing.Any]]
    user: User

@typing.type_check_only
class AccessProposal(typing_extensions.TypedDict, total=False):
    createTime: str
    fileId: str
    proposalId: str
    recipientEmailAddress: str
    requestMessage: str
    requesterEmailAddress: str
    rolesAndViews: _list[AccessProposalRoleAndView]

@typing.type_check_only
class AccessProposalRoleAndView(typing_extensions.TypedDict, total=False):
    role: str
    view: str

@typing.type_check_only
class App(typing_extensions.TypedDict, total=False):
    authorized: bool
    createInFolderTemplate: str
    createUrl: str
    hasDriveWideScope: bool
    icons: _list[AppIcons]
    id: str
    installed: bool
    kind: str
    longDescription: str
    name: str
    objectType: str
    openUrlTemplate: str
    primaryFileExtensions: _list[str]
    primaryMimeTypes: _list[str]
    productId: str
    productUrl: str
    secondaryFileExtensions: _list[str]
    secondaryMimeTypes: _list[str]
    shortDescription: str
    supportsCreate: bool
    supportsImport: bool
    supportsMultiOpen: bool
    supportsOfflineCreate: bool
    useByDefault: bool

@typing.type_check_only
class AppIcons(typing_extensions.TypedDict, total=False):
    category: str
    iconUrl: str
    size: int

@typing.type_check_only
class AppList(typing_extensions.TypedDict, total=False):
    defaultAppIds: _list[str]
    items: _list[App]
    kind: str
    selfLink: str

@typing.type_check_only
class Change(typing_extensions.TypedDict, total=False):
    changeType: str
    drive: Drive
    driveId: str
    file: File
    fileId: str
    kind: str
    removed: bool
    teamDrive: TeamDrive
    teamDriveId: str
    time: str
    type: str

@typing.type_check_only
class ChangeList(typing_extensions.TypedDict, total=False):
    changes: _list[Change]
    kind: str
    newStartPageToken: str
    nextPageToken: str

@typing.type_check_only
class Channel(typing_extensions.TypedDict, total=False):
    address: str
    expiration: str
    id: str
    kind: str
    params: dict[str, typing.Any]
    payload: bool
    resourceId: str
    resourceUri: str
    token: str
    type: str

@typing.type_check_only
class Comment(typing_extensions.TypedDict, total=False):
    anchor: str
    author: User
    content: str
    createdTime: str
    deleted: bool
    htmlContent: str
    id: str
    kind: str
    modifiedTime: str
    quotedFileContent: dict[str, typing.Any]
    replies: _list[Reply]
    resolved: bool

@typing.type_check_only
class CommentList(typing_extensions.TypedDict, total=False):
    comments: _list[Comment]
    kind: str
    nextPageToken: str

@typing.type_check_only
class ContentRestriction(typing_extensions.TypedDict, total=False):
    ownerRestricted: bool
    readOnly: bool
    reason: str
    restrictingUser: User
    restrictionTime: str
    systemRestricted: bool
    type: str

@typing.type_check_only
class DownloadRestriction(typing_extensions.TypedDict, total=False):
    restrictedForReaders: bool
    restrictedForWriters: bool

@typing.type_check_only
class DownloadRestrictionsMetadata(typing_extensions.TypedDict, total=False):
    effectiveDownloadRestrictionWithContext: DownloadRestriction
    itemDownloadRestriction: DownloadRestriction

@typing.type_check_only
class Drive(typing_extensions.TypedDict, total=False):
    backgroundImageFile: dict[str, typing.Any]
    backgroundImageLink: str
    capabilities: dict[str, typing.Any]
    colorRgb: str
    createdTime: str
    hidden: bool
    id: str
    kind: str
    name: str
    orgUnitId: str
    restrictions: dict[str, typing.Any]
    themeId: str

@typing.type_check_only
class DriveList(typing_extensions.TypedDict, total=False):
    drives: _list[Drive]
    kind: str
    nextPageToken: str

@typing.type_check_only
class File(typing_extensions.TypedDict, total=False):
    appProperties: dict[str, typing.Any]
    capabilities: dict[str, typing.Any]
    contentHints: dict[str, typing.Any]
    contentRestrictions: _list[ContentRestriction]
    copyRequiresWriterPermission: bool
    createdTime: str
    description: str
    downloadRestrictions: DownloadRestrictionsMetadata
    driveId: str
    explicitlyTrashed: bool
    exportLinks: dict[str, typing.Any]
    fileExtension: str
    folderColorRgb: str
    fullFileExtension: str
    hasAugmentedPermissions: bool
    hasThumbnail: bool
    headRevisionId: str
    iconLink: str
    id: str
    imageMediaMetadata: dict[str, typing.Any]
    inheritedPermissionsDisabled: bool
    isAppAuthorized: bool
    kind: str
    labelInfo: dict[str, typing.Any]
    lastModifyingUser: User
    linkShareMetadata: dict[str, typing.Any]
    md5Checksum: str
    mimeType: str
    modifiedByMe: bool
    modifiedByMeTime: str
    modifiedTime: str
    name: str
    originalFilename: str
    ownedByMe: bool
    owners: _list[User]
    parents: _list[str]
    permissionIds: _list[str]
    permissions: _list[Permission]
    properties: dict[str, typing.Any]
    quotaBytesUsed: str
    resourceKey: str
    sha1Checksum: str
    sha256Checksum: str
    shared: bool
    sharedWithMeTime: str
    sharingUser: User
    shortcutDetails: dict[str, typing.Any]
    size: str
    spaces: _list[str]
    starred: bool
    teamDriveId: str
    thumbnailLink: str
    thumbnailVersion: str
    trashed: bool
    trashedTime: str
    trashingUser: User
    version: str
    videoMediaMetadata: dict[str, typing.Any]
    viewedByMe: bool
    viewedByMeTime: str
    viewersCanCopyContent: bool
    webContentLink: str
    webViewLink: str
    writersCanShare: bool

@typing.type_check_only
class FileList(typing_extensions.TypedDict, total=False):
    files: _list[File]
    incompleteSearch: bool
    kind: str
    nextPageToken: str

@typing.type_check_only
class GeneratedIds(typing_extensions.TypedDict, total=False):
    ids: _list[str]
    kind: str
    space: str

@typing.type_check_only
class Label(typing_extensions.TypedDict, total=False):
    fields: dict[str, typing.Any]
    id: str
    kind: str
    revisionId: str

@typing.type_check_only
class LabelField(typing_extensions.TypedDict, total=False):
    dateString: _list[str]
    id: str
    integer: _list[str]
    kind: str
    selection: _list[str]
    text: _list[str]
    user: _list[User]
    valueType: str

@typing.type_check_only
class LabelFieldModification(typing_extensions.TypedDict, total=False):
    fieldId: str
    kind: str
    setDateValues: _list[str]
    setIntegerValues: _list[str]
    setSelectionValues: _list[str]
    setTextValues: _list[str]
    setUserValues: _list[str]
    unsetValues: bool

@typing.type_check_only
class LabelList(typing_extensions.TypedDict, total=False):
    kind: str
    labels: _list[Label]
    nextPageToken: str

@typing.type_check_only
class LabelModification(typing_extensions.TypedDict, total=False):
    fieldModifications: _list[LabelFieldModification]
    kind: str
    labelId: str
    removeLabel: bool

@typing.type_check_only
class ListAccessProposalsResponse(typing_extensions.TypedDict, total=False):
    accessProposals: _list[AccessProposal]
    nextPageToken: str

@typing.type_check_only
class ListOperationsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    operations: _list[Operation]

@typing.type_check_only
class ModifyLabelsRequest(typing_extensions.TypedDict, total=False):
    kind: str
    labelModifications: _list[LabelModification]

@typing.type_check_only
class ModifyLabelsResponse(typing_extensions.TypedDict, total=False):
    kind: str
    modifiedLabels: _list[Label]

@typing.type_check_only
class Operation(typing_extensions.TypedDict, total=False):
    done: bool
    error: Status
    metadata: dict[str, typing.Any]
    name: str
    response: dict[str, typing.Any]

@typing.type_check_only
class Permission(typing_extensions.TypedDict, total=False):
    allowFileDiscovery: bool
    deleted: bool
    displayName: str
    domain: str
    emailAddress: str
    expirationTime: str
    id: str
    inheritedPermissionsDisabled: bool
    kind: str
    pendingOwner: bool
    permissionDetails: _list[dict[str, typing.Any]]
    photoLink: str
    role: str
    teamDrivePermissionDetails: _list[dict[str, typing.Any]]
    type: str
    view: str

@typing.type_check_only
class PermissionList(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    permissions: _list[Permission]

@typing.type_check_only
class Reply(typing_extensions.TypedDict, total=False):
    action: str
    author: User
    content: str
    createdTime: str
    deleted: bool
    htmlContent: str
    id: str
    kind: str
    modifiedTime: str

@typing.type_check_only
class ReplyList(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    replies: _list[Reply]

@typing.type_check_only
class ResolveAccessProposalRequest(typing_extensions.TypedDict, total=False):
    action: typing_extensions.Literal["ACTION_UNSPECIFIED", "ACCEPT", "DENY"]
    role: _list[str]
    sendNotification: bool
    view: str

@typing.type_check_only
class Revision(typing_extensions.TypedDict, total=False):
    exportLinks: dict[str, typing.Any]
    id: str
    keepForever: bool
    kind: str
    lastModifyingUser: User
    md5Checksum: str
    mimeType: str
    modifiedTime: str
    originalFilename: str
    publishAuto: bool
    published: bool
    publishedLink: str
    publishedOutsideDomain: bool
    size: str

@typing.type_check_only
class RevisionList(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    revisions: _list[Revision]

@typing.type_check_only
class StartPageToken(typing_extensions.TypedDict, total=False):
    kind: str
    startPageToken: str

@typing.type_check_only
class Status(typing_extensions.TypedDict, total=False):
    code: int
    details: _list[dict[str, typing.Any]]
    message: str

@typing.type_check_only
class TeamDrive(typing_extensions.TypedDict, total=False):
    backgroundImageFile: dict[str, typing.Any]
    backgroundImageLink: str
    capabilities: dict[str, typing.Any]
    colorRgb: str
    createdTime: str
    id: str
    kind: str
    name: str
    orgUnitId: str
    restrictions: dict[str, typing.Any]
    themeId: str

@typing.type_check_only
class TeamDriveList(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    teamDrives: _list[TeamDrive]

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    displayName: str
    emailAddress: str
    kind: str
    me: bool
    permissionId: str
    photoLink: str

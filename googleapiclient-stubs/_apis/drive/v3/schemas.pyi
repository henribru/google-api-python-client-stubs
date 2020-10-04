import typing

import typing_extensions
@typing.type_check_only
class About(typing_extensions.TypedDict, total=False):
    appInstalled: bool
    canCreateDrives: bool
    canCreateTeamDrives: bool
    driveThemes: typing.List[typing.Dict[str, typing.Any]]
    exportFormats: typing.Dict[str, typing.Any]
    folderColorPalette: typing.List[str]
    importFormats: typing.Dict[str, typing.Any]
    kind: str
    maxImportSizes: typing.Dict[str, typing.Any]
    maxUploadSize: str
    storageQuota: typing.Dict[str, typing.Any]
    teamDriveThemes: typing.List[typing.Dict[str, typing.Any]]
    user: User

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
    changes: typing.List[Change]
    kind: str
    newStartPageToken: str
    nextPageToken: str

@typing.type_check_only
class Channel(typing_extensions.TypedDict, total=False):
    address: str
    expiration: str
    id: str
    kind: str
    params: typing.Dict[str, typing.Any]
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
    quotedFileContent: typing.Dict[str, typing.Any]
    replies: typing.List[Reply]
    resolved: bool

@typing.type_check_only
class CommentList(typing_extensions.TypedDict, total=False):
    comments: typing.List[Comment]
    kind: str
    nextPageToken: str

@typing.type_check_only
class ContentRestriction(typing_extensions.TypedDict, total=False):
    readOnly: bool
    reason: str
    restrictingUser: User
    restrictionTime: str
    type: str

@typing.type_check_only
class Drive(typing_extensions.TypedDict, total=False):
    backgroundImageFile: typing.Dict[str, typing.Any]
    backgroundImageLink: str
    capabilities: typing.Dict[str, typing.Any]
    colorRgb: str
    createdTime: str
    hidden: bool
    id: str
    kind: str
    name: str
    restrictions: typing.Dict[str, typing.Any]
    themeId: str

@typing.type_check_only
class DriveList(typing_extensions.TypedDict, total=False):
    drives: typing.List[Drive]
    kind: str
    nextPageToken: str

@typing.type_check_only
class File(typing_extensions.TypedDict, total=False):
    appProperties: typing.Dict[str, typing.Any]
    capabilities: typing.Dict[str, typing.Any]
    contentHints: typing.Dict[str, typing.Any]
    contentRestrictions: typing.List[ContentRestriction]
    copyRequiresWriterPermission: bool
    createdTime: str
    description: str
    driveId: str
    explicitlyTrashed: bool
    exportLinks: typing.Dict[str, typing.Any]
    fileExtension: str
    folderColorRgb: str
    fullFileExtension: str
    hasAugmentedPermissions: bool
    hasThumbnail: bool
    headRevisionId: str
    iconLink: str
    id: str
    imageMediaMetadata: typing.Dict[str, typing.Any]
    isAppAuthorized: bool
    kind: str
    lastModifyingUser: User
    md5Checksum: str
    mimeType: str
    modifiedByMe: bool
    modifiedByMeTime: str
    modifiedTime: str
    name: str
    originalFilename: str
    ownedByMe: bool
    owners: typing.List[User]
    parents: typing.List[str]
    permissionIds: typing.List[str]
    permissions: typing.List[Permission]
    properties: typing.Dict[str, typing.Any]
    quotaBytesUsed: str
    shared: bool
    sharedWithMeTime: str
    sharingUser: User
    shortcutDetails: typing.Dict[str, typing.Any]
    size: str
    spaces: typing.List[str]
    starred: bool
    teamDriveId: str
    thumbnailLink: str
    thumbnailVersion: str
    trashed: bool
    trashedTime: str
    trashingUser: User
    version: str
    videoMediaMetadata: typing.Dict[str, typing.Any]
    viewedByMe: bool
    viewedByMeTime: str
    viewersCanCopyContent: bool
    webContentLink: str
    webViewLink: str
    writersCanShare: bool

@typing.type_check_only
class FileList(typing_extensions.TypedDict, total=False):
    files: typing.List[File]
    incompleteSearch: bool
    kind: str
    nextPageToken: str

@typing.type_check_only
class GeneratedIds(typing_extensions.TypedDict, total=False):
    ids: typing.List[str]
    kind: str
    space: str

@typing.type_check_only
class Permission(typing_extensions.TypedDict, total=False):
    allowFileDiscovery: bool
    deleted: bool
    displayName: str
    domain: str
    emailAddress: str
    expirationTime: str
    id: str
    kind: str
    permissionDetails: typing.List[typing.Dict[str, typing.Any]]
    photoLink: str
    role: str
    teamDrivePermissionDetails: typing.List[typing.Dict[str, typing.Any]]
    type: str
    view: str

@typing.type_check_only
class PermissionList(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    permissions: typing.List[Permission]

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
    replies: typing.List[Reply]

@typing.type_check_only
class Revision(typing_extensions.TypedDict, total=False):
    exportLinks: typing.Dict[str, typing.Any]
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
    revisions: typing.List[Revision]

@typing.type_check_only
class StartPageToken(typing_extensions.TypedDict, total=False):
    kind: str
    startPageToken: str

@typing.type_check_only
class TeamDrive(typing_extensions.TypedDict, total=False):
    backgroundImageFile: typing.Dict[str, typing.Any]
    backgroundImageLink: str
    capabilities: typing.Dict[str, typing.Any]
    colorRgb: str
    createdTime: str
    id: str
    kind: str
    name: str
    restrictions: typing.Dict[str, typing.Any]
    themeId: str

@typing.type_check_only
class TeamDriveList(typing_extensions.TypedDict, total=False):
    kind: str
    nextPageToken: str
    teamDrives: typing.List[TeamDrive]

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    displayName: str
    emailAddress: str
    kind: str
    me: bool
    permissionId: str
    photoLink: str

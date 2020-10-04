import typing

import typing_extensions
@typing.type_check_only
class About(typing_extensions.TypedDict, total=False):
    additionalRoleInfo: typing.List[typing.Dict[str, typing.Any]]
    canCreateDrives: bool
    canCreateTeamDrives: bool
    domainSharingPolicy: str
    driveThemes: typing.List[typing.Dict[str, typing.Any]]
    etag: str
    exportFormats: typing.List[typing.Dict[str, typing.Any]]
    features: typing.List[typing.Dict[str, typing.Any]]
    folderColorPalette: typing.List[str]
    importFormats: typing.List[typing.Dict[str, typing.Any]]
    isCurrentAppInstalled: bool
    kind: str
    languageCode: str
    largestChangeId: str
    maxUploadSizes: typing.List[typing.Dict[str, typing.Any]]
    name: str
    permissionId: str
    quotaBytesByService: typing.List[typing.Dict[str, typing.Any]]
    quotaBytesTotal: str
    quotaBytesUsed: str
    quotaBytesUsedAggregate: str
    quotaBytesUsedInTrash: str
    quotaType: str
    remainingChangeIds: str
    rootFolderId: str
    selfLink: str
    teamDriveThemes: typing.List[typing.Dict[str, typing.Any]]
    user: User

@typing.type_check_only
class App(typing_extensions.TypedDict, total=False):
    authorized: bool
    createInFolderTemplate: str
    createUrl: str
    hasDriveWideScope: bool
    icons: typing.List[typing.Dict[str, typing.Any]]
    id: str
    installed: bool
    kind: str
    longDescription: str
    name: str
    objectType: str
    openUrlTemplate: str
    primaryFileExtensions: typing.List[str]
    primaryMimeTypes: typing.List[str]
    productId: str
    productUrl: str
    secondaryFileExtensions: typing.List[str]
    secondaryMimeTypes: typing.List[str]
    shortDescription: str
    supportsCreate: bool
    supportsImport: bool
    supportsMultiOpen: bool
    supportsOfflineCreate: bool
    useByDefault: bool

@typing.type_check_only
class AppList(typing_extensions.TypedDict, total=False):
    defaultAppIds: typing.List[str]
    etag: str
    items: typing.List[App]
    kind: str
    selfLink: str

@typing.type_check_only
class Change(typing_extensions.TypedDict, total=False):
    changeType: str
    deleted: bool
    drive: Drive
    driveId: str
    file: File
    fileId: str
    id: str
    kind: str
    modificationDate: str
    selfLink: str
    teamDrive: TeamDrive
    teamDriveId: str
    type: str

@typing.type_check_only
class ChangeList(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[Change]
    kind: str
    largestChangeId: str
    newStartPageToken: str
    nextLink: str
    nextPageToken: str
    selfLink: str

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
class ChildList(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[ChildReference]
    kind: str
    nextLink: str
    nextPageToken: str
    selfLink: str

@typing.type_check_only
class ChildReference(typing_extensions.TypedDict, total=False):
    childLink: str
    id: str
    kind: str
    selfLink: str

@typing.type_check_only
class Comment(typing_extensions.TypedDict, total=False):
    anchor: str
    author: User
    commentId: str
    content: str
    context: typing.Dict[str, typing.Any]
    createdDate: str
    deleted: bool
    fileId: str
    fileTitle: str
    htmlContent: str
    kind: str
    modifiedDate: str
    replies: typing.List[CommentReply]
    selfLink: str
    status: str

@typing.type_check_only
class CommentList(typing_extensions.TypedDict, total=False):
    items: typing.List[Comment]
    kind: str
    nextLink: str
    nextPageToken: str
    selfLink: str

@typing.type_check_only
class CommentReply(typing_extensions.TypedDict, total=False):
    author: User
    content: str
    createdDate: str
    deleted: bool
    htmlContent: str
    kind: str
    modifiedDate: str
    replyId: str
    verb: str

@typing.type_check_only
class CommentReplyList(typing_extensions.TypedDict, total=False):
    items: typing.List[CommentReply]
    kind: str
    nextLink: str
    nextPageToken: str
    selfLink: str

@typing.type_check_only
class ContentRestriction(typing_extensions.TypedDict, total=False):
    readOnly: bool
    reason: str
    restrictingUser: User
    restrictionDate: str
    type: str

@typing.type_check_only
class Drive(typing_extensions.TypedDict, total=False):
    backgroundImageFile: typing.Dict[str, typing.Any]
    backgroundImageLink: str
    capabilities: typing.Dict[str, typing.Any]
    colorRgb: str
    createdDate: str
    hidden: bool
    id: str
    kind: str
    name: str
    restrictions: typing.Dict[str, typing.Any]
    themeId: str

@typing.type_check_only
class DriveList(typing_extensions.TypedDict, total=False):
    items: typing.List[Drive]
    kind: str
    nextPageToken: str

@typing.type_check_only
class File(typing_extensions.TypedDict, total=False):
    alternateLink: str
    appDataContents: bool
    canComment: bool
    canReadRevisions: bool
    capabilities: typing.Dict[str, typing.Any]
    contentRestrictions: typing.List[ContentRestriction]
    copyRequiresWriterPermission: bool
    copyable: bool
    createdDate: str
    defaultOpenWithLink: str
    description: str
    downloadUrl: str
    driveId: str
    editable: bool
    embedLink: str
    etag: str
    explicitlyTrashed: bool
    exportLinks: typing.Dict[str, typing.Any]
    fileExtension: str
    fileSize: str
    folderColorRgb: str
    fullFileExtension: str
    hasAugmentedPermissions: bool
    hasThumbnail: bool
    headRevisionId: str
    iconLink: str
    id: str
    imageMediaMetadata: typing.Dict[str, typing.Any]
    indexableText: typing.Dict[str, typing.Any]
    isAppAuthorized: bool
    kind: str
    labels: typing.Dict[str, typing.Any]
    lastModifyingUser: User
    lastModifyingUserName: str
    lastViewedByMeDate: str
    markedViewedByMeDate: str
    md5Checksum: str
    mimeType: str
    modifiedByMeDate: str
    modifiedDate: str
    openWithLinks: typing.Dict[str, typing.Any]
    originalFilename: str
    ownedByMe: bool
    ownerNames: typing.List[str]
    owners: typing.List[User]
    parents: typing.List[ParentReference]
    permissionIds: typing.List[str]
    permissions: typing.List[Permission]
    properties: typing.List[Property]
    quotaBytesUsed: str
    selfLink: str
    shareable: bool
    shared: bool
    sharedWithMeDate: str
    sharingUser: User
    shortcutDetails: typing.Dict[str, typing.Any]
    spaces: typing.List[str]
    teamDriveId: str
    thumbnail: typing.Dict[str, typing.Any]
    thumbnailLink: str
    thumbnailVersion: str
    title: str
    trashedDate: str
    trashingUser: User
    userPermission: Permission
    version: str
    videoMediaMetadata: typing.Dict[str, typing.Any]
    webContentLink: str
    webViewLink: str
    writersCanShare: bool

@typing.type_check_only
class FileList(typing_extensions.TypedDict, total=False):
    etag: str
    incompleteSearch: bool
    items: typing.List[File]
    kind: str
    nextLink: str
    nextPageToken: str
    selfLink: str

@typing.type_check_only
class GeneratedIds(typing_extensions.TypedDict, total=False):
    ids: typing.List[str]
    kind: str
    space: str

@typing.type_check_only
class ParentList(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[ParentReference]
    kind: str
    selfLink: str

@typing.type_check_only
class ParentReference(typing_extensions.TypedDict, total=False):
    id: str
    isRoot: bool
    kind: str
    parentLink: str
    selfLink: str

@typing.type_check_only
class Permission(typing_extensions.TypedDict, total=False):
    additionalRoles: typing.List[str]
    authKey: str
    deleted: bool
    domain: str
    emailAddress: str
    etag: str
    expirationDate: str
    id: str
    kind: str
    name: str
    permissionDetails: typing.List[typing.Dict[str, typing.Any]]
    photoLink: str
    role: str
    selfLink: str
    teamDrivePermissionDetails: typing.List[typing.Dict[str, typing.Any]]
    type: str
    value: str
    view: str
    withLink: bool

@typing.type_check_only
class PermissionId(typing_extensions.TypedDict, total=False):
    id: str
    kind: str

@typing.type_check_only
class PermissionList(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[Permission]
    kind: str
    nextPageToken: str
    selfLink: str

@typing.type_check_only
class Property(typing_extensions.TypedDict, total=False):
    etag: str
    key: str
    kind: str
    selfLink: str
    value: str
    visibility: str

@typing.type_check_only
class PropertyList(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[Property]
    kind: str
    selfLink: str

@typing.type_check_only
class Revision(typing_extensions.TypedDict, total=False):
    downloadUrl: str
    etag: str
    exportLinks: typing.Dict[str, typing.Any]
    fileSize: str
    id: str
    kind: str
    lastModifyingUser: User
    lastModifyingUserName: str
    md5Checksum: str
    mimeType: str
    modifiedDate: str
    originalFilename: str
    pinned: bool
    publishAuto: bool
    published: bool
    publishedLink: str
    publishedOutsideDomain: bool
    selfLink: str

@typing.type_check_only
class RevisionList(typing_extensions.TypedDict, total=False):
    etag: str
    items: typing.List[Revision]
    kind: str
    nextPageToken: str
    selfLink: str

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
    createdDate: str
    id: str
    kind: str
    name: str
    restrictions: typing.Dict[str, typing.Any]
    themeId: str

@typing.type_check_only
class TeamDriveList(typing_extensions.TypedDict, total=False):
    items: typing.List[TeamDrive]
    kind: str
    nextPageToken: str

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    displayName: str
    emailAddress: str
    isAuthenticatedUser: bool
    kind: str
    permissionId: str
    picture: typing.Dict[str, typing.Any]

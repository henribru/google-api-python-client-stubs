import typing

import typing_extensions

_list = list

@typing.type_check_only
class About(typing_extensions.TypedDict, total=False):
    additionalRoleInfo: _list[dict[str, typing.Any]]
    canCreateDrives: bool
    canCreateTeamDrives: bool
    domainSharingPolicy: str
    driveThemes: _list[dict[str, typing.Any]]
    etag: str
    exportFormats: _list[dict[str, typing.Any]]
    features: _list[dict[str, typing.Any]]
    folderColorPalette: _list[str]
    importFormats: _list[dict[str, typing.Any]]
    isCurrentAppInstalled: bool
    kind: str
    languageCode: str
    largestChangeId: str
    maxUploadSizes: _list[dict[str, typing.Any]]
    name: str
    permissionId: str
    quotaBytesByService: _list[dict[str, typing.Any]]
    quotaBytesTotal: str
    quotaBytesUsed: str
    quotaBytesUsedAggregate: str
    quotaBytesUsedInTrash: str
    quotaType: str
    remainingChangeIds: str
    rootFolderId: str
    selfLink: str
    teamDriveThemes: _list[dict[str, typing.Any]]
    user: User

@typing.type_check_only
class App(typing_extensions.TypedDict, total=False):
    authorized: bool
    createInFolderTemplate: str
    createUrl: str
    hasDriveWideScope: bool
    icons: _list[dict[str, typing.Any]]
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
class AppList(typing_extensions.TypedDict, total=False):
    defaultAppIds: _list[str]
    etag: str
    items: _list[App]
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
    items: _list[Change]
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
    params: dict[str, typing.Any]
    payload: bool
    resourceId: str
    resourceUri: str
    token: str
    type: str

@typing.type_check_only
class ChildList(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[ChildReference]
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
    context: dict[str, typing.Any]
    createdDate: str
    deleted: bool
    fileId: str
    fileTitle: str
    htmlContent: str
    kind: str
    modifiedDate: str
    replies: _list[CommentReply]
    selfLink: str
    status: str

@typing.type_check_only
class CommentList(typing_extensions.TypedDict, total=False):
    items: _list[Comment]
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
    items: _list[CommentReply]
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
    backgroundImageFile: dict[str, typing.Any]
    backgroundImageLink: str
    capabilities: dict[str, typing.Any]
    colorRgb: str
    createdDate: str
    hidden: bool
    id: str
    kind: str
    name: str
    orgUnitId: str
    restrictions: dict[str, typing.Any]
    themeId: str

@typing.type_check_only
class DriveList(typing_extensions.TypedDict, total=False):
    items: _list[Drive]
    kind: str
    nextPageToken: str

@typing.type_check_only
class File(typing_extensions.TypedDict, total=False):
    alternateLink: str
    appDataContents: bool
    canComment: bool
    canReadRevisions: bool
    capabilities: dict[str, typing.Any]
    contentRestrictions: _list[ContentRestriction]
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
    exportLinks: dict[str, typing.Any]
    fileExtension: str
    fileSize: str
    folderColorRgb: str
    fullFileExtension: str
    hasAugmentedPermissions: bool
    hasThumbnail: bool
    headRevisionId: str
    iconLink: str
    id: str
    imageMediaMetadata: dict[str, typing.Any]
    indexableText: dict[str, typing.Any]
    isAppAuthorized: bool
    kind: str
    labelInfo: dict[str, typing.Any]
    labels: dict[str, typing.Any]
    lastModifyingUser: User
    lastModifyingUserName: str
    lastViewedByMeDate: str
    linkShareMetadata: dict[str, typing.Any]
    markedViewedByMeDate: str
    md5Checksum: str
    mimeType: str
    modifiedByMeDate: str
    modifiedDate: str
    openWithLinks: dict[str, typing.Any]
    originalFilename: str
    ownedByMe: bool
    ownerNames: _list[str]
    owners: _list[User]
    parents: _list[ParentReference]
    permissionIds: _list[str]
    permissions: _list[Permission]
    properties: _list[Property]
    quotaBytesUsed: str
    resourceKey: str
    selfLink: str
    sha1Checksum: str
    sha256Checksum: str
    shareable: bool
    shared: bool
    sharedWithMeDate: str
    sharingUser: User
    shortcutDetails: dict[str, typing.Any]
    spaces: _list[str]
    teamDriveId: str
    thumbnail: dict[str, typing.Any]
    thumbnailLink: str
    thumbnailVersion: str
    title: str
    trashedDate: str
    trashingUser: User
    userPermission: Permission
    version: str
    videoMediaMetadata: dict[str, typing.Any]
    webContentLink: str
    webViewLink: str
    writersCanShare: bool

@typing.type_check_only
class FileList(typing_extensions.TypedDict, total=False):
    etag: str
    incompleteSearch: bool
    items: _list[File]
    kind: str
    nextLink: str
    nextPageToken: str
    selfLink: str

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
    items: _list[Label]
    kind: str
    nextPageToken: str

@typing.type_check_only
class LabelModification(typing_extensions.TypedDict, total=False):
    fieldModifications: _list[LabelFieldModification]
    kind: str
    labelId: str
    removeLabel: bool

@typing.type_check_only
class ModifyLabelsRequest(typing_extensions.TypedDict, total=False):
    kind: str
    labelModifications: _list[LabelModification]

@typing.type_check_only
class ModifyLabelsResponse(typing_extensions.TypedDict, total=False):
    kind: str
    modifiedLabels: _list[Label]

@typing.type_check_only
class ParentList(typing_extensions.TypedDict, total=False):
    etag: str
    items: _list[ParentReference]
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
    additionalRoles: _list[str]
    authKey: str
    deleted: bool
    domain: str
    emailAddress: str
    etag: str
    expirationDate: str
    id: str
    kind: str
    name: str
    pendingOwner: bool
    permissionDetails: _list[dict[str, typing.Any]]
    photoLink: str
    role: str
    selfLink: str
    teamDrivePermissionDetails: _list[dict[str, typing.Any]]
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
    items: _list[Permission]
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
    items: _list[Property]
    kind: str
    selfLink: str

@typing.type_check_only
class Revision(typing_extensions.TypedDict, total=False):
    downloadUrl: str
    etag: str
    exportLinks: dict[str, typing.Any]
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
    items: _list[Revision]
    kind: str
    nextPageToken: str
    selfLink: str

@typing.type_check_only
class StartPageToken(typing_extensions.TypedDict, total=False):
    kind: str
    startPageToken: str

@typing.type_check_only
class TeamDrive(typing_extensions.TypedDict, total=False):
    backgroundImageFile: dict[str, typing.Any]
    backgroundImageLink: str
    capabilities: dict[str, typing.Any]
    colorRgb: str
    createdDate: str
    id: str
    kind: str
    name: str
    orgUnitId: str
    restrictions: dict[str, typing.Any]
    themeId: str

@typing.type_check_only
class TeamDriveList(typing_extensions.TypedDict, total=False):
    items: _list[TeamDrive]
    kind: str
    nextPageToken: str

@typing.type_check_only
class User(typing_extensions.TypedDict, total=False):
    displayName: str
    emailAddress: str
    isAuthenticatedUser: bool
    kind: str
    permissionId: str
    picture: dict[str, typing.Any]

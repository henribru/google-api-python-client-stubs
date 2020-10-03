import typing

import typing_extensions

class DeletedUser(typing_extensions.TypedDict, total=False): ...

class Permission(typing_extensions.TypedDict, total=False):
    group: Group
    user: User
    anyone: Anyone
    domain: Domain
    role: typing_extensions.Literal[
        "ROLE_UNSPECIFIED",
        "OWNER",
        "ORGANIZER",
        "FILE_ORGANIZER",
        "EDITOR",
        "COMMENTER",
        "VIEWER",
        "PUBLISHED_VIEWER",
    ]
    allowDiscovery: bool

class TargetReference(typing_extensions.TypedDict, total=False):
    drive: DriveReference
    teamDrive: TeamDriveReference
    driveItem: DriveItemReference

class Folder(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "MY_DRIVE_ROOT", "TEAM_DRIVE_ROOT", "STANDARD_FOLDER"
    ]

class DataLeakPreventionChange(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "FLAGGED", "CLEARED"]

class Anyone(typing_extensions.TypedDict, total=False): ...
class Edit(typing_extensions.TypedDict, total=False): ...

class Copy(typing_extensions.TypedDict, total=False):
    originalObject: TargetReference

class DriveReference(typing_extensions.TypedDict, total=False):
    name: str
    title: str

class Suggestion(typing_extensions.TypedDict, total=False):
    subtype: typing_extensions.Literal[
        "SUBTYPE_UNSPECIFIED",
        "ADDED",
        "DELETED",
        "REPLY_ADDED",
        "REPLY_DELETED",
        "ACCEPTED",
        "REJECTED",
        "ACCEPT_DELETED",
        "REJECT_DELETED",
    ]

class Action(typing_extensions.TypedDict, total=False):
    detail: ActionDetail
    timeRange: TimeRange
    target: Target
    timestamp: str
    actor: Actor

class DriveFolder(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "MY_DRIVE_ROOT", "SHARED_DRIVE_ROOT", "STANDARD_FOLDER"
    ]

class Rename(typing_extensions.TypedDict, total=False):
    oldTitle: str
    newTitle: str

class Actor(typing_extensions.TypedDict, total=False):
    impersonation: Impersonation
    administrator: Administrator
    anonymous: AnonymousUser
    user: User
    system: SystemEvent

class ApplicationReference(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["UNSPECIFIED_REFERENCE_TYPE", "LINK", "DISCUSS"]

class QueryDriveActivityResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    activities: typing.List[DriveActivity]

class New(typing_extensions.TypedDict, total=False): ...

class Create(typing_extensions.TypedDict, total=False):
    new: New
    copy: Copy
    upload: Upload

class UnknownUser(typing_extensions.TypedDict, total=False): ...

class Group(typing_extensions.TypedDict, total=False):
    title: str
    email: str

class Move(typing_extensions.TypedDict, total=False):
    addedParents: typing.List[TargetReference]
    removedParents: typing.List[TargetReference]

class AnonymousUser(typing_extensions.TypedDict, total=False): ...
class Administrator(typing_extensions.TypedDict, total=False): ...
class Upload(typing_extensions.TypedDict, total=False): ...

class TeamDrive(typing_extensions.TypedDict, total=False):
    root: DriveItem
    name: str
    title: str

class SettingsChange(typing_extensions.TypedDict, total=False):
    restrictionChanges: typing.List[RestrictionChange]

class KnownUser(typing_extensions.TypedDict, total=False):
    isCurrentUser: bool
    personName: str

class Restore(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "UNTRASH"]

class RestrictionChange(typing_extensions.TypedDict, total=False):
    newRestriction: typing_extensions.Literal[
        "RESTRICTION_UNSPECIFIED", "UNRESTRICTED", "FULLY_RESTRICTED"
    ]
    feature: typing_extensions.Literal[
        "FEATURE_UNSPECIFIED",
        "SHARING_OUTSIDE_DOMAIN",
        "DIRECT_SHARING",
        "ITEM_DUPLICATION",
        "DRIVE_FILE_STREAM",
    ]

class File(typing_extensions.TypedDict, total=False): ...

class SystemEvent(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal[
        "TYPE_UNSPECIFIED", "USER_DELETION", "TRASH_AUTO_PURGE"
    ]

class DriveFile(typing_extensions.TypedDict, total=False): ...

class ConsolidationStrategy(typing_extensions.TypedDict, total=False):
    legacy: Legacy
    none: NoConsolidation

class Owner(typing_extensions.TypedDict, total=False):
    user: User
    drive: DriveReference
    domain: Domain
    teamDrive: TeamDriveReference

class ActionDetail(typing_extensions.TypedDict, total=False):
    rename: Rename
    permissionChange: PermissionChange
    delete: Delete
    restore: Restore
    settingsChange: SettingsChange
    move: Move
    dlpChange: DataLeakPreventionChange
    edit: Edit
    create: Create
    comment: Comment
    reference: ApplicationReference

class Drive(typing_extensions.TypedDict, total=False):
    name: str
    root: DriveItem
    title: str

class Delete(typing_extensions.TypedDict, total=False):
    type: typing_extensions.Literal["TYPE_UNSPECIFIED", "TRASH", "PERMANENT_DELETE"]

class FileComment(typing_extensions.TypedDict, total=False):
    legacyCommentId: str
    legacyDiscussionId: str
    parent: DriveItem
    linkToDiscussion: str

class Target(typing_extensions.TypedDict, total=False):
    teamDrive: TeamDrive
    drive: Drive
    fileComment: FileComment
    driveItem: DriveItem

class QueryDriveActivityRequest(typing_extensions.TypedDict, total=False):
    itemName: str
    pageToken: str
    pageSize: int
    filter: str
    ancestorName: str
    consolidationStrategy: ConsolidationStrategy

class Impersonation(typing_extensions.TypedDict, total=False):
    impersonatedUser: User

class Assignment(typing_extensions.TypedDict, total=False):
    assignedUser: User
    subtype: typing_extensions.Literal[
        "SUBTYPE_UNSPECIFIED",
        "ADDED",
        "DELETED",
        "REPLY_ADDED",
        "REPLY_DELETED",
        "RESOLVED",
        "REOPENED",
        "REASSIGNED",
    ]

class NoConsolidation(typing_extensions.TypedDict, total=False): ...

class PermissionChange(typing_extensions.TypedDict, total=False):
    removedPermissions: typing.List[Permission]
    addedPermissions: typing.List[Permission]

class Post(typing_extensions.TypedDict, total=False):
    subtype: typing_extensions.Literal[
        "SUBTYPE_UNSPECIFIED",
        "ADDED",
        "DELETED",
        "REPLY_ADDED",
        "REPLY_DELETED",
        "RESOLVED",
        "REOPENED",
    ]

class DriveItem(typing_extensions.TypedDict, total=False):
    folder: Folder
    title: str
    name: str
    driveFolder: DriveFolder
    driveFile: DriveFile
    file: File
    mimeType: str
    owner: Owner

class Comment(typing_extensions.TypedDict, total=False):
    mentionedUsers: typing.List[User]
    suggestion: Suggestion
    post: Post
    assignment: Assignment

class DriveActivity(typing_extensions.TypedDict, total=False):
    actors: typing.List[Actor]
    targets: typing.List[Target]
    timeRange: TimeRange
    primaryActionDetail: ActionDetail
    actions: typing.List[Action]
    timestamp: str

class TeamDriveReference(typing_extensions.TypedDict, total=False):
    title: str
    name: str

class Legacy(typing_extensions.TypedDict, total=False): ...

class User(typing_extensions.TypedDict, total=False):
    unknownUser: UnknownUser
    knownUser: KnownUser
    deletedUser: DeletedUser

class TimeRange(typing_extensions.TypedDict, total=False):
    startTime: str
    endTime: str

class DriveItemReference(typing_extensions.TypedDict, total=False):
    folder: Folder
    title: str
    name: str
    file: File
    driveFolder: DriveFolder
    driveFile: DriveFile

class Domain(typing_extensions.TypedDict, total=False):
    name: str
    legacyId: str

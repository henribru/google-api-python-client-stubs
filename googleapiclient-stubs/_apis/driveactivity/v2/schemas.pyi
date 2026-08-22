import typing

_list = list

@typing.type_check_only
class Action(typing.TypedDict, total=False):
    actor: Actor
    detail: ActionDetail
    target: Target
    timeRange: TimeRange
    timestamp: str

@typing.type_check_only
class ActionDetail(typing.TypedDict, total=False):
    appliedLabelChange: AppliedLabelChange
    comment: Comment
    create: Create
    delete: Delete
    dlpChange: DataLeakPreventionChange
    edit: Edit
    move: Move
    permissionChange: PermissionChange
    reference: ApplicationReference
    rename: Rename
    restore: Restore
    settingsChange: SettingsChange

@typing.type_check_only
class Actor(typing.TypedDict, total=False):
    administrator: Administrator
    anonymous: AnonymousUser
    impersonation: Impersonation
    system: SystemEvent
    user: User

@typing.type_check_only
class Administrator(typing.TypedDict, total=False): ...

@typing.type_check_only
class AnonymousUser(typing.TypedDict, total=False): ...

@typing.type_check_only
class Anyone(typing.TypedDict, total=False): ...

@typing.type_check_only
class ApplicationReference(typing.TypedDict, total=False):
    type: typing.Literal["UNSPECIFIED_REFERENCE_TYPE", "LINK", "DISCUSS"]

@typing.type_check_only
class AppliedLabelChange(typing.TypedDict, total=False):
    changes: _list[AppliedLabelChangeDetail]

@typing.type_check_only
class AppliedLabelChangeDetail(typing.TypedDict, total=False):
    fieldChanges: _list[FieldValueChange]
    label: str
    title: str
    types: _list[
        typing.Literal[
            "TYPE_UNSPECIFIED",
            "LABEL_ADDED",
            "LABEL_REMOVED",
            "LABEL_FIELD_VALUE_CHANGED",
            "LABEL_APPLIED_BY_ITEM_CREATE",
        ]
    ]

@typing.type_check_only
class Assignment(typing.TypedDict, total=False):
    assignedUser: User
    subtype: typing.Literal[
        "SUBTYPE_UNSPECIFIED",
        "ADDED",
        "DELETED",
        "REPLY_ADDED",
        "REPLY_DELETED",
        "RESOLVED",
        "REOPENED",
        "REASSIGNED",
    ]

@typing.type_check_only
class Comment(typing.TypedDict, total=False):
    assignment: Assignment
    mentionedUsers: _list[User]
    post: Post
    suggestion: Suggestion

@typing.type_check_only
class ConsolidationStrategy(typing.TypedDict, total=False):
    legacy: Legacy
    none: NoConsolidation

@typing.type_check_only
class Copy(typing.TypedDict, total=False):
    originalObject: TargetReference

@typing.type_check_only
class Create(typing.TypedDict, total=False):
    copy: Copy
    new: New
    upload: Upload

@typing.type_check_only
class DataLeakPreventionChange(typing.TypedDict, total=False):
    type: typing.Literal["TYPE_UNSPECIFIED", "FLAGGED", "CLEARED"]

@typing.type_check_only
class Date(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class Delete(typing.TypedDict, total=False):
    type: typing.Literal["TYPE_UNSPECIFIED", "TRASH", "PERMANENT_DELETE"]

@typing.type_check_only
class DeletedUser(typing.TypedDict, total=False): ...

@typing.type_check_only
class Domain(typing.TypedDict, total=False):
    legacyId: str
    name: str

@typing.type_check_only
class Drive(typing.TypedDict, total=False):
    name: str
    root: DriveItem
    title: str

@typing.type_check_only
class DriveActivity(typing.TypedDict, total=False):
    actions: _list[Action]
    actors: _list[Actor]
    primaryActionDetail: ActionDetail
    targets: _list[Target]
    timeRange: TimeRange
    timestamp: str

@typing.type_check_only
class DriveFile(typing.TypedDict, total=False): ...

@typing.type_check_only
class DriveFolder(typing.TypedDict, total=False):
    type: typing.Literal[
        "TYPE_UNSPECIFIED", "MY_DRIVE_ROOT", "SHARED_DRIVE_ROOT", "STANDARD_FOLDER"
    ]

@typing.type_check_only
class DriveItem(typing.TypedDict, total=False):
    driveFile: DriveFile
    driveFolder: DriveFolder
    file: File
    folder: Folder
    mimeType: str
    name: str
    owner: Owner
    title: str

@typing.type_check_only
class DriveItemReference(typing.TypedDict, total=False):
    driveFile: DriveFile
    driveFolder: DriveFolder
    file: File
    folder: Folder
    name: str
    title: str

@typing.type_check_only
class DriveReference(typing.TypedDict, total=False):
    name: str
    title: str

@typing.type_check_only
class Edit(typing.TypedDict, total=False): ...

@typing.type_check_only
class FieldValue(typing.TypedDict, total=False):
    date: Date
    integer: Integer
    selection: Selection
    selectionList: SelectionList
    text: Text
    textList: TextList
    user: SingleUser
    userList: UserList

@typing.type_check_only
class FieldValueChange(typing.TypedDict, total=False):
    displayName: str
    fieldId: str
    newValue: FieldValue
    oldValue: FieldValue

@typing.type_check_only
class File(typing.TypedDict, total=False): ...

@typing.type_check_only
class FileComment(typing.TypedDict, total=False):
    legacyCommentId: str
    legacyDiscussionId: str
    linkToDiscussion: str
    parent: DriveItem

@typing.type_check_only
class Folder(typing.TypedDict, total=False):
    type: typing.Literal[
        "TYPE_UNSPECIFIED", "MY_DRIVE_ROOT", "TEAM_DRIVE_ROOT", "STANDARD_FOLDER"
    ]

@typing.type_check_only
class Group(typing.TypedDict, total=False):
    email: str
    title: str

@typing.type_check_only
class Impersonation(typing.TypedDict, total=False):
    impersonatedUser: User

@typing.type_check_only
class Integer(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class KnownUser(typing.TypedDict, total=False):
    isCurrentUser: bool
    personName: str

@typing.type_check_only
class Legacy(typing.TypedDict, total=False): ...

@typing.type_check_only
class Move(typing.TypedDict, total=False):
    addedParents: _list[TargetReference]
    removedParents: _list[TargetReference]

@typing.type_check_only
class New(typing.TypedDict, total=False): ...

@typing.type_check_only
class NoConsolidation(typing.TypedDict, total=False): ...

@typing.type_check_only
class Owner(typing.TypedDict, total=False):
    domain: Domain
    drive: DriveReference
    teamDrive: TeamDriveReference
    user: User

@typing.type_check_only
class Permission(typing.TypedDict, total=False):
    allowDiscovery: bool
    anyone: Anyone
    domain: Domain
    group: Group
    role: typing.Literal[
        "ROLE_UNSPECIFIED",
        "OWNER",
        "ORGANIZER",
        "FILE_ORGANIZER",
        "EDITOR",
        "COMMENTER",
        "VIEWER",
        "PUBLISHED_VIEWER",
    ]
    user: User

@typing.type_check_only
class PermissionChange(typing.TypedDict, total=False):
    addedPermissions: _list[Permission]
    removedPermissions: _list[Permission]

@typing.type_check_only
class Post(typing.TypedDict, total=False):
    subtype: typing.Literal[
        "SUBTYPE_UNSPECIFIED",
        "ADDED",
        "DELETED",
        "REPLY_ADDED",
        "REPLY_DELETED",
        "RESOLVED",
        "REOPENED",
    ]

@typing.type_check_only
class QueryDriveActivityRequest(typing.TypedDict, total=False):
    ancestorName: str
    consolidationStrategy: ConsolidationStrategy
    filter: str
    itemName: str
    pageSize: int
    pageToken: str

@typing.type_check_only
class QueryDriveActivityResponse(typing.TypedDict, total=False):
    activities: _list[DriveActivity]
    nextPageToken: str

@typing.type_check_only
class Rename(typing.TypedDict, total=False):
    newTitle: str
    oldTitle: str

@typing.type_check_only
class Restore(typing.TypedDict, total=False):
    type: typing.Literal["TYPE_UNSPECIFIED", "UNTRASH"]

@typing.type_check_only
class RestrictionChange(typing.TypedDict, total=False):
    feature: typing.Literal[
        "FEATURE_UNSPECIFIED",
        "SHARING_OUTSIDE_DOMAIN",
        "DIRECT_SHARING",
        "ITEM_DUPLICATION",
        "DRIVE_FILE_STREAM",
        "FILE_ORGANIZER_CAN_SHARE_FOLDERS",
        "READERS_CAN_DOWNLOAD",
        "WRITERS_CAN_DOWNLOAD",
    ]
    newRestriction: typing.Literal[
        "RESTRICTION_UNSPECIFIED", "UNRESTRICTED", "FULLY_RESTRICTED"
    ]

@typing.type_check_only
class Selection(typing.TypedDict, total=False):
    displayName: str
    value: str

@typing.type_check_only
class SelectionList(typing.TypedDict, total=False):
    values: _list[Selection]

@typing.type_check_only
class SettingsChange(typing.TypedDict, total=False):
    restrictionChanges: _list[RestrictionChange]

@typing.type_check_only
class SingleUser(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class Suggestion(typing.TypedDict, total=False):
    subtype: typing.Literal[
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

@typing.type_check_only
class SystemEvent(typing.TypedDict, total=False):
    type: typing.Literal["TYPE_UNSPECIFIED", "USER_DELETION", "TRASH_AUTO_PURGE"]

@typing.type_check_only
class Target(typing.TypedDict, total=False):
    drive: Drive
    driveItem: DriveItem
    fileComment: FileComment
    teamDrive: TeamDrive

@typing.type_check_only
class TargetReference(typing.TypedDict, total=False):
    drive: DriveReference
    driveItem: DriveItemReference
    teamDrive: TeamDriveReference

@typing.type_check_only
class TeamDrive(typing.TypedDict, total=False):
    name: str
    root: DriveItem
    title: str

@typing.type_check_only
class TeamDriveReference(typing.TypedDict, total=False):
    name: str
    title: str

@typing.type_check_only
class Text(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class TextList(typing.TypedDict, total=False):
    values: _list[Text]

@typing.type_check_only
class TimeRange(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class UnknownUser(typing.TypedDict, total=False): ...

@typing.type_check_only
class Upload(typing.TypedDict, total=False): ...

@typing.type_check_only
class User(typing.TypedDict, total=False):
    deletedUser: DeletedUser
    knownUser: KnownUser
    unknownUser: UnknownUser

@typing.type_check_only
class UserList(typing.TypedDict, total=False):
    values: _list[SingleUser]

import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class DriveResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AboutResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            includeSubscribed: bool = ...,
            maxChangeIdCount: str = ...,
            startChangeId: str = ...,
            **kwargs: typing.Any
        ) -> AboutHttpRequest: ...

    @typing.type_check_only
    class AppsResource(googleapiclient.discovery.Resource):
        def get(self, *, appId: str, **kwargs: typing.Any) -> AppHttpRequest: ...
        def list(
            self,
            *,
            appFilterExtensions: str = ...,
            appFilterMimeTypes: str = ...,
            languageCode: str = ...,
            **kwargs: typing.Any
        ) -> AppListHttpRequest: ...

    @typing.type_check_only
    class ChangesResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            changeId: str,
            driveId: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            teamDriveId: str = ...,
            **kwargs: typing.Any
        ) -> ChangeHttpRequest: ...
        def getStartPageToken(
            self,
            *,
            driveId: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            teamDriveId: str = ...,
            **kwargs: typing.Any
        ) -> StartPageTokenHttpRequest: ...
        def list(
            self,
            *,
            driveId: str = ...,
            includeCorpusRemovals: bool = ...,
            includeDeleted: bool = ...,
            includeItemsFromAllDrives: bool = ...,
            includeLabels: str = ...,
            includePermissionsForView: str = ...,
            includeSubscribed: bool = ...,
            includeTeamDriveItems: bool = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            spaces: str = ...,
            startChangeId: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            teamDriveId: str = ...,
            **kwargs: typing.Any
        ) -> ChangeListHttpRequest: ...
        def list_next(
            self, previous_request: ChangeListHttpRequest, previous_response: ChangeList
        ) -> ChangeListHttpRequest | None: ...
        def watch(
            self,
            *,
            body: Channel = ...,
            driveId: str = ...,
            includeCorpusRemovals: bool = ...,
            includeDeleted: bool = ...,
            includeItemsFromAllDrives: bool = ...,
            includeLabels: str = ...,
            includePermissionsForView: str = ...,
            includeSubscribed: bool = ...,
            includeTeamDriveItems: bool = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            spaces: str = ...,
            startChangeId: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            teamDriveId: str = ...,
            **kwargs: typing.Any
        ) -> ChannelHttpRequest: ...

    @typing.type_check_only
    class ChannelsResource(googleapiclient.discovery.Resource):
        def stop(
            self, *, body: Channel = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class ChildrenResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            folderId: str,
            childId: str,
            enforceSingleParent: bool = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, folderId: str, childId: str, **kwargs: typing.Any
        ) -> ChildReferenceHttpRequest: ...
        def insert(
            self,
            *,
            folderId: str,
            body: ChildReference = ...,
            enforceSingleParent: bool = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            **kwargs: typing.Any
        ) -> ChildReferenceHttpRequest: ...
        def list(
            self,
            *,
            folderId: str,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            q: str = ...,
            **kwargs: typing.Any
        ) -> ChildListHttpRequest: ...
        def list_next(
            self, previous_request: ChildListHttpRequest, previous_response: ChildList
        ) -> ChildListHttpRequest | None: ...

    @typing.type_check_only
    class CommentsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, fileId: str, commentId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            fileId: str,
            commentId: str,
            includeDeleted: bool = ...,
            **kwargs: typing.Any
        ) -> CommentHttpRequest: ...
        def insert(
            self, *, fileId: str, body: Comment = ..., **kwargs: typing.Any
        ) -> CommentHttpRequest: ...
        def list(
            self,
            *,
            fileId: str,
            includeDeleted: bool = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            updatedMin: str = ...,
            **kwargs: typing.Any
        ) -> CommentListHttpRequest: ...
        def list_next(
            self,
            previous_request: CommentListHttpRequest,
            previous_response: CommentList,
        ) -> CommentListHttpRequest | None: ...
        def patch(
            self,
            *,
            fileId: str,
            commentId: str,
            body: Comment = ...,
            **kwargs: typing.Any
        ) -> CommentHttpRequest: ...
        def update(
            self,
            *,
            fileId: str,
            commentId: str,
            body: Comment = ...,
            **kwargs: typing.Any
        ) -> CommentHttpRequest: ...

    @typing.type_check_only
    class DrivesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            driveId: str,
            allowItemDeletion: bool = ...,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            driveId: str,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any
        ) -> DriveHttpRequest: ...
        def hide(self, *, driveId: str, **kwargs: typing.Any) -> DriveHttpRequest: ...
        def insert(
            self, *, requestId: str, body: Drive = ..., **kwargs: typing.Any
        ) -> DriveHttpRequest: ...
        def list(
            self,
            *,
            maxResults: int = ...,
            pageToken: str = ...,
            q: str = ...,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any
        ) -> DriveListHttpRequest: ...
        def list_next(
            self, previous_request: DriveListHttpRequest, previous_response: DriveList
        ) -> DriveListHttpRequest | None: ...
        def unhide(self, *, driveId: str, **kwargs: typing.Any) -> DriveHttpRequest: ...
        def update(
            self,
            *,
            driveId: str,
            body: Drive = ...,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any
        ) -> DriveHttpRequest: ...

    @typing.type_check_only
    class FilesResource(googleapiclient.discovery.Resource):
        def copy(
            self,
            *,
            fileId: str,
            body: File = ...,
            convert: bool = ...,
            enforceSingleParent: bool = ...,
            includeLabels: str = ...,
            includePermissionsForView: str = ...,
            ocr: bool = ...,
            ocrLanguage: str = ...,
            pinned: bool = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            timedTextLanguage: str = ...,
            timedTextTrackName: str = ...,
            visibility: typing_extensions.Literal["DEFAULT", "PRIVATE"] = ...,
            **kwargs: typing.Any
        ) -> FileHttpRequest: ...
        def delete(
            self,
            *,
            fileId: str,
            enforceSingleParent: bool = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def emptyTrash(
            self, *, enforceSingleParent: bool = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def export(
            self, *, fileId: str, mimeType: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def generateIds(
            self,
            *,
            maxResults: int = ...,
            space: str = ...,
            type: str = ...,
            **kwargs: typing.Any
        ) -> GeneratedIdsHttpRequest: ...
        def get(
            self,
            *,
            fileId: str,
            acknowledgeAbuse: bool = ...,
            includeLabels: str = ...,
            includePermissionsForView: str = ...,
            projection: typing_extensions.Literal["BASIC", "FULL"] = ...,
            revisionId: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            updateViewedDate: bool = ...,
            **kwargs: typing.Any
        ) -> FileHttpRequest: ...
        def insert(
            self,
            *,
            body: File = ...,
            convert: bool = ...,
            enforceSingleParent: bool = ...,
            includeLabels: str = ...,
            includePermissionsForView: str = ...,
            ocr: bool = ...,
            ocrLanguage: str = ...,
            pinned: bool = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            timedTextLanguage: str = ...,
            timedTextTrackName: str = ...,
            useContentAsIndexableText: bool = ...,
            visibility: typing_extensions.Literal["DEFAULT", "PRIVATE"] = ...,
            **kwargs: typing.Any
        ) -> FileHttpRequest: ...
        def list(
            self,
            *,
            corpora: str = ...,
            corpus: typing_extensions.Literal["DEFAULT", "DOMAIN"] = ...,
            driveId: str = ...,
            includeItemsFromAllDrives: bool = ...,
            includeLabels: str = ...,
            includePermissionsForView: str = ...,
            includeTeamDriveItems: bool = ...,
            maxResults: int = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            projection: typing_extensions.Literal["BASIC", "FULL"] = ...,
            q: str = ...,
            spaces: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            teamDriveId: str = ...,
            **kwargs: typing.Any
        ) -> FileListHttpRequest: ...
        def list_next(
            self, previous_request: FileListHttpRequest, previous_response: FileList
        ) -> FileListHttpRequest | None: ...
        def listLabels(
            self,
            *,
            fileId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> LabelListHttpRequest: ...
        def listLabels_next(
            self, previous_request: LabelListHttpRequest, previous_response: LabelList
        ) -> LabelListHttpRequest | None: ...
        def modifyLabels(
            self, *, fileId: str, body: ModifyLabelsRequest = ..., **kwargs: typing.Any
        ) -> ModifyLabelsResponseHttpRequest: ...
        def patch(
            self,
            *,
            fileId: str,
            body: File = ...,
            addParents: str = ...,
            convert: bool = ...,
            enforceSingleParent: bool = ...,
            includeLabels: str = ...,
            includePermissionsForView: str = ...,
            modifiedDateBehavior: typing_extensions.Literal[
                "fromBody",
                "fromBodyIfNeeded",
                "fromBodyOrNow",
                "noChange",
                "now",
                "nowIfNeeded",
            ] = ...,
            newRevision: bool = ...,
            ocr: bool = ...,
            ocrLanguage: str = ...,
            pinned: bool = ...,
            removeParents: str = ...,
            setModifiedDate: bool = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            timedTextLanguage: str = ...,
            timedTextTrackName: str = ...,
            updateViewedDate: bool = ...,
            useContentAsIndexableText: bool = ...,
            **kwargs: typing.Any
        ) -> FileHttpRequest: ...
        def touch(
            self,
            *,
            fileId: str,
            includeLabels: str = ...,
            includePermissionsForView: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            **kwargs: typing.Any
        ) -> FileHttpRequest: ...
        def trash(
            self,
            *,
            fileId: str,
            includeLabels: str = ...,
            includePermissionsForView: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            **kwargs: typing.Any
        ) -> FileHttpRequest: ...
        def untrash(
            self,
            *,
            fileId: str,
            includeLabels: str = ...,
            includePermissionsForView: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            **kwargs: typing.Any
        ) -> FileHttpRequest: ...
        def update(
            self,
            *,
            fileId: str,
            body: File = ...,
            addParents: str = ...,
            convert: bool = ...,
            enforceSingleParent: bool = ...,
            includeLabels: str = ...,
            includePermissionsForView: str = ...,
            modifiedDateBehavior: typing_extensions.Literal[
                "fromBody",
                "fromBodyIfNeeded",
                "fromBodyOrNow",
                "noChange",
                "now",
                "nowIfNeeded",
            ] = ...,
            newRevision: bool = ...,
            ocr: bool = ...,
            ocrLanguage: str = ...,
            pinned: bool = ...,
            removeParents: str = ...,
            setModifiedDate: bool = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            timedTextLanguage: str = ...,
            timedTextTrackName: str = ...,
            updateViewedDate: bool = ...,
            useContentAsIndexableText: bool = ...,
            **kwargs: typing.Any
        ) -> FileHttpRequest: ...
        def watch(
            self,
            *,
            fileId: str,
            body: Channel = ...,
            acknowledgeAbuse: bool = ...,
            includeLabels: str = ...,
            includePermissionsForView: str = ...,
            projection: typing_extensions.Literal["BASIC", "FULL"] = ...,
            revisionId: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            updateViewedDate: bool = ...,
            **kwargs: typing.Any
        ) -> ChannelHttpRequest: ...

    @typing.type_check_only
    class ParentsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            fileId: str,
            parentId: str,
            enforceSingleParent: bool = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, fileId: str, parentId: str, **kwargs: typing.Any
        ) -> ParentReferenceHttpRequest: ...
        def insert(
            self,
            *,
            fileId: str,
            body: ParentReference = ...,
            enforceSingleParent: bool = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            **kwargs: typing.Any
        ) -> ParentReferenceHttpRequest: ...
        def list(
            self, *, fileId: str, **kwargs: typing.Any
        ) -> ParentListHttpRequest: ...

    @typing.type_check_only
    class PermissionsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            fileId: str,
            permissionId: str,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            fileId: str,
            permissionId: str,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any
        ) -> PermissionHttpRequest: ...
        def getIdForEmail(
            self, *, email: str, **kwargs: typing.Any
        ) -> PermissionIdHttpRequest: ...
        def insert(
            self,
            *,
            fileId: str,
            body: Permission = ...,
            emailMessage: str = ...,
            enforceSingleParent: bool = ...,
            moveToNewOwnersRoot: bool = ...,
            sendNotificationEmails: bool = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any
        ) -> PermissionHttpRequest: ...
        def list(
            self,
            *,
            fileId: str,
            includePermissionsForView: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any
        ) -> PermissionListHttpRequest: ...
        def list_next(
            self,
            previous_request: PermissionListHttpRequest,
            previous_response: PermissionList,
        ) -> PermissionListHttpRequest | None: ...
        def patch(
            self,
            *,
            fileId: str,
            permissionId: str,
            body: Permission = ...,
            removeExpiration: bool = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            transferOwnership: bool = ...,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any
        ) -> PermissionHttpRequest: ...
        def update(
            self,
            *,
            fileId: str,
            permissionId: str,
            body: Permission = ...,
            removeExpiration: bool = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            transferOwnership: bool = ...,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any
        ) -> PermissionHttpRequest: ...

    @typing.type_check_only
    class PropertiesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            fileId: str,
            propertyKey: str,
            visibility: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            fileId: str,
            propertyKey: str,
            visibility: str = ...,
            **kwargs: typing.Any
        ) -> PropertyHttpRequest: ...
        def insert(
            self, *, fileId: str, body: Property = ..., **kwargs: typing.Any
        ) -> PropertyHttpRequest: ...
        def list(
            self, *, fileId: str, **kwargs: typing.Any
        ) -> PropertyListHttpRequest: ...
        def patch(
            self,
            *,
            fileId: str,
            propertyKey: str,
            body: Property = ...,
            visibility: str = ...,
            **kwargs: typing.Any
        ) -> PropertyHttpRequest: ...
        def update(
            self,
            *,
            fileId: str,
            propertyKey: str,
            body: Property = ...,
            visibility: str = ...,
            **kwargs: typing.Any
        ) -> PropertyHttpRequest: ...

    @typing.type_check_only
    class RepliesResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, fileId: str, commentId: str, replyId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            fileId: str,
            commentId: str,
            replyId: str,
            includeDeleted: bool = ...,
            **kwargs: typing.Any
        ) -> CommentReplyHttpRequest: ...
        def insert(
            self,
            *,
            fileId: str,
            commentId: str,
            body: CommentReply = ...,
            **kwargs: typing.Any
        ) -> CommentReplyHttpRequest: ...
        def list(
            self,
            *,
            fileId: str,
            commentId: str,
            includeDeleted: bool = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> CommentReplyListHttpRequest: ...
        def list_next(
            self,
            previous_request: CommentReplyListHttpRequest,
            previous_response: CommentReplyList,
        ) -> CommentReplyListHttpRequest | None: ...
        def patch(
            self,
            *,
            fileId: str,
            commentId: str,
            replyId: str,
            body: CommentReply = ...,
            **kwargs: typing.Any
        ) -> CommentReplyHttpRequest: ...
        def update(
            self,
            *,
            fileId: str,
            commentId: str,
            replyId: str,
            body: CommentReply = ...,
            **kwargs: typing.Any
        ) -> CommentReplyHttpRequest: ...

    @typing.type_check_only
    class RevisionsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, fileId: str, revisionId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, fileId: str, revisionId: str, **kwargs: typing.Any
        ) -> RevisionHttpRequest: ...
        def list(
            self,
            *,
            fileId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> RevisionListHttpRequest: ...
        def list_next(
            self,
            previous_request: RevisionListHttpRequest,
            previous_response: RevisionList,
        ) -> RevisionListHttpRequest | None: ...
        def patch(
            self,
            *,
            fileId: str,
            revisionId: str,
            body: Revision = ...,
            **kwargs: typing.Any
        ) -> RevisionHttpRequest: ...
        def update(
            self,
            *,
            fileId: str,
            revisionId: str,
            body: Revision = ...,
            **kwargs: typing.Any
        ) -> RevisionHttpRequest: ...

    @typing.type_check_only
    class TeamdrivesResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, teamDriveId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            teamDriveId: str,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any
        ) -> TeamDriveHttpRequest: ...
        def insert(
            self, *, requestId: str, body: TeamDrive = ..., **kwargs: typing.Any
        ) -> TeamDriveHttpRequest: ...
        def list(
            self,
            *,
            maxResults: int = ...,
            pageToken: str = ...,
            q: str = ...,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any
        ) -> TeamDriveListHttpRequest: ...
        def list_next(
            self,
            previous_request: TeamDriveListHttpRequest,
            previous_response: TeamDriveList,
        ) -> TeamDriveListHttpRequest | None: ...
        def update(
            self,
            *,
            teamDriveId: str,
            body: TeamDrive = ...,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any
        ) -> TeamDriveHttpRequest: ...

    def new_batch_http_request(
        self,
        callback: collections.abc.Callable[
            [
                str,
                googleapiclient.http.HttpRequest,
                googleapiclient.errors.HttpError | None,
            ],
            typing.Any,
        ]
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def about(self) -> AboutResource: ...
    def apps(self) -> AppsResource: ...
    def changes(self) -> ChangesResource: ...
    def channels(self) -> ChannelsResource: ...
    def children(self) -> ChildrenResource: ...
    def comments(self) -> CommentsResource: ...
    def drives(self) -> DrivesResource: ...
    def files(self) -> FilesResource: ...
    def parents(self) -> ParentsResource: ...
    def permissions(self) -> PermissionsResource: ...
    def properties(self) -> PropertiesResource: ...
    def replies(self) -> RepliesResource: ...
    def revisions(self) -> RevisionsResource: ...
    def teamdrives(self) -> TeamdrivesResource: ...

@typing.type_check_only
class AboutHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> About: ...

@typing.type_check_only
class AppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> App: ...

@typing.type_check_only
class AppListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AppList: ...

@typing.type_check_only
class ChangeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Change: ...

@typing.type_check_only
class ChangeListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ChangeList: ...

@typing.type_check_only
class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Channel: ...

@typing.type_check_only
class ChildListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ChildList: ...

@typing.type_check_only
class ChildReferenceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ChildReference: ...

@typing.type_check_only
class CommentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Comment: ...

@typing.type_check_only
class CommentListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CommentList: ...

@typing.type_check_only
class CommentReplyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CommentReply: ...

@typing.type_check_only
class CommentReplyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CommentReplyList: ...

@typing.type_check_only
class DriveHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Drive: ...

@typing.type_check_only
class DriveListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DriveList: ...

@typing.type_check_only
class FileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> File: ...

@typing.type_check_only
class FileListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FileList: ...

@typing.type_check_only
class GeneratedIdsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GeneratedIds: ...

@typing.type_check_only
class LabelListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> LabelList: ...

@typing.type_check_only
class ModifyLabelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ModifyLabelsResponse: ...

@typing.type_check_only
class ParentListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ParentList: ...

@typing.type_check_only
class ParentReferenceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ParentReference: ...

@typing.type_check_only
class PermissionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Permission: ...

@typing.type_check_only
class PermissionIdHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PermissionId: ...

@typing.type_check_only
class PermissionListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PermissionList: ...

@typing.type_check_only
class PropertyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Property: ...

@typing.type_check_only
class PropertyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PropertyList: ...

@typing.type_check_only
class RevisionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Revision: ...

@typing.type_check_only
class RevisionListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RevisionList: ...

@typing.type_check_only
class StartPageTokenHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> StartPageToken: ...

@typing.type_check_only
class TeamDriveHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TeamDrive: ...

@typing.type_check_only
class TeamDriveListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TeamDriveList: ...

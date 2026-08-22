import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class DriveResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AboutResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            includeSubscribed: bool | None = ...,
            maxChangeIdCount: str | None = ...,
            startChangeId: str | None = ...,
            **kwargs: typing.Any,
        ) -> AboutHttpRequest: ...

    @typing.type_check_only
    class AppsResource(googleapiclient.discovery.Resource):
        def get(self, *, appId: str, **kwargs: typing.Any) -> AppHttpRequest: ...
        def list(
            self,
            *,
            appFilterExtensions: str | None = ...,
            appFilterMimeTypes: str | None = ...,
            languageCode: str | None = ...,
            **kwargs: typing.Any,
        ) -> AppListHttpRequest: ...

    @typing.type_check_only
    class ChangesResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            changeId: str,
            driveId: str | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            teamDriveId: str | None = ...,
            **kwargs: typing.Any,
        ) -> ChangeHttpRequest: ...
        def getStartPageToken(
            self,
            *,
            driveId: str | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            teamDriveId: str | None = ...,
            **kwargs: typing.Any,
        ) -> StartPageTokenHttpRequest: ...
        def list(
            self,
            *,
            driveId: str | None = ...,
            includeCorpusRemovals: bool | None = ...,
            includeDeleted: bool | None = ...,
            includeItemsFromAllDrives: bool | None = ...,
            includeLabels: str | None = ...,
            includePermissionsForView: str | None = ...,
            includeSubscribed: bool | None = ...,
            includeTeamDriveItems: bool | None = ...,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            spaces: str | None = ...,
            startChangeId: str | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            teamDriveId: str | None = ...,
            **kwargs: typing.Any,
        ) -> ChangeListHttpRequest: ...
        def list_next(
            self, previous_request: ChangeListHttpRequest, previous_response: ChangeList
        ) -> ChangeListHttpRequest | None: ...
        def watch(
            self,
            *,
            body: Channel,
            driveId: str | None = ...,
            includeCorpusRemovals: bool | None = ...,
            includeDeleted: bool | None = ...,
            includeItemsFromAllDrives: bool | None = ...,
            includeLabels: str | None = ...,
            includePermissionsForView: str | None = ...,
            includeSubscribed: bool | None = ...,
            includeTeamDriveItems: bool | None = ...,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            spaces: str | None = ...,
            startChangeId: str | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            teamDriveId: str | None = ...,
            **kwargs: typing.Any,
        ) -> ChannelHttpRequest: ...

    @typing.type_check_only
    class ChannelsResource(googleapiclient.discovery.Resource):
        def stop(
            self, *, body: Channel, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class ChildrenResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            folderId: str,
            childId: str,
            enforceSingleParent: bool | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, folderId: str, childId: str, **kwargs: typing.Any
        ) -> ChildReferenceHttpRequest: ...
        def insert(
            self,
            *,
            folderId: str,
            body: ChildReference,
            enforceSingleParent: bool | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            **kwargs: typing.Any,
        ) -> ChildReferenceHttpRequest: ...
        def list(
            self,
            *,
            folderId: str,
            maxResults: int | None = ...,
            orderBy: str | None = ...,
            pageToken: str | None = ...,
            q: str | None = ...,
            **kwargs: typing.Any,
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
            includeDeleted: bool | None = ...,
            **kwargs: typing.Any,
        ) -> CommentHttpRequest: ...
        def insert(
            self, *, fileId: str, body: Comment, **kwargs: typing.Any
        ) -> CommentHttpRequest: ...
        def list(
            self,
            *,
            fileId: str,
            includeDeleted: bool | None = ...,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            updatedMin: str | None = ...,
            **kwargs: typing.Any,
        ) -> CommentListHttpRequest: ...
        def list_next(
            self,
            previous_request: CommentListHttpRequest,
            previous_response: CommentList,
        ) -> CommentListHttpRequest | None: ...
        def patch(
            self, *, fileId: str, commentId: str, body: Comment, **kwargs: typing.Any
        ) -> CommentHttpRequest: ...
        def update(
            self, *, fileId: str, commentId: str, body: Comment, **kwargs: typing.Any
        ) -> CommentHttpRequest: ...

    @typing.type_check_only
    class DrivesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            driveId: str,
            allowItemDeletion: bool | None = ...,
            useDomainAdminAccess: bool | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            driveId: str,
            useDomainAdminAccess: bool | None = ...,
            **kwargs: typing.Any,
        ) -> DriveHttpRequest: ...
        def hide(self, *, driveId: str, **kwargs: typing.Any) -> DriveHttpRequest: ...
        def insert(
            self, *, requestId: str, body: Drive, **kwargs: typing.Any
        ) -> DriveHttpRequest: ...
        def list(
            self,
            *,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            q: str | None = ...,
            useDomainAdminAccess: bool | None = ...,
            **kwargs: typing.Any,
        ) -> DriveListHttpRequest: ...
        def list_next(
            self, previous_request: DriveListHttpRequest, previous_response: DriveList
        ) -> DriveListHttpRequest | None: ...
        def unhide(self, *, driveId: str, **kwargs: typing.Any) -> DriveHttpRequest: ...
        def update(
            self,
            *,
            driveId: str,
            body: Drive,
            useDomainAdminAccess: bool | None = ...,
            **kwargs: typing.Any,
        ) -> DriveHttpRequest: ...

    @typing.type_check_only
    class FilesResource(googleapiclient.discovery.Resource):
        def copy(
            self,
            *,
            fileId: str,
            body: File,
            convert: bool | None = ...,
            enforceSingleParent: bool | None = ...,
            includeLabels: str | None = ...,
            includePermissionsForView: str | None = ...,
            ocr: bool | None = ...,
            ocrLanguage: str | None = ...,
            pinned: bool | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            timedTextLanguage: str | None = ...,
            timedTextTrackName: str | None = ...,
            visibility: typing.Literal["DEFAULT", "PRIVATE"] | None = ...,
            **kwargs: typing.Any,
        ) -> FileHttpRequest: ...
        def delete(
            self,
            *,
            fileId: str,
            enforceSingleParent: bool | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def emptyTrash(
            self,
            *,
            driveId: str | None = ...,
            enforceSingleParent: bool | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def export(
            self, *, fileId: str, mimeType: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def export_media(
            self, *, fileId: str, mimeType: str, **kwargs: typing.Any
        ) -> BytesHttpRequest: ...
        def generateCseToken(
            self,
            *,
            fileId: str | None = ...,
            parent: str | None = ...,
            **kwargs: typing.Any,
        ) -> GenerateCseTokenResponseHttpRequest: ...
        def generateIds(
            self,
            *,
            maxResults: int | None = ...,
            space: str | None = ...,
            type: str | None = ...,
            **kwargs: typing.Any,
        ) -> GeneratedIdsHttpRequest: ...
        def get(
            self,
            *,
            fileId: str,
            acknowledgeAbuse: bool | None = ...,
            includeLabels: str | None = ...,
            includePermissionsForView: str | None = ...,
            projection: typing.Literal["BASIC", "FULL"] | None = ...,
            revisionId: str | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            updateViewedDate: bool | None = ...,
            **kwargs: typing.Any,
        ) -> FileHttpRequest: ...
        def get_media(
            self,
            *,
            fileId: str,
            acknowledgeAbuse: bool | None = ...,
            includeLabels: str | None = ...,
            includePermissionsForView: str | None = ...,
            projection: typing.Literal["BASIC", "FULL"] | None = ...,
            revisionId: str | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            updateViewedDate: bool | None = ...,
            **kwargs: typing.Any,
        ) -> BytesHttpRequest: ...
        def insert(
            self,
            *,
            body: File,
            convert: bool | None = ...,
            enforceSingleParent: bool | None = ...,
            includeLabels: str | None = ...,
            includePermissionsForView: str | None = ...,
            ocr: bool | None = ...,
            ocrLanguage: str | None = ...,
            pinned: bool | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            timedTextLanguage: str | None = ...,
            timedTextTrackName: str | None = ...,
            useContentAsIndexableText: bool | None = ...,
            visibility: typing.Literal["DEFAULT", "PRIVATE"] | None = ...,
            **kwargs: typing.Any,
        ) -> FileHttpRequest: ...
        def list(
            self,
            *,
            corpora: str | None = ...,
            corpus: typing.Literal["DEFAULT", "DOMAIN"] | None = ...,
            driveId: str | None = ...,
            includeItemsFromAllDrives: bool | None = ...,
            includeLabels: str | None = ...,
            includePermissionsForView: str | None = ...,
            includeTeamDriveItems: bool | None = ...,
            maxResults: int | None = ...,
            orderBy: str | None = ...,
            pageToken: str | None = ...,
            projection: typing.Literal["BASIC", "FULL"] | None = ...,
            q: str | None = ...,
            spaces: str | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            teamDriveId: str | None = ...,
            **kwargs: typing.Any,
        ) -> FileListHttpRequest: ...
        def list_next(
            self, previous_request: FileListHttpRequest, previous_response: FileList
        ) -> FileListHttpRequest | None: ...
        def listLabels(
            self,
            *,
            fileId: str,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> LabelListHttpRequest: ...
        def listLabels_next(
            self, previous_request: LabelListHttpRequest, previous_response: LabelList
        ) -> LabelListHttpRequest | None: ...
        def modifyLabels(
            self, *, fileId: str, body: ModifyLabelsRequest, **kwargs: typing.Any
        ) -> ModifyLabelsResponseHttpRequest: ...
        def patch(
            self,
            *,
            fileId: str,
            body: File,
            addParents: str | None = ...,
            convert: bool | None = ...,
            enforceSingleParent: bool | None = ...,
            includeLabels: str | None = ...,
            includePermissionsForView: str | None = ...,
            modifiedDateBehavior: typing.Literal[
                "fromBody",
                "fromBodyIfNeeded",
                "fromBodyOrNow",
                "noChange",
                "now",
                "nowIfNeeded",
            ]
            | None = ...,
            newRevision: bool | None = ...,
            ocr: bool | None = ...,
            ocrLanguage: str | None = ...,
            pinned: bool | None = ...,
            removeParents: str | None = ...,
            setModifiedDate: bool | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            timedTextLanguage: str | None = ...,
            timedTextTrackName: str | None = ...,
            updateViewedDate: bool | None = ...,
            useContentAsIndexableText: bool | None = ...,
            **kwargs: typing.Any,
        ) -> FileHttpRequest: ...
        def touch(
            self,
            *,
            fileId: str,
            includeLabels: str | None = ...,
            includePermissionsForView: str | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            **kwargs: typing.Any,
        ) -> FileHttpRequest: ...
        def trash(
            self,
            *,
            fileId: str,
            includeLabels: str | None = ...,
            includePermissionsForView: str | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            **kwargs: typing.Any,
        ) -> FileHttpRequest: ...
        def untrash(
            self,
            *,
            fileId: str,
            includeLabels: str | None = ...,
            includePermissionsForView: str | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            **kwargs: typing.Any,
        ) -> FileHttpRequest: ...
        def update(
            self,
            *,
            fileId: str,
            body: File,
            addParents: str | None = ...,
            convert: bool | None = ...,
            enforceSingleParent: bool | None = ...,
            includeLabels: str | None = ...,
            includePermissionsForView: str | None = ...,
            modifiedDateBehavior: typing.Literal[
                "fromBody",
                "fromBodyIfNeeded",
                "fromBodyOrNow",
                "noChange",
                "now",
                "nowIfNeeded",
            ]
            | None = ...,
            newRevision: bool | None = ...,
            ocr: bool | None = ...,
            ocrLanguage: str | None = ...,
            pinned: bool | None = ...,
            removeParents: str | None = ...,
            setModifiedDate: bool | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            timedTextLanguage: str | None = ...,
            timedTextTrackName: str | None = ...,
            updateViewedDate: bool | None = ...,
            useContentAsIndexableText: bool | None = ...,
            **kwargs: typing.Any,
        ) -> FileHttpRequest: ...
        def watch(
            self,
            *,
            fileId: str,
            body: Channel,
            acknowledgeAbuse: bool | None = ...,
            includeLabels: str | None = ...,
            includePermissionsForView: str | None = ...,
            projection: typing.Literal["BASIC", "FULL"] | None = ...,
            revisionId: str | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            updateViewedDate: bool | None = ...,
            **kwargs: typing.Any,
        ) -> ChannelHttpRequest: ...

    @typing.type_check_only
    class ParentsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            fileId: str,
            parentId: str,
            enforceSingleParent: bool | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, fileId: str, parentId: str, **kwargs: typing.Any
        ) -> ParentReferenceHttpRequest: ...
        def insert(
            self,
            *,
            fileId: str,
            body: ParentReference,
            enforceSingleParent: bool | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            **kwargs: typing.Any,
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
            enforceExpansiveAccess: bool | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            useDomainAdminAccess: bool | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            fileId: str,
            permissionId: str,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            useDomainAdminAccess: bool | None = ...,
            **kwargs: typing.Any,
        ) -> PermissionHttpRequest: ...
        def getIdForEmail(
            self, *, email: str, **kwargs: typing.Any
        ) -> PermissionIdHttpRequest: ...
        def insert(
            self,
            *,
            fileId: str,
            body: Permission,
            emailMessage: str | None = ...,
            enforceExpansiveAccess: bool | None = ...,
            enforceSingleParent: bool | None = ...,
            moveToNewOwnersRoot: bool | None = ...,
            sendNotificationEmails: bool | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            useDomainAdminAccess: bool | None = ...,
            **kwargs: typing.Any,
        ) -> PermissionHttpRequest: ...
        def list(
            self,
            *,
            fileId: str,
            includePermissionsForView: str | None = ...,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            useDomainAdminAccess: bool | None = ...,
            **kwargs: typing.Any,
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
            body: Permission,
            enforceExpansiveAccess: bool | None = ...,
            removeExpiration: bool | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            transferOwnership: bool | None = ...,
            useDomainAdminAccess: bool | None = ...,
            **kwargs: typing.Any,
        ) -> PermissionHttpRequest: ...
        def update(
            self,
            *,
            fileId: str,
            permissionId: str,
            body: Permission,
            enforceExpansiveAccess: bool | None = ...,
            removeExpiration: bool | None = ...,
            supportsAllDrives: bool | None = ...,
            supportsTeamDrives: bool | None = ...,
            transferOwnership: bool | None = ...,
            useDomainAdminAccess: bool | None = ...,
            **kwargs: typing.Any,
        ) -> PermissionHttpRequest: ...

    @typing.type_check_only
    class PropertiesResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            fileId: str,
            propertyKey: str,
            visibility: str | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            fileId: str,
            propertyKey: str,
            visibility: str | None = ...,
            **kwargs: typing.Any,
        ) -> PropertyHttpRequest: ...
        def insert(
            self, *, fileId: str, body: Property, **kwargs: typing.Any
        ) -> PropertyHttpRequest: ...
        def list(
            self, *, fileId: str, **kwargs: typing.Any
        ) -> PropertyListHttpRequest: ...
        def patch(
            self,
            *,
            fileId: str,
            propertyKey: str,
            body: Property,
            visibility: str | None = ...,
            **kwargs: typing.Any,
        ) -> PropertyHttpRequest: ...
        def update(
            self,
            *,
            fileId: str,
            propertyKey: str,
            body: Property,
            visibility: str | None = ...,
            **kwargs: typing.Any,
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
            includeDeleted: bool | None = ...,
            **kwargs: typing.Any,
        ) -> CommentReplyHttpRequest: ...
        def insert(
            self,
            *,
            fileId: str,
            commentId: str,
            body: CommentReply,
            **kwargs: typing.Any,
        ) -> CommentReplyHttpRequest: ...
        def list(
            self,
            *,
            fileId: str,
            commentId: str,
            includeDeleted: bool | None = ...,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
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
            body: CommentReply,
            **kwargs: typing.Any,
        ) -> CommentReplyHttpRequest: ...
        def update(
            self,
            *,
            fileId: str,
            commentId: str,
            replyId: str,
            body: CommentReply,
            **kwargs: typing.Any,
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
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> RevisionListHttpRequest: ...
        def list_next(
            self,
            previous_request: RevisionListHttpRequest,
            previous_response: RevisionList,
        ) -> RevisionListHttpRequest | None: ...
        def patch(
            self, *, fileId: str, revisionId: str, body: Revision, **kwargs: typing.Any
        ) -> RevisionHttpRequest: ...
        def update(
            self, *, fileId: str, revisionId: str, body: Revision, **kwargs: typing.Any
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
            useDomainAdminAccess: bool | None = ...,
            **kwargs: typing.Any,
        ) -> TeamDriveHttpRequest: ...
        def insert(
            self, *, requestId: str, body: TeamDrive, **kwargs: typing.Any
        ) -> TeamDriveHttpRequest: ...
        def list(
            self,
            *,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            q: str | None = ...,
            useDomainAdminAccess: bool | None = ...,
            **kwargs: typing.Any,
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
            body: TeamDrive,
            useDomainAdminAccess: bool | None = ...,
            **kwargs: typing.Any,
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
        | None = None,
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
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> About: ...

@typing.type_check_only
class AppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> App: ...

@typing.type_check_only
class AppListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AppList: ...

@typing.type_check_only
class ChangeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Change: ...

@typing.type_check_only
class ChangeListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ChangeList: ...

@typing.type_check_only
class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Channel: ...

@typing.type_check_only
class ChildListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ChildList: ...

@typing.type_check_only
class ChildReferenceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ChildReference: ...

@typing.type_check_only
class CommentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Comment: ...

@typing.type_check_only
class CommentListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CommentList: ...

@typing.type_check_only
class CommentReplyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CommentReply: ...

@typing.type_check_only
class CommentReplyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CommentReplyList: ...

@typing.type_check_only
class DriveHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Drive: ...

@typing.type_check_only
class DriveListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DriveList: ...

@typing.type_check_only
class FileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> File: ...

@typing.type_check_only
class FileListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FileList: ...

@typing.type_check_only
class GenerateCseTokenResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GenerateCseTokenResponse: ...

@typing.type_check_only
class GeneratedIdsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GeneratedIds: ...

@typing.type_check_only
class LabelListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LabelList: ...

@typing.type_check_only
class ModifyLabelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ModifyLabelsResponse: ...

@typing.type_check_only
class ParentListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ParentList: ...

@typing.type_check_only
class ParentReferenceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ParentReference: ...

@typing.type_check_only
class PermissionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Permission: ...

@typing.type_check_only
class PermissionIdHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PermissionId: ...

@typing.type_check_only
class PermissionListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PermissionList: ...

@typing.type_check_only
class PropertyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Property: ...

@typing.type_check_only
class PropertyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PropertyList: ...

@typing.type_check_only
class RevisionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Revision: ...

@typing.type_check_only
class RevisionListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RevisionList: ...

@typing.type_check_only
class StartPageTokenHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> StartPageToken: ...

@typing.type_check_only
class TeamDriveHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TeamDrive: ...

@typing.type_check_only
class TeamDriveListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TeamDriveList: ...

@typing.type_check_only
class BytesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> bytes: ...

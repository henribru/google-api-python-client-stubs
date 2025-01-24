import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class DriveResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AboutResource(googleapiclient.discovery.Resource):
        def get(self, **kwargs: typing.Any) -> AboutHttpRequest: ...

    @typing.type_check_only
    class AccessproposalsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, fileId: str, proposalId: str, **kwargs: typing.Any
        ) -> AccessProposalHttpRequest: ...
        def list(
            self,
            *,
            fileId: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ListAccessProposalsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListAccessProposalsResponseHttpRequest,
            previous_response: ListAccessProposalsResponse,
        ) -> ListAccessProposalsResponseHttpRequest | None: ...
        def resolve(
            self,
            *,
            fileId: str,
            proposalId: str,
            body: ResolveAccessProposalRequest = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class AppsResource(googleapiclient.discovery.Resource):
        def get(self, *, appId: str, **kwargs: typing.Any) -> AppHttpRequest: ...
        def list(
            self,
            *,
            appFilterExtensions: str = ...,
            appFilterMimeTypes: str = ...,
            languageCode: str = ...,
            **kwargs: typing.Any,
        ) -> AppListHttpRequest: ...

    @typing.type_check_only
    class ChangesResource(googleapiclient.discovery.Resource):
        def getStartPageToken(
            self,
            *,
            driveId: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            teamDriveId: str = ...,
            **kwargs: typing.Any,
        ) -> StartPageTokenHttpRequest: ...
        def list(
            self,
            *,
            pageToken: str,
            driveId: str = ...,
            includeCorpusRemovals: bool = ...,
            includeItemsFromAllDrives: bool = ...,
            includeLabels: str = ...,
            includePermissionsForView: str = ...,
            includeRemoved: bool = ...,
            includeTeamDriveItems: bool = ...,
            pageSize: int = ...,
            restrictToMyDrive: bool = ...,
            spaces: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            teamDriveId: str = ...,
            **kwargs: typing.Any,
        ) -> ChangeListHttpRequest: ...
        def list_next(
            self, previous_request: ChangeListHttpRequest, previous_response: ChangeList
        ) -> ChangeListHttpRequest | None: ...
        def watch(
            self,
            *,
            pageToken: str,
            body: Channel = ...,
            driveId: str = ...,
            includeCorpusRemovals: bool = ...,
            includeItemsFromAllDrives: bool = ...,
            includeLabels: str = ...,
            includePermissionsForView: str = ...,
            includeRemoved: bool = ...,
            includeTeamDriveItems: bool = ...,
            pageSize: int = ...,
            restrictToMyDrive: bool = ...,
            spaces: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            teamDriveId: str = ...,
            **kwargs: typing.Any,
        ) -> ChannelHttpRequest: ...

    @typing.type_check_only
    class ChannelsResource(googleapiclient.discovery.Resource):
        def stop(
            self, *, body: Channel = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class CommentsResource(googleapiclient.discovery.Resource):
        def create(
            self, *, fileId: str, body: Comment = ..., **kwargs: typing.Any
        ) -> CommentHttpRequest: ...
        def delete(
            self, *, fileId: str, commentId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            fileId: str,
            commentId: str,
            includeDeleted: bool = ...,
            **kwargs: typing.Any,
        ) -> CommentHttpRequest: ...
        def list(
            self,
            *,
            fileId: str,
            includeDeleted: bool = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            startModifiedTime: str = ...,
            **kwargs: typing.Any,
        ) -> CommentListHttpRequest: ...
        def list_next(
            self,
            previous_request: CommentListHttpRequest,
            previous_response: CommentList,
        ) -> CommentListHttpRequest | None: ...
        def update(
            self,
            *,
            fileId: str,
            commentId: str,
            body: Comment = ...,
            **kwargs: typing.Any,
        ) -> CommentHttpRequest: ...

    @typing.type_check_only
    class DrivesResource(googleapiclient.discovery.Resource):
        def create(
            self, *, requestId: str, body: Drive = ..., **kwargs: typing.Any
        ) -> DriveHttpRequest: ...
        def delete(
            self,
            *,
            driveId: str,
            allowItemDeletion: bool = ...,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            driveId: str,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any,
        ) -> DriveHttpRequest: ...
        def hide(self, *, driveId: str, **kwargs: typing.Any) -> DriveHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            q: str = ...,
            useDomainAdminAccess: bool = ...,
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
            body: Drive = ...,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any,
        ) -> DriveHttpRequest: ...

    @typing.type_check_only
    class FilesResource(googleapiclient.discovery.Resource):
        def copy(
            self,
            *,
            fileId: str,
            body: File = ...,
            enforceSingleParent: bool = ...,
            ignoreDefaultVisibility: bool = ...,
            includeLabels: str = ...,
            includePermissionsForView: str = ...,
            keepRevisionForever: bool = ...,
            ocrLanguage: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            **kwargs: typing.Any,
        ) -> FileHttpRequest: ...
        def create(
            self,
            *,
            body: File = ...,
            enforceSingleParent: bool = ...,
            ignoreDefaultVisibility: bool = ...,
            includeLabels: str = ...,
            includePermissionsForView: str = ...,
            keepRevisionForever: bool = ...,
            ocrLanguage: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            useContentAsIndexableText: bool = ...,
            **kwargs: typing.Any,
        ) -> FileHttpRequest: ...
        def delete(
            self,
            *,
            fileId: str,
            enforceSingleParent: bool = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def download(
            self,
            *,
            fileId: str,
            mimeType: str = ...,
            revisionId: str = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def emptyTrash(
            self,
            *,
            driveId: str = ...,
            enforceSingleParent: bool = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def export(
            self, *, fileId: str, mimeType: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def export_media(
            self, *, fileId: str, mimeType: str, **kwargs: typing.Any
        ) -> BytesHttpRequest: ...
        def generateIds(
            self,
            *,
            count: int = ...,
            space: str = ...,
            type: str = ...,
            **kwargs: typing.Any,
        ) -> GeneratedIdsHttpRequest: ...
        def get(
            self,
            *,
            fileId: str,
            acknowledgeAbuse: bool = ...,
            includeLabels: str = ...,
            includePermissionsForView: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            **kwargs: typing.Any,
        ) -> FileHttpRequest: ...
        def get_media(
            self,
            *,
            fileId: str,
            acknowledgeAbuse: bool = ...,
            includeLabels: str = ...,
            includePermissionsForView: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            **kwargs: typing.Any,
        ) -> BytesHttpRequest: ...
        def list(
            self,
            *,
            corpora: str = ...,
            corpus: typing_extensions.Literal["domain", "user"] = ...,
            driveId: str = ...,
            includeItemsFromAllDrives: bool = ...,
            includeLabels: str = ...,
            includePermissionsForView: str = ...,
            includeTeamDriveItems: bool = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            q: str = ...,
            spaces: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            teamDriveId: str = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> LabelListHttpRequest: ...
        def listLabels_next(
            self, previous_request: LabelListHttpRequest, previous_response: LabelList
        ) -> LabelListHttpRequest | None: ...
        def modifyLabels(
            self, *, fileId: str, body: ModifyLabelsRequest = ..., **kwargs: typing.Any
        ) -> ModifyLabelsResponseHttpRequest: ...
        def update(
            self,
            *,
            fileId: str,
            body: File = ...,
            addParents: str = ...,
            enforceSingleParent: bool = ...,
            includeLabels: str = ...,
            includePermissionsForView: str = ...,
            keepRevisionForever: bool = ...,
            ocrLanguage: str = ...,
            removeParents: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            useContentAsIndexableText: bool = ...,
            **kwargs: typing.Any,
        ) -> FileHttpRequest: ...
        def watch(
            self,
            *,
            fileId: str,
            body: Channel = ...,
            acknowledgeAbuse: bool = ...,
            includeLabels: str = ...,
            includePermissionsForView: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            **kwargs: typing.Any,
        ) -> ChannelHttpRequest: ...

    @typing.type_check_only
    class OperationResource(googleapiclient.discovery.Resource):
        def cancel(
            self, *, name: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            name: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ListOperationsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListOperationsResponseHttpRequest,
            previous_response: ListOperationsResponse,
        ) -> ListOperationsResponseHttpRequest | None: ...

    @typing.type_check_only
    class PermissionsResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            fileId: str,
            body: Permission = ...,
            emailMessage: str = ...,
            enforceSingleParent: bool = ...,
            moveToNewOwnersRoot: bool = ...,
            sendNotificationEmail: bool = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            transferOwnership: bool = ...,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any,
        ) -> PermissionHttpRequest: ...
        def delete(
            self,
            *,
            fileId: str,
            permissionId: str,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            fileId: str,
            permissionId: str,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any,
        ) -> PermissionHttpRequest: ...
        def list(
            self,
            *,
            fileId: str,
            includePermissionsForView: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any,
        ) -> PermissionListHttpRequest: ...
        def list_next(
            self,
            previous_request: PermissionListHttpRequest,
            previous_response: PermissionList,
        ) -> PermissionListHttpRequest | None: ...
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
            **kwargs: typing.Any,
        ) -> PermissionHttpRequest: ...

    @typing.type_check_only
    class RepliesResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            fileId: str,
            commentId: str,
            body: Reply = ...,
            **kwargs: typing.Any,
        ) -> ReplyHttpRequest: ...
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
            **kwargs: typing.Any,
        ) -> ReplyHttpRequest: ...
        def list(
            self,
            *,
            fileId: str,
            commentId: str,
            includeDeleted: bool = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ReplyListHttpRequest: ...
        def list_next(
            self, previous_request: ReplyListHttpRequest, previous_response: ReplyList
        ) -> ReplyListHttpRequest | None: ...
        def update(
            self,
            *,
            fileId: str,
            commentId: str,
            replyId: str,
            body: Reply = ...,
            **kwargs: typing.Any,
        ) -> ReplyHttpRequest: ...

    @typing.type_check_only
    class RevisionsResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, fileId: str, revisionId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            fileId: str,
            revisionId: str,
            acknowledgeAbuse: bool = ...,
            **kwargs: typing.Any,
        ) -> RevisionHttpRequest: ...
        def get_media(
            self,
            *,
            fileId: str,
            revisionId: str,
            acknowledgeAbuse: bool = ...,
            **kwargs: typing.Any,
        ) -> BytesHttpRequest: ...
        def list(
            self,
            *,
            fileId: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> RevisionListHttpRequest: ...
        def list_next(
            self,
            previous_request: RevisionListHttpRequest,
            previous_response: RevisionList,
        ) -> RevisionListHttpRequest | None: ...
        def update(
            self,
            *,
            fileId: str,
            revisionId: str,
            body: Revision = ...,
            **kwargs: typing.Any,
        ) -> RevisionHttpRequest: ...

    @typing.type_check_only
    class TeamdrivesResource(googleapiclient.discovery.Resource):
        def create(
            self, *, requestId: str, body: TeamDrive = ..., **kwargs: typing.Any
        ) -> TeamDriveHttpRequest: ...
        def delete(
            self, *, teamDriveId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            teamDriveId: str,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any,
        ) -> TeamDriveHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            q: str = ...,
            useDomainAdminAccess: bool = ...,
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
            body: TeamDrive = ...,
            useDomainAdminAccess: bool = ...,
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
    def accessproposals(self) -> AccessproposalsResource: ...
    def apps(self) -> AppsResource: ...
    def changes(self) -> ChangesResource: ...
    def channels(self) -> ChannelsResource: ...
    def comments(self) -> CommentsResource: ...
    def drives(self) -> DrivesResource: ...
    def files(self) -> FilesResource: ...
    def operation(self) -> OperationResource: ...
    def operations(self) -> OperationsResource: ...
    def permissions(self) -> PermissionsResource: ...
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
class AccessProposalHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AccessProposal: ...

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
class ListAccessProposalsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAccessProposalsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ModifyLabelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ModifyLabelsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class PermissionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Permission: ...

@typing.type_check_only
class PermissionListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PermissionList: ...

@typing.type_check_only
class ReplyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Reply: ...

@typing.type_check_only
class ReplyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ReplyList: ...

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

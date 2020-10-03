import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DriveResource(googleapiclient.discovery.Resource):
    class AboutResource(googleapiclient.discovery.Resource):
        def get(self, **kwargs: typing.Any) -> AboutHttpRequest: ...
    class ChangesResource(googleapiclient.discovery.Resource):
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
            pageToken: str,
            driveId: str = ...,
            includeCorpusRemovals: bool = ...,
            includeItemsFromAllDrives: bool = ...,
            includePermissionsForView: str = ...,
            includeRemoved: bool = ...,
            includeTeamDriveItems: bool = ...,
            pageSize: int = ...,
            restrictToMyDrive: bool = ...,
            spaces: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            teamDriveId: str = ...,
            **kwargs: typing.Any
        ) -> ChangeListHttpRequest: ...
        def watch(
            self,
            *,
            pageToken: str,
            body: Channel = ...,
            driveId: str = ...,
            includeCorpusRemovals: bool = ...,
            includeItemsFromAllDrives: bool = ...,
            includePermissionsForView: str = ...,
            includeRemoved: bool = ...,
            includeTeamDriveItems: bool = ...,
            pageSize: int = ...,
            restrictToMyDrive: bool = ...,
            spaces: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            teamDriveId: str = ...,
            **kwargs: typing.Any
        ) -> ChannelHttpRequest: ...
    class ChannelsResource(googleapiclient.discovery.Resource):
        def stop(
            self, *, body: Channel = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
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
            **kwargs: typing.Any
        ) -> CommentHttpRequest: ...
        def list(
            self,
            *,
            fileId: str,
            includeDeleted: bool = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            startModifiedTime: str = ...,
            **kwargs: typing.Any
        ) -> CommentListHttpRequest: ...
        def update(
            self,
            *,
            fileId: str,
            commentId: str,
            body: Comment = ...,
            **kwargs: typing.Any
        ) -> CommentHttpRequest: ...
    class DrivesResource(googleapiclient.discovery.Resource):
        def create(
            self, *, requestId: str, body: Drive = ..., **kwargs: typing.Any
        ) -> DriveHttpRequest: ...
        def delete(
            self, *, driveId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            driveId: str,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any
        ) -> DriveHttpRequest: ...
        def hide(self, *, driveId: str, **kwargs: typing.Any) -> DriveHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            q: str = ...,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any
        ) -> DriveListHttpRequest: ...
        def unhide(self, *, driveId: str, **kwargs: typing.Any) -> DriveHttpRequest: ...
        def update(
            self,
            *,
            driveId: str,
            body: Drive = ...,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any
        ) -> DriveHttpRequest: ...
    class FilesResource(googleapiclient.discovery.Resource):
        def copy(
            self,
            *,
            fileId: str,
            body: File = ...,
            enforceSingleParent: bool = ...,
            ignoreDefaultVisibility: bool = ...,
            includePermissionsForView: str = ...,
            keepRevisionForever: bool = ...,
            ocrLanguage: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            **kwargs: typing.Any
        ) -> FileHttpRequest: ...
        def create(
            self,
            *,
            body: File = ...,
            enforceSingleParent: bool = ...,
            ignoreDefaultVisibility: bool = ...,
            includePermissionsForView: str = ...,
            keepRevisionForever: bool = ...,
            ocrLanguage: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            useContentAsIndexableText: bool = ...,
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
            self, *, count: int = ..., space: str = ..., **kwargs: typing.Any
        ) -> GeneratedIdsHttpRequest: ...
        def get(
            self,
            *,
            fileId: str,
            acknowledgeAbuse: bool = ...,
            includePermissionsForView: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            **kwargs: typing.Any
        ) -> FileHttpRequest: ...
        def list(
            self,
            *,
            corpora: str = ...,
            corpus: typing_extensions.Literal["domain", "user"] = ...,
            driveId: str = ...,
            includeItemsFromAllDrives: bool = ...,
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
            **kwargs: typing.Any
        ) -> FileListHttpRequest: ...
        def update(
            self,
            *,
            fileId: str,
            body: File = ...,
            addParents: str = ...,
            enforceSingleParent: bool = ...,
            includePermissionsForView: str = ...,
            keepRevisionForever: bool = ...,
            ocrLanguage: str = ...,
            removeParents: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            useContentAsIndexableText: bool = ...,
            **kwargs: typing.Any
        ) -> FileHttpRequest: ...
        def watch(
            self,
            *,
            fileId: str,
            body: Channel = ...,
            acknowledgeAbuse: bool = ...,
            includePermissionsForView: str = ...,
            supportsAllDrives: bool = ...,
            supportsTeamDrives: bool = ...,
            **kwargs: typing.Any
        ) -> ChannelHttpRequest: ...
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
            **kwargs: typing.Any
        ) -> PermissionHttpRequest: ...
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
            **kwargs: typing.Any
        ) -> PermissionListHttpRequest: ...
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
    class RepliesResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            fileId: str,
            commentId: str,
            body: Reply = ...,
            **kwargs: typing.Any
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
            **kwargs: typing.Any
        ) -> ReplyHttpRequest: ...
        def list(
            self,
            *,
            fileId: str,
            commentId: str,
            includeDeleted: bool = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ReplyListHttpRequest: ...
        def update(
            self,
            *,
            fileId: str,
            commentId: str,
            replyId: str,
            body: Reply = ...,
            **kwargs: typing.Any
        ) -> ReplyHttpRequest: ...
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
            **kwargs: typing.Any
        ) -> RevisionHttpRequest: ...
        def list(
            self,
            *,
            fileId: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> RevisionListHttpRequest: ...
        def update(
            self,
            *,
            fileId: str,
            revisionId: str,
            body: Revision = ...,
            **kwargs: typing.Any
        ) -> RevisionHttpRequest: ...
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
            **kwargs: typing.Any
        ) -> TeamDriveHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            q: str = ...,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any
        ) -> TeamDriveListHttpRequest: ...
        def update(
            self,
            *,
            teamDriveId: str,
            body: TeamDrive = ...,
            useDomainAdminAccess: bool = ...,
            **kwargs: typing.Any
        ) -> TeamDriveHttpRequest: ...
    def about(self) -> AboutResource: ...
    def changes(self) -> ChangesResource: ...
    def channels(self) -> ChannelsResource: ...
    def comments(self) -> CommentsResource: ...
    def drives(self) -> DrivesResource: ...
    def files(self) -> FilesResource: ...
    def permissions(self) -> PermissionsResource: ...
    def replies(self) -> RepliesResource: ...
    def revisions(self) -> RevisionsResource: ...
    def teamdrives(self) -> TeamdrivesResource: ...

class AboutHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> About: ...

class DriveListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DriveList: ...

class CommentListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CommentList: ...

class ChangeListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ChangeList: ...

class StartPageTokenHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> StartPageToken: ...

class FileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> File: ...

class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Channel: ...

class FileListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FileList: ...

class TeamDriveHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TeamDrive: ...

class TeamDriveListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TeamDriveList: ...

class GeneratedIdsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GeneratedIds: ...

class RevisionListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RevisionList: ...

class PermissionListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PermissionList: ...

class CommentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Comment: ...

class DriveHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Drive: ...

class RevisionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Revision: ...

class ReplyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Reply: ...

class ReplyListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReplyList: ...

class PermissionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Permission: ...

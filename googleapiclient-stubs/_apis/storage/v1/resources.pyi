import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class StorageResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class BucketAccessControlsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            bucket: str,
            entity: str,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            entity: str,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> BucketAccessControlHttpRequest: ...
        def insert(
            self,
            *,
            bucket: str,
            body: BucketAccessControl = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> BucketAccessControlHttpRequest: ...
        def list(
            self, *, bucket: str, userProject: str = ..., **kwargs: typing.Any
        ) -> BucketAccessControlsHttpRequest: ...
        def patch(
            self,
            *,
            bucket: str,
            entity: str,
            body: BucketAccessControl = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> BucketAccessControlHttpRequest: ...
        def update(
            self,
            *,
            bucket: str,
            entity: str,
            body: BucketAccessControl = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> BucketAccessControlHttpRequest: ...

    @typing.type_check_only
    class BucketsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            bucket: str,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            projection: typing_extensions.Literal["full", "noAcl"] = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> BucketHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            bucket: str,
            optionsRequestedPolicyVersion: int = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: Bucket = ...,
            predefinedAcl: typing_extensions.Literal[
                "authenticatedRead",
                "private",
                "projectPrivate",
                "publicRead",
                "publicReadWrite",
            ] = ...,
            predefinedDefaultObjectAcl: typing_extensions.Literal[
                "authenticatedRead",
                "bucketOwnerFullControl",
                "bucketOwnerRead",
                "private",
                "projectPrivate",
                "publicRead",
            ] = ...,
            projection: typing_extensions.Literal["full", "noAcl"] = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> BucketHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            maxResults: int = ...,
            pageToken: str = ...,
            prefix: str = ...,
            projection: typing_extensions.Literal["full", "noAcl"] = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> BucketsHttpRequest: ...
        def list_next(
            self, previous_request: BucketsHttpRequest, previous_response: Buckets
        ) -> BucketsHttpRequest | None: ...
        def lockRetentionPolicy(
            self,
            *,
            bucket: str,
            ifMetagenerationMatch: str,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> BucketHttpRequest: ...
        def patch(
            self,
            *,
            bucket: str,
            body: Bucket = ...,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            predefinedAcl: typing_extensions.Literal[
                "authenticatedRead",
                "private",
                "projectPrivate",
                "publicRead",
                "publicReadWrite",
            ] = ...,
            predefinedDefaultObjectAcl: typing_extensions.Literal[
                "authenticatedRead",
                "bucketOwnerFullControl",
                "bucketOwnerRead",
                "private",
                "projectPrivate",
                "publicRead",
            ] = ...,
            projection: typing_extensions.Literal["full", "noAcl"] = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> BucketHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            bucket: str,
            body: Policy = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            bucket: str,
            permissions: str | _list[str],
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> TestIamPermissionsResponseHttpRequest: ...
        def update(
            self,
            *,
            bucket: str,
            body: Bucket = ...,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            predefinedAcl: typing_extensions.Literal[
                "authenticatedRead",
                "private",
                "projectPrivate",
                "publicRead",
                "publicReadWrite",
            ] = ...,
            predefinedDefaultObjectAcl: typing_extensions.Literal[
                "authenticatedRead",
                "bucketOwnerFullControl",
                "bucketOwnerRead",
                "private",
                "projectPrivate",
                "publicRead",
            ] = ...,
            projection: typing_extensions.Literal["full", "noAcl"] = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> BucketHttpRequest: ...

    @typing.type_check_only
    class ChannelsResource(googleapiclient.discovery.Resource):
        def stop(
            self, *, body: Channel = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class DefaultObjectAccessControlsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            bucket: str,
            entity: str,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            entity: str,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectAccessControlHttpRequest: ...
        def insert(
            self,
            *,
            bucket: str,
            body: ObjectAccessControl = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectAccessControlHttpRequest: ...
        def list(
            self,
            *,
            bucket: str,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectAccessControlsHttpRequest: ...
        def patch(
            self,
            *,
            bucket: str,
            entity: str,
            body: ObjectAccessControl = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectAccessControlHttpRequest: ...
        def update(
            self,
            *,
            bucket: str,
            entity: str,
            body: ObjectAccessControl = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectAccessControlHttpRequest: ...

    @typing.type_check_only
    class NotificationsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            bucket: str,
            notification: str,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            notification: str,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> NotificationHttpRequest: ...
        def insert(
            self,
            *,
            bucket: str,
            body: Notification = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> NotificationHttpRequest: ...
        def list(
            self, *, bucket: str, userProject: str = ..., **kwargs: typing.Any
        ) -> NotificationsHttpRequest: ...

    @typing.type_check_only
    class ObjectAccessControlsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            bucket: str,
            object: str,
            entity: str,
            generation: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            object: str,
            entity: str,
            generation: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectAccessControlHttpRequest: ...
        def insert(
            self,
            *,
            bucket: str,
            object: str,
            body: ObjectAccessControl = ...,
            generation: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectAccessControlHttpRequest: ...
        def list(
            self,
            *,
            bucket: str,
            object: str,
            generation: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectAccessControlsHttpRequest: ...
        def patch(
            self,
            *,
            bucket: str,
            object: str,
            entity: str,
            body: ObjectAccessControl = ...,
            generation: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectAccessControlHttpRequest: ...
        def update(
            self,
            *,
            bucket: str,
            object: str,
            entity: str,
            body: ObjectAccessControl = ...,
            generation: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectAccessControlHttpRequest: ...

    @typing.type_check_only
    class ObjectsResource(googleapiclient.discovery.Resource):
        def compose(
            self,
            *,
            destinationBucket: str,
            destinationObject: str,
            body: ComposeRequest = ...,
            destinationPredefinedAcl: typing_extensions.Literal[
                "authenticatedRead",
                "bucketOwnerFullControl",
                "bucketOwnerRead",
                "private",
                "projectPrivate",
                "publicRead",
            ] = ...,
            ifGenerationMatch: str = ...,
            ifMetagenerationMatch: str = ...,
            kmsKeyName: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectHttpRequest: ...
        def copy(
            self,
            *,
            sourceBucket: str,
            sourceObject: str,
            destinationBucket: str,
            destinationObject: str,
            body: Object = ...,
            destinationKmsKeyName: str = ...,
            destinationPredefinedAcl: typing_extensions.Literal[
                "authenticatedRead",
                "bucketOwnerFullControl",
                "bucketOwnerRead",
                "private",
                "projectPrivate",
                "publicRead",
            ] = ...,
            ifGenerationMatch: str = ...,
            ifGenerationNotMatch: str = ...,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            ifSourceGenerationMatch: str = ...,
            ifSourceGenerationNotMatch: str = ...,
            ifSourceMetagenerationMatch: str = ...,
            ifSourceMetagenerationNotMatch: str = ...,
            projection: typing_extensions.Literal["full", "noAcl"] = ...,
            sourceGeneration: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectHttpRequest: ...
        def delete(
            self,
            *,
            bucket: str,
            object: str,
            generation: str = ...,
            ifGenerationMatch: str = ...,
            ifGenerationNotMatch: str = ...,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            object: str,
            generation: str = ...,
            ifGenerationMatch: str = ...,
            ifGenerationNotMatch: str = ...,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            projection: typing_extensions.Literal["full", "noAcl"] = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            bucket: str,
            object: str,
            generation: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def insert(
            self,
            *,
            bucket: str,
            body: Object = ...,
            contentEncoding: str = ...,
            ifGenerationMatch: str = ...,
            ifGenerationNotMatch: str = ...,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            kmsKeyName: str = ...,
            name: str = ...,
            predefinedAcl: typing_extensions.Literal[
                "authenticatedRead",
                "bucketOwnerFullControl",
                "bucketOwnerRead",
                "private",
                "projectPrivate",
                "publicRead",
            ] = ...,
            projection: typing_extensions.Literal["full", "noAcl"] = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectHttpRequest: ...
        def list(
            self,
            *,
            bucket: str,
            delimiter: str = ...,
            endOffset: str = ...,
            includeTrailingDelimiter: bool = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            prefix: str = ...,
            projection: typing_extensions.Literal["full", "noAcl"] = ...,
            startOffset: str = ...,
            userProject: str = ...,
            versions: bool = ...,
            **kwargs: typing.Any
        ) -> ObjectsHttpRequest: ...
        def list_next(
            self, previous_request: ObjectsHttpRequest, previous_response: Objects
        ) -> ObjectsHttpRequest | None: ...
        def patch(
            self,
            *,
            bucket: str,
            object: str,
            body: Object = ...,
            generation: str = ...,
            ifGenerationMatch: str = ...,
            ifGenerationNotMatch: str = ...,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            predefinedAcl: typing_extensions.Literal[
                "authenticatedRead",
                "bucketOwnerFullControl",
                "bucketOwnerRead",
                "private",
                "projectPrivate",
                "publicRead",
            ] = ...,
            projection: typing_extensions.Literal["full", "noAcl"] = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectHttpRequest: ...
        def rewrite(
            self,
            *,
            sourceBucket: str,
            sourceObject: str,
            destinationBucket: str,
            destinationObject: str,
            body: Object = ...,
            destinationKmsKeyName: str = ...,
            destinationPredefinedAcl: typing_extensions.Literal[
                "authenticatedRead",
                "bucketOwnerFullControl",
                "bucketOwnerRead",
                "private",
                "projectPrivate",
                "publicRead",
            ] = ...,
            ifGenerationMatch: str = ...,
            ifGenerationNotMatch: str = ...,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            ifSourceGenerationMatch: str = ...,
            ifSourceGenerationNotMatch: str = ...,
            ifSourceMetagenerationMatch: str = ...,
            ifSourceMetagenerationNotMatch: str = ...,
            maxBytesRewrittenPerCall: str = ...,
            projection: typing_extensions.Literal["full", "noAcl"] = ...,
            rewriteToken: str = ...,
            sourceGeneration: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> RewriteResponseHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            bucket: str,
            object: str,
            body: Policy = ...,
            generation: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            bucket: str,
            object: str,
            permissions: str | _list[str],
            generation: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> TestIamPermissionsResponseHttpRequest: ...
        def update(
            self,
            *,
            bucket: str,
            object: str,
            body: Object = ...,
            generation: str = ...,
            ifGenerationMatch: str = ...,
            ifGenerationNotMatch: str = ...,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            predefinedAcl: typing_extensions.Literal[
                "authenticatedRead",
                "bucketOwnerFullControl",
                "bucketOwnerRead",
                "private",
                "projectPrivate",
                "publicRead",
            ] = ...,
            projection: typing_extensions.Literal["full", "noAcl"] = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectHttpRequest: ...
        def watchAll(
            self,
            *,
            bucket: str,
            body: Channel = ...,
            delimiter: str = ...,
            endOffset: str = ...,
            includeTrailingDelimiter: bool = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            prefix: str = ...,
            projection: typing_extensions.Literal["full", "noAcl"] = ...,
            startOffset: str = ...,
            userProject: str = ...,
            versions: bool = ...,
            **kwargs: typing.Any
        ) -> ChannelHttpRequest: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class HmacKeysResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                projectId: str,
                serviceAccountEmail: str,
                userProject: str = ...,
                **kwargs: typing.Any
            ) -> HmacKeyHttpRequest: ...
            def delete(
                self,
                *,
                projectId: str,
                accessId: str,
                userProject: str = ...,
                **kwargs: typing.Any
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self,
                *,
                projectId: str,
                accessId: str,
                userProject: str = ...,
                **kwargs: typing.Any
            ) -> HmacKeyMetadataHttpRequest: ...
            def list(
                self,
                *,
                projectId: str,
                maxResults: int = ...,
                pageToken: str = ...,
                serviceAccountEmail: str = ...,
                showDeletedKeys: bool = ...,
                userProject: str = ...,
                **kwargs: typing.Any
            ) -> HmacKeysMetadataHttpRequest: ...
            def list_next(
                self,
                previous_request: HmacKeysMetadataHttpRequest,
                previous_response: HmacKeysMetadata,
            ) -> HmacKeysMetadataHttpRequest | None: ...
            def update(
                self,
                *,
                projectId: str,
                accessId: str,
                body: HmacKeyMetadata = ...,
                userProject: str = ...,
                **kwargs: typing.Any
            ) -> HmacKeyMetadataHttpRequest: ...

        @typing.type_check_only
        class ServiceAccountResource(googleapiclient.discovery.Resource):
            def get(
                self, *, projectId: str, userProject: str = ..., **kwargs: typing.Any
            ) -> ServiceAccountHttpRequest: ...

        def hmacKeys(self) -> HmacKeysResource: ...
        def serviceAccount(self) -> ServiceAccountResource: ...

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
    def bucketAccessControls(self) -> BucketAccessControlsResource: ...
    def buckets(self) -> BucketsResource: ...
    def channels(self) -> ChannelsResource: ...
    def defaultObjectAccessControls(self) -> DefaultObjectAccessControlsResource: ...
    def notifications(self) -> NotificationsResource: ...
    def objectAccessControls(self) -> ObjectAccessControlsResource: ...
    def objects(self) -> ObjectsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class BucketHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Bucket: ...

@typing.type_check_only
class BucketAccessControlHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BucketAccessControl: ...

@typing.type_check_only
class BucketAccessControlsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BucketAccessControls: ...

@typing.type_check_only
class BucketsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Buckets: ...

@typing.type_check_only
class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Channel: ...

@typing.type_check_only
class HmacKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> HmacKey: ...

@typing.type_check_only
class HmacKeyMetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> HmacKeyMetadata: ...

@typing.type_check_only
class HmacKeysMetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> HmacKeysMetadata: ...

@typing.type_check_only
class NotificationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Notification: ...

@typing.type_check_only
class NotificationsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Notifications: ...

@typing.type_check_only
class ObjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Object: ...

@typing.type_check_only
class ObjectAccessControlHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ObjectAccessControl: ...

@typing.type_check_only
class ObjectAccessControlsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ObjectAccessControls: ...

@typing.type_check_only
class ObjectsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Objects: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class RewriteResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> RewriteResponse: ...

@typing.type_check_only
class ServiceAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ServiceAccount: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...

import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class StorageResource(googleapiclient.discovery.Resource):
    class BucketAccessControlsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            bucket: str,
            entity: str,
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            entity: str,
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> BucketAccessControlHttpRequest: ...
        def insert(
            self,
            *,
            bucket: str,
            body: BucketAccessControl = ...,
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> BucketAccessControlHttpRequest: ...
        def list(
            self,
            *,
            bucket: str,
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> BucketAccessControlsHttpRequest: ...
        def patch(
            self,
            *,
            bucket: str,
            entity: str,
            body: BucketAccessControl = ...,
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> BucketAccessControlHttpRequest: ...
        def update(
            self,
            *,
            bucket: str,
            entity: str,
            body: BucketAccessControl = ...,
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> BucketAccessControlHttpRequest: ...
    class BucketsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            bucket: str,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            provisionalUserProject: str = ...,
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
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> BucketHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            bucket: str,
            optionsRequestedPolicyVersion: int = ...,
            provisionalUserProject: str = ...,
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
            provisionalUserProject: str = ...,
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
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> BucketsHttpRequest: ...
        def lockRetentionPolicy(
            self,
            *,
            bucket: str,
            ifMetagenerationMatch: str,
            provisionalUserProject: str = ...,
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
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> BucketHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            bucket: str,
            body: Policy = ...,
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            bucket: str,
            permissions: typing.Union[str, typing.List[str]],
            provisionalUserProject: str = ...,
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
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> BucketHttpRequest: ...
    class ChannelsResource(googleapiclient.discovery.Resource):
        def stop(
            self, *, body: Channel = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
    class DefaultObjectAccessControlsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            bucket: str,
            entity: str,
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            entity: str,
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectAccessControlHttpRequest: ...
        def insert(
            self,
            *,
            bucket: str,
            body: ObjectAccessControl = ...,
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectAccessControlHttpRequest: ...
        def list(
            self,
            *,
            bucket: str,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectAccessControlsHttpRequest: ...
        def patch(
            self,
            *,
            bucket: str,
            entity: str,
            body: ObjectAccessControl = ...,
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectAccessControlHttpRequest: ...
        def update(
            self,
            *,
            bucket: str,
            entity: str,
            body: ObjectAccessControl = ...,
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectAccessControlHttpRequest: ...
    class NotificationsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            bucket: str,
            notification: str,
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            notification: str,
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> NotificationHttpRequest: ...
        def insert(
            self,
            *,
            bucket: str,
            body: Notification = ...,
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> NotificationHttpRequest: ...
        def list(
            self,
            *,
            bucket: str,
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> NotificationsHttpRequest: ...
    class ObjectAccessControlsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            bucket: str,
            object: str,
            entity: str,
            generation: str = ...,
            provisionalUserProject: str = ...,
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
            provisionalUserProject: str = ...,
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
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectAccessControlHttpRequest: ...
        def list(
            self,
            *,
            bucket: str,
            object: str,
            generation: str = ...,
            provisionalUserProject: str = ...,
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
            provisionalUserProject: str = ...,
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
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectAccessControlHttpRequest: ...
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
            provisionalUserProject: str = ...,
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
            provisionalUserProject: str = ...,
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
            provisionalUserProject: str = ...,
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
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> ObjectHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            bucket: str,
            object: str,
            generation: str = ...,
            provisionalUserProject: str = ...,
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
            provisionalUserProject: str = ...,
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
            provisionalUserProject: str = ...,
            startOffset: str = ...,
            userProject: str = ...,
            versions: bool = ...,
            **kwargs: typing.Any
        ) -> ObjectsHttpRequest: ...
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
            provisionalUserProject: str = ...,
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
            provisionalUserProject: str = ...,
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
            provisionalUserProject: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            bucket: str,
            object: str,
            permissions: typing.Union[str, typing.List[str]],
            generation: str = ...,
            provisionalUserProject: str = ...,
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
            provisionalUserProject: str = ...,
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
            provisionalUserProject: str = ...,
            startOffset: str = ...,
            userProject: str = ...,
            versions: bool = ...,
            **kwargs: typing.Any
        ) -> ChannelHttpRequest: ...
    class ProjectsResource(googleapiclient.discovery.Resource):
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
            def update(
                self,
                *,
                projectId: str,
                accessId: str,
                body: HmacKeyMetadata = ...,
                userProject: str = ...,
                **kwargs: typing.Any
            ) -> HmacKeyMetadataHttpRequest: ...
        class ServiceAccountResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                projectId: str,
                provisionalUserProject: str = ...,
                userProject: str = ...,
                **kwargs: typing.Any
            ) -> ServiceAccountHttpRequest: ...
        def hmacKeys(self) -> HmacKeysResource: ...
        def serviceAccount(self) -> ServiceAccountResource: ...
    def bucketAccessControls(self) -> BucketAccessControlsResource: ...
    def buckets(self) -> BucketsResource: ...
    def channels(self) -> ChannelsResource: ...
    def defaultObjectAccessControls(self) -> DefaultObjectAccessControlsResource: ...
    def notifications(self) -> NotificationsResource: ...
    def objectAccessControls(self) -> ObjectAccessControlsResource: ...
    def objects(self) -> ObjectsResource: ...
    def projects(self) -> ProjectsResource: ...

class BucketAccessControlHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BucketAccessControl: ...

class NotificationsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Notifications: ...

class BucketsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Buckets: ...

class ObjectAccessControlsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ObjectAccessControls: ...

class ServiceAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ServiceAccount: ...

class HmacKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> HmacKey: ...

class BucketAccessControlsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BucketAccessControls: ...

class ObjectAccessControlHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ObjectAccessControl: ...

class ObjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Object: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class NotificationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Notification: ...

class RewriteResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RewriteResponse: ...

class HmacKeysMetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> HmacKeysMetadata: ...

class HmacKeyMetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> HmacKeyMetadata: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Channel: ...

class BucketHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Bucket: ...

class ObjectsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Objects: ...

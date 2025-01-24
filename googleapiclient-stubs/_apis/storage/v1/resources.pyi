import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class StorageResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AnywhereCachesResource(googleapiclient.discovery.Resource):
        def disable(
            self, *, bucket: str, anywhereCacheId: str, **kwargs: typing.Any
        ) -> AnywhereCacheHttpRequest: ...
        def get(
            self, *, bucket: str, anywhereCacheId: str, **kwargs: typing.Any
        ) -> AnywhereCacheHttpRequest: ...
        def insert(
            self, *, bucket: str, body: AnywhereCache = ..., **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def list(
            self,
            *,
            bucket: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> AnywhereCachesHttpRequest: ...
        def list_next(
            self,
            previous_request: AnywhereCachesHttpRequest,
            previous_response: AnywhereCaches,
        ) -> AnywhereCachesHttpRequest | None: ...
        def pause(
            self, *, bucket: str, anywhereCacheId: str, **kwargs: typing.Any
        ) -> AnywhereCacheHttpRequest: ...
        def resume(
            self, *, bucket: str, anywhereCacheId: str, **kwargs: typing.Any
        ) -> AnywhereCacheHttpRequest: ...
        def update(
            self,
            *,
            bucket: str,
            anywhereCacheId: str,
            body: AnywhereCache = ...,
            **kwargs: typing.Any,
        ) -> GoogleLongrunningOperationHttpRequest: ...

    @typing.type_check_only
    class BucketAccessControlsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            bucket: str,
            entity: str,
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            entity: str,
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> BucketAccessControlHttpRequest: ...
        def insert(
            self,
            *,
            bucket: str,
            body: BucketAccessControl = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> BucketAccessControlHttpRequest: ...
        def update(
            self,
            *,
            bucket: str,
            entity: str,
            body: BucketAccessControl = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            generation: str = ...,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            projection: typing_extensions.Literal["full", "noAcl"] = ...,
            softDeleted: bool = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> BucketHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            bucket: str,
            optionsRequestedPolicyVersion: int = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def getStorageLayout(
            self, *, bucket: str, prefix: str = ..., **kwargs: typing.Any
        ) -> BucketStorageLayoutHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: Bucket = ...,
            enableObjectRetention: bool = ...,
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
            **kwargs: typing.Any,
        ) -> BucketHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            maxResults: int = ...,
            pageToken: str = ...,
            prefix: str = ...,
            projection: typing_extensions.Literal["full", "noAcl"] = ...,
            softDeleted: bool = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> BucketHttpRequest: ...
        def relocate(
            self,
            *,
            bucket: str,
            body: RelocateBucketRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def restore(
            self,
            *,
            bucket: str,
            generation: str,
            projection: typing_extensions.Literal["full", "noAcl"] = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> BucketHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            bucket: str,
            body: Policy = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            bucket: str,
            permissions: str | _list[str],
            userProject: str = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            entity: str,
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> ObjectAccessControlHttpRequest: ...
        def insert(
            self,
            *,
            bucket: str,
            body: ObjectAccessControl = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> ObjectAccessControlHttpRequest: ...
        def list(
            self,
            *,
            bucket: str,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> ObjectAccessControlsHttpRequest: ...
        def patch(
            self,
            *,
            bucket: str,
            entity: str,
            body: ObjectAccessControl = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> ObjectAccessControlHttpRequest: ...
        def update(
            self,
            *,
            bucket: str,
            entity: str,
            body: ObjectAccessControl = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> ObjectAccessControlHttpRequest: ...

    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            bucket: str,
            folder: str,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            folder: str,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            **kwargs: typing.Any,
        ) -> FolderHttpRequest: ...
        def insert(
            self,
            *,
            bucket: str,
            body: Folder = ...,
            recursive: bool = ...,
            **kwargs: typing.Any,
        ) -> FolderHttpRequest: ...
        def list(
            self,
            *,
            bucket: str,
            delimiter: str = ...,
            endOffset: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            prefix: str = ...,
            startOffset: str = ...,
            **kwargs: typing.Any,
        ) -> FoldersHttpRequest: ...
        def list_next(
            self, previous_request: FoldersHttpRequest, previous_response: Folders
        ) -> FoldersHttpRequest | None: ...
        def rename(
            self,
            *,
            bucket: str,
            sourceFolder: str,
            destinationFolder: str,
            ifSourceMetagenerationMatch: str = ...,
            ifSourceMetagenerationNotMatch: str = ...,
            **kwargs: typing.Any,
        ) -> GoogleLongrunningOperationHttpRequest: ...

    @typing.type_check_only
    class ManagedFoldersResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            bucket: str,
            managedFolder: str,
            allowNonEmpty: bool = ...,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            managedFolder: str,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            **kwargs: typing.Any,
        ) -> ManagedFolderHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            bucket: str,
            managedFolder: str,
            optionsRequestedPolicyVersion: int = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def insert(
            self, *, bucket: str, body: ManagedFolder = ..., **kwargs: typing.Any
        ) -> ManagedFolderHttpRequest: ...
        def list(
            self,
            *,
            bucket: str,
            pageSize: int = ...,
            pageToken: str = ...,
            prefix: str = ...,
            **kwargs: typing.Any,
        ) -> ManagedFoldersHttpRequest: ...
        def list_next(
            self,
            previous_request: ManagedFoldersHttpRequest,
            previous_response: ManagedFolders,
        ) -> ManagedFoldersHttpRequest | None: ...
        def setIamPolicy(
            self,
            *,
            bucket: str,
            managedFolder: str,
            body: Policy = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            bucket: str,
            managedFolder: str,
            permissions: str | _list[str],
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> TestIamPermissionsResponseHttpRequest: ...

    @typing.type_check_only
    class NotificationsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            bucket: str,
            notification: str,
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            notification: str,
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> NotificationHttpRequest: ...
        def insert(
            self,
            *,
            bucket: str,
            body: Notification = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            object: str,
            entity: str,
            generation: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> ObjectAccessControlHttpRequest: ...
        def insert(
            self,
            *,
            bucket: str,
            object: str,
            body: ObjectAccessControl = ...,
            generation: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> ObjectAccessControlHttpRequest: ...
        def list(
            self,
            *,
            bucket: str,
            object: str,
            generation: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> ObjectAccessControlHttpRequest: ...

    @typing.type_check_only
    class ObjectsResource(googleapiclient.discovery.Resource):
        def bulkRestore(
            self,
            *,
            bucket: str,
            body: BulkRestoreObjectsRequest = ...,
            **kwargs: typing.Any,
        ) -> GoogleLongrunningOperationHttpRequest: ...
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
            restoreToken: str = ...,
            softDeleted: bool = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> ObjectHttpRequest: ...
        def get_media(
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
            restoreToken: str = ...,
            softDeleted: bool = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> BytesHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            bucket: str,
            object: str,
            generation: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> ObjectHttpRequest: ...
        def list(
            self,
            *,
            bucket: str,
            delimiter: str = ...,
            endOffset: str = ...,
            includeFoldersAsPrefixes: bool = ...,
            includeTrailingDelimiter: bool = ...,
            matchGlob: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            prefix: str = ...,
            projection: typing_extensions.Literal["full", "noAcl"] = ...,
            softDeleted: bool = ...,
            startOffset: str = ...,
            userProject: str = ...,
            versions: bool = ...,
            **kwargs: typing.Any,
        ) -> ObjectsHttpRequest: ...
        def list_next(
            self, previous_request: ObjectsHttpRequest, previous_response: Objects
        ) -> ObjectsHttpRequest | None: ...
        def move(
            self,
            *,
            bucket: str,
            sourceObject: str,
            destinationObject: str,
            ifGenerationMatch: str = ...,
            ifGenerationNotMatch: str = ...,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            ifSourceGenerationMatch: str = ...,
            ifSourceGenerationNotMatch: str = ...,
            ifSourceMetagenerationMatch: str = ...,
            ifSourceMetagenerationNotMatch: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> ObjectHttpRequest: ...
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
            overrideUnlockedRetention: bool = ...,
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
            **kwargs: typing.Any,
        ) -> ObjectHttpRequest: ...
        def restore(
            self,
            *,
            bucket: str,
            object: str,
            generation: str,
            copySourceAcl: bool = ...,
            ifGenerationMatch: str = ...,
            ifGenerationNotMatch: str = ...,
            ifMetagenerationMatch: str = ...,
            ifMetagenerationNotMatch: str = ...,
            projection: typing_extensions.Literal["full", "noAcl"] = ...,
            restoreToken: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> RewriteResponseHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            bucket: str,
            object: str,
            body: Policy = ...,
            generation: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            bucket: str,
            object: str,
            permissions: str | _list[str],
            generation: str = ...,
            userProject: str = ...,
            **kwargs: typing.Any,
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
            overrideUnlockedRetention: bool = ...,
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
            **kwargs: typing.Any,
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
            **kwargs: typing.Any,
        ) -> ChannelHttpRequest: ...

    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def advanceRelocateBucket(
            self,
            *,
            bucket: str,
            operationId: str,
            body: AdvanceRelocateBucketOperationRequest = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def cancel(
            self, *, bucket: str, operationId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, bucket: str, operationId: str, **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def list(
            self,
            *,
            bucket: str,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleLongrunningListOperationsResponseHttpRequest,
            previous_response: GoogleLongrunningListOperationsResponse,
        ) -> GoogleLongrunningListOperationsResponseHttpRequest | None: ...

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
                **kwargs: typing.Any,
            ) -> HmacKeyHttpRequest: ...
            def delete(
                self,
                *,
                projectId: str,
                accessId: str,
                userProject: str = ...,
                **kwargs: typing.Any,
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self,
                *,
                projectId: str,
                accessId: str,
                userProject: str = ...,
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def anywhereCaches(self) -> AnywhereCachesResource: ...
    def bucketAccessControls(self) -> BucketAccessControlsResource: ...
    def buckets(self) -> BucketsResource: ...
    def channels(self) -> ChannelsResource: ...
    def defaultObjectAccessControls(self) -> DefaultObjectAccessControlsResource: ...
    def folders(self) -> FoldersResource: ...
    def managedFolders(self) -> ManagedFoldersResource: ...
    def notifications(self) -> NotificationsResource: ...
    def objectAccessControls(self) -> ObjectAccessControlsResource: ...
    def objects(self) -> ObjectsResource: ...
    def operations(self) -> OperationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AnywhereCacheHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AnywhereCache: ...

@typing.type_check_only
class AnywhereCachesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AnywhereCaches: ...

@typing.type_check_only
class BucketHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Bucket: ...

@typing.type_check_only
class BucketAccessControlHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BucketAccessControl: ...

@typing.type_check_only
class BucketAccessControlsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BucketAccessControls: ...

@typing.type_check_only
class BucketStorageLayoutHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BucketStorageLayout: ...

@typing.type_check_only
class BucketsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Buckets: ...

@typing.type_check_only
class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Channel: ...

@typing.type_check_only
class FolderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Folder: ...

@typing.type_check_only
class FoldersHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Folders: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class HmacKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> HmacKey: ...

@typing.type_check_only
class HmacKeyMetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> HmacKeyMetadata: ...

@typing.type_check_only
class HmacKeysMetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> HmacKeysMetadata: ...

@typing.type_check_only
class ManagedFolderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ManagedFolder: ...

@typing.type_check_only
class ManagedFoldersHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ManagedFolders: ...

@typing.type_check_only
class NotificationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Notification: ...

@typing.type_check_only
class NotificationsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Notifications: ...

@typing.type_check_only
class ObjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Object: ...

@typing.type_check_only
class ObjectAccessControlHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ObjectAccessControl: ...

@typing.type_check_only
class ObjectAccessControlsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ObjectAccessControls: ...

@typing.type_check_only
class ObjectsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Objects: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class RewriteResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RewriteResponse: ...

@typing.type_check_only
class ServiceAccountHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ServiceAccount: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...

@typing.type_check_only
class BytesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> bytes: ...

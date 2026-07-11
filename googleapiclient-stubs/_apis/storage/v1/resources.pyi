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
            self, *, bucket: str, body: AnywhereCache, **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def list(
            self,
            *,
            bucket: str,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
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
            body: AnywhereCache,
            **kwargs: typing.Any,
        ) -> GoogleLongrunningOperationHttpRequest: ...

    @typing.type_check_only
    class BucketAccessControlsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            bucket: str,
            entity: str,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            entity: str,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> BucketAccessControlHttpRequest: ...
        def insert(
            self,
            *,
            bucket: str,
            body: BucketAccessControl,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> BucketAccessControlHttpRequest: ...
        def list(
            self, *, bucket: str, userProject: str | None = ..., **kwargs: typing.Any
        ) -> BucketAccessControlsHttpRequest: ...
        def patch(
            self,
            *,
            bucket: str,
            entity: str,
            body: BucketAccessControl,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> BucketAccessControlHttpRequest: ...
        def update(
            self,
            *,
            bucket: str,
            entity: str,
            body: BucketAccessControl,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> BucketAccessControlHttpRequest: ...

    @typing.type_check_only
    class BucketsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            bucket: str,
            ifMetagenerationMatch: str | None = ...,
            ifMetagenerationNotMatch: str | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            generation: str | None = ...,
            ifMetagenerationMatch: str | None = ...,
            ifMetagenerationNotMatch: str | None = ...,
            projection: typing_extensions.Literal["full", "noAcl"] | None = ...,
            softDeleted: bool | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> BucketHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            bucket: str,
            optionsRequestedPolicyVersion: int | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def getStorageLayout(
            self, *, bucket: str, prefix: str | None = ..., **kwargs: typing.Any
        ) -> BucketStorageLayoutHttpRequest: ...
        def insert(
            self,
            *,
            project: str,
            body: Bucket,
            enableObjectRetention: bool | None = ...,
            predefinedAcl: typing_extensions.Literal[
                "authenticatedRead",
                "private",
                "projectPrivate",
                "publicRead",
                "publicReadWrite",
            ]
            | None = ...,
            predefinedDefaultObjectAcl: typing_extensions.Literal[
                "authenticatedRead",
                "bucketOwnerFullControl",
                "bucketOwnerRead",
                "private",
                "projectPrivate",
                "publicRead",
            ]
            | None = ...,
            projection: typing_extensions.Literal["full", "noAcl"] | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> BucketHttpRequest: ...
        def list(
            self,
            *,
            project: str,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            prefix: str | None = ...,
            projection: typing_extensions.Literal["full", "noAcl"] | None = ...,
            returnPartialSuccess: bool | None = ...,
            softDeleted: bool | None = ...,
            userProject: str | None = ...,
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
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> BucketHttpRequest: ...
        def patch(
            self,
            *,
            bucket: str,
            body: Bucket,
            ifMetagenerationMatch: str | None = ...,
            ifMetagenerationNotMatch: str | None = ...,
            predefinedAcl: typing_extensions.Literal[
                "authenticatedRead",
                "private",
                "projectPrivate",
                "publicRead",
                "publicReadWrite",
            ]
            | None = ...,
            predefinedDefaultObjectAcl: typing_extensions.Literal[
                "authenticatedRead",
                "bucketOwnerFullControl",
                "bucketOwnerRead",
                "private",
                "projectPrivate",
                "publicRead",
            ]
            | None = ...,
            projection: typing_extensions.Literal["full", "noAcl"] | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> BucketHttpRequest: ...
        def relocate(
            self, *, bucket: str, body: RelocateBucketRequest, **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def restore(
            self,
            *,
            bucket: str,
            generation: str,
            projection: typing_extensions.Literal["full", "noAcl"] | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> BucketHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            bucket: str,
            body: Policy,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            bucket: str,
            permissions: str | _list[str],
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> TestIamPermissionsResponseHttpRequest: ...
        def update(
            self,
            *,
            bucket: str,
            body: Bucket,
            ifMetagenerationMatch: str | None = ...,
            ifMetagenerationNotMatch: str | None = ...,
            predefinedAcl: typing_extensions.Literal[
                "authenticatedRead",
                "private",
                "projectPrivate",
                "publicRead",
                "publicReadWrite",
            ]
            | None = ...,
            predefinedDefaultObjectAcl: typing_extensions.Literal[
                "authenticatedRead",
                "bucketOwnerFullControl",
                "bucketOwnerRead",
                "private",
                "projectPrivate",
                "publicRead",
            ]
            | None = ...,
            projection: typing_extensions.Literal["full", "noAcl"] | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> BucketHttpRequest: ...

    @typing.type_check_only
    class ChannelsResource(googleapiclient.discovery.Resource):
        def stop(
            self, *, body: Channel, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class DefaultObjectAccessControlsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            bucket: str,
            entity: str,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            entity: str,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> ObjectAccessControlHttpRequest: ...
        def insert(
            self,
            *,
            bucket: str,
            body: ObjectAccessControl,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> ObjectAccessControlHttpRequest: ...
        def list(
            self,
            *,
            bucket: str,
            ifMetagenerationMatch: str | None = ...,
            ifMetagenerationNotMatch: str | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> ObjectAccessControlsHttpRequest: ...
        def patch(
            self,
            *,
            bucket: str,
            entity: str,
            body: ObjectAccessControl,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> ObjectAccessControlHttpRequest: ...
        def update(
            self,
            *,
            bucket: str,
            entity: str,
            body: ObjectAccessControl,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> ObjectAccessControlHttpRequest: ...

    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            bucket: str,
            folder: str,
            ifMetagenerationMatch: str | None = ...,
            ifMetagenerationNotMatch: str | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def deleteRecursive(
            self,
            *,
            bucket: str,
            folder: str,
            ifMetagenerationMatch: str | None = ...,
            ifMetagenerationNotMatch: str | None = ...,
            **kwargs: typing.Any,
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            folder: str,
            ifMetagenerationMatch: str | None = ...,
            ifMetagenerationNotMatch: str | None = ...,
            **kwargs: typing.Any,
        ) -> FolderHttpRequest: ...
        def insert(
            self,
            *,
            bucket: str,
            body: Folder,
            recursive: bool | None = ...,
            **kwargs: typing.Any,
        ) -> FolderHttpRequest: ...
        def list(
            self,
            *,
            bucket: str,
            delimiter: str | None = ...,
            endOffset: str | None = ...,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            prefix: str | None = ...,
            startOffset: str | None = ...,
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
            ifSourceMetagenerationMatch: str | None = ...,
            ifSourceMetagenerationNotMatch: str | None = ...,
            **kwargs: typing.Any,
        ) -> GoogleLongrunningOperationHttpRequest: ...

    @typing.type_check_only
    class ManagedFoldersResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            bucket: str,
            managedFolder: str,
            allowNonEmpty: bool | None = ...,
            ifMetagenerationMatch: str | None = ...,
            ifMetagenerationNotMatch: str | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            managedFolder: str,
            ifMetagenerationMatch: str | None = ...,
            ifMetagenerationNotMatch: str | None = ...,
            **kwargs: typing.Any,
        ) -> ManagedFolderHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            bucket: str,
            managedFolder: str,
            optionsRequestedPolicyVersion: int | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def insert(
            self, *, bucket: str, body: ManagedFolder, **kwargs: typing.Any
        ) -> ManagedFolderHttpRequest: ...
        def list(
            self,
            *,
            bucket: str,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
            prefix: str | None = ...,
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
            body: Policy,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            bucket: str,
            managedFolder: str,
            permissions: str | _list[str],
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> TestIamPermissionsResponseHttpRequest: ...

    @typing.type_check_only
    class NotificationsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            bucket: str,
            notification: str,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            notification: str,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> NotificationHttpRequest: ...
        def insert(
            self,
            *,
            bucket: str,
            body: Notification,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> NotificationHttpRequest: ...
        def list(
            self, *, bucket: str, userProject: str | None = ..., **kwargs: typing.Any
        ) -> NotificationsHttpRequest: ...

    @typing.type_check_only
    class ObjectAccessControlsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            bucket: str,
            object: str,
            entity: str,
            generation: str | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            object: str,
            entity: str,
            generation: str | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> ObjectAccessControlHttpRequest: ...
        def insert(
            self,
            *,
            bucket: str,
            object: str,
            body: ObjectAccessControl,
            generation: str | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> ObjectAccessControlHttpRequest: ...
        def list(
            self,
            *,
            bucket: str,
            object: str,
            generation: str | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> ObjectAccessControlsHttpRequest: ...
        def patch(
            self,
            *,
            bucket: str,
            object: str,
            entity: str,
            body: ObjectAccessControl,
            generation: str | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> ObjectAccessControlHttpRequest: ...
        def update(
            self,
            *,
            bucket: str,
            object: str,
            entity: str,
            body: ObjectAccessControl,
            generation: str | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> ObjectAccessControlHttpRequest: ...

    @typing.type_check_only
    class ObjectsResource(googleapiclient.discovery.Resource):
        def bulkRestore(
            self, *, bucket: str, body: BulkRestoreObjectsRequest, **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def compose(
            self,
            *,
            destinationBucket: str,
            destinationObject: str,
            body: ComposeRequest,
            destinationPredefinedAcl: typing_extensions.Literal[
                "authenticatedRead",
                "bucketOwnerFullControl",
                "bucketOwnerRead",
                "private",
                "projectPrivate",
                "publicRead",
            ]
            | None = ...,
            dropContextGroups: str | _list[str] | None = ...,
            ifGenerationMatch: str | None = ...,
            ifMetagenerationMatch: str | None = ...,
            kmsKeyName: str | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> ObjectHttpRequest: ...
        def copy(
            self,
            *,
            sourceBucket: str,
            sourceObject: str,
            destinationBucket: str,
            destinationObject: str,
            body: Object,
            destinationKmsKeyName: str | None = ...,
            destinationPredefinedAcl: typing_extensions.Literal[
                "authenticatedRead",
                "bucketOwnerFullControl",
                "bucketOwnerRead",
                "private",
                "projectPrivate",
                "publicRead",
            ]
            | None = ...,
            ifGenerationMatch: str | None = ...,
            ifGenerationNotMatch: str | None = ...,
            ifMetagenerationMatch: str | None = ...,
            ifMetagenerationNotMatch: str | None = ...,
            ifSourceGenerationMatch: str | None = ...,
            ifSourceGenerationNotMatch: str | None = ...,
            ifSourceMetagenerationMatch: str | None = ...,
            ifSourceMetagenerationNotMatch: str | None = ...,
            projection: typing_extensions.Literal["full", "noAcl"] | None = ...,
            sourceGeneration: str | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> ObjectHttpRequest: ...
        def delete(
            self,
            *,
            bucket: str,
            object: str,
            generation: str | None = ...,
            ifGenerationMatch: str | None = ...,
            ifGenerationNotMatch: str | None = ...,
            ifMetagenerationMatch: str | None = ...,
            ifMetagenerationNotMatch: str | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            bucket: str,
            object: str,
            generation: str | None = ...,
            ifGenerationMatch: str | None = ...,
            ifGenerationNotMatch: str | None = ...,
            ifMetagenerationMatch: str | None = ...,
            ifMetagenerationNotMatch: str | None = ...,
            projection: typing_extensions.Literal["full", "noAcl"] | None = ...,
            restoreToken: str | None = ...,
            softDeleted: bool | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> ObjectHttpRequest: ...
        def get_media(
            self,
            *,
            bucket: str,
            object: str,
            generation: str | None = ...,
            ifGenerationMatch: str | None = ...,
            ifGenerationNotMatch: str | None = ...,
            ifMetagenerationMatch: str | None = ...,
            ifMetagenerationNotMatch: str | None = ...,
            projection: typing_extensions.Literal["full", "noAcl"] | None = ...,
            restoreToken: str | None = ...,
            softDeleted: bool | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> BytesHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            bucket: str,
            object: str,
            generation: str | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def insert(
            self,
            *,
            bucket: str,
            body: Object,
            contentEncoding: str | None = ...,
            ifGenerationMatch: str | None = ...,
            ifGenerationNotMatch: str | None = ...,
            ifMetagenerationMatch: str | None = ...,
            ifMetagenerationNotMatch: str | None = ...,
            kmsKeyName: str | None = ...,
            name: str | None = ...,
            predefinedAcl: typing_extensions.Literal[
                "authenticatedRead",
                "bucketOwnerFullControl",
                "bucketOwnerRead",
                "private",
                "projectPrivate",
                "publicRead",
            ]
            | None = ...,
            projection: typing_extensions.Literal["full", "noAcl"] | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> ObjectHttpRequest: ...
        def list(
            self,
            *,
            bucket: str,
            delimiter: str | None = ...,
            endOffset: str | None = ...,
            filter: str | None = ...,
            includeFoldersAsPrefixes: bool | None = ...,
            includeTrailingDelimiter: bool | None = ...,
            matchGlob: str | None = ...,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            prefix: str | None = ...,
            projection: typing_extensions.Literal["full", "noAcl"] | None = ...,
            softDeleted: bool | None = ...,
            startOffset: str | None = ...,
            userProject: str | None = ...,
            versions: bool | None = ...,
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
            ifGenerationMatch: str | None = ...,
            ifGenerationNotMatch: str | None = ...,
            ifMetagenerationMatch: str | None = ...,
            ifMetagenerationNotMatch: str | None = ...,
            ifSourceGenerationMatch: str | None = ...,
            ifSourceGenerationNotMatch: str | None = ...,
            ifSourceMetagenerationMatch: str | None = ...,
            ifSourceMetagenerationNotMatch: str | None = ...,
            projection: typing_extensions.Literal["full", "noAcl"] | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> ObjectHttpRequest: ...
        def patch(
            self,
            *,
            bucket: str,
            object: str,
            body: Object,
            generation: str | None = ...,
            ifGenerationMatch: str | None = ...,
            ifGenerationNotMatch: str | None = ...,
            ifMetagenerationMatch: str | None = ...,
            ifMetagenerationNotMatch: str | None = ...,
            overrideUnlockedRetention: bool | None = ...,
            predefinedAcl: typing_extensions.Literal[
                "authenticatedRead",
                "bucketOwnerFullControl",
                "bucketOwnerRead",
                "private",
                "projectPrivate",
                "publicRead",
            ]
            | None = ...,
            projection: typing_extensions.Literal["full", "noAcl"] | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> ObjectHttpRequest: ...
        def restore(
            self,
            *,
            bucket: str,
            object: str,
            generation: str,
            copySourceAcl: bool | None = ...,
            ifGenerationMatch: str | None = ...,
            ifGenerationNotMatch: str | None = ...,
            ifMetagenerationMatch: str | None = ...,
            ifMetagenerationNotMatch: str | None = ...,
            projection: typing_extensions.Literal["full", "noAcl"] | None = ...,
            restoreToken: str | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> ObjectHttpRequest: ...
        def rewrite(
            self,
            *,
            sourceBucket: str,
            sourceObject: str,
            destinationBucket: str,
            destinationObject: str,
            body: Object,
            destinationKmsKeyName: str | None = ...,
            destinationPredefinedAcl: typing_extensions.Literal[
                "authenticatedRead",
                "bucketOwnerFullControl",
                "bucketOwnerRead",
                "private",
                "projectPrivate",
                "publicRead",
            ]
            | None = ...,
            dropContextGroups: str | _list[str] | None = ...,
            ifGenerationMatch: str | None = ...,
            ifGenerationNotMatch: str | None = ...,
            ifMetagenerationMatch: str | None = ...,
            ifMetagenerationNotMatch: str | None = ...,
            ifSourceGenerationMatch: str | None = ...,
            ifSourceGenerationNotMatch: str | None = ...,
            ifSourceMetagenerationMatch: str | None = ...,
            ifSourceMetagenerationNotMatch: str | None = ...,
            maxBytesRewrittenPerCall: str | None = ...,
            projection: typing_extensions.Literal["full", "noAcl"] | None = ...,
            rewriteToken: str | None = ...,
            sourceGeneration: str | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> RewriteResponseHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            bucket: str,
            object: str,
            body: Policy,
            generation: str | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            bucket: str,
            object: str,
            permissions: str | _list[str],
            generation: str | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> TestIamPermissionsResponseHttpRequest: ...
        def update(
            self,
            *,
            bucket: str,
            object: str,
            body: Object,
            generation: str | None = ...,
            ifGenerationMatch: str | None = ...,
            ifGenerationNotMatch: str | None = ...,
            ifMetagenerationMatch: str | None = ...,
            ifMetagenerationNotMatch: str | None = ...,
            overrideUnlockedRetention: bool | None = ...,
            predefinedAcl: typing_extensions.Literal[
                "authenticatedRead",
                "bucketOwnerFullControl",
                "bucketOwnerRead",
                "private",
                "projectPrivate",
                "publicRead",
            ]
            | None = ...,
            projection: typing_extensions.Literal["full", "noAcl"] | None = ...,
            userProject: str | None = ...,
            **kwargs: typing.Any,
        ) -> ObjectHttpRequest: ...

    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def advanceRelocateBucket(
            self,
            *,
            bucket: str,
            operationId: str,
            body: AdvanceRelocateBucketOperationRequest,
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
            filter: str | None = ...,
            pageSize: int | None = ...,
            pageToken: str | None = ...,
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
                userProject: str | None = ...,
                **kwargs: typing.Any,
            ) -> HmacKeyHttpRequest: ...
            def delete(
                self,
                *,
                projectId: str,
                accessId: str,
                userProject: str | None = ...,
                **kwargs: typing.Any,
            ) -> googleapiclient.http.HttpRequest: ...
            def get(
                self,
                *,
                projectId: str,
                accessId: str,
                userProject: str | None = ...,
                **kwargs: typing.Any,
            ) -> HmacKeyMetadataHttpRequest: ...
            def list(
                self,
                *,
                projectId: str,
                maxResults: int | None = ...,
                pageToken: str | None = ...,
                serviceAccountEmail: str | None = ...,
                showDeletedKeys: bool | None = ...,
                userProject: str | None = ...,
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
                body: HmacKeyMetadata,
                userProject: str | None = ...,
                **kwargs: typing.Any,
            ) -> HmacKeyMetadataHttpRequest: ...

        @typing.type_check_only
        class ServiceAccountResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                projectId: str,
                userProject: str | None = ...,
                **kwargs: typing.Any,
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

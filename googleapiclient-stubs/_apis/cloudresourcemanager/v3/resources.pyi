import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudResourceManagerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class EffectiveTagsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            parent: str = ...,
            **kwargs: typing.Any,
        ) -> ListEffectiveTagsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListEffectiveTagsResponseHttpRequest,
            previous_response: ListEffectiveTagsResponse,
        ) -> ListEffectiveTagsResponseHttpRequest | None: ...

    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: Folder = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> FolderHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            resource: str,
            body: GetIamPolicyRequest = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            parent: str = ...,
            showDeleted: bool = ...,
            **kwargs: typing.Any,
        ) -> ListFoldersResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListFoldersResponseHttpRequest,
            previous_response: ListFoldersResponse,
        ) -> ListFoldersResponseHttpRequest | None: ...
        def move(
            self, *, name: str, body: MoveFolderRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: Folder = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def search(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            query: str = ...,
            **kwargs: typing.Any,
        ) -> SearchFoldersResponseHttpRequest: ...
        def search_next(
            self,
            previous_request: SearchFoldersResponseHttpRequest,
            previous_response: SearchFoldersResponse,
        ) -> SearchFoldersResponseHttpRequest | None: ...
        def setIamPolicy(
            self,
            *,
            resource: str,
            body: SetIamPolicyRequest = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            resource: str,
            body: TestIamPermissionsRequest = ...,
            **kwargs: typing.Any,
        ) -> TestIamPermissionsResponseHttpRequest: ...
        def undelete(
            self, *, name: str, body: UndeleteFolderRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
    class LiensResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: Lien = ..., **kwargs: typing.Any
        ) -> LienHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> LienHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            parent: str = ...,
            **kwargs: typing.Any,
        ) -> ListLiensResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListLiensResponseHttpRequest,
            previous_response: ListLiensResponse,
        ) -> ListLiensResponseHttpRequest | None: ...

    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...

    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> OrganizationHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            resource: str,
            body: GetIamPolicyRequest = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def search(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            query: str = ...,
            **kwargs: typing.Any,
        ) -> SearchOrganizationsResponseHttpRequest: ...
        def search_next(
            self,
            previous_request: SearchOrganizationsResponseHttpRequest,
            previous_response: SearchOrganizationsResponse,
        ) -> SearchOrganizationsResponseHttpRequest | None: ...
        def setIamPolicy(
            self,
            *,
            resource: str,
            body: SetIamPolicyRequest = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            resource: str,
            body: TestIamPermissionsRequest = ...,
            **kwargs: typing.Any,
        ) -> TestIamPermissionsResponseHttpRequest: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: Project = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> ProjectHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            resource: str,
            body: GetIamPolicyRequest = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            parent: str = ...,
            showDeleted: bool = ...,
            **kwargs: typing.Any,
        ) -> ListProjectsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListProjectsResponseHttpRequest,
            previous_response: ListProjectsResponse,
        ) -> ListProjectsResponseHttpRequest | None: ...
        def move(
            self, *, name: str, body: MoveProjectRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def patch(
            self,
            *,
            name: str,
            body: Project = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def search(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            query: str = ...,
            **kwargs: typing.Any,
        ) -> SearchProjectsResponseHttpRequest: ...
        def search_next(
            self,
            previous_request: SearchProjectsResponseHttpRequest,
            previous_response: SearchProjectsResponse,
        ) -> SearchProjectsResponseHttpRequest | None: ...
        def setIamPolicy(
            self,
            *,
            resource: str,
            body: SetIamPolicyRequest = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            resource: str,
            body: TestIamPermissionsRequest = ...,
            **kwargs: typing.Any,
        ) -> TestIamPermissionsResponseHttpRequest: ...
        def undelete(
            self, *, name: str, body: UndeleteProjectRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
    class TagBindingsResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            body: TagBinding = ...,
            validateOnly: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            parent: str = ...,
            **kwargs: typing.Any,
        ) -> ListTagBindingsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListTagBindingsResponseHttpRequest,
            previous_response: ListTagBindingsResponse,
        ) -> ListTagBindingsResponseHttpRequest | None: ...

    @typing.type_check_only
    class TagKeysResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: TagKey = ..., validateOnly: bool = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(
            self,
            *,
            name: str,
            etag: str = ...,
            validateOnly: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> TagKeyHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            resource: str,
            body: GetIamPolicyRequest = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def getNamespaced(
            self, *, name: str = ..., **kwargs: typing.Any
        ) -> TagKeyHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            parent: str = ...,
            **kwargs: typing.Any,
        ) -> ListTagKeysResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListTagKeysResponseHttpRequest,
            previous_response: ListTagKeysResponse,
        ) -> ListTagKeysResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: TagKey = ...,
            updateMask: str = ...,
            validateOnly: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            resource: str,
            body: SetIamPolicyRequest = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            resource: str,
            body: TestIamPermissionsRequest = ...,
            **kwargs: typing.Any,
        ) -> TestIamPermissionsResponseHttpRequest: ...

    @typing.type_check_only
    class TagValuesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class TagHoldsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: TagHold = ...,
                validateOnly: bool = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def delete(
                self, *, name: str, validateOnly: bool = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListTagHoldsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListTagHoldsResponseHttpRequest,
                previous_response: ListTagHoldsResponse,
            ) -> ListTagHoldsResponseHttpRequest | None: ...

        def create(
            self,
            *,
            body: TagValue = ...,
            validateOnly: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def delete(
            self,
            *,
            name: str,
            etag: str = ...,
            validateOnly: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> TagValueHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            resource: str,
            body: GetIamPolicyRequest = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def getNamespaced(
            self, *, name: str = ..., **kwargs: typing.Any
        ) -> TagValueHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            parent: str = ...,
            **kwargs: typing.Any,
        ) -> ListTagValuesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListTagValuesResponseHttpRequest,
            previous_response: ListTagValuesResponse,
        ) -> ListTagValuesResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: TagValue = ...,
            updateMask: str = ...,
            validateOnly: bool = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            resource: str,
            body: SetIamPolicyRequest = ...,
            **kwargs: typing.Any,
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            resource: str,
            body: TestIamPermissionsRequest = ...,
            **kwargs: typing.Any,
        ) -> TestIamPermissionsResponseHttpRequest: ...
        def tagHolds(self) -> TagHoldsResource: ...

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
    def effectiveTags(self) -> EffectiveTagsResource: ...
    def folders(self) -> FoldersResource: ...
    def liens(self) -> LiensResource: ...
    def operations(self) -> OperationsResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...
    def tagBindings(self) -> TagBindingsResource: ...
    def tagKeys(self) -> TagKeysResource: ...
    def tagValues(self) -> TagValuesResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class FolderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Folder: ...

@typing.type_check_only
class LienHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Lien: ...

@typing.type_check_only
class ListEffectiveTagsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEffectiveTagsResponse: ...

@typing.type_check_only
class ListFoldersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListFoldersResponse: ...

@typing.type_check_only
class ListLiensResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLiensResponse: ...

@typing.type_check_only
class ListProjectsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListProjectsResponse: ...

@typing.type_check_only
class ListTagBindingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListTagBindingsResponse: ...

@typing.type_check_only
class ListTagHoldsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListTagHoldsResponse: ...

@typing.type_check_only
class ListTagKeysResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListTagKeysResponse: ...

@typing.type_check_only
class ListTagValuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListTagValuesResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class OrganizationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Organization: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class ProjectHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Project: ...

@typing.type_check_only
class SearchFoldersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchFoldersResponse: ...

@typing.type_check_only
class SearchOrganizationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchOrganizationsResponse: ...

@typing.type_check_only
class SearchProjectsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchProjectsResponse: ...

@typing.type_check_only
class TagKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TagKey: ...

@typing.type_check_only
class TagValueHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TagValue: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...

import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudResourceManagerResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: Folder = ..., parent: str = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> FolderHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> FolderHttpRequest: ...
        def getIamPolicy(
            self,
            *,
            resource: str,
            body: GetIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def list(
            self,
            *,
            pageSize: int = ...,
            pageToken: str = ...,
            parent: str = ...,
            showDeleted: bool = ...,
            **kwargs: typing.Any
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
            **kwargs: typing.Any
        ) -> FolderHttpRequest: ...
        def search(
            self, *, body: SearchFoldersRequest = ..., **kwargs: typing.Any
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
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            resource: str,
            body: TestIamPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestIamPermissionsResponseHttpRequest: ...
        def undelete(
            self, *, name: str, body: UndeleteFolderRequest = ..., **kwargs: typing.Any
        ) -> FolderHttpRequest: ...

    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...

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
    def folders(self) -> FoldersResource: ...
    def operations(self) -> OperationsResource: ...

@typing.type_check_only
class FolderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Folder: ...

@typing.type_check_only
class ListFoldersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListFoldersResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class SearchFoldersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SearchFoldersResponse: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...

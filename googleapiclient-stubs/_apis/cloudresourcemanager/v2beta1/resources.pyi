import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudResourceManagerResource(googleapiclient.discovery.Resource):
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
    class FoldersResource(googleapiclient.discovery.Resource):
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
        def get(self, *, name: str, **kwargs: typing.Any) -> FolderHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> FolderHttpRequest: ...
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
            showDeleted: bool = ...,
            parent: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListFoldersResponseHttpRequest: ...
        def testIamPermissions(
            self,
            *,
            resource: str,
            body: TestIamPermissionsRequest = ...,
            **kwargs: typing.Any
        ) -> TestIamPermissionsResponseHttpRequest: ...
        def setIamPolicy(
            self,
            *,
            resource: str,
            body: SetIamPolicyRequest = ...,
            **kwargs: typing.Any
        ) -> PolicyHttpRequest: ...
        def undelete(
            self, *, name: str, body: UndeleteFolderRequest = ..., **kwargs: typing.Any
        ) -> FolderHttpRequest: ...
        def create(
            self, *, body: Folder = ..., parent: str = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def move(
            self, *, name: str, body: MoveFolderRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    def operations(self) -> OperationsResource: ...
    def folders(self) -> FoldersResource: ...

class ListFoldersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListFoldersResponse: ...

class SearchFoldersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchFoldersResponse: ...

class FolderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Folder: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

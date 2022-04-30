import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudAssetResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        def exportAssets(
            self, *, parent: str, body: ExportAssetsRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def operations(self) -> OperationsResource: ...

    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        def batchGetAssetsHistory(
            self,
            *,
            parent: str,
            assetNames: str | _list[str] = ...,
            contentType: typing_extensions.Literal[
                "CONTENT_TYPE_UNSPECIFIED", "RESOURCE", "IAM_POLICY"
            ] = ...,
            readTimeWindow_endTime: str = ...,
            readTimeWindow_startTime: str = ...,
            **kwargs: typing.Any
        ) -> BatchGetAssetsHistoryResponseHttpRequest: ...
        def exportAssets(
            self, *, parent: str, body: ExportAssetsRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def operations(self) -> OperationsResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        def batchGetAssetsHistory(
            self,
            *,
            parent: str,
            assetNames: str | _list[str] = ...,
            contentType: typing_extensions.Literal[
                "CONTENT_TYPE_UNSPECIFIED", "RESOURCE", "IAM_POLICY"
            ] = ...,
            readTimeWindow_endTime: str = ...,
            readTimeWindow_startTime: str = ...,
            **kwargs: typing.Any
        ) -> BatchGetAssetsHistoryResponseHttpRequest: ...
        def exportAssets(
            self, *, parent: str, body: ExportAssetsRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def operations(self) -> OperationsResource: ...

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
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class BatchGetAssetsHistoryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchGetAssetsHistoryResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

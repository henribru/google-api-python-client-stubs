import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
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
            assetNames: typing.Union[str, typing.List[str]] = ...,
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
            assetNames: typing.Union[str, typing.List[str]] = ...,
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
    def folders(self) -> FoldersResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class BatchGetAssetsHistoryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BatchGetAssetsHistoryResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Operation: ...

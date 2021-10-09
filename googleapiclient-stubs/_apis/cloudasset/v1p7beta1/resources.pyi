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
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
    @typing.type_check_only
    class V1p7beta1Resource(googleapiclient.discovery.Resource):
        def exportAssets(
            self,
            *,
            parent: str,
            body: GoogleCloudAssetV1p7beta1ExportAssetsRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    def operations(self) -> OperationsResource: ...
    def v1p7beta1(self) -> V1p7beta1Resource: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

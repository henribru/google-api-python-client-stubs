import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class CloudAssetResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class V1p7beta1Resource(googleapiclient.discovery.Resource):
        def exportAssets(
            self,
            *,
            parent: str,
            body: GoogleCloudAssetV1p7beta1ExportAssetsRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    def v1p7beta1(self) -> V1p7beta1Resource: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Operation: ...

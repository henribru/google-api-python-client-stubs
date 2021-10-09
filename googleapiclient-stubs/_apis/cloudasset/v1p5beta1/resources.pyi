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
    class AssetsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            parent: str,
            assetTypes: str | _list[str] = ...,
            contentType: typing_extensions.Literal[
                "CONTENT_TYPE_UNSPECIFIED",
                "RESOURCE",
                "IAM_POLICY",
                "ORG_POLICY",
                "ACCESS_POLICY",
            ] = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            readTime: str = ...,
            **kwargs: typing.Any
        ) -> ListAssetsResponseHttpRequest: ...
    def assets(self) -> AssetsResource: ...

@typing.type_check_only
class ListAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAssetsResponse: ...

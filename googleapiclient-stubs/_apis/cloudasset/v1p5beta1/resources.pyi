import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudAssetResource(googleapiclient.discovery.Resource):
    class AssetsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            parent: str,
            pageToken: str = ...,
            readTime: str = ...,
            assetTypes: typing.Union[str, typing.List[str]] = ...,
            pageSize: int = ...,
            contentType: typing_extensions.Literal[
                "CONTENT_TYPE_UNSPECIFIED",
                "RESOURCE",
                "IAM_POLICY",
                "ORG_POLICY",
                "ACCESS_POLICY",
            ] = ...,
            **kwargs: typing.Any
        ) -> ListAssetsResponseHttpRequest: ...
    def assets(self) -> AssetsResource: ...

class ListAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAssetsResponse: ...

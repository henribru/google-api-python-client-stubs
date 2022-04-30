import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class DigitalassetlinksResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AssetlinksResource(googleapiclient.discovery.Resource):
        def bulkCheck(
            self, *, body: BulkCheckRequest = ..., **kwargs: typing.Any
        ) -> BulkCheckResponseHttpRequest: ...
        def check(
            self,
            *,
            relation: str = ...,
            source_androidApp_certificate_sha256Fingerprint: str = ...,
            source_androidApp_packageName: str = ...,
            source_web_site: str = ...,
            target_androidApp_certificate_sha256Fingerprint: str = ...,
            target_androidApp_packageName: str = ...,
            target_web_site: str = ...,
            **kwargs: typing.Any
        ) -> CheckResponseHttpRequest: ...

    @typing.type_check_only
    class StatementsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            relation: str = ...,
            source_androidApp_certificate_sha256Fingerprint: str = ...,
            source_androidApp_packageName: str = ...,
            source_web_site: str = ...,
            **kwargs: typing.Any
        ) -> ListResponseHttpRequest: ...

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
    def assetlinks(self) -> AssetlinksResource: ...
    def statements(self) -> StatementsResource: ...

@typing.type_check_only
class BulkCheckResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BulkCheckResponse: ...

@typing.type_check_only
class CheckResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CheckResponse: ...

@typing.type_check_only
class ListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListResponse: ...

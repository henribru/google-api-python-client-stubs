import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class SubscriptionLinkingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class PublicationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ReadersResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, name: str, force: bool = ..., **kwargs: typing.Any
            ) -> DeleteReaderResponseHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> ReaderHttpRequest: ...
            def getEntitlements(
                self, *, name: str, **kwargs: typing.Any
            ) -> ReaderEntitlementsHttpRequest: ...
            def updateEntitlements(
                self,
                *,
                name: str,
                body: ReaderEntitlements = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> ReaderEntitlementsHttpRequest: ...

        def readers(self) -> ReadersResource: ...

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
    def publications(self) -> PublicationsResource: ...

@typing.type_check_only
class DeleteReaderResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DeleteReaderResponse: ...

@typing.type_check_only
class ReaderHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Reader: ...

@typing.type_check_only
class ReaderEntitlementsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReaderEntitlements: ...

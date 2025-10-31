import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class MerchantResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ReportsResource(googleapiclient.discovery.Resource):
            def search(
                self, *, parent: str, body: SearchRequest = ..., **kwargs: typing.Any
            ) -> SearchResponseHttpRequest: ...
            def search_next(
                self,
                previous_request: SearchResponseHttpRequest,
                previous_response: SearchResponse,
            ) -> SearchResponseHttpRequest | None: ...

        def reports(self) -> ReportsResource: ...

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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def accounts(self) -> AccountsResource: ...

@typing.type_check_only
class SearchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchResponse: ...

import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class SafebrowsingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class HashesResource(googleapiclient.discovery.Resource):
        def search(
            self, *, hashPrefixes: str | _list[str] = ..., **kwargs: typing.Any
        ) -> GoogleSecuritySafebrowsingV5SearchHashesResponseHttpRequest: ...

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
    def hashes(self) -> HashesResource: ...

@typing.type_check_only
class GoogleSecuritySafebrowsingV5SearchHashesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleSecuritySafebrowsingV5SearchHashesResponse: ...

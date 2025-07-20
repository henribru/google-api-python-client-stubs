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
    class HashListResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            name: str,
            sizeConstraints_maxDatabaseEntries: int = ...,
            sizeConstraints_maxUpdateEntries: int = ...,
            version: str = ...,
            **kwargs: typing.Any,
        ) -> GoogleSecuritySafebrowsingV5HashListHttpRequest: ...

    @typing.type_check_only
    class HashListsResource(googleapiclient.discovery.Resource):
        def batchGet(
            self,
            *,
            names: str | _list[str] = ...,
            sizeConstraints_maxDatabaseEntries: int = ...,
            sizeConstraints_maxUpdateEntries: int = ...,
            version: str | _list[str] = ...,
            **kwargs: typing.Any,
        ) -> GoogleSecuritySafebrowsingV5BatchGetHashListsResponseHttpRequest: ...
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> GoogleSecuritySafebrowsingV5ListHashListsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: GoogleSecuritySafebrowsingV5ListHashListsResponseHttpRequest,
            previous_response: GoogleSecuritySafebrowsingV5ListHashListsResponse,
        ) -> GoogleSecuritySafebrowsingV5ListHashListsResponseHttpRequest | None: ...

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
    def hashList(self) -> HashListResource: ...
    def hashLists(self) -> HashListsResource: ...
    def hashes(self) -> HashesResource: ...

@typing.type_check_only
class GoogleSecuritySafebrowsingV5BatchGetHashListsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleSecuritySafebrowsingV5BatchGetHashListsResponse: ...

@typing.type_check_only
class GoogleSecuritySafebrowsingV5HashListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleSecuritySafebrowsingV5HashList: ...

@typing.type_check_only
class GoogleSecuritySafebrowsingV5ListHashListsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleSecuritySafebrowsingV5ListHashListsResponse: ...

@typing.type_check_only
class GoogleSecuritySafebrowsingV5SearchHashesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleSecuritySafebrowsingV5SearchHashesResponse: ...

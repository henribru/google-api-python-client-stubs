import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class SafebrowsingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class EncodedFullHashesResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            encodedRequest: str,
            clientId: str = ...,
            clientVersion: str = ...,
            **kwargs: typing.Any
        ) -> GoogleSecuritySafebrowsingV4FindFullHashesResponseHttpRequest: ...

    @typing.type_check_only
    class EncodedUpdatesResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            encodedRequest: str,
            clientId: str = ...,
            clientVersion: str = ...,
            **kwargs: typing.Any
        ) -> GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseHttpRequest: ...

    @typing.type_check_only
    class FullHashesResource(googleapiclient.discovery.Resource):
        def find(
            self,
            *,
            body: GoogleSecuritySafebrowsingV4FindFullHashesRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleSecuritySafebrowsingV4FindFullHashesResponseHttpRequest: ...

    @typing.type_check_only
    class ThreatHitsResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            body: GoogleSecuritySafebrowsingV4ThreatHit = ...,
            **kwargs: typing.Any
        ) -> GoogleProtobufEmptyHttpRequest: ...

    @typing.type_check_only
    class ThreatListUpdatesResource(googleapiclient.discovery.Resource):
        def fetch(
            self,
            *,
            body: GoogleSecuritySafebrowsingV4FetchThreatListUpdatesRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseHttpRequest: ...

    @typing.type_check_only
    class ThreatListsResource(googleapiclient.discovery.Resource):
        def list(
            self, **kwargs: typing.Any
        ) -> GoogleSecuritySafebrowsingV4ListThreatListsResponseHttpRequest: ...

    @typing.type_check_only
    class ThreatMatchesResource(googleapiclient.discovery.Resource):
        def find(
            self,
            *,
            body: GoogleSecuritySafebrowsingV4FindThreatMatchesRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleSecuritySafebrowsingV4FindThreatMatchesResponseHttpRequest: ...

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
    def encodedFullHashes(self) -> EncodedFullHashesResource: ...
    def encodedUpdates(self) -> EncodedUpdatesResource: ...
    def fullHashes(self) -> FullHashesResource: ...
    def threatHits(self) -> ThreatHitsResource: ...
    def threatListUpdates(self) -> ThreatListUpdatesResource: ...
    def threatLists(self) -> ThreatListsResource: ...
    def threatMatches(self) -> ThreatMatchesResource: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...

@typing.type_check_only
class GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleSecuritySafebrowsingV4FetchThreatListUpdatesResponse: ...

@typing.type_check_only
class GoogleSecuritySafebrowsingV4FindFullHashesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleSecuritySafebrowsingV4FindFullHashesResponse: ...

@typing.type_check_only
class GoogleSecuritySafebrowsingV4FindThreatMatchesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleSecuritySafebrowsingV4FindThreatMatchesResponse: ...

@typing.type_check_only
class GoogleSecuritySafebrowsingV4ListThreatListsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleSecuritySafebrowsingV4ListThreatListsResponse: ...

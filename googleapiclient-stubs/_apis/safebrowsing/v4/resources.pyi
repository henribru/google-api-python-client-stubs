import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
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
        ) -> FindFullHashesResponseHttpRequest: ...
    @typing.type_check_only
    class EncodedUpdatesResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            encodedRequest: str,
            clientId: str = ...,
            clientVersion: str = ...,
            **kwargs: typing.Any
        ) -> FetchThreatListUpdatesResponseHttpRequest: ...
    @typing.type_check_only
    class FullHashesResource(googleapiclient.discovery.Resource):
        def find(
            self, *, body: FindFullHashesRequest = ..., **kwargs: typing.Any
        ) -> FindFullHashesResponseHttpRequest: ...
    @typing.type_check_only
    class ThreatHitsResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: ThreatHit = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
    @typing.type_check_only
    class ThreatListUpdatesResource(googleapiclient.discovery.Resource):
        def fetch(
            self, *, body: FetchThreatListUpdatesRequest = ..., **kwargs: typing.Any
        ) -> FetchThreatListUpdatesResponseHttpRequest: ...
    @typing.type_check_only
    class ThreatListsResource(googleapiclient.discovery.Resource):
        def list(self, **kwargs: typing.Any) -> ListThreatListsResponseHttpRequest: ...
    @typing.type_check_only
    class ThreatMatchesResource(googleapiclient.discovery.Resource):
        def find(
            self, *, body: FindThreatMatchesRequest = ..., **kwargs: typing.Any
        ) -> FindThreatMatchesResponseHttpRequest: ...
    def encodedFullHashes(self) -> EncodedFullHashesResource: ...
    def encodedUpdates(self) -> EncodedUpdatesResource: ...
    def fullHashes(self) -> FullHashesResource: ...
    def threatHits(self) -> ThreatHitsResource: ...
    def threatListUpdates(self) -> ThreatListUpdatesResource: ...
    def threatLists(self) -> ThreatListsResource: ...
    def threatMatches(self) -> ThreatMatchesResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

@typing.type_check_only
class FetchThreatListUpdatesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FetchThreatListUpdatesResponse: ...

@typing.type_check_only
class FindFullHashesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FindFullHashesResponse: ...

@typing.type_check_only
class FindThreatMatchesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FindThreatMatchesResponse: ...

@typing.type_check_only
class ListThreatListsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListThreatListsResponse: ...

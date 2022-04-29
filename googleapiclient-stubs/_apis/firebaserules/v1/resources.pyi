import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class FirebaseRulesResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ReleasesResource(googleapiclient.discovery.Resource):
            def create(
                self, *, name: str, body: Release = ..., **kwargs: typing.Any
            ) -> ReleaseHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> ReleaseHttpRequest: ...
            def getExecutable(
                self,
                *,
                name: str,
                executableVersion: typing_extensions.Literal[
                    "RELEASE_EXECUTABLE_VERSION_UNSPECIFIED",
                    "FIREBASE_RULES_EXECUTABLE_V1",
                    "FIREBASE_RULES_EXECUTABLE_V2",
                ] = ...,
                **kwargs: typing.Any
            ) -> GetReleaseExecutableResponseHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListReleasesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListReleasesResponseHttpRequest,
                previous_response: ListReleasesResponse,
            ) -> ListReleasesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: UpdateReleaseRequest = ...,
                **kwargs: typing.Any
            ) -> ReleaseHttpRequest: ...

        @typing.type_check_only
        class RulesetsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, name: str, body: Ruleset = ..., **kwargs: typing.Any
            ) -> RulesetHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> RulesetHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListRulesetsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListRulesetsResponseHttpRequest,
                previous_response: ListRulesetsResponse,
            ) -> ListRulesetsResponseHttpRequest | None: ...

        def test(
            self, *, name: str, body: TestRulesetRequest = ..., **kwargs: typing.Any
        ) -> TestRulesetResponseHttpRequest: ...
        def releases(self) -> ReleasesResource: ...
        def rulesets(self) -> RulesetsResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GetReleaseExecutableResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GetReleaseExecutableResponse: ...

@typing.type_check_only
class ListReleasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListReleasesResponse: ...

@typing.type_check_only
class ListRulesetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListRulesetsResponse: ...

@typing.type_check_only
class ReleaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Release: ...

@typing.type_check_only
class RulesetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Ruleset: ...

@typing.type_check_only
class TestRulesetResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestRulesetResponse: ...

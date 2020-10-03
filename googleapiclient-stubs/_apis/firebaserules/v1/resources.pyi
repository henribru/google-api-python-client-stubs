import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class FirebaseRulesResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class ReleasesResource(googleapiclient.discovery.Resource):
            def patch(
                self,
                *,
                name: str,
                body: UpdateReleaseRequest = ...,
                **kwargs: typing.Any
            ) -> ReleaseHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                pageSize: int = ...,
                filter: str = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListReleasesResponseHttpRequest: ...
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
            def create(
                self, *, name: str, body: Release = ..., **kwargs: typing.Any
            ) -> ReleaseHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
        class RulesetsResource(googleapiclient.discovery.Resource):
            def get(self, *, name: str, **kwargs: typing.Any) -> RulesetHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListRulesetsResponseHttpRequest: ...
            def create(
                self, *, name: str, body: Ruleset = ..., **kwargs: typing.Any
            ) -> RulesetHttpRequest: ...
        def test(
            self, *, name: str, body: TestRulesetRequest = ..., **kwargs: typing.Any
        ) -> TestRulesetResponseHttpRequest: ...
        def releases(self) -> ReleasesResource: ...
        def rulesets(self) -> RulesetsResource: ...
    def projects(self) -> ProjectsResource: ...

class GetReleaseExecutableResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetReleaseExecutableResponse: ...

class ListRulesetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListRulesetsResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class RulesetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Ruleset: ...

class ListReleasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListReleasesResponse: ...

class ReleaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Release: ...

class TestRulesetResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestRulesetResponse: ...

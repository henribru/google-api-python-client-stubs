import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class VerifiedaccessResource(googleapiclient.discovery.Resource):
    class ChallengeResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: Empty = ..., **kwargs: typing.Any
        ) -> ChallengeHttpRequest: ...
        def verify(
            self, *, body: VerifyChallengeResponseRequest = ..., **kwargs: typing.Any
        ) -> VerifyChallengeResponseResultHttpRequest: ...
    def challenge(self) -> ChallengeResource: ...

class ChallengeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Challenge: ...

class VerifyChallengeResponseResultHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VerifyChallengeResponseResult: ...

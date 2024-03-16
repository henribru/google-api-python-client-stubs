import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class VerifiedaccessResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ChallengeResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: Empty = ..., **kwargs: typing.Any
        ) -> ChallengeHttpRequest: ...
        def verify(
            self, *, body: VerifyChallengeResponseRequest = ..., **kwargs: typing.Any
        ) -> VerifyChallengeResponseResultHttpRequest: ...

    def new_batch_http_request(
        self,
        callback: (
            collections.abc.Callable[
                [
                    str,
                    googleapiclient.http.HttpRequest,
                    googleapiclient.errors.HttpError | None,
                ],
                typing.Any,
            ]
            | None
        ) = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def challenge(self) -> ChallengeResource: ...

@typing.type_check_only
class ChallengeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Challenge: ...

@typing.type_check_only
class VerifyChallengeResponseResultHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> VerifyChallengeResponseResult: ...

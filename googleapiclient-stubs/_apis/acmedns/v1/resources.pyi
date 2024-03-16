import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class ACMEDNSResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AcmeChallengeSetsResource(googleapiclient.discovery.Resource):
        def get(
            self, *, rootDomain: str, **kwargs: typing.Any
        ) -> AcmeChallengeSetHttpRequest: ...
        def rotateChallenges(
            self,
            *,
            rootDomain: str,
            body: RotateChallengesRequest = ...,
            **kwargs: typing.Any,
        ) -> AcmeChallengeSetHttpRequest: ...

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
    def acmeChallengeSets(self) -> AcmeChallengeSetsResource: ...

@typing.type_check_only
class AcmeChallengeSetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AcmeChallengeSet: ...

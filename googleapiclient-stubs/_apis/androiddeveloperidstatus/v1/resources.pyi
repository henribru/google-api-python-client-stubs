import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class AndroidDeveloperIDStatusResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class PackagesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class PackageRegistrationStatusResource(googleapiclient.discovery.Resource):
            def check(
                self,
                *,
                name: str,
                certificateFingerprint: str | None = ...,
                **kwargs: typing.Any,
            ) -> PackageRegistrationStatusHttpRequest: ...

        def packageRegistrationStatus(self) -> PackageRegistrationStatusResource: ...

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
    def packages(self) -> PackagesResource: ...

@typing.type_check_only
class PackageRegistrationStatusHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PackageRegistrationStatus: ...

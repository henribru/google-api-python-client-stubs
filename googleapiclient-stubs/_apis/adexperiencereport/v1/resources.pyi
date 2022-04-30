import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class AdExperienceReportResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class SitesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> SiteSummaryResponseHttpRequest: ...

    @typing.type_check_only
    class ViolatingSitesResource(googleapiclient.discovery.Resource):
        def list(self, **kwargs: typing.Any) -> ViolatingSitesResponseHttpRequest: ...

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
    def sites(self) -> SitesResource: ...
    def violatingSites(self) -> ViolatingSitesResource: ...

@typing.type_check_only
class SiteSummaryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SiteSummaryResponse: ...

@typing.type_check_only
class ViolatingSitesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ViolatingSitesResponse: ...

import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
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
    def sites(self) -> SitesResource: ...
    def violatingSites(self) -> ViolatingSitesResource: ...

@typing.type_check_only
class SiteSummaryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SiteSummaryResponse: ...

@typing.type_check_only
class ViolatingSitesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ViolatingSitesResponse: ...

import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class AdExperienceReportResource(googleapiclient.discovery.Resource):
    class SitesResource(googleapiclient.discovery.Resource):
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> SiteSummaryResponseHttpRequest: ...
    class ViolatingSitesResource(googleapiclient.discovery.Resource):
        def list(self, **kwargs: typing.Any) -> ViolatingSitesResponseHttpRequest: ...
    def sites(self) -> SitesResource: ...
    def violatingSites(self) -> ViolatingSitesResource: ...

class SiteSummaryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SiteSummaryResponse: ...

class ViolatingSitesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ViolatingSitesResponse: ...

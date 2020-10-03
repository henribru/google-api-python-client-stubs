import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class ServiceControlResource(googleapiclient.discovery.Resource):
    class ServicesResource(googleapiclient.discovery.Resource):
        def check(
            self, *, serviceName: str, body: CheckRequest = ..., **kwargs: typing.Any
        ) -> CheckResponseHttpRequest: ...
        def report(
            self, *, serviceName: str, body: ReportRequest = ..., **kwargs: typing.Any
        ) -> ReportResponseHttpRequest: ...
        def allocateQuota(
            self,
            *,
            serviceName: str,
            body: AllocateQuotaRequest = ...,
            **kwargs: typing.Any
        ) -> AllocateQuotaResponseHttpRequest: ...
    def services(self) -> ServicesResource: ...

class CheckResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CheckResponse: ...

class ReportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReportResponse: ...

class AllocateQuotaResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AllocateQuotaResponse: ...

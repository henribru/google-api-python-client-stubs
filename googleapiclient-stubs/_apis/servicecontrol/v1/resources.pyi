import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class ServiceControlResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ServicesResource(googleapiclient.discovery.Resource):
        def allocateQuota(
            self,
            *,
            serviceName: str,
            body: AllocateQuotaRequest = ...,
            **kwargs: typing.Any
        ) -> AllocateQuotaResponseHttpRequest: ...
        def check(
            self, *, serviceName: str, body: CheckRequest = ..., **kwargs: typing.Any
        ) -> CheckResponseHttpRequest: ...
        def report(
            self, *, serviceName: str, body: ReportRequest = ..., **kwargs: typing.Any
        ) -> ReportResponseHttpRequest: ...
    def services(self) -> ServicesResource: ...

@typing.type_check_only
class AllocateQuotaResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> AllocateQuotaResponse: ...

@typing.type_check_only
class CheckResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CheckResponse: ...

@typing.type_check_only
class ReportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ReportResponse: ...

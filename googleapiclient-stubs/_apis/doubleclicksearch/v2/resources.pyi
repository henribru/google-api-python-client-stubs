import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class DoubleclicksearchResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ConversionResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            agencyId: str,
            advertiserId: str,
            engineAccountId: str,
            endDate: int,
            rowCount: int,
            startDate: int,
            startRow: int,
            adGroupId: str = ...,
            adId: str = ...,
            campaignId: str = ...,
            criterionId: str = ...,
            customerId: str = ...,
            **kwargs: typing.Any
        ) -> ConversionListHttpRequest: ...
        def getByCustomerId(
            self,
            *,
            customerId: str,
            endDate: int,
            rowCount: int,
            startDate: int,
            startRow: int,
            adGroupId: str = ...,
            adId: str = ...,
            advertiserId: str = ...,
            agencyId: str = ...,
            campaignId: str = ...,
            criterionId: str = ...,
            engineAccountId: str = ...,
            **kwargs: typing.Any
        ) -> ConversionListHttpRequest: ...
        def insert(
            self, *, body: ConversionList = ..., **kwargs: typing.Any
        ) -> ConversionListHttpRequest: ...
        def update(
            self, *, body: ConversionList = ..., **kwargs: typing.Any
        ) -> ConversionListHttpRequest: ...
        def updateAvailability(
            self, *, body: UpdateAvailabilityRequest = ..., **kwargs: typing.Any
        ) -> UpdateAvailabilityResponseHttpRequest: ...

    @typing.type_check_only
    class ReportsResource(googleapiclient.discovery.Resource):
        def generate(
            self, *, body: ReportRequest = ..., **kwargs: typing.Any
        ) -> ReportHttpRequest: ...
        def get(self, *, reportId: str, **kwargs: typing.Any) -> ReportHttpRequest: ...
        def getFile(
            self, *, reportId: str, reportFragment: int, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def getFile_media(
            self, *, reportId: str, reportFragment: int, **kwargs: typing.Any
        ) -> BytesHttpRequest: ...
        def getIdMappingFile(
            self, *, agencyId: str, advertiserId: str, **kwargs: typing.Any
        ) -> IdMappingFileHttpRequest: ...
        def getIdMappingFile_media(
            self, *, agencyId: str, advertiserId: str, **kwargs: typing.Any
        ) -> BytesHttpRequest: ...
        def request(
            self, *, body: ReportRequest = ..., **kwargs: typing.Any
        ) -> ReportHttpRequest: ...

    @typing.type_check_only
    class SavedColumnsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, agencyId: str, advertiserId: str, **kwargs: typing.Any
        ) -> SavedColumnListHttpRequest: ...

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
    def conversion(self) -> ConversionResource: ...
    def reports(self) -> ReportsResource: ...
    def savedColumns(self) -> SavedColumnsResource: ...

@typing.type_check_only
class ConversionListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ConversionList: ...

@typing.type_check_only
class IdMappingFileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> IdMappingFile: ...

@typing.type_check_only
class ReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Report: ...

@typing.type_check_only
class SavedColumnListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SavedColumnList: ...

@typing.type_check_only
class UpdateAvailabilityResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UpdateAvailabilityResponse: ...

@typing.type_check_only
class BytesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> bytes: ...

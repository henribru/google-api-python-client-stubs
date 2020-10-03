import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DoubleclicksearchResource(googleapiclient.discovery.Resource):
    class ReportsResource(googleapiclient.discovery.Resource):
        def request(
            self, *, body: ReportRequest = ..., **kwargs: typing.Any
        ) -> ReportHttpRequest: ...
        def getFile(
            self, *, reportId: str, reportFragment: int, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(self, *, reportId: str, **kwargs: typing.Any) -> ReportHttpRequest: ...
        def generate(
            self, *, body: ReportRequest = ..., **kwargs: typing.Any
        ) -> ReportHttpRequest: ...
    class SavedColumnsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, agencyId: str, advertiserId: str, **kwargs: typing.Any
        ) -> SavedColumnListHttpRequest: ...
    class ConversionResource(googleapiclient.discovery.Resource):
        def insert(
            self, *, body: ConversionList = ..., **kwargs: typing.Any
        ) -> ConversionListHttpRequest: ...
        def updateAvailability(
            self, *, body: UpdateAvailabilityRequest = ..., **kwargs: typing.Any
        ) -> UpdateAvailabilityResponseHttpRequest: ...
        def update(
            self, *, body: ConversionList = ..., **kwargs: typing.Any
        ) -> ConversionListHttpRequest: ...
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
            campaignId: str = ...,
            criterionId: str = ...,
            adId: str = ...,
            adGroupId: str = ...,
            **kwargs: typing.Any
        ) -> ConversionListHttpRequest: ...
    def reports(self) -> ReportsResource: ...
    def savedColumns(self) -> SavedColumnsResource: ...
    def conversion(self) -> ConversionResource: ...

class ConversionListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ConversionList: ...

class ReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Report: ...

class SavedColumnListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SavedColumnList: ...

class UpdateAvailabilityResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UpdateAvailabilityResponse: ...

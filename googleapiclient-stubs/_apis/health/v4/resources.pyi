import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class GoogleHealthAPIResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class UsersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DataTypesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DataPointsResource(googleapiclient.discovery.Resource):
                def batchDelete(
                    self,
                    *,
                    parent: str,
                    body: BatchDeleteDataPointsRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def create(
                    self, *, parent: str, body: DataPoint = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def dailyRollUp(
                    self,
                    *,
                    parent: str,
                    body: DailyRollUpDataPointsRequest = ...,
                    **kwargs: typing.Any,
                ) -> DailyRollUpDataPointsResponseHttpRequest: ...
                def exportExerciseTcx(
                    self, *, name: str, partialData: bool = ..., **kwargs: typing.Any
                ) -> ExportExerciseTcxResponseHttpRequest: ...
                def exportExerciseTcx_media(
                    self, *, name: str, partialData: bool = ..., **kwargs: typing.Any
                ) -> BytesHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListDataPointsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDataPointsResponseHttpRequest,
                    previous_response: ListDataPointsResponse,
                ) -> ListDataPointsResponseHttpRequest | None: ...
                def patch(
                    self, *, name: str, body: DataPoint = ..., **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def reconcile(
                    self,
                    *,
                    parent: str,
                    dataSourceFamily: str = ...,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ReconcileDataPointsResponseHttpRequest: ...
                def reconcile_next(
                    self,
                    previous_request: ReconcileDataPointsResponseHttpRequest,
                    previous_response: ReconcileDataPointsResponse,
                ) -> ReconcileDataPointsResponseHttpRequest | None: ...
                def rollUp(
                    self,
                    *,
                    parent: str,
                    body: RollUpDataPointsRequest = ...,
                    **kwargs: typing.Any,
                ) -> RollUpDataPointsResponseHttpRequest: ...
                def rollUp_next(
                    self,
                    previous_request: RollUpDataPointsResponseHttpRequest,
                    previous_response: RollUpDataPointsResponse,
                ) -> RollUpDataPointsResponseHttpRequest | None: ...

            def dataPoints(self) -> DataPointsResource: ...

        def getIdentity(
            self, *, name: str, **kwargs: typing.Any
        ) -> IdentityHttpRequest: ...
        def getProfile(
            self, *, name: str, **kwargs: typing.Any
        ) -> ProfileHttpRequest: ...
        def getSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> SettingsHttpRequest: ...
        def updateProfile(
            self,
            *,
            name: str,
            body: Profile = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> ProfileHttpRequest: ...
        def updateSettings(
            self,
            *,
            name: str,
            body: Settings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> SettingsHttpRequest: ...
        def dataTypes(self) -> DataTypesResource: ...

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
    def users(self) -> UsersResource: ...

@typing.type_check_only
class DailyRollUpDataPointsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DailyRollUpDataPointsResponse: ...

@typing.type_check_only
class ExportExerciseTcxResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ExportExerciseTcxResponse: ...

@typing.type_check_only
class IdentityHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Identity: ...

@typing.type_check_only
class ListDataPointsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDataPointsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class ProfileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Profile: ...

@typing.type_check_only
class ReconcileDataPointsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ReconcileDataPointsResponse: ...

@typing.type_check_only
class RollUpDataPointsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RollUpDataPointsResponse: ...

@typing.type_check_only
class SettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Settings: ...

@typing.type_check_only
class BytesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> bytes: ...

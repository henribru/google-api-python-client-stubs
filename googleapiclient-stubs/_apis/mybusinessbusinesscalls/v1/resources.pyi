import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class MyBusinessBusinessCallsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class LocationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class BusinesscallsinsightsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListBusinessCallsInsightsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListBusinessCallsInsightsResponseHttpRequest,
                previous_response: ListBusinessCallsInsightsResponse,
            ) -> ListBusinessCallsInsightsResponseHttpRequest | None: ...

        def getBusinesscallssettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> BusinessCallsSettingsHttpRequest: ...
        def updateBusinesscallssettings(
            self,
            *,
            name: str,
            body: BusinessCallsSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> BusinessCallsSettingsHttpRequest: ...
        def businesscallsinsights(self) -> BusinesscallsinsightsResource: ...

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
    def locations(self) -> LocationsResource: ...

@typing.type_check_only
class BusinessCallsSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BusinessCallsSettings: ...

@typing.type_check_only
class ListBusinessCallsInsightsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListBusinessCallsInsightsResponse: ...

import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class AlertCenterResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AlertsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class FeedbackResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                alertId: str,
                body: AlertFeedback = ...,
                customerId: str = ...,
                **kwargs: typing.Any
            ) -> AlertFeedbackHttpRequest: ...
            def list(
                self,
                *,
                alertId: str,
                customerId: str = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> ListAlertFeedbackResponseHttpRequest: ...

        def batchDelete(
            self, *, body: BatchDeleteAlertsRequest = ..., **kwargs: typing.Any
        ) -> BatchDeleteAlertsResponseHttpRequest: ...
        def batchUndelete(
            self, *, body: BatchUndeleteAlertsRequest = ..., **kwargs: typing.Any
        ) -> BatchUndeleteAlertsResponseHttpRequest: ...
        def delete(
            self, *, alertId: str, customerId: str = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(
            self, *, alertId: str, customerId: str = ..., **kwargs: typing.Any
        ) -> AlertHttpRequest: ...
        def getMetadata(
            self, *, alertId: str, customerId: str = ..., **kwargs: typing.Any
        ) -> AlertMetadataHttpRequest: ...
        def list(
            self,
            *,
            customerId: str = ...,
            filter: str = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListAlertsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListAlertsResponseHttpRequest,
            previous_response: ListAlertsResponse,
        ) -> ListAlertsResponseHttpRequest | None: ...
        def undelete(
            self,
            *,
            alertId: str,
            body: UndeleteAlertRequest = ...,
            **kwargs: typing.Any
        ) -> AlertHttpRequest: ...
        def feedback(self) -> FeedbackResource: ...

    @typing.type_check_only
    class V1beta1Resource(googleapiclient.discovery.Resource):
        def getSettings(
            self, *, customerId: str = ..., **kwargs: typing.Any
        ) -> SettingsHttpRequest: ...
        def updateSettings(
            self, *, body: Settings = ..., customerId: str = ..., **kwargs: typing.Any
        ) -> SettingsHttpRequest: ...

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
    def alerts(self) -> AlertsResource: ...
    def v1beta1(self) -> V1beta1Resource: ...

@typing.type_check_only
class AlertHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Alert: ...

@typing.type_check_only
class AlertFeedbackHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AlertFeedback: ...

@typing.type_check_only
class AlertMetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AlertMetadata: ...

@typing.type_check_only
class BatchDeleteAlertsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchDeleteAlertsResponse: ...

@typing.type_check_only
class BatchUndeleteAlertsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchUndeleteAlertsResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListAlertFeedbackResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAlertFeedbackResponse: ...

@typing.type_check_only
class ListAlertsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAlertsResponse: ...

@typing.type_check_only
class SettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Settings: ...

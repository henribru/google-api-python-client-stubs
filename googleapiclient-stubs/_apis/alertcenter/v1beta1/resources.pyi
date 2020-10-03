import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class AlertCenterResource(googleapiclient.discovery.Resource):
    class AlertsResource(googleapiclient.discovery.Resource):
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
        def batchUndelete(
            self, *, body: BatchUndeleteAlertsRequest = ..., **kwargs: typing.Any
        ) -> BatchUndeleteAlertsResponseHttpRequest: ...
        def get(
            self, *, alertId: str, customerId: str = ..., **kwargs: typing.Any
        ) -> AlertHttpRequest: ...
        def undelete(
            self,
            *,
            alertId: str,
            body: UndeleteAlertRequest = ...,
            **kwargs: typing.Any
        ) -> AlertHttpRequest: ...
        def delete(
            self, *, alertId: str, customerId: str = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def getMetadata(
            self, *, alertId: str, customerId: str = ..., **kwargs: typing.Any
        ) -> AlertMetadataHttpRequest: ...
        def batchDelete(
            self, *, body: BatchDeleteAlertsRequest = ..., **kwargs: typing.Any
        ) -> BatchDeleteAlertsResponseHttpRequest: ...
        def list(
            self,
            *,
            orderBy: str = ...,
            pageToken: str = ...,
            pageSize: int = ...,
            filter: str = ...,
            customerId: str = ...,
            **kwargs: typing.Any
        ) -> ListAlertsResponseHttpRequest: ...
        def feedback(self) -> FeedbackResource: ...
    class V1beta1Resource(googleapiclient.discovery.Resource):
        def updateSettings(
            self, *, body: Settings = ..., customerId: str = ..., **kwargs: typing.Any
        ) -> SettingsHttpRequest: ...
        def getSettings(
            self, *, customerId: str = ..., **kwargs: typing.Any
        ) -> SettingsHttpRequest: ...
    def alerts(self) -> AlertsResource: ...
    def v1beta1(self) -> V1beta1Resource: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class BatchUndeleteAlertsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchUndeleteAlertsResponse: ...

class AlertHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Alert: ...

class BatchDeleteAlertsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchDeleteAlertsResponse: ...

class AlertMetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AlertMetadata: ...

class SettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Settings: ...

class ListAlertFeedbackResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAlertFeedbackResponse: ...

class ListAlertsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAlertsResponse: ...

class AlertFeedbackHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AlertFeedback: ...

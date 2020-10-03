import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class ServiceConsumerManagementResource(googleapiclient.discovery.Resource):
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
    class ServicesResource(googleapiclient.discovery.Resource):
        class ConsumerQuotaMetricsResource(googleapiclient.discovery.Resource):
            class LimitsResource(googleapiclient.discovery.Resource):
                class ProducerOverridesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: V1Beta1QuotaOverride = ...,
                        force: bool = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> V1Beta1ListProducerOverridesResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: V1Beta1QuotaOverride = ...,
                        force: bool = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    view: typing_extensions.Literal[
                        "QUOTA_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any
                ) -> V1Beta1ConsumerQuotaLimitHttpRequest: ...
                def producerOverrides(self) -> ProducerOverridesResource: ...
            def get(
                self,
                *,
                name: str,
                view: typing_extensions.Literal[
                    "QUOTA_VIEW_UNSPECIFIED", "BASIC", "FULL"
                ] = ...,
                **kwargs: typing.Any
            ) -> V1Beta1ConsumerQuotaMetricHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                view: typing_extensions.Literal[
                    "QUOTA_VIEW_UNSPECIFIED", "BASIC", "FULL"
                ] = ...,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> V1Beta1ListConsumerQuotaMetricsResponseHttpRequest: ...
            def importProducerOverrides(
                self,
                *,
                parent: str,
                body: V1Beta1ImportProducerOverridesRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def limits(self) -> LimitsResource: ...
        def consumerQuotaMetrics(self) -> ConsumerQuotaMetricsResource: ...
    def operations(self) -> OperationsResource: ...
    def services(self) -> ServicesResource: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class V1Beta1ListConsumerQuotaMetricsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> V1Beta1ListConsumerQuotaMetricsResponse: ...

class V1Beta1ConsumerQuotaMetricHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> V1Beta1ConsumerQuotaMetric: ...

class V1Beta1ConsumerQuotaLimitHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> V1Beta1ConsumerQuotaLimit: ...

class V1Beta1ListProducerOverridesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> V1Beta1ListProducerOverridesResponse: ...

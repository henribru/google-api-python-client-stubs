import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ServiceConsumerManagementResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...

    @typing.type_check_only
    class ServicesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ConsumerQuotaMetricsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class LimitsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ProducerOverridesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: V1Beta1QuotaOverride = ...,
                        force: bool = ...,
                        forceOnly: typing_extensions.Literal[
                            "QUOTA_SAFETY_CHECK_UNSPECIFIED",
                            "LIMIT_DECREASE_BELOW_USAGE",
                            "LIMIT_DECREASE_PERCENTAGE_TOO_HIGH",
                        ]
                        | _list[
                            typing_extensions.Literal[
                                "QUOTA_SAFETY_CHECK_UNSPECIFIED",
                                "LIMIT_DECREASE_BELOW_USAGE",
                                "LIMIT_DECREASE_PERCENTAGE_TOO_HIGH",
                            ]
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        force: bool = ...,
                        forceOnly: typing_extensions.Literal[
                            "QUOTA_SAFETY_CHECK_UNSPECIFIED",
                            "LIMIT_DECREASE_BELOW_USAGE",
                            "LIMIT_DECREASE_PERCENTAGE_TOO_HIGH",
                        ]
                        | _list[
                            typing_extensions.Literal[
                                "QUOTA_SAFETY_CHECK_UNSPECIFIED",
                                "LIMIT_DECREASE_BELOW_USAGE",
                                "LIMIT_DECREASE_PERCENTAGE_TOO_HIGH",
                            ]
                        ] = ...,
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
                    def list_next(
                        self,
                        previous_request: V1Beta1ListProducerOverridesResponseHttpRequest,
                        previous_response: V1Beta1ListProducerOverridesResponse,
                    ) -> V1Beta1ListProducerOverridesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: V1Beta1QuotaOverride = ...,
                        force: bool = ...,
                        forceOnly: typing_extensions.Literal[
                            "QUOTA_SAFETY_CHECK_UNSPECIFIED",
                            "LIMIT_DECREASE_BELOW_USAGE",
                            "LIMIT_DECREASE_PERCENTAGE_TOO_HIGH",
                        ]
                        | _list[
                            typing_extensions.Literal[
                                "QUOTA_SAFETY_CHECK_UNSPECIFIED",
                                "LIMIT_DECREASE_BELOW_USAGE",
                                "LIMIT_DECREASE_PERCENTAGE_TOO_HIGH",
                            ]
                        ] = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
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
            def importProducerOverrides(
                self,
                *,
                parent: str,
                body: V1Beta1ImportProducerOverridesRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                view: typing_extensions.Literal[
                    "QUOTA_VIEW_UNSPECIFIED", "BASIC", "FULL"
                ] = ...,
                **kwargs: typing.Any
            ) -> V1Beta1ListConsumerQuotaMetricsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: V1Beta1ListConsumerQuotaMetricsResponseHttpRequest,
                previous_response: V1Beta1ListConsumerQuotaMetricsResponse,
            ) -> V1Beta1ListConsumerQuotaMetricsResponseHttpRequest | None: ...
            def limits(self) -> LimitsResource: ...

        def consumerQuotaMetrics(self) -> ConsumerQuotaMetricsResource: ...

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
    def operations(self) -> OperationsResource: ...
    def services(self) -> ServicesResource: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class V1Beta1ConsumerQuotaLimitHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> V1Beta1ConsumerQuotaLimit: ...

@typing.type_check_only
class V1Beta1ConsumerQuotaMetricHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> V1Beta1ConsumerQuotaMetric: ...

@typing.type_check_only
class V1Beta1ListConsumerQuotaMetricsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> V1Beta1ListConsumerQuotaMetricsResponse: ...

@typing.type_check_only
class V1Beta1ListProducerOverridesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> V1Beta1ListProducerOverridesResponse: ...

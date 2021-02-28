import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
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
                        forceOnly: typing.Union[
                            typing_extensions.Literal[
                                "QUOTA_SAFETY_CHECK_UNSPECIFIED",
                                "LIMIT_DECREASE_BELOW_USAGE",
                                "LIMIT_DECREASE_PERCENTAGE_TOO_HIGH",
                            ],
                            typing.List[
                                typing_extensions.Literal[
                                    "QUOTA_SAFETY_CHECK_UNSPECIFIED",
                                    "LIMIT_DECREASE_BELOW_USAGE",
                                    "LIMIT_DECREASE_PERCENTAGE_TOO_HIGH",
                                ]
                            ],
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self,
                        *,
                        name: str,
                        force: bool = ...,
                        forceOnly: typing.Union[
                            typing_extensions.Literal[
                                "QUOTA_SAFETY_CHECK_UNSPECIFIED",
                                "LIMIT_DECREASE_BELOW_USAGE",
                                "LIMIT_DECREASE_PERCENTAGE_TOO_HIGH",
                            ],
                            typing.List[
                                typing_extensions.Literal[
                                    "QUOTA_SAFETY_CHECK_UNSPECIFIED",
                                    "LIMIT_DECREASE_BELOW_USAGE",
                                    "LIMIT_DECREASE_PERCENTAGE_TOO_HIGH",
                                ]
                            ],
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
                    def patch(
                        self,
                        *,
                        name: str,
                        body: V1Beta1QuotaOverride = ...,
                        force: bool = ...,
                        forceOnly: typing.Union[
                            typing_extensions.Literal[
                                "QUOTA_SAFETY_CHECK_UNSPECIFIED",
                                "LIMIT_DECREASE_BELOW_USAGE",
                                "LIMIT_DECREASE_PERCENTAGE_TOO_HIGH",
                            ],
                            typing.List[
                                typing_extensions.Literal[
                                    "QUOTA_SAFETY_CHECK_UNSPECIFIED",
                                    "LIMIT_DECREASE_BELOW_USAGE",
                                    "LIMIT_DECREASE_PERCENTAGE_TOO_HIGH",
                                ]
                            ],
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
            def limits(self) -> LimitsResource: ...
        def consumerQuotaMetrics(self) -> ConsumerQuotaMetricsResource: ...
    def operations(self) -> OperationsResource: ...
    def services(self) -> ServicesResource: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class V1Beta1ConsumerQuotaLimitHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> V1Beta1ConsumerQuotaLimit: ...

@typing.type_check_only
class V1Beta1ConsumerQuotaMetricHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> V1Beta1ConsumerQuotaMetric: ...

@typing.type_check_only
class V1Beta1ListConsumerQuotaMetricsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> V1Beta1ListConsumerQuotaMetricsResponse: ...

@typing.type_check_only
class V1Beta1ListProducerOverridesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> V1Beta1ListProducerOverridesResponse: ...

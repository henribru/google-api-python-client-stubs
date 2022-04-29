import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ServiceUsageResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            filter: str = ...,
            name: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListOperationsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListOperationsResponseHttpRequest,
            previous_response: ListOperationsResponse,
        ) -> ListOperationsResponseHttpRequest | None: ...

    @typing.type_check_only
    class ServicesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ConsumerQuotaMetricsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class LimitsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AdminOverridesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: QuotaOverride = ...,
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
                    ) -> ListAdminOverridesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListAdminOverridesResponseHttpRequest,
                        previous_response: ListAdminOverridesResponse,
                    ) -> ListAdminOverridesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: QuotaOverride = ...,
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

                @typing.type_check_only
                class ConsumerOverridesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: QuotaOverride = ...,
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
                    ) -> ListConsumerOverridesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListConsumerOverridesResponseHttpRequest,
                        previous_response: ListConsumerOverridesResponse,
                    ) -> ListConsumerOverridesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: QuotaOverride = ...,
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
                ) -> ConsumerQuotaLimitHttpRequest: ...
                def adminOverrides(self) -> AdminOverridesResource: ...
                def consumerOverrides(self) -> ConsumerOverridesResource: ...

            def get(
                self,
                *,
                name: str,
                view: typing_extensions.Literal[
                    "QUOTA_VIEW_UNSPECIFIED", "BASIC", "FULL"
                ] = ...,
                **kwargs: typing.Any
            ) -> ConsumerQuotaMetricHttpRequest: ...
            def importAdminOverrides(
                self,
                *,
                parent: str,
                body: ImportAdminOverridesRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def importConsumerOverrides(
                self,
                *,
                parent: str,
                body: ImportConsumerOverridesRequest = ...,
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
            ) -> ListConsumerQuotaMetricsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListConsumerQuotaMetricsResponseHttpRequest,
                previous_response: ListConsumerQuotaMetricsResponse,
            ) -> ListConsumerQuotaMetricsResponseHttpRequest | None: ...
            def limits(self) -> LimitsResource: ...

        def batchEnable(
            self,
            *,
            parent: str,
            body: BatchEnableServicesRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def disable(
            self, *, name: str, body: DisableServiceRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def enable(
            self, *, name: str, body: EnableServiceRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def generateServiceIdentity(
            self, *, parent: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> ServiceHttpRequest: ...
        def list(
            self,
            *,
            parent: str,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListServicesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListServicesResponseHttpRequest,
            previous_response: ListServicesResponse,
        ) -> ListServicesResponseHttpRequest | None: ...
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
class ConsumerQuotaLimitHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ConsumerQuotaLimit: ...

@typing.type_check_only
class ConsumerQuotaMetricHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ConsumerQuotaMetric: ...

@typing.type_check_only
class ListAdminOverridesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAdminOverridesResponse: ...

@typing.type_check_only
class ListConsumerOverridesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListConsumerOverridesResponse: ...

@typing.type_check_only
class ListConsumerQuotaMetricsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListConsumerQuotaMetricsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListServicesResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class ServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Service: ...

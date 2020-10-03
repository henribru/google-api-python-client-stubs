import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class ServiceUsageResource(googleapiclient.discovery.Resource):
    class ServicesResource(googleapiclient.discovery.Resource):
        class ConsumerQuotaMetricsResource(googleapiclient.discovery.Resource):
            class LimitsResource(googleapiclient.discovery.Resource):
                class ConsumerOverridesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: QuotaOverride = ...,
                        force: bool = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: QuotaOverride = ...,
                        updateMask: str = ...,
                        force: bool = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> ListConsumerOverridesResponseHttpRequest: ...
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                class AdminOverridesResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, name: str, force: bool = ..., **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: QuotaOverride = ...,
                        updateMask: str = ...,
                        force: bool = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: QuotaOverride = ...,
                        force: bool = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> ListAdminOverridesResponseHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    view: typing_extensions.Literal[
                        "QUOTA_VIEW_UNSPECIFIED", "BASIC", "FULL"
                    ] = ...,
                    **kwargs: typing.Any
                ) -> ConsumerQuotaLimitHttpRequest: ...
                def consumerOverrides(self) -> ConsumerOverridesResource: ...
                def adminOverrides(self) -> AdminOverridesResource: ...
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
                view: typing_extensions.Literal[
                    "QUOTA_VIEW_UNSPECIFIED", "BASIC", "FULL"
                ] = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListConsumerQuotaMetricsResponseHttpRequest: ...
            def get(
                self,
                *,
                name: str,
                view: typing_extensions.Literal[
                    "QUOTA_VIEW_UNSPECIFIED", "BASIC", "FULL"
                ] = ...,
                **kwargs: typing.Any
            ) -> ConsumerQuotaMetricHttpRequest: ...
            def limits(self) -> LimitsResource: ...
        def generateServiceIdentity(
            self, *, parent: str, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def batchEnable(
            self,
            *,
            parent: str,
            body: BatchEnableServicesRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def enable(
            self, *, name: str, body: EnableServiceRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            parent: str,
            filter: str = ...,
            pageToken: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListServicesResponseHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> ServiceHttpRequest: ...
        def disable(
            self, *, name: str, body: DisableServiceRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def consumerQuotaMetrics(self) -> ConsumerQuotaMetricsResource: ...
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            name: str = ...,
            filter: str = ...,
            pageToken: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListOperationsResponseHttpRequest: ...
    def services(self) -> ServicesResource: ...
    def operations(self) -> OperationsResource: ...

class ListServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListServicesResponse: ...

class ConsumerQuotaMetricHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ConsumerQuotaMetric: ...

class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOperationsResponse: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class ListConsumerOverridesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListConsumerOverridesResponse: ...

class ServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Service: ...

class ConsumerQuotaLimitHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ConsumerQuotaLimit: ...

class ListConsumerQuotaMetricsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListConsumerQuotaMetricsResponse: ...

class ListAdminOverridesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAdminOverridesResponse: ...

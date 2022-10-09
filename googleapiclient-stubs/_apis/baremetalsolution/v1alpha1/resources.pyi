import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class BaremetalsolutionResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            def submitProvisioningConfig(
                self,
                *,
                project: str,
                location: str,
                body: SubmitProvisioningConfigRequest = ...,
                **kwargs: typing.Any
            ) -> ProvisioningConfigHttpRequest: ...

        @typing.type_check_only
        class ProvisioningQuotasResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListProvisioningQuotasResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListProvisioningQuotasResponseHttpRequest,
                previous_response: ListProvisioningQuotasResponse,
            ) -> ListProvisioningQuotasResponseHttpRequest | None: ...

        def locations(self) -> LocationsResource: ...
        def provisioningQuotas(self) -> ProvisioningQuotasResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class ListProvisioningQuotasResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListProvisioningQuotasResponse: ...

@typing.type_check_only
class ProvisioningConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ProvisioningConfig: ...

import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudControlsPartnerServiceResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CustomersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class WorkloadsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class AccessApprovalRequestsResource(
                        googleapiclient.discovery.Resource
                    ):
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> ListAccessApprovalRequestsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListAccessApprovalRequestsResponseHttpRequest,
                            previous_response: ListAccessApprovalRequestsResponse,
                        ) -> ListAccessApprovalRequestsResponseHttpRequest | None: ...

                    @typing.type_check_only
                    class ViolationsResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> ViolationHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            interval_endTime: str = ...,
                            interval_startTime: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> ListViolationsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListViolationsResponseHttpRequest,
                            previous_response: ListViolationsResponse,
                        ) -> ListViolationsResponseHttpRequest | None: ...

                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> WorkloadHttpRequest: ...
                    def getEkmConnections(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EkmConnectionsHttpRequest: ...
                    def getPartnerPermissions(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> PartnerPermissionsHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListWorkloadsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListWorkloadsResponseHttpRequest,
                        previous_response: ListWorkloadsResponse,
                    ) -> ListWorkloadsResponseHttpRequest | None: ...
                    def accessApprovalRequests(
                        self,
                    ) -> AccessApprovalRequestsResource: ...
                    def violations(self) -> ViolationsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Customer = ...,
                    customerId: str = ...,
                    **kwargs: typing.Any,
                ) -> CustomerHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CustomerHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListCustomersResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListCustomersResponseHttpRequest,
                    previous_response: ListCustomersResponse,
                ) -> ListCustomersResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Customer = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> CustomerHttpRequest: ...
                def workloads(self) -> WorkloadsResource: ...

            def getPartner(
                self, *, name: str, **kwargs: typing.Any
            ) -> PartnerHttpRequest: ...
            def customers(self) -> CustomersResource: ...

        def locations(self) -> LocationsResource: ...

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
    def organizations(self) -> OrganizationsResource: ...

@typing.type_check_only
class CustomerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Customer: ...

@typing.type_check_only
class EkmConnectionsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> EkmConnections: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class ListAccessApprovalRequestsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAccessApprovalRequestsResponse: ...

@typing.type_check_only
class ListCustomersResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCustomersResponse: ...

@typing.type_check_only
class ListViolationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListViolationsResponse: ...

@typing.type_check_only
class ListWorkloadsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListWorkloadsResponse: ...

@typing.type_check_only
class PartnerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Partner: ...

@typing.type_check_only
class PartnerPermissionsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PartnerPermissions: ...

@typing.type_check_only
class ViolationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Violation: ...

@typing.type_check_only
class WorkloadHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Workload: ...

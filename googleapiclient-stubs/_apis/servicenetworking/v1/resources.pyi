import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ServiceNetworkingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def cancel(
            self, *, name: str, body: CancelOperationRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            name: str,
            filter: str = ...,
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
        class ConnectionsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: Connection = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def deleteConnection(
                self,
                *,
                name: str,
                body: DeleteConnectionRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self, *, parent: str, network: str = ..., **kwargs: typing.Any
            ) -> ListConnectionsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Connection = ...,
                force: bool = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        @typing.type_check_only
        class DnsRecordSetsResource(googleapiclient.discovery.Resource):
            def add(
                self,
                *,
                parent: str,
                body: AddDnsRecordSetRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def remove(
                self,
                *,
                parent: str,
                body: RemoveDnsRecordSetRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def update(
                self,
                *,
                parent: str,
                body: UpdateDnsRecordSetRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        @typing.type_check_only
        class DnsZonesResource(googleapiclient.discovery.Resource):
            def add(
                self,
                *,
                parent: str,
                body: AddDnsZoneRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def remove(
                self,
                *,
                parent: str,
                body: RemoveDnsZoneRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        @typing.type_check_only
        class ProjectsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class GlobalResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class NetworksResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class PeeredDnsDomainsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: PeeredDnsDomain = ...,
                            **kwargs: typing.Any
                        ) -> OperationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> OperationHttpRequest: ...
                        def list(
                            self, *, parent: str, **kwargs: typing.Any
                        ) -> ListPeeredDnsDomainsResponseHttpRequest: ...

                    def get(
                        self,
                        *,
                        name: str,
                        includeUsedIpRanges: bool = ...,
                        **kwargs: typing.Any
                    ) -> ConsumerConfigHttpRequest: ...
                    def updateConsumerConfig(
                        self,
                        *,
                        parent: str,
                        body: UpdateConsumerConfigRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def peeredDnsDomains(self) -> PeeredDnsDomainsResource: ...

                def networks(self) -> NetworksResource: ...

            def global_(self) -> GlobalResource: ...

        @typing.type_check_only
        class RolesResource(googleapiclient.discovery.Resource):
            def add(
                self, *, parent: str, body: AddRolesRequest = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        def addSubnetwork(
            self, *, parent: str, body: AddSubnetworkRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def disableVpcServiceControls(
            self,
            *,
            parent: str,
            body: DisableVpcServiceControlsRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def enableVpcServiceControls(
            self,
            *,
            parent: str,
            body: EnableVpcServiceControlsRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def searchRange(
            self, *, parent: str, body: SearchRangeRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def validate(
            self,
            *,
            parent: str,
            body: ValidateConsumerConfigRequest = ...,
            **kwargs: typing.Any
        ) -> ValidateConsumerConfigResponseHttpRequest: ...
        def connections(self) -> ConnectionsResource: ...
        def dnsRecordSets(self) -> DnsRecordSetsResource: ...
        def dnsZones(self) -> DnsZonesResource: ...
        def projects(self) -> ProjectsResource: ...
        def roles(self) -> RolesResource: ...

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
class ConsumerConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ConsumerConfig: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListConnectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListConnectionsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListPeeredDnsDomainsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListPeeredDnsDomainsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class ValidateConsumerConfigResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ValidateConsumerConfigResponse: ...

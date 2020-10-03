import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class ServiceNetworkingResource(googleapiclient.discovery.Resource):
    class ServicesResource(googleapiclient.discovery.Resource):
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
        class ConnectionsResource(googleapiclient.discovery.Resource):
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
            def create(
                self, *, parent: str, body: Connection = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        class ProjectsResource(googleapiclient.discovery.Resource):
            class GlobalResource(googleapiclient.discovery.Resource):
                class NetworksResource(googleapiclient.discovery.Resource):
                    class PeeredDnsDomainsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: PeeredDnsDomain = ...,
                            **kwargs: typing.Any
                        ) -> OperationHttpRequest: ...
                        def list(
                            self, *, parent: str, **kwargs: typing.Any
                        ) -> ListPeeredDnsDomainsResponseHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> OperationHttpRequest: ...
                    def peeredDnsDomains(self) -> PeeredDnsDomainsResource: ...
                def networks(self) -> NetworksResource: ...
            def global_(self) -> GlobalResource: ...
        class RolesResource(googleapiclient.discovery.Resource):
            def add(
                self, *, parent: str, body: AddRolesRequest = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        class DnsZonesResource(googleapiclient.discovery.Resource):
            def remove(
                self,
                *,
                parent: str,
                body: RemoveDnsZoneRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def add(
                self,
                *,
                parent: str,
                body: AddDnsZoneRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        def searchRange(
            self, *, parent: str, body: SearchRangeRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def addSubnetwork(
            self, *, parent: str, body: AddSubnetworkRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def enableVpcServiceControls(
            self,
            *,
            parent: str,
            body: EnableVpcServiceControlsRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def disableVpcServiceControls(
            self,
            *,
            parent: str,
            body: DisableVpcServiceControlsRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def validate(
            self,
            *,
            parent: str,
            body: ValidateConsumerConfigRequest = ...,
            **kwargs: typing.Any
        ) -> ValidateConsumerConfigResponseHttpRequest: ...
        def dnsRecordSets(self) -> DnsRecordSetsResource: ...
        def connections(self) -> ConnectionsResource: ...
        def projects(self) -> ProjectsResource: ...
        def roles(self) -> RolesResource: ...
        def dnsZones(self) -> DnsZonesResource: ...
    class OperationsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            name: str,
            pageToken: str = ...,
            pageSize: int = ...,
            filter: str = ...,
            **kwargs: typing.Any
        ) -> ListOperationsResponseHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def cancel(
            self, *, name: str, body: CancelOperationRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
    def services(self) -> ServicesResource: ...
    def operations(self) -> OperationsResource: ...

class ValidateConsumerConfigResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ValidateConsumerConfigResponse: ...

class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOperationsResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListConnectionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListConnectionsResponse: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class ListPeeredDnsDomainsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListPeeredDnsDomainsResponse: ...

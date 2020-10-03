import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class AppengineResource(googleapiclient.discovery.Resource):
    class AppsResource(googleapiclient.discovery.Resource):
        class AuthorizedDomainsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                appsId: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListAuthorizedDomainsResponseHttpRequest: ...
        class DomainMappingsResource(googleapiclient.discovery.Resource):
            def patch(
                self,
                *,
                appsId: str,
                domainMappingsId: str,
                body: DomainMapping = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def create(
                self,
                *,
                appsId: str,
                body: DomainMapping = ...,
                overrideStrategy: typing_extensions.Literal[
                    "UNSPECIFIED_DOMAIN_OVERRIDE_STRATEGY", "STRICT", "OVERRIDE"
                ] = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                appsId: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListDomainMappingsResponseHttpRequest: ...
            def get(
                self, *, appsId: str, domainMappingsId: str, **kwargs: typing.Any
            ) -> DomainMappingHttpRequest: ...
            def delete(
                self, *, appsId: str, domainMappingsId: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        class ServicesResource(googleapiclient.discovery.Resource):
            class VersionsResource(googleapiclient.discovery.Resource):
                class InstancesResource(googleapiclient.discovery.Resource):
                    def get(
                        self,
                        *,
                        appsId: str,
                        servicesId: str,
                        versionsId: str,
                        instancesId: str,
                        **kwargs: typing.Any
                    ) -> InstanceHttpRequest: ...
                    def debug(
                        self,
                        *,
                        appsId: str,
                        servicesId: str,
                        versionsId: str,
                        instancesId: str,
                        body: DebugInstanceRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        appsId: str,
                        servicesId: str,
                        versionsId: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListInstancesResponseHttpRequest: ...
                    def delete(
                        self,
                        *,
                        appsId: str,
                        servicesId: str,
                        versionsId: str,
                        instancesId: str,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    appsId: str,
                    servicesId: str,
                    view: typing_extensions.Literal["BASIC", "FULL"] = ...,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListVersionsResponseHttpRequest: ...
                def get(
                    self,
                    *,
                    appsId: str,
                    servicesId: str,
                    versionsId: str,
                    view: typing_extensions.Literal["BASIC", "FULL"] = ...,
                    **kwargs: typing.Any
                ) -> VersionHttpRequest: ...
                def create(
                    self,
                    *,
                    appsId: str,
                    servicesId: str,
                    body: Version = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def patch(
                    self,
                    *,
                    appsId: str,
                    servicesId: str,
                    versionsId: str,
                    body: Version = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    appsId: str,
                    servicesId: str,
                    versionsId: str,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def instances(self) -> InstancesResource: ...
            def delete(
                self, *, appsId: str, servicesId: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def patch(
                self,
                *,
                appsId: str,
                servicesId: str,
                body: Service = ...,
                migrateTraffic: bool = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                appsId: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListServicesResponseHttpRequest: ...
            def get(
                self, *, appsId: str, servicesId: str, **kwargs: typing.Any
            ) -> ServiceHttpRequest: ...
            def versions(self) -> VersionsResource: ...
        class LocationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, appsId: str, locationsId: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                appsId: str,
                pageSize: int = ...,
                filter: str = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
        class AuthorizedCertificatesResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                appsId: str,
                authorizedCertificatesId: str,
                view: typing_extensions.Literal[
                    "BASIC_CERTIFICATE", "FULL_CERTIFICATE"
                ] = ...,
                **kwargs: typing.Any
            ) -> AuthorizedCertificateHttpRequest: ...
            def create(
                self,
                *,
                appsId: str,
                body: AuthorizedCertificate = ...,
                **kwargs: typing.Any
            ) -> AuthorizedCertificateHttpRequest: ...
            def patch(
                self,
                *,
                appsId: str,
                authorizedCertificatesId: str,
                body: AuthorizedCertificate = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> AuthorizedCertificateHttpRequest: ...
            def delete(
                self,
                *,
                appsId: str,
                authorizedCertificatesId: str,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                appsId: str,
                pageSize: int = ...,
                view: typing_extensions.Literal[
                    "BASIC_CERTIFICATE", "FULL_CERTIFICATE"
                ] = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListAuthorizedCertificatesResponseHttpRequest: ...
        class OperationsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                appsId: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListOperationsResponseHttpRequest: ...
            def get(
                self, *, appsId: str, operationsId: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        class FirewallResource(googleapiclient.discovery.Resource):
            class IngressRulesResource(googleapiclient.discovery.Resource):
                def create(
                    self, *, appsId: str, body: FirewallRule = ..., **kwargs: typing.Any
                ) -> FirewallRuleHttpRequest: ...
                def list(
                    self,
                    *,
                    appsId: str,
                    pageSize: int = ...,
                    matchingAddress: str = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListIngressRulesResponseHttpRequest: ...
                def batchUpdate(
                    self,
                    *,
                    appsId: str,
                    body: BatchUpdateIngressRulesRequest = ...,
                    **kwargs: typing.Any
                ) -> BatchUpdateIngressRulesResponseHttpRequest: ...
                def delete(
                    self, *, appsId: str, ingressRulesId: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, appsId: str, ingressRulesId: str, **kwargs: typing.Any
                ) -> FirewallRuleHttpRequest: ...
                def patch(
                    self,
                    *,
                    appsId: str,
                    ingressRulesId: str,
                    body: FirewallRule = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> FirewallRuleHttpRequest: ...
            def ingressRules(self) -> IngressRulesResource: ...
        def repair(
            self,
            *,
            appsId: str,
            body: RepairApplicationRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def get(
            self, *, appsId: str, **kwargs: typing.Any
        ) -> ApplicationHttpRequest: ...
        def patch(
            self,
            *,
            appsId: str,
            body: Application = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def create(
            self, *, body: Application = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def authorizedDomains(self) -> AuthorizedDomainsResource: ...
        def domainMappings(self) -> DomainMappingsResource: ...
        def services(self) -> ServicesResource: ...
        def locations(self) -> LocationsResource: ...
        def authorizedCertificates(self) -> AuthorizedCertificatesResource: ...
        def operations(self) -> OperationsResource: ...
        def firewall(self) -> FirewallResource: ...
    def apps(self) -> AppsResource: ...

class ListAuthorizedDomainsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAuthorizedDomainsResponse: ...

class ListServicesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListServicesResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class InstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Instance: ...

class ApplicationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Application: ...

class BatchUpdateIngressRulesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchUpdateIngressRulesResponse: ...

class VersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Version: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class DomainMappingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DomainMapping: ...

class ListDomainMappingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDomainMappingsResponse: ...

class ListAuthorizedCertificatesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAuthorizedCertificatesResponse: ...

class ListInstancesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListInstancesResponse: ...

class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLocationsResponse: ...

class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Location: ...

class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOperationsResponse: ...

class FirewallRuleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FirewallRule: ...

class ListIngressRulesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListIngressRulesResponse: ...

class AuthorizedCertificateHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AuthorizedCertificate: ...

class ListVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListVersionsResponse: ...

class ServiceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Service: ...

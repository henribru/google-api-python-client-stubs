import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudSecurityTokenResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class WorkloadIdentityPoolsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OpenidResource(googleapiclient.discovery.Resource):
                    def getJwks(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleIdentityStsV1JwksHttpRequest: ...

                @typing.type_check_only
                class WellKnownResource(googleapiclient.discovery.Resource):
                    def getOpenid_configuration(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleIdentityStsV1OpenIdProviderConfigHttpRequest: ...

                def openid(self) -> OpenidResource: ...
                def well_known(self) -> WellKnownResource: ...

            def workloadIdentityPools(self) -> WorkloadIdentityPoolsResource: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class WorkloadIdentityPoolsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OpenidResource(googleapiclient.discovery.Resource):
                    def getJwks(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleIdentityStsV1JwksHttpRequest: ...

                @typing.type_check_only
                class WellKnownResource(googleapiclient.discovery.Resource):
                    def getOpenid_configuration(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleIdentityStsV1OpenIdProviderConfigHttpRequest: ...

                def openid(self) -> OpenidResource: ...
                def well_known(self) -> WellKnownResource: ...

            def workloadIdentityPools(self) -> WorkloadIdentityPoolsResource: ...

        def locations(self) -> LocationsResource: ...

    @typing.type_check_only
    class V1Resource(googleapiclient.discovery.Resource):
        def token(
            self, *, body: GoogleIdentityStsV1ExchangeTokenRequest, **kwargs: typing.Any
        ) -> GoogleIdentityStsV1ExchangeTokenResponseHttpRequest: ...

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
    def projects(self) -> ProjectsResource: ...
    def v1(self) -> V1Resource: ...

@typing.type_check_only
class GoogleIdentityStsV1ExchangeTokenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleIdentityStsV1ExchangeTokenResponse: ...

@typing.type_check_only
class GoogleIdentityStsV1JwksHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleIdentityStsV1Jwks: ...

@typing.type_check_only
class GoogleIdentityStsV1OpenIdProviderConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleIdentityStsV1OpenIdProviderConfig: ...

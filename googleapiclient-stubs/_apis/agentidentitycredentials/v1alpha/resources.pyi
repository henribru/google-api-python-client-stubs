import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class AgentIdentityCredentialsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AuthProvidersResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class CredentialsResource(googleapiclient.discovery.Resource):
                    def finalize(
                        self,
                        *,
                        authProvider: str,
                        body: GoogleCloudAgentidentitycredentialsV1alpha_FinalizeCredentialsRequest,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAgentidentitycredentialsV1alpha_FinalizeCredentialsResponseHttpRequest: ...
                    def retrieve(
                        self,
                        *,
                        authProvider: str,
                        body: GoogleCloudAgentidentitycredentialsV1alpha_RetrieveCredentialsRequest,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudAgentidentitycredentialsV1alpha_RetrieveCredentialsResponseHttpRequest: ...

                def credentials(self) -> CredentialsResource: ...

            def authProviders(self) -> AuthProvidersResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1alpha_FinalizeCredentialsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAgentidentitycredentialsV1alpha_FinalizeCredentialsResponse: ...

@typing.type_check_only
class GoogleCloudAgentidentitycredentialsV1alpha_RetrieveCredentialsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudAgentidentitycredentialsV1alpha_RetrieveCredentialsResponse: ...

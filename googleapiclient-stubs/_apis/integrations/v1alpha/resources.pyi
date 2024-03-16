import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class IntegrationsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class CallbackResource(googleapiclient.discovery.Resource):
        def generateToken(
            self,
            *,
            code: str = ...,
            gcpProjectId: str = ...,
            product: typing_extensions.Literal[
                "UNSPECIFIED_PRODUCT", "IP", "APIGEE", "SECURITY"
            ] = ...,
            redirectUri: str = ...,
            state: str = ...,
            **kwargs: typing.Any,
        ) -> GoogleCloudIntegrationsV1alphaGenerateTokenResponseHttpRequest: ...

    @typing.type_check_only
    class ConnectorPlatformRegionsResource(googleapiclient.discovery.Resource):
        def enumerate(
            self, **kwargs: typing.Any
        ) -> GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseHttpRequest: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AppsScriptProjectsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseHttpRequest: ...
                def link(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseHttpRequest: ...

            @typing.type_check_only
            class AuthConfigsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudIntegrationsV1alphaAuthConfig = ...,
                    clientCertificate_encryptedPrivateKey: str = ...,
                    clientCertificate_passphrase: str = ...,
                    clientCertificate_sslCertificate: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIntegrationsV1alphaAuthConfigHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudIntegrationsV1alphaAuthConfigHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudIntegrationsV1alphaListAuthConfigsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudIntegrationsV1alphaListAuthConfigsResponseHttpRequest,
                    previous_response: GoogleCloudIntegrationsV1alphaListAuthConfigsResponse,
                ) -> (
                    GoogleCloudIntegrationsV1alphaListAuthConfigsResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudIntegrationsV1alphaAuthConfig = ...,
                    clientCertificate_encryptedPrivateKey: str = ...,
                    clientCertificate_passphrase: str = ...,
                    clientCertificate_sslCertificate: str = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIntegrationsV1alphaAuthConfigHttpRequest: ...

            @typing.type_check_only
            class CertificatesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudIntegrationsV1alphaCertificateHttpRequest: ...

            @typing.type_check_only
            class ConnectionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class RuntimeActionSchemasResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseHttpRequest,
                        previous_response: GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponse,
                    ) -> (
                        GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseHttpRequest
                        | None
                    ): ...

                @typing.type_check_only
                class RuntimeEntitySchemasResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseHttpRequest,
                        previous_response: GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponse,
                    ) -> (
                        GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseHttpRequest
                        | None
                    ): ...

                def getConnectionSchemaMetadata(
                    self, *, name: str, **kwargs: typing.Any
                ) -> (
                    GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataHttpRequest
                ): ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudIntegrationsV1alphaListConnectionsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudIntegrationsV1alphaListConnectionsResponseHttpRequest,
                    previous_response: GoogleCloudIntegrationsV1alphaListConnectionsResponse,
                ) -> (
                    GoogleCloudIntegrationsV1alphaListConnectionsResponseHttpRequest
                    | None
                ): ...
                def runtimeActionSchemas(self) -> RuntimeActionSchemasResource: ...
                def runtimeEntitySchemas(self) -> RuntimeEntitySchemasResource: ...

            @typing.type_check_only
            class IntegrationsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ExecutionsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class SuspensionsResource(googleapiclient.discovery.Resource):
                        def lift(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudIntegrationsV1alphaLiftSuspensionRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaLiftSuspensionResponseHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaListSuspensionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudIntegrationsV1alphaListSuspensionsResponseHttpRequest,
                            previous_response: GoogleCloudIntegrationsV1alphaListSuspensionsResponse,
                        ) -> (
                            GoogleCloudIntegrationsV1alphaListSuspensionsResponseHttpRequest
                            | None
                        ): ...
                        def resolve(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudIntegrationsV1alphaResolveSuspensionRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaResolveSuspensionResponseHttpRequest: ...

                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        filterParams_customFilter: str = ...,
                        filterParams_endTime: str = ...,
                        filterParams_eventStatuses: str | _list[str] = ...,
                        filterParams_executionId: str = ...,
                        filterParams_parameterKey: str = ...,
                        filterParams_parameterPairKey: str = ...,
                        filterParams_parameterPairValue: str = ...,
                        filterParams_parameterType: str = ...,
                        filterParams_parameterValue: str = ...,
                        filterParams_startTime: str = ...,
                        filterParams_taskStatuses: str | _list[str] = ...,
                        filterParams_workflowName: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        readMask: str = ...,
                        refreshAcl: bool = ...,
                        snapshotMetadataWithoutParams: bool = ...,
                        truncateParams: bool = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudIntegrationsV1alphaListExecutionsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudIntegrationsV1alphaListExecutionsResponseHttpRequest,
                        previous_response: GoogleCloudIntegrationsV1alphaListExecutionsResponse,
                    ) -> (
                        GoogleCloudIntegrationsV1alphaListExecutionsResponseHttpRequest
                        | None
                    ): ...
                    def suspensions(self) -> SuspensionsResource: ...

                @typing.type_check_only
                class VersionsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudIntegrationsV1alphaIntegrationVersion = ...,
                        createSampleIntegrations: bool = ...,
                        newIntegration: bool = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudIntegrationsV1alphaIntegrationVersionHttpRequest
                    ): ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def download(
                        self,
                        *,
                        name: str,
                        fileFormat: typing_extensions.Literal[
                            "FILE_FORMAT_UNSPECIFIED", "JSON", "YAML"
                        ] = ...,
                        files: typing_extensions.Literal[
                            "INTEGRATION_FILE_UNSPECIFIED",
                            "INTEGRATION",
                            "INTEGRATION_CONFIG_VARIABLES",
                        ]
                        | _list[
                            typing_extensions.Literal[
                                "INTEGRATION_FILE_UNSPECIFIED",
                                "INTEGRATION",
                                "INTEGRATION_CONFIG_VARIABLES",
                            ]
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> (
                        GoogleCloudIntegrationsV1alphaIntegrationVersionHttpRequest
                    ): ...
                    def list(
                        self,
                        *,
                        parent: str,
                        fieldMask: str = ...,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseHttpRequest,
                        previous_response: GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponse,
                    ) -> (
                        GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudIntegrationsV1alphaIntegrationVersion = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudIntegrationsV1alphaIntegrationVersionHttpRequest
                    ): ...
                    def publish(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseHttpRequest: ...
                    def takeoverEditLock(
                        self,
                        *,
                        integrationVersion: str,
                        body: GoogleCloudIntegrationsV1alphaTakeoverEditLockRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseHttpRequest: ...
                    def unpublish(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def upload(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseHttpRequest: ...

                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def execute(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseHttpRequest
                ): ...
                def executeEvent(
                    self,
                    *,
                    name: str,
                    body: dict[str, typing.Any] = ...,
                    triggerId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIntegrationsV1alphaExecuteEventResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudIntegrationsV1alphaListIntegrationsResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudIntegrationsV1alphaListIntegrationsResponseHttpRequest,
                    previous_response: GoogleCloudIntegrationsV1alphaListIntegrationsResponse,
                ) -> (
                    GoogleCloudIntegrationsV1alphaListIntegrationsResponseHttpRequest
                    | None
                ): ...
                def schedule(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseHttpRequest: ...
                def executions(self) -> ExecutionsResource: ...
                def versions(self) -> VersionsResource: ...

            @typing.type_check_only
            class ProductsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AuthConfigsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudIntegrationsV1alphaAuthConfig = ...,
                        clientCertificate_encryptedPrivateKey: str = ...,
                        clientCertificate_passphrase: str = ...,
                        clientCertificate_sslCertificate: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaAuthConfigHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudIntegrationsV1alphaAuthConfigHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        readMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudIntegrationsV1alphaListAuthConfigsResponseHttpRequest
                    ): ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudIntegrationsV1alphaListAuthConfigsResponseHttpRequest,
                        previous_response: GoogleCloudIntegrationsV1alphaListAuthConfigsResponse,
                    ) -> (
                        GoogleCloudIntegrationsV1alphaListAuthConfigsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudIntegrationsV1alphaAuthConfig = ...,
                        clientCertificate_encryptedPrivateKey: str = ...,
                        clientCertificate_passphrase: str = ...,
                        clientCertificate_sslCertificate: str = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaAuthConfigHttpRequest: ...

                @typing.type_check_only
                class CertificatesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudIntegrationsV1alphaCertificate = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaCertificateHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudIntegrationsV1alphaCertificateHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        readMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaListCertificatesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudIntegrationsV1alphaListCertificatesResponseHttpRequest,
                        previous_response: GoogleCloudIntegrationsV1alphaListCertificatesResponse,
                    ) -> (
                        GoogleCloudIntegrationsV1alphaListCertificatesResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudIntegrationsV1alphaCertificate = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaCertificateHttpRequest: ...

                @typing.type_check_only
                class IntegrationsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ExecutionsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class SuspensionsResource(googleapiclient.discovery.Resource):
                            def lift(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudIntegrationsV1alphaLiftSuspensionRequest = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudIntegrationsV1alphaLiftSuspensionResponseHttpRequest: ...
                            def list(
                                self,
                                *,
                                parent: str,
                                filter: str = ...,
                                orderBy: str = ...,
                                pageSize: int = ...,
                                pageToken: str = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudIntegrationsV1alphaListSuspensionsResponseHttpRequest: ...
                            def list_next(
                                self,
                                previous_request: GoogleCloudIntegrationsV1alphaListSuspensionsResponseHttpRequest,
                                previous_response: GoogleCloudIntegrationsV1alphaListSuspensionsResponse,
                            ) -> (
                                GoogleCloudIntegrationsV1alphaListSuspensionsResponseHttpRequest
                                | None
                            ): ...
                            def resolve(
                                self,
                                *,
                                name: str,
                                body: GoogleCloudIntegrationsV1alphaResolveSuspensionRequest = ...,
                                **kwargs: typing.Any,
                            ) -> GoogleCloudIntegrationsV1alphaResolveSuspensionResponseHttpRequest: ...

                        def cancel(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudIntegrationsV1alphaCancelExecutionRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaCancelExecutionResponseHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudIntegrationsV1alphaExecutionHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            filterParams_customFilter: str = ...,
                            filterParams_endTime: str = ...,
                            filterParams_eventStatuses: str | _list[str] = ...,
                            filterParams_executionId: str = ...,
                            filterParams_parameterKey: str = ...,
                            filterParams_parameterPairKey: str = ...,
                            filterParams_parameterPairValue: str = ...,
                            filterParams_parameterType: str = ...,
                            filterParams_parameterValue: str = ...,
                            filterParams_startTime: str = ...,
                            filterParams_taskStatuses: str | _list[str] = ...,
                            filterParams_workflowName: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            readMask: str = ...,
                            refreshAcl: bool = ...,
                            snapshotMetadataWithoutParams: bool = ...,
                            truncateParams: bool = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaListExecutionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudIntegrationsV1alphaListExecutionsResponseHttpRequest,
                            previous_response: GoogleCloudIntegrationsV1alphaListExecutionsResponse,
                        ) -> (
                            GoogleCloudIntegrationsV1alphaListExecutionsResponseHttpRequest
                            | None
                        ): ...
                        def suspensions(self) -> SuspensionsResource: ...

                    @typing.type_check_only
                    class VersionsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudIntegrationsV1alphaIntegrationVersion = ...,
                            createSampleIntegrations: bool = ...,
                            newIntegration: bool = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudIntegrationsV1alphaIntegrationVersionHttpRequest
                        ): ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def download(
                            self,
                            *,
                            name: str,
                            fileFormat: typing_extensions.Literal[
                                "FILE_FORMAT_UNSPECIFIED", "JSON", "YAML"
                            ] = ...,
                            files: typing_extensions.Literal[
                                "INTEGRATION_FILE_UNSPECIFIED",
                                "INTEGRATION",
                                "INTEGRATION_CONFIG_VARIABLES",
                            ]
                            | _list[
                                typing_extensions.Literal[
                                    "INTEGRATION_FILE_UNSPECIFIED",
                                    "INTEGRATION",
                                    "INTEGRATION_CONFIG_VARIABLES",
                                ]
                            ] = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> (
                            GoogleCloudIntegrationsV1alphaIntegrationVersionHttpRequest
                        ): ...
                        def list(
                            self,
                            *,
                            parent: str,
                            fieldMask: str = ...,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseHttpRequest,
                            previous_response: GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponse,
                        ) -> (
                            GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudIntegrationsV1alphaIntegrationVersion = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> (
                            GoogleCloudIntegrationsV1alphaIntegrationVersionHttpRequest
                        ): ...
                        def publish(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudIntegrationsV1alphaPublishIntegrationVersionRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseHttpRequest: ...
                        def takeoverEditLock(
                            self,
                            *,
                            integrationVersion: str,
                            body: GoogleCloudIntegrationsV1alphaTakeoverEditLockRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseHttpRequest: ...
                        def unpublish(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudIntegrationsV1alphaUnpublishIntegrationVersionRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def upload(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudIntegrationsV1alphaUploadIntegrationVersionRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseHttpRequest: ...

                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def execute(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudIntegrationsV1alphaExecuteIntegrationsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaListIntegrationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudIntegrationsV1alphaListIntegrationsResponseHttpRequest,
                        previous_response: GoogleCloudIntegrationsV1alphaListIntegrationsResponse,
                    ) -> (
                        GoogleCloudIntegrationsV1alphaListIntegrationsResponseHttpRequest
                        | None
                    ): ...
                    def schedule(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudIntegrationsV1alphaScheduleIntegrationsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseHttpRequest: ...
                    def executions(self) -> ExecutionsResource: ...
                    def versions(self) -> VersionsResource: ...

                @typing.type_check_only
                class IntegrationtemplatesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class VersionsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudIntegrationsV1alphaIntegrationTemplateVersion = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseHttpRequest,
                            previous_response: GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponse,
                        ) -> (
                            GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseHttpRequest
                            | None
                        ): ...

                    def versions(self) -> VersionsResource: ...

                @typing.type_check_only
                class SfdcInstancesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class SfdcChannelsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudIntegrationsV1alphaSfdcChannel = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaSfdcChannelHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudIntegrationsV1alphaSfdcChannelHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            readMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseHttpRequest,
                            previous_response: GoogleCloudIntegrationsV1alphaListSfdcChannelsResponse,
                        ) -> (
                            GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudIntegrationsV1alphaSfdcChannel = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaSfdcChannelHttpRequest: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudIntegrationsV1alphaSfdcInstance = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaSfdcInstanceHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudIntegrationsV1alphaSfdcInstanceHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        readMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseHttpRequest,
                        previous_response: GoogleCloudIntegrationsV1alphaListSfdcInstancesResponse,
                    ) -> (
                        GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudIntegrationsV1alphaSfdcInstance = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaSfdcInstanceHttpRequest: ...
                    def sfdcChannels(self) -> SfdcChannelsResource: ...

                def authConfigs(self) -> AuthConfigsResource: ...
                def certificates(self) -> CertificatesResource: ...
                def integrations(self) -> IntegrationsResource: ...
                def integrationtemplates(self) -> IntegrationtemplatesResource: ...
                def sfdcInstances(self) -> SfdcInstancesResource: ...

            @typing.type_check_only
            class SfdcInstancesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class SfdcChannelsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudIntegrationsV1alphaSfdcChannel = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaSfdcChannelHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudIntegrationsV1alphaSfdcChannelHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        readMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseHttpRequest,
                        previous_response: GoogleCloudIntegrationsV1alphaListSfdcChannelsResponse,
                    ) -> (
                        GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseHttpRequest
                        | None
                    ): ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudIntegrationsV1alphaSfdcChannel = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaSfdcChannelHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudIntegrationsV1alphaSfdcInstance = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIntegrationsV1alphaSfdcInstanceHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudIntegrationsV1alphaSfdcInstanceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseHttpRequest
                ): ...
                def list_next(
                    self,
                    previous_request: GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseHttpRequest,
                    previous_response: GoogleCloudIntegrationsV1alphaListSfdcInstancesResponse,
                ) -> (
                    GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudIntegrationsV1alphaSfdcInstance = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIntegrationsV1alphaSfdcInstanceHttpRequest: ...
                def sfdcChannels(self) -> SfdcChannelsResource: ...

            def appsScriptProjects(self) -> AppsScriptProjectsResource: ...
            def authConfigs(self) -> AuthConfigsResource: ...
            def certificates(self) -> CertificatesResource: ...
            def connections(self) -> ConnectionsResource: ...
            def integrations(self) -> IntegrationsResource: ...
            def products(self) -> ProductsResource: ...
            def sfdcInstances(self) -> SfdcInstancesResource: ...

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
    def callback(self) -> CallbackResource: ...
    def connectorPlatformRegions(self) -> ConnectorPlatformRegionsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaAuthConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaAuthConfig: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCancelExecutionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaCancelExecutionResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCertificateHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaCertificate: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaConnectionSchemaMetadataHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaConnectionSchemaMetadata: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaCreateAppsScriptProjectResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaDownloadIntegrationVersionResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaEnumerateConnectorPlatformRegionsResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaExecuteEventResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaExecuteEventResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaExecuteIntegrationsResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaExecutionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaExecution: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaGenerateTokenResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaGenerateTokenResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaIntegrationTemplateVersionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaIntegrationTemplateVersion: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaIntegrationVersionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaIntegrationVersion: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaLiftSuspensionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaLiftSuspensionResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaLinkAppsScriptProjectResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListAuthConfigsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaListAuthConfigsResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListCertificatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaListCertificatesResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListConnectionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaListConnectionsResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListExecutionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaListExecutionsResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaListIntegrationTemplateVersionsResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaListIntegrationVersionsResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListIntegrationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaListIntegrationsResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaListRuntimeActionSchemasResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaListRuntimeEntitySchemasResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListSfdcChannelsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaListSfdcChannelsResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListSfdcInstancesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaListSfdcInstancesResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListSuspensionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaListSuspensionsResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaPublishIntegrationVersionResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaResolveSuspensionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaResolveSuspensionResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaScheduleIntegrationsResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaSfdcChannelHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaSfdcChannel: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaSfdcInstanceHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaSfdcInstance: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaTakeoverEditLockResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaTakeoverEditLockResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaUploadIntegrationVersionResponse: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleProtobufEmpty: ...

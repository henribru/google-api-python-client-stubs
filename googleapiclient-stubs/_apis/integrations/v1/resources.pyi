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
                ) -> (
                    GoogleCloudIntegrationsV1alphaListCertificatesResponseHttpRequest
                ): ...
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
            class ClientsResource(googleapiclient.discovery.Resource):
                def deprovision(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudIntegrationsV1alphaDeprovisionClientRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def provision(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudIntegrationsV1alphaProvisionClientRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def replace(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudIntegrationsV1alphaReplaceServiceAccountRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def switch(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudIntegrationsV1alphaSwitchEncryptionRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def switchVariableMasking(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudIntegrationsV1alphaSwitchVariableMaskingRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...

            @typing.type_check_only
            class CloudFunctionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudIntegrationsV1alphaCreateCloudFunctionRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudIntegrationsV1alphaCreateCloudFunctionResponseHttpRequest
                ): ...

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

                    def cancel(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudIntegrationsV1alphaCancelExecutionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudIntegrationsV1alphaCancelExecutionResponseHttpRequest
                    ): ...
                    def download(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudIntegrationsV1alphaDownloadExecutionResponseHttpRequest: ...
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
                    def replay(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudIntegrationsV1alphaReplayExecutionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> (
                        GoogleCloudIntegrationsV1alphaReplayExecutionResponseHttpRequest
                    ): ...
                    def suspensions(self) -> SuspensionsResource: ...

                @typing.type_check_only
                class VersionsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class TestCasesResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudIntegrationsV1alphaTestCase = ...,
                            testCaseId: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaTestCaseHttpRequest: ...
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
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaDownloadTestCaseResponseHttpRequest: ...
                        def execute(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudIntegrationsV1alphaExecuteTestCasesRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaExecuteTestCasesResponseHttpRequest: ...
                        def executeTest(
                            self,
                            *,
                            testCaseName: str,
                            body: GoogleCloudIntegrationsV1alphaExecuteTestCaseRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaExecuteTestCaseResponseHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudIntegrationsV1alphaTestCaseHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            readMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaListTestCasesResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: GoogleCloudIntegrationsV1alphaListTestCasesResponseHttpRequest,
                            previous_response: GoogleCloudIntegrationsV1alphaListTestCasesResponse,
                        ) -> (
                            GoogleCloudIntegrationsV1alphaListTestCasesResponseHttpRequest
                            | None
                        ): ...
                        def listExecutions(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            readMask: str = ...,
                            truncateParams: bool = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaListTestCaseExecutionsResponseHttpRequest: ...
                        def listExecutions_next(
                            self,
                            previous_request: GoogleCloudIntegrationsV1alphaListTestCaseExecutionsResponseHttpRequest,
                            previous_response: GoogleCloudIntegrationsV1alphaListTestCaseExecutionsResponse,
                        ) -> (
                            GoogleCloudIntegrationsV1alphaListTestCaseExecutionsResponseHttpRequest
                            | None
                        ): ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudIntegrationsV1alphaTestCase = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaTestCaseHttpRequest: ...
                        def takeoverEditLock(
                            self,
                            *,
                            name: str,
                            body: GoogleCloudIntegrationsV1alphaTakeoverTestCaseEditLockRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaTestCaseHttpRequest: ...
                        def upload(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudIntegrationsV1alphaUploadTestCaseRequest = ...,
                            **kwargs: typing.Any,
                        ) -> GoogleCloudIntegrationsV1alphaUploadTestCaseResponseHttpRequest: ...

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
                    def downloadJsonPackage(
                        self,
                        *,
                        name: str,
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
                    ) -> GoogleCloudIntegrationsV1alphaDownloadJsonPackageResponseHttpRequest: ...
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
                    def testCases(self) -> TestCasesResource: ...

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
                def test(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudIntegrationsV1alphaTestIntegrationsRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudIntegrationsV1alphaTestIntegrationsResponseHttpRequest
                ): ...
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
                class CloudFunctionsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudIntegrationsV1alphaCreateCloudFunctionRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaCreateCloudFunctionResponseHttpRequest: ...

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

                        def download(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudIntegrationsV1alphaDownloadExecutionResponseHttpRequest: ...
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
                    def test(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudIntegrationsV1alphaTestIntegrationsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleCloudIntegrationsV1alphaTestIntegrationsResponseHttpRequest: ...
                    def executions(self) -> ExecutionsResource: ...
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
                def cloudFunctions(self) -> CloudFunctionsResource: ...
                def integrations(self) -> IntegrationsResource: ...
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

            @typing.type_check_only
            class TemplatesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudIntegrationsV1alphaTemplate = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIntegrationsV1alphaTemplateHttpRequest: ...
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
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudIntegrationsV1alphaDownloadTemplateResponseHttpRequest
                ): ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudIntegrationsV1alphaTemplateHttpRequest: ...
                def import_(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudIntegrationsV1alphaImportTemplateRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudIntegrationsV1alphaImportTemplateResponseHttpRequest
                ): ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIntegrationsV1alphaListTemplatesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudIntegrationsV1alphaListTemplatesResponseHttpRequest,
                    previous_response: GoogleCloudIntegrationsV1alphaListTemplatesResponse,
                ) -> (
                    GoogleCloudIntegrationsV1alphaListTemplatesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudIntegrationsV1alphaTemplate = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIntegrationsV1alphaTemplateHttpRequest: ...
                def search(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    readMask: str = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudIntegrationsV1alphaSearchTemplatesResponseHttpRequest
                ): ...
                def search_next(
                    self,
                    previous_request: GoogleCloudIntegrationsV1alphaSearchTemplatesResponseHttpRequest,
                    previous_response: GoogleCloudIntegrationsV1alphaSearchTemplatesResponse,
                ) -> (
                    GoogleCloudIntegrationsV1alphaSearchTemplatesResponseHttpRequest
                    | None
                ): ...
                def share(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudIntegrationsV1alphaShareTemplateRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def unshare(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudIntegrationsV1alphaUnshareTemplateRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def upload(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudIntegrationsV1alphaUploadTemplateRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleCloudIntegrationsV1alphaUploadTemplateResponseHttpRequest
                ): ...
                def use(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudIntegrationsV1alphaUseTemplateRequest = ...,
                    **kwargs: typing.Any,
                ) -> GoogleCloudIntegrationsV1alphaUseTemplateResponseHttpRequest: ...

            def generateOpenApiSpec(
                self,
                *,
                name: str,
                body: GoogleCloudIntegrationsV1alphaGenerateOpenApiSpecRequest = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleCloudIntegrationsV1alphaGenerateOpenApiSpecResponseHttpRequest
            ): ...
            def getClients(
                self, *, parent: str, **kwargs: typing.Any
            ) -> GoogleCloudIntegrationsV1alphaGetClientResponseHttpRequest: ...
            def appsScriptProjects(self) -> AppsScriptProjectsResource: ...
            def authConfigs(self) -> AuthConfigsResource: ...
            def certificates(self) -> CertificatesResource: ...
            def clients(self) -> ClientsResource: ...
            def cloudFunctions(self) -> CloudFunctionsResource: ...
            def connections(self) -> ConnectionsResource: ...
            def integrations(self) -> IntegrationsResource: ...
            def products(self) -> ProductsResource: ...
            def sfdcInstances(self) -> SfdcInstancesResource: ...
            def templates(self) -> TemplatesResource: ...

        def getClientmetadata(
            self, *, parent: str, **kwargs: typing.Any
        ) -> GoogleCloudIntegrationsV1alphaGetClientMetadataResponseHttpRequest: ...
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
class GoogleCloudIntegrationsV1alphaCreateCloudFunctionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaCreateCloudFunctionResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaDownloadExecutionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaDownloadExecutionResponse: ...

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
class GoogleCloudIntegrationsV1alphaDownloadJsonPackageResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaDownloadJsonPackageResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaDownloadTemplateResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaDownloadTemplateResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaDownloadTestCaseResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaDownloadTestCaseResponse: ...

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
class GoogleCloudIntegrationsV1alphaExecuteTestCaseResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaExecuteTestCaseResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaExecuteTestCasesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaExecuteTestCasesResponse: ...

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
class GoogleCloudIntegrationsV1alphaGenerateOpenApiSpecResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaGenerateOpenApiSpecResponse: ...

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
class GoogleCloudIntegrationsV1alphaGetClientMetadataResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaGetClientMetadataResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaGetClientResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaGetClientResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaImportTemplateResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaImportTemplateResponse: ...

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
class GoogleCloudIntegrationsV1alphaListTemplatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaListTemplatesResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListTestCaseExecutionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaListTestCaseExecutionsResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaListTestCasesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaListTestCasesResponse: ...

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
class GoogleCloudIntegrationsV1alphaReplayExecutionResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaReplayExecutionResponse: ...

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
class GoogleCloudIntegrationsV1alphaSearchTemplatesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaSearchTemplatesResponse: ...

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
class GoogleCloudIntegrationsV1alphaTemplateHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaTemplate: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaTestCaseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaTestCase: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaTestIntegrationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaTestIntegrationsResponse: ...

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
class GoogleCloudIntegrationsV1alphaUploadTemplateResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaUploadTemplateResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaUploadTestCaseResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaUploadTestCaseResponse: ...

@typing.type_check_only
class GoogleCloudIntegrationsV1alphaUseTemplateResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudIntegrationsV1alphaUseTemplateResponse: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleProtobufEmpty: ...

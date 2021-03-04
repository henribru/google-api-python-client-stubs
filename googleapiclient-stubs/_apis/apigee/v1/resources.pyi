import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class ApigeeResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class HybridResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class IssuersResource(googleapiclient.discovery.Resource):
            def list(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListHybridIssuersResponseHttpRequest: ...
        def issuers(self) -> IssuersResource: ...
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AnalyticsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DatastoresResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1Datastore = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1DatastoreHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1DatastoreHttpRequest: ...
                def list(
                    self, *, parent: str, targetType: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListDatastoresResponseHttpRequest: ...
                def test(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1Datastore = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1TestDatastoreResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1Datastore = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1DatastoreHttpRequest: ...
            def datastores(self) -> DatastoresResource: ...
        @typing.type_check_only
        class ApiproductsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AttributesResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributesHttpRequest: ...
                def updateApiProductAttribute(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1Attribute = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1ApiProduct = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ApiProductHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ApiProductHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ApiProductHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                attributename: str = ...,
                attributevalue: str = ...,
                count: str = ...,
                expand: bool = ...,
                startKey: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListApiProductsResponseHttpRequest: ...
            def update(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1ApiProduct = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ApiProductHttpRequest: ...
            def attributes(self) -> AttributesResource: ...
        @typing.type_check_only
        class ApisResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DeploymentsResource(googleapiclient.discovery.Resource):
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...
            @typing.type_check_only
            class KeyvaluemapsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1KeyValueMap = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1KeyValueMapHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1KeyValueMapHttpRequest: ...
            @typing.type_check_only
            class RevisionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DeploymentsResource(googleapiclient.discovery.Resource):
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ApiProxyRevisionHttpRequest: ...
                def get(
                    self, *, name: str, format: str = ..., **kwargs: typing.Any
                ) -> GoogleApiHttpBodyHttpRequest: ...
                def updateApiProxyRevision(
                    self,
                    *,
                    name: str,
                    body: GoogleApiHttpBody = ...,
                    validate: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ApiProxyRevisionHttpRequest: ...
                def deployments(self) -> DeploymentsResource: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleApiHttpBody = ...,
                action: str = ...,
                name: str = ...,
                validate: bool = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ApiProxyRevisionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ApiProxyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ApiProxyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                includeMetaData: bool = ...,
                includeRevisions: bool = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListApiProxiesResponseHttpRequest: ...
            def deployments(self) -> DeploymentsResource: ...
            def keyvaluemaps(self) -> KeyvaluemapsResource: ...
            def revisions(self) -> RevisionsResource: ...
        @typing.type_check_only
        class AppsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1AppHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                apiProduct: str = ...,
                apptype: str = ...,
                expand: bool = ...,
                ids: str = ...,
                includeCred: bool = ...,
                keyStatus: str = ...,
                rows: str = ...,
                startKey: str = ...,
                status: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListAppsResponseHttpRequest: ...
        @typing.type_check_only
        class DatacollectorsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1DataCollector = ...,
                dataCollectorId: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DataCollectorHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DataCollectorHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListDataCollectorsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1DataCollector = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DataCollectorHttpRequest: ...
        @typing.type_check_only
        class DeploymentsResource(googleapiclient.discovery.Resource):
            def list(
                self, *, parent: str, sharedFlows: bool = ..., **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...
        @typing.type_check_only
        class DevelopersResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AppsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AttributesResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1AttributesHttpRequest: ...
                    def updateDeveloperAppAttribute(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudApigeeV1Attribute = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
                @typing.type_check_only
                class KeysResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class ApiproductsResource(googleapiclient.discovery.Resource):
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudApigeeV1DeveloperAppKeyHttpRequest: ...
                        def updateDeveloperAppKeyApiProduct(
                            self, *, name: str, action: str = ..., **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                    @typing.type_check_only
                    class CreateResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudApigeeV1DeveloperAppKey = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudApigeeV1DeveloperAppKeyHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1DeveloperAppKeyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1DeveloperAppKeyHttpRequest: ...
                    def replaceDeveloperAppKey(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudApigeeV1DeveloperAppKey = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1DeveloperAppKeyHttpRequest: ...
                    def updateDeveloperAppKey(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudApigeeV1DeveloperAppKey = ...,
                        action: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1DeveloperAppKeyHttpRequest: ...
                    def apiproducts(self) -> ApiproductsResource: ...
                    def create(self) -> CreateResource: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1DeveloperApp = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1DeveloperAppHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1DeveloperAppHttpRequest: ...
                def generateKeyPairOrUpdateDeveloperAppStatus(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1DeveloperApp = ...,
                    action: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1DeveloperAppHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    entity: str = ...,
                    query: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1DeveloperAppHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    count: str = ...,
                    expand: bool = ...,
                    shallowExpand: bool = ...,
                    startKey: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListDeveloperAppsResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1DeveloperApp = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1DeveloperAppHttpRequest: ...
                def attributes(self) -> AttributesResource: ...
                def keys(self) -> KeysResource: ...
            @typing.type_check_only
            class AttributesResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributesHttpRequest: ...
                def updateDeveloperAttribute(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1Attribute = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1Developer = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DeveloperHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DeveloperHttpRequest: ...
            def get(
                self, *, name: str, action: str = ..., **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DeveloperHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                app: str = ...,
                count: str = ...,
                expand: bool = ...,
                ids: str = ...,
                includeCompany: bool = ...,
                startKey: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListOfDevelopersResponseHttpRequest: ...
            def setDeveloperStatus(
                self, *, name: str, action: str = ..., **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def update(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1Developer = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DeveloperHttpRequest: ...
            def apps(self) -> AppsResource: ...
            def attributes(self) -> AttributesResource: ...
        @typing.type_check_only
        class EnvgroupsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AttachmentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1EnvironmentGroupAttachment = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1EnvironmentGroupAttachmentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1EnvironmentGroup = ...,
                name: str = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1EnvironmentGroupHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListEnvironmentGroupsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1EnvironmentGroup = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def attachments(self) -> AttachmentsResource: ...
        @typing.type_check_only
        class EnvironmentsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AnalyticsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AdminResource(googleapiclient.discovery.Resource):
                    def getSchemav2(
                        self, *, name: str, type: str = ..., **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1SchemaHttpRequest: ...
                @typing.type_check_only
                class ExportsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudApigeeV1ExportRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1ExportHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1ExportHttpRequest: ...
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1ListExportsResponseHttpRequest: ...
                def admin(self) -> AdminResource: ...
                def exports(self) -> ExportsResource: ...
            @typing.type_check_only
            class ApisResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DeploymentsResource(googleapiclient.discovery.Resource):
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...
                @typing.type_check_only
                class RevisionsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class DebugsessionsResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class DataResource(googleapiclient.discovery.Resource):
                            def get(
                                self, *, name: str, **kwargs: typing.Any
                            ) -> GoogleCloudApigeeV1DebugSessionTransactionHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudApigeeV1DebugSession = ...,
                            timeout: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudApigeeV1DebugSessionHttpRequest: ...
                        def deleteData(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudApigeeV1DebugSessionHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudApigeeV1ListDebugSessionsResponseHttpRequest: ...
                        def data(self) -> DataResource: ...
                    @typing.type_check_only
                    class DeploymentsResource(googleapiclient.discovery.Resource):
                        def generateDeployChangeReport(
                            self,
                            *,
                            name: str,
                            override: bool = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudApigeeV1DeploymentChangeReportHttpRequest: ...
                        def generateUndeployChangeReport(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudApigeeV1DeploymentChangeReportHttpRequest: ...
                    def deploy(
                        self,
                        *,
                        name: str,
                        override: bool = ...,
                        sequencedRollout: bool = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1DeploymentHttpRequest: ...
                    def getDeployments(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1DeploymentHttpRequest: ...
                    def undeploy(
                        self,
                        *,
                        name: str,
                        sequencedRollout: bool = ...,
                        **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def debugsessions(self) -> DebugsessionsResource: ...
                    def deployments(self) -> DeploymentsResource: ...
                def deployments(self) -> DeploymentsResource: ...
                def revisions(self) -> RevisionsResource: ...
            @typing.type_check_only
            class CachesResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
            @typing.type_check_only
            class DeploymentsResource(googleapiclient.discovery.Resource):
                def list(
                    self, *, parent: str, sharedFlows: bool = ..., **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...
            @typing.type_check_only
            class FlowhooksResource(googleapiclient.discovery.Resource):
                def attachSharedFlowToFlowHook(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1FlowHook = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1FlowHookHttpRequest: ...
                def detachSharedFlowFromFlowHook(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1FlowHookHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1FlowHookHttpRequest: ...
            @typing.type_check_only
            class KeystoresResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AliasesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleApiHttpBody = ...,
                        alias: str = ...,
                        format: str = ...,
                        ignoreExpiryValidation: bool = ...,
                        ignoreNewlineValidation: bool = ...,
                        x_password: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1AliasHttpRequest: ...
                    def csr(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleApiHttpBodyHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1AliasHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1AliasHttpRequest: ...
                    def getCertificate(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleApiHttpBodyHttpRequest: ...
                    def update(
                        self,
                        *,
                        name: str,
                        body: GoogleApiHttpBody = ...,
                        ignoreExpiryValidation: bool = ...,
                        ignoreNewlineValidation: bool = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1AliasHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1Keystore = ...,
                    name: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1KeystoreHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1KeystoreHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1KeystoreHttpRequest: ...
                def aliases(self) -> AliasesResource: ...
            @typing.type_check_only
            class KeyvaluemapsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1KeyValueMap = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1KeyValueMapHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1KeyValueMapHttpRequest: ...
            @typing.type_check_only
            class OptimizedStatsResource(googleapiclient.discovery.Resource):
                def get(
                    self,
                    *,
                    name: str,
                    accuracy: str = ...,
                    aggTable: str = ...,
                    filter: str = ...,
                    limit: str = ...,
                    offset: str = ...,
                    realtime: bool = ...,
                    select: str = ...,
                    sonar: bool = ...,
                    sort: str = ...,
                    sortby: str = ...,
                    timeRange: str = ...,
                    timeUnit: str = ...,
                    topk: str = ...,
                    tsAscending: bool = ...,
                    tzo: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1OptimizedStatsHttpRequest: ...
            @typing.type_check_only
            class QueriesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1Query = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AsyncQueryHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AsyncQueryHttpRequest: ...
                def getResult(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleApiHttpBodyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    dataset: str = ...,
                    inclQueriesWithoutReport: str = ...,
                    status: str = ...,
                    submittedBy: str = ...,
                    to: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListAsyncQueriesResponseHttpRequest: ...
            @typing.type_check_only
            class ReferencesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1Reference = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ReferenceHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ReferenceHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ReferenceHttpRequest: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1Reference = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ReferenceHttpRequest: ...
            @typing.type_check_only
            class ResourcefilesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleApiHttpBody = ...,
                    name: str = ...,
                    type: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ResourceFileHttpRequest: ...
                def delete(
                    self, *, parent: str, type: str, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ResourceFileHttpRequest: ...
                def get(
                    self, *, parent: str, type: str, name: str, **kwargs: typing.Any
                ) -> GoogleApiHttpBodyHttpRequest: ...
                def list(
                    self, *, parent: str, type: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListEnvironmentResourcesResponseHttpRequest: ...
                def listEnvironmentResources(
                    self, *, parent: str, type: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListEnvironmentResourcesResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    parent: str,
                    type: str,
                    name: str,
                    body: GoogleApiHttpBody = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ResourceFileHttpRequest: ...
            @typing.type_check_only
            class SharedflowsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DeploymentsResource(googleapiclient.discovery.Resource):
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...
                @typing.type_check_only
                class RevisionsResource(googleapiclient.discovery.Resource):
                    def deploy(
                        self, *, name: str, override: bool = ..., **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1DeploymentHttpRequest: ...
                    def getDeployments(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1DeploymentHttpRequest: ...
                    def undeploy(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                def deployments(self) -> DeploymentsResource: ...
                def revisions(self) -> RevisionsResource: ...
            @typing.type_check_only
            class StatsResource(googleapiclient.discovery.Resource):
                def get(
                    self,
                    *,
                    name: str,
                    accuracy: str = ...,
                    aggTable: str = ...,
                    filter: str = ...,
                    limit: str = ...,
                    offset: str = ...,
                    realtime: bool = ...,
                    select: str = ...,
                    sonar: bool = ...,
                    sort: str = ...,
                    sortby: str = ...,
                    timeRange: str = ...,
                    timeUnit: str = ...,
                    topk: str = ...,
                    tsAscending: bool = ...,
                    tzo: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1StatsHttpRequest: ...
            @typing.type_check_only
            class TargetserversResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1TargetServer = ...,
                    name: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1TargetServerHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1TargetServerHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1TargetServerHttpRequest: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1TargetServer = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1TargetServerHttpRequest: ...
            @typing.type_check_only
            class TraceConfigResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OverridesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudApigeeV1TraceConfigOverride = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1TraceConfigOverrideHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1TraceConfigOverrideHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1ListTraceConfigOverridesResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudApigeeV1TraceConfigOverride = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1TraceConfigOverrideHttpRequest: ...
                def overrides(self) -> OverridesResource: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1Environment = ...,
                name: str = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1EnvironmentHttpRequest: ...
            def getDebugmask(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DebugMaskHttpRequest: ...
            def getDeployedConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1EnvironmentConfigHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                options_requestedPolicyVersion: int = ...,
                **kwargs: typing.Any
            ) -> GoogleIamV1PolicyHttpRequest: ...
            def getTraceConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1TraceConfigHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: GoogleIamV1SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleIamV1PolicyHttpRequest: ...
            def subscribe(
                self, *, parent: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1SubscriptionHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: GoogleIamV1TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
            def unsubscribe(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1Subscription = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def update(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1Environment = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1EnvironmentHttpRequest: ...
            def updateDebugmask(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1DebugMask = ...,
                replaceRepeatedFields: bool = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DebugMaskHttpRequest: ...
            def updateEnvironment(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1Environment = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1EnvironmentHttpRequest: ...
            def updateTraceConfig(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1TraceConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1TraceConfigHttpRequest: ...
            def analytics(self) -> AnalyticsResource: ...
            def apis(self) -> ApisResource: ...
            def caches(self) -> CachesResource: ...
            def deployments(self) -> DeploymentsResource: ...
            def flowhooks(self) -> FlowhooksResource: ...
            def keystores(self) -> KeystoresResource: ...
            def keyvaluemaps(self) -> KeyvaluemapsResource: ...
            def optimizedStats(self) -> OptimizedStatsResource: ...
            def queries(self) -> QueriesResource: ...
            def references(self) -> ReferencesResource: ...
            def resourcefiles(self) -> ResourcefilesResource: ...
            def sharedflows(self) -> SharedflowsResource: ...
            def stats(self) -> StatsResource: ...
            def targetservers(self) -> TargetserversResource: ...
            def traceConfig(self) -> TraceConfigResource: ...
        @typing.type_check_only
        class HostQueriesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1Query = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1AsyncQueryHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1AsyncQueryHttpRequest: ...
            def getResult(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleApiHttpBodyHttpRequest: ...
            def getResultView(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1AsyncQueryResultViewHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                dataset: str = ...,
                envgroupHostname: str = ...,
                inclQueriesWithoutReport: str = ...,
                status: str = ...,
                submittedBy: str = ...,
                to: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListAsyncQueriesResponseHttpRequest: ...
        @typing.type_check_only
        class HostStatsResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                name: str,
                accuracy: str = ...,
                envgroupHostname: str = ...,
                filter: str = ...,
                limit: str = ...,
                offset: str = ...,
                realtime: bool = ...,
                select: str = ...,
                sort: str = ...,
                sortby: str = ...,
                timeRange: str = ...,
                timeUnit: str = ...,
                topk: str = ...,
                tsAscending: bool = ...,
                tzo: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1StatsHttpRequest: ...
        @typing.type_check_only
        class InstancesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class AttachmentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1InstanceAttachment = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1InstanceAttachmentHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListInstanceAttachmentsResponseHttpRequest: ...
            @typing.type_check_only
            class CanaryevaluationsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1CanaryEvaluation = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1CanaryEvaluationHttpRequest: ...
            @typing.type_check_only
            class NatAddressesResource(googleapiclient.discovery.Resource):
                def activate(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1ActivateNatAddressRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1NatAddress = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1NatAddressHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListNatAddressesResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1Instance = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1InstanceHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListInstancesResponseHttpRequest: ...
            def reportStatus(
                self,
                *,
                instance: str,
                body: GoogleCloudApigeeV1ReportInstanceStatusRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ReportInstanceStatusResponseHttpRequest: ...
            def attachments(self) -> AttachmentsResource: ...
            def canaryevaluations(self) -> CanaryevaluationsResource: ...
            def natAddresses(self) -> NatAddressesResource: ...
        @typing.type_check_only
        class KeyvaluemapsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1KeyValueMap = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1KeyValueMapHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1KeyValueMapHttpRequest: ...
        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
        @typing.type_check_only
        class OptimizedHostStatsResource(googleapiclient.discovery.Resource):
            def get(
                self,
                *,
                name: str,
                accuracy: str = ...,
                envgroupHostname: str = ...,
                filter: str = ...,
                limit: str = ...,
                offset: str = ...,
                realtime: bool = ...,
                select: str = ...,
                sort: str = ...,
                sortby: str = ...,
                timeRange: str = ...,
                timeUnit: str = ...,
                topk: str = ...,
                tsAscending: bool = ...,
                tzo: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1OptimizedStatsHttpRequest: ...
        @typing.type_check_only
        class ReportsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1CustomReport = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1CustomReportHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DeleteCustomReportResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1CustomReportHttpRequest: ...
            def list(
                self, *, parent: str, expand: bool = ..., **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListCustomReportsResponseHttpRequest: ...
            def update(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1CustomReport = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1CustomReportHttpRequest: ...
        @typing.type_check_only
        class SharedflowsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DeploymentsResource(googleapiclient.discovery.Resource):
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...
            @typing.type_check_only
            class RevisionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class DeploymentsResource(googleapiclient.discovery.Resource):
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1SharedFlowRevisionHttpRequest: ...
                def get(
                    self, *, name: str, format: str = ..., **kwargs: typing.Any
                ) -> GoogleApiHttpBodyHttpRequest: ...
                def updateSharedFlowRevision(
                    self,
                    *,
                    name: str,
                    body: GoogleApiHttpBody = ...,
                    validate: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1SharedFlowRevisionHttpRequest: ...
                def deployments(self) -> DeploymentsResource: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleApiHttpBody = ...,
                action: str = ...,
                name: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1SharedFlowRevisionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1SharedFlowHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1SharedFlowHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                includeMetaData: bool = ...,
                includeRevisions: bool = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListSharedFlowsResponseHttpRequest: ...
            def deployments(self) -> DeploymentsResource: ...
            def revisions(self) -> RevisionsResource: ...
        @typing.type_check_only
        class SitesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ApicategoriesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1ApiCategoryData = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ApiCategoryHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ApiResponseWrapperHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ApiCategoryHttpRequest: ...
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListApiCategoriesResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1ApiCategoryData = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ApiCategoryHttpRequest: ...
            def apicategories(self) -> ApicategoriesResource: ...
        def create(
            self,
            *,
            body: GoogleCloudApigeeV1Organization = ...,
            parent: str = ...,
            **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleCloudApigeeV1OrganizationHttpRequest: ...
        def getDeployedIngressConfig(
            self,
            *,
            name: str,
            view: typing_extensions.Literal[
                "INGRESS_CONFIG_VIEW_UNSPECIFIED", "BASIC", "FULL"
            ] = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudApigeeV1IngressConfigHttpRequest: ...
        def getSyncAuthorization(
            self,
            *,
            name: str,
            body: GoogleCloudApigeeV1GetSyncAuthorizationRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudApigeeV1SyncAuthorizationHttpRequest: ...
        def list(
            self, *, parent: str, **kwargs: typing.Any
        ) -> GoogleCloudApigeeV1ListOrganizationsResponseHttpRequest: ...
        def setSyncAuthorization(
            self,
            *,
            name: str,
            body: GoogleCloudApigeeV1SyncAuthorization = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudApigeeV1SyncAuthorizationHttpRequest: ...
        def update(
            self,
            *,
            name: str,
            body: GoogleCloudApigeeV1Organization = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudApigeeV1OrganizationHttpRequest: ...
        def analytics(self) -> AnalyticsResource: ...
        def apiproducts(self) -> ApiproductsResource: ...
        def apis(self) -> ApisResource: ...
        def apps(self) -> AppsResource: ...
        def datacollectors(self) -> DatacollectorsResource: ...
        def deployments(self) -> DeploymentsResource: ...
        def developers(self) -> DevelopersResource: ...
        def envgroups(self) -> EnvgroupsResource: ...
        def environments(self) -> EnvironmentsResource: ...
        def hostQueries(self) -> HostQueriesResource: ...
        def hostStats(self) -> HostStatsResource: ...
        def instances(self) -> InstancesResource: ...
        def keyvaluemaps(self) -> KeyvaluemapsResource: ...
        def operations(self) -> OperationsResource: ...
        def optimizedHostStats(self) -> OptimizedHostStatsResource: ...
        def reports(self) -> ReportsResource: ...
        def sharedflows(self) -> SharedflowsResource: ...
        def sites(self) -> SitesResource: ...
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        def provisionOrganization(
            self,
            *,
            project: str,
            body: GoogleCloudApigeeV1ProvisionOrganizationRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
    def hybrid(self) -> HybridResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleApiHttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleApiHttpBody: ...

@typing.type_check_only
class GoogleCloudApigeeV1AliasHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1Alias: ...

@typing.type_check_only
class GoogleCloudApigeeV1ApiCategoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ApiCategory: ...

@typing.type_check_only
class GoogleCloudApigeeV1ApiProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ApiProduct: ...

@typing.type_check_only
class GoogleCloudApigeeV1ApiProxyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ApiProxy: ...

@typing.type_check_only
class GoogleCloudApigeeV1ApiProxyRevisionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ApiProxyRevision: ...

@typing.type_check_only
class GoogleCloudApigeeV1ApiResponseWrapperHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ApiResponseWrapper: ...

@typing.type_check_only
class GoogleCloudApigeeV1AppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1App: ...

@typing.type_check_only
class GoogleCloudApigeeV1AsyncQueryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1AsyncQuery: ...

@typing.type_check_only
class GoogleCloudApigeeV1AsyncQueryResultViewHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1AsyncQueryResultView: ...

@typing.type_check_only
class GoogleCloudApigeeV1AttributeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1Attribute: ...

@typing.type_check_only
class GoogleCloudApigeeV1AttributesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1Attributes: ...

@typing.type_check_only
class GoogleCloudApigeeV1CanaryEvaluationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1CanaryEvaluation: ...

@typing.type_check_only
class GoogleCloudApigeeV1CustomReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1CustomReport: ...

@typing.type_check_only
class GoogleCloudApigeeV1DataCollectorHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1DataCollector: ...

@typing.type_check_only
class GoogleCloudApigeeV1DatastoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1Datastore: ...

@typing.type_check_only
class GoogleCloudApigeeV1DebugMaskHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1DebugMask: ...

@typing.type_check_only
class GoogleCloudApigeeV1DebugSessionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1DebugSession: ...

@typing.type_check_only
class GoogleCloudApigeeV1DebugSessionTransactionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1DebugSessionTransaction: ...

@typing.type_check_only
class GoogleCloudApigeeV1DeleteCustomReportResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1DeleteCustomReportResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1DeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1Deployment: ...

@typing.type_check_only
class GoogleCloudApigeeV1DeploymentChangeReportHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1DeploymentChangeReport: ...

@typing.type_check_only
class GoogleCloudApigeeV1DeveloperHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1Developer: ...

@typing.type_check_only
class GoogleCloudApigeeV1DeveloperAppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1DeveloperApp: ...

@typing.type_check_only
class GoogleCloudApigeeV1DeveloperAppKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1DeveloperAppKey: ...

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1Environment: ...

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1EnvironmentConfig: ...

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1EnvironmentGroup: ...

@typing.type_check_only
class GoogleCloudApigeeV1EnvironmentGroupAttachmentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1EnvironmentGroupAttachment: ...

@typing.type_check_only
class GoogleCloudApigeeV1ExportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1Export: ...

@typing.type_check_only
class GoogleCloudApigeeV1FlowHookHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1FlowHook: ...

@typing.type_check_only
class GoogleCloudApigeeV1IngressConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1IngressConfig: ...

@typing.type_check_only
class GoogleCloudApigeeV1InstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1Instance: ...

@typing.type_check_only
class GoogleCloudApigeeV1InstanceAttachmentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1InstanceAttachment: ...

@typing.type_check_only
class GoogleCloudApigeeV1KeyValueMapHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1KeyValueMap: ...

@typing.type_check_only
class GoogleCloudApigeeV1KeystoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1Keystore: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListApiCategoriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListApiCategoriesResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListApiProductsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListApiProductsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListApiProxiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListApiProxiesResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListAppsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListAppsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListAsyncQueriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListAsyncQueriesResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListCustomReportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListCustomReportsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListDataCollectorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListDataCollectorsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListDatastoresResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListDatastoresResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListDebugSessionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListDebugSessionsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListDeploymentsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListDeveloperAppsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListDeveloperAppsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListEnvironmentGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListEnvironmentGroupsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListEnvironmentResourcesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListEnvironmentResourcesResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListExportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListExportsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListHybridIssuersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListHybridIssuersResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListInstanceAttachmentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListInstanceAttachmentsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListInstancesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListInstancesResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListNatAddressesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListNatAddressesResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListOfDevelopersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListOfDevelopersResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListOrganizationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListOrganizationsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListSharedFlowsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListSharedFlowsResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ListTraceConfigOverridesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ListTraceConfigOverridesResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1NatAddressHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1NatAddress: ...

@typing.type_check_only
class GoogleCloudApigeeV1OptimizedStatsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1OptimizedStats: ...

@typing.type_check_only
class GoogleCloudApigeeV1OrganizationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1Organization: ...

@typing.type_check_only
class GoogleCloudApigeeV1ReferenceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1Reference: ...

@typing.type_check_only
class GoogleCloudApigeeV1ReportInstanceStatusResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ReportInstanceStatusResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1ResourceFileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1ResourceFile: ...

@typing.type_check_only
class GoogleCloudApigeeV1SchemaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1Schema: ...

@typing.type_check_only
class GoogleCloudApigeeV1SharedFlowHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1SharedFlow: ...

@typing.type_check_only
class GoogleCloudApigeeV1SharedFlowRevisionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1SharedFlowRevision: ...

@typing.type_check_only
class GoogleCloudApigeeV1StatsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1Stats: ...

@typing.type_check_only
class GoogleCloudApigeeV1SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1Subscription: ...

@typing.type_check_only
class GoogleCloudApigeeV1SyncAuthorizationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1SyncAuthorization: ...

@typing.type_check_only
class GoogleCloudApigeeV1TargetServerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1TargetServer: ...

@typing.type_check_only
class GoogleCloudApigeeV1TestDatastoreResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1TestDatastoreResponse: ...

@typing.type_check_only
class GoogleCloudApigeeV1TraceConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1TraceConfig: ...

@typing.type_check_only
class GoogleCloudApigeeV1TraceConfigOverrideHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleCloudApigeeV1TraceConfigOverride: ...

@typing.type_check_only
class GoogleIamV1PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleIamV1Policy: ...

@typing.type_check_only
class GoogleIamV1TestIamPermissionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleIamV1TestIamPermissionsResponse: ...

@typing.type_check_only
class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningOperation: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...

import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class ApigeeResource(googleapiclient.discovery.Resource):
    class OrganizationsResource(googleapiclient.discovery.Resource):
        class EnvironmentsResource(googleapiclient.discovery.Resource):
            class KeystoresResource(googleapiclient.discovery.Resource):
                class AliasesResource(googleapiclient.discovery.Resource):
                    def csr(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleApiHttpBodyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1AliasHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1AliasHttpRequest: ...
                    def update(
                        self,
                        *,
                        name: str,
                        body: GoogleApiHttpBody = ...,
                        ignoreNewlineValidation: bool = ...,
                        ignoreExpiryValidation: bool = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1AliasHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleApiHttpBody = ...,
                        ignoreExpiryValidation: bool = ...,
                        alias: str = ...,
                        ignoreNewlineValidation: bool = ...,
                        format: str = ...,
                        x_password: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1AliasHttpRequest: ...
                    def getCertificate(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleApiHttpBodyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1KeystoreHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1KeystoreHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1Keystore = ...,
                    name: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1KeystoreHttpRequest: ...
                def aliases(self) -> AliasesResource: ...
            class ResourcefilesResource(googleapiclient.discovery.Resource):
                def listEnvironmentResources(
                    self, *, parent: str, type: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListEnvironmentResourcesResponseHttpRequest: ...
                def get(
                    self, *, parent: str, type: str, name: str, **kwargs: typing.Any
                ) -> GoogleApiHttpBodyHttpRequest: ...
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
                def update(
                    self,
                    *,
                    parent: str,
                    type: str,
                    name: str,
                    body: GoogleApiHttpBody = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ResourceFileHttpRequest: ...
                def list(
                    self, *, parent: str, type: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListEnvironmentResourcesResponseHttpRequest: ...
            class ReferencesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1Reference = ...,
                    **kwargs: typing.Any
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
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ReferenceHttpRequest: ...
            class QueriesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AsyncQueryHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1Query = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AsyncQueryHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    submittedBy: str = ...,
                    dataset: str = ...,
                    to: str = ...,
                    inclQueriesWithoutReport: str = ...,
                    status: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListAsyncQueriesResponseHttpRequest: ...
                def getResult(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleApiHttpBodyHttpRequest: ...
            class AnalyticsResource(googleapiclient.discovery.Resource):
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
                class AdminResource(googleapiclient.discovery.Resource):
                    def getSchemav2(
                        self, *, name: str, type: str = ..., **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1SchemaHttpRequest: ...
                def exports(self) -> ExportsResource: ...
                def admin(self) -> AdminResource: ...
            class StatsResource(googleapiclient.discovery.Resource):
                def get(
                    self,
                    *,
                    name: str,
                    sort: str = ...,
                    select: str = ...,
                    aggTable: str = ...,
                    realtime: bool = ...,
                    filter: str = ...,
                    timeRange: str = ...,
                    accuracy: str = ...,
                    sortby: str = ...,
                    tsAscending: bool = ...,
                    sonar: bool = ...,
                    limit: str = ...,
                    tzo: str = ...,
                    topk: str = ...,
                    timeUnit: str = ...,
                    offset: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1StatsHttpRequest: ...
            class FlowhooksResource(googleapiclient.discovery.Resource):
                def attachSharedFlowToFlowHook(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1FlowHook = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1FlowHookHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1FlowHookHttpRequest: ...
                def detachSharedFlowFromFlowHook(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1FlowHookHttpRequest: ...
            class ApisResource(googleapiclient.discovery.Resource):
                class RevisionsResource(googleapiclient.discovery.Resource):
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
                    class DebugsessionsResource(googleapiclient.discovery.Resource):
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
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudApigeeV1DebugSessionHttpRequest: ...
                        def deleteData(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageToken: str = ...,
                            pageSize: int = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudApigeeV1ListDebugSessionsResponseHttpRequest: ...
                        def data(self) -> DataResource: ...
                    def undeploy(
                        self,
                        *,
                        name: str,
                        sequencedRollout: bool = ...,
                        **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
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
                    def deployments(self) -> DeploymentsResource: ...
                    def debugsessions(self) -> DebugsessionsResource: ...
                class DeploymentsResource(googleapiclient.discovery.Resource):
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...
                def revisions(self) -> RevisionsResource: ...
                def deployments(self) -> DeploymentsResource: ...
            class OptimizedStatsResource(googleapiclient.discovery.Resource):
                def get(
                    self,
                    *,
                    name: str,
                    select: str = ...,
                    offset: str = ...,
                    timeRange: str = ...,
                    tzo: str = ...,
                    tsAscending: bool = ...,
                    filter: str = ...,
                    realtime: bool = ...,
                    timeUnit: str = ...,
                    sonar: bool = ...,
                    sortby: str = ...,
                    aggTable: str = ...,
                    accuracy: str = ...,
                    topk: str = ...,
                    limit: str = ...,
                    sort: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1OptimizedStatsHttpRequest: ...
            class CachesResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
            class TargetserversResource(googleapiclient.discovery.Resource):
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
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1TargetServerHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1TargetServer = ...,
                    name: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1TargetServerHttpRequest: ...
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
            class SharedflowsResource(googleapiclient.discovery.Resource):
                class DeploymentsResource(googleapiclient.discovery.Resource):
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...
                class RevisionsResource(googleapiclient.discovery.Resource):
                    def getDeployments(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1DeploymentHttpRequest: ...
                    def deploy(
                        self, *, name: str, override: bool = ..., **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1DeploymentHttpRequest: ...
                    def undeploy(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobufEmptyHttpRequest: ...
                def deployments(self) -> DeploymentsResource: ...
                def revisions(self) -> RevisionsResource: ...
            class DeploymentsResource(googleapiclient.discovery.Resource):
                def list(
                    self, *, parent: str, sharedFlows: bool = ..., **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                options_requestedPolicyVersion: int = ...,
                **kwargs: typing.Any
            ) -> GoogleIamV1PolicyHttpRequest: ...
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
            def getDebugmask(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DebugMaskHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: GoogleIamV1TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleIamV1TestIamPermissionsResponseHttpRequest: ...
            def getDeployedConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1EnvironmentConfigHttpRequest: ...
            def subscribe(
                self, *, parent: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1SubscriptionHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: GoogleIamV1SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleIamV1PolicyHttpRequest: ...
            def unsubscribe(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1Subscription = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1Environment = ...,
                name: str = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1EnvironmentHttpRequest: ...
            def updateEnvironment(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1Environment = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1EnvironmentHttpRequest: ...
            def keystores(self) -> KeystoresResource: ...
            def resourcefiles(self) -> ResourcefilesResource: ...
            def references(self) -> ReferencesResource: ...
            def queries(self) -> QueriesResource: ...
            def analytics(self) -> AnalyticsResource: ...
            def stats(self) -> StatsResource: ...
            def flowhooks(self) -> FlowhooksResource: ...
            def apis(self) -> ApisResource: ...
            def optimizedStats(self) -> OptimizedStatsResource: ...
            def caches(self) -> CachesResource: ...
            def targetservers(self) -> TargetserversResource: ...
            def keyvaluemaps(self) -> KeyvaluemapsResource: ...
            def sharedflows(self) -> SharedflowsResource: ...
            def deployments(self) -> DeploymentsResource: ...
        class InstancesResource(googleapiclient.discovery.Resource):
            class AttachmentsResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListInstanceAttachmentsResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1InstanceAttachment = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1InstanceAttachmentHttpRequest: ...
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
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1Instance = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def reportStatus(
                self,
                *,
                instance: str,
                body: GoogleCloudApigeeV1ReportInstanceStatusRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ReportInstanceStatusResponseHttpRequest: ...
            def attachments(self) -> AttachmentsResource: ...
        class ReportsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DeleteCustomReportResponseHttpRequest: ...
            def list(
                self, *, parent: str, expand: bool = ..., **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListCustomReportsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1CustomReportHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1CustomReport = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1CustomReportHttpRequest: ...
            def update(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1CustomReport = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1CustomReportHttpRequest: ...
        class AppsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1AppHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                expand: bool = ...,
                status: str = ...,
                ids: str = ...,
                keyStatus: str = ...,
                apptype: str = ...,
                startKey: str = ...,
                apiProduct: str = ...,
                includeCred: bool = ...,
                rows: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListAppsResponseHttpRequest: ...
        class DevelopersResource(googleapiclient.discovery.Resource):
            class AttributesResource(googleapiclient.discovery.Resource):
                def updateDeveloperAttribute(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1Attribute = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributesHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
            class AppsResource(googleapiclient.discovery.Resource):
                class AttributesResource(googleapiclient.discovery.Resource):
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
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
                class KeysResource(googleapiclient.discovery.Resource):
                    class CreateResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: GoogleCloudApigeeV1DeveloperAppKey = ...,
                            **kwargs: typing.Any
                        ) -> GoogleCloudApigeeV1DeveloperAppKeyHttpRequest: ...
                    class ApiproductsResource(googleapiclient.discovery.Resource):
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> GoogleCloudApigeeV1DeveloperAppKeyHttpRequest: ...
                        def updateDeveloperAppKeyApiProduct(
                            self, *, name: str, action: str = ..., **kwargs: typing.Any
                        ) -> GoogleProtobufEmptyHttpRequest: ...
                    def replaceDeveloperAppKey(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudApigeeV1DeveloperAppKey = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1DeveloperAppKeyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1DeveloperAppKeyHttpRequest: ...
                    def updateDeveloperAppKey(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudApigeeV1DeveloperAppKey = ...,
                        action: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1DeveloperAppKeyHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1DeveloperAppKeyHttpRequest: ...
                    def create(self) -> CreateResource: ...
                    def apiproducts(self) -> ApiproductsResource: ...
                def list(
                    self,
                    *,
                    parent: str,
                    count: str = ...,
                    shallowExpand: bool = ...,
                    startKey: str = ...,
                    expand: bool = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListDeveloperAppsResponseHttpRequest: ...
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
                def update(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1DeveloperApp = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1DeveloperAppHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    query: str = ...,
                    entity: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1DeveloperAppHttpRequest: ...
                def attributes(self) -> AttributesResource: ...
                def keys(self) -> KeysResource: ...
            def setDeveloperStatus(
                self, *, name: str, action: str = ..., **kwargs: typing.Any
            ) -> GoogleProtobufEmptyHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DeveloperHttpRequest: ...
            def update(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1Developer = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DeveloperHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1Developer = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DeveloperHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                includeCompany: bool = ...,
                expand: bool = ...,
                ids: str = ...,
                startKey: str = ...,
                count: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListOfDevelopersResponseHttpRequest: ...
            def get(
                self, *, name: str, action: str = ..., **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1DeveloperHttpRequest: ...
            def attributes(self) -> AttributesResource: ...
            def apps(self) -> AppsResource: ...
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
        class ApiproductsResource(googleapiclient.discovery.Resource):
            class AttributesResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
                def updateApiProductAttribute(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1Attribute = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributeHttpRequest: ...
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1AttributesHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ApiProductHttpRequest: ...
            def update(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1ApiProduct = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ApiProductHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                expand: bool = ...,
                attributevalue: str = ...,
                count: str = ...,
                attributename: str = ...,
                startKey: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListApiProductsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ApiProductHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1ApiProduct = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ApiProductHttpRequest: ...
            def attributes(self) -> AttributesResource: ...
        class OperationsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                name: str,
                pageToken: str = ...,
                filter: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningListOperationsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
        class SharedflowsResource(googleapiclient.discovery.Resource):
            class DeploymentsResource(googleapiclient.discovery.Resource):
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...
            class RevisionsResource(googleapiclient.discovery.Resource):
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
            def list(
                self,
                *,
                parent: str,
                includeMetaData: bool = ...,
                includeRevisions: bool = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListSharedFlowsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1SharedFlowHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1SharedFlowHttpRequest: ...
            def deployments(self) -> DeploymentsResource: ...
            def revisions(self) -> RevisionsResource: ...
        class EnvgroupsResource(googleapiclient.discovery.Resource):
            class AttachmentsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1EnvironmentGroupAttachment = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponseHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunningOperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1EnvironmentGroupAttachmentHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudApigeeV1EnvironmentGroup = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListEnvironmentGroupsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1EnvironmentGroupHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudApigeeV1EnvironmentGroup = ...,
                name: str = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def attachments(self) -> AttachmentsResource: ...
        class DeploymentsResource(googleapiclient.discovery.Resource):
            def list(
                self, *, parent: str, sharedFlows: bool = ..., **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...
        class ApisResource(googleapiclient.discovery.Resource):
            class RevisionsResource(googleapiclient.discovery.Resource):
                class DeploymentsResource(googleapiclient.discovery.Resource):
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...
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
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ApiProxyRevisionHttpRequest: ...
                def deployments(self) -> DeploymentsResource: ...
            class DeploymentsResource(googleapiclient.discovery.Resource):
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest: ...
            class KeyvaluemapsResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1KeyValueMapHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1KeyValueMap = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1KeyValueMapHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ApiProxyHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleApiHttpBody = ...,
                validate: bool = ...,
                name: str = ...,
                action: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ApiProxyRevisionHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ApiProxyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                includeRevisions: bool = ...,
                includeMetaData: bool = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListApiProxiesResponseHttpRequest: ...
            def revisions(self) -> RevisionsResource: ...
            def deployments(self) -> DeploymentsResource: ...
            def keyvaluemaps(self) -> KeyvaluemapsResource: ...
        class AnalyticsResource(googleapiclient.discovery.Resource):
            class DatastoresResource(googleapiclient.discovery.Resource):
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def test(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1Datastore = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1TestDatastoreResponseHttpRequest: ...
                def list(
                    self, *, parent: str, targetType: str = ..., **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1ListDatastoresResponseHttpRequest: ...
                def update(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudApigeeV1Datastore = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1DatastoreHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1DatastoreHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudApigeeV1Datastore = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudApigeeV1DatastoreHttpRequest: ...
            def datastores(self) -> DatastoresResource: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleCloudApigeeV1OrganizationHttpRequest: ...
        def getDeployedIngressConfig(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleCloudApigeeV1IngressConfigHttpRequest: ...
        def setSyncAuthorization(
            self,
            *,
            name: str,
            body: GoogleCloudApigeeV1SyncAuthorization = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudApigeeV1SyncAuthorizationHttpRequest: ...
        def list(
            self, *, parent: str, **kwargs: typing.Any
        ) -> GoogleCloudApigeeV1ListOrganizationsResponseHttpRequest: ...
        def update(
            self,
            *,
            name: str,
            body: GoogleCloudApigeeV1Organization = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudApigeeV1OrganizationHttpRequest: ...
        def create(
            self,
            *,
            body: GoogleCloudApigeeV1Organization = ...,
            parent: str = ...,
            **kwargs: typing.Any
        ) -> GoogleLongrunningOperationHttpRequest: ...
        def getSyncAuthorization(
            self,
            *,
            name: str,
            body: GoogleCloudApigeeV1GetSyncAuthorizationRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudApigeeV1SyncAuthorizationHttpRequest: ...
        def environments(self) -> EnvironmentsResource: ...
        def instances(self) -> InstancesResource: ...
        def reports(self) -> ReportsResource: ...
        def apps(self) -> AppsResource: ...
        def developers(self) -> DevelopersResource: ...
        def keyvaluemaps(self) -> KeyvaluemapsResource: ...
        def apiproducts(self) -> ApiproductsResource: ...
        def operations(self) -> OperationsResource: ...
        def sharedflows(self) -> SharedflowsResource: ...
        def envgroups(self) -> EnvgroupsResource: ...
        def deployments(self) -> DeploymentsResource: ...
        def apis(self) -> ApisResource: ...
        def analytics(self) -> AnalyticsResource: ...
    class HybridResource(googleapiclient.discovery.Resource):
        class IssuersResource(googleapiclient.discovery.Resource):
            def list(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudApigeeV1ListHybridIssuersResponseHttpRequest: ...
        def issuers(self) -> IssuersResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def hybrid(self) -> HybridResource: ...

class GoogleCloudApigeeV1ResourceFileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ResourceFile: ...

class GoogleCloudApigeeV1AsyncQueryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1AsyncQuery: ...

class GoogleCloudApigeeV1ExportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1Export: ...

class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleProtobufEmpty: ...

class GoogleCloudApigeeV1AttributeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1Attribute: ...

class GoogleCloudApigeeV1EnvironmentConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1EnvironmentConfig: ...

class GoogleCloudApigeeV1InstanceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1Instance: ...

class GoogleCloudApigeeV1OptimizedStatsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1OptimizedStats: ...

class GoogleCloudApigeeV1SharedFlowRevisionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1SharedFlowRevision: ...

class GoogleCloudApigeeV1OrganizationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1Organization: ...

class GoogleCloudApigeeV1ListSharedFlowsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ListSharedFlowsResponse: ...

class GoogleCloudApigeeV1ReportInstanceStatusResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ReportInstanceStatusResponse: ...

class GoogleCloudApigeeV1DebugMaskHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1DebugMask: ...

class GoogleCloudApigeeV1DatastoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1Datastore: ...

class GoogleCloudApigeeV1DeleteCustomReportResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1DeleteCustomReportResponse: ...

class GoogleCloudApigeeV1KeystoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1Keystore: ...

class GoogleCloudApigeeV1ListDeploymentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ListDeploymentsResponse: ...

class GoogleCloudApigeeV1CustomReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1CustomReport: ...

class GoogleCloudApigeeV1IngressConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1IngressConfig: ...

class GoogleCloudApigeeV1EnvironmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1Environment: ...

class GoogleCloudApigeeV1ListInstancesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ListInstancesResponse: ...

class GoogleCloudApigeeV1ListDatastoresResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ListDatastoresResponse: ...

class GoogleCloudApigeeV1DeploymentChangeReportHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1DeploymentChangeReport: ...

class GoogleCloudApigeeV1ListAppsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ListAppsResponse: ...

class GoogleCloudApigeeV1ListDebugSessionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ListDebugSessionsResponse: ...

class GoogleApiHttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleApiHttpBody: ...

class GoogleCloudApigeeV1ListHybridIssuersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ListHybridIssuersResponse: ...

class GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ListEnvironmentGroupAttachmentsResponse: ...

class GoogleCloudApigeeV1ApiProxyRevisionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ApiProxyRevision: ...

class GoogleCloudApigeeV1KeyValueMapHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1KeyValueMap: ...

class GoogleCloudApigeeV1ListExportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ListExportsResponse: ...

class GoogleCloudApigeeV1ReferenceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1Reference: ...

class GoogleCloudApigeeV1SharedFlowHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1SharedFlow: ...

class GoogleCloudApigeeV1AppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1App: ...

class GoogleCloudApigeeV1ListCustomReportsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ListCustomReportsResponse: ...

class GoogleCloudApigeeV1AliasHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1Alias: ...

class GoogleCloudApigeeV1SubscriptionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1Subscription: ...

class GoogleCloudApigeeV1AttributesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1Attributes: ...

class GoogleCloudApigeeV1ApiProxyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ApiProxy: ...

class GoogleCloudApigeeV1SyncAuthorizationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1SyncAuthorization: ...

class GoogleCloudApigeeV1ListInstanceAttachmentsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ListInstanceAttachmentsResponse: ...

class GoogleCloudApigeeV1DeploymentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1Deployment: ...

class GoogleCloudApigeeV1ListDeveloperAppsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ListDeveloperAppsResponse: ...

class GoogleCloudApigeeV1TestDatastoreResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1TestDatastoreResponse: ...

class GoogleIamV1PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleIamV1Policy: ...

class GoogleCloudApigeeV1SchemaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1Schema: ...

class GoogleCloudApigeeV1ListOfDevelopersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ListOfDevelopersResponse: ...

class GoogleCloudApigeeV1EnvironmentGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1EnvironmentGroup: ...

class GoogleCloudApigeeV1ListEnvironmentResourcesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ListEnvironmentResourcesResponse: ...

class GoogleIamV1TestIamPermissionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleIamV1TestIamPermissionsResponse: ...

class GoogleCloudApigeeV1TargetServerHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1TargetServer: ...

class GoogleCloudApigeeV1DeveloperAppKeyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1DeveloperAppKey: ...

class GoogleCloudApigeeV1ListOrganizationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ListOrganizationsResponse: ...

class GoogleCloudApigeeV1DeveloperAppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1DeveloperApp: ...

class GoogleCloudApigeeV1ApiProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ApiProduct: ...

class GoogleLongrunningListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunningListOperationsResponse: ...

class GoogleCloudApigeeV1ListApiProductsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ListApiProductsResponse: ...

class GoogleCloudApigeeV1DebugSessionTransactionHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1DebugSessionTransaction: ...

class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunningOperation: ...

class GoogleCloudApigeeV1InstanceAttachmentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1InstanceAttachment: ...

class GoogleCloudApigeeV1ListApiProxiesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ListApiProxiesResponse: ...

class GoogleCloudApigeeV1FlowHookHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1FlowHook: ...

class GoogleCloudApigeeV1StatsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1Stats: ...

class GoogleCloudApigeeV1DebugSessionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1DebugSession: ...

class GoogleCloudApigeeV1ListEnvironmentGroupsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ListEnvironmentGroupsResponse: ...

class GoogleCloudApigeeV1DeveloperHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1Developer: ...

class GoogleCloudApigeeV1ListAsyncQueriesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1ListAsyncQueriesResponse: ...

class GoogleCloudApigeeV1EnvironmentGroupAttachmentHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudApigeeV1EnvironmentGroupAttachment: ...

import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudHealthcareResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            class DatasetsResource(googleapiclient.discovery.Resource):
                class FhirStoresResource(googleapiclient.discovery.Resource):
                    class FhirResource(googleapiclient.discovery.Resource):
                        def search(
                            self,
                            *,
                            parent: str,
                            body: SearchResourcesRequest = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def ConceptMap_translate(
                            self,
                            *,
                            name: str,
                            code: str = ...,
                            conceptMapVersion: str = ...,
                            system: str = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def Patient_everything(
                            self,
                            *,
                            name: str,
                            x_type: str = ...,
                            end: str = ...,
                            x_page_token: str = ...,
                            x_since: str = ...,
                            start: str = ...,
                            x_count: int = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def Resource_purge(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def conditionalDelete(
                            self, *, parent: str, type: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            type: str,
                            body: HttpBody = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def vread(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def conditionalUpdate(
                            self,
                            *,
                            parent: str,
                            type: str,
                            body: HttpBody = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def executeBundle(
                            self,
                            *,
                            parent: str,
                            body: HttpBody = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: HttpBody = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def conditionalPatch(
                            self,
                            *,
                            parent: str,
                            type: str,
                            body: HttpBody = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def history(
                            self,
                            *,
                            name: str,
                            x_count: int = ...,
                            x_page_token: str = ...,
                            x_since: str = ...,
                            x_at: str = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def capabilities(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def update(
                            self,
                            *,
                            name: str,
                            body: HttpBody = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def read(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def Observation_lastn(
                            self, *, parent: str, **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def ConceptMap_search_translate(
                            self,
                            *,
                            parent: str,
                            target: str = ...,
                            url: str = ...,
                            source: str = ...,
                            code: str = ...,
                            conceptMapVersion: str = ...,
                            system: str = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                    def deidentify(
                        self,
                        *,
                        sourceStore: str,
                        body: DeidentifyFhirStoreRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> FhirStoreHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: FhirStore = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> FhirStoreHttpRequest: ...
                    def import_(
                        self,
                        *,
                        name: str,
                        body: ImportResourcesRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: FhirStore = ...,
                        fhirStoreId: str = ...,
                        **kwargs: typing.Any
                    ) -> FhirStoreHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageToken: str = ...,
                        filter: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> ListFhirStoresResponseHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> TestIamPermissionsResponseHttpRequest: ...
                    def export(
                        self,
                        *,
                        name: str,
                        body: ExportResourcesRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def fhir(self) -> FhirResource: ...
                class OperationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def cancel(
                        self,
                        *,
                        name: str,
                        body: CancelOperationRequest = ...,
                        **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def list(
                        self,
                        *,
                        name: str,
                        filter: str = ...,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> ListOperationsResponseHttpRequest: ...
                class DicomStoresResource(googleapiclient.discovery.Resource):
                    class StudiesResource(googleapiclient.discovery.Resource):
                        class SeriesResource(googleapiclient.discovery.Resource):
                            class InstancesResource(googleapiclient.discovery.Resource):
                                class FramesResource(
                                    googleapiclient.discovery.Resource
                                ):
                                    def retrieveFrames(
                                        self,
                                        *,
                                        parent: str,
                                        dicomWebPath: str,
                                        **kwargs: typing.Any
                                    ) -> HttpBodyHttpRequest: ...
                                    def retrieveRendered(
                                        self,
                                        *,
                                        parent: str,
                                        dicomWebPath: str,
                                        **kwargs: typing.Any
                                    ) -> HttpBodyHttpRequest: ...
                                def retrieveRendered(
                                    self,
                                    *,
                                    parent: str,
                                    dicomWebPath: str,
                                    **kwargs: typing.Any
                                ) -> HttpBodyHttpRequest: ...
                                def retrieveMetadata(
                                    self,
                                    *,
                                    parent: str,
                                    dicomWebPath: str,
                                    **kwargs: typing.Any
                                ) -> HttpBodyHttpRequest: ...
                                def delete(
                                    self,
                                    *,
                                    parent: str,
                                    dicomWebPath: str,
                                    **kwargs: typing.Any
                                ) -> EmptyHttpRequest: ...
                                def retrieveInstance(
                                    self,
                                    *,
                                    parent: str,
                                    dicomWebPath: str,
                                    **kwargs: typing.Any
                                ) -> HttpBodyHttpRequest: ...
                                def frames(self) -> FramesResource: ...
                            def delete(
                                self,
                                *,
                                parent: str,
                                dicomWebPath: str,
                                **kwargs: typing.Any
                            ) -> EmptyHttpRequest: ...
                            def searchForInstances(
                                self,
                                *,
                                parent: str,
                                dicomWebPath: str,
                                **kwargs: typing.Any
                            ) -> HttpBodyHttpRequest: ...
                            def retrieveMetadata(
                                self,
                                *,
                                parent: str,
                                dicomWebPath: str,
                                **kwargs: typing.Any
                            ) -> HttpBodyHttpRequest: ...
                            def retrieveSeries(
                                self,
                                *,
                                parent: str,
                                dicomWebPath: str,
                                **kwargs: typing.Any
                            ) -> HttpBodyHttpRequest: ...
                            def instances(self) -> InstancesResource: ...
                        def searchForInstances(
                            self,
                            *,
                            parent: str,
                            dicomWebPath: str,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def retrieveMetadata(
                            self,
                            *,
                            parent: str,
                            dicomWebPath: str,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def delete(
                            self,
                            *,
                            parent: str,
                            dicomWebPath: str,
                            **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def searchForSeries(
                            self,
                            *,
                            parent: str,
                            dicomWebPath: str,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def storeInstances(
                            self,
                            *,
                            parent: str,
                            dicomWebPath: str,
                            body: HttpBody = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def retrieveStudy(
                            self,
                            *,
                            parent: str,
                            dicomWebPath: str,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def series(self) -> SeriesResource: ...
                    def import_(
                        self,
                        *,
                        name: str,
                        body: ImportDicomDataRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def searchForStudies(
                        self, *, parent: str, dicomWebPath: str, **kwargs: typing.Any
                    ) -> HttpBodyHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def searchForInstances(
                        self, *, parent: str, dicomWebPath: str, **kwargs: typing.Any
                    ) -> HttpBodyHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> DicomStoreHttpRequest: ...
                    def searchForSeries(
                        self, *, parent: str, dicomWebPath: str, **kwargs: typing.Any
                    ) -> HttpBodyHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> TestIamPermissionsResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: DicomStore = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> DicomStoreHttpRequest: ...
                    def export(
                        self,
                        *,
                        name: str,
                        body: ExportDicomDataRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListDicomStoresResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: DicomStore = ...,
                        dicomStoreId: str = ...,
                        **kwargs: typing.Any
                    ) -> DicomStoreHttpRequest: ...
                    def deidentify(
                        self,
                        *,
                        sourceStore: str,
                        body: DeidentifyDicomStoreRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def storeInstances(
                        self,
                        *,
                        parent: str,
                        dicomWebPath: str,
                        body: HttpBody = ...,
                        **kwargs: typing.Any
                    ) -> HttpBodyHttpRequest: ...
                    def studies(self) -> StudiesResource: ...
                class AnnotationStoresResource(googleapiclient.discovery.Resource):
                    class AnnotationsResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> AnnotationHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageToken: str = ...,
                            filter: str = ...,
                            pageSize: int = ...,
                            view: typing_extensions.Literal[
                                "ANNOTATION_VIEW_UNSPECIFIED",
                                "ANNOTATION_VIEW_BASIC",
                                "ANNOTATION_VIEW_FULL",
                            ] = ...,
                            **kwargs: typing.Any
                        ) -> ListAnnotationsResponseHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: Annotation = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> AnnotationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: Annotation = ...,
                            **kwargs: typing.Any
                        ) -> AnnotationHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: AnnotationStore = ...,
                        annotationStoreId: str = ...,
                        **kwargs: typing.Any
                    ) -> AnnotationStoreHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: AnnotationStore = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> AnnotationStoreHttpRequest: ...
                    def evaluate(
                        self,
                        *,
                        evalStore: str,
                        body: EvaluateAnnotationStoreRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        filter: str = ...,
                        **kwargs: typing.Any
                    ) -> ListAnnotationStoresResponseHttpRequest: ...
                    def import_(
                        self,
                        *,
                        annotationStore: str,
                        body: ImportAnnotationsRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> TestIamPermissionsResponseHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> AnnotationStoreHttpRequest: ...
                    def export(
                        self,
                        *,
                        annotationStore: str,
                        body: ExportAnnotationsRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def annotations(self) -> AnnotationsResource: ...
                class ConsentStoresResource(googleapiclient.discovery.Resource):
                    class ConsentArtifactsResource(googleapiclient.discovery.Resource):
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> ConsentArtifactHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: ConsentArtifact = ...,
                            **kwargs: typing.Any
                        ) -> ConsentArtifactHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageToken: str = ...,
                            pageSize: int = ...,
                            filter: str = ...,
                            **kwargs: typing.Any
                        ) -> ListConsentArtifactsResponseHttpRequest: ...
                    class AttributeDefinitionsResource(
                        googleapiclient.discovery.Resource
                    ):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> AttributeDefinitionHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: AttributeDefinition = ...,
                            attributeDefinitionId: str = ...,
                            **kwargs: typing.Any
                        ) -> AttributeDefinitionHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageToken: str = ...,
                            pageSize: int = ...,
                            filter: str = ...,
                            **kwargs: typing.Any
                        ) -> ListAttributeDefinitionsResponseHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: AttributeDefinition = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> AttributeDefinitionHttpRequest: ...
                    class UserDataMappingsResource(googleapiclient.discovery.Resource):
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> UserDataMappingHttpRequest: ...
                        def archive(
                            self,
                            *,
                            name: str,
                            body: ArchiveUserDataMappingRequest = ...,
                            **kwargs: typing.Any
                        ) -> ArchiveUserDataMappingResponseHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageToken: str = ...,
                            pageSize: int = ...,
                            **kwargs: typing.Any
                        ) -> ListUserDataMappingsResponseHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: UserDataMapping = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> UserDataMappingHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: UserDataMapping = ...,
                            **kwargs: typing.Any
                        ) -> UserDataMappingHttpRequest: ...
                    class ConsentsResource(googleapiclient.discovery.Resource):
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            filter: str = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListConsentsResponseHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: Consent = ...,
                            **kwargs: typing.Any
                        ) -> ConsentHttpRequest: ...
                        def reject(
                            self,
                            *,
                            name: str,
                            body: RejectConsentRequest = ...,
                            **kwargs: typing.Any
                        ) -> ConsentHttpRequest: ...
                        def revoke(
                            self,
                            *,
                            name: str,
                            body: RevokeConsentRequest = ...,
                            **kwargs: typing.Any
                        ) -> ConsentHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> ConsentHttpRequest: ...
                        def deleteRevision(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def listRevisions(
                            self,
                            *,
                            name: str,
                            pageToken: str = ...,
                            filter: str = ...,
                            pageSize: int = ...,
                            **kwargs: typing.Any
                        ) -> ListConsentRevisionsResponseHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: Consent = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> ConsentHttpRequest: ...
                        def activate(
                            self,
                            *,
                            name: str,
                            body: ActivateConsentRequest = ...,
                            **kwargs: typing.Any
                        ) -> ConsentHttpRequest: ...
                    def checkDataAccess(
                        self,
                        *,
                        consentStore: str,
                        body: CheckDataAccessRequest = ...,
                        **kwargs: typing.Any
                    ) -> CheckDataAccessResponseHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: ConsentStore = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> ConsentStoreHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> ListConsentStoresResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: ConsentStore = ...,
                        consentStoreId: str = ...,
                        **kwargs: typing.Any
                    ) -> ConsentStoreHttpRequest: ...
                    def evaluateUserConsents(
                        self,
                        *,
                        consentStore: str,
                        body: EvaluateUserConsentsRequest = ...,
                        **kwargs: typing.Any
                    ) -> EvaluateUserConsentsResponseHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def queryAccessibleData(
                        self,
                        *,
                        consentStore: str,
                        body: QueryAccessibleDataRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> TestIamPermissionsResponseHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ConsentStoreHttpRequest: ...
                    def consentArtifacts(self) -> ConsentArtifactsResource: ...
                    def attributeDefinitions(self) -> AttributeDefinitionsResource: ...
                    def userDataMappings(self) -> UserDataMappingsResource: ...
                    def consents(self) -> ConsentsResource: ...
                class Hl7V2StoresResource(googleapiclient.discovery.Resource):
                    class MessagesResource(googleapiclient.discovery.Resource):
                        def ingest(
                            self,
                            *,
                            parent: str,
                            body: IngestMessageRequest = ...,
                            **kwargs: typing.Any
                        ) -> IngestMessageResponseHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageToken: str = ...,
                            pageSize: int = ...,
                            filter: str = ...,
                            orderBy: str = ...,
                            view: typing_extensions.Literal[
                                "MESSAGE_VIEW_UNSPECIFIED",
                                "RAW_ONLY",
                                "PARSED_ONLY",
                                "FULL",
                                "SCHEMATIZED_ONLY",
                                "BASIC",
                            ] = ...,
                            **kwargs: typing.Any
                        ) -> ListMessagesResponseHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: Message = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> MessageHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: CreateMessageRequest = ...,
                            **kwargs: typing.Any
                        ) -> MessageHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            view: typing_extensions.Literal[
                                "MESSAGE_VIEW_UNSPECIFIED",
                                "RAW_ONLY",
                                "PARSED_ONLY",
                                "FULL",
                                "SCHEMATIZED_ONLY",
                                "BASIC",
                            ] = ...,
                            **kwargs: typing.Any
                        ) -> MessageHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Hl7V2Store = ...,
                        hl7V2StoreId: str = ...,
                        **kwargs: typing.Any
                    ) -> Hl7V2StoreHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> TestIamPermissionsResponseHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        filter: str = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListHl7V2StoresResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Hl7V2Store = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> Hl7V2StoreHttpRequest: ...
                    def import_(
                        self,
                        *,
                        name: str,
                        body: ImportMessagesRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> Hl7V2StoreHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def messages(self) -> MessagesResource: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Dataset = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> DatasetHttpRequest: ...
                def deidentify(
                    self,
                    *,
                    sourceDataset: str,
                    body: DeidentifyDatasetRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: Dataset = ...,
                    datasetId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DatasetHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListDatasetsResponseHttpRequest: ...
                def fhirStores(self) -> FhirStoresResource: ...
                def operations(self) -> OperationsResource: ...
                def dicomStores(self) -> DicomStoresResource: ...
                def annotationStores(self) -> AnnotationStoresResource: ...
                def consentStores(self) -> ConsentStoresResource: ...
                def hl7V2Stores(self) -> Hl7V2StoresResource: ...
            def list(
                self,
                *,
                name: str,
                pageSize: int = ...,
                filter: str = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def datasets(self) -> DatasetsResource: ...
        def locations(self) -> LocationsResource: ...
    def projects(self) -> ProjectsResource: ...

class AnnotationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Annotation: ...

class ConsentArtifactHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ConsentArtifact: ...

class MessageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Message: ...

class ListAnnotationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAnnotationsResponse: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class ListConsentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListConsentsResponse: ...

class ListAnnotationStoresResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAnnotationStoresResponse: ...

class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLocationsResponse: ...

class AnnotationStoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AnnotationStore: ...

class ListDicomStoresResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDicomStoresResponse: ...

class ListDatasetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDatasetsResponse: ...

class ListAttributeDefinitionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListAttributeDefinitionsResponse: ...

class AttributeDefinitionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AttributeDefinition: ...

class ListUserDataMappingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListUserDataMappingsResponse: ...

class HttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> HttpBody: ...

class ListConsentStoresResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListConsentStoresResponse: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class CheckDataAccessResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CheckDataAccessResponse: ...

class DicomStoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DicomStore: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListHl7V2StoresResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListHl7V2StoresResponse: ...

class ListFhirStoresResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListFhirStoresResponse: ...

class FhirStoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FhirStore: ...

class DatasetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Dataset: ...

class ArchiveUserDataMappingResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ArchiveUserDataMappingResponse: ...

class UserDataMappingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UserDataMapping: ...

class Hl7V2StoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Hl7V2Store: ...

class IngestMessageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> IngestMessageResponse: ...

class ListConsentRevisionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListConsentRevisionsResponse: ...

class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Location: ...

class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOperationsResponse: ...

class ConsentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Consent: ...

class ListMessagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListMessagesResponse: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class ConsentStoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ConsentStore: ...

class ListConsentArtifactsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListConsentArtifactsResponse: ...

class EvaluateUserConsentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> EvaluateUserConsentsResponse: ...

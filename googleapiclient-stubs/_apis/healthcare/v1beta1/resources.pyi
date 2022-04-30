import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudHealthcareResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DatasetsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AnnotationStoresResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class AnnotationsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: Annotation = ...,
                            **kwargs: typing.Any
                        ) -> AnnotationHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> AnnotationHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            view: typing_extensions.Literal[
                                "ANNOTATION_VIEW_UNSPECIFIED",
                                "ANNOTATION_VIEW_BASIC",
                                "ANNOTATION_VIEW_FULL",
                            ] = ...,
                            **kwargs: typing.Any
                        ) -> ListAnnotationsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListAnnotationsResponseHttpRequest,
                            previous_response: ListAnnotationsResponse,
                        ) -> ListAnnotationsResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: Annotation = ...,
                            updateMask: str = ...,
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
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def evaluate(
                        self,
                        *,
                        name: str,
                        body: EvaluateAnnotationStoreRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def export(
                        self,
                        *,
                        name: str,
                        body: ExportAnnotationsRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> AnnotationStoreHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def import_(
                        self,
                        *,
                        name: str,
                        body: ImportAnnotationsRequest = ...,
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
                    ) -> ListAnnotationStoresResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListAnnotationStoresResponseHttpRequest,
                        previous_response: ListAnnotationStoresResponse,
                    ) -> ListAnnotationStoresResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: AnnotationStore = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> AnnotationStoreHttpRequest: ...
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
                    def annotations(self) -> AnnotationsResource: ...

                @typing.type_check_only
                class ConsentStoresResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class AttributeDefinitionsResource(
                        googleapiclient.discovery.Resource
                    ):
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
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> AttributeDefinitionHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListAttributeDefinitionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListAttributeDefinitionsResponseHttpRequest,
                            previous_response: ListAttributeDefinitionsResponse,
                        ) -> ListAttributeDefinitionsResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: AttributeDefinition = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> AttributeDefinitionHttpRequest: ...

                    @typing.type_check_only
                    class ConsentArtifactsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: ConsentArtifact = ...,
                            **kwargs: typing.Any
                        ) -> ConsentArtifactHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> ConsentArtifactHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListConsentArtifactsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListConsentArtifactsResponseHttpRequest,
                            previous_response: ListConsentArtifactsResponse,
                        ) -> ListConsentArtifactsResponseHttpRequest | None: ...

                    @typing.type_check_only
                    class ConsentsResource(googleapiclient.discovery.Resource):
                        def activate(
                            self,
                            *,
                            name: str,
                            body: ActivateConsentRequest = ...,
                            **kwargs: typing.Any
                        ) -> ConsentHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: Consent = ...,
                            **kwargs: typing.Any
                        ) -> ConsentHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def deleteRevision(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> ConsentHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListConsentsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListConsentsResponseHttpRequest,
                            previous_response: ListConsentsResponse,
                        ) -> ListConsentsResponseHttpRequest | None: ...
                        def listRevisions(
                            self,
                            *,
                            name: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListConsentRevisionsResponseHttpRequest: ...
                        def listRevisions_next(
                            self,
                            previous_request: ListConsentRevisionsResponseHttpRequest,
                            previous_response: ListConsentRevisionsResponse,
                        ) -> ListConsentRevisionsResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: Consent = ...,
                            updateMask: str = ...,
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

                    @typing.type_check_only
                    class UserDataMappingsResource(googleapiclient.discovery.Resource):
                        def archive(
                            self,
                            *,
                            name: str,
                            body: ArchiveUserDataMappingRequest = ...,
                            **kwargs: typing.Any
                        ) -> ArchiveUserDataMappingResponseHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: UserDataMapping = ...,
                            **kwargs: typing.Any
                        ) -> UserDataMappingHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> UserDataMappingHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListUserDataMappingsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListUserDataMappingsResponseHttpRequest,
                            previous_response: ListUserDataMappingsResponse,
                        ) -> ListUserDataMappingsResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: UserDataMapping = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> UserDataMappingHttpRequest: ...

                    def checkDataAccess(
                        self,
                        *,
                        consentStore: str,
                        body: CheckDataAccessRequest = ...,
                        **kwargs: typing.Any
                    ) -> CheckDataAccessResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: ConsentStore = ...,
                        consentStoreId: str = ...,
                        **kwargs: typing.Any
                    ) -> ConsentStoreHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def evaluateUserConsents(
                        self,
                        *,
                        consentStore: str,
                        body: EvaluateUserConsentsRequest = ...,
                        **kwargs: typing.Any
                    ) -> EvaluateUserConsentsResponseHttpRequest: ...
                    def evaluateUserConsents_next(
                        self,
                        previous_request: EvaluateUserConsentsResponseHttpRequest,
                        previous_response: EvaluateUserConsentsResponse,
                    ) -> EvaluateUserConsentsResponseHttpRequest | None: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ConsentStoreHttpRequest: ...
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
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListConsentStoresResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListConsentStoresResponseHttpRequest,
                        previous_response: ListConsentStoresResponse,
                    ) -> ListConsentStoresResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: ConsentStore = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> ConsentStoreHttpRequest: ...
                    def queryAccessibleData(
                        self,
                        *,
                        consentStore: str,
                        body: QueryAccessibleDataRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
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
                    def attributeDefinitions(self) -> AttributeDefinitionsResource: ...
                    def consentArtifacts(self) -> ConsentArtifactsResource: ...
                    def consents(self) -> ConsentsResource: ...
                    def userDataMappings(self) -> UserDataMappingsResource: ...

                @typing.type_check_only
                class DicomStoresResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class StudiesResource(googleapiclient.discovery.Resource):
                        @typing.type_check_only
                        class SeriesResource(googleapiclient.discovery.Resource):
                            @typing.type_check_only
                            class InstancesResource(googleapiclient.discovery.Resource):
                                @typing.type_check_only
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
                                def retrieveMetadata(
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
                                def frames(self) -> FramesResource: ...

                            def delete(
                                self,
                                *,
                                parent: str,
                                dicomWebPath: str,
                                **kwargs: typing.Any
                            ) -> OperationHttpRequest: ...
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
                            def searchForInstances(
                                self,
                                *,
                                parent: str,
                                dicomWebPath: str,
                                **kwargs: typing.Any
                            ) -> HttpBodyHttpRequest: ...
                            def instances(self) -> InstancesResource: ...

                        def delete(
                            self,
                            *,
                            parent: str,
                            dicomWebPath: str,
                            **kwargs: typing.Any
                        ) -> OperationHttpRequest: ...
                        def retrieveMetadata(
                            self,
                            *,
                            parent: str,
                            dicomWebPath: str,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def retrieveStudy(
                            self,
                            *,
                            parent: str,
                            dicomWebPath: str,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def searchForInstances(
                            self,
                            *,
                            parent: str,
                            dicomWebPath: str,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
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
                        def series(self) -> SeriesResource: ...

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
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def export(
                        self,
                        *,
                        name: str,
                        body: ExportDicomDataRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> DicomStoreHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def import_(
                        self,
                        *,
                        name: str,
                        body: ImportDicomDataRequest = ...,
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
                    def list_next(
                        self,
                        previous_request: ListDicomStoresResponseHttpRequest,
                        previous_response: ListDicomStoresResponse,
                    ) -> ListDicomStoresResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: DicomStore = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> DicomStoreHttpRequest: ...
                    def searchForInstances(
                        self, *, parent: str, dicomWebPath: str, **kwargs: typing.Any
                    ) -> HttpBodyHttpRequest: ...
                    def searchForSeries(
                        self, *, parent: str, dicomWebPath: str, **kwargs: typing.Any
                    ) -> HttpBodyHttpRequest: ...
                    def searchForStudies(
                        self, *, parent: str, dicomWebPath: str, **kwargs: typing.Any
                    ) -> HttpBodyHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def storeInstances(
                        self,
                        *,
                        parent: str,
                        dicomWebPath: str,
                        body: HttpBody = ...,
                        **kwargs: typing.Any
                    ) -> HttpBodyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> TestIamPermissionsResponseHttpRequest: ...
                    def studies(self) -> StudiesResource: ...

                @typing.type_check_only
                class FhirStoresResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class FhirResource(googleapiclient.discovery.Resource):
                        def ConceptMap_search_translate(
                            self,
                            *,
                            parent: str,
                            code: str = ...,
                            conceptMapVersion: str = ...,
                            source: str = ...,
                            system: str = ...,
                            target: str = ...,
                            url: str = ...,
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
                        def Observation_lastn(
                            self, *, parent: str, **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def Patient_everything(
                            self,
                            *,
                            name: str,
                            end: str = ...,
                            start: str = ...,
                            x_count: int = ...,
                            x_page_token: str = ...,
                            x_since: str = ...,
                            x_type: str = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def Resource_purge(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def Resource_validate(
                            self,
                            *,
                            parent: str,
                            type: str,
                            body: HttpBody = ...,
                            profile: str = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def capabilities(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def conditionalDelete(
                            self, *, parent: str, type: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def conditionalPatch(
                            self,
                            *,
                            parent: str,
                            type: str,
                            body: HttpBody = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def conditionalUpdate(
                            self,
                            *,
                            parent: str,
                            type: str,
                            body: HttpBody = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            type: str,
                            body: HttpBody = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def executeBundle(
                            self,
                            *,
                            parent: str,
                            body: HttpBody = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def history(
                            self,
                            *,
                            name: str,
                            x_at: str = ...,
                            x_count: int = ...,
                            x_page_token: str = ...,
                            x_since: str = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: HttpBody = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def read(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def search(
                            self,
                            *,
                            parent: str,
                            body: SearchResourcesRequest = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def search_type(
                            self,
                            *,
                            parent: str,
                            resourceType: str,
                            body: SearchResourcesRequest = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def update(
                            self,
                            *,
                            name: str,
                            body: HttpBody = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def vread(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...

                    def configureSearch(
                        self,
                        *,
                        name: str,
                        body: ConfigureSearchRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: FhirStore = ...,
                        fhirStoreId: str = ...,
                        **kwargs: typing.Any
                    ) -> FhirStoreHttpRequest: ...
                    def deidentify(
                        self,
                        *,
                        sourceStore: str,
                        body: DeidentifyFhirStoreRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def export(
                        self,
                        *,
                        name: str,
                        body: ExportResourcesRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> FhirStoreHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def import_(
                        self,
                        *,
                        name: str,
                        body: ImportResourcesRequest = ...,
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
                    ) -> ListFhirStoresResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListFhirStoresResponseHttpRequest,
                        previous_response: ListFhirStoresResponse,
                    ) -> ListFhirStoresResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: FhirStore = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> FhirStoreHttpRequest: ...
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
                    def fhir(self) -> FhirResource: ...

                @typing.type_check_only
                class Hl7V2StoresResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class MessagesResource(googleapiclient.discovery.Resource):
                        def batchGet(
                            self,
                            *,
                            parent: str,
                            ids: str | _list[str] = ...,
                            view: typing_extensions.Literal[
                                "MESSAGE_VIEW_UNSPECIFIED",
                                "RAW_ONLY",
                                "PARSED_ONLY",
                                "FULL",
                                "SCHEMATIZED_ONLY",
                                "BASIC",
                            ] = ...,
                            **kwargs: typing.Any
                        ) -> BatchGetMessagesResponseHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            body: CreateMessageRequest = ...,
                            **kwargs: typing.Any
                        ) -> MessageHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
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
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
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
                        def list_next(
                            self,
                            previous_request: ListMessagesResponseHttpRequest,
                            previous_response: ListMessagesResponse,
                        ) -> ListMessagesResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: Message = ...,
                            updateMask: str = ...,
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
                    def export(
                        self,
                        *,
                        name: str,
                        body: ExportMessagesRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> Hl7V2StoreHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def import_(
                        self,
                        *,
                        name: str,
                        body: ImportMessagesRequest = ...,
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
                    ) -> ListHl7V2StoresResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListHl7V2StoresResponseHttpRequest,
                        previous_response: ListHl7V2StoresResponse,
                    ) -> ListHl7V2StoresResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Hl7V2Store = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> Hl7V2StoreHttpRequest: ...
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
                    def messages(self) -> MessagesResource: ...

                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self,
                        *,
                        name: str,
                        body: CancelOperationRequest = ...,
                        **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
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

                def create(
                    self,
                    *,
                    parent: str,
                    body: Dataset = ...,
                    datasetId: str = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def deidentify(
                    self,
                    *,
                    sourceDataset: str,
                    body: DeidentifyDatasetRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DatasetHttpRequest: ...
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
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListDatasetsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDatasetsResponseHttpRequest,
                    previous_response: ListDatasetsResponse,
                ) -> ListDatasetsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Dataset = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> DatasetHttpRequest: ...
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
                def annotationStores(self) -> AnnotationStoresResource: ...
                def consentStores(self) -> ConsentStoresResource: ...
                def dicomStores(self) -> DicomStoresResource: ...
                def fhirStores(self) -> FhirStoresResource: ...
                def hl7V2Stores(self) -> Hl7V2StoresResource: ...
                def operations(self) -> OperationsResource: ...

            @typing.type_check_only
            class ServicesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class NlpResource(googleapiclient.discovery.Resource):
                    def analyzeEntities(
                        self,
                        *,
                        nlpService: str,
                        body: AnalyzeEntitiesRequest = ...,
                        **kwargs: typing.Any
                    ) -> AnalyzeEntitiesResponseHttpRequest: ...

                def nlp(self) -> NlpResource: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def datasets(self) -> DatasetsResource: ...
            def services(self) -> ServicesResource: ...

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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AnalyzeEntitiesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AnalyzeEntitiesResponse: ...

@typing.type_check_only
class AnnotationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Annotation: ...

@typing.type_check_only
class AnnotationStoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AnnotationStore: ...

@typing.type_check_only
class ArchiveUserDataMappingResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ArchiveUserDataMappingResponse: ...

@typing.type_check_only
class AttributeDefinitionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AttributeDefinition: ...

@typing.type_check_only
class BatchGetMessagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchGetMessagesResponse: ...

@typing.type_check_only
class CheckDataAccessResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CheckDataAccessResponse: ...

@typing.type_check_only
class ConsentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Consent: ...

@typing.type_check_only
class ConsentArtifactHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ConsentArtifact: ...

@typing.type_check_only
class ConsentStoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ConsentStore: ...

@typing.type_check_only
class DatasetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Dataset: ...

@typing.type_check_only
class DicomStoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DicomStore: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class EvaluateUserConsentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> EvaluateUserConsentsResponse: ...

@typing.type_check_only
class FhirStoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FhirStore: ...

@typing.type_check_only
class Hl7V2StoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Hl7V2Store: ...

@typing.type_check_only
class HttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> HttpBody: ...

@typing.type_check_only
class IngestMessageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> IngestMessageResponse: ...

@typing.type_check_only
class ListAnnotationStoresResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAnnotationStoresResponse: ...

@typing.type_check_only
class ListAnnotationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAnnotationsResponse: ...

@typing.type_check_only
class ListAttributeDefinitionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListAttributeDefinitionsResponse: ...

@typing.type_check_only
class ListConsentArtifactsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListConsentArtifactsResponse: ...

@typing.type_check_only
class ListConsentRevisionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListConsentRevisionsResponse: ...

@typing.type_check_only
class ListConsentStoresResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListConsentStoresResponse: ...

@typing.type_check_only
class ListConsentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListConsentsResponse: ...

@typing.type_check_only
class ListDatasetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDatasetsResponse: ...

@typing.type_check_only
class ListDicomStoresResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDicomStoresResponse: ...

@typing.type_check_only
class ListFhirStoresResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListFhirStoresResponse: ...

@typing.type_check_only
class ListHl7V2StoresResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListHl7V2StoresResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListMessagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListMessagesResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListUserDataMappingsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListUserDataMappingsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Location: ...

@typing.type_check_only
class MessageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Message: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...

@typing.type_check_only
class UserDataMappingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UserDataMapping: ...

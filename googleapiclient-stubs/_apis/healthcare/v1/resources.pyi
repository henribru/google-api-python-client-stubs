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
                            def retrieveMetadata(
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
                            def delete(
                                self,
                                *,
                                parent: str,
                                dicomWebPath: str,
                                **kwargs: typing.Any
                            ) -> OperationHttpRequest: ...
                            def retrieveSeries(
                                self,
                                *,
                                parent: str,
                                dicomWebPath: str,
                                **kwargs: typing.Any
                            ) -> HttpBodyHttpRequest: ...
                            def instances(self) -> InstancesResource: ...
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
                        def searchForSeries(
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
                        ) -> OperationHttpRequest: ...
                        def storeInstances(
                            self,
                            *,
                            parent: str,
                            dicomWebPath: str,
                            body: HttpBody = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def searchForInstances(
                            self,
                            *,
                            parent: str,
                            dicomWebPath: str,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def series(self) -> SeriesResource: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListDicomStoresResponseHttpRequest: ...
                    def searchForStudies(
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
                    def import_(
                        self,
                        *,
                        name: str,
                        body: ImportDicomDataRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: DicomStore = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> DicomStoreHttpRequest: ...
                    def storeInstances(
                        self,
                        *,
                        parent: str,
                        dicomWebPath: str,
                        body: HttpBody = ...,
                        **kwargs: typing.Any
                    ) -> HttpBodyHttpRequest: ...
                    def deidentify(
                        self,
                        *,
                        sourceStore: str,
                        body: DeidentifyDicomStoreRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: DicomStore = ...,
                        dicomStoreId: str = ...,
                        **kwargs: typing.Any
                    ) -> DicomStoreHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any
                    ) -> TestIamPermissionsResponseHttpRequest: ...
                    def searchForInstances(
                        self, *, parent: str, dicomWebPath: str, **kwargs: typing.Any
                    ) -> HttpBodyHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def searchForSeries(
                        self, *, parent: str, dicomWebPath: str, **kwargs: typing.Any
                    ) -> HttpBodyHttpRequest: ...
                    def export(
                        self,
                        *,
                        name: str,
                        body: ExportDicomDataRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def studies(self) -> StudiesResource: ...
                class Hl7V2StoresResource(googleapiclient.discovery.Resource):
                    class MessagesResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: CreateMessageRequest = ...,
                            **kwargs: typing.Any
                        ) -> MessageHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            pageToken: str = ...,
                            orderBy: str = ...,
                            view: typing_extensions.Literal[
                                "MESSAGE_VIEW_UNSPECIFIED",
                                "RAW_ONLY",
                                "PARSED_ONLY",
                                "FULL",
                                "BASIC",
                            ] = ...,
                            pageSize: int = ...,
                            filter: str = ...,
                            **kwargs: typing.Any
                        ) -> ListMessagesResponseHttpRequest: ...
                        def ingest(
                            self,
                            *,
                            parent: str,
                            body: IngestMessageRequest = ...,
                            **kwargs: typing.Any
                        ) -> IngestMessageResponseHttpRequest: ...
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
                                "BASIC",
                            ] = ...,
                            **kwargs: typing.Any
                        ) -> MessageHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: Message = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any
                        ) -> MessageHttpRequest: ...
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
                        body: Hl7V2Store = ...,
                        hl7V2StoreId: str = ...,
                        **kwargs: typing.Any
                    ) -> Hl7V2StoreHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        filter: str = ...,
                        **kwargs: typing.Any
                    ) -> ListHl7V2StoresResponseHttpRequest: ...
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
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> Hl7V2StoreHttpRequest: ...
                    def messages(self) -> MessagesResource: ...
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
                        pageToken: str = ...,
                        pageSize: int = ...,
                        filter: str = ...,
                        **kwargs: typing.Any
                    ) -> ListOperationsResponseHttpRequest: ...
                class FhirStoresResource(googleapiclient.discovery.Resource):
                    class FhirResource(googleapiclient.discovery.Resource):
                        def Patient_everything(
                            self,
                            *,
                            name: str,
                            end: str = ...,
                            x_type: str = ...,
                            start: str = ...,
                            x_page_token: str = ...,
                            x_since: str = ...,
                            x_count: int = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def update(
                            self,
                            *,
                            name: str,
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
                        def search(
                            self,
                            *,
                            parent: str,
                            body: SearchResourcesRequest = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def capabilities(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: HttpBody = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def history(
                            self,
                            *,
                            name: str,
                            x_at: str = ...,
                            x_page_token: str = ...,
                            x_since: str = ...,
                            x_count: int = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def vread(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def Resource_purge(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def read(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                        def create(
                            self,
                            *,
                            parent: str,
                            type: str,
                            body: HttpBody = ...,
                            **kwargs: typing.Any
                        ) -> HttpBodyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageToken: str = ...,
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
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> FhirStoreHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
                    def deidentify(
                        self,
                        *,
                        sourceStore: str,
                        body: DeidentifyFhirStoreRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def export(
                        self,
                        *,
                        name: str,
                        body: ExportResourcesRequest = ...,
                        **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
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
                    def patch(
                        self,
                        *,
                        name: str,
                        body: FhirStore = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> FhirStoreHttpRequest: ...
                    def fhir(self) -> FhirResource: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListDatasetsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DatasetHttpRequest: ...
                def deidentify(
                    self,
                    *,
                    sourceDataset: str,
                    body: DeidentifyDatasetRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
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
                def create(
                    self,
                    *,
                    parent: str,
                    body: Dataset = ...,
                    datasetId: str = ...,
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
                def dicomStores(self) -> DicomStoresResource: ...
                def hl7V2Stores(self) -> Hl7V2StoresResource: ...
                def operations(self) -> OperationsResource: ...
                def fhirStores(self) -> FhirStoresResource: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def datasets(self) -> DatasetsResource: ...
        def locations(self) -> LocationsResource: ...
    def projects(self) -> ProjectsResource: ...

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

class MessageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Message: ...

class Hl7V2StoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Hl7V2Store: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class IngestMessageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> IngestMessageResponse: ...

class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLocationsResponse: ...

class ListDicomStoresResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDicomStoresResponse: ...

class ListMessagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListMessagesResponse: ...

class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOperationsResponse: ...

class ListDatasetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDatasetsResponse: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Location: ...

class HttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> HttpBody: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class DicomStoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DicomStore: ...

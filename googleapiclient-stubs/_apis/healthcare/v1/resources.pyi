import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class CloudHealthcareResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DatasetsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ConsentStoresResource(googleapiclient.discovery.Resource):
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        options_requestedPolicyVersion: int = ...,
                        **kwargs: typing.Any
                    ) -> PolicyHttpRequest: ...
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
                        def capabilities(
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
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
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
                def consentStores(self) -> ConsentStoresResource: ...
                def dicomStores(self) -> DicomStoresResource: ...
                def fhirStores(self) -> FhirStoresResource: ...
                def hl7V2Stores(self) -> Hl7V2StoresResource: ...
                def operations(self) -> OperationsResource: ...
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
            def datasets(self) -> DatasetsResource: ...
        def locations(self) -> LocationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class DatasetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Dataset: ...

@typing.type_check_only
class DicomStoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> DicomStore: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class FhirStoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> FhirStore: ...

@typing.type_check_only
class Hl7V2StoreHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Hl7V2Store: ...

@typing.type_check_only
class HttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> HttpBody: ...

@typing.type_check_only
class IngestMessageResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> IngestMessageResponse: ...

@typing.type_check_only
class ListDatasetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListDatasetsResponse: ...

@typing.type_check_only
class ListDicomStoresResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListDicomStoresResponse: ...

@typing.type_check_only
class ListFhirStoresResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListFhirStoresResponse: ...

@typing.type_check_only
class ListHl7V2StoresResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListHl7V2StoresResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListMessagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListMessagesResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Location: ...

@typing.type_check_only
class MessageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Message: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Policy: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...

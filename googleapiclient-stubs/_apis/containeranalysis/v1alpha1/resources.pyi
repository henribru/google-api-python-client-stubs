import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ContainerAnalysisResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class NotesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OccurrencesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListNoteOccurrencesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListNoteOccurrencesResponseHttpRequest,
                    previous_response: ListNoteOccurrencesResponse,
                ) -> ListNoteOccurrencesResponseHttpRequest | None: ...

            def create(
                self,
                *,
                parent: str,
                body: Note = ...,
                name: str = ...,
                noteId: str = ...,
                **kwargs: typing.Any
            ) -> NoteHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> NoteHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                body: GetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                name: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListNotesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListNotesResponseHttpRequest,
                previous_response: ListNotesResponse,
            ) -> ListNotesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Note = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> NoteHttpRequest: ...
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
            def occurrences(self) -> OccurrencesResource: ...

        @typing.type_check_only
        class OccurrencesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: Occurrence = ...,
                name: str = ...,
                **kwargs: typing.Any
            ) -> OccurrenceHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OccurrenceHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                body: GetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def getNotes(
                self, *, name: str, **kwargs: typing.Any
            ) -> NoteHttpRequest: ...
            def getVulnerabilitySummary(
                self, *, parent: str, filter: str = ..., **kwargs: typing.Any
            ) -> GetVulnzOccurrencesSummaryResponseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                kind: typing_extensions.Literal[
                    "KIND_UNSPECIFIED",
                    "PACKAGE_VULNERABILITY",
                    "BUILD_DETAILS",
                    "IMAGE_BASIS",
                    "PACKAGE_MANAGER",
                    "DEPLOYABLE",
                    "DISCOVERY",
                    "ATTESTATION_AUTHORITY",
                    "UPGRADE",
                    "COMPLIANCE",
                    "SBOM",
                    "SPDX_PACKAGE",
                    "SPDX_FILE",
                    "SPDX_RELATIONSHIP",
                    "DSSE_ATTESTATION",
                ] = ...,
                name: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListOccurrencesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListOccurrencesResponseHttpRequest,
                previous_response: ListOccurrencesResponse,
            ) -> ListOccurrencesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Occurrence = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> OccurrenceHttpRequest: ...
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
        class OperationsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: CreateOperationRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: UpdateOperationRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        @typing.type_check_only
        class ScanConfigsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ScanConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListScanConfigsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListScanConfigsResponseHttpRequest,
                previous_response: ListScanConfigsResponse,
            ) -> ListScanConfigsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: ScanConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> ScanConfigHttpRequest: ...

        def notes(self) -> NotesResource: ...
        def occurrences(self) -> OccurrencesResource: ...
        def operations(self) -> OperationsResource: ...
        def scanConfigs(self) -> ScanConfigsResource: ...

    @typing.type_check_only
    class ProvidersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class NotesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OccurrencesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListNoteOccurrencesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListNoteOccurrencesResponseHttpRequest,
                    previous_response: ListNoteOccurrencesResponse,
                ) -> ListNoteOccurrencesResponseHttpRequest | None: ...

            def create(
                self,
                *,
                name: str,
                body: Note = ...,
                noteId: str = ...,
                parent: str = ...,
                **kwargs: typing.Any
            ) -> NoteHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> NoteHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                body: GetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                parent: str = ...,
                **kwargs: typing.Any
            ) -> ListNotesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListNotesResponseHttpRequest,
                previous_response: ListNotesResponse,
            ) -> ListNotesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Note = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> NoteHttpRequest: ...
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
            def occurrences(self) -> OccurrencesResource: ...

        def notes(self) -> NotesResource: ...

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
    def providers(self) -> ProvidersResource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GetVulnzOccurrencesSummaryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GetVulnzOccurrencesSummaryResponse: ...

@typing.type_check_only
class ListNoteOccurrencesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListNoteOccurrencesResponse: ...

@typing.type_check_only
class ListNotesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListNotesResponse: ...

@typing.type_check_only
class ListOccurrencesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOccurrencesResponse: ...

@typing.type_check_only
class ListScanConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListScanConfigsResponse: ...

@typing.type_check_only
class NoteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Note: ...

@typing.type_check_only
class OccurrenceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Occurrence: ...

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
class ScanConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ScanConfig: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TestIamPermissionsResponse: ...

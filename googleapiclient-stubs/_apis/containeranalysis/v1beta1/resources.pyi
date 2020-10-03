import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class ContainerAnalysisResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class ScanConfigsResource(googleapiclient.discovery.Resource):
            def update(
                self, *, name: str, body: ScanConfig = ..., **kwargs: typing.Any
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
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> ScanConfigHttpRequest: ...
        class OccurrencesResource(googleapiclient.discovery.Resource):
            def getNotes(
                self, *, name: str, **kwargs: typing.Any
            ) -> NoteHttpRequest: ...
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
            def getVulnerabilitySummary(
                self, *, parent: str, filter: str = ..., **kwargs: typing.Any
            ) -> VulnerabilityOccurrencesSummaryHttpRequest: ...
            def create(
                self, *, parent: str, body: Occurrence = ..., **kwargs: typing.Any
            ) -> OccurrenceHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> TestIamPermissionsResponseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> ListOccurrencesResponseHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                body: GetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OccurrenceHttpRequest: ...
            def batchCreate(
                self,
                *,
                parent: str,
                body: BatchCreateOccurrencesRequest = ...,
                **kwargs: typing.Any
            ) -> BatchCreateOccurrencesResponseHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
        class NotesResource(googleapiclient.discovery.Resource):
            class OccurrencesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    name: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    filter: str = ...,
                    **kwargs: typing.Any
                ) -> ListNoteOccurrencesResponseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListNotesResponseHttpRequest: ...
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
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                body: GetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> PolicyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> NoteHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Note = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> NoteHttpRequest: ...
            def batchCreate(
                self,
                *,
                parent: str,
                body: BatchCreateNotesRequest = ...,
                **kwargs: typing.Any
            ) -> BatchCreateNotesResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: Note = ...,
                noteId: str = ...,
                **kwargs: typing.Any
            ) -> NoteHttpRequest: ...
            def occurrences(self) -> OccurrencesResource: ...
        def scanConfigs(self) -> ScanConfigsResource: ...
        def occurrences(self) -> OccurrencesResource: ...
        def notes(self) -> NotesResource: ...
    def projects(self) -> ProjectsResource: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class NoteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Note: ...

class ScanConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ScanConfig: ...

class BatchCreateNotesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchCreateNotesResponse: ...

class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestIamPermissionsResponse: ...

class VulnerabilityOccurrencesSummaryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> VulnerabilityOccurrencesSummary: ...

class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Policy: ...

class ListNoteOccurrencesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListNoteOccurrencesResponse: ...

class ListScanConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListScanConfigsResponse: ...

class OccurrenceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Occurrence: ...

class ListOccurrencesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOccurrencesResponse: ...

class BatchCreateOccurrencesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchCreateOccurrencesResponse: ...

class ListNotesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListNotesResponse: ...

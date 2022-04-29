import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudMachineLearningEngineResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class JobsResource(googleapiclient.discovery.Resource):
            def cancel(
                self,
                *,
                name: str,
                body: GoogleCloudMlV1__CancelJobRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobuf__EmptyHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudMlV1__Job = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudMlV1__JobHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudMlV1__JobHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                options_requestedPolicyVersion: int = ...,
                **kwargs: typing.Any
            ) -> GoogleIamV1__PolicyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudMlV1__ListJobsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudMlV1__ListJobsResponseHttpRequest,
                previous_response: GoogleCloudMlV1__ListJobsResponse,
            ) -> GoogleCloudMlV1__ListJobsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudMlV1__Job = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudMlV1__JobHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: GoogleIamV1__SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleIamV1__PolicyHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: GoogleIamV1__TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleIamV1__TestIamPermissionsResponseHttpRequest: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobuf__EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunning__OperationHttpRequest: ...

            @typing.type_check_only
            class StudiesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class TrialsResource(googleapiclient.discovery.Resource):
                    def addMeasurement(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudMlV1__AddTrialMeasurementRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudMlV1__TrialHttpRequest: ...
                    def checkEarlyStoppingState(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudMlV1__CheckTrialEarlyStoppingStateRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunning__OperationHttpRequest: ...
                    def complete(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudMlV1__CompleteTrialRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudMlV1__TrialHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudMlV1__Trial = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudMlV1__TrialHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobuf__EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudMlV1__TrialHttpRequest: ...
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GoogleCloudMlV1__ListTrialsResponseHttpRequest: ...
                    def listOptimalTrials(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudMlV1__ListOptimalTrialsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudMlV1__ListOptimalTrialsResponseHttpRequest: ...
                    def stop(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudMlV1__StopTrialRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudMlV1__TrialHttpRequest: ...
                    def suggest(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudMlV1__SuggestTrialsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunning__OperationHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudMlV1__Study = ...,
                    studyId: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudMlV1__StudyHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobuf__EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudMlV1__StudyHttpRequest: ...
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleCloudMlV1__ListStudiesResponseHttpRequest: ...
                def trials(self) -> TrialsResource: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudMlV1__LocationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudMlV1__ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudMlV1__ListLocationsResponseHttpRequest,
                previous_response: GoogleCloudMlV1__ListLocationsResponse,
            ) -> GoogleCloudMlV1__ListLocationsResponseHttpRequest | None: ...
            def operations(self) -> OperationsResource: ...
            def studies(self) -> StudiesResource: ...

        @typing.type_check_only
        class ModelsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class VersionsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudMlV1__Version = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunning__OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunning__OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudMlV1__VersionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudMlV1__ListVersionsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleCloudMlV1__ListVersionsResponseHttpRequest,
                    previous_response: GoogleCloudMlV1__ListVersionsResponse,
                ) -> GoogleCloudMlV1__ListVersionsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudMlV1__Version = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunning__OperationHttpRequest: ...
                def setDefault(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudMlV1__SetDefaultVersionRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudMlV1__VersionHttpRequest: ...

            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudMlV1__Model = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudMlV1__ModelHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunning__OperationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudMlV1__ModelHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                options_requestedPolicyVersion: int = ...,
                **kwargs: typing.Any
            ) -> GoogleIamV1__PolicyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudMlV1__ListModelsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudMlV1__ListModelsResponseHttpRequest,
                previous_response: GoogleCloudMlV1__ListModelsResponse,
            ) -> GoogleCloudMlV1__ListModelsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudMlV1__Model = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunning__OperationHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: GoogleIamV1__SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleIamV1__PolicyHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: GoogleIamV1__TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleIamV1__TestIamPermissionsResponseHttpRequest: ...
            def versions(self) -> VersionsResource: ...

        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def cancel(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobuf__EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunning__OperationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunning__ListOperationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleLongrunning__ListOperationsResponseHttpRequest,
                previous_response: GoogleLongrunning__ListOperationsResponse,
            ) -> GoogleLongrunning__ListOperationsResponseHttpRequest | None: ...

        def explain(
            self,
            *,
            name: str,
            body: GoogleCloudMlV1__ExplainRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleApi__HttpBodyHttpRequest: ...
        def getConfig(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleCloudMlV1__GetConfigResponseHttpRequest: ...
        def predict(
            self,
            *,
            name: str,
            body: GoogleCloudMlV1__PredictRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleApi__HttpBodyHttpRequest: ...
        def jobs(self) -> JobsResource: ...
        def locations(self) -> LocationsResource: ...
        def models(self) -> ModelsResource: ...
        def operations(self) -> OperationsResource: ...

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
class GoogleApi__HttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleApi__HttpBody: ...

@typing.type_check_only
class GoogleCloudMlV1__GetConfigResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudMlV1__GetConfigResponse: ...

@typing.type_check_only
class GoogleCloudMlV1__JobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudMlV1__Job: ...

@typing.type_check_only
class GoogleCloudMlV1__ListJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudMlV1__ListJobsResponse: ...

@typing.type_check_only
class GoogleCloudMlV1__ListLocationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudMlV1__ListLocationsResponse: ...

@typing.type_check_only
class GoogleCloudMlV1__ListModelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudMlV1__ListModelsResponse: ...

@typing.type_check_only
class GoogleCloudMlV1__ListOptimalTrialsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudMlV1__ListOptimalTrialsResponse: ...

@typing.type_check_only
class GoogleCloudMlV1__ListStudiesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudMlV1__ListStudiesResponse: ...

@typing.type_check_only
class GoogleCloudMlV1__ListTrialsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudMlV1__ListTrialsResponse: ...

@typing.type_check_only
class GoogleCloudMlV1__ListVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudMlV1__ListVersionsResponse: ...

@typing.type_check_only
class GoogleCloudMlV1__LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudMlV1__Location: ...

@typing.type_check_only
class GoogleCloudMlV1__ModelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudMlV1__Model: ...

@typing.type_check_only
class GoogleCloudMlV1__StudyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudMlV1__Study: ...

@typing.type_check_only
class GoogleCloudMlV1__TrialHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudMlV1__Trial: ...

@typing.type_check_only
class GoogleCloudMlV1__VersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudMlV1__Version: ...

@typing.type_check_only
class GoogleIamV1__PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleIamV1__Policy: ...

@typing.type_check_only
class GoogleIamV1__TestIamPermissionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleIamV1__TestIamPermissionsResponse: ...

@typing.type_check_only
class GoogleLongrunning__ListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunning__ListOperationsResponse: ...

@typing.type_check_only
class GoogleLongrunning__OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunning__Operation: ...

@typing.type_check_only
class GoogleProtobuf__EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleProtobuf__Empty: ...

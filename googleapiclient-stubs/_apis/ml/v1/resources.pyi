import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudMachineLearningEngineResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class ModelsResource(googleapiclient.discovery.Resource):
            class VersionsResource(googleapiclient.discovery.Resource):
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
                    body: GoogleCloudMlV1__Version = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunning__OperationHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudMlV1__Version = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunning__OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    filter: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudMlV1__ListVersionsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudMlV1__VersionHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunning__OperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunning__OperationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudMlV1__ListModelsResponseHttpRequest: ...
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
            def getIamPolicy(
                self,
                *,
                resource: str,
                options_requestedPolicyVersion: int = ...,
                **kwargs: typing.Any
            ) -> GoogleIamV1__PolicyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudMlV1__ModelHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudMlV1__Model = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudMlV1__ModelHttpRequest: ...
            def versions(self) -> VersionsResource: ...
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleLongrunning__OperationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                pageToken: str = ...,
                pageSize: int = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunning__ListOperationsResponseHttpRequest: ...
            def cancel(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleProtobuf__EmptyHttpRequest: ...
        class LocationsResource(googleapiclient.discovery.Resource):
            class OperationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunning__OperationHttpRequest: ...
                def cancel(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobuf__EmptyHttpRequest: ...
            class StudiesResource(googleapiclient.discovery.Resource):
                class TrialsResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobuf__EmptyHttpRequest: ...
                    def suggest(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudMlV1__SuggestTrialsRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunning__OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleCloudMlV1__TrialHttpRequest: ...
                    def addMeasurement(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudMlV1__AddTrialMeasurementRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudMlV1__TrialHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleCloudMlV1__Trial = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudMlV1__TrialHttpRequest: ...
                    def complete(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudMlV1__CompleteTrialRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudMlV1__TrialHttpRequest: ...
                    def list(
                        self, *, parent: str, **kwargs: typing.Any
                    ) -> GoogleCloudMlV1__ListTrialsResponseHttpRequest: ...
                    def checkEarlyStoppingState(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudMlV1__CheckTrialEarlyStoppingStateRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunning__OperationHttpRequest: ...
                    def stop(
                        self,
                        *,
                        name: str,
                        body: GoogleCloudMlV1__StopTrialRequest = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudMlV1__TrialHttpRequest: ...
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> GoogleCloudMlV1__ListStudiesResponseHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobuf__EmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudMlV1__Study = ...,
                    studyId: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudMlV1__StudyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudMlV1__StudyHttpRequest: ...
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
            def operations(self) -> OperationsResource: ...
            def studies(self) -> StudiesResource: ...
        class JobsResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: GoogleCloudMlV1__Job = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudMlV1__JobHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudMlV1__ListJobsResponseHttpRequest: ...
            def cancel(
                self,
                *,
                name: str,
                body: GoogleCloudMlV1__CancelJobRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleProtobuf__EmptyHttpRequest: ...
            def setIamPolicy(
                self,
                *,
                resource: str,
                body: GoogleIamV1__SetIamPolicyRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleIamV1__PolicyHttpRequest: ...
            def getIamPolicy(
                self,
                *,
                resource: str,
                options_requestedPolicyVersion: int = ...,
                **kwargs: typing.Any
            ) -> GoogleIamV1__PolicyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleCloudMlV1__JobHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: GoogleCloudMlV1__Job = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudMlV1__JobHttpRequest: ...
            def testIamPermissions(
                self,
                *,
                resource: str,
                body: GoogleIamV1__TestIamPermissionsRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleIamV1__TestIamPermissionsResponseHttpRequest: ...
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
        def explain(
            self,
            *,
            name: str,
            body: GoogleCloudMlV1__ExplainRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleApi__HttpBodyHttpRequest: ...
        def models(self) -> ModelsResource: ...
        def operations(self) -> OperationsResource: ...
        def locations(self) -> LocationsResource: ...
        def jobs(self) -> JobsResource: ...
    def projects(self) -> ProjectsResource: ...

class GoogleIamV1__TestIamPermissionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleIamV1__TestIamPermissionsResponse: ...

class GoogleApi__HttpBodyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleApi__HttpBody: ...

class GoogleCloudMlV1__StudyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudMlV1__Study: ...

class GoogleIamV1__PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleIamV1__Policy: ...

class GoogleCloudMlV1__LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudMlV1__Location: ...

class GoogleProtobuf__EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleProtobuf__Empty: ...

class GoogleCloudMlV1__ListTrialsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudMlV1__ListTrialsResponse: ...

class GoogleCloudMlV1__TrialHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudMlV1__Trial: ...

class GoogleCloudMlV1__JobHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudMlV1__Job: ...

class GoogleLongrunning__OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunning__Operation: ...

class GoogleCloudMlV1__ListModelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudMlV1__ListModelsResponse: ...

class GoogleCloudMlV1__ListJobsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudMlV1__ListJobsResponse: ...

class GoogleCloudMlV1__GetConfigResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudMlV1__GetConfigResponse: ...

class GoogleCloudMlV1__ModelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudMlV1__Model: ...

class GoogleCloudMlV1__ListLocationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudMlV1__ListLocationsResponse: ...

class GoogleCloudMlV1__VersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudMlV1__Version: ...

class GoogleCloudMlV1__ListVersionsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudMlV1__ListVersionsResponse: ...

class GoogleCloudMlV1__ListStudiesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleCloudMlV1__ListStudiesResponse: ...

class GoogleLongrunning__ListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunning__ListOperationsResponse: ...

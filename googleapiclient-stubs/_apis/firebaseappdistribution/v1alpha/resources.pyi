import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class FirebaseAppDistributionResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AppsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class Release_by_hashResource(googleapiclient.discovery.Resource):
            def get(
                self, *, mobilesdkAppId: str, uploadHash: str, **kwargs: typing.Any
            ) -> (
                GoogleFirebaseAppdistroV1alphaGetReleaseByUploadHashResponseHttpRequest
            ): ...

        @typing.type_check_only
        class ReleasesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class NotesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    mobilesdkAppId: str,
                    releaseId: str,
                    body: GoogleFirebaseAppdistroV1alphaCreateReleaseNotesRequest = ...,
                    **kwargs: typing.Any,
                ) -> (
                    GoogleFirebaseAppdistroV1alphaCreateReleaseNotesResponseHttpRequest
                ): ...

            def enable_access(
                self,
                *,
                mobilesdkAppId: str,
                releaseId: str,
                body: GoogleFirebaseAppdistroV1alphaEnableAccessOnReleaseRequest = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleFirebaseAppdistroV1alphaEnableAccessOnReleaseResponseHttpRequest
            ): ...
            def notes(self) -> NotesResource: ...

        @typing.type_check_only
        class TestersResource(googleapiclient.discovery.Resource):
            def getTesterUdids(
                self, *, mobilesdkAppId: str, project: str = ..., **kwargs: typing.Any
            ) -> GoogleFirebaseAppdistroV1alphaGetTesterUdidsResponseHttpRequest: ...

        @typing.type_check_only
        class Upload_statusResource(googleapiclient.discovery.Resource):
            def get(
                self, *, mobilesdkAppId: str, uploadToken: str, **kwargs: typing.Any
            ) -> GoogleFirebaseAppdistroV1alphaGetUploadStatusResponseHttpRequest: ...

        def get(
            self,
            *,
            mobilesdkAppId: str,
            appView: typing_extensions.Literal[
                "APP_VIEW_UNSPECIFIED", "BASIC", "FULL"
            ] = ...,
            **kwargs: typing.Any,
        ) -> GoogleFirebaseAppdistroV1alphaAppHttpRequest: ...
        def getJwt(
            self, *, mobilesdkAppId: str, **kwargs: typing.Any
        ) -> GoogleFirebaseAppdistroV1alphaJwtHttpRequest: ...
        def provisionApp(
            self, *, mobilesdkAppId: str, **kwargs: typing.Any
        ) -> GoogleFirebaseAppdistroV1alphaProvisionAppResponseHttpRequest: ...
        def release_by_hash(self) -> Release_by_hashResource: ...
        def releases(self) -> ReleasesResource: ...
        def testers(self) -> TestersResource: ...
        def upload_status(self) -> Upload_statusResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AppsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ReleasesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class TestsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleFirebaseAppdistroV1alphaCancelReleaseTestResponseHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleFirebaseAppdistroV1alphaReleaseTest = ...,
                        releaseTestId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleFirebaseAppdistroV1alphaReleaseTestHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleFirebaseAppdistroV1alphaReleaseTestHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        view: typing_extensions.Literal[
                            "RELEASE_TEST_VIEW_UNSPECIFIED",
                            "RELEASE_TEST_VIEW_BASIC",
                            "RELEASE_TEST_VIEW_FULL",
                        ] = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleFirebaseAppdistroV1alphaListReleaseTestsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleFirebaseAppdistroV1alphaListReleaseTestsResponseHttpRequest,
                        previous_response: GoogleFirebaseAppdistroV1alphaListReleaseTestsResponse,
                    ) -> (
                        GoogleFirebaseAppdistroV1alphaListReleaseTestsResponseHttpRequest
                        | None
                    ): ...

                def tests(self) -> TestsResource: ...

            @typing.type_check_only
            class TestCasesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleFirebaseAppdistroV1alphaTestCase = ...,
                    testCaseId: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleFirebaseAppdistroV1alphaTestCaseHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleFirebaseAppdistroV1alphaTestCaseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> GoogleFirebaseAppdistroV1alphaListTestCasesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: GoogleFirebaseAppdistroV1alphaListTestCasesResponseHttpRequest,
                    previous_response: GoogleFirebaseAppdistroV1alphaListTestCasesResponse,
                ) -> (
                    GoogleFirebaseAppdistroV1alphaListTestCasesResponseHttpRequest
                    | None
                ): ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleFirebaseAppdistroV1alphaTestCase = ...,
                    **kwargs: typing.Any,
                ) -> GoogleFirebaseAppdistroV1alphaTestCaseHttpRequest: ...

            def getTestConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> GoogleFirebaseAppdistroV1alphaTestConfigHttpRequest: ...
            def updateTestConfig(
                self,
                *,
                name: str,
                body: GoogleFirebaseAppdistroV1alphaTestConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleFirebaseAppdistroV1alphaTestConfigHttpRequest: ...
            def releases(self) -> ReleasesResource: ...
            def testCases(self) -> TestCasesResource: ...

        @typing.type_check_only
        class TestersResource(googleapiclient.discovery.Resource):
            def getUdids(
                self, *, project: str, mobilesdkAppId: str = ..., **kwargs: typing.Any
            ) -> GoogleFirebaseAppdistroV1alphaGetTesterUdidsResponseHttpRequest: ...

        def apps(self) -> AppsResource: ...
        def testers(self) -> TestersResource: ...

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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def apps(self) -> AppsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaAppHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1alphaApp: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaCancelReleaseTestResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1alphaCancelReleaseTestResponse: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaCreateReleaseNotesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1alphaCreateReleaseNotesResponse: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaEnableAccessOnReleaseResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1alphaEnableAccessOnReleaseResponse: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaGetReleaseByUploadHashResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1alphaGetReleaseByUploadHashResponse: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaGetTesterUdidsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1alphaGetTesterUdidsResponse: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaGetUploadStatusResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1alphaGetUploadStatusResponse: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaJwtHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1alphaJwt: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaListReleaseTestsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1alphaListReleaseTestsResponse: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaListTestCasesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1alphaListTestCasesResponse: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaProvisionAppResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1alphaProvisionAppResponse: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaReleaseTestHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1alphaReleaseTest: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaTestCaseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1alphaTestCase: ...

@typing.type_check_only
class GoogleFirebaseAppdistroV1alphaTestConfigHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleFirebaseAppdistroV1alphaTestConfig: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleProtobufEmpty: ...

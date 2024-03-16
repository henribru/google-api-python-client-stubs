import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class TestingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ApplicationDetailServiceResource(googleapiclient.discovery.Resource):
        def getApkDetails(
            self,
            *,
            body: FileReference = ...,
            bundleLocation_gcsPath: str = ...,
            **kwargs: typing.Any,
        ) -> GetApkDetailsResponseHttpRequest: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DeviceSessionsResource(googleapiclient.discovery.Resource):
            def cancel(
                self,
                *,
                name: str,
                body: CancelDeviceSessionRequest = ...,
                **kwargs: typing.Any,
            ) -> EmptyHttpRequest: ...
            def create(
                self, *, parent: str, body: DeviceSession = ..., **kwargs: typing.Any
            ) -> DeviceSessionHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> DeviceSessionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListDeviceSessionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListDeviceSessionsResponseHttpRequest,
                previous_response: ListDeviceSessionsResponse,
            ) -> ListDeviceSessionsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: DeviceSession = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> DeviceSessionHttpRequest: ...

        @typing.type_check_only
        class TestMatricesResource(googleapiclient.discovery.Resource):
            def cancel(
                self, *, projectId: str, testMatrixId: str, **kwargs: typing.Any
            ) -> CancelTestMatrixResponseHttpRequest: ...
            def create(
                self,
                *,
                projectId: str,
                body: TestMatrix = ...,
                requestId: str = ...,
                **kwargs: typing.Any,
            ) -> TestMatrixHttpRequest: ...
            def get(
                self, *, projectId: str, testMatrixId: str, **kwargs: typing.Any
            ) -> TestMatrixHttpRequest: ...

        def deviceSessions(self) -> DeviceSessionsResource: ...
        def testMatrices(self) -> TestMatricesResource: ...

    @typing.type_check_only
    class TestEnvironmentCatalogResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            environmentType: typing_extensions.Literal[
                "ENVIRONMENT_TYPE_UNSPECIFIED",
                "ANDROID",
                "IOS",
                "NETWORK_CONFIGURATION",
                "PROVIDED_SOFTWARE",
                "DEVICE_IP_BLOCKS",
            ],
            projectId: str = ...,
            **kwargs: typing.Any,
        ) -> TestEnvironmentCatalogHttpRequest: ...

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
    def applicationDetailService(self) -> ApplicationDetailServiceResource: ...
    def projects(self) -> ProjectsResource: ...
    def testEnvironmentCatalog(self) -> TestEnvironmentCatalogResource: ...

@typing.type_check_only
class CancelTestMatrixResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CancelTestMatrixResponse: ...

@typing.type_check_only
class DeviceSessionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DeviceSession: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class GetApkDetailsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GetApkDetailsResponse: ...

@typing.type_check_only
class ListDeviceSessionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDeviceSessionsResponse: ...

@typing.type_check_only
class TestEnvironmentCatalogHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestEnvironmentCatalog: ...

@typing.type_check_only
class TestMatrixHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestMatrix: ...

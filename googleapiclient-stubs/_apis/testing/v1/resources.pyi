import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class TestingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ApplicationDetailServiceResource(googleapiclient.discovery.Resource):
        def getApkDetails(
            self, *, body: FileReference = ..., **kwargs: typing.Any
        ) -> GetApkDetailsResponseHttpRequest: ...
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
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
                **kwargs: typing.Any
            ) -> TestMatrixHttpRequest: ...
            def get(
                self, *, projectId: str, testMatrixId: str, **kwargs: typing.Any
            ) -> TestMatrixHttpRequest: ...
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
            **kwargs: typing.Any
        ) -> TestEnvironmentCatalogHttpRequest: ...
    def applicationDetailService(self) -> ApplicationDetailServiceResource: ...
    def projects(self) -> ProjectsResource: ...
    def testEnvironmentCatalog(self) -> TestEnvironmentCatalogResource: ...

@typing.type_check_only
class CancelTestMatrixResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CancelTestMatrixResponse: ...

@typing.type_check_only
class GetApkDetailsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GetApkDetailsResponse: ...

@typing.type_check_only
class TestEnvironmentCatalogHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> TestEnvironmentCatalog: ...

@typing.type_check_only
class TestMatrixHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> TestMatrix: ...

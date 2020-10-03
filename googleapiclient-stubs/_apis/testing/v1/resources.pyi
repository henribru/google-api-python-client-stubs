import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class TestingResource(googleapiclient.discovery.Resource):
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
    class ApplicationDetailServiceResource(googleapiclient.discovery.Resource):
        def getApkDetails(
            self, *, body: FileReference = ..., **kwargs: typing.Any
        ) -> GetApkDetailsResponseHttpRequest: ...
    class ProjectsResource(googleapiclient.discovery.Resource):
        class TestMatricesResource(googleapiclient.discovery.Resource):
            def cancel(
                self, *, projectId: str, testMatrixId: str, **kwargs: typing.Any
            ) -> CancelTestMatrixResponseHttpRequest: ...
            def get(
                self, *, projectId: str, testMatrixId: str, **kwargs: typing.Any
            ) -> TestMatrixHttpRequest: ...
            def create(
                self,
                *,
                projectId: str,
                body: TestMatrix = ...,
                requestId: str = ...,
                **kwargs: typing.Any
            ) -> TestMatrixHttpRequest: ...
        def testMatrices(self) -> TestMatricesResource: ...
    def testEnvironmentCatalog(self) -> TestEnvironmentCatalogResource: ...
    def applicationDetailService(self) -> ApplicationDetailServiceResource: ...
    def projects(self) -> ProjectsResource: ...

class CancelTestMatrixResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CancelTestMatrixResponse: ...

class TestMatrixHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestMatrix: ...

class GetApkDetailsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetApkDetailsResponse: ...

class TestEnvironmentCatalogHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TestEnvironmentCatalog: ...

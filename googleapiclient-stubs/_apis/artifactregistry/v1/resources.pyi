import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class ArtifactRegistryResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class RepositoriesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class AptArtifactsResource(googleapiclient.discovery.Resource):
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: ImportAptArtifactsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def upload(
                        self,
                        *,
                        parent: str,
                        body: UploadAptArtifactRequest = ...,
                        **kwargs: typing.Any,
                    ) -> UploadAptArtifactMediaResponseHttpRequest: ...

                @typing.type_check_only
                class AttachmentsResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Attachment = ...,
                        attachmentId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> AttachmentHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListAttachmentsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListAttachmentsResponseHttpRequest,
                        previous_response: ListAttachmentsResponse,
                    ) -> ListAttachmentsResponseHttpRequest | None: ...

                @typing.type_check_only
                class DockerImagesResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> DockerImageHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListDockerImagesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListDockerImagesResponseHttpRequest,
                        previous_response: ListDockerImagesResponse,
                    ) -> ListDockerImagesResponseHttpRequest | None: ...

                @typing.type_check_only
                class FilesResource(googleapiclient.discovery.Resource):
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def download(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> DownloadFileResponseHttpRequest: ...
                    def download_media(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> BytesHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleDevtoolsArtifactregistryV1FileHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListFilesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListFilesResponseHttpRequest,
                        previous_response: ListFilesResponse,
                    ) -> ListFilesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleDevtoolsArtifactregistryV1File = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleDevtoolsArtifactregistryV1FileHttpRequest: ...
                    def upload(
                        self,
                        *,
                        parent: str,
                        body: UploadFileRequest = ...,
                        **kwargs: typing.Any,
                    ) -> UploadFileMediaResponseHttpRequest: ...

                @typing.type_check_only
                class GenericArtifactsResource(googleapiclient.discovery.Resource):
                    def upload(
                        self,
                        *,
                        parent: str,
                        body: UploadGenericArtifactRequest = ...,
                        **kwargs: typing.Any,
                    ) -> UploadGenericArtifactMediaResponseHttpRequest: ...

                @typing.type_check_only
                class GoModulesResource(googleapiclient.discovery.Resource):
                    def upload(
                        self,
                        *,
                        parent: str,
                        body: UploadGoModuleRequest = ...,
                        **kwargs: typing.Any,
                    ) -> UploadGoModuleMediaResponseHttpRequest: ...

                @typing.type_check_only
                class GoogetArtifactsResource(googleapiclient.discovery.Resource):
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: ImportGoogetArtifactsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def upload(
                        self,
                        *,
                        parent: str,
                        body: UploadGoogetArtifactRequest = ...,
                        **kwargs: typing.Any,
                    ) -> UploadGoogetArtifactMediaResponseHttpRequest: ...

                @typing.type_check_only
                class KfpArtifactsResource(googleapiclient.discovery.Resource):
                    def upload(
                        self,
                        *,
                        parent: str,
                        body: UploadKfpArtifactRequest = ...,
                        **kwargs: typing.Any,
                    ) -> UploadKfpArtifactMediaResponseHttpRequest: ...

                @typing.type_check_only
                class MavenArtifactsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> MavenArtifactHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListMavenArtifactsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListMavenArtifactsResponseHttpRequest,
                        previous_response: ListMavenArtifactsResponse,
                    ) -> ListMavenArtifactsResponseHttpRequest | None: ...

                @typing.type_check_only
                class NpmPackagesResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> NpmPackageHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListNpmPackagesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListNpmPackagesResponseHttpRequest,
                        previous_response: ListNpmPackagesResponse,
                    ) -> ListNpmPackagesResponseHttpRequest | None: ...

                @typing.type_check_only
                class PackagesResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class TagsResource(googleapiclient.discovery.Resource):
                        def create(
                            self,
                            *,
                            parent: str,
                            body: Tag = ...,
                            tagId: str = ...,
                            **kwargs: typing.Any,
                        ) -> TagHttpRequest: ...
                        def delete(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> EmptyHttpRequest: ...
                        def get(
                            self, *, name: str, **kwargs: typing.Any
                        ) -> TagHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any,
                        ) -> ListTagsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListTagsResponseHttpRequest,
                            previous_response: ListTagsResponse,
                        ) -> ListTagsResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: Tag = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> TagHttpRequest: ...

                    @typing.type_check_only
                    class VersionsResource(googleapiclient.discovery.Resource):
                        def batchDelete(
                            self,
                            *,
                            parent: str,
                            body: BatchDeleteVersionsRequest = ...,
                            **kwargs: typing.Any,
                        ) -> OperationHttpRequest: ...
                        def delete(
                            self, *, name: str, force: bool = ..., **kwargs: typing.Any
                        ) -> OperationHttpRequest: ...
                        def get(
                            self,
                            *,
                            name: str,
                            view: typing_extensions.Literal[
                                "VERSION_VIEW_UNSPECIFIED", "BASIC", "FULL"
                            ] = ...,
                            **kwargs: typing.Any,
                        ) -> VersionHttpRequest: ...
                        def list(
                            self,
                            *,
                            parent: str,
                            filter: str = ...,
                            orderBy: str = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            view: typing_extensions.Literal[
                                "VERSION_VIEW_UNSPECIFIED", "BASIC", "FULL"
                            ] = ...,
                            **kwargs: typing.Any,
                        ) -> ListVersionsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListVersionsResponseHttpRequest,
                            previous_response: ListVersionsResponse,
                        ) -> ListVersionsResponseHttpRequest | None: ...
                        def patch(
                            self,
                            *,
                            name: str,
                            body: Version = ...,
                            updateMask: str = ...,
                            **kwargs: typing.Any,
                        ) -> VersionHttpRequest: ...

                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> PackageHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        orderBy: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListPackagesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListPackagesResponseHttpRequest,
                        previous_response: ListPackagesResponse,
                    ) -> ListPackagesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: Package = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> PackageHttpRequest: ...
                    def tags(self) -> TagsResource: ...
                    def versions(self) -> VersionsResource: ...

                @typing.type_check_only
                class PythonPackagesResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> PythonPackageHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListPythonPackagesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListPythonPackagesResponseHttpRequest,
                        previous_response: ListPythonPackagesResponse,
                    ) -> ListPythonPackagesResponseHttpRequest | None: ...

                @typing.type_check_only
                class RulesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleDevtoolsArtifactregistryV1Rule = ...,
                        ruleId: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleDevtoolsArtifactregistryV1RuleHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleDevtoolsArtifactregistryV1RuleHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListRulesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListRulesResponseHttpRequest,
                        previous_response: ListRulesResponse,
                    ) -> ListRulesResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleDevtoolsArtifactregistryV1Rule = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> GoogleDevtoolsArtifactregistryV1RuleHttpRequest: ...

                @typing.type_check_only
                class YumArtifactsResource(googleapiclient.discovery.Resource):
                    def import_(
                        self,
                        *,
                        parent: str,
                        body: ImportYumArtifactsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def upload(
                        self,
                        *,
                        parent: str,
                        body: UploadYumArtifactRequest = ...,
                        **kwargs: typing.Any,
                    ) -> UploadYumArtifactMediaResponseHttpRequest: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Repository = ...,
                    repositoryId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> RepositoryHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    options_requestedPolicyVersion: int = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    orderBy: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListRepositoriesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListRepositoriesResponseHttpRequest,
                    previous_response: ListRepositoriesResponse,
                ) -> ListRepositoriesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Repository = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> RepositoryHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...
                def aptArtifacts(self) -> AptArtifactsResource: ...
                def attachments(self) -> AttachmentsResource: ...
                def dockerImages(self) -> DockerImagesResource: ...
                def files(self) -> FilesResource: ...
                def genericArtifacts(self) -> GenericArtifactsResource: ...
                def goModules(self) -> GoModulesResource: ...
                def googetArtifacts(self) -> GoogetArtifactsResource: ...
                def kfpArtifacts(self) -> KfpArtifactsResource: ...
                def mavenArtifacts(self) -> MavenArtifactsResource: ...
                def npmPackages(self) -> NpmPackagesResource: ...
                def packages(self) -> PackagesResource: ...
                def pythonPackages(self) -> PythonPackagesResource: ...
                def rules(self) -> RulesResource: ...
                def yumArtifacts(self) -> YumArtifactsResource: ...

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def getVpcscConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> VPCSCConfigHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def updateVpcscConfig(
                self,
                *,
                name: str,
                body: VPCSCConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> VPCSCConfigHttpRequest: ...
            def operations(self) -> OperationsResource: ...
            def repositories(self) -> RepositoriesResource: ...

        def getProjectSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> ProjectSettingsHttpRequest: ...
        def updateProjectSettings(
            self,
            *,
            name: str,
            body: ProjectSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> ProjectSettingsHttpRequest: ...
        def locations(self) -> LocationsResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class AttachmentHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Attachment: ...

@typing.type_check_only
class DockerImageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DockerImage: ...

@typing.type_check_only
class DownloadFileResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DownloadFileResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class GoogleDevtoolsArtifactregistryV1FileHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleDevtoolsArtifactregistryV1File: ...

@typing.type_check_only
class GoogleDevtoolsArtifactregistryV1RuleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleDevtoolsArtifactregistryV1Rule: ...

@typing.type_check_only
class ListAttachmentsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAttachmentsResponse: ...

@typing.type_check_only
class ListDockerImagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDockerImagesResponse: ...

@typing.type_check_only
class ListFilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListFilesResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListMavenArtifactsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMavenArtifactsResponse: ...

@typing.type_check_only
class ListNpmPackagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListNpmPackagesResponse: ...

@typing.type_check_only
class ListPackagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPackagesResponse: ...

@typing.type_check_only
class ListPythonPackagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPythonPackagesResponse: ...

@typing.type_check_only
class ListRepositoriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRepositoriesResponse: ...

@typing.type_check_only
class ListRulesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRulesResponse: ...

@typing.type_check_only
class ListTagsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListTagsResponse: ...

@typing.type_check_only
class ListVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListVersionsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class MavenArtifactHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> MavenArtifact: ...

@typing.type_check_only
class NpmPackageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> NpmPackage: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class PackageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Package: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class ProjectSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ProjectSettings: ...

@typing.type_check_only
class PythonPackageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PythonPackage: ...

@typing.type_check_only
class RepositoryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Repository: ...

@typing.type_check_only
class TagHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Tag: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...

@typing.type_check_only
class UploadAptArtifactMediaResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UploadAptArtifactMediaResponse: ...

@typing.type_check_only
class UploadFileMediaResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UploadFileMediaResponse: ...

@typing.type_check_only
class UploadGenericArtifactMediaResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UploadGenericArtifactMediaResponse: ...

@typing.type_check_only
class UploadGoModuleMediaResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UploadGoModuleMediaResponse: ...

@typing.type_check_only
class UploadGoogetArtifactMediaResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UploadGoogetArtifactMediaResponse: ...

@typing.type_check_only
class UploadKfpArtifactMediaResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UploadKfpArtifactMediaResponse: ...

@typing.type_check_only
class UploadYumArtifactMediaResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UploadYumArtifactMediaResponse: ...

@typing.type_check_only
class VPCSCConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> VPCSCConfig: ...

@typing.type_check_only
class VersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Version: ...

@typing.type_check_only
class BytesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> bytes: ...

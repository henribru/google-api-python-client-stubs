import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class FirebaseHostingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        @typing.type_check_only
        class SitesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ChannelsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ReleasesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Release = ...,
                        versionName: str = ...,
                        **kwargs: typing.Any
                    ) -> ReleaseHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListReleasesResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: Channel = ...,
                    channelId: str = ...,
                    **kwargs: typing.Any
                ) -> ChannelHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ChannelHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListChannelsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Channel = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> ChannelHttpRequest: ...
                def releases(self) -> ReleasesResource: ...
            @typing.type_check_only
            class DomainsResource(googleapiclient.discovery.Resource):
                def create(
                    self, *, parent: str, body: Domain = ..., **kwargs: typing.Any
                ) -> DomainHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DomainHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListDomainsResponseHttpRequest: ...
                def update(
                    self, *, name: str, body: Domain = ..., **kwargs: typing.Any
                ) -> DomainHttpRequest: ...
            @typing.type_check_only
            class ReleasesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Release = ...,
                    versionName: str = ...,
                    **kwargs: typing.Any
                ) -> ReleaseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListReleasesResponseHttpRequest: ...
            @typing.type_check_only
            class VersionsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class FilesResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        status: typing_extensions.Literal[
                            "STATUS_UNSPECIFIED", "EXPECTED", "ACTIVE"
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> ListVersionFilesResponseHttpRequest: ...
                def clone(
                    self,
                    *,
                    parent: str,
                    body: CloneVersionRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: Version = ...,
                    sizeBytes: str = ...,
                    versionId: str = ...,
                    **kwargs: typing.Any
                ) -> VersionHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListVersionsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Version = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> VersionHttpRequest: ...
                def populateFiles(
                    self,
                    *,
                    parent: str,
                    body: PopulateVersionFilesRequest = ...,
                    **kwargs: typing.Any
                ) -> PopulateVersionFilesResponseHttpRequest: ...
                def files(self) -> FilesResource: ...
            def getConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> SiteConfigHttpRequest: ...
            def updateConfig(
                self,
                *,
                name: str,
                body: SiteConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SiteConfigHttpRequest: ...
            def channels(self) -> ChannelsResource: ...
            def domains(self) -> DomainsResource: ...
            def releases(self) -> ReleasesResource: ...
            def versions(self) -> VersionsResource: ...
        def operations(self) -> OperationsResource: ...
        def sites(self) -> SitesResource: ...
    @typing.type_check_only
    class SitesResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ChannelsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ReleasesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Release = ...,
                    versionName: str = ...,
                    **kwargs: typing.Any
                ) -> ReleaseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListReleasesResponseHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: Channel = ...,
                channelId: str = ...,
                **kwargs: typing.Any
            ) -> ChannelHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> ChannelHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListChannelsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Channel = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> ChannelHttpRequest: ...
            def releases(self) -> ReleasesResource: ...
        @typing.type_check_only
        class DomainsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: Domain = ..., **kwargs: typing.Any
            ) -> DomainHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> DomainHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListDomainsResponseHttpRequest: ...
            def update(
                self, *, name: str, body: Domain = ..., **kwargs: typing.Any
            ) -> DomainHttpRequest: ...
        @typing.type_check_only
        class ReleasesResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: Release = ...,
                versionName: str = ...,
                **kwargs: typing.Any
            ) -> ReleaseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListReleasesResponseHttpRequest: ...
        @typing.type_check_only
        class VersionsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class FilesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    status: typing_extensions.Literal[
                        "STATUS_UNSPECIFIED", "EXPECTED", "ACTIVE"
                    ] = ...,
                    **kwargs: typing.Any
                ) -> ListVersionFilesResponseHttpRequest: ...
            def clone(
                self,
                *,
                parent: str,
                body: CloneVersionRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: Version = ...,
                sizeBytes: str = ...,
                versionId: str = ...,
                **kwargs: typing.Any
            ) -> VersionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListVersionsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Version = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> VersionHttpRequest: ...
            def populateFiles(
                self,
                *,
                parent: str,
                body: PopulateVersionFilesRequest = ...,
                **kwargs: typing.Any
            ) -> PopulateVersionFilesResponseHttpRequest: ...
            def files(self) -> FilesResource: ...
        def getConfig(
            self, *, name: str, **kwargs: typing.Any
        ) -> SiteConfigHttpRequest: ...
        def updateConfig(
            self,
            *,
            name: str,
            body: SiteConfig = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> SiteConfigHttpRequest: ...
        def channels(self) -> ChannelsResource: ...
        def domains(self) -> DomainsResource: ...
        def releases(self) -> ReleasesResource: ...
        def versions(self) -> VersionsResource: ...
    def projects(self) -> ProjectsResource: ...
    def sites(self) -> SitesResource: ...

@typing.type_check_only
class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Channel: ...

@typing.type_check_only
class DomainHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Domain: ...

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
class ListChannelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListChannelsResponse: ...

@typing.type_check_only
class ListDomainsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListDomainsResponse: ...

@typing.type_check_only
class ListReleasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListReleasesResponse: ...

@typing.type_check_only
class ListVersionFilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListVersionFilesResponse: ...

@typing.type_check_only
class ListVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListVersionsResponse: ...

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
class PopulateVersionFilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> PopulateVersionFilesResponse: ...

@typing.type_check_only
class ReleaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Release: ...

@typing.type_check_only
class SiteConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> SiteConfig: ...

@typing.type_check_only
class VersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Version: ...

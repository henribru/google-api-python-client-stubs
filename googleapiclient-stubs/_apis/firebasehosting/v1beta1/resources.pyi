import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class FirebaseHostingResource(googleapiclient.discovery.Resource):
    class SitesResource(googleapiclient.discovery.Resource):
        class ChannelsResource(googleapiclient.discovery.Resource):
            class ReleasesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListReleasesResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: Release = ...,
                    versionName: str = ...,
                    **kwargs: typing.Any
                ) -> ReleaseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: Channel = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> ChannelHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: Channel = ...,
                channelId: str = ...,
                **kwargs: typing.Any
            ) -> ChannelHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> ChannelHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListChannelsResponseHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def releases(self) -> ReleasesResource: ...
        class DomainsResource(googleapiclient.discovery.Resource):
            def update(
                self, *, name: str, body: Domain = ..., **kwargs: typing.Any
            ) -> DomainHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> DomainHttpRequest: ...
            def create(
                self, *, parent: str, body: Domain = ..., **kwargs: typing.Any
            ) -> DomainHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListDomainsResponseHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
        class ReleasesResource(googleapiclient.discovery.Resource):
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
                body: Release = ...,
                versionName: str = ...,
                **kwargs: typing.Any
            ) -> ReleaseHttpRequest: ...
        class VersionsResource(googleapiclient.discovery.Resource):
            class FilesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    status: typing_extensions.Literal[
                        "STATUS_UNSPECIFIED", "EXPECTED", "ACTIVE"
                    ] = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
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
            def patch(
                self,
                *,
                name: str,
                body: Version = ...,
                updateMask: str = ...,
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
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListVersionsResponseHttpRequest: ...
            def populateFiles(
                self,
                *,
                parent: str,
                body: PopulateVersionFilesRequest = ...,
                **kwargs: typing.Any
            ) -> PopulateVersionFilesResponseHttpRequest: ...
            def files(self) -> FilesResource: ...
        def updateConfig(
            self,
            *,
            name: str,
            body: SiteConfig = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> SiteConfigHttpRequest: ...
        def getConfig(
            self, *, name: str, **kwargs: typing.Any
        ) -> SiteConfigHttpRequest: ...
        def channels(self) -> ChannelsResource: ...
        def domains(self) -> DomainsResource: ...
        def releases(self) -> ReleasesResource: ...
        def versions(self) -> VersionsResource: ...
    class ProjectsResource(googleapiclient.discovery.Resource):
        class SitesResource(googleapiclient.discovery.Resource):
            class ReleasesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListReleasesResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: Release = ...,
                    versionName: str = ...,
                    **kwargs: typing.Any
                ) -> ReleaseHttpRequest: ...
            class ChannelsResource(googleapiclient.discovery.Resource):
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
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> ListReleasesResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Channel = ...,
                    updateMask: str = ...,
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
                def create(
                    self,
                    *,
                    parent: str,
                    body: Channel = ...,
                    channelId: str = ...,
                    **kwargs: typing.Any
                ) -> ChannelHttpRequest: ...
                def releases(self) -> ReleasesResource: ...
            class DomainsResource(googleapiclient.discovery.Resource):
                def update(
                    self, *, name: str, body: Domain = ..., **kwargs: typing.Any
                ) -> DomainHttpRequest: ...
                def create(
                    self, *, parent: str, body: Domain = ..., **kwargs: typing.Any
                ) -> DomainHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListDomainsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DomainHttpRequest: ...
            class VersionsResource(googleapiclient.discovery.Resource):
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
                def create(
                    self,
                    *,
                    parent: str,
                    body: Version = ...,
                    sizeBytes: str = ...,
                    versionId: str = ...,
                    **kwargs: typing.Any
                ) -> VersionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    filter: str = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListVersionsResponseHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def populateFiles(
                    self,
                    *,
                    parent: str,
                    body: PopulateVersionFilesRequest = ...,
                    **kwargs: typing.Any
                ) -> PopulateVersionFilesResponseHttpRequest: ...
                def clone(
                    self,
                    *,
                    parent: str,
                    body: CloneVersionRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Version = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> VersionHttpRequest: ...
                def files(self) -> FilesResource: ...
            def updateConfig(
                self,
                *,
                name: str,
                body: SiteConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SiteConfigHttpRequest: ...
            def getConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> SiteConfigHttpRequest: ...
            def releases(self) -> ReleasesResource: ...
            def channels(self) -> ChannelsResource: ...
            def domains(self) -> DomainsResource: ...
            def versions(self) -> VersionsResource: ...
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        def sites(self) -> SitesResource: ...
        def operations(self) -> OperationsResource: ...
    def sites(self) -> SitesResource: ...
    def projects(self) -> ProjectsResource: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class DomainHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Domain: ...

class ListChannelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListChannelsResponse: ...

class ListVersionFilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListVersionFilesResponse: ...

class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Channel: ...

class ListDomainsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDomainsResponse: ...

class VersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Version: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class ReleaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Release: ...

class ListReleasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListReleasesResponse: ...

class PopulateVersionFilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PopulateVersionFilesResponse: ...

class SiteConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SiteConfig: ...

class ListVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListVersionsResponse: ...

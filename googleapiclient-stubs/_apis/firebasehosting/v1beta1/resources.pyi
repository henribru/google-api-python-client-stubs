import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

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
                    def list_next(
                        self,
                        previous_request: ListReleasesResponseHttpRequest,
                        previous_response: ListReleasesResponse,
                    ) -> ListReleasesResponseHttpRequest | None: ...

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
                def list_next(
                    self,
                    previous_request: ListChannelsResponseHttpRequest,
                    previous_response: ListChannelsResponse,
                ) -> ListChannelsResponseHttpRequest | None: ...
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
                def list_next(
                    self,
                    previous_request: ListDomainsResponseHttpRequest,
                    previous_response: ListDomainsResponse,
                ) -> ListDomainsResponseHttpRequest | None: ...
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
                def list_next(
                    self,
                    previous_request: ListReleasesResponseHttpRequest,
                    previous_response: ListReleasesResponse,
                ) -> ListReleasesResponseHttpRequest | None: ...

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
                    def list_next(
                        self,
                        previous_request: ListVersionFilesResponseHttpRequest,
                        previous_response: ListVersionFilesResponse,
                    ) -> ListVersionFilesResponseHttpRequest | None: ...

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

            def create(
                self,
                *,
                parent: str,
                body: Site = ...,
                siteId: str = ...,
                **kwargs: typing.Any
            ) -> SiteHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> SiteHttpRequest: ...
            def getConfig(
                self, *, name: str, **kwargs: typing.Any
            ) -> SiteConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListSitesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListSitesResponseHttpRequest,
                previous_response: ListSitesResponse,
            ) -> ListSitesResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Site = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> SiteHttpRequest: ...
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
                def list_next(
                    self,
                    previous_request: ListReleasesResponseHttpRequest,
                    previous_response: ListReleasesResponse,
                ) -> ListReleasesResponseHttpRequest | None: ...

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
            def list_next(
                self,
                previous_request: ListChannelsResponseHttpRequest,
                previous_response: ListChannelsResponse,
            ) -> ListChannelsResponseHttpRequest | None: ...
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
            def list_next(
                self,
                previous_request: ListDomainsResponseHttpRequest,
                previous_response: ListDomainsResponse,
            ) -> ListDomainsResponseHttpRequest | None: ...
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
            def list_next(
                self,
                previous_request: ListReleasesResponseHttpRequest,
                previous_response: ListReleasesResponse,
            ) -> ListReleasesResponseHttpRequest | None: ...

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
                def list_next(
                    self,
                    previous_request: ListVersionFilesResponseHttpRequest,
                    previous_response: ListVersionFilesResponse,
                ) -> ListVersionFilesResponseHttpRequest | None: ...

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
    def sites(self) -> SitesResource: ...

@typing.type_check_only
class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Channel: ...

@typing.type_check_only
class DomainHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Domain: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListChannelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListChannelsResponse: ...

@typing.type_check_only
class ListDomainsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDomainsResponse: ...

@typing.type_check_only
class ListReleasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListReleasesResponse: ...

@typing.type_check_only
class ListSitesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListSitesResponse: ...

@typing.type_check_only
class ListVersionFilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListVersionFilesResponse: ...

@typing.type_check_only
class ListVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListVersionsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class PopulateVersionFilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> PopulateVersionFilesResponse: ...

@typing.type_check_only
class ReleaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Release: ...

@typing.type_check_only
class SiteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Site: ...

@typing.type_check_only
class SiteConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SiteConfig: ...

@typing.type_check_only
class VersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Version: ...

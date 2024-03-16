import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

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
                        **kwargs: typing.Any,
                    ) -> ReleaseHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ReleaseHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> ChannelHttpRequest: ...
                def releases(self) -> ReleasesResource: ...

            @typing.type_check_only
            class CustomDomainsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class OperationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def list(
                        self,
                        *,
                        name: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListOperationsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListOperationsResponseHttpRequest,
                        previous_response: ListOperationsResponse,
                    ) -> ListOperationsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: CustomDomain = ...,
                    customDomainId: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    allowMissing: bool = ...,
                    etag: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> CustomDomainHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    showDeleted: bool = ...,
                    **kwargs: typing.Any,
                ) -> ListCustomDomainsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListCustomDomainsResponseHttpRequest,
                    previous_response: ListCustomDomainsResponse,
                ) -> ListCustomDomainsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: CustomDomain = ...,
                    allowMissing: bool = ...,
                    updateMask: str = ...,
                    validateOnly: bool = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def undelete(
                    self,
                    *,
                    name: str,
                    body: UndeleteCustomDomainRequest = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def operations(self) -> OperationsResource: ...

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
                    **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> ReleaseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ReleaseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
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
                        **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: Version = ...,
                    sizeBytes: str = ...,
                    versionId: str = ...,
                    **kwargs: typing.Any,
                ) -> VersionHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> VersionHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
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
                def populateFiles(
                    self,
                    *,
                    parent: str,
                    body: PopulateVersionFilesRequest = ...,
                    **kwargs: typing.Any,
                ) -> PopulateVersionFilesResponseHttpRequest: ...
                def files(self) -> FilesResource: ...

            def create(
                self,
                *,
                parent: str,
                body: Site = ...,
                siteId: str = ...,
                validateOnly: bool = ...,
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
            ) -> SiteHttpRequest: ...
            def updateConfig(
                self,
                *,
                name: str,
                body: SiteConfig = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> SiteConfigHttpRequest: ...
            def channels(self) -> ChannelsResource: ...
            def customDomains(self) -> CustomDomainsResource: ...
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
                    **kwargs: typing.Any,
                ) -> ReleaseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ReleaseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
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
                **kwargs: typing.Any,
            ) -> ReleaseHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> ReleaseHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
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
                    **kwargs: typing.Any,
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
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: Version = ...,
                sizeBytes: str = ...,
                versionId: str = ...,
                **kwargs: typing.Any,
            ) -> VersionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> VersionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
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
            def populateFiles(
                self,
                *,
                parent: str,
                body: PopulateVersionFilesRequest = ...,
                **kwargs: typing.Any,
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
            **kwargs: typing.Any,
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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def projects(self) -> ProjectsResource: ...
    def sites(self) -> SitesResource: ...

@typing.type_check_only
class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Channel: ...

@typing.type_check_only
class CustomDomainHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CustomDomain: ...

@typing.type_check_only
class DomainHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Domain: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class ListChannelsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListChannelsResponse: ...

@typing.type_check_only
class ListCustomDomainsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCustomDomainsResponse: ...

@typing.type_check_only
class ListDomainsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDomainsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListReleasesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListReleasesResponse: ...

@typing.type_check_only
class ListSitesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSitesResponse: ...

@typing.type_check_only
class ListVersionFilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListVersionFilesResponse: ...

@typing.type_check_only
class ListVersionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListVersionsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class PopulateVersionFilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PopulateVersionFilesResponse: ...

@typing.type_check_only
class ReleaseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Release: ...

@typing.type_check_only
class SiteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Site: ...

@typing.type_check_only
class SiteConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SiteConfig: ...

@typing.type_check_only
class VersionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Version: ...

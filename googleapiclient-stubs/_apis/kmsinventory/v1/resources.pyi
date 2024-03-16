import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class KmsinventoryResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ProtectedResourcesResource(googleapiclient.discovery.Resource):
            def search(
                self,
                *,
                scope: str,
                cryptoKey: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                resourceTypes: str | _list[str] = ...,
                **kwargs: typing.Any,
            ) -> (
                GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseHttpRequest
            ): ...
            def search_next(
                self,
                previous_request: GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseHttpRequest,
                previous_response: GoogleCloudKmsInventoryV1SearchProtectedResourcesResponse,
            ) -> (
                GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseHttpRequest
                | None
            ): ...

        def protectedResources(self) -> ProtectedResourcesResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class CryptoKeysResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> GoogleCloudKmsInventoryV1ListCryptoKeysResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: GoogleCloudKmsInventoryV1ListCryptoKeysResponseHttpRequest,
                previous_response: GoogleCloudKmsInventoryV1ListCryptoKeysResponse,
            ) -> GoogleCloudKmsInventoryV1ListCryptoKeysResponseHttpRequest | None: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class KeyRingsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class CryptoKeysResource(googleapiclient.discovery.Resource):
                    def getProtectedResourcesSummary(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> (
                        GoogleCloudKmsInventoryV1ProtectedResourcesSummaryHttpRequest
                    ): ...

                def cryptoKeys(self) -> CryptoKeysResource: ...

            def keyRings(self) -> KeyRingsResource: ...

        def cryptoKeys(self) -> CryptoKeysResource: ...
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
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudKmsInventoryV1ListCryptoKeysResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudKmsInventoryV1ListCryptoKeysResponse: ...

@typing.type_check_only
class GoogleCloudKmsInventoryV1ProtectedResourcesSummaryHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudKmsInventoryV1ProtectedResourcesSummary: ...

@typing.type_check_only
class GoogleCloudKmsInventoryV1SearchProtectedResourcesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GoogleCloudKmsInventoryV1SearchProtectedResourcesResponse: ...

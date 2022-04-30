import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class FirestoreResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DatabasesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CollectionGroupsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class FieldsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleFirestoreAdminV1beta2FieldHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleFirestoreAdminV1beta2ListFieldsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleFirestoreAdminV1beta2ListFieldsResponseHttpRequest,
                        previous_response: GoogleFirestoreAdminV1beta2ListFieldsResponse,
                    ) -> GoogleFirestoreAdminV1beta2ListFieldsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: GoogleFirestoreAdminV1beta2Field = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...

                @typing.type_check_only
                class IndexesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: GoogleFirestoreAdminV1beta2Index = ...,
                        **kwargs: typing.Any
                    ) -> GoogleLongrunningOperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleFirestoreAdminV1beta2IndexHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        filter: str = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleFirestoreAdminV1beta2ListIndexesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleFirestoreAdminV1beta2ListIndexesResponseHttpRequest,
                        previous_response: GoogleFirestoreAdminV1beta2ListIndexesResponse,
                    ) -> GoogleFirestoreAdminV1beta2ListIndexesResponseHttpRequest | None: ...

                def fields(self) -> FieldsResource: ...
                def indexes(self) -> IndexesResource: ...

            def exportDocuments(
                self,
                *,
                name: str,
                body: GoogleFirestoreAdminV1beta2ExportDocumentsRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def importDocuments(
                self,
                *,
                name: str,
                body: GoogleFirestoreAdminV1beta2ImportDocumentsRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleLongrunningOperationHttpRequest: ...
            def collectionGroups(self) -> CollectionGroupsResource: ...

        def databases(self) -> DatabasesResource: ...

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

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class GoogleFirestoreAdminV1beta2FieldHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirestoreAdminV1beta2Field: ...

@typing.type_check_only
class GoogleFirestoreAdminV1beta2IndexHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirestoreAdminV1beta2Index: ...

@typing.type_check_only
class GoogleFirestoreAdminV1beta2ListFieldsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirestoreAdminV1beta2ListFieldsResponse: ...

@typing.type_check_only
class GoogleFirestoreAdminV1beta2ListIndexesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleFirestoreAdminV1beta2ListIndexesResponse: ...

@typing.type_check_only
class GoogleLongrunningOperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleLongrunningOperation: ...

import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class VisionResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class FilesResource(googleapiclient.discovery.Resource):
        def annotate(
            self, *, body: BatchAnnotateFilesRequest = ..., **kwargs: typing.Any
        ) -> BatchAnnotateFilesResponseHttpRequest: ...
        def asyncBatchAnnotate(
            self, *, body: AsyncBatchAnnotateFilesRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
    class ImagesResource(googleapiclient.discovery.Resource):
        def annotate(
            self, *, body: BatchAnnotateImagesRequest = ..., **kwargs: typing.Any
        ) -> BatchAnnotateImagesResponseHttpRequest: ...
        def asyncBatchAnnotate(
            self, *, body: AsyncBatchAnnotateImagesRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
    class LocationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        def operations(self) -> OperationsResource: ...

    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def cancel(
            self, *, name: str, body: CancelOperationRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
        def list(
            self,
            *,
            name: str,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListOperationsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListOperationsResponseHttpRequest,
            previous_response: ListOperationsResponse,
        ) -> ListOperationsResponseHttpRequest | None: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class FilesResource(googleapiclient.discovery.Resource):
            def annotate(
                self,
                *,
                parent: str,
                body: BatchAnnotateFilesRequest = ...,
                **kwargs: typing.Any
            ) -> BatchAnnotateFilesResponseHttpRequest: ...
            def asyncBatchAnnotate(
                self,
                *,
                parent: str,
                body: AsyncBatchAnnotateFilesRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        @typing.type_check_only
        class ImagesResource(googleapiclient.discovery.Resource):
            def annotate(
                self,
                *,
                parent: str,
                body: BatchAnnotateImagesRequest = ...,
                **kwargs: typing.Any
            ) -> BatchAnnotateImagesResponseHttpRequest: ...
            def asyncBatchAnnotate(
                self,
                *,
                parent: str,
                body: AsyncBatchAnnotateImagesRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class FilesResource(googleapiclient.discovery.Resource):
                def annotate(
                    self,
                    *,
                    parent: str,
                    body: BatchAnnotateFilesRequest = ...,
                    **kwargs: typing.Any
                ) -> BatchAnnotateFilesResponseHttpRequest: ...
                def asyncBatchAnnotate(
                    self,
                    *,
                    parent: str,
                    body: AsyncBatchAnnotateFilesRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class ImagesResource(googleapiclient.discovery.Resource):
                def annotate(
                    self,
                    *,
                    parent: str,
                    body: BatchAnnotateImagesRequest = ...,
                    **kwargs: typing.Any
                ) -> BatchAnnotateImagesResponseHttpRequest: ...
                def asyncBatchAnnotate(
                    self,
                    *,
                    parent: str,
                    body: AsyncBatchAnnotateImagesRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class ProductSetsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ProductsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        name: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListProductsInProductSetResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListProductsInProductSetResponseHttpRequest,
                        previous_response: ListProductsInProductSetResponse,
                    ) -> ListProductsInProductSetResponseHttpRequest | None: ...

                def addProduct(
                    self,
                    *,
                    name: str,
                    body: AddProductToProductSetRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: ProductSet = ...,
                    productSetId: str = ...,
                    **kwargs: typing.Any
                ) -> ProductSetHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ProductSetHttpRequest: ...
                def import_(
                    self,
                    *,
                    parent: str,
                    body: ImportProductSetsRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListProductSetsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListProductSetsResponseHttpRequest,
                    previous_response: ListProductSetsResponse,
                ) -> ListProductSetsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ProductSet = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> ProductSetHttpRequest: ...
                def removeProduct(
                    self,
                    *,
                    name: str,
                    body: RemoveProductFromProductSetRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def products(self) -> ProductsResource: ...

            @typing.type_check_only
            class ProductsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class ReferenceImagesResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: ReferenceImage = ...,
                        referenceImageId: str = ...,
                        **kwargs: typing.Any
                    ) -> ReferenceImageHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ReferenceImageHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListReferenceImagesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListReferenceImagesResponseHttpRequest,
                        previous_response: ListReferenceImagesResponse,
                    ) -> ListReferenceImagesResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: Product = ...,
                    productId: str = ...,
                    **kwargs: typing.Any
                ) -> ProductHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ProductHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListProductsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListProductsResponseHttpRequest,
                    previous_response: ListProductsResponse,
                ) -> ListProductsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Product = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> ProductHttpRequest: ...
                def purge(
                    self,
                    *,
                    parent: str,
                    body: PurgeProductsRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def referenceImages(self) -> ReferenceImagesResource: ...

            def files(self) -> FilesResource: ...
            def images(self) -> ImagesResource: ...
            def operations(self) -> OperationsResource: ...
            def productSets(self) -> ProductSetsResource: ...
            def products(self) -> ProductsResource: ...

        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        def files(self) -> FilesResource: ...
        def images(self) -> ImagesResource: ...
        def locations(self) -> LocationsResource: ...
        def operations(self) -> OperationsResource: ...

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
    def files(self) -> FilesResource: ...
    def images(self) -> ImagesResource: ...
    def locations(self) -> LocationsResource: ...
    def operations(self) -> OperationsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class BatchAnnotateFilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchAnnotateFilesResponse: ...

@typing.type_check_only
class BatchAnnotateImagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> BatchAnnotateImagesResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListProductSetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListProductSetsResponse: ...

@typing.type_check_only
class ListProductsInProductSetResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListProductsInProductSetResponse: ...

@typing.type_check_only
class ListProductsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListProductsResponse: ...

@typing.type_check_only
class ListReferenceImagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListReferenceImagesResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

@typing.type_check_only
class ProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Product: ...

@typing.type_check_only
class ProductSetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ProductSet: ...

@typing.type_check_only
class ReferenceImageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ReferenceImage: ...

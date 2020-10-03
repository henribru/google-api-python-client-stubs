import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class VisionResource(googleapiclient.discovery.Resource):
    class ImagesResource(googleapiclient.discovery.Resource):
        def annotate(
            self, *, body: BatchAnnotateImagesRequest = ..., **kwargs: typing.Any
        ) -> BatchAnnotateImagesResponseHttpRequest: ...
        def asyncBatchAnnotate(
            self, *, body: AsyncBatchAnnotateImagesRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class ProjectsResource(googleapiclient.discovery.Resource):
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
        class ImagesResource(googleapiclient.discovery.Resource):
            def asyncBatchAnnotate(
                self,
                *,
                parent: str,
                body: AsyncBatchAnnotateImagesRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def annotate(
                self,
                *,
                parent: str,
                body: BatchAnnotateImagesRequest = ...,
                **kwargs: typing.Any
            ) -> BatchAnnotateImagesResponseHttpRequest: ...
        class LocationsResource(googleapiclient.discovery.Resource):
            class ProductsResource(googleapiclient.discovery.Resource):
                class ReferenceImagesResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListReferenceImagesResponseHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: ReferenceImage = ...,
                        referenceImageId: str = ...,
                        **kwargs: typing.Any
                    ) -> ReferenceImageHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> ReferenceImageHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Product = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> ProductHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ProductHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: Product = ...,
                    productId: str = ...,
                    **kwargs: typing.Any
                ) -> ProductHttpRequest: ...
                def purge(
                    self,
                    *,
                    parent: str,
                    body: PurgeProductsRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListProductsResponseHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def referenceImages(self) -> ReferenceImagesResource: ...
            class ImagesResource(googleapiclient.discovery.Resource):
                def asyncBatchAnnotate(
                    self,
                    *,
                    parent: str,
                    body: AsyncBatchAnnotateImagesRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def annotate(
                    self,
                    *,
                    parent: str,
                    body: BatchAnnotateImagesRequest = ...,
                    **kwargs: typing.Any
                ) -> BatchAnnotateImagesResponseHttpRequest: ...
            class FilesResource(googleapiclient.discovery.Resource):
                def asyncBatchAnnotate(
                    self,
                    *,
                    parent: str,
                    body: AsyncBatchAnnotateFilesRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def annotate(
                    self,
                    *,
                    parent: str,
                    body: BatchAnnotateFilesRequest = ...,
                    **kwargs: typing.Any
                ) -> BatchAnnotateFilesResponseHttpRequest: ...
            class ProductSetsResource(googleapiclient.discovery.Resource):
                class ProductsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        name: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListProductsInProductSetResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: ProductSet = ...,
                    productSetId: str = ...,
                    **kwargs: typing.Any
                ) -> ProductSetHttpRequest: ...
                def import_(
                    self,
                    *,
                    parent: str,
                    body: ImportProductSetsRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def removeProduct(
                    self,
                    *,
                    name: str,
                    body: RemoveProductFromProductSetRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def addProduct(
                    self,
                    *,
                    name: str,
                    body: AddProductToProductSetRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListProductSetsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> ProductSetHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: ProductSet = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> ProductSetHttpRequest: ...
                def products(self) -> ProductsResource: ...
            class OperationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
            def products(self) -> ProductsResource: ...
            def images(self) -> ImagesResource: ...
            def files(self) -> FilesResource: ...
            def productSets(self) -> ProductSetsResource: ...
            def operations(self) -> OperationsResource: ...
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        def files(self) -> FilesResource: ...
        def images(self) -> ImagesResource: ...
        def locations(self) -> LocationsResource: ...
        def operations(self) -> OperationsResource: ...
    class OperationsResource(googleapiclient.discovery.Resource):
        def cancel(
            self, *, name: str, body: CancelOperationRequest = ..., **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def list(
            self,
            *,
            name: str,
            pageToken: str = ...,
            filter: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListOperationsResponseHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
    class FilesResource(googleapiclient.discovery.Resource):
        def asyncBatchAnnotate(
            self, *, body: AsyncBatchAnnotateFilesRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def annotate(
            self, *, body: BatchAnnotateFilesRequest = ..., **kwargs: typing.Any
        ) -> BatchAnnotateFilesResponseHttpRequest: ...
    class LocationsResource(googleapiclient.discovery.Resource):
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        def operations(self) -> OperationsResource: ...
    def images(self) -> ImagesResource: ...
    def projects(self) -> ProjectsResource: ...
    def operations(self) -> OperationsResource: ...
    def files(self) -> FilesResource: ...
    def locations(self) -> LocationsResource: ...

class BatchAnnotateImagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchAnnotateImagesResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ProductSetHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ProductSet: ...

class ListProductsInProductSetResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListProductsInProductSetResponse: ...

class ListProductsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListProductsResponse: ...

class BatchAnnotateFilesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchAnnotateFilesResponse: ...

class ListProductSetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListProductSetsResponse: ...

class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOperationsResponse: ...

class ProductHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Product: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class ListReferenceImagesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListReferenceImagesResponse: ...

class ReferenceImageHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReferenceImage: ...

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
            self,
            *,
            body: GoogleCloudVisionV1p2beta1BatchAnnotateFilesRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudVisionV1p2beta1BatchAnnotateFilesResponseHttpRequest: ...
        def asyncBatchAnnotate(
            self,
            *,
            body: GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
    class ImagesResource(googleapiclient.discovery.Resource):
        def annotate(
            self,
            *,
            body: GoogleCloudVisionV1p2beta1BatchAnnotateImagesRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleCloudVisionV1p2beta1BatchAnnotateImagesResponseHttpRequest: ...
        def asyncBatchAnnotate(
            self,
            *,
            body: GoogleCloudVisionV1p2beta1AsyncBatchAnnotateImagesRequest = ...,
            **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class FilesResource(googleapiclient.discovery.Resource):
            def annotate(
                self,
                *,
                parent: str,
                body: GoogleCloudVisionV1p2beta1BatchAnnotateFilesRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudVisionV1p2beta1BatchAnnotateFilesResponseHttpRequest: ...
            def asyncBatchAnnotate(
                self,
                *,
                parent: str,
                body: GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        @typing.type_check_only
        class ImagesResource(googleapiclient.discovery.Resource):
            def annotate(
                self,
                *,
                parent: str,
                body: GoogleCloudVisionV1p2beta1BatchAnnotateImagesRequest = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudVisionV1p2beta1BatchAnnotateImagesResponseHttpRequest: ...
            def asyncBatchAnnotate(
                self,
                *,
                parent: str,
                body: GoogleCloudVisionV1p2beta1AsyncBatchAnnotateImagesRequest = ...,
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
                    body: GoogleCloudVisionV1p2beta1BatchAnnotateFilesRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudVisionV1p2beta1BatchAnnotateFilesResponseHttpRequest: ...
                def asyncBatchAnnotate(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudVisionV1p2beta1AsyncBatchAnnotateFilesRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            @typing.type_check_only
            class ImagesResource(googleapiclient.discovery.Resource):
                def annotate(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudVisionV1p2beta1BatchAnnotateImagesRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudVisionV1p2beta1BatchAnnotateImagesResponseHttpRequest: ...
                def asyncBatchAnnotate(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudVisionV1p2beta1AsyncBatchAnnotateImagesRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...

            def files(self) -> FilesResource: ...
            def images(self) -> ImagesResource: ...

        def files(self) -> FilesResource: ...
        def images(self) -> ImagesResource: ...
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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def files(self) -> FilesResource: ...
    def images(self) -> ImagesResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudVisionV1p2beta1BatchAnnotateFilesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudVisionV1p2beta1BatchAnnotateFilesResponse: ...

@typing.type_check_only
class GoogleCloudVisionV1p2beta1BatchAnnotateImagesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudVisionV1p2beta1BatchAnnotateImagesResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Operation: ...

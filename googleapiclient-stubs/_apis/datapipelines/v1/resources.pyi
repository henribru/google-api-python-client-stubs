import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class DatapipelinesResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class PipelinesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class JobsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> GoogleCloudDatapipelinesV1ListJobsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: GoogleCloudDatapipelinesV1ListJobsResponseHttpRequest,
                        previous_response: GoogleCloudDatapipelinesV1ListJobsResponse,
                    ) -> GoogleCloudDatapipelinesV1ListJobsResponseHttpRequest | None: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: GoogleCloudDatapipelinesV1Pipeline = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatapipelinesV1PipelineHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobufEmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleCloudDatapipelinesV1PipelineHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDatapipelinesV1Pipeline = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatapipelinesV1PipelineHttpRequest: ...
                def run(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDatapipelinesV1RunPipelineRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatapipelinesV1RunPipelineResponseHttpRequest: ...
                def stop(
                    self,
                    *,
                    name: str,
                    body: GoogleCloudDatapipelinesV1StopPipelineRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleCloudDatapipelinesV1PipelineHttpRequest: ...
                def jobs(self) -> JobsResource: ...

            def listPipelines(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> GoogleCloudDatapipelinesV1ListPipelinesResponseHttpRequest: ...
            def listPipelines_next(
                self,
                previous_request: GoogleCloudDatapipelinesV1ListPipelinesResponseHttpRequest,
                previous_response: GoogleCloudDatapipelinesV1ListPipelinesResponse,
            ) -> GoogleCloudDatapipelinesV1ListPipelinesResponseHttpRequest | None: ...
            def pipelines(self) -> PipelinesResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class GoogleCloudDatapipelinesV1ListJobsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatapipelinesV1ListJobsResponse: ...

@typing.type_check_only
class GoogleCloudDatapipelinesV1ListPipelinesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatapipelinesV1ListPipelinesResponse: ...

@typing.type_check_only
class GoogleCloudDatapipelinesV1PipelineHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatapipelinesV1Pipeline: ...

@typing.type_check_only
class GoogleCloudDatapipelinesV1RunPipelineResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleCloudDatapipelinesV1RunPipelineResponse: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...

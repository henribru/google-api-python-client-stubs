import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudVideoIntelligenceResource(googleapiclient.discovery.Resource):
    class VideosResource(googleapiclient.discovery.Resource):
        def annotate(
            self,
            *,
            body: GoogleCloudVideointelligenceV1_AnnotateVideoRequest = ...,
            **kwargs: typing.Any
        ) -> GoogleLongrunning_OperationHttpRequest: ...
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            class OperationsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleLongrunning_OperationHttpRequest: ...
                def cancel(
                    self,
                    *,
                    name: str,
                    body: GoogleLongrunning_CancelOperationRequest = ...,
                    **kwargs: typing.Any
                ) -> GoogleProtobuf_EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    pageToken: str = ...,
                    filter: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> GoogleLongrunning_ListOperationsResponseHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> GoogleProtobuf_EmptyHttpRequest: ...
            class CorpuraResource(googleapiclient.discovery.Resource):
                class OperationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunning_OperationHttpRequest: ...
                def operations(self) -> OperationsResource: ...
            class CorporaResource(googleapiclient.discovery.Resource):
                class OperationsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunning_OperationHttpRequest: ...
                def operations(self) -> OperationsResource: ...
            def operations(self) -> OperationsResource: ...
            def corpura(self) -> CorpuraResource: ...
            def corpora(self) -> CorporaResource: ...
        def locations(self) -> LocationsResource: ...
    class OperationsResource(googleapiclient.discovery.Resource):
        class ProjectsResource(googleapiclient.discovery.Resource):
            class LocationsResource(googleapiclient.discovery.Resource):
                class OperationsResource(googleapiclient.discovery.Resource):
                    def cancel(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobuf_EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleLongrunning_OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> GoogleProtobuf_EmptyHttpRequest: ...
                def operations(self) -> OperationsResource: ...
            def locations(self) -> LocationsResource: ...
        def projects(self) -> ProjectsResource: ...
    def videos(self) -> VideosResource: ...
    def projects(self) -> ProjectsResource: ...
    def operations(self) -> OperationsResource: ...

class GoogleLongrunning_OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunning_Operation: ...

class GoogleProtobuf_EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleProtobuf_Empty: ...

class GoogleLongrunning_ListOperationsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleLongrunning_ListOperationsResponse: ...

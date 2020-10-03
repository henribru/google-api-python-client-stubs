import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class SpeechResource(googleapiclient.discovery.Resource):
    class SpeechResource(googleapiclient.discovery.Resource):
        def recognize(
            self, *, body: RecognizeRequest = ..., **kwargs: typing.Any
        ) -> RecognizeResponseHttpRequest: ...
        def longrunningrecognize(
            self, *, body: LongRunningRecognizeRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
    class ProjectsResource(googleapiclient.discovery.Resource):
        class LocationsResource(googleapiclient.discovery.Resource):
            class OperationsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    name: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    filter: str = ...,
                    **kwargs: typing.Any
                ) -> ListOperationsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
            def operations(self) -> OperationsResource: ...
        def locations(self) -> LocationsResource: ...
    class OperationsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            pageToken: str = ...,
            filter: str = ...,
            name: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListOperationsResponseHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
    def speech(self) -> SpeechResource: ...
    def projects(self) -> ProjectsResource: ...
    def operations(self) -> OperationsResource: ...

class RecognizeResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> RecognizeResponse: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOperationsResponse: ...

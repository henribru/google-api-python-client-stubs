import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DisplayVideoResource(googleapiclient.discovery.Resource):
    class SdfdownloadtasksResource(googleapiclient.discovery.Resource):
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        def operations(self) -> OperationsResource: ...
    class SdfdownloadtaskResource(googleapiclient.discovery.Resource):
        class OperationsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        def operations(self) -> OperationsResource: ...
    class MediaResource(googleapiclient.discovery.Resource):
        def download(
            self, *, resourceName: str, **kwargs: typing.Any
        ) -> GoogleBytestreamMediaHttpRequest: ...
    def sdfdownloadtasks(self) -> SdfdownloadtasksResource: ...
    def sdfdownloadtask(self) -> SdfdownloadtaskResource: ...
    def media(self) -> MediaResource: ...

class GoogleBytestreamMediaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleBytestreamMedia: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

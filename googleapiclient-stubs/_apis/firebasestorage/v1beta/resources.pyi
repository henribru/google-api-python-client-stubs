import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

@typing.type_check_only
class FirebasestorageResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class BucketsResource(googleapiclient.discovery.Resource):
            def addFirebase(
                self,
                *,
                bucket: str,
                body: AddFirebaseRequest = ...,
                **kwargs: typing.Any
            ) -> BucketHttpRequest: ...
            def get(self, *, name: str, **kwargs: typing.Any) -> BucketHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListBucketsResponseHttpRequest: ...
            def removeFirebase(
                self,
                *,
                bucket: str,
                body: RemoveFirebaseRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
        def buckets(self) -> BucketsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class BucketHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Bucket: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListBucketsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListBucketsResponse: ...

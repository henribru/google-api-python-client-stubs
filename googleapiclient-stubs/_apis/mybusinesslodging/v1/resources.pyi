import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

@typing.type_check_only
class MyBusinessLodgingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class LocationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LodgingResource(googleapiclient.discovery.Resource):
            def getGoogleUpdated(
                self, *, name: str, readMask: str = ..., **kwargs: typing.Any
            ) -> GetGoogleUpdatedLodgingResponseHttpRequest: ...
        def getLodging(
            self, *, name: str, readMask: str = ..., **kwargs: typing.Any
        ) -> LodgingHttpRequest: ...
        def updateLodging(
            self,
            *,
            name: str,
            body: Lodging = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> LodgingHttpRequest: ...
        def lodging(self) -> LodgingResource: ...
    def locations(self) -> LocationsResource: ...

@typing.type_check_only
class GetGoogleUpdatedLodgingResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GetGoogleUpdatedLodgingResponse: ...

@typing.type_check_only
class LodgingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Lodging: ...

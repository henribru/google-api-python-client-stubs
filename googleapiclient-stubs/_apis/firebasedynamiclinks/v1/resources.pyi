import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class FirebaseDynamicLinksResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ManagedShortLinksResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: CreateManagedShortLinkRequest = ..., **kwargs: typing.Any
        ) -> CreateManagedShortLinkResponseHttpRequest: ...
    @typing.type_check_only
    class ShortLinksResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: CreateShortDynamicLinkRequest = ..., **kwargs: typing.Any
        ) -> CreateShortDynamicLinkResponseHttpRequest: ...
    @typing.type_check_only
    class V1Resource(googleapiclient.discovery.Resource):
        def getLinkStats(
            self,
            *,
            dynamicLink: str,
            durationDays: str = ...,
            sdkVersion: str = ...,
            **kwargs: typing.Any
        ) -> DynamicLinkStatsHttpRequest: ...
        def installAttribution(
            self,
            *,
            body: GetIosPostInstallAttributionRequest = ...,
            **kwargs: typing.Any
        ) -> GetIosPostInstallAttributionResponseHttpRequest: ...
        def reopenAttribution(
            self, *, body: GetIosReopenAttributionRequest = ..., **kwargs: typing.Any
        ) -> GetIosReopenAttributionResponseHttpRequest: ...
    def managedShortLinks(self) -> ManagedShortLinksResource: ...
    def shortLinks(self) -> ShortLinksResource: ...
    def v1(self) -> V1Resource: ...

@typing.type_check_only
class CreateManagedShortLinkResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CreateManagedShortLinkResponse: ...

@typing.type_check_only
class CreateShortDynamicLinkResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> CreateShortDynamicLinkResponse: ...

@typing.type_check_only
class DynamicLinkStatsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> DynamicLinkStats: ...

@typing.type_check_only
class GetIosPostInstallAttributionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GetIosPostInstallAttributionResponse: ...

@typing.type_check_only
class GetIosReopenAttributionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GetIosReopenAttributionResponse: ...

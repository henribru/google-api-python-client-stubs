import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class FirebaseDynamicLinksResource(googleapiclient.discovery.Resource):
    class ManagedShortLinksResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: CreateManagedShortLinkRequest = ..., **kwargs: typing.Any
        ) -> CreateManagedShortLinkResponseHttpRequest: ...
    class ShortLinksResource(googleapiclient.discovery.Resource):
        def create(
            self, *, body: CreateShortDynamicLinkRequest = ..., **kwargs: typing.Any
        ) -> CreateShortDynamicLinkResponseHttpRequest: ...
    class V1Resource(googleapiclient.discovery.Resource):
        def installAttribution(
            self,
            *,
            body: GetIosPostInstallAttributionRequest = ...,
            **kwargs: typing.Any
        ) -> GetIosPostInstallAttributionResponseHttpRequest: ...
        def getLinkStats(
            self,
            *,
            dynamicLink: str,
            sdkVersion: str = ...,
            durationDays: str = ...,
            **kwargs: typing.Any
        ) -> DynamicLinkStatsHttpRequest: ...
        def reopenAttribution(
            self, *, body: GetIosReopenAttributionRequest = ..., **kwargs: typing.Any
        ) -> GetIosReopenAttributionResponseHttpRequest: ...
    def managedShortLinks(self) -> ManagedShortLinksResource: ...
    def shortLinks(self) -> ShortLinksResource: ...
    def v1(self) -> V1Resource: ...

class DynamicLinkStatsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DynamicLinkStats: ...

class GetIosPostInstallAttributionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetIosPostInstallAttributionResponse: ...

class GetIosReopenAttributionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetIosReopenAttributionResponse: ...

class CreateManagedShortLinkResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CreateManagedShortLinkResponse: ...

class CreateShortDynamicLinkResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CreateShortDynamicLinkResponse: ...

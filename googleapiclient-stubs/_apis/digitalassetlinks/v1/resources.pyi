import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class DigitalassetlinksResource(googleapiclient.discovery.Resource):
    class AssetlinksResource(googleapiclient.discovery.Resource):
        def check(
            self,
            *,
            relation: str = ...,
            source_web_site: str = ...,
            source_androidApp_packageName: str = ...,
            target_web_site: str = ...,
            target_androidApp_packageName: str = ...,
            target_androidApp_certificate_sha256Fingerprint: str = ...,
            source_androidApp_certificate_sha256Fingerprint: str = ...,
            **kwargs: typing.Any
        ) -> CheckResponseHttpRequest: ...
    class StatementsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            source_androidApp_certificate_sha256Fingerprint: str = ...,
            source_web_site: str = ...,
            source_androidApp_packageName: str = ...,
            relation: str = ...,
            **kwargs: typing.Any
        ) -> ListResponseHttpRequest: ...
    def assetlinks(self) -> AssetlinksResource: ...
    def statements(self) -> StatementsResource: ...

class ListResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListResponse: ...

class CheckResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CheckResponse: ...

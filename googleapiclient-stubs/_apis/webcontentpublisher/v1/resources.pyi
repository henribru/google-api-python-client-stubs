import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class WebContentPublisherResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class PublicationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class CtasResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Cta,
                    ctaId: str | None = ...,
                    **kwargs: typing.Any,
                ) -> CtaHttpRequest: ...
                def get(self, *, name: str, **kwargs: typing.Any) -> CtaHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListCtasResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListCtasResponseHttpRequest,
                    previous_response: ListCtasResponse,
                ) -> ListCtasResponseHttpRequest | None: ...

            def create(
                self,
                *,
                parent: str,
                body: Publication,
                publicationId: str | None = ...,
                **kwargs: typing.Any,
            ) -> PublicationHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> PublicationHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> ListPublicationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListPublicationsResponseHttpRequest,
                previous_response: ListPublicationsResponse,
            ) -> ListPublicationsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: Publication,
                updateMask: str | None = ...,
                **kwargs: typing.Any,
            ) -> PublicationHttpRequest: ...
            def ctas(self) -> CtasResource: ...

        def publications(self) -> PublicationsResource: ...

    @typing.type_check_only
    class PublicationsResource(googleapiclient.discovery.Resource):
        def checkFreeAccess(
            self,
            *,
            name: str,
            httpReferrer: str | None = ...,
            uri: str | None = ...,
            **kwargs: typing.Any,
        ) -> CheckFreeAccessResponseHttpRequest: ...

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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def organizations(self) -> OrganizationsResource: ...
    def publications(self) -> PublicationsResource: ...

@typing.type_check_only
class CheckFreeAccessResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CheckFreeAccessResponse: ...

@typing.type_check_only
class CtaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Cta: ...

@typing.type_check_only
class ListCtasResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListCtasResponse: ...

@typing.type_check_only
class ListPublicationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListPublicationsResponse: ...

@typing.type_check_only
class PublicationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Publication: ...

import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class FactCheckToolsResource(googleapiclient.discovery.Resource):
    class ClaimsResource(googleapiclient.discovery.Resource):
        def search(
            self,
            *,
            offset: int = ...,
            reviewPublisherSiteFilter: str = ...,
            query: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            languageCode: str = ...,
            maxAgeDays: int = ...,
            **kwargs: typing.Any
        ) -> GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponseHttpRequest: ...
    class PagesResource(googleapiclient.discovery.Resource):
        def update(
            self,
            *,
            name: str,
            body: GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPage = ...,
            **kwargs: typing.Any
        ) -> GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageHttpRequest: ...
        def create(
            self,
            *,
            body: GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPage = ...,
            **kwargs: typing.Any
        ) -> GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageHttpRequest: ...
        def list(
            self,
            *,
            url: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            offset: int = ...,
            organization: str = ...,
            **kwargs: typing.Any
        ) -> GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponseHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleProtobufEmptyHttpRequest: ...
    def claims(self) -> ClaimsResource: ...
    def pages(self) -> PagesResource: ...

class GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponse: ...

class GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPage: ...

class GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponse: ...

class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GoogleProtobufEmpty: ...

import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class FactCheckToolsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ClaimsResource(googleapiclient.discovery.Resource):
        def search(
            self,
            *,
            languageCode: str = ...,
            maxAgeDays: int = ...,
            offset: int = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            query: str = ...,
            reviewPublisherSiteFilter: str = ...,
            **kwargs: typing.Any
        ) -> GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponseHttpRequest: ...
    @typing.type_check_only
    class PagesResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            body: GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPage = ...,
            **kwargs: typing.Any
        ) -> GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageHttpRequest: ...
        def delete(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleProtobufEmptyHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageHttpRequest: ...
        def list(
            self,
            *,
            offset: int = ...,
            organization: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            url: str = ...,
            **kwargs: typing.Any
        ) -> GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponseHttpRequest: ...
        def update(
            self,
            *,
            name: str,
            body: GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPage = ...,
            **kwargs: typing.Any
        ) -> GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageHttpRequest: ...
    def claims(self) -> ClaimsResource: ...
    def pages(self) -> PagesResource: ...

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPageHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleFactcheckingFactchecktoolsV1alpha1ClaimReviewMarkupPage: ...

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleFactcheckingFactchecktoolsV1alpha1FactCheckedClaimSearchResponse: ...

@typing.type_check_only
class GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleFactcheckingFactchecktoolsV1alpha1ListClaimReviewMarkupPagesResponse: ...

@typing.type_check_only
class GoogleProtobufEmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> GoogleProtobufEmpty: ...

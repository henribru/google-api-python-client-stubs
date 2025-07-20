import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class MerchantResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AggregateProductStatusesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListAggregateProductStatusesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListAggregateProductStatusesResponseHttpRequest,
                previous_response: ListAggregateProductStatusesResponse,
            ) -> ListAggregateProductStatusesResponseHttpRequest | None: ...

        def aggregateProductStatuses(self) -> AggregateProductStatusesResource: ...

    @typing.type_check_only
    class IssueresolutionResource(googleapiclient.discovery.Resource):
        def renderaccountissues(
            self,
            *,
            name: str,
            body: RenderIssuesRequestPayload = ...,
            languageCode: str = ...,
            timeZone: str = ...,
            **kwargs: typing.Any,
        ) -> RenderAccountIssuesResponseHttpRequest: ...
        def renderproductissues(
            self,
            *,
            name: str,
            body: RenderIssuesRequestPayload = ...,
            languageCode: str = ...,
            timeZone: str = ...,
            **kwargs: typing.Any,
        ) -> RenderProductIssuesResponseHttpRequest: ...
        def triggeraction(
            self,
            *,
            name: str,
            body: TriggerActionPayload = ...,
            languageCode: str = ...,
            **kwargs: typing.Any,
        ) -> TriggerActionResponseHttpRequest: ...

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
    def accounts(self) -> AccountsResource: ...
    def issueresolution(self) -> IssueresolutionResource: ...

@typing.type_check_only
class ListAggregateProductStatusesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAggregateProductStatusesResponse: ...

@typing.type_check_only
class RenderAccountIssuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RenderAccountIssuesResponse: ...

@typing.type_check_only
class RenderProductIssuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RenderProductIssuesResponse: ...

@typing.type_check_only
class TriggerActionResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TriggerActionResponse: ...

import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CloudAssetResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class IamPoliciesResource(googleapiclient.discovery.Resource):
        def searchAll(
            self,
            *,
            scope: str,
            pageSize: int = ...,
            pageToken: str = ...,
            query: str = ...,
            **kwargs: typing.Any
        ) -> SearchAllIamPoliciesResponseHttpRequest: ...
        def searchAll_next(
            self,
            previous_request: SearchAllIamPoliciesResponseHttpRequest,
            previous_response: SearchAllIamPoliciesResponse,
        ) -> SearchAllIamPoliciesResponseHttpRequest | None: ...

    @typing.type_check_only
    class ResourcesResource(googleapiclient.discovery.Resource):
        def searchAll(
            self,
            *,
            scope: str,
            assetTypes: str | _list[str] = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            query: str = ...,
            **kwargs: typing.Any
        ) -> SearchAllResourcesResponseHttpRequest: ...
        def searchAll_next(
            self,
            previous_request: SearchAllResourcesResponseHttpRequest,
            previous_response: SearchAllResourcesResponse,
        ) -> SearchAllResourcesResponseHttpRequest | None: ...

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
        | None = ...,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def iamPolicies(self) -> IamPoliciesResource: ...
    def resources(self) -> ResourcesResource: ...

@typing.type_check_only
class SearchAllIamPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SearchAllIamPoliciesResponse: ...

@typing.type_check_only
class SearchAllResourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> SearchAllResourcesResponse: ...

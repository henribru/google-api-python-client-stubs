import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudAssetResource(googleapiclient.discovery.Resource):
    class FeedsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, parent: str, **kwargs: typing.Any
        ) -> ListFeedsResponseHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> FeedHttpRequest: ...
        def patch(
            self, *, name: str, body: UpdateFeedRequest = ..., **kwargs: typing.Any
        ) -> FeedHttpRequest: ...
        def create(
            self, *, parent: str, body: CreateFeedRequest = ..., **kwargs: typing.Any
        ) -> FeedHttpRequest: ...
    class V1Resource(googleapiclient.discovery.Resource):
        def searchAllResources(
            self,
            *,
            scope: str,
            pageSize: int = ...,
            assetTypes: typing.Union[str, typing.List[str]] = ...,
            query: str = ...,
            orderBy: str = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> SearchAllResourcesResponseHttpRequest: ...
        def searchAllIamPolicies(
            self,
            *,
            scope: str,
            pageToken: str = ...,
            query: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> SearchAllIamPoliciesResponseHttpRequest: ...
        def exportAssets(
            self, *, parent: str, body: ExportAssetsRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def batchGetAssetsHistory(
            self,
            *,
            parent: str,
            assetNames: typing.Union[str, typing.List[str]] = ...,
            readTimeWindow_startTime: str = ...,
            readTimeWindow_endTime: str = ...,
            contentType: typing_extensions.Literal[
                "CONTENT_TYPE_UNSPECIFIED",
                "RESOURCE",
                "IAM_POLICY",
                "ORG_POLICY",
                "ACCESS_POLICY",
            ] = ...,
            **kwargs: typing.Any
        ) -> BatchGetAssetsHistoryResponseHttpRequest: ...
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
    def feeds(self) -> FeedsResource: ...
    def v1(self) -> V1Resource: ...
    def operations(self) -> OperationsResource: ...

class SearchAllIamPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchAllIamPoliciesResponse: ...

class SearchAllResourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchAllResourcesResponse: ...

class FeedHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Feed: ...

class ListFeedsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListFeedsResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class BatchGetAssetsHistoryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchGetAssetsHistoryResponse: ...

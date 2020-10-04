import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class CloudAssetResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class FeedsResource(googleapiclient.discovery.Resource):
        def create(
            self, *, parent: str, body: CreateFeedRequest = ..., **kwargs: typing.Any
        ) -> FeedHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> FeedHttpRequest: ...
        def list(
            self, *, parent: str, **kwargs: typing.Any
        ) -> ListFeedsResponseHttpRequest: ...
        def patch(
            self, *, name: str, body: UpdateFeedRequest = ..., **kwargs: typing.Any
        ) -> FeedHttpRequest: ...
    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
    @typing.type_check_only
    class V1Resource(googleapiclient.discovery.Resource):
        def batchGetAssetsHistory(
            self,
            *,
            parent: str,
            assetNames: typing.Union[str, typing.List[str]] = ...,
            contentType: typing_extensions.Literal[
                "CONTENT_TYPE_UNSPECIFIED",
                "RESOURCE",
                "IAM_POLICY",
                "ORG_POLICY",
                "ACCESS_POLICY",
            ] = ...,
            readTimeWindow_endTime: str = ...,
            readTimeWindow_startTime: str = ...,
            **kwargs: typing.Any
        ) -> BatchGetAssetsHistoryResponseHttpRequest: ...
        def exportAssets(
            self, *, parent: str, body: ExportAssetsRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def searchAllIamPolicies(
            self,
            *,
            scope: str,
            pageSize: int = ...,
            pageToken: str = ...,
            query: str = ...,
            **kwargs: typing.Any
        ) -> SearchAllIamPoliciesResponseHttpRequest: ...
        def searchAllResources(
            self,
            *,
            scope: str,
            assetTypes: typing.Union[str, typing.List[str]] = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            query: str = ...,
            **kwargs: typing.Any
        ) -> SearchAllResourcesResponseHttpRequest: ...
    def feeds(self) -> FeedsResource: ...
    def operations(self) -> OperationsResource: ...
    def v1(self) -> V1Resource: ...

@typing.type_check_only
class BatchGetAssetsHistoryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> BatchGetAssetsHistoryResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

@typing.type_check_only
class FeedHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Feed: ...

@typing.type_check_only
class ListFeedsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListFeedsResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

@typing.type_check_only
class SearchAllIamPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchAllIamPoliciesResponse: ...

@typing.type_check_only
class SearchAllResourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchAllResourcesResponse: ...

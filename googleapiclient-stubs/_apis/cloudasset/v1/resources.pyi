import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudAssetResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AssetsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            parent: str,
            assetTypes: str | _list[str] = ...,
            contentType: typing_extensions.Literal[
                "CONTENT_TYPE_UNSPECIFIED",
                "RESOURCE",
                "IAM_POLICY",
                "ORG_POLICY",
                "ACCESS_POLICY",
                "OS_INVENTORY",
                "RELATIONSHIP",
            ] = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            readTime: str = ...,
            relationshipTypes: str | _list[str] = ...,
            **kwargs: typing.Any,
        ) -> ListAssetsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListAssetsResponseHttpRequest,
            previous_response: ListAssetsResponse,
        ) -> ListAssetsResponseHttpRequest | None: ...

    @typing.type_check_only
    class EffectiveIamPoliciesResource(googleapiclient.discovery.Resource):
        def batchGet(
            self, *, scope: str, names: str | _list[str] = ..., **kwargs: typing.Any
        ) -> BatchGetEffectiveIamPoliciesResponseHttpRequest: ...

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
    class SavedQueriesResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            parent: str,
            body: SavedQuery = ...,
            savedQueryId: str = ...,
            **kwargs: typing.Any,
        ) -> SavedQueryHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> SavedQueryHttpRequest: ...
        def list(
            self,
            *,
            parent: str,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ListSavedQueriesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListSavedQueriesResponseHttpRequest,
            previous_response: ListSavedQueriesResponse,
        ) -> ListSavedQueriesResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: SavedQuery = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> SavedQueryHttpRequest: ...

    @typing.type_check_only
    class V1Resource(googleapiclient.discovery.Resource):
        def analyzeIamPolicy(
            self,
            *,
            scope: str,
            analysisQuery_accessSelector_permissions: str | _list[str] = ...,
            analysisQuery_accessSelector_roles: str | _list[str] = ...,
            analysisQuery_conditionContext_accessTime: str = ...,
            analysisQuery_identitySelector_identity: str = ...,
            analysisQuery_options_analyzeServiceAccountImpersonation: bool = ...,
            analysisQuery_options_expandGroups: bool = ...,
            analysisQuery_options_expandResources: bool = ...,
            analysisQuery_options_expandRoles: bool = ...,
            analysisQuery_options_outputGroupEdges: bool = ...,
            analysisQuery_options_outputResourceEdges: bool = ...,
            analysisQuery_resourceSelector_fullResourceName: str = ...,
            executionTimeout: str = ...,
            savedAnalysisQuery: str = ...,
            **kwargs: typing.Any,
        ) -> AnalyzeIamPolicyResponseHttpRequest: ...
        def analyzeIamPolicyLongrunning(
            self,
            *,
            scope: str,
            body: AnalyzeIamPolicyLongrunningRequest = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def analyzeMove(
            self,
            *,
            resource: str,
            destinationParent: str = ...,
            view: typing_extensions.Literal[
                "ANALYSIS_VIEW_UNSPECIFIED", "FULL", "BASIC"
            ] = ...,
            **kwargs: typing.Any,
        ) -> AnalyzeMoveResponseHttpRequest: ...
        def analyzeOrgPolicies(
            self,
            *,
            scope: str,
            constraint: str = ...,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> AnalyzeOrgPoliciesResponseHttpRequest: ...
        def analyzeOrgPolicies_next(
            self,
            previous_request: AnalyzeOrgPoliciesResponseHttpRequest,
            previous_response: AnalyzeOrgPoliciesResponse,
        ) -> AnalyzeOrgPoliciesResponseHttpRequest | None: ...
        def analyzeOrgPolicyGovernedAssets(
            self,
            *,
            scope: str,
            constraint: str = ...,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> AnalyzeOrgPolicyGovernedAssetsResponseHttpRequest: ...
        def analyzeOrgPolicyGovernedAssets_next(
            self,
            previous_request: AnalyzeOrgPolicyGovernedAssetsResponseHttpRequest,
            previous_response: AnalyzeOrgPolicyGovernedAssetsResponse,
        ) -> AnalyzeOrgPolicyGovernedAssetsResponseHttpRequest | None: ...
        def analyzeOrgPolicyGovernedContainers(
            self,
            *,
            scope: str,
            constraint: str = ...,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> AnalyzeOrgPolicyGovernedContainersResponseHttpRequest: ...
        def analyzeOrgPolicyGovernedContainers_next(
            self,
            previous_request: AnalyzeOrgPolicyGovernedContainersResponseHttpRequest,
            previous_response: AnalyzeOrgPolicyGovernedContainersResponse,
        ) -> AnalyzeOrgPolicyGovernedContainersResponseHttpRequest | None: ...
        def batchGetAssetsHistory(
            self,
            *,
            parent: str,
            assetNames: str | _list[str] = ...,
            contentType: typing_extensions.Literal[
                "CONTENT_TYPE_UNSPECIFIED",
                "RESOURCE",
                "IAM_POLICY",
                "ORG_POLICY",
                "ACCESS_POLICY",
                "OS_INVENTORY",
                "RELATIONSHIP",
            ] = ...,
            readTimeWindow_endTime: str = ...,
            readTimeWindow_startTime: str = ...,
            relationshipTypes: str | _list[str] = ...,
            **kwargs: typing.Any,
        ) -> BatchGetAssetsHistoryResponseHttpRequest: ...
        def exportAssets(
            self, *, parent: str, body: ExportAssetsRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def queryAssets(
            self, *, parent: str, body: QueryAssetsRequest = ..., **kwargs: typing.Any
        ) -> QueryAssetsResponseHttpRequest: ...
        def searchAllIamPolicies(
            self,
            *,
            scope: str,
            assetTypes: str | _list[str] = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            query: str = ...,
            **kwargs: typing.Any,
        ) -> SearchAllIamPoliciesResponseHttpRequest: ...
        def searchAllIamPolicies_next(
            self,
            previous_request: SearchAllIamPoliciesResponseHttpRequest,
            previous_response: SearchAllIamPoliciesResponse,
        ) -> SearchAllIamPoliciesResponseHttpRequest | None: ...
        def searchAllResources(
            self,
            *,
            scope: str,
            assetTypes: str | _list[str] = ...,
            orderBy: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            query: str = ...,
            readMask: str = ...,
            **kwargs: typing.Any,
        ) -> SearchAllResourcesResponseHttpRequest: ...
        def searchAllResources_next(
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
        | None = None,
    ) -> googleapiclient.http.BatchHttpRequest: ...
    def assets(self) -> AssetsResource: ...
    def effectiveIamPolicies(self) -> EffectiveIamPoliciesResource: ...
    def feeds(self) -> FeedsResource: ...
    def operations(self) -> OperationsResource: ...
    def savedQueries(self) -> SavedQueriesResource: ...
    def v1(self) -> V1Resource: ...

@typing.type_check_only
class AnalyzeIamPolicyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AnalyzeIamPolicyResponse: ...

@typing.type_check_only
class AnalyzeMoveResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AnalyzeMoveResponse: ...

@typing.type_check_only
class AnalyzeOrgPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AnalyzeOrgPoliciesResponse: ...

@typing.type_check_only
class AnalyzeOrgPolicyGovernedAssetsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AnalyzeOrgPolicyGovernedAssetsResponse: ...

@typing.type_check_only
class AnalyzeOrgPolicyGovernedContainersResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AnalyzeOrgPolicyGovernedContainersResponse: ...

@typing.type_check_only
class BatchGetAssetsHistoryResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchGetAssetsHistoryResponse: ...

@typing.type_check_only
class BatchGetEffectiveIamPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchGetEffectiveIamPoliciesResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class FeedHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Feed: ...

@typing.type_check_only
class ListAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListAssetsResponse: ...

@typing.type_check_only
class ListFeedsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListFeedsResponse: ...

@typing.type_check_only
class ListSavedQueriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSavedQueriesResponse: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class QueryAssetsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> QueryAssetsResponse: ...

@typing.type_check_only
class SavedQueryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SavedQuery: ...

@typing.type_check_only
class SearchAllIamPoliciesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchAllIamPoliciesResponse: ...

@typing.type_check_only
class SearchAllResourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchAllResourcesResponse: ...

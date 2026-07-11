import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class CloudSearchResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class DebugResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DatasourcesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ItemsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class UnmappedidsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        debugOptions_enableDebugging: bool | None = ...,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> ListUnmappedIdentitiesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListUnmappedIdentitiesResponseHttpRequest,
                        previous_response: ListUnmappedIdentitiesResponse,
                    ) -> ListUnmappedIdentitiesResponseHttpRequest | None: ...

                def checkAccess(
                    self,
                    *,
                    name: str,
                    body: Principal,
                    debugOptions_enableDebugging: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> CheckAccessResponseHttpRequest: ...
                def searchByViewUrl(
                    self,
                    *,
                    name: str,
                    body: SearchItemsByViewUrlRequest,
                    **kwargs: typing.Any,
                ) -> SearchItemsByViewUrlResponseHttpRequest: ...
                def searchByViewUrl_next(
                    self,
                    previous_request: SearchItemsByViewUrlResponseHttpRequest,
                    previous_response: SearchItemsByViewUrlResponse,
                ) -> SearchItemsByViewUrlResponseHttpRequest | None: ...
                def unmappedids(self) -> UnmappedidsResource: ...

            def items(self) -> ItemsResource: ...

        @typing.type_check_only
        class IdentitysourcesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ItemsResource(googleapiclient.discovery.Resource):
                def listForunmappedidentity(
                    self,
                    *,
                    parent: str,
                    debugOptions_enableDebugging: bool | None = ...,
                    groupResourceName: str | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    userResourceName: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListItemNamesForUnmappedIdentityResponseHttpRequest: ...
                def listForunmappedidentity_next(
                    self,
                    previous_request: ListItemNamesForUnmappedIdentityResponseHttpRequest,
                    previous_response: ListItemNamesForUnmappedIdentityResponse,
                ) -> ListItemNamesForUnmappedIdentityResponseHttpRequest | None: ...

            @typing.type_check_only
            class UnmappedidsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    debugOptions_enableDebugging: bool | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    resolutionStatusCode: typing_extensions.Literal[
                        "CODE_UNSPECIFIED",
                        "NOT_FOUND",
                        "IDENTITY_SOURCE_NOT_FOUND",
                        "IDENTITY_SOURCE_MISCONFIGURED",
                        "TOO_MANY_MAPPINGS_FOUND",
                        "INTERNAL_ERROR",
                    ]
                    | None = ...,
                    **kwargs: typing.Any,
                ) -> ListUnmappedIdentitiesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListUnmappedIdentitiesResponseHttpRequest,
                    previous_response: ListUnmappedIdentitiesResponse,
                ) -> ListUnmappedIdentitiesResponseHttpRequest | None: ...

            def items(self) -> ItemsResource: ...
            def unmappedids(self) -> UnmappedidsResource: ...

        def datasources(self) -> DatasourcesResource: ...
        def identitysources(self) -> IdentitysourcesResource: ...

    @typing.type_check_only
    class IndexingResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DatasourcesResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class ItemsResource(googleapiclient.discovery.Resource):
                def delete(
                    self,
                    *,
                    name: str,
                    connectorName: str | None = ...,
                    debugOptions_enableDebugging: bool | None = ...,
                    mode: typing_extensions.Literal[
                        "UNSPECIFIED", "SYNCHRONOUS", "ASYNCHRONOUS"
                    ]
                    | None = ...,
                    version: str | None = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def deleteQueueItems(
                    self,
                    *,
                    name: str,
                    body: DeleteQueueItemsRequest,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    connectorName: str | None = ...,
                    debugOptions_enableDebugging: bool | None = ...,
                    **kwargs: typing.Any,
                ) -> ItemHttpRequest: ...
                def index(
                    self, *, name: str, body: IndexItemRequest, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    brief: bool | None = ...,
                    connectorName: str | None = ...,
                    debugOptions_enableDebugging: bool | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListItemsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListItemsResponseHttpRequest,
                    previous_response: ListItemsResponse,
                ) -> ListItemsResponseHttpRequest | None: ...
                def poll(
                    self, *, name: str, body: PollItemsRequest, **kwargs: typing.Any
                ) -> PollItemsResponseHttpRequest: ...
                def push(
                    self, *, name: str, body: PushItemRequest, **kwargs: typing.Any
                ) -> ItemHttpRequest: ...
                def unreserve(
                    self,
                    *,
                    name: str,
                    body: UnreserveItemsRequest,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def upload(
                    self,
                    *,
                    name: str,
                    body: StartUploadItemRequest,
                    **kwargs: typing.Any,
                ) -> UploadItemRefHttpRequest: ...

            def deleteSchema(
                self,
                *,
                name: str,
                debugOptions_enableDebugging: bool | None = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def getSchema(
                self,
                *,
                name: str,
                debugOptions_enableDebugging: bool | None = ...,
                **kwargs: typing.Any,
            ) -> SchemaHttpRequest: ...
            def updateSchema(
                self, *, name: str, body: UpdateSchemaRequest, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def items(self) -> ItemsResource: ...

        def datasources(self) -> DatasourcesResource: ...

    @typing.type_check_only
    class MediaResource(googleapiclient.discovery.Resource):
        def upload(
            self, *, resourceName: str, body: Media, **kwargs: typing.Any
        ) -> MediaHttpRequest: ...

    @typing.type_check_only
    class OperationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class LroResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                name: str,
                filter: str | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                returnPartialSuccess: bool | None = ...,
                **kwargs: typing.Any,
            ) -> ListOperationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListOperationsResponseHttpRequest,
                previous_response: ListOperationsResponse,
            ) -> ListOperationsResponseHttpRequest | None: ...

        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
        def lro(self) -> LroResource: ...

    @typing.type_check_only
    class QueryResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class SourcesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                pageToken: str | None = ...,
                requestOptions_clientDisplayLanguageCode: str | None = ...,
                requestOptions_debugOptions_enableDebugging: bool | None = ...,
                requestOptions_languageCode: str | None = ...,
                requestOptions_searchApplicationId: str | None = ...,
                requestOptions_timeZone: str | None = ...,
                **kwargs: typing.Any,
            ) -> ListQuerySourcesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListQuerySourcesResponseHttpRequest,
                previous_response: ListQuerySourcesResponse,
            ) -> ListQuerySourcesResponseHttpRequest | None: ...

        def removeActivity(
            self, *, body: RemoveActivityRequest, **kwargs: typing.Any
        ) -> RemoveActivityResponseHttpRequest: ...
        def search(
            self, *, body: SearchRequest, **kwargs: typing.Any
        ) -> SearchResponseHttpRequest: ...
        def suggest(
            self, *, body: SuggestRequest, **kwargs: typing.Any
        ) -> SuggestResponseHttpRequest: ...
        def sources(self) -> SourcesResource: ...

    @typing.type_check_only
    class SettingsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DatasourcesResource(googleapiclient.discovery.Resource):
            def create(
                self, *, body: DataSource, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                debugOptions_enableDebugging: bool | None = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def get(
                self,
                *,
                name: str,
                debugOptions_enableDebugging: bool | None = ...,
                **kwargs: typing.Any,
            ) -> DataSourceHttpRequest: ...
            def list(
                self,
                *,
                debugOptions_enableDebugging: bool | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> ListDataSourceResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListDataSourceResponseHttpRequest,
                previous_response: ListDataSourceResponse,
            ) -> ListDataSourceResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: DataSource,
                debugOptions_enableDebugging: bool | None = ...,
                updateMask: str | None = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def update(
                self, *, name: str, body: UpdateDataSourceRequest, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...

        @typing.type_check_only
        class SearchapplicationsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, body: SearchApplication, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                debugOptions_enableDebugging: bool | None = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def get(
                self,
                *,
                name: str,
                debugOptions_enableDebugging: bool | None = ...,
                **kwargs: typing.Any,
            ) -> SearchApplicationHttpRequest: ...
            def list(
                self,
                *,
                debugOptions_enableDebugging: bool | None = ...,
                pageSize: int | None = ...,
                pageToken: str | None = ...,
                **kwargs: typing.Any,
            ) -> ListSearchApplicationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListSearchApplicationsResponseHttpRequest,
                previous_response: ListSearchApplicationsResponse,
            ) -> ListSearchApplicationsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: SearchApplication,
                updateMask: str | None = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def reset(
                self,
                *,
                name: str,
                body: ResetSearchApplicationRequest,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def update(
                self,
                *,
                name: str,
                body: SearchApplication,
                updateMask: str | None = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...

        def getCustomer(self, **kwargs: typing.Any) -> CustomerSettingsHttpRequest: ...
        def updateCustomer(
            self,
            *,
            body: CustomerSettings,
            updateMask: str | None = ...,
            **kwargs: typing.Any,
        ) -> OperationHttpRequest: ...
        def datasources(self) -> DatasourcesResource: ...
        def searchapplications(self) -> SearchapplicationsResource: ...

    @typing.type_check_only
    class StatsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class IndexResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DatasourcesResource(googleapiclient.discovery.Resource):
                def get(
                    self,
                    *,
                    name: str,
                    fromDate_day: int | None = ...,
                    fromDate_month: int | None = ...,
                    fromDate_year: int | None = ...,
                    toDate_day: int | None = ...,
                    toDate_month: int | None = ...,
                    toDate_year: int | None = ...,
                    **kwargs: typing.Any,
                ) -> GetDataSourceIndexStatsResponseHttpRequest: ...

            def datasources(self) -> DatasourcesResource: ...

        @typing.type_check_only
        class QueryResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class SearchapplicationsResource(googleapiclient.discovery.Resource):
                def get(
                    self,
                    *,
                    name: str,
                    fromDate_day: int | None = ...,
                    fromDate_month: int | None = ...,
                    fromDate_year: int | None = ...,
                    toDate_day: int | None = ...,
                    toDate_month: int | None = ...,
                    toDate_year: int | None = ...,
                    **kwargs: typing.Any,
                ) -> GetSearchApplicationQueryStatsResponseHttpRequest: ...

            def searchapplications(self) -> SearchapplicationsResource: ...

        @typing.type_check_only
        class SessionResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class SearchapplicationsResource(googleapiclient.discovery.Resource):
                def get(
                    self,
                    *,
                    name: str,
                    fromDate_day: int | None = ...,
                    fromDate_month: int | None = ...,
                    fromDate_year: int | None = ...,
                    toDate_day: int | None = ...,
                    toDate_month: int | None = ...,
                    toDate_year: int | None = ...,
                    **kwargs: typing.Any,
                ) -> GetSearchApplicationSessionStatsResponseHttpRequest: ...

            def searchapplications(self) -> SearchapplicationsResource: ...

        @typing.type_check_only
        class UserResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class SearchapplicationsResource(googleapiclient.discovery.Resource):
                def get(
                    self,
                    *,
                    name: str,
                    fromDate_day: int | None = ...,
                    fromDate_month: int | None = ...,
                    fromDate_year: int | None = ...,
                    toDate_day: int | None = ...,
                    toDate_month: int | None = ...,
                    toDate_year: int | None = ...,
                    **kwargs: typing.Any,
                ) -> GetSearchApplicationUserStatsResponseHttpRequest: ...

            def searchapplications(self) -> SearchapplicationsResource: ...

        def getIndex(
            self,
            *,
            fromDate_day: int | None = ...,
            fromDate_month: int | None = ...,
            fromDate_year: int | None = ...,
            toDate_day: int | None = ...,
            toDate_month: int | None = ...,
            toDate_year: int | None = ...,
            **kwargs: typing.Any,
        ) -> GetCustomerIndexStatsResponseHttpRequest: ...
        def getQuery(
            self,
            *,
            fromDate_day: int | None = ...,
            fromDate_month: int | None = ...,
            fromDate_year: int | None = ...,
            toDate_day: int | None = ...,
            toDate_month: int | None = ...,
            toDate_year: int | None = ...,
            **kwargs: typing.Any,
        ) -> GetCustomerQueryStatsResponseHttpRequest: ...
        def getSearchapplication(
            self,
            *,
            endDate_day: int | None = ...,
            endDate_month: int | None = ...,
            endDate_year: int | None = ...,
            startDate_day: int | None = ...,
            startDate_month: int | None = ...,
            startDate_year: int | None = ...,
            **kwargs: typing.Any,
        ) -> GetCustomerSearchApplicationStatsResponseHttpRequest: ...
        def getSession(
            self,
            *,
            fromDate_day: int | None = ...,
            fromDate_month: int | None = ...,
            fromDate_year: int | None = ...,
            toDate_day: int | None = ...,
            toDate_month: int | None = ...,
            toDate_year: int | None = ...,
            **kwargs: typing.Any,
        ) -> GetCustomerSessionStatsResponseHttpRequest: ...
        def getUser(
            self,
            *,
            fromDate_day: int | None = ...,
            fromDate_month: int | None = ...,
            fromDate_year: int | None = ...,
            toDate_day: int | None = ...,
            toDate_month: int | None = ...,
            toDate_year: int | None = ...,
            **kwargs: typing.Any,
        ) -> GetCustomerUserStatsResponseHttpRequest: ...
        def index(self) -> IndexResource: ...
        def query(self) -> QueryResource: ...
        def session(self) -> SessionResource: ...
        def user(self) -> UserResource: ...

    @typing.type_check_only
    class V1Resource(googleapiclient.discovery.Resource):
        def initializeCustomer(
            self, *, body: InitializeCustomerRequest, **kwargs: typing.Any
        ) -> OperationHttpRequest: ...

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
    def debug(self) -> DebugResource: ...
    def indexing(self) -> IndexingResource: ...
    def media(self) -> MediaResource: ...
    def operations(self) -> OperationsResource: ...
    def query(self) -> QueryResource: ...
    def settings(self) -> SettingsResource: ...
    def stats(self) -> StatsResource: ...
    def v1(self) -> V1Resource: ...

@typing.type_check_only
class CheckAccessResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CheckAccessResponse: ...

@typing.type_check_only
class CustomerSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CustomerSettings: ...

@typing.type_check_only
class DataSourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DataSource: ...

@typing.type_check_only
class GetCustomerIndexStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GetCustomerIndexStatsResponse: ...

@typing.type_check_only
class GetCustomerQueryStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GetCustomerQueryStatsResponse: ...

@typing.type_check_only
class GetCustomerSearchApplicationStatsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GetCustomerSearchApplicationStatsResponse: ...

@typing.type_check_only
class GetCustomerSessionStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GetCustomerSessionStatsResponse: ...

@typing.type_check_only
class GetCustomerUserStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GetCustomerUserStatsResponse: ...

@typing.type_check_only
class GetDataSourceIndexStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GetDataSourceIndexStatsResponse: ...

@typing.type_check_only
class GetSearchApplicationQueryStatsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GetSearchApplicationQueryStatsResponse: ...

@typing.type_check_only
class GetSearchApplicationSessionStatsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GetSearchApplicationSessionStatsResponse: ...

@typing.type_check_only
class GetSearchApplicationUserStatsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> GetSearchApplicationUserStatsResponse: ...

@typing.type_check_only
class ItemHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Item: ...

@typing.type_check_only
class ListDataSourceResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListDataSourceResponse: ...

@typing.type_check_only
class ListItemNamesForUnmappedIdentityResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListItemNamesForUnmappedIdentityResponse: ...

@typing.type_check_only
class ListItemsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListItemsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListQuerySourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListQuerySourcesResponse: ...

@typing.type_check_only
class ListSearchApplicationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSearchApplicationsResponse: ...

@typing.type_check_only
class ListUnmappedIdentitiesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListUnmappedIdentitiesResponse: ...

@typing.type_check_only
class MediaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Media: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class PollItemsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> PollItemsResponse: ...

@typing.type_check_only
class RemoveActivityResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> RemoveActivityResponse: ...

@typing.type_check_only
class SchemaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Schema: ...

@typing.type_check_only
class SearchApplicationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchApplication: ...

@typing.type_check_only
class SearchItemsByViewUrlResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchItemsByViewUrlResponse: ...

@typing.type_check_only
class SearchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SearchResponse: ...

@typing.type_check_only
class SuggestResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SuggestResponse: ...

@typing.type_check_only
class UploadItemRefHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> UploadItemRef: ...

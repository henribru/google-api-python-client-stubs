import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CloudSearchResource(googleapiclient.discovery.Resource):
    class MediaResource(googleapiclient.discovery.Resource):
        def upload(
            self, *, resourceName: str, body: Media = ..., **kwargs: typing.Any
        ) -> MediaHttpRequest: ...
    class IndexingResource(googleapiclient.discovery.Resource):
        class DatasourcesResource(googleapiclient.discovery.Resource):
            class ItemsResource(googleapiclient.discovery.Resource):
                def index(
                    self,
                    *,
                    name: str,
                    body: IndexItemRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def deleteQueueItems(
                    self,
                    *,
                    name: str,
                    body: DeleteQueueItemsRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    debugOptions_enableDebugging: bool = ...,
                    brief: bool = ...,
                    connectorName: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListItemsResponseHttpRequest: ...
                def get(
                    self,
                    *,
                    name: str,
                    connectorName: str = ...,
                    debugOptions_enableDebugging: bool = ...,
                    **kwargs: typing.Any
                ) -> ItemHttpRequest: ...
                def unreserve(
                    self,
                    *,
                    name: str,
                    body: UnreserveItemsRequest = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def push(
                    self,
                    *,
                    name: str,
                    body: PushItemRequest = ...,
                    **kwargs: typing.Any
                ) -> ItemHttpRequest: ...
                def delete(
                    self,
                    *,
                    name: str,
                    debugOptions_enableDebugging: bool = ...,
                    version: str = ...,
                    connectorName: str = ...,
                    mode: typing_extensions.Literal[
                        "UNSPECIFIED", "SYNCHRONOUS", "ASYNCHRONOUS"
                    ] = ...,
                    **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def upload(
                    self,
                    *,
                    name: str,
                    body: StartUploadItemRequest = ...,
                    **kwargs: typing.Any
                ) -> UploadItemRefHttpRequest: ...
                def poll(
                    self,
                    *,
                    name: str,
                    body: PollItemsRequest = ...,
                    **kwargs: typing.Any
                ) -> PollItemsResponseHttpRequest: ...
            def getSchema(
                self,
                *,
                name: str,
                debugOptions_enableDebugging: bool = ...,
                **kwargs: typing.Any
            ) -> SchemaHttpRequest: ...
            def updateSchema(
                self,
                *,
                name: str,
                body: UpdateSchemaRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def deleteSchema(
                self,
                *,
                name: str,
                debugOptions_enableDebugging: bool = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def items(self) -> ItemsResource: ...
        def datasources(self) -> DatasourcesResource: ...
    class SettingsResource(googleapiclient.discovery.Resource):
        class DatasourcesResource(googleapiclient.discovery.Resource):
            def delete(
                self,
                *,
                name: str,
                debugOptions_enableDebugging: bool = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def update(
                self,
                *,
                name: str,
                body: UpdateDataSourceRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def create(
                self, *, body: DataSource = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self,
                *,
                name: str,
                debugOptions_enableDebugging: bool = ...,
                **kwargs: typing.Any
            ) -> DataSourceHttpRequest: ...
            def list(
                self,
                *,
                debugOptions_enableDebugging: bool = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListDataSourceResponseHttpRequest: ...
        class SearchapplicationsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                debugOptions_enableDebugging: bool = ...,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListSearchApplicationsResponseHttpRequest: ...
            def delete(
                self,
                *,
                name: str,
                debugOptions_enableDebugging: bool = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def create(
                self, *, body: SearchApplication = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def reset(
                self,
                *,
                name: str,
                body: ResetSearchApplicationRequest = ...,
                **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def get(
                self,
                *,
                name: str,
                debugOptions_enableDebugging: bool = ...,
                **kwargs: typing.Any
            ) -> SearchApplicationHttpRequest: ...
            def update(
                self, *, name: str, body: SearchApplication = ..., **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
        def datasources(self) -> DatasourcesResource: ...
        def searchapplications(self) -> SearchapplicationsResource: ...
    class StatsResource(googleapiclient.discovery.Resource):
        class SessionResource(googleapiclient.discovery.Resource):
            class SearchapplicationsResource(googleapiclient.discovery.Resource):
                def get(
                    self,
                    *,
                    name: str,
                    toDate_year: int = ...,
                    fromDate_day: int = ...,
                    fromDate_year: int = ...,
                    fromDate_month: int = ...,
                    toDate_day: int = ...,
                    toDate_month: int = ...,
                    **kwargs: typing.Any
                ) -> GetSearchApplicationSessionStatsResponseHttpRequest: ...
            def searchapplications(self) -> SearchapplicationsResource: ...
        class IndexResource(googleapiclient.discovery.Resource):
            class DatasourcesResource(googleapiclient.discovery.Resource):
                def get(
                    self,
                    *,
                    name: str,
                    toDate_day: int = ...,
                    toDate_year: int = ...,
                    toDate_month: int = ...,
                    fromDate_month: int = ...,
                    fromDate_day: int = ...,
                    fromDate_year: int = ...,
                    **kwargs: typing.Any
                ) -> GetDataSourceIndexStatsResponseHttpRequest: ...
            def datasources(self) -> DatasourcesResource: ...
        class UserResource(googleapiclient.discovery.Resource):
            class SearchapplicationsResource(googleapiclient.discovery.Resource):
                def get(
                    self,
                    *,
                    name: str,
                    fromDate_day: int = ...,
                    toDate_day: int = ...,
                    fromDate_month: int = ...,
                    toDate_year: int = ...,
                    toDate_month: int = ...,
                    fromDate_year: int = ...,
                    **kwargs: typing.Any
                ) -> GetSearchApplicationUserStatsResponseHttpRequest: ...
            def searchapplications(self) -> SearchapplicationsResource: ...
        class QueryResource(googleapiclient.discovery.Resource):
            class SearchapplicationsResource(googleapiclient.discovery.Resource):
                def get(
                    self,
                    *,
                    name: str,
                    toDate_month: int = ...,
                    toDate_day: int = ...,
                    toDate_year: int = ...,
                    fromDate_year: int = ...,
                    fromDate_day: int = ...,
                    fromDate_month: int = ...,
                    **kwargs: typing.Any
                ) -> GetSearchApplicationQueryStatsResponseHttpRequest: ...
            def searchapplications(self) -> SearchapplicationsResource: ...
        def getSession(
            self,
            *,
            toDate_year: int = ...,
            toDate_month: int = ...,
            fromDate_day: int = ...,
            fromDate_year: int = ...,
            fromDate_month: int = ...,
            toDate_day: int = ...,
            **kwargs: typing.Any
        ) -> GetCustomerSessionStatsResponseHttpRequest: ...
        def getIndex(
            self,
            *,
            fromDate_day: int = ...,
            toDate_day: int = ...,
            fromDate_year: int = ...,
            toDate_month: int = ...,
            toDate_year: int = ...,
            fromDate_month: int = ...,
            **kwargs: typing.Any
        ) -> GetCustomerIndexStatsResponseHttpRequest: ...
        def getUser(
            self,
            *,
            toDate_year: int = ...,
            fromDate_day: int = ...,
            toDate_day: int = ...,
            fromDate_year: int = ...,
            toDate_month: int = ...,
            fromDate_month: int = ...,
            **kwargs: typing.Any
        ) -> GetCustomerUserStatsResponseHttpRequest: ...
        def getQuery(
            self,
            *,
            toDate_month: int = ...,
            toDate_year: int = ...,
            fromDate_year: int = ...,
            toDate_day: int = ...,
            fromDate_day: int = ...,
            fromDate_month: int = ...,
            **kwargs: typing.Any
        ) -> GetCustomerQueryStatsResponseHttpRequest: ...
        def session(self) -> SessionResource: ...
        def index(self) -> IndexResource: ...
        def user(self) -> UserResource: ...
        def query(self) -> QueryResource: ...
    class QueryResource(googleapiclient.discovery.Resource):
        class SourcesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                requestOptions_languageCode: str = ...,
                requestOptions_timeZone: str = ...,
                requestOptions_searchApplicationId: str = ...,
                requestOptions_debugOptions_enableDebugging: bool = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListQuerySourcesResponseHttpRequest: ...
        def search(
            self, *, body: SearchRequest = ..., **kwargs: typing.Any
        ) -> SearchResponseHttpRequest: ...
        def suggest(
            self, *, body: SuggestRequest = ..., **kwargs: typing.Any
        ) -> SuggestResponseHttpRequest: ...
        def sources(self) -> SourcesResource: ...
    class OperationsResource(googleapiclient.discovery.Resource):
        class LroResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                name: str,
                pageSize: int = ...,
                pageToken: str = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> ListOperationsResponseHttpRequest: ...
        def get(self, *, name: str, **kwargs: typing.Any) -> OperationHttpRequest: ...
        def lro(self) -> LroResource: ...
    class DebugResource(googleapiclient.discovery.Resource):
        class DatasourcesResource(googleapiclient.discovery.Resource):
            class ItemsResource(googleapiclient.discovery.Resource):
                class UnmappedidsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        debugOptions_enableDebugging: bool = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListUnmappedIdentitiesResponseHttpRequest: ...
                def checkAccess(
                    self,
                    *,
                    name: str,
                    body: Principal = ...,
                    debugOptions_enableDebugging: bool = ...,
                    **kwargs: typing.Any
                ) -> CheckAccessResponseHttpRequest: ...
                def searchByViewUrl(
                    self,
                    *,
                    name: str,
                    body: SearchItemsByViewUrlRequest = ...,
                    **kwargs: typing.Any
                ) -> SearchItemsByViewUrlResponseHttpRequest: ...
                def unmappedids(self) -> UnmappedidsResource: ...
            def items(self) -> ItemsResource: ...
        class IdentitysourcesResource(googleapiclient.discovery.Resource):
            class ItemsResource(googleapiclient.discovery.Resource):
                def listForunmappedidentity(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    groupResourceName: str = ...,
                    userResourceName: str = ...,
                    pageSize: int = ...,
                    debugOptions_enableDebugging: bool = ...,
                    **kwargs: typing.Any
                ) -> ListItemNamesForUnmappedIdentityResponseHttpRequest: ...
            class UnmappedidsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    debugOptions_enableDebugging: bool = ...,
                    resolutionStatusCode: typing_extensions.Literal[
                        "CODE_UNSPECIFIED",
                        "NOT_FOUND",
                        "IDENTITY_SOURCE_NOT_FOUND",
                        "IDENTITY_SOURCE_MISCONFIGURED",
                        "TOO_MANY_MAPPINGS_FOUND",
                        "INTERNAL_ERROR",
                    ] = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListUnmappedIdentitiesResponseHttpRequest: ...
            def items(self) -> ItemsResource: ...
            def unmappedids(self) -> UnmappedidsResource: ...
        def datasources(self) -> DatasourcesResource: ...
        def identitysources(self) -> IdentitysourcesResource: ...
    def media(self) -> MediaResource: ...
    def indexing(self) -> IndexingResource: ...
    def settings(self) -> SettingsResource: ...
    def stats(self) -> StatsResource: ...
    def query(self) -> QueryResource: ...
    def operations(self) -> OperationsResource: ...
    def debug(self) -> DebugResource: ...

class MediaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Media: ...

class ListDataSourceResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDataSourceResponse: ...

class SchemaHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Schema: ...

class CheckAccessResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CheckAccessResponse: ...

class ListItemsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListItemsResponse: ...

class GetSearchApplicationSessionStatsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetSearchApplicationSessionStatsResponse: ...

class GetCustomerIndexStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetCustomerIndexStatsResponse: ...

class PollItemsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> PollItemsResponse: ...

class GetCustomerUserStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetCustomerUserStatsResponse: ...

class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Operation: ...

class ListQuerySourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListQuerySourcesResponse: ...

class SearchItemsByViewUrlResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchItemsByViewUrlResponse: ...

class ListItemNamesForUnmappedIdentityResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListItemNamesForUnmappedIdentityResponse: ...

class DataSourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DataSource: ...

class GetCustomerSessionStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetCustomerSessionStatsResponse: ...

class ListSearchApplicationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListSearchApplicationsResponse: ...

class GetSearchApplicationUserStatsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetSearchApplicationUserStatsResponse: ...

class GetSearchApplicationQueryStatsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetSearchApplicationQueryStatsResponse: ...

class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListOperationsResponse: ...

class SearchResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchResponse: ...

class SearchApplicationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SearchApplication: ...

class UploadItemRefHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UploadItemRef: ...

class GetDataSourceIndexStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetDataSourceIndexStatsResponse: ...

class SuggestResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> SuggestResponse: ...

class ListUnmappedIdentitiesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListUnmappedIdentitiesResponse: ...

class ItemHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Item: ...

class GetCustomerQueryStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> GetCustomerQueryStatsResponse: ...

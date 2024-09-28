import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class LoggingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class BillingAccountsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ExclusionsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: LogExclusion = ..., **kwargs: typing.Any
            ) -> LogExclusionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LogExclusionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListExclusionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListExclusionsResponseHttpRequest,
                previous_response: ListExclusionsResponse,
            ) -> ListExclusionsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: LogExclusion = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> LogExclusionHttpRequest: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class BucketsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class LinksResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Link = ...,
                        linkId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> LinkHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListLinksResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListLinksResponseHttpRequest,
                        previous_response: ListLinksResponse,
                    ) -> ListLinksResponseHttpRequest | None: ...

                @typing.type_check_only
                class ViewsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class LogsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            resourceNames: str | _list[str] = ...,
                            **kwargs: typing.Any,
                        ) -> ListLogsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListLogsResponseHttpRequest,
                            previous_response: ListLogsResponse,
                        ) -> ListLogsResponseHttpRequest | None: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: LogView = ...,
                        viewId: str = ...,
                        **kwargs: typing.Any,
                    ) -> LogViewHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> LogViewHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListViewsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListViewsResponseHttpRequest,
                        previous_response: ListViewsResponse,
                    ) -> ListViewsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: LogView = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> LogViewHttpRequest: ...
                    def logs(self) -> LogsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: LogBucket = ...,
                    bucketId: str = ...,
                    **kwargs: typing.Any,
                ) -> LogBucketHttpRequest: ...
                def createAsync(
                    self,
                    *,
                    parent: str,
                    body: LogBucket = ...,
                    bucketId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> LogBucketHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListBucketsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListBucketsResponseHttpRequest,
                    previous_response: ListBucketsResponse,
                ) -> ListBucketsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: LogBucket = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> LogBucketHttpRequest: ...
                def undelete(
                    self,
                    *,
                    name: str,
                    body: UndeleteBucketRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def updateAsync(
                    self,
                    *,
                    name: str,
                    body: LogBucket = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def links(self) -> LinksResource: ...
                def views(self) -> ViewsResource: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class RecentQueriesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListRecentQueriesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListRecentQueriesResponseHttpRequest,
                    previous_response: ListRecentQueriesResponse,
                ) -> ListRecentQueriesResponseHttpRequest | None: ...

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
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> SavedQueryHttpRequest: ...
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

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def buckets(self) -> BucketsResource: ...
            def operations(self) -> OperationsResource: ...
            def recentQueries(self) -> RecentQueriesResource: ...
            def savedQueries(self) -> SavedQueriesResource: ...

        @typing.type_check_only
        class LogsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, logName: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                resourceNames: str | _list[str] = ...,
                **kwargs: typing.Any,
            ) -> ListLogsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLogsResponseHttpRequest,
                previous_response: ListLogsResponse,
            ) -> ListLogsResponseHttpRequest | None: ...

        @typing.type_check_only
        class SinksResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: LogSink = ...,
                customWriterIdentity: str = ...,
                uniqueWriterIdentity: bool = ...,
                **kwargs: typing.Any,
            ) -> LogSinkHttpRequest: ...
            def delete(
                self, *, sinkName: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, sinkName: str, **kwargs: typing.Any
            ) -> LogSinkHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListSinksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListSinksResponseHttpRequest,
                previous_response: ListSinksResponse,
            ) -> ListSinksResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                sinkName: str,
                body: LogSink = ...,
                customWriterIdentity: str = ...,
                uniqueWriterIdentity: bool = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> LogSinkHttpRequest: ...
            def update(
                self,
                *,
                sinkName: str,
                body: LogSink = ...,
                customWriterIdentity: str = ...,
                uniqueWriterIdentity: bool = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> LogSinkHttpRequest: ...

        def getCmekSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> CmekSettingsHttpRequest: ...
        def getSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> SettingsHttpRequest: ...
        def exclusions(self) -> ExclusionsResource: ...
        def locations(self) -> LocationsResource: ...
        def logs(self) -> LogsResource: ...
        def sinks(self) -> SinksResource: ...

    @typing.type_check_only
    class EntriesResource(googleapiclient.discovery.Resource):
        def copy(
            self, *, body: CopyLogEntriesRequest = ..., **kwargs: typing.Any
        ) -> OperationHttpRequest: ...
        def list(
            self, *, body: ListLogEntriesRequest = ..., **kwargs: typing.Any
        ) -> ListLogEntriesResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListLogEntriesResponseHttpRequest,
            previous_response: ListLogEntriesResponse,
        ) -> ListLogEntriesResponseHttpRequest | None: ...
        def tail(
            self, *, body: TailLogEntriesRequest = ..., **kwargs: typing.Any
        ) -> TailLogEntriesResponseHttpRequest: ...
        def write(
            self, *, body: WriteLogEntriesRequest = ..., **kwargs: typing.Any
        ) -> WriteLogEntriesResponseHttpRequest: ...

    @typing.type_check_only
    class ExclusionsResource(googleapiclient.discovery.Resource):
        def create(
            self, *, parent: str, body: LogExclusion = ..., **kwargs: typing.Any
        ) -> LogExclusionHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> LogExclusionHttpRequest: ...
        def list(
            self,
            *,
            parent: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ListExclusionsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListExclusionsResponseHttpRequest,
            previous_response: ListExclusionsResponse,
        ) -> ListExclusionsResponseHttpRequest | None: ...
        def patch(
            self,
            *,
            name: str,
            body: LogExclusion = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> LogExclusionHttpRequest: ...

    @typing.type_check_only
    class FoldersResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ExclusionsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: LogExclusion = ..., **kwargs: typing.Any
            ) -> LogExclusionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LogExclusionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListExclusionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListExclusionsResponseHttpRequest,
                previous_response: ListExclusionsResponse,
            ) -> ListExclusionsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: LogExclusion = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> LogExclusionHttpRequest: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class BucketsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class LinksResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Link = ...,
                        linkId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> LinkHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListLinksResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListLinksResponseHttpRequest,
                        previous_response: ListLinksResponse,
                    ) -> ListLinksResponseHttpRequest | None: ...

                @typing.type_check_only
                class ViewsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class LogsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            resourceNames: str | _list[str] = ...,
                            **kwargs: typing.Any,
                        ) -> ListLogsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListLogsResponseHttpRequest,
                            previous_response: ListLogsResponse,
                        ) -> ListLogsResponseHttpRequest | None: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: LogView = ...,
                        viewId: str = ...,
                        **kwargs: typing.Any,
                    ) -> LogViewHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> LogViewHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListViewsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListViewsResponseHttpRequest,
                        previous_response: ListViewsResponse,
                    ) -> ListViewsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: LogView = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> LogViewHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> TestIamPermissionsResponseHttpRequest: ...
                    def logs(self) -> LogsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: LogBucket = ...,
                    bucketId: str = ...,
                    **kwargs: typing.Any,
                ) -> LogBucketHttpRequest: ...
                def createAsync(
                    self,
                    *,
                    parent: str,
                    body: LogBucket = ...,
                    bucketId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> LogBucketHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListBucketsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListBucketsResponseHttpRequest,
                    previous_response: ListBucketsResponse,
                ) -> ListBucketsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: LogBucket = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> LogBucketHttpRequest: ...
                def undelete(
                    self,
                    *,
                    name: str,
                    body: UndeleteBucketRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def updateAsync(
                    self,
                    *,
                    name: str,
                    body: LogBucket = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def links(self) -> LinksResource: ...
                def views(self) -> ViewsResource: ...

            @typing.type_check_only
            class LogScopesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: LogScope = ...,
                    logScopeId: str = ...,
                    **kwargs: typing.Any,
                ) -> LogScopeHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> LogScopeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListLogScopesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListLogScopesResponseHttpRequest,
                    previous_response: ListLogScopesResponse,
                ) -> ListLogScopesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: LogScope = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> LogScopeHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class RecentQueriesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListRecentQueriesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListRecentQueriesResponseHttpRequest,
                    previous_response: ListRecentQueriesResponse,
                ) -> ListRecentQueriesResponseHttpRequest | None: ...

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
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> SavedQueryHttpRequest: ...
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

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def buckets(self) -> BucketsResource: ...
            def logScopes(self) -> LogScopesResource: ...
            def operations(self) -> OperationsResource: ...
            def recentQueries(self) -> RecentQueriesResource: ...
            def savedQueries(self) -> SavedQueriesResource: ...

        @typing.type_check_only
        class LogsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, logName: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                resourceNames: str | _list[str] = ...,
                **kwargs: typing.Any,
            ) -> ListLogsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLogsResponseHttpRequest,
                previous_response: ListLogsResponse,
            ) -> ListLogsResponseHttpRequest | None: ...

        @typing.type_check_only
        class SinksResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: LogSink = ...,
                customWriterIdentity: str = ...,
                uniqueWriterIdentity: bool = ...,
                **kwargs: typing.Any,
            ) -> LogSinkHttpRequest: ...
            def delete(
                self, *, sinkName: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, sinkName: str, **kwargs: typing.Any
            ) -> LogSinkHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListSinksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListSinksResponseHttpRequest,
                previous_response: ListSinksResponse,
            ) -> ListSinksResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                sinkName: str,
                body: LogSink = ...,
                customWriterIdentity: str = ...,
                uniqueWriterIdentity: bool = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> LogSinkHttpRequest: ...
            def update(
                self,
                *,
                sinkName: str,
                body: LogSink = ...,
                customWriterIdentity: str = ...,
                uniqueWriterIdentity: bool = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> LogSinkHttpRequest: ...

        def getCmekSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> CmekSettingsHttpRequest: ...
        def getSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> SettingsHttpRequest: ...
        def updateSettings(
            self,
            *,
            name: str,
            body: Settings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> SettingsHttpRequest: ...
        def exclusions(self) -> ExclusionsResource: ...
        def locations(self) -> LocationsResource: ...
        def logs(self) -> LogsResource: ...
        def sinks(self) -> SinksResource: ...

    @typing.type_check_only
    class LocationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class BucketsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class LinksResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: Link = ...,
                    linkId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> LinkHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListLinksResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListLinksResponseHttpRequest,
                    previous_response: ListLinksResponse,
                ) -> ListLinksResponseHttpRequest | None: ...

            @typing.type_check_only
            class ViewsResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: LogView = ...,
                    viewId: str = ...,
                    **kwargs: typing.Any,
                ) -> LogViewHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> LogViewHttpRequest: ...
                def getIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: GetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListViewsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListViewsResponseHttpRequest,
                    previous_response: ListViewsResponse,
                ) -> ListViewsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: LogView = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> LogViewHttpRequest: ...
                def setIamPolicy(
                    self,
                    *,
                    resource: str,
                    body: SetIamPolicyRequest = ...,
                    **kwargs: typing.Any,
                ) -> PolicyHttpRequest: ...
                def testIamPermissions(
                    self,
                    *,
                    resource: str,
                    body: TestIamPermissionsRequest = ...,
                    **kwargs: typing.Any,
                ) -> TestIamPermissionsResponseHttpRequest: ...

            def create(
                self,
                *,
                parent: str,
                body: LogBucket = ...,
                bucketId: str = ...,
                **kwargs: typing.Any,
            ) -> LogBucketHttpRequest: ...
            def createAsync(
                self,
                *,
                parent: str,
                body: LogBucket = ...,
                bucketId: str = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LogBucketHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListBucketsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListBucketsResponseHttpRequest,
                previous_response: ListBucketsResponse,
            ) -> ListBucketsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: LogBucket = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> LogBucketHttpRequest: ...
            def undelete(
                self,
                *,
                name: str,
                body: UndeleteBucketRequest = ...,
                **kwargs: typing.Any,
            ) -> EmptyHttpRequest: ...
            def updateAsync(
                self,
                *,
                name: str,
                body: LogBucket = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> OperationHttpRequest: ...
            def links(self) -> LinksResource: ...
            def views(self) -> ViewsResource: ...

        @typing.type_check_only
        class OperationsResource(googleapiclient.discovery.Resource):
            def cancel(
                self,
                *,
                name: str,
                body: CancelOperationRequest = ...,
                **kwargs: typing.Any,
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> OperationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListOperationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListOperationsResponseHttpRequest,
                previous_response: ListOperationsResponse,
            ) -> ListOperationsResponseHttpRequest | None: ...

        def get(self, *, name: str, **kwargs: typing.Any) -> LocationHttpRequest: ...
        def list(
            self,
            *,
            name: str,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ListLocationsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListLocationsResponseHttpRequest,
            previous_response: ListLocationsResponse,
        ) -> ListLocationsResponseHttpRequest | None: ...
        def buckets(self) -> BucketsResource: ...
        def operations(self) -> OperationsResource: ...

    @typing.type_check_only
    class LogsResource(googleapiclient.discovery.Resource):
        def delete(self, *, logName: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def list(
            self,
            *,
            parent: str,
            pageSize: int = ...,
            pageToken: str = ...,
            resourceNames: str | _list[str] = ...,
            **kwargs: typing.Any,
        ) -> ListLogsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListLogsResponseHttpRequest,
            previous_response: ListLogsResponse,
        ) -> ListLogsResponseHttpRequest | None: ...

    @typing.type_check_only
    class MonitoredResourceDescriptorsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, pageSize: int = ..., pageToken: str = ..., **kwargs: typing.Any
        ) -> ListMonitoredResourceDescriptorsResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListMonitoredResourceDescriptorsResponseHttpRequest,
            previous_response: ListMonitoredResourceDescriptorsResponse,
        ) -> ListMonitoredResourceDescriptorsResponseHttpRequest | None: ...

    @typing.type_check_only
    class OrganizationsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ExclusionsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: LogExclusion = ..., **kwargs: typing.Any
            ) -> LogExclusionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LogExclusionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListExclusionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListExclusionsResponseHttpRequest,
                previous_response: ListExclusionsResponse,
            ) -> ListExclusionsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: LogExclusion = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> LogExclusionHttpRequest: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class BucketsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class LinksResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Link = ...,
                        linkId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> LinkHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListLinksResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListLinksResponseHttpRequest,
                        previous_response: ListLinksResponse,
                    ) -> ListLinksResponseHttpRequest | None: ...

                @typing.type_check_only
                class ViewsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class LogsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            resourceNames: str | _list[str] = ...,
                            **kwargs: typing.Any,
                        ) -> ListLogsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListLogsResponseHttpRequest,
                            previous_response: ListLogsResponse,
                        ) -> ListLogsResponseHttpRequest | None: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: LogView = ...,
                        viewId: str = ...,
                        **kwargs: typing.Any,
                    ) -> LogViewHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> LogViewHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListViewsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListViewsResponseHttpRequest,
                        previous_response: ListViewsResponse,
                    ) -> ListViewsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: LogView = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> LogViewHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> TestIamPermissionsResponseHttpRequest: ...
                    def logs(self) -> LogsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: LogBucket = ...,
                    bucketId: str = ...,
                    **kwargs: typing.Any,
                ) -> LogBucketHttpRequest: ...
                def createAsync(
                    self,
                    *,
                    parent: str,
                    body: LogBucket = ...,
                    bucketId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> LogBucketHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListBucketsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListBucketsResponseHttpRequest,
                    previous_response: ListBucketsResponse,
                ) -> ListBucketsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: LogBucket = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> LogBucketHttpRequest: ...
                def undelete(
                    self,
                    *,
                    name: str,
                    body: UndeleteBucketRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def updateAsync(
                    self,
                    *,
                    name: str,
                    body: LogBucket = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def links(self) -> LinksResource: ...
                def views(self) -> ViewsResource: ...

            @typing.type_check_only
            class LogScopesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: LogScope = ...,
                    logScopeId: str = ...,
                    **kwargs: typing.Any,
                ) -> LogScopeHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> LogScopeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListLogScopesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListLogScopesResponseHttpRequest,
                    previous_response: ListLogScopesResponse,
                ) -> ListLogScopesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: LogScope = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> LogScopeHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class RecentQueriesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListRecentQueriesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListRecentQueriesResponseHttpRequest,
                    previous_response: ListRecentQueriesResponse,
                ) -> ListRecentQueriesResponseHttpRequest | None: ...

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
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> SavedQueryHttpRequest: ...
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

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def buckets(self) -> BucketsResource: ...
            def logScopes(self) -> LogScopesResource: ...
            def operations(self) -> OperationsResource: ...
            def recentQueries(self) -> RecentQueriesResource: ...
            def savedQueries(self) -> SavedQueriesResource: ...

        @typing.type_check_only
        class LogsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, logName: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                resourceNames: str | _list[str] = ...,
                **kwargs: typing.Any,
            ) -> ListLogsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLogsResponseHttpRequest,
                previous_response: ListLogsResponse,
            ) -> ListLogsResponseHttpRequest | None: ...

        @typing.type_check_only
        class SinksResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: LogSink = ...,
                customWriterIdentity: str = ...,
                uniqueWriterIdentity: bool = ...,
                **kwargs: typing.Any,
            ) -> LogSinkHttpRequest: ...
            def delete(
                self, *, sinkName: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, sinkName: str, **kwargs: typing.Any
            ) -> LogSinkHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListSinksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListSinksResponseHttpRequest,
                previous_response: ListSinksResponse,
            ) -> ListSinksResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                sinkName: str,
                body: LogSink = ...,
                customWriterIdentity: str = ...,
                uniqueWriterIdentity: bool = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> LogSinkHttpRequest: ...
            def update(
                self,
                *,
                sinkName: str,
                body: LogSink = ...,
                customWriterIdentity: str = ...,
                uniqueWriterIdentity: bool = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> LogSinkHttpRequest: ...

        def getCmekSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> CmekSettingsHttpRequest: ...
        def getSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> SettingsHttpRequest: ...
        def updateCmekSettings(
            self,
            *,
            name: str,
            body: CmekSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> CmekSettingsHttpRequest: ...
        def updateSettings(
            self,
            *,
            name: str,
            body: Settings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> SettingsHttpRequest: ...
        def exclusions(self) -> ExclusionsResource: ...
        def locations(self) -> LocationsResource: ...
        def logs(self) -> LogsResource: ...
        def sinks(self) -> SinksResource: ...

    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class ExclusionsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: LogExclusion = ..., **kwargs: typing.Any
            ) -> LogExclusionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LogExclusionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListExclusionsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListExclusionsResponseHttpRequest,
                previous_response: ListExclusionsResponse,
            ) -> ListExclusionsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: LogExclusion = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> LogExclusionHttpRequest: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class BucketsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class LinksResource(googleapiclient.discovery.Resource):
                    def create(
                        self,
                        *,
                        parent: str,
                        body: Link = ...,
                        linkId: str = ...,
                        **kwargs: typing.Any,
                    ) -> OperationHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> OperationHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> LinkHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListLinksResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListLinksResponseHttpRequest,
                        previous_response: ListLinksResponse,
                    ) -> ListLinksResponseHttpRequest | None: ...

                @typing.type_check_only
                class ViewsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class LogsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            parent: str,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            resourceNames: str | _list[str] = ...,
                            **kwargs: typing.Any,
                        ) -> ListLogsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListLogsResponseHttpRequest,
                            previous_response: ListLogsResponse,
                        ) -> ListLogsResponseHttpRequest | None: ...

                    def create(
                        self,
                        *,
                        parent: str,
                        body: LogView = ...,
                        viewId: str = ...,
                        **kwargs: typing.Any,
                    ) -> LogViewHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> LogViewHttpRequest: ...
                    def getIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: GetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> PolicyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any,
                    ) -> ListViewsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListViewsResponseHttpRequest,
                        previous_response: ListViewsResponse,
                    ) -> ListViewsResponseHttpRequest | None: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: LogView = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any,
                    ) -> LogViewHttpRequest: ...
                    def setIamPolicy(
                        self,
                        *,
                        resource: str,
                        body: SetIamPolicyRequest = ...,
                        **kwargs: typing.Any,
                    ) -> PolicyHttpRequest: ...
                    def testIamPermissions(
                        self,
                        *,
                        resource: str,
                        body: TestIamPermissionsRequest = ...,
                        **kwargs: typing.Any,
                    ) -> TestIamPermissionsResponseHttpRequest: ...
                    def logs(self) -> LogsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: LogBucket = ...,
                    bucketId: str = ...,
                    **kwargs: typing.Any,
                ) -> LogBucketHttpRequest: ...
                def createAsync(
                    self,
                    *,
                    parent: str,
                    body: LogBucket = ...,
                    bucketId: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> LogBucketHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListBucketsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListBucketsResponseHttpRequest,
                    previous_response: ListBucketsResponse,
                ) -> ListBucketsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: LogBucket = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> LogBucketHttpRequest: ...
                def undelete(
                    self,
                    *,
                    name: str,
                    body: UndeleteBucketRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def updateAsync(
                    self,
                    *,
                    name: str,
                    body: LogBucket = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> OperationHttpRequest: ...
                def links(self) -> LinksResource: ...
                def views(self) -> ViewsResource: ...

            @typing.type_check_only
            class LogScopesResource(googleapiclient.discovery.Resource):
                def create(
                    self,
                    *,
                    parent: str,
                    body: LogScope = ...,
                    logScopeId: str = ...,
                    **kwargs: typing.Any,
                ) -> LogScopeHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> LogScopeHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListLogScopesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListLogScopesResponseHttpRequest,
                    previous_response: ListLogScopesResponse,
                ) -> ListLogScopesResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: LogScope = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any,
                ) -> LogScopeHttpRequest: ...

            @typing.type_check_only
            class OperationsResource(googleapiclient.discovery.Resource):
                def cancel(
                    self,
                    *,
                    name: str,
                    body: CancelOperationRequest = ...,
                    **kwargs: typing.Any,
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> OperationHttpRequest: ...
                def list(
                    self,
                    *,
                    name: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListOperationsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListOperationsResponseHttpRequest,
                    previous_response: ListOperationsResponse,
                ) -> ListOperationsResponseHttpRequest | None: ...

            @typing.type_check_only
            class RecentQueriesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    filter: str = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any,
                ) -> ListRecentQueriesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListRecentQueriesResponseHttpRequest,
                    previous_response: ListRecentQueriesResponse,
                ) -> ListRecentQueriesResponseHttpRequest | None: ...

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
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> SavedQueryHttpRequest: ...
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

            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def buckets(self) -> BucketsResource: ...
            def logScopes(self) -> LogScopesResource: ...
            def operations(self) -> OperationsResource: ...
            def recentQueries(self) -> RecentQueriesResource: ...
            def savedQueries(self) -> SavedQueriesResource: ...

        @typing.type_check_only
        class LogsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, logName: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                resourceNames: str | _list[str] = ...,
                **kwargs: typing.Any,
            ) -> ListLogsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLogsResponseHttpRequest,
                previous_response: ListLogsResponse,
            ) -> ListLogsResponseHttpRequest | None: ...

        @typing.type_check_only
        class MetricsResource(googleapiclient.discovery.Resource):
            def create(
                self, *, parent: str, body: LogMetric = ..., **kwargs: typing.Any
            ) -> LogMetricHttpRequest: ...
            def delete(
                self, *, metricName: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, metricName: str, **kwargs: typing.Any
            ) -> LogMetricHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListLogMetricsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLogMetricsResponseHttpRequest,
                previous_response: ListLogMetricsResponse,
            ) -> ListLogMetricsResponseHttpRequest | None: ...
            def update(
                self, *, metricName: str, body: LogMetric = ..., **kwargs: typing.Any
            ) -> LogMetricHttpRequest: ...

        @typing.type_check_only
        class SinksResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: LogSink = ...,
                customWriterIdentity: str = ...,
                uniqueWriterIdentity: bool = ...,
                **kwargs: typing.Any,
            ) -> LogSinkHttpRequest: ...
            def delete(
                self, *, sinkName: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, sinkName: str, **kwargs: typing.Any
            ) -> LogSinkHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                filter: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any,
            ) -> ListSinksResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListSinksResponseHttpRequest,
                previous_response: ListSinksResponse,
            ) -> ListSinksResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                sinkName: str,
                body: LogSink = ...,
                customWriterIdentity: str = ...,
                uniqueWriterIdentity: bool = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> LogSinkHttpRequest: ...
            def update(
                self,
                *,
                sinkName: str,
                body: LogSink = ...,
                customWriterIdentity: str = ...,
                uniqueWriterIdentity: bool = ...,
                updateMask: str = ...,
                **kwargs: typing.Any,
            ) -> LogSinkHttpRequest: ...

        def getCmekSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> CmekSettingsHttpRequest: ...
        def getSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> SettingsHttpRequest: ...
        def exclusions(self) -> ExclusionsResource: ...
        def locations(self) -> LocationsResource: ...
        def logs(self) -> LogsResource: ...
        def metrics(self) -> MetricsResource: ...
        def sinks(self) -> SinksResource: ...

    @typing.type_check_only
    class SinksResource(googleapiclient.discovery.Resource):
        def create(
            self,
            *,
            parent: str,
            body: LogSink = ...,
            customWriterIdentity: str = ...,
            uniqueWriterIdentity: bool = ...,
            **kwargs: typing.Any,
        ) -> LogSinkHttpRequest: ...
        def delete(
            self, *, sinkName: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def get(self, *, sinkName: str, **kwargs: typing.Any) -> LogSinkHttpRequest: ...
        def list(
            self,
            *,
            parent: str,
            filter: str = ...,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any,
        ) -> ListSinksResponseHttpRequest: ...
        def list_next(
            self,
            previous_request: ListSinksResponseHttpRequest,
            previous_response: ListSinksResponse,
        ) -> ListSinksResponseHttpRequest | None: ...
        def update(
            self,
            *,
            sinkName: str,
            body: LogSink = ...,
            customWriterIdentity: str = ...,
            uniqueWriterIdentity: bool = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> LogSinkHttpRequest: ...

    @typing.type_check_only
    class V2Resource(googleapiclient.discovery.Resource):
        def getCmekSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> CmekSettingsHttpRequest: ...
        def getSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> SettingsHttpRequest: ...
        def updateCmekSettings(
            self,
            *,
            name: str,
            body: CmekSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> CmekSettingsHttpRequest: ...
        def updateSettings(
            self,
            *,
            name: str,
            body: Settings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any,
        ) -> SettingsHttpRequest: ...

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
    def billingAccounts(self) -> BillingAccountsResource: ...
    def entries(self) -> EntriesResource: ...
    def exclusions(self) -> ExclusionsResource: ...
    def folders(self) -> FoldersResource: ...
    def locations(self) -> LocationsResource: ...
    def logs(self) -> LogsResource: ...
    def monitoredResourceDescriptors(self) -> MonitoredResourceDescriptorsResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def projects(self) -> ProjectsResource: ...
    def sinks(self) -> SinksResource: ...
    def v2(self) -> V2Resource: ...

@typing.type_check_only
class CmekSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CmekSettings: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class LinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Link: ...

@typing.type_check_only
class ListBucketsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListBucketsResponse: ...

@typing.type_check_only
class ListExclusionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListExclusionsResponse: ...

@typing.type_check_only
class ListLinksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLinksResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListLogEntriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLogEntriesResponse: ...

@typing.type_check_only
class ListLogMetricsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLogMetricsResponse: ...

@typing.type_check_only
class ListLogScopesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLogScopesResponse: ...

@typing.type_check_only
class ListLogsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListLogsResponse: ...

@typing.type_check_only
class ListMonitoredResourceDescriptorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListMonitoredResourceDescriptorsResponse: ...

@typing.type_check_only
class ListOperationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListOperationsResponse: ...

@typing.type_check_only
class ListRecentQueriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListRecentQueriesResponse: ...

@typing.type_check_only
class ListSavedQueriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSavedQueriesResponse: ...

@typing.type_check_only
class ListSinksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListSinksResponse: ...

@typing.type_check_only
class ListViewsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListViewsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Location: ...

@typing.type_check_only
class LogBucketHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LogBucket: ...

@typing.type_check_only
class LogExclusionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LogExclusion: ...

@typing.type_check_only
class LogMetricHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LogMetric: ...

@typing.type_check_only
class LogScopeHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LogScope: ...

@typing.type_check_only
class LogSinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LogSink: ...

@typing.type_check_only
class LogViewHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> LogView: ...

@typing.type_check_only
class OperationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Operation: ...

@typing.type_check_only
class PolicyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Policy: ...

@typing.type_check_only
class SavedQueryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> SavedQuery: ...

@typing.type_check_only
class SettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Settings: ...

@typing.type_check_only
class TailLogEntriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TailLogEntriesResponse: ...

@typing.type_check_only
class TestIamPermissionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> TestIamPermissionsResponse: ...

@typing.type_check_only
class WriteLogEntriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> WriteLogEntriesResponse: ...

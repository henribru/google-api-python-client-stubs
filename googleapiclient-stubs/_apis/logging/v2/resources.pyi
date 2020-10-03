import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class LoggingResource(googleapiclient.discovery.Resource):
    class EntriesResource(googleapiclient.discovery.Resource):
        def list(
            self, *, body: ListLogEntriesRequest = ..., **kwargs: typing.Any
        ) -> ListLogEntriesResponseHttpRequest: ...
        def write(
            self, *, body: WriteLogEntriesRequest = ..., **kwargs: typing.Any
        ) -> WriteLogEntriesResponseHttpRequest: ...
    class LogsResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            parent: str,
            pageToken: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListLogsResponseHttpRequest: ...
        def delete(self, *, logName: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
    class MonitoredResourceDescriptorsResource(googleapiclient.discovery.Resource):
        def list(
            self, *, pageToken: str = ..., pageSize: int = ..., **kwargs: typing.Any
        ) -> ListMonitoredResourceDescriptorsResponseHttpRequest: ...
    class ExclusionsResource(googleapiclient.discovery.Resource):
        def patch(
            self,
            *,
            name: str,
            body: LogExclusion = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> LogExclusionHttpRequest: ...
        def create(
            self, *, parent: str, body: LogExclusion = ..., **kwargs: typing.Any
        ) -> LogExclusionHttpRequest: ...
        def get(
            self, *, name: str, **kwargs: typing.Any
        ) -> LogExclusionHttpRequest: ...
        def delete(self, *, name: str, **kwargs: typing.Any) -> EmptyHttpRequest: ...
        def list(
            self,
            *,
            parent: str,
            pageSize: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ListExclusionsResponseHttpRequest: ...
    class BillingAccountsResource(googleapiclient.discovery.Resource):
        class ExclusionsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListExclusionsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: LogExclusion = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> LogExclusionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LogExclusionHttpRequest: ...
            def create(
                self, *, parent: str, body: LogExclusion = ..., **kwargs: typing.Any
            ) -> LogExclusionHttpRequest: ...
        class BucketsResource(googleapiclient.discovery.Resource):
            class ViewsResource(googleapiclient.discovery.Resource):
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> LogViewHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LogBucketHttpRequest: ...
            def views(self) -> ViewsResource: ...
        class LocationsResource(googleapiclient.discovery.Resource):
            class BucketsResource(googleapiclient.discovery.Resource):
                class ViewsResource(googleapiclient.discovery.Resource):
                    def patch(
                        self,
                        *,
                        name: str,
                        body: LogView = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> LogViewHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: LogView = ...,
                        viewId: str = ...,
                        **kwargs: typing.Any
                    ) -> LogViewHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> ListViewsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: LogBucket = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> LogBucketHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def undelete(
                    self,
                    *,
                    name: str,
                    body: UndeleteBucketRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListBucketsResponseHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: LogBucket = ...,
                    bucketId: str = ...,
                    **kwargs: typing.Any
                ) -> LogBucketHttpRequest: ...
                def views(self) -> ViewsResource: ...
            def buckets(self) -> BucketsResource: ...
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
                **kwargs: typing.Any
            ) -> ListLogsResponseHttpRequest: ...
        class SinksResource(googleapiclient.discovery.Resource):
            def patch(
                self,
                *,
                sinkName: str,
                body: LogSink = ...,
                updateMask: str = ...,
                uniqueWriterIdentity: bool = ...,
                **kwargs: typing.Any
            ) -> LogSinkHttpRequest: ...
            def delete(
                self, *, sinkName: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def update(
                self,
                *,
                sinkName: str,
                body: LogSink = ...,
                updateMask: str = ...,
                uniqueWriterIdentity: bool = ...,
                **kwargs: typing.Any
            ) -> LogSinkHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: LogSink = ...,
                uniqueWriterIdentity: bool = ...,
                **kwargs: typing.Any
            ) -> LogSinkHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListSinksResponseHttpRequest: ...
            def get(
                self, *, sinkName: str, **kwargs: typing.Any
            ) -> LogSinkHttpRequest: ...
        def exclusions(self) -> ExclusionsResource: ...
        def buckets(self) -> BucketsResource: ...
        def locations(self) -> LocationsResource: ...
        def logs(self) -> LogsResource: ...
        def sinks(self) -> SinksResource: ...
    class SinksResource(googleapiclient.discovery.Resource):
        def get(self, *, sinkName: str, **kwargs: typing.Any) -> LogSinkHttpRequest: ...
        def list(
            self,
            *,
            parent: str,
            pageToken: str = ...,
            pageSize: int = ...,
            **kwargs: typing.Any
        ) -> ListSinksResponseHttpRequest: ...
        def delete(
            self, *, sinkName: str, **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def create(
            self,
            *,
            parent: str,
            body: LogSink = ...,
            uniqueWriterIdentity: bool = ...,
            **kwargs: typing.Any
        ) -> LogSinkHttpRequest: ...
        def update(
            self,
            *,
            sinkName: str,
            body: LogSink = ...,
            updateMask: str = ...,
            uniqueWriterIdentity: bool = ...,
            **kwargs: typing.Any
        ) -> LogSinkHttpRequest: ...
    class FoldersResource(googleapiclient.discovery.Resource):
        class ExclusionsResource(googleapiclient.discovery.Resource):
            def patch(
                self,
                *,
                name: str,
                body: LogExclusion = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> LogExclusionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListExclusionsResponseHttpRequest: ...
            def create(
                self, *, parent: str, body: LogExclusion = ..., **kwargs: typing.Any
            ) -> LogExclusionHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LogExclusionHttpRequest: ...
        class SinksResource(googleapiclient.discovery.Resource):
            def get(
                self, *, sinkName: str, **kwargs: typing.Any
            ) -> LogSinkHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: LogSink = ...,
                uniqueWriterIdentity: bool = ...,
                **kwargs: typing.Any
            ) -> LogSinkHttpRequest: ...
            def delete(
                self, *, sinkName: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListSinksResponseHttpRequest: ...
            def update(
                self,
                *,
                sinkName: str,
                body: LogSink = ...,
                updateMask: str = ...,
                uniqueWriterIdentity: bool = ...,
                **kwargs: typing.Any
            ) -> LogSinkHttpRequest: ...
            def patch(
                self,
                *,
                sinkName: str,
                body: LogSink = ...,
                updateMask: str = ...,
                uniqueWriterIdentity: bool = ...,
                **kwargs: typing.Any
            ) -> LogSinkHttpRequest: ...
        class LocationsResource(googleapiclient.discovery.Resource):
            class BucketsResource(googleapiclient.discovery.Resource):
                class ViewsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> LogViewHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: LogView = ...,
                        viewId: str = ...,
                        **kwargs: typing.Any
                    ) -> LogViewHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: LogView = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> LogViewHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> ListViewsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> LogBucketHttpRequest: ...
                def undelete(
                    self,
                    *,
                    name: str,
                    body: UndeleteBucketRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListBucketsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: LogBucket = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> LogBucketHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: LogBucket = ...,
                    bucketId: str = ...,
                    **kwargs: typing.Any
                ) -> LogBucketHttpRequest: ...
                def views(self) -> ViewsResource: ...
            def buckets(self) -> BucketsResource: ...
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
                **kwargs: typing.Any
            ) -> ListLogsResponseHttpRequest: ...
        def exclusions(self) -> ExclusionsResource: ...
        def sinks(self) -> SinksResource: ...
        def locations(self) -> LocationsResource: ...
        def logs(self) -> LogsResource: ...
    class LocationsResource(googleapiclient.discovery.Resource):
        class BucketsResource(googleapiclient.discovery.Resource):
            class ViewsResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListViewsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: LogView = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> LogViewHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> LogViewHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: LogView = ...,
                    viewId: str = ...,
                    **kwargs: typing.Any
                ) -> LogViewHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: LogBucket = ...,
                bucketId: str = ...,
                **kwargs: typing.Any
            ) -> LogBucketHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LogBucketHttpRequest: ...
            def undelete(
                self,
                *,
                name: str,
                body: UndeleteBucketRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListBucketsResponseHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: LogBucket = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> LogBucketHttpRequest: ...
            def views(self) -> ViewsResource: ...
        def buckets(self) -> BucketsResource: ...
    class OrganizationsResource(googleapiclient.discovery.Resource):
        class SinksResource(googleapiclient.discovery.Resource):
            def create(
                self,
                *,
                parent: str,
                body: LogSink = ...,
                uniqueWriterIdentity: bool = ...,
                **kwargs: typing.Any
            ) -> LogSinkHttpRequest: ...
            def get(
                self, *, sinkName: str, **kwargs: typing.Any
            ) -> LogSinkHttpRequest: ...
            def update(
                self,
                *,
                sinkName: str,
                body: LogSink = ...,
                uniqueWriterIdentity: bool = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> LogSinkHttpRequest: ...
            def delete(
                self, *, sinkName: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListSinksResponseHttpRequest: ...
            def patch(
                self,
                *,
                sinkName: str,
                body: LogSink = ...,
                updateMask: str = ...,
                uniqueWriterIdentity: bool = ...,
                **kwargs: typing.Any
            ) -> LogSinkHttpRequest: ...
        class LogsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListLogsResponseHttpRequest: ...
            def delete(
                self, *, logName: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
        class ExclusionsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LogExclusionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListExclusionsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: LogExclusion = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> LogExclusionHttpRequest: ...
            def create(
                self, *, parent: str, body: LogExclusion = ..., **kwargs: typing.Any
            ) -> LogExclusionHttpRequest: ...
        class LocationsResource(googleapiclient.discovery.Resource):
            class BucketsResource(googleapiclient.discovery.Resource):
                class ViewsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> LogViewHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListViewsResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: LogView = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> LogViewHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: LogView = ...,
                        viewId: str = ...,
                        **kwargs: typing.Any
                    ) -> LogViewHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListBucketsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> LogBucketHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: LogBucket = ...,
                    bucketId: str = ...,
                    **kwargs: typing.Any
                ) -> LogBucketHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: LogBucket = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> LogBucketHttpRequest: ...
                def undelete(
                    self,
                    *,
                    name: str,
                    body: UndeleteBucketRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def views(self) -> ViewsResource: ...
            def buckets(self) -> BucketsResource: ...
        def updateCmekSettings(
            self,
            *,
            name: str,
            body: CmekSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> CmekSettingsHttpRequest: ...
        def getCmekSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> CmekSettingsHttpRequest: ...
        def sinks(self) -> SinksResource: ...
        def logs(self) -> LogsResource: ...
        def exclusions(self) -> ExclusionsResource: ...
        def locations(self) -> LocationsResource: ...
    class V2Resource(googleapiclient.discovery.Resource):
        def updateCmekSettings(
            self,
            *,
            name: str,
            body: CmekSettings = ...,
            updateMask: str = ...,
            **kwargs: typing.Any
        ) -> CmekSettingsHttpRequest: ...
        def getCmekSettings(
            self, *, name: str, **kwargs: typing.Any
        ) -> CmekSettingsHttpRequest: ...
    class ProjectsResource(googleapiclient.discovery.Resource):
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
                **kwargs: typing.Any
            ) -> ListLogsResponseHttpRequest: ...
        class LocationsResource(googleapiclient.discovery.Resource):
            class BucketsResource(googleapiclient.discovery.Resource):
                class ViewsResource(googleapiclient.discovery.Resource):
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> LogViewHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> ListViewsResponseHttpRequest: ...
                    def patch(
                        self,
                        *,
                        name: str,
                        body: LogView = ...,
                        updateMask: str = ...,
                        **kwargs: typing.Any
                    ) -> LogViewHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def create(
                        self,
                        *,
                        parent: str,
                        body: LogView = ...,
                        viewId: str = ...,
                        **kwargs: typing.Any
                    ) -> LogViewHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: LogBucket = ...,
                    updateMask: str = ...,
                    **kwargs: typing.Any
                ) -> LogBucketHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def undelete(
                    self,
                    *,
                    name: str,
                    body: UndeleteBucketRequest = ...,
                    **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListBucketsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> LogBucketHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: LogBucket = ...,
                    bucketId: str = ...,
                    **kwargs: typing.Any
                ) -> LogBucketHttpRequest: ...
                def views(self) -> ViewsResource: ...
            def buckets(self) -> BucketsResource: ...
        class SinksResource(googleapiclient.discovery.Resource):
            def patch(
                self,
                *,
                sinkName: str,
                body: LogSink = ...,
                updateMask: str = ...,
                uniqueWriterIdentity: bool = ...,
                **kwargs: typing.Any
            ) -> LogSinkHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListSinksResponseHttpRequest: ...
            def delete(
                self, *, sinkName: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def update(
                self,
                *,
                sinkName: str,
                body: LogSink = ...,
                updateMask: str = ...,
                uniqueWriterIdentity: bool = ...,
                **kwargs: typing.Any
            ) -> LogSinkHttpRequest: ...
            def get(
                self, *, sinkName: str, **kwargs: typing.Any
            ) -> LogSinkHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: LogSink = ...,
                uniqueWriterIdentity: bool = ...,
                **kwargs: typing.Any
            ) -> LogSinkHttpRequest: ...
        class MetricsResource(googleapiclient.discovery.Resource):
            def delete(
                self, *, metricName: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, metricName: str, **kwargs: typing.Any
            ) -> LogMetricHttpRequest: ...
            def update(
                self, *, metricName: str, body: LogMetric = ..., **kwargs: typing.Any
            ) -> LogMetricHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListLogMetricsResponseHttpRequest: ...
            def create(
                self, *, parent: str, body: LogMetric = ..., **kwargs: typing.Any
            ) -> LogMetricHttpRequest: ...
        class ExclusionsResource(googleapiclient.discovery.Resource):
            def patch(
                self,
                *,
                name: str,
                body: LogExclusion = ...,
                updateMask: str = ...,
                **kwargs: typing.Any
            ) -> LogExclusionHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LogExclusionHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def create(
                self, *, parent: str, body: LogExclusion = ..., **kwargs: typing.Any
            ) -> LogExclusionHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListExclusionsResponseHttpRequest: ...
        def logs(self) -> LogsResource: ...
        def locations(self) -> LocationsResource: ...
        def sinks(self) -> SinksResource: ...
        def metrics(self) -> MetricsResource: ...
        def exclusions(self) -> ExclusionsResource: ...
    def entries(self) -> EntriesResource: ...
    def logs(self) -> LogsResource: ...
    def monitoredResourceDescriptors(self) -> MonitoredResourceDescriptorsResource: ...
    def exclusions(self) -> ExclusionsResource: ...
    def billingAccounts(self) -> BillingAccountsResource: ...
    def sinks(self) -> SinksResource: ...
    def folders(self) -> FoldersResource: ...
    def locations(self) -> LocationsResource: ...
    def organizations(self) -> OrganizationsResource: ...
    def v2(self) -> V2Resource: ...
    def projects(self) -> ProjectsResource: ...

class ListSinksResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListSinksResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class ListLogEntriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLogEntriesResponse: ...

class ListBucketsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListBucketsResponse: ...

class LogViewHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LogView: ...

class LogExclusionHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LogExclusion: ...

class ListMonitoredResourceDescriptorsResponseHttpRequest(
    googleapiclient.http.HttpRequest
):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListMonitoredResourceDescriptorsResponse: ...

class LogMetricHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LogMetric: ...

class ListViewsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListViewsResponse: ...

class LogBucketHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LogBucket: ...

class LogSinkHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> LogSink: ...

class ListLogsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLogsResponse: ...

class ListExclusionsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListExclusionsResponse: ...

class ListLogMetricsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLogMetricsResponse: ...

class CmekSettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CmekSettings: ...

class WriteLogEntriesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> WriteLogEntriesResponse: ...

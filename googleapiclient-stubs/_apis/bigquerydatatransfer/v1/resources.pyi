import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class BigQueryDataTransferResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class DataSourcesResource(googleapiclient.discovery.Resource):
            def checkValidCreds(
                self,
                *,
                name: str,
                body: CheckValidCredsRequest = ...,
                **kwargs: typing.Any
            ) -> CheckValidCredsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> DataSourceHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListDataSourcesResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListDataSourcesResponseHttpRequest,
                previous_response: ListDataSourcesResponse,
            ) -> ListDataSourcesResponseHttpRequest | None: ...

        @typing.type_check_only
        class LocationsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class DataSourcesResource(googleapiclient.discovery.Resource):
                def checkValidCreds(
                    self,
                    *,
                    name: str,
                    body: CheckValidCredsRequest = ...,
                    **kwargs: typing.Any
                ) -> CheckValidCredsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DataSourceHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListDataSourcesResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListDataSourcesResponseHttpRequest,
                    previous_response: ListDataSourcesResponse,
                ) -> ListDataSourcesResponseHttpRequest | None: ...

            @typing.type_check_only
            class TransferConfigsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class RunsResource(googleapiclient.discovery.Resource):
                    @typing.type_check_only
                    class TransferLogsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            parent: str,
                            messageTypes: typing_extensions.Literal[
                                "MESSAGE_SEVERITY_UNSPECIFIED",
                                "INFO",
                                "WARNING",
                                "ERROR",
                            ]
                            | _list[
                                typing_extensions.Literal[
                                    "MESSAGE_SEVERITY_UNSPECIFIED",
                                    "INFO",
                                    "WARNING",
                                    "ERROR",
                                ]
                            ] = ...,
                            pageSize: int = ...,
                            pageToken: str = ...,
                            **kwargs: typing.Any
                        ) -> ListTransferLogsResponseHttpRequest: ...
                        def list_next(
                            self,
                            previous_request: ListTransferLogsResponseHttpRequest,
                            previous_response: ListTransferLogsResponse,
                        ) -> ListTransferLogsResponseHttpRequest | None: ...

                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> TransferRunHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        runAttempt: typing_extensions.Literal[
                            "RUN_ATTEMPT_UNSPECIFIED", "LATEST"
                        ] = ...,
                        states: typing_extensions.Literal[
                            "TRANSFER_STATE_UNSPECIFIED",
                            "PENDING",
                            "RUNNING",
                            "SUCCEEDED",
                            "FAILED",
                            "CANCELLED",
                        ]
                        | _list[
                            typing_extensions.Literal[
                                "TRANSFER_STATE_UNSPECIFIED",
                                "PENDING",
                                "RUNNING",
                                "SUCCEEDED",
                                "FAILED",
                                "CANCELLED",
                            ]
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> ListTransferRunsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListTransferRunsResponseHttpRequest,
                        previous_response: ListTransferRunsResponse,
                    ) -> ListTransferRunsResponseHttpRequest | None: ...
                    def transferLogs(self) -> TransferLogsResource: ...

                def create(
                    self,
                    *,
                    parent: str,
                    body: TransferConfig = ...,
                    authorizationCode: str = ...,
                    serviceAccountName: str = ...,
                    versionInfo: str = ...,
                    **kwargs: typing.Any
                ) -> TransferConfigHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> TransferConfigHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    dataSourceIds: str | _list[str] = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListTransferConfigsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListTransferConfigsResponseHttpRequest,
                    previous_response: ListTransferConfigsResponse,
                ) -> ListTransferConfigsResponseHttpRequest | None: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: TransferConfig = ...,
                    authorizationCode: str = ...,
                    serviceAccountName: str = ...,
                    updateMask: str = ...,
                    versionInfo: str = ...,
                    **kwargs: typing.Any
                ) -> TransferConfigHttpRequest: ...
                def scheduleRuns(
                    self,
                    *,
                    parent: str,
                    body: ScheduleTransferRunsRequest = ...,
                    **kwargs: typing.Any
                ) -> ScheduleTransferRunsResponseHttpRequest: ...
                def startManualRuns(
                    self,
                    *,
                    parent: str,
                    body: StartManualTransferRunsRequest = ...,
                    **kwargs: typing.Any
                ) -> StartManualTransferRunsResponseHttpRequest: ...
                def runs(self) -> RunsResource: ...

            def enrollDataSources(
                self,
                *,
                name: str,
                body: EnrollDataSourcesRequest = ...,
                **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
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
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListLocationsResponseHttpRequest,
                previous_response: ListLocationsResponse,
            ) -> ListLocationsResponseHttpRequest | None: ...
            def dataSources(self) -> DataSourcesResource: ...
            def transferConfigs(self) -> TransferConfigsResource: ...

        @typing.type_check_only
        class TransferConfigsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class RunsResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class TransferLogsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        messageTypes: typing_extensions.Literal[
                            "MESSAGE_SEVERITY_UNSPECIFIED", "INFO", "WARNING", "ERROR"
                        ]
                        | _list[
                            typing_extensions.Literal[
                                "MESSAGE_SEVERITY_UNSPECIFIED",
                                "INFO",
                                "WARNING",
                                "ERROR",
                            ]
                        ] = ...,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        **kwargs: typing.Any
                    ) -> ListTransferLogsResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListTransferLogsResponseHttpRequest,
                        previous_response: ListTransferLogsResponse,
                    ) -> ListTransferLogsResponseHttpRequest | None: ...

                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> TransferRunHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    runAttempt: typing_extensions.Literal[
                        "RUN_ATTEMPT_UNSPECIFIED", "LATEST"
                    ] = ...,
                    states: typing_extensions.Literal[
                        "TRANSFER_STATE_UNSPECIFIED",
                        "PENDING",
                        "RUNNING",
                        "SUCCEEDED",
                        "FAILED",
                        "CANCELLED",
                    ]
                    | _list[
                        typing_extensions.Literal[
                            "TRANSFER_STATE_UNSPECIFIED",
                            "PENDING",
                            "RUNNING",
                            "SUCCEEDED",
                            "FAILED",
                            "CANCELLED",
                        ]
                    ] = ...,
                    **kwargs: typing.Any
                ) -> ListTransferRunsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListTransferRunsResponseHttpRequest,
                    previous_response: ListTransferRunsResponse,
                ) -> ListTransferRunsResponseHttpRequest | None: ...
                def transferLogs(self) -> TransferLogsResource: ...

            def create(
                self,
                *,
                parent: str,
                body: TransferConfig = ...,
                authorizationCode: str = ...,
                serviceAccountName: str = ...,
                versionInfo: str = ...,
                **kwargs: typing.Any
            ) -> TransferConfigHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> TransferConfigHttpRequest: ...
            def list(
                self,
                *,
                parent: str,
                dataSourceIds: str | _list[str] = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListTransferConfigsResponseHttpRequest: ...
            def list_next(
                self,
                previous_request: ListTransferConfigsResponseHttpRequest,
                previous_response: ListTransferConfigsResponse,
            ) -> ListTransferConfigsResponseHttpRequest | None: ...
            def patch(
                self,
                *,
                name: str,
                body: TransferConfig = ...,
                authorizationCode: str = ...,
                serviceAccountName: str = ...,
                updateMask: str = ...,
                versionInfo: str = ...,
                **kwargs: typing.Any
            ) -> TransferConfigHttpRequest: ...
            def scheduleRuns(
                self,
                *,
                parent: str,
                body: ScheduleTransferRunsRequest = ...,
                **kwargs: typing.Any
            ) -> ScheduleTransferRunsResponseHttpRequest: ...
            def startManualRuns(
                self,
                *,
                parent: str,
                body: StartManualTransferRunsRequest = ...,
                **kwargs: typing.Any
            ) -> StartManualTransferRunsResponseHttpRequest: ...
            def runs(self) -> RunsResource: ...

        def enrollDataSources(
            self,
            *,
            name: str,
            body: EnrollDataSourcesRequest = ...,
            **kwargs: typing.Any
        ) -> EmptyHttpRequest: ...
        def dataSources(self) -> DataSourcesResource: ...
        def locations(self) -> LocationsResource: ...
        def transferConfigs(self) -> TransferConfigsResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class CheckValidCredsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CheckValidCredsResponse: ...

@typing.type_check_only
class DataSourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> DataSource: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Empty: ...

@typing.type_check_only
class ListDataSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListDataSourcesResponse: ...

@typing.type_check_only
class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListLocationsResponse: ...

@typing.type_check_only
class ListTransferConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListTransferConfigsResponse: ...

@typing.type_check_only
class ListTransferLogsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListTransferLogsResponse: ...

@typing.type_check_only
class ListTransferRunsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ListTransferRunsResponse: ...

@typing.type_check_only
class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Location: ...

@typing.type_check_only
class ScheduleTransferRunsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> ScheduleTransferRunsResponse: ...

@typing.type_check_only
class StartManualTransferRunsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> StartManualTransferRunsResponse: ...

@typing.type_check_only
class TransferConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TransferConfig: ...

@typing.type_check_only
class TransferRunHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> TransferRun: ...

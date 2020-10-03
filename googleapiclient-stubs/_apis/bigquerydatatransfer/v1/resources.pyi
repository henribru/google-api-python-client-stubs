import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class BigQueryDataTransferResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class TransferConfigsResource(googleapiclient.discovery.Resource):
            class RunsResource(googleapiclient.discovery.Resource):
                class TransferLogsResource(googleapiclient.discovery.Resource):
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int = ...,
                        pageToken: str = ...,
                        messageTypes: typing.Union[
                            typing_extensions.Literal[
                                "MESSAGE_SEVERITY_UNSPECIFIED",
                                "INFO",
                                "WARNING",
                                "ERROR",
                            ],
                            typing.List[
                                typing_extensions.Literal[
                                    "MESSAGE_SEVERITY_UNSPECIFIED",
                                    "INFO",
                                    "WARNING",
                                    "ERROR",
                                ]
                            ],
                        ] = ...,
                        **kwargs: typing.Any
                    ) -> ListTransferLogsResponseHttpRequest: ...
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
                    pageToken: str = ...,
                    states: typing.Union[
                        typing_extensions.Literal[
                            "TRANSFER_STATE_UNSPECIFIED",
                            "PENDING",
                            "RUNNING",
                            "SUCCEEDED",
                            "FAILED",
                            "CANCELLED",
                        ],
                        typing.List[
                            typing_extensions.Literal[
                                "TRANSFER_STATE_UNSPECIFIED",
                                "PENDING",
                                "RUNNING",
                                "SUCCEEDED",
                                "FAILED",
                                "CANCELLED",
                            ]
                        ],
                    ] = ...,
                    runAttempt: typing_extensions.Literal[
                        "RUN_ATTEMPT_UNSPECIFIED", "LATEST"
                    ] = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListTransferRunsResponseHttpRequest: ...
                def transferLogs(self) -> TransferLogsResource: ...
            def list(
                self,
                *,
                parent: str,
                pageSize: int = ...,
                dataSourceIds: typing.Union[str, typing.List[str]] = ...,
                pageToken: str = ...,
                **kwargs: typing.Any
            ) -> ListTransferConfigsResponseHttpRequest: ...
            def startManualRuns(
                self,
                *,
                parent: str,
                body: StartManualTransferRunsRequest = ...,
                **kwargs: typing.Any
            ) -> StartManualTransferRunsResponseHttpRequest: ...
            def scheduleRuns(
                self,
                *,
                parent: str,
                body: ScheduleTransferRunsRequest = ...,
                **kwargs: typing.Any
            ) -> ScheduleTransferRunsResponseHttpRequest: ...
            def patch(
                self,
                *,
                name: str,
                body: TransferConfig = ...,
                serviceAccountName: str = ...,
                updateMask: str = ...,
                versionInfo: str = ...,
                authorizationCode: str = ...,
                **kwargs: typing.Any
            ) -> TransferConfigHttpRequest: ...
            def create(
                self,
                *,
                parent: str,
                body: TransferConfig = ...,
                versionInfo: str = ...,
                serviceAccountName: str = ...,
                authorizationCode: str = ...,
                **kwargs: typing.Any
            ) -> TransferConfigHttpRequest: ...
            def delete(
                self, *, name: str, **kwargs: typing.Any
            ) -> EmptyHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> TransferConfigHttpRequest: ...
            def runs(self) -> RunsResource: ...
        class DataSourcesResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                parent: str,
                pageToken: str = ...,
                pageSize: int = ...,
                **kwargs: typing.Any
            ) -> ListDataSourcesResponseHttpRequest: ...
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
        class LocationsResource(googleapiclient.discovery.Resource):
            class TransferConfigsResource(googleapiclient.discovery.Resource):
                class RunsResource(googleapiclient.discovery.Resource):
                    class TransferLogsResource(googleapiclient.discovery.Resource):
                        def list(
                            self,
                            *,
                            parent: str,
                            pageToken: str = ...,
                            messageTypes: typing.Union[
                                typing_extensions.Literal[
                                    "MESSAGE_SEVERITY_UNSPECIFIED",
                                    "INFO",
                                    "WARNING",
                                    "ERROR",
                                ],
                                typing.List[
                                    typing_extensions.Literal[
                                        "MESSAGE_SEVERITY_UNSPECIFIED",
                                        "INFO",
                                        "WARNING",
                                        "ERROR",
                                    ]
                                ],
                            ] = ...,
                            pageSize: int = ...,
                            **kwargs: typing.Any
                        ) -> ListTransferLogsResponseHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        runAttempt: typing_extensions.Literal[
                            "RUN_ATTEMPT_UNSPECIFIED", "LATEST"
                        ] = ...,
                        states: typing.Union[
                            typing_extensions.Literal[
                                "TRANSFER_STATE_UNSPECIFIED",
                                "PENDING",
                                "RUNNING",
                                "SUCCEEDED",
                                "FAILED",
                                "CANCELLED",
                            ],
                            typing.List[
                                typing_extensions.Literal[
                                    "TRANSFER_STATE_UNSPECIFIED",
                                    "PENDING",
                                    "RUNNING",
                                    "SUCCEEDED",
                                    "FAILED",
                                    "CANCELLED",
                                ]
                            ],
                        ] = ...,
                        pageToken: str = ...,
                        pageSize: int = ...,
                        **kwargs: typing.Any
                    ) -> ListTransferRunsResponseHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def get(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> TransferRunHttpRequest: ...
                    def transferLogs(self) -> TransferLogsResource: ...
                def scheduleRuns(
                    self,
                    *,
                    parent: str,
                    body: ScheduleTransferRunsRequest = ...,
                    **kwargs: typing.Any
                ) -> ScheduleTransferRunsResponseHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: TransferConfig = ...,
                    updateMask: str = ...,
                    versionInfo: str = ...,
                    authorizationCode: str = ...,
                    serviceAccountName: str = ...,
                    **kwargs: typing.Any
                ) -> TransferConfigHttpRequest: ...
                def create(
                    self,
                    *,
                    parent: str,
                    body: TransferConfig = ...,
                    serviceAccountName: str = ...,
                    authorizationCode: str = ...,
                    versionInfo: str = ...,
                    **kwargs: typing.Any
                ) -> TransferConfigHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    dataSourceIds: typing.Union[str, typing.List[str]] = ...,
                    pageSize: int = ...,
                    pageToken: str = ...,
                    **kwargs: typing.Any
                ) -> ListTransferConfigsResponseHttpRequest: ...
                def startManualRuns(
                    self,
                    *,
                    parent: str,
                    body: StartManualTransferRunsRequest = ...,
                    **kwargs: typing.Any
                ) -> StartManualTransferRunsResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> TransferConfigHttpRequest: ...
                def delete(
                    self, *, name: str, **kwargs: typing.Any
                ) -> EmptyHttpRequest: ...
                def runs(self) -> RunsResource: ...
            class DataSourcesResource(googleapiclient.discovery.Resource):
                def list(
                    self,
                    *,
                    parent: str,
                    pageToken: str = ...,
                    pageSize: int = ...,
                    **kwargs: typing.Any
                ) -> ListDataSourcesResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DataSourceHttpRequest: ...
                def checkValidCreds(
                    self,
                    *,
                    name: str,
                    body: CheckValidCredsRequest = ...,
                    **kwargs: typing.Any
                ) -> CheckValidCredsResponseHttpRequest: ...
            def list(
                self,
                *,
                name: str,
                pageToken: str = ...,
                pageSize: int = ...,
                filter: str = ...,
                **kwargs: typing.Any
            ) -> ListLocationsResponseHttpRequest: ...
            def get(
                self, *, name: str, **kwargs: typing.Any
            ) -> LocationHttpRequest: ...
            def transferConfigs(self) -> TransferConfigsResource: ...
            def dataSources(self) -> DataSourcesResource: ...
        def transferConfigs(self) -> TransferConfigsResource: ...
        def dataSources(self) -> DataSourcesResource: ...
        def locations(self) -> LocationsResource: ...
    def projects(self) -> ProjectsResource: ...

class ListTransferConfigsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTransferConfigsResponse: ...

class ListTransferRunsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTransferRunsResponse: ...

class ListLocationsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListLocationsResponse: ...

class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Empty: ...

class StartManualTransferRunsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> StartManualTransferRunsResponse: ...

class TransferRunHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TransferRun: ...

class ListDataSourcesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListDataSourcesResponse: ...

class CheckValidCredsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CheckValidCredsResponse: ...

class LocationHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Location: ...

class ScheduleTransferRunsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ScheduleTransferRunsResponse: ...

class TransferConfigHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> TransferConfig: ...

class ListTransferLogsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListTransferLogsResponse: ...

class DataSourceHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DataSource: ...

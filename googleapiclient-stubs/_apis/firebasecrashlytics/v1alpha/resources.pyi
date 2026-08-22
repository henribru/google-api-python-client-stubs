import collections.abc
import typing

import httplib2

import googleapiclient.discovery
import googleapiclient.http

from .schemas import *

_list = list

@typing.type_check_only
class FirebaseCrashlyticsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class AppsResource(googleapiclient.discovery.Resource):
            @typing.type_check_only
            class EventsResource(googleapiclient.discovery.Resource):
                def batchGet(
                    self,
                    *,
                    parent: str,
                    names: str | _list[str] | None = ...,
                    readMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> BatchGetEventsResponseHttpRequest: ...
                def list(
                    self,
                    *,
                    parent: str,
                    filter_browser_displayNames: str | _list[str] | None = ...,
                    filter_device_displayNames: str | _list[str] | None = ...,
                    filter_device_formFactors: typing.Literal[
                        "FORM_FACTOR_UNSPECIFIED",
                        "PHONE",
                        "TABLET",
                        "DESKTOP",
                        "TV",
                        "WATCH",
                    ]
                    | _list[
                        typing.Literal[
                            "FORM_FACTOR_UNSPECIFIED",
                            "PHONE",
                            "TABLET",
                            "DESKTOP",
                            "TV",
                            "WATCH",
                        ]
                    ]
                    | None = ...,
                    filter_interval_endTime: str | None = ...,
                    filter_interval_startTime: str | None = ...,
                    filter_issue_content: str | None = ...,
                    filter_issue_errorTypes: typing.Literal[
                        "ERROR_TYPE_UNSPECIFIED", "FATAL", "NON_FATAL", "ANR"
                    ]
                    | _list[
                        typing.Literal[
                            "ERROR_TYPE_UNSPECIFIED", "FATAL", "NON_FATAL", "ANR"
                        ]
                    ]
                    | None = ...,
                    filter_issue_id: str | None = ...,
                    filter_issue_signals: typing.Literal[
                        "SIGNAL_UNSPECIFIED",
                        "SIGNAL_EARLY",
                        "SIGNAL_FRESH",
                        "SIGNAL_REGRESSED",
                        "SIGNAL_REPETITIVE",
                    ]
                    | _list[
                        typing.Literal[
                            "SIGNAL_UNSPECIFIED",
                            "SIGNAL_EARLY",
                            "SIGNAL_FRESH",
                            "SIGNAL_REGRESSED",
                            "SIGNAL_REPETITIVE",
                        ]
                    ]
                    | None = ...,
                    filter_issue_state: typing.Literal[
                        "STATE_UNSPECIFIED", "OPEN", "CLOSED", "MUTED"
                    ]
                    | None = ...,
                    filter_issue_states: typing.Literal[
                        "STATE_UNSPECIFIED", "OPEN", "CLOSED", "MUTED"
                    ]
                    | _list[
                        typing.Literal["STATE_UNSPECIFIED", "OPEN", "CLOSED", "MUTED"]
                    ]
                    | None = ...,
                    filter_issue_variantId: str | None = ...,
                    filter_operatingSystem_displayNames: str | _list[str] | None = ...,
                    filter_version_displayNames: str | _list[str] | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    readMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ListEventsResponseHttpRequest: ...
                def list_next(
                    self,
                    previous_request: ListEventsResponseHttpRequest,
                    previous_response: ListEventsResponse,
                ) -> ListEventsResponseHttpRequest | None: ...

            @typing.type_check_only
            class IssuesResource(googleapiclient.discovery.Resource):
                @typing.type_check_only
                class NotesResource(googleapiclient.discovery.Resource):
                    def create(
                        self, *, parent: str, body: Note, **kwargs: typing.Any
                    ) -> NoteHttpRequest: ...
                    def delete(
                        self, *, name: str, **kwargs: typing.Any
                    ) -> EmptyHttpRequest: ...
                    def list(
                        self,
                        *,
                        parent: str,
                        pageSize: int | None = ...,
                        pageToken: str | None = ...,
                        **kwargs: typing.Any,
                    ) -> ListNotesResponseHttpRequest: ...
                    def list_next(
                        self,
                        previous_request: ListNotesResponseHttpRequest,
                        previous_response: ListNotesResponse,
                    ) -> ListNotesResponseHttpRequest | None: ...

                def batchUpdate(
                    self,
                    *,
                    parent: str,
                    body: BatchUpdateIssuesRequest,
                    **kwargs: typing.Any,
                ) -> BatchUpdateIssuesResponseHttpRequest: ...
                def get(
                    self, *, name: str, **kwargs: typing.Any
                ) -> IssueHttpRequest: ...
                def patch(
                    self,
                    *,
                    name: str,
                    body: Issue,
                    updateMask: str | None = ...,
                    **kwargs: typing.Any,
                ) -> IssueHttpRequest: ...
                def notes(self) -> NotesResource: ...

            @typing.type_check_only
            class ReportsResource(googleapiclient.discovery.Resource):
                def get(
                    self,
                    *,
                    name: str,
                    filter_browser_displayNames: str | _list[str] | None = ...,
                    filter_device_displayNames: str | _list[str] | None = ...,
                    filter_device_formFactors: typing.Literal[
                        "FORM_FACTOR_UNSPECIFIED",
                        "PHONE",
                        "TABLET",
                        "DESKTOP",
                        "TV",
                        "WATCH",
                    ]
                    | _list[
                        typing.Literal[
                            "FORM_FACTOR_UNSPECIFIED",
                            "PHONE",
                            "TABLET",
                            "DESKTOP",
                            "TV",
                            "WATCH",
                        ]
                    ]
                    | None = ...,
                    filter_interval_endTime: str | None = ...,
                    filter_interval_startTime: str | None = ...,
                    filter_issue_content: str | None = ...,
                    filter_issue_errorTypes: typing.Literal[
                        "ERROR_TYPE_UNSPECIFIED", "FATAL", "NON_FATAL", "ANR"
                    ]
                    | _list[
                        typing.Literal[
                            "ERROR_TYPE_UNSPECIFIED", "FATAL", "NON_FATAL", "ANR"
                        ]
                    ]
                    | None = ...,
                    filter_issue_id: str | None = ...,
                    filter_issue_signals: typing.Literal[
                        "SIGNAL_UNSPECIFIED",
                        "SIGNAL_EARLY",
                        "SIGNAL_FRESH",
                        "SIGNAL_REGRESSED",
                        "SIGNAL_REPETITIVE",
                    ]
                    | _list[
                        typing.Literal[
                            "SIGNAL_UNSPECIFIED",
                            "SIGNAL_EARLY",
                            "SIGNAL_FRESH",
                            "SIGNAL_REGRESSED",
                            "SIGNAL_REPETITIVE",
                        ]
                    ]
                    | None = ...,
                    filter_issue_state: typing.Literal[
                        "STATE_UNSPECIFIED", "OPEN", "CLOSED", "MUTED"
                    ]
                    | None = ...,
                    filter_issue_states: typing.Literal[
                        "STATE_UNSPECIFIED", "OPEN", "CLOSED", "MUTED"
                    ]
                    | _list[
                        typing.Literal["STATE_UNSPECIFIED", "OPEN", "CLOSED", "MUTED"]
                    ]
                    | None = ...,
                    filter_issue_variantId: str | None = ...,
                    filter_operatingSystem_displayNames: str | _list[str] | None = ...,
                    filter_version_displayNames: str | _list[str] | None = ...,
                    granularity: typing.Literal[
                        "TIME_GRANULARITY_UNSPECIFIED",
                        "TIME_GRANULARITY_NONE",
                        "TIME_GRANULARITY_HOUR",
                        "TIME_GRANULARITY_DAY",
                    ]
                    | None = ...,
                    pageSize: int | None = ...,
                    pageToken: str | None = ...,
                    **kwargs: typing.Any,
                ) -> ReportHttpRequest: ...
                def get_next(
                    self, previous_request: ReportHttpRequest, previous_response: Report
                ) -> ReportHttpRequest | None: ...
                def list(
                    self, *, parent: str, **kwargs: typing.Any
                ) -> ListReportsResponseHttpRequest: ...

            @typing.type_check_only
            class UsersResource(googleapiclient.discovery.Resource):
                def deleteCrashReports(
                    self, *, name: str, **kwargs: typing.Any
                ) -> DeleteUserCrashReportsResponseHttpRequest: ...

            def events(self) -> EventsResource: ...
            def issues(self) -> IssuesResource: ...
            def reports(self) -> ReportsResource: ...
            def users(self) -> UsersResource: ...

        def apps(self) -> AppsResource: ...

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
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class BatchGetEventsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchGetEventsResponse: ...

@typing.type_check_only
class BatchUpdateIssuesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> BatchUpdateIssuesResponse: ...

@typing.type_check_only
class DeleteUserCrashReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> DeleteUserCrashReportsResponse: ...

@typing.type_check_only
class EmptyHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Empty: ...

@typing.type_check_only
class IssueHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Issue: ...

@typing.type_check_only
class ListEventsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListEventsResponse: ...

@typing.type_check_only
class ListNotesResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListNotesResponse: ...

@typing.type_check_only
class ListReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> ListReportsResponse: ...

@typing.type_check_only
class NoteHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Note: ...

@typing.type_check_only
class ReportHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Report: ...

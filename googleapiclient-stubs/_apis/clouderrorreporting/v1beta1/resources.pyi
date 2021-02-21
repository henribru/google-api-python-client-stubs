import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class ClouderrorreportingResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ProjectsResource(googleapiclient.discovery.Resource):
        @typing.type_check_only
        class EventsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                projectName: str,
                groupId: str = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                serviceFilter_resourceType: str = ...,
                serviceFilter_service: str = ...,
                serviceFilter_version: str = ...,
                timeRange_period: typing_extensions.Literal[
                    "PERIOD_UNSPECIFIED",
                    "PERIOD_1_HOUR",
                    "PERIOD_6_HOURS",
                    "PERIOD_1_DAY",
                    "PERIOD_1_WEEK",
                    "PERIOD_30_DAYS",
                ] = ...,
                **kwargs: typing.Any
            ) -> ListEventsResponseHttpRequest: ...
            def report(
                self,
                *,
                projectName: str,
                body: ReportedErrorEvent = ...,
                **kwargs: typing.Any
            ) -> ReportErrorEventResponseHttpRequest: ...
        @typing.type_check_only
        class GroupStatsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                projectName: str,
                alignment: typing_extensions.Literal[
                    "ERROR_COUNT_ALIGNMENT_UNSPECIFIED",
                    "ALIGNMENT_EQUAL_ROUNDED",
                    "ALIGNMENT_EQUAL_AT_END",
                ] = ...,
                alignmentTime: str = ...,
                groupId: typing.Union[str, typing.List[str]] = ...,
                order: typing_extensions.Literal[
                    "GROUP_ORDER_UNSPECIFIED",
                    "COUNT_DESC",
                    "LAST_SEEN_DESC",
                    "CREATED_DESC",
                    "AFFECTED_USERS_DESC",
                ] = ...,
                pageSize: int = ...,
                pageToken: str = ...,
                serviceFilter_resourceType: str = ...,
                serviceFilter_service: str = ...,
                serviceFilter_version: str = ...,
                timeRange_period: typing_extensions.Literal[
                    "PERIOD_UNSPECIFIED",
                    "PERIOD_1_HOUR",
                    "PERIOD_6_HOURS",
                    "PERIOD_1_DAY",
                    "PERIOD_1_WEEK",
                    "PERIOD_30_DAYS",
                ] = ...,
                timedCountDuration: str = ...,
                **kwargs: typing.Any
            ) -> ListGroupStatsResponseHttpRequest: ...
        @typing.type_check_only
        class GroupsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, groupName: str, **kwargs: typing.Any
            ) -> ErrorGroupHttpRequest: ...
            def update(
                self, *, name: str, body: ErrorGroup = ..., **kwargs: typing.Any
            ) -> ErrorGroupHttpRequest: ...
        def deleteEvents(
            self, *, projectName: str, **kwargs: typing.Any
        ) -> DeleteEventsResponseHttpRequest: ...
        def events(self) -> EventsResource: ...
        def groupStats(self) -> GroupStatsResource: ...
        def groups(self) -> GroupsResource: ...
    def projects(self) -> ProjectsResource: ...

@typing.type_check_only
class DeleteEventsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> DeleteEventsResponse: ...

@typing.type_check_only
class ErrorGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ErrorGroup: ...

@typing.type_check_only
class ListEventsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListEventsResponse: ...

@typing.type_check_only
class ListGroupStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ListGroupStatsResponse: ...

@typing.type_check_only
class ReportErrorEventResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> ReportErrorEventResponse: ...

import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class ClouderrorreportingResource(googleapiclient.discovery.Resource):
    class ProjectsResource(googleapiclient.discovery.Resource):
        class EventsResource(googleapiclient.discovery.Resource):
            def report(
                self,
                *,
                projectName: str,
                body: ReportedErrorEvent = ...,
                **kwargs: typing.Any
            ) -> ReportErrorEventResponseHttpRequest: ...
            def list(
                self,
                *,
                projectName: str,
                pageSize: int = ...,
                serviceFilter_resourceType: str = ...,
                serviceFilter_version: str = ...,
                pageToken: str = ...,
                groupId: str = ...,
                timeRange_period: typing_extensions.Literal[
                    "PERIOD_UNSPECIFIED",
                    "PERIOD_1_HOUR",
                    "PERIOD_6_HOURS",
                    "PERIOD_1_DAY",
                    "PERIOD_1_WEEK",
                    "PERIOD_30_DAYS",
                ] = ...,
                serviceFilter_service: str = ...,
                **kwargs: typing.Any
            ) -> ListEventsResponseHttpRequest: ...
        class GroupsResource(googleapiclient.discovery.Resource):
            def get(
                self, *, groupName: str, **kwargs: typing.Any
            ) -> ErrorGroupHttpRequest: ...
            def update(
                self, *, name: str, body: ErrorGroup = ..., **kwargs: typing.Any
            ) -> ErrorGroupHttpRequest: ...
        class GroupStatsResource(googleapiclient.discovery.Resource):
            def list(
                self,
                *,
                projectName: str,
                pageToken: str = ...,
                serviceFilter_service: str = ...,
                pageSize: int = ...,
                serviceFilter_resourceType: str = ...,
                timedCountDuration: str = ...,
                serviceFilter_version: str = ...,
                groupId: typing.Union[str, typing.List[str]] = ...,
                order: typing_extensions.Literal[
                    "GROUP_ORDER_UNSPECIFIED",
                    "COUNT_DESC",
                    "LAST_SEEN_DESC",
                    "CREATED_DESC",
                    "AFFECTED_USERS_DESC",
                ] = ...,
                alignmentTime: str = ...,
                alignment: typing_extensions.Literal[
                    "ERROR_COUNT_ALIGNMENT_UNSPECIFIED",
                    "ALIGNMENT_EQUAL_ROUNDED",
                    "ALIGNMENT_EQUAL_AT_END",
                ] = ...,
                timeRange_period: typing_extensions.Literal[
                    "PERIOD_UNSPECIFIED",
                    "PERIOD_1_HOUR",
                    "PERIOD_6_HOURS",
                    "PERIOD_1_DAY",
                    "PERIOD_1_WEEK",
                    "PERIOD_30_DAYS",
                ] = ...,
                **kwargs: typing.Any
            ) -> ListGroupStatsResponseHttpRequest: ...
        def deleteEvents(
            self, *, projectName: str, **kwargs: typing.Any
        ) -> DeleteEventsResponseHttpRequest: ...
        def events(self) -> EventsResource: ...
        def groups(self) -> GroupsResource: ...
        def groupStats(self) -> GroupStatsResource: ...
    def projects(self) -> ProjectsResource: ...

class ListEventsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListEventsResponse: ...

class ReportErrorEventResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ReportErrorEventResponse: ...

class DeleteEventsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> DeleteEventsResponse: ...

class ListGroupStatsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ListGroupStatsResponse: ...

class ErrorGroupHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> ErrorGroup: ...

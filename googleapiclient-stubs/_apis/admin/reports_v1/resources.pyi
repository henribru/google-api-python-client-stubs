import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class ReportsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ActivitiesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            userKey: str,
            applicationName: typing_extensions.Literal[
                "access_transparency",
                "admin",
                "calendar",
                "chat",
                "drive",
                "gcp",
                "gplus",
                "groups",
                "groups_enterprise",
                "jamboard",
                "login",
                "meet",
                "mobile",
                "rules",
                "saml",
                "token",
                "user_accounts",
                "context_aware_access",
                "chrome",
                "data_studio",
                "keep",
            ],
            actorIpAddress: str = ...,
            customerId: str = ...,
            endTime: str = ...,
            eventName: str = ...,
            filters: str = ...,
            groupIdFilter: str = ...,
            maxResults: int = ...,
            orgUnitID: str = ...,
            pageToken: str = ...,
            startTime: str = ...,
            **kwargs: typing.Any
        ) -> ActivitiesHttpRequest: ...
        def list_next(
            self, previous_request: ActivitiesHttpRequest, previous_response: Activities
        ) -> ActivitiesHttpRequest | None: ...
        def watch(
            self,
            *,
            userKey: str,
            applicationName: typing_extensions.Literal[
                "access_transparency",
                "admin",
                "calendar",
                "chat",
                "drive",
                "gcp",
                "gplus",
                "groups",
                "groups_enterprise",
                "jamboard",
                "login",
                "meet",
                "mobile",
                "rules",
                "saml",
                "token",
                "user_accounts",
                "context_aware_access",
                "chrome",
                "data_studio",
                "keep",
            ],
            body: Channel = ...,
            actorIpAddress: str = ...,
            customerId: str = ...,
            endTime: str = ...,
            eventName: str = ...,
            filters: str = ...,
            groupIdFilter: str = ...,
            maxResults: int = ...,
            orgUnitID: str = ...,
            pageToken: str = ...,
            startTime: str = ...,
            **kwargs: typing.Any
        ) -> ChannelHttpRequest: ...

    @typing.type_check_only
    class ChannelsResource(googleapiclient.discovery.Resource):
        def stop(
            self, *, body: Channel = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class CustomerUsageReportsResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            date: str,
            customerId: str = ...,
            pageToken: str = ...,
            parameters: str = ...,
            **kwargs: typing.Any
        ) -> UsageReportsHttpRequest: ...
        def get_next(
            self,
            previous_request: UsageReportsHttpRequest,
            previous_response: UsageReports,
        ) -> UsageReportsHttpRequest | None: ...

    @typing.type_check_only
    class EntityUsageReportsResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            entityType: typing_extensions.Literal["gplus_communities"],
            entityKey: str,
            date: str,
            customerId: str = ...,
            filters: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            parameters: str = ...,
            **kwargs: typing.Any
        ) -> UsageReportsHttpRequest: ...
        def get_next(
            self,
            previous_request: UsageReportsHttpRequest,
            previous_response: UsageReports,
        ) -> UsageReportsHttpRequest | None: ...

    @typing.type_check_only
    class UserUsageReportResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            userKey: str,
            date: str,
            customerId: str = ...,
            filters: str = ...,
            groupIdFilter: str = ...,
            maxResults: int = ...,
            orgUnitID: str = ...,
            pageToken: str = ...,
            parameters: str = ...,
            **kwargs: typing.Any
        ) -> UsageReportsHttpRequest: ...
        def get_next(
            self,
            previous_request: UsageReportsHttpRequest,
            previous_response: UsageReports,
        ) -> UsageReportsHttpRequest | None: ...

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
    def activities(self) -> ActivitiesResource: ...
    def channels(self) -> ChannelsResource: ...
    def customerUsageReports(self) -> CustomerUsageReportsResource: ...
    def entityUsageReports(self) -> EntityUsageReportsResource: ...
    def userUsageReport(self) -> UserUsageReportResource: ...

@typing.type_check_only
class ActivitiesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Activities: ...

@typing.type_check_only
class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Channel: ...

@typing.type_check_only
class UsageReportsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> UsageReports: ...

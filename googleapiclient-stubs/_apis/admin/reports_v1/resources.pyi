import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *
@typing.type_check_only
class ReportsResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class ActivitiesResource(googleapiclient.discovery.Resource):
        def list(
            self,
            *,
            userKey: str,
            applicationName: typing_extensions.Literal[
                "application_name_undefined",
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
        def watch(
            self,
            *,
            userKey: str,
            applicationName: typing_extensions.Literal[
                "application_name_unspecified",
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
    @typing.type_check_only
    class EntityUsageReportsResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            entityType: typing_extensions.Literal[
                "entity_type_undefined", "gplus_communities"
            ],
            entityKey: typing_extensions.Literal[
                "entityKeyUndefined", "all", "entityKey"
            ],
            date: str,
            customerId: str = ...,
            filters: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            parameters: str = ...,
            **kwargs: typing.Any
        ) -> UsageReportsHttpRequest: ...
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
    def activities(self) -> ActivitiesResource: ...
    def channels(self) -> ChannelsResource: ...
    def customerUsageReports(self) -> CustomerUsageReportsResource: ...
    def entityUsageReports(self) -> EntityUsageReportsResource: ...
    def userUsageReport(self) -> UserUsageReportResource: ...

@typing.type_check_only
class ActivitiesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Activities: ...

@typing.type_check_only
class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Channel: ...

@typing.type_check_only
class UsageReportsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> UsageReports: ...

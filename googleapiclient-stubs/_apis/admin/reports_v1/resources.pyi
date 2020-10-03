import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class ReportsResource(googleapiclient.discovery.Resource):
    class UserUsageReportResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            userKey: str,
            date: str,
            parameters: str = ...,
            maxResults: int = ...,
            filters: str = ...,
            customerId: str = ...,
            pageToken: str = ...,
            orgUnitID: str = ...,
            **kwargs: typing.Any
        ) -> UsageReportsHttpRequest: ...
    class ChannelsResource(googleapiclient.discovery.Resource):
        def stop(
            self, *, body: Channel = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
    class CustomerUsageReportsResource(googleapiclient.discovery.Resource):
        def get(
            self,
            *,
            date: str,
            parameters: str = ...,
            pageToken: str = ...,
            customerId: str = ...,
            **kwargs: typing.Any
        ) -> UsageReportsHttpRequest: ...
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
            pageToken: str = ...,
            parameters: str = ...,
            customerId: str = ...,
            filters: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> UsageReportsHttpRequest: ...
    class ActivitiesResource(googleapiclient.discovery.Resource):
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
            ],
            body: Channel = ...,
            actorIpAddress: str = ...,
            endTime: str = ...,
            filters: str = ...,
            pageToken: str = ...,
            orgUnitID: str = ...,
            startTime: str = ...,
            eventName: str = ...,
            customerId: str = ...,
            maxResults: int = ...,
            **kwargs: typing.Any
        ) -> ChannelHttpRequest: ...
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
            ],
            eventName: str = ...,
            pageToken: str = ...,
            startTime: str = ...,
            orgUnitID: str = ...,
            actorIpAddress: str = ...,
            filters: str = ...,
            customerId: str = ...,
            maxResults: int = ...,
            endTime: str = ...,
            **kwargs: typing.Any
        ) -> ActivitiesHttpRequest: ...
    def userUsageReport(self) -> UserUsageReportResource: ...
    def channels(self) -> ChannelsResource: ...
    def customerUsageReports(self) -> CustomerUsageReportsResource: ...
    def entityUsageReports(self) -> EntityUsageReportsResource: ...
    def activities(self) -> ActivitiesResource: ...

class ActivitiesHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Activities: ...

class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Channel: ...

class UsageReportsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> UsageReports: ...

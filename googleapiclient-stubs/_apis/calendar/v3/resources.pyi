import collections.abc
import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

_list = list

@typing.type_check_only
class CalendarResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class AclResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, calendarId: str, ruleId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, calendarId: str, ruleId: str, **kwargs: typing.Any
        ) -> AclRuleHttpRequest: ...
        def insert(
            self,
            *,
            calendarId: str,
            body: AclRule = ...,
            sendNotifications: bool = ...,
            **kwargs: typing.Any
        ) -> AclRuleHttpRequest: ...
        def list(
            self,
            *,
            calendarId: str,
            maxResults: int = ...,
            pageToken: str = ...,
            showDeleted: bool = ...,
            syncToken: str = ...,
            **kwargs: typing.Any
        ) -> AclHttpRequest: ...
        def list_next(
            self, previous_request: AclHttpRequest, previous_response: Acl
        ) -> AclHttpRequest | None: ...
        def patch(
            self,
            *,
            calendarId: str,
            ruleId: str,
            body: AclRule = ...,
            sendNotifications: bool = ...,
            **kwargs: typing.Any
        ) -> AclRuleHttpRequest: ...
        def update(
            self,
            *,
            calendarId: str,
            ruleId: str,
            body: AclRule = ...,
            sendNotifications: bool = ...,
            **kwargs: typing.Any
        ) -> AclRuleHttpRequest: ...
        def watch(
            self,
            *,
            calendarId: str,
            body: Channel = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            showDeleted: bool = ...,
            syncToken: str = ...,
            **kwargs: typing.Any
        ) -> ChannelHttpRequest: ...

    @typing.type_check_only
    class CalendarListResource(googleapiclient.discovery.Resource):
        def delete(
            self, *, calendarId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, calendarId: str, **kwargs: typing.Any
        ) -> CalendarListEntryHttpRequest: ...
        def insert(
            self,
            *,
            body: CalendarListEntry = ...,
            colorRgbFormat: bool = ...,
            **kwargs: typing.Any
        ) -> CalendarListEntryHttpRequest: ...
        def list(
            self,
            *,
            maxResults: int = ...,
            minAccessRole: typing_extensions.Literal[
                "freeBusyReader", "owner", "reader", "writer"
            ] = ...,
            pageToken: str = ...,
            showDeleted: bool = ...,
            showHidden: bool = ...,
            syncToken: str = ...,
            **kwargs: typing.Any
        ) -> CalendarListHttpRequest: ...
        def list_next(
            self,
            previous_request: CalendarListHttpRequest,
            previous_response: CalendarList,
        ) -> CalendarListHttpRequest | None: ...
        def patch(
            self,
            *,
            calendarId: str,
            body: CalendarListEntry = ...,
            colorRgbFormat: bool = ...,
            **kwargs: typing.Any
        ) -> CalendarListEntryHttpRequest: ...
        def update(
            self,
            *,
            calendarId: str,
            body: CalendarListEntry = ...,
            colorRgbFormat: bool = ...,
            **kwargs: typing.Any
        ) -> CalendarListEntryHttpRequest: ...
        def watch(
            self,
            *,
            body: Channel = ...,
            maxResults: int = ...,
            minAccessRole: typing_extensions.Literal[
                "freeBusyReader", "owner", "reader", "writer"
            ] = ...,
            pageToken: str = ...,
            showDeleted: bool = ...,
            showHidden: bool = ...,
            syncToken: str = ...,
            **kwargs: typing.Any
        ) -> ChannelHttpRequest: ...

    @typing.type_check_only
    class CalendarsResource(googleapiclient.discovery.Resource):
        def clear(
            self, *, calendarId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def delete(
            self, *, calendarId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, calendarId: str, **kwargs: typing.Any
        ) -> CalendarHttpRequest: ...
        def insert(
            self, *, body: Calendar = ..., **kwargs: typing.Any
        ) -> CalendarHttpRequest: ...
        def patch(
            self, *, calendarId: str, body: Calendar = ..., **kwargs: typing.Any
        ) -> CalendarHttpRequest: ...
        def update(
            self, *, calendarId: str, body: Calendar = ..., **kwargs: typing.Any
        ) -> CalendarHttpRequest: ...

    @typing.type_check_only
    class ChannelsResource(googleapiclient.discovery.Resource):
        def stop(
            self, *, body: Channel = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...

    @typing.type_check_only
    class ColorsResource(googleapiclient.discovery.Resource):
        def get(self, **kwargs: typing.Any) -> ColorsHttpRequest: ...

    @typing.type_check_only
    class EventsResource(googleapiclient.discovery.Resource):
        def delete(
            self,
            *,
            calendarId: str,
            eventId: str,
            sendNotifications: bool = ...,
            sendUpdates: typing_extensions.Literal["all", "externalOnly", "none"] = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            calendarId: str,
            eventId: str,
            alwaysIncludeEmail: bool = ...,
            maxAttendees: int = ...,
            timeZone: str = ...,
            **kwargs: typing.Any
        ) -> EventHttpRequest: ...
        def import_(
            self,
            *,
            calendarId: str,
            body: Event = ...,
            conferenceDataVersion: int = ...,
            supportsAttachments: bool = ...,
            **kwargs: typing.Any
        ) -> EventHttpRequest: ...
        def insert(
            self,
            *,
            calendarId: str,
            body: Event = ...,
            conferenceDataVersion: int = ...,
            maxAttendees: int = ...,
            sendNotifications: bool = ...,
            sendUpdates: typing_extensions.Literal["all", "externalOnly", "none"] = ...,
            supportsAttachments: bool = ...,
            **kwargs: typing.Any
        ) -> EventHttpRequest: ...
        def instances(
            self,
            *,
            calendarId: str,
            eventId: str,
            alwaysIncludeEmail: bool = ...,
            maxAttendees: int = ...,
            maxResults: int = ...,
            originalStart: str = ...,
            pageToken: str = ...,
            showDeleted: bool = ...,
            timeMax: str = ...,
            timeMin: str = ...,
            timeZone: str = ...,
            **kwargs: typing.Any
        ) -> EventsHttpRequest: ...
        def instances_next(
            self, previous_request: EventsHttpRequest, previous_response: Events
        ) -> EventsHttpRequest | None: ...
        def list(
            self,
            *,
            calendarId: str,
            alwaysIncludeEmail: bool = ...,
            iCalUID: str = ...,
            maxAttendees: int = ...,
            maxResults: int = ...,
            orderBy: typing_extensions.Literal["startTime", "updated"] = ...,
            pageToken: str = ...,
            privateExtendedProperty: str | _list[str] = ...,
            q: str = ...,
            sharedExtendedProperty: str | _list[str] = ...,
            showDeleted: bool = ...,
            showHiddenInvitations: bool = ...,
            singleEvents: bool = ...,
            syncToken: str = ...,
            timeMax: str = ...,
            timeMin: str = ...,
            timeZone: str = ...,
            updatedMin: str = ...,
            **kwargs: typing.Any
        ) -> EventsHttpRequest: ...
        def list_next(
            self, previous_request: EventsHttpRequest, previous_response: Events
        ) -> EventsHttpRequest | None: ...
        def move(
            self,
            *,
            calendarId: str,
            eventId: str,
            destination: str,
            sendNotifications: bool = ...,
            sendUpdates: typing_extensions.Literal["all", "externalOnly", "none"] = ...,
            **kwargs: typing.Any
        ) -> EventHttpRequest: ...
        def patch(
            self,
            *,
            calendarId: str,
            eventId: str,
            body: Event = ...,
            alwaysIncludeEmail: bool = ...,
            conferenceDataVersion: int = ...,
            maxAttendees: int = ...,
            sendNotifications: bool = ...,
            sendUpdates: typing_extensions.Literal["all", "externalOnly", "none"] = ...,
            supportsAttachments: bool = ...,
            **kwargs: typing.Any
        ) -> EventHttpRequest: ...
        def quickAdd(
            self,
            *,
            calendarId: str,
            text: str,
            sendNotifications: bool = ...,
            sendUpdates: typing_extensions.Literal["all", "externalOnly", "none"] = ...,
            **kwargs: typing.Any
        ) -> EventHttpRequest: ...
        def update(
            self,
            *,
            calendarId: str,
            eventId: str,
            body: Event = ...,
            alwaysIncludeEmail: bool = ...,
            conferenceDataVersion: int = ...,
            maxAttendees: int = ...,
            sendNotifications: bool = ...,
            sendUpdates: typing_extensions.Literal["all", "externalOnly", "none"] = ...,
            supportsAttachments: bool = ...,
            **kwargs: typing.Any
        ) -> EventHttpRequest: ...
        def watch(
            self,
            *,
            calendarId: str,
            body: Channel = ...,
            alwaysIncludeEmail: bool = ...,
            iCalUID: str = ...,
            maxAttendees: int = ...,
            maxResults: int = ...,
            orderBy: typing_extensions.Literal["startTime", "updated"] = ...,
            pageToken: str = ...,
            privateExtendedProperty: str | _list[str] = ...,
            q: str = ...,
            sharedExtendedProperty: str | _list[str] = ...,
            showDeleted: bool = ...,
            showHiddenInvitations: bool = ...,
            singleEvents: bool = ...,
            syncToken: str = ...,
            timeMax: str = ...,
            timeMin: str = ...,
            timeZone: str = ...,
            updatedMin: str = ...,
            **kwargs: typing.Any
        ) -> ChannelHttpRequest: ...

    @typing.type_check_only
    class FreebusyResource(googleapiclient.discovery.Resource):
        def query(
            self, *, body: FreeBusyRequest = ..., **kwargs: typing.Any
        ) -> FreeBusyResponseHttpRequest: ...

    @typing.type_check_only
    class SettingsResource(googleapiclient.discovery.Resource):
        def get(self, *, setting: str, **kwargs: typing.Any) -> SettingHttpRequest: ...
        def list(
            self,
            *,
            maxResults: int = ...,
            pageToken: str = ...,
            syncToken: str = ...,
            **kwargs: typing.Any
        ) -> SettingsHttpRequest: ...
        def list_next(
            self, previous_request: SettingsHttpRequest, previous_response: Settings
        ) -> SettingsHttpRequest | None: ...
        def watch(
            self,
            *,
            body: Channel = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            syncToken: str = ...,
            **kwargs: typing.Any
        ) -> ChannelHttpRequest: ...

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
    def acl(self) -> AclResource: ...
    def calendarList(self) -> CalendarListResource: ...
    def calendars(self) -> CalendarsResource: ...
    def channels(self) -> ChannelsResource: ...
    def colors(self) -> ColorsResource: ...
    def events(self) -> EventsResource: ...
    def freebusy(self) -> FreebusyResource: ...
    def settings(self) -> SettingsResource: ...

@typing.type_check_only
class AclHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Acl: ...

@typing.type_check_only
class AclRuleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> AclRule: ...

@typing.type_check_only
class CalendarHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Calendar: ...

@typing.type_check_only
class CalendarListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CalendarList: ...

@typing.type_check_only
class CalendarListEntryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> CalendarListEntry: ...

@typing.type_check_only
class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Channel: ...

@typing.type_check_only
class ColorsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Colors: ...

@typing.type_check_only
class EventHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Event: ...

@typing.type_check_only
class EventsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Events: ...

@typing.type_check_only
class FreeBusyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> FreeBusyResponse: ...

@typing.type_check_only
class SettingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Setting: ...

@typing.type_check_only
class SettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = ...,
        num_retries: int = ...,
    ) -> Settings: ...

import collections.abc
import typing

import httplib2
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http

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
            body: AclRule,
            sendNotifications: bool | None = ...,
            **kwargs: typing.Any,
        ) -> AclRuleHttpRequest: ...
        def list(
            self,
            *,
            calendarId: str,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            showDeleted: bool | None = ...,
            syncToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> AclHttpRequest: ...
        def list_next(
            self, previous_request: AclHttpRequest, previous_response: Acl
        ) -> AclHttpRequest | None: ...
        def patch(
            self,
            *,
            calendarId: str,
            ruleId: str,
            body: AclRule,
            sendNotifications: bool | None = ...,
            **kwargs: typing.Any,
        ) -> AclRuleHttpRequest: ...
        def update(
            self,
            *,
            calendarId: str,
            ruleId: str,
            body: AclRule,
            sendNotifications: bool | None = ...,
            **kwargs: typing.Any,
        ) -> AclRuleHttpRequest: ...
        def watch(
            self,
            *,
            calendarId: str,
            body: Channel,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            showDeleted: bool | None = ...,
            syncToken: str | None = ...,
            **kwargs: typing.Any,
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
            body: CalendarListEntry,
            colorRgbFormat: bool | None = ...,
            **kwargs: typing.Any,
        ) -> CalendarListEntryHttpRequest: ...
        def list(
            self,
            *,
            maxResults: int | None = ...,
            minAccessRole: typing_extensions.Literal[
                "freeBusyReader",
                "owner",
                "reader",
                "writer",
                "writerWithoutPrivateAccess",
            ]
            | None = ...,
            pageToken: str | None = ...,
            showDeleted: bool | None = ...,
            showHidden: bool | None = ...,
            syncToken: str | None = ...,
            **kwargs: typing.Any,
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
            body: CalendarListEntry,
            colorRgbFormat: bool | None = ...,
            **kwargs: typing.Any,
        ) -> CalendarListEntryHttpRequest: ...
        def update(
            self,
            *,
            calendarId: str,
            body: CalendarListEntry,
            colorRgbFormat: bool | None = ...,
            **kwargs: typing.Any,
        ) -> CalendarListEntryHttpRequest: ...
        def watch(
            self,
            *,
            body: Channel,
            maxResults: int | None = ...,
            minAccessRole: typing_extensions.Literal[
                "freeBusyReader",
                "owner",
                "reader",
                "writer",
                "writerWithoutPrivateAccess",
            ]
            | None = ...,
            pageToken: str | None = ...,
            showDeleted: bool | None = ...,
            showHidden: bool | None = ...,
            syncToken: str | None = ...,
            **kwargs: typing.Any,
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
            self, *, body: Calendar, **kwargs: typing.Any
        ) -> CalendarHttpRequest: ...
        def patch(
            self, *, calendarId: str, body: Calendar, **kwargs: typing.Any
        ) -> CalendarHttpRequest: ...
        def update(
            self, *, calendarId: str, body: Calendar, **kwargs: typing.Any
        ) -> CalendarHttpRequest: ...

    @typing.type_check_only
    class ChannelsResource(googleapiclient.discovery.Resource):
        def stop(
            self, *, body: Channel, **kwargs: typing.Any
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
            sendNotifications: bool | None = ...,
            sendUpdates: typing_extensions.Literal["all", "externalOnly", "none"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self,
            *,
            calendarId: str,
            eventId: str,
            alwaysIncludeEmail: bool | None = ...,
            maxAttendees: int | None = ...,
            timeZone: str | None = ...,
            **kwargs: typing.Any,
        ) -> EventHttpRequest: ...
        def import_(
            self,
            *,
            calendarId: str,
            body: Event,
            conferenceDataVersion: int | None = ...,
            supportsAttachments: bool | None = ...,
            **kwargs: typing.Any,
        ) -> EventHttpRequest: ...
        def insert(
            self,
            *,
            calendarId: str,
            body: Event,
            conferenceDataVersion: int | None = ...,
            maxAttendees: int | None = ...,
            sendNotifications: bool | None = ...,
            sendUpdates: typing_extensions.Literal["all", "externalOnly", "none"]
            | None = ...,
            supportsAttachments: bool | None = ...,
            **kwargs: typing.Any,
        ) -> EventHttpRequest: ...
        def instances(
            self,
            *,
            calendarId: str,
            eventId: str,
            alwaysIncludeEmail: bool | None = ...,
            maxAttendees: int | None = ...,
            maxResults: int | None = ...,
            originalStart: str | None = ...,
            pageToken: str | None = ...,
            showDeleted: bool | None = ...,
            timeMax: str | None = ...,
            timeMin: str | None = ...,
            timeZone: str | None = ...,
            **kwargs: typing.Any,
        ) -> EventsHttpRequest: ...
        def instances_next(
            self, previous_request: EventsHttpRequest, previous_response: Events
        ) -> EventsHttpRequest | None: ...
        def list(
            self,
            *,
            calendarId: str,
            alwaysIncludeEmail: bool | None = ...,
            eventTypes: typing_extensions.Literal[
                "birthday",
                "default",
                "focusTime",
                "fromGmail",
                "outOfOffice",
                "workingLocation",
            ]
            | _list[
                typing_extensions.Literal[
                    "birthday",
                    "default",
                    "focusTime",
                    "fromGmail",
                    "outOfOffice",
                    "workingLocation",
                ]
            ]
            | None = ...,
            iCalUID: str | None = ...,
            maxAttendees: int | None = ...,
            maxResults: int | None = ...,
            orderBy: typing_extensions.Literal["startTime", "updated"] | None = ...,
            pageToken: str | None = ...,
            privateExtendedProperty: str | _list[str] | None = ...,
            q: str | None = ...,
            sharedExtendedProperty: str | _list[str] | None = ...,
            showDeleted: bool | None = ...,
            showHiddenInvitations: bool | None = ...,
            singleEvents: bool | None = ...,
            syncToken: str | None = ...,
            timeMax: str | None = ...,
            timeMin: str | None = ...,
            timeZone: str | None = ...,
            updatedMin: str | None = ...,
            **kwargs: typing.Any,
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
            sendNotifications: bool | None = ...,
            sendUpdates: typing_extensions.Literal["all", "externalOnly", "none"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> EventHttpRequest: ...
        def patch(
            self,
            *,
            calendarId: str,
            eventId: str,
            body: Event,
            alwaysIncludeEmail: bool | None = ...,
            conferenceDataVersion: int | None = ...,
            maxAttendees: int | None = ...,
            sendNotifications: bool | None = ...,
            sendUpdates: typing_extensions.Literal["all", "externalOnly", "none"]
            | None = ...,
            supportsAttachments: bool | None = ...,
            **kwargs: typing.Any,
        ) -> EventHttpRequest: ...
        def quickAdd(
            self,
            *,
            calendarId: str,
            text: str,
            sendNotifications: bool | None = ...,
            sendUpdates: typing_extensions.Literal["all", "externalOnly", "none"]
            | None = ...,
            **kwargs: typing.Any,
        ) -> EventHttpRequest: ...
        def update(
            self,
            *,
            calendarId: str,
            eventId: str,
            body: Event,
            alwaysIncludeEmail: bool | None = ...,
            conferenceDataVersion: int | None = ...,
            maxAttendees: int | None = ...,
            sendNotifications: bool | None = ...,
            sendUpdates: typing_extensions.Literal["all", "externalOnly", "none"]
            | None = ...,
            supportsAttachments: bool | None = ...,
            **kwargs: typing.Any,
        ) -> EventHttpRequest: ...
        def watch(
            self,
            *,
            calendarId: str,
            body: Channel,
            alwaysIncludeEmail: bool | None = ...,
            eventTypes: typing_extensions.Literal[
                "birthday",
                "default",
                "focusTime",
                "fromGmail",
                "outOfOffice",
                "workingLocation",
            ]
            | _list[
                typing_extensions.Literal[
                    "birthday",
                    "default",
                    "focusTime",
                    "fromGmail",
                    "outOfOffice",
                    "workingLocation",
                ]
            ]
            | None = ...,
            iCalUID: str | None = ...,
            maxAttendees: int | None = ...,
            maxResults: int | None = ...,
            orderBy: typing_extensions.Literal["startTime", "updated"] | None = ...,
            pageToken: str | None = ...,
            privateExtendedProperty: str | _list[str] | None = ...,
            q: str | None = ...,
            sharedExtendedProperty: str | _list[str] | None = ...,
            showDeleted: bool | None = ...,
            showHiddenInvitations: bool | None = ...,
            singleEvents: bool | None = ...,
            syncToken: str | None = ...,
            timeMax: str | None = ...,
            timeMin: str | None = ...,
            timeZone: str | None = ...,
            updatedMin: str | None = ...,
            **kwargs: typing.Any,
        ) -> ChannelHttpRequest: ...

    @typing.type_check_only
    class FreebusyResource(googleapiclient.discovery.Resource):
        def query(
            self, *, body: FreeBusyRequest, **kwargs: typing.Any
        ) -> FreeBusyResponseHttpRequest: ...

    @typing.type_check_only
    class SettingsResource(googleapiclient.discovery.Resource):
        def get(self, *, setting: str, **kwargs: typing.Any) -> SettingHttpRequest: ...
        def list(
            self,
            *,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            syncToken: str | None = ...,
            **kwargs: typing.Any,
        ) -> SettingsHttpRequest: ...
        def list_next(
            self, previous_request: SettingsHttpRequest, previous_response: Settings
        ) -> SettingsHttpRequest | None: ...
        def watch(
            self,
            *,
            body: Channel,
            maxResults: int | None = ...,
            pageToken: str | None = ...,
            syncToken: str | None = ...,
            **kwargs: typing.Any,
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
        | None = None,
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
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Acl: ...

@typing.type_check_only
class AclRuleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> AclRule: ...

@typing.type_check_only
class CalendarHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Calendar: ...

@typing.type_check_only
class CalendarListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CalendarList: ...

@typing.type_check_only
class CalendarListEntryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> CalendarListEntry: ...

@typing.type_check_only
class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Channel: ...

@typing.type_check_only
class ColorsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Colors: ...

@typing.type_check_only
class EventHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Event: ...

@typing.type_check_only
class EventsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Events: ...

@typing.type_check_only
class FreeBusyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> FreeBusyResponse: ...

@typing.type_check_only
class SettingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Setting: ...

@typing.type_check_only
class SettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: httplib2.Http | googleapiclient.http.HttpMock | None = None,
        num_retries: int = 0,
    ) -> Settings: ...

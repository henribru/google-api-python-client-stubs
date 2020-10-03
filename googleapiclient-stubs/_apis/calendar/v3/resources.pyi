import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

class CalendarResource(googleapiclient.discovery.Resource):
    class FreebusyResource(googleapiclient.discovery.Resource):
        def query(
            self, *, body: FreeBusyRequest = ..., **kwargs: typing.Any
        ) -> FreeBusyResponseHttpRequest: ...
    class AclResource(googleapiclient.discovery.Resource):
        def watch(
            self,
            *,
            calendarId: str,
            body: Channel = ...,
            showDeleted: bool = ...,
            pageToken: str = ...,
            maxResults: int = ...,
            syncToken: str = ...,
            **kwargs: typing.Any
        ) -> ChannelHttpRequest: ...
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
            syncToken: str = ...,
            showDeleted: bool = ...,
            **kwargs: typing.Any
        ) -> AclHttpRequest: ...
        def update(
            self,
            *,
            calendarId: str,
            ruleId: str,
            body: AclRule = ...,
            sendNotifications: bool = ...,
            **kwargs: typing.Any
        ) -> AclRuleHttpRequest: ...
        def patch(
            self,
            *,
            calendarId: str,
            ruleId: str,
            body: AclRule = ...,
            sendNotifications: bool = ...,
            **kwargs: typing.Any
        ) -> AclRuleHttpRequest: ...
    class SettingsResource(googleapiclient.discovery.Resource):
        def watch(
            self,
            *,
            body: Channel = ...,
            syncToken: str = ...,
            maxResults: int = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ChannelHttpRequest: ...
        def get(self, *, setting: str, **kwargs: typing.Any) -> SettingHttpRequest: ...
        def list(
            self,
            *,
            pageToken: str = ...,
            maxResults: int = ...,
            syncToken: str = ...,
            **kwargs: typing.Any
        ) -> SettingsHttpRequest: ...
    class ChannelsResource(googleapiclient.discovery.Resource):
        def stop(
            self, *, body: Channel = ..., **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
    class CalendarListResource(googleapiclient.discovery.Resource):
        def watch(
            self,
            *,
            body: Channel = ...,
            maxResults: int = ...,
            syncToken: str = ...,
            showDeleted: bool = ...,
            minAccessRole: typing_extensions.Literal[
                "freeBusyReader", "owner", "reader", "writer"
            ] = ...,
            showHidden: bool = ...,
            pageToken: str = ...,
            **kwargs: typing.Any
        ) -> ChannelHttpRequest: ...
        def insert(
            self,
            *,
            body: CalendarListEntry = ...,
            colorRgbFormat: bool = ...,
            **kwargs: typing.Any
        ) -> CalendarListEntryHttpRequest: ...
        def delete(
            self, *, calendarId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def list(
            self,
            *,
            maxResults: int = ...,
            syncToken: str = ...,
            showDeleted: bool = ...,
            pageToken: str = ...,
            minAccessRole: typing_extensions.Literal[
                "freeBusyReader", "owner", "reader", "writer"
            ] = ...,
            showHidden: bool = ...,
            **kwargs: typing.Any
        ) -> CalendarListHttpRequest: ...
        def update(
            self,
            *,
            calendarId: str,
            body: CalendarListEntry = ...,
            colorRgbFormat: bool = ...,
            **kwargs: typing.Any
        ) -> CalendarListEntryHttpRequest: ...
        def patch(
            self,
            *,
            calendarId: str,
            body: CalendarListEntry = ...,
            colorRgbFormat: bool = ...,
            **kwargs: typing.Any
        ) -> CalendarListEntryHttpRequest: ...
        def get(
            self, *, calendarId: str, **kwargs: typing.Any
        ) -> CalendarListEntryHttpRequest: ...
    class CalendarsResource(googleapiclient.discovery.Resource):
        def insert(
            self, *, body: Calendar = ..., **kwargs: typing.Any
        ) -> CalendarHttpRequest: ...
        def update(
            self, *, calendarId: str, body: Calendar = ..., **kwargs: typing.Any
        ) -> CalendarHttpRequest: ...
        def clear(
            self, *, calendarId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def patch(
            self, *, calendarId: str, body: Calendar = ..., **kwargs: typing.Any
        ) -> CalendarHttpRequest: ...
        def delete(
            self, *, calendarId: str, **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def get(
            self, *, calendarId: str, **kwargs: typing.Any
        ) -> CalendarHttpRequest: ...
    class ColorsResource(googleapiclient.discovery.Resource):
        def get(self, **kwargs: typing.Any) -> ColorsHttpRequest: ...
    class EventsResource(googleapiclient.discovery.Resource):
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
            sendUpdates: typing_extensions.Literal["all", "externalOnly", "none"] = ...,
            conferenceDataVersion: int = ...,
            supportsAttachments: bool = ...,
            sendNotifications: bool = ...,
            maxAttendees: int = ...,
            alwaysIncludeEmail: bool = ...,
            **kwargs: typing.Any
        ) -> EventHttpRequest: ...
        def insert(
            self,
            *,
            calendarId: str,
            body: Event = ...,
            supportsAttachments: bool = ...,
            sendNotifications: bool = ...,
            conferenceDataVersion: int = ...,
            maxAttendees: int = ...,
            sendUpdates: typing_extensions.Literal["all", "externalOnly", "none"] = ...,
            **kwargs: typing.Any
        ) -> EventHttpRequest: ...
        def instances(
            self,
            *,
            calendarId: str,
            eventId: str,
            showDeleted: bool = ...,
            originalStart: str = ...,
            maxResults: int = ...,
            timeMax: str = ...,
            timeZone: str = ...,
            pageToken: str = ...,
            maxAttendees: int = ...,
            timeMin: str = ...,
            alwaysIncludeEmail: bool = ...,
            **kwargs: typing.Any
        ) -> EventsHttpRequest: ...
        def delete(
            self,
            *,
            calendarId: str,
            eventId: str,
            sendUpdates: typing_extensions.Literal["all", "externalOnly", "none"] = ...,
            sendNotifications: bool = ...,
            **kwargs: typing.Any
        ) -> googleapiclient.http.HttpRequest: ...
        def import_(
            self,
            *,
            calendarId: str,
            body: Event = ...,
            conferenceDataVersion: int = ...,
            supportsAttachments: bool = ...,
            **kwargs: typing.Any
        ) -> EventHttpRequest: ...
        def update(
            self,
            *,
            calendarId: str,
            eventId: str,
            body: Event = ...,
            sendNotifications: bool = ...,
            supportsAttachments: bool = ...,
            alwaysIncludeEmail: bool = ...,
            maxAttendees: int = ...,
            sendUpdates: typing_extensions.Literal["all", "externalOnly", "none"] = ...,
            conferenceDataVersion: int = ...,
            **kwargs: typing.Any
        ) -> EventHttpRequest: ...
        def list(
            self,
            *,
            calendarId: str,
            maxAttendees: int = ...,
            timeZone: str = ...,
            timeMin: str = ...,
            syncToken: str = ...,
            showDeleted: bool = ...,
            showHiddenInvitations: bool = ...,
            iCalUID: str = ...,
            updatedMin: str = ...,
            timeMax: str = ...,
            maxResults: int = ...,
            q: str = ...,
            privateExtendedProperty: typing.Union[str, typing.List[str]] = ...,
            pageToken: str = ...,
            singleEvents: bool = ...,
            sharedExtendedProperty: typing.Union[str, typing.List[str]] = ...,
            alwaysIncludeEmail: bool = ...,
            orderBy: typing_extensions.Literal["startTime", "updated"] = ...,
            **kwargs: typing.Any
        ) -> EventsHttpRequest: ...
        def quickAdd(
            self,
            *,
            calendarId: str,
            text: str,
            sendNotifications: bool = ...,
            sendUpdates: typing_extensions.Literal["all", "externalOnly", "none"] = ...,
            **kwargs: typing.Any
        ) -> EventHttpRequest: ...
        def get(
            self,
            *,
            calendarId: str,
            eventId: str,
            maxAttendees: int = ...,
            alwaysIncludeEmail: bool = ...,
            timeZone: str = ...,
            **kwargs: typing.Any
        ) -> EventHttpRequest: ...
        def watch(
            self,
            *,
            calendarId: str,
            body: Channel = ...,
            maxResults: int = ...,
            syncToken: str = ...,
            alwaysIncludeEmail: bool = ...,
            timeZone: str = ...,
            timeMin: str = ...,
            privateExtendedProperty: typing.Union[str, typing.List[str]] = ...,
            orderBy: typing_extensions.Literal["startTime", "updated"] = ...,
            sharedExtendedProperty: typing.Union[str, typing.List[str]] = ...,
            pageToken: str = ...,
            singleEvents: bool = ...,
            showDeleted: bool = ...,
            iCalUID: str = ...,
            timeMax: str = ...,
            updatedMin: str = ...,
            showHiddenInvitations: bool = ...,
            q: str = ...,
            maxAttendees: int = ...,
            **kwargs: typing.Any
        ) -> ChannelHttpRequest: ...
    def freebusy(self) -> FreebusyResource: ...
    def acl(self) -> AclResource: ...
    def settings(self) -> SettingsResource: ...
    def channels(self) -> ChannelsResource: ...
    def calendarList(self) -> CalendarListResource: ...
    def calendars(self) -> CalendarsResource: ...
    def colors(self) -> ColorsResource: ...
    def events(self) -> EventsResource: ...

class CalendarListHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CalendarList: ...

class ColorsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Colors: ...

class FreeBusyResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> FreeBusyResponse: ...

class EventHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Event: ...

class ChannelHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Channel: ...

class SettingsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Settings: ...

class AclRuleHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> AclRule: ...

class SettingHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Setting: ...

class AclHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Acl: ...

class EventsHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Events: ...

class CalendarHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> Calendar: ...

class CalendarListEntryHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self, http: typing.Optional[httplib2.Http] = ..., num_retries: int = ...
    ) -> CalendarListEntry: ...

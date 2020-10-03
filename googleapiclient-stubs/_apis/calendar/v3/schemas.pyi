import typing

import typing_extensions

class Setting(typing_extensions.TypedDict, total=False):
    etag: str
    kind: str
    id: str
    value: str

class EntryPoint(typing_extensions.TypedDict, total=False):
    meetingCode: str
    entryPointType: str
    label: str
    regionCode: str
    uri: str
    passcode: str
    accessCode: str
    entryPointFeatures: typing.List[str]
    pin: str
    password: str

class ConferenceRequestStatus(typing_extensions.TypedDict, total=False):
    statusCode: str

class FreeBusyResponse(typing_extensions.TypedDict, total=False):
    calendars: typing.Dict[str, typing.Any]
    kind: str
    groups: typing.Dict[str, typing.Any]
    timeMax: str
    timeMin: str

class FreeBusyRequestItem(typing_extensions.TypedDict, total=False):
    id: str

class EventReminder(typing_extensions.TypedDict, total=False):
    minutes: int
    method: str

class ConferenceSolutionKey(typing_extensions.TypedDict, total=False):
    type: str

class CalendarListEntry(typing_extensions.TypedDict, total=False):
    id: str
    accessRole: str
    foregroundColor: str
    conferenceProperties: ConferenceProperties
    backgroundColor: str
    summaryOverride: str
    hidden: bool
    summary: str
    colorId: str
    primary: bool
    selected: bool
    location: str
    deleted: bool
    timeZone: str
    notificationSettings: typing.Dict[str, typing.Any]
    description: str
    kind: str
    defaultReminders: typing.List[EventReminder]
    etag: str

class ConferenceParameters(typing_extensions.TypedDict, total=False):
    addOnParameters: ConferenceParametersAddOnParameters

class EventAttendee(typing_extensions.TypedDict, total=False):
    self: bool
    resource: bool
    displayName: str
    additionalGuests: int
    responseStatus: str
    comment: str
    email: str
    id: str
    organizer: bool
    optional: bool

class ConferenceParametersAddOnParameters(typing_extensions.TypedDict, total=False):
    parameters: typing.Dict[str, typing.Any]

class EventAttachment(typing_extensions.TypedDict, total=False):
    mimeType: str
    fileId: str
    fileUrl: str
    iconLink: str
    title: str

class EventDateTime(typing_extensions.TypedDict, total=False):
    dateTime: str
    timeZone: str
    date: str

class CreateConferenceRequest(typing_extensions.TypedDict, total=False):
    status: ConferenceRequestStatus
    requestId: str
    conferenceSolutionKey: ConferenceSolutionKey

class Channel(typing_extensions.TypedDict, total=False):
    type: str
    expiration: str
    payload: bool
    params: typing.Dict[str, typing.Any]
    token: str
    address: str
    id: str
    resourceUri: str
    kind: str
    resourceId: str

class CalendarNotification(typing_extensions.TypedDict, total=False):
    type: str
    method: str

class ConferenceData(typing_extensions.TypedDict, total=False):
    createRequest: CreateConferenceRequest
    parameters: ConferenceParameters
    entryPoints: typing.List[EntryPoint]
    conferenceSolution: ConferenceSolution
    notes: str
    signature: str
    conferenceId: str

class TimePeriod(typing_extensions.TypedDict, total=False):
    end: str
    start: str

class AclRule(typing_extensions.TypedDict, total=False):
    kind: str
    scope: typing.Dict[str, typing.Any]
    etag: str
    role: str
    id: str

class FreeBusyRequest(typing_extensions.TypedDict, total=False):
    timeMin: str
    timeMax: str
    timeZone: str
    calendarExpansionMax: int
    items: typing.List[FreeBusyRequestItem]
    groupExpansionMax: int

class ConferenceSolution(typing_extensions.TypedDict, total=False):
    iconUri: str
    name: str
    key: ConferenceSolutionKey

class Events(typing_extensions.TypedDict, total=False):
    description: str
    accessRole: str
    summary: str
    items: typing.List[Event]
    timeZone: str
    updated: str
    etag: str
    nextPageToken: str
    defaultReminders: typing.List[EventReminder]
    kind: str
    nextSyncToken: str

class ColorDefinition(typing_extensions.TypedDict, total=False):
    background: str
    foreground: str

class FreeBusyGroup(typing_extensions.TypedDict, total=False):
    calendars: typing.List[str]
    errors: typing.List[Error]

class FreeBusyCalendar(typing_extensions.TypedDict, total=False):
    errors: typing.List[Error]
    busy: typing.List[TimePeriod]

class ConferenceProperties(typing_extensions.TypedDict, total=False):
    allowedConferenceSolutionTypes: typing.List[str]

class CalendarList(typing_extensions.TypedDict, total=False):
    nextSyncToken: str
    kind: str
    items: typing.List[CalendarListEntry]
    etag: str
    nextPageToken: str

class Calendar(typing_extensions.TypedDict, total=False):
    id: str
    conferenceProperties: ConferenceProperties
    location: str
    description: str
    summary: str
    kind: str
    etag: str
    timeZone: str

class Acl(typing_extensions.TypedDict, total=False):
    etag: str
    nextSyncToken: str
    kind: str
    items: typing.List[AclRule]
    nextPageToken: str

class Settings(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    kind: str
    nextSyncToken: str
    etag: str
    items: typing.List[Setting]

class Colors(typing_extensions.TypedDict, total=False):
    calendar: typing.Dict[str, typing.Any]
    updated: str
    event: typing.Dict[str, typing.Any]
    kind: str

class Error(typing_extensions.TypedDict, total=False):
    reason: str
    domain: str

class Event(typing_extensions.TypedDict, total=False):
    iCalUID: str
    reminders: typing.Dict[str, typing.Any]
    description: str
    updated: str
    guestsCanModify: bool
    gadget: typing.Dict[str, typing.Any]
    originalStartTime: EventDateTime
    sequence: int
    status: str
    etag: str
    id: str
    attachments: typing.List[EventAttachment]
    visibility: str
    htmlLink: str
    attendeesOmitted: bool
    location: str
    guestsCanInviteOthers: bool
    created: str
    start: EventDateTime
    conferenceData: ConferenceData
    transparency: str
    anyoneCanAddSelf: bool
    creator: typing.Dict[str, typing.Any]
    source: typing.Dict[str, typing.Any]
    organizer: typing.Dict[str, typing.Any]
    hangoutLink: str
    end: EventDateTime
    recurrence: typing.List[str]
    attendees: typing.List[EventAttendee]
    endTimeUnspecified: bool
    colorId: str
    kind: str
    summary: str
    guestsCanSeeOtherGuests: bool
    recurringEventId: str
    extendedProperties: typing.Dict[str, typing.Any]
    privateCopy: bool
    locked: bool

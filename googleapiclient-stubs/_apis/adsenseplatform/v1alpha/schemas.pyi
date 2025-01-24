import typing

import typing_extensions

_list = list

@typing.type_check_only
class Account(typing_extensions.TypedDict, total=False):
    createTime: str
    creationRequestId: str
    displayName: str
    name: str
    regionCode: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED", "UNCHECKED", "APPROVED", "DISAPPROVED"
    ]
    timeZone: TimeZone

@typing.type_check_only
class Address(typing_extensions.TypedDict, total=False):
    address1: str
    address2: str
    city: str
    company: str
    contact: str
    fax: str
    phone: str
    regionCode: str
    state: str
    zip: str

@typing.type_check_only
class CloseAccountRequest(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class CloseAccountResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Decimal(typing_extensions.TypedDict, total=False):
    value: str

@typing.type_check_only
class Empty(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Event(typing_extensions.TypedDict, total=False):
    eventInfo: EventInfo
    eventTime: str
    eventType: typing_extensions.Literal[
        "EVENT_TYPE_UNSPECIFIED", "LOG_IN_VIA_PLATFORM", "SIGN_UP_VIA_PLATFORM"
    ]

@typing.type_check_only
class EventInfo(typing_extensions.TypedDict, total=False):
    billingAddress: Address
    email: str

@typing.type_check_only
class ListAccountsResponse(typing_extensions.TypedDict, total=False):
    accounts: _list[Account]
    nextPageToken: str

@typing.type_check_only
class ListPlatformChildSitesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    platformChildSites: _list[PlatformChildSite]

@typing.type_check_only
class ListPlatformGroupsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    platformGroups: _list[PlatformGroup]

@typing.type_check_only
class ListPlatformsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    platforms: _list[Platform]

@typing.type_check_only
class ListSitesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    sites: _list[Site]

@typing.type_check_only
class LookupAccountResponse(typing_extensions.TypedDict, total=False):
    name: str

@typing.type_check_only
class Platform(typing_extensions.TypedDict, total=False):
    defaultPlatformGroup: str
    description: str
    name: str

@typing.type_check_only
class PlatformChildSite(typing_extensions.TypedDict, total=False):
    domain: str
    name: str
    platformGroup: str

@typing.type_check_only
class PlatformGroup(typing_extensions.TypedDict, total=False):
    description: str
    name: str
    revshareMillipercent: Decimal

@typing.type_check_only
class RequestSiteReviewResponse(typing_extensions.TypedDict, total=False): ...

@typing.type_check_only
class Site(typing_extensions.TypedDict, total=False):
    domain: str
    name: str
    state: typing_extensions.Literal[
        "STATE_UNSPECIFIED",
        "REQUIRES_REVIEW",
        "GETTING_READY",
        "READY",
        "NEEDS_ATTENTION",
    ]

@typing.type_check_only
class TimeZone(typing_extensions.TypedDict, total=False):
    id: str
    version: str

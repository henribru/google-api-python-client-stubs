import typing

_list = list

@typing.type_check_only
class Account(typing.TypedDict, total=False):
    createTime: str
    creationRequestId: str
    displayName: str
    name: str
    regionCode: str
    state: typing.Literal["STATE_UNSPECIFIED", "UNCHECKED", "APPROVED", "DISAPPROVED"]
    timeZone: TimeZone

@typing.type_check_only
class Address(typing.TypedDict, total=False):
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
class CloseAccountRequest(typing.TypedDict, total=False): ...

@typing.type_check_only
class CloseAccountResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class Decimal(typing.TypedDict, total=False):
    value: str

@typing.type_check_only
class Empty(typing.TypedDict, total=False): ...

@typing.type_check_only
class Event(typing.TypedDict, total=False):
    eventInfo: EventInfo
    eventTime: str
    eventType: typing.Literal[
        "EVENT_TYPE_UNSPECIFIED", "LOG_IN_VIA_PLATFORM", "SIGN_UP_VIA_PLATFORM"
    ]

@typing.type_check_only
class EventInfo(typing.TypedDict, total=False):
    billingAddress: Address
    email: str

@typing.type_check_only
class ListAccountsResponse(typing.TypedDict, total=False):
    accounts: _list[Account]
    nextPageToken: str

@typing.type_check_only
class ListPlatformChildSitesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    platformChildSites: _list[PlatformChildSite]

@typing.type_check_only
class ListPlatformGroupsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    platformGroups: _list[PlatformGroup]

@typing.type_check_only
class ListPlatformsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    platforms: _list[Platform]

@typing.type_check_only
class ListSitesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    sites: _list[Site]

@typing.type_check_only
class LookupAccountResponse(typing.TypedDict, total=False):
    name: str

@typing.type_check_only
class Platform(typing.TypedDict, total=False):
    defaultPlatformGroup: str
    description: str
    name: str

@typing.type_check_only
class PlatformChildSite(typing.TypedDict, total=False):
    domain: str
    name: str
    platformGroup: str

@typing.type_check_only
class PlatformGroup(typing.TypedDict, total=False):
    description: str
    name: str
    revshareMillipercent: Decimal

@typing.type_check_only
class RequestSiteReviewResponse(typing.TypedDict, total=False): ...

@typing.type_check_only
class Site(typing.TypedDict, total=False):
    domain: str
    name: str
    state: typing.Literal[
        "STATE_UNSPECIFIED",
        "REQUIRES_REVIEW",
        "GETTING_READY",
        "READY",
        "NEEDS_ATTENTION",
    ]

@typing.type_check_only
class TimeZone(typing.TypedDict, total=False):
    id: str
    version: str

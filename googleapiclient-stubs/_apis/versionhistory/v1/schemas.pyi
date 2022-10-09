import typing

import typing_extensions

_list = list

@typing.type_check_only
class Channel(typing_extensions.TypedDict, total=False):
    channelType: typing_extensions.Literal[
        "CHANNEL_TYPE_UNSPECIFIED",
        "STABLE",
        "BETA",
        "DEV",
        "CANARY",
        "CANARY_ASAN",
        "ALL",
        "EXTENDED",
    ]
    name: str

@typing.type_check_only
class Interval(typing_extensions.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class ListChannelsResponse(typing_extensions.TypedDict, total=False):
    channels: _list[Channel]
    nextPageToken: str

@typing.type_check_only
class ListPlatformsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    platforms: _list[Platform]

@typing.type_check_only
class ListReleasesResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    releases: _list[Release]

@typing.type_check_only
class ListVersionsResponse(typing_extensions.TypedDict, total=False):
    nextPageToken: str
    versions: _list[Version]

@typing.type_check_only
class Platform(typing_extensions.TypedDict, total=False):
    name: str
    platformType: typing_extensions.Literal[
        "PLATFORM_TYPE_UNSPECIFIED",
        "WIN",
        "WIN64",
        "MAC",
        "LINUX",
        "ANDROID",
        "WEBVIEW",
        "IOS",
        "ALL",
        "MAC_ARM64",
        "LACROS",
        "LACROS_ARM32",
        "CHROMEOS",
        "LACROS_ARM64",
    ]

@typing.type_check_only
class Release(typing_extensions.TypedDict, total=False):
    fraction: float
    fractionGroup: str
    name: str
    serving: Interval
    version: str

@typing.type_check_only
class Version(typing_extensions.TypedDict, total=False):
    name: str
    version: str

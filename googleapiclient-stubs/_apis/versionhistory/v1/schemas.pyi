import typing

_list = list

@typing.type_check_only
class Channel(typing.TypedDict, total=False):
    channelType: typing.Literal[
        "CHANNEL_TYPE_UNSPECIFIED",
        "STABLE",
        "BETA",
        "DEV",
        "CANARY",
        "CANARY_ASAN",
        "ALL",
        "EXTENDED",
        "LTS",
        "LTC",
    ]
    name: str

@typing.type_check_only
class Interval(typing.TypedDict, total=False):
    endTime: str
    startTime: str

@typing.type_check_only
class ListChannelsResponse(typing.TypedDict, total=False):
    channels: _list[Channel]
    nextPageToken: str

@typing.type_check_only
class ListPlatformsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    platforms: _list[Platform]

@typing.type_check_only
class ListReleasesResponse(typing.TypedDict, total=False):
    nextPageToken: str
    releases: _list[Release]

@typing.type_check_only
class ListVersionsResponse(typing.TypedDict, total=False):
    nextPageToken: str
    versions: _list[Version]

@typing.type_check_only
class Platform(typing.TypedDict, total=False):
    name: str
    platformType: typing.Literal[
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
        "FUCHSIA",
        "WIN_ARM64",
    ]

@typing.type_check_only
class Release(typing.TypedDict, total=False):
    fraction: float
    fractionGroup: str
    name: str
    pinnable: bool
    rolloutData: _list[RolloutData]
    serving: Interval
    version: str

@typing.type_check_only
class RolloutData(typing.TypedDict, total=False):
    rolloutName: str
    tag: _list[str]

@typing.type_check_only
class Version(typing.TypedDict, total=False):
    name: str
    version: str
